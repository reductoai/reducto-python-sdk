from __future__ import annotations

from pathlib import Path

import pytest

from reducto.lib.sagemaker import _client as client_module
from reducto.lib.sagemaker._session import Boto3Session
from reducto.lib.sagemaker._transport import RuntimeClient

from ._stubs import FakeRuntime

_HIDDEN_VARIABLES = (
    "AWS_REGION",
    "AWS_DEFAULT_REGION",
    "AWS_PROFILE",
    "AWS_DEFAULT_PROFILE",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
    "AWS_ROLE_ARN",
    "AWS_WEB_IDENTITY_TOKEN_FILE",
    "AWS_CONTAINER_CREDENTIALS_RELATIVE_URI",
    "AWS_CONTAINER_CREDENTIALS_FULL_URI",
    "AWS_ENDPOINT_URL",
    "AWS_ENDPOINT_URL_SAGEMAKER_RUNTIME",
    "AWS_IGNORE_CONFIGURED_ENDPOINT_URLS",
    "HTTP_PROXY",
    "https_proxy",
    "http_proxy",
    "no_proxy",
)


@pytest.fixture(autouse=True)
def isolated_aws(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Hides the machine's AWS settings and credentials. Returns the AWS config file, which starts empty."""
    for name in _HIDDEN_VARIABLES:
        monkeypatch.delenv(name, raising=False)
    config = tmp_path / "aws-config"
    config.write_text("")
    monkeypatch.setenv("AWS_CONFIG_FILE", str(config))
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", str(tmp_path / "aws-credentials"))
    monkeypatch.setenv("AWS_EC2_METADATA_DISABLED", "true")
    # A call that misses the loopback server goes to a closed proxy port, never to AWS.
    monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:9")
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    return config


@pytest.fixture
def runtimes(monkeypatch: pytest.MonkeyPatch) -> list[RuntimeClient]:
    """The real botocore clients that the SageMaker clients create, in order."""
    created: list[RuntimeClient] = []
    real_factory = client_module.runtime_client

    def factory(session: Boto3Session, *, timeout: float, max_pool_connections: int) -> RuntimeClient:
        runtime = real_factory(session, timeout=timeout, max_pool_connections=max_pool_connections)
        created.append(runtime)
        return runtime

    monkeypatch.setattr(client_module, "runtime_client", factory)
    return created


@pytest.fixture
def fake_runtime(monkeypatch: pytest.MonkeyPatch) -> FakeRuntime:
    """A fake `sagemaker-runtime` client that every SageMaker client made in the test uses."""
    runtime = FakeRuntime()

    def factory(_session: Boto3Session, *, timeout: float, max_pool_connections: int) -> RuntimeClient:  # noqa: ARG001
        return runtime

    monkeypatch.setattr(client_module, "runtime_client", factory)
    return runtime
