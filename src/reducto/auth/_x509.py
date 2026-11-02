"""X.509 workload identity: authenticate with a client certificate over mutual TLS."""

from __future__ import annotations

import os
import ssl
import threading
from typing import Tuple, Iterator, Optional, NamedTuple, AsyncIterator, cast
from pathlib import Path
from typing_extensions import Literal, TypedDict, override

import httpx

from .._constants import DEFAULT_CONNECTION_LIMITS
from .._exceptions import SubjectTokenProviderError
from .._base_client import SyncHttpxClientWrapper, AsyncHttpxClientWrapper

__all__ = ["ClientCertificate", "X509Provider", "x509_workload_identity"]

MTLS_ENVIRONMENTS = {
    "production": "https://mtls.platform.reducto.ai",
    "eu": "https://mtls.eu.platform.reducto.ai",
    "au": "https://mtls.au.platform.reducto.ai",
}


class LoadedCertificate(NamedTuple):
    files: Tuple[bytes, bytes]
    context: ssl.SSLContext


class ClientCertificate:
    """A client certificate chain and private key on disk, loaded into an `ssl.SSLContext`."""

    def __init__(self, cert_chain: str | os.PathLike[str], key: str | os.PathLike[str]) -> None:
        self.cert_chain = cert_chain
        self.key = key
        self._lock = threading.Lock()
        self._current: Optional[LoadedCertificate] = None

    @property
    def context(self) -> ssl.SSLContext:
        """The context that API requests use. Loaded on first use, then replaced only by `use`."""
        with self._lock:
            current = self._current
        if current is None:
            current = self.load()
            self.use(current)
        return current.context

    def load(self) -> LoadedCertificate:
        """Read both files. Returns the current context if they have not changed."""
        try:
            files = (Path(self.cert_chain).read_bytes(), Path(self.key).read_bytes())
        except OSError as e:
            raise SubjectTokenProviderError(f"Failed to read the client certificate: {e}") from e
        with self._lock:
            if self._current is not None and self._current.files == files:
                return self._current
        context = httpx.create_ssl_context()
        try:
            context.load_cert_chain(self.cert_chain, self.key)
        except (OSError, ssl.SSLError) as e:
            raise SubjectTokenProviderError(
                f"Failed to load the client certificate chain {self.cert_chain} with key {self.key}: {e}"
            ) from e
        return LoadedCertificate(files, context)

    def use(self, loaded: LoadedCertificate) -> None:
        """Send later API requests with this certificate. Called once it got an access token, so both match."""
        with self._lock:
            self._current = loaded


class X509Provider(TypedDict):
    token_type: Literal["x509"]

    client_certificate: ClientCertificate
    """Presented on the token exchange and on every API request."""


def x509_workload_identity(cert_chain: str | os.PathLike[str], key: str | os.PathLike[str]) -> X509Provider:
    """Authenticate with a client certificate (X.509 workload identity over mutual TLS).

    Args:
        cert_chain: PEM file with the leaf certificate first, then any intermediates.
        key: PEM file with the unencrypted private key of the leaf certificate.

    Both files are re-read on each token exchange, so rotated certificates are picked up.
    """
    return {"token_type": "x509", "client_certificate": ClientCertificate(cert_chain, key)}


class _SyncPool:
    """An `httpx.Client` for one certificate. Once replaced, it is closed after its last response is closed."""

    def __init__(self, context: ssl.SSLContext) -> None:
        self.context = context
        self.client = httpx.Client(verify=context, limits=DEFAULT_CONNECTION_LIMITS)
        self._lock = threading.Lock()
        self._active = 0
        self._retired = False

    def acquire(self) -> None:
        with self._lock:
            self._active += 1

    def release(self) -> None:
        with self._lock:
            self._active -= 1
            close = self._retired and self._active == 0
        if close:
            self.client.close()

    def retire(self) -> None:
        with self._lock:
            self._retired = True
            close = self._active == 0
        if close:
            self.client.close()


class _ReleasingStream(httpx.SyncByteStream):
    def __init__(self, stream: httpx.SyncByteStream, pool: _SyncPool) -> None:
        self._stream = stream
        self._pool: Optional[_SyncPool] = pool

    @override
    def __iter__(self) -> Iterator[bytes]:
        yield from self._stream

    @override
    def close(self) -> None:
        self._stream.close()
        pool, self._pool = self._pool, None
        if pool is not None:
            pool.release()


class SyncClientCertificateTransport(httpx.BaseTransport):
    """Sends each request through an `httpx.Client` that presents the current client certificate.

    A new client (and connection pool) is used when the certificate changes, so pooled connections
    never present a certificate other than the one the current access token is bound to.
    """

    def __init__(self, certificate: ClientCertificate) -> None:
        self.certificate = certificate
        self._lock = threading.Lock()
        self._pool: Optional[_SyncPool] = None

    @override
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        context = self.certificate.context
        retired: Optional[_SyncPool] = None
        with self._lock:
            if self._pool is None or self._pool.context is not context:
                retired, self._pool = self._pool, _SyncPool(context)
            pool = self._pool
            pool.acquire()
        if retired is not None:
            retired.retire()
        try:
            response = pool.client.send(request, stream=True)
        except BaseException:
            pool.release()
            raise
        response.stream = _ReleasingStream(cast(httpx.SyncByteStream, response.stream), pool)
        return response

    @override
    def close(self) -> None:
        with self._lock:
            pool, self._pool = self._pool, None
        if pool is not None:
            pool.retire()


class _AsyncPool:
    """Async version of `_SyncPool`. Used from one event loop, so it needs no lock."""

    def __init__(self, context: ssl.SSLContext) -> None:
        self.context = context
        self.client = httpx.AsyncClient(verify=context, limits=DEFAULT_CONNECTION_LIMITS)
        self._active = 0
        self._retired = False

    def acquire(self) -> None:
        self._active += 1

    async def release(self) -> None:
        self._active -= 1
        if self._retired and self._active == 0:
            await self.client.aclose()

    async def retire(self) -> None:
        self._retired = True
        if self._active == 0:
            await self.client.aclose()


class _AsyncReleasingStream(httpx.AsyncByteStream):
    def __init__(self, stream: httpx.AsyncByteStream, pool: _AsyncPool) -> None:
        self._stream = stream
        self._pool: Optional[_AsyncPool] = pool

    @override
    async def __aiter__(self) -> AsyncIterator[bytes]:
        async for chunk in self._stream:
            yield chunk

    @override
    async def aclose(self) -> None:
        await self._stream.aclose()
        pool, self._pool = self._pool, None
        if pool is not None:
            await pool.release()


class AsyncClientCertificateTransport(httpx.AsyncBaseTransport):
    """Async version of `SyncClientCertificateTransport`."""

    def __init__(self, certificate: ClientCertificate) -> None:
        self.certificate = certificate
        self._pool: Optional[_AsyncPool] = None

    @override
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        context = self.certificate.context
        retired: Optional[_AsyncPool] = None
        if self._pool is None or self._pool.context is not context:
            retired, self._pool = self._pool, _AsyncPool(context)
        pool = self._pool
        pool.acquire()
        if retired is not None:
            await retired.retire()
        try:
            response = await pool.client.send(request, stream=True)
        except BaseException:
            await pool.release()
            raise
        response.stream = _AsyncReleasingStream(cast(httpx.AsyncByteStream, response.stream), pool)
        return response

    @override
    async def aclose(self) -> None:
        pool, self._pool = self._pool, None
        if pool is not None:
            await pool.retire()


class SyncClientCertificateHttpxClient(SyncHttpxClientWrapper):
    def __init__(self, certificate: ClientCertificate) -> None:
        super().__init__(transport=SyncClientCertificateTransport(certificate))
        self.client_certificate = certificate


class AsyncClientCertificateHttpxClient(AsyncHttpxClientWrapper):
    def __init__(self, certificate: ClientCertificate) -> None:
        super().__init__(transport=AsyncClientCertificateTransport(certificate))
        self.client_certificate = certificate
