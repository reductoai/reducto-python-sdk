"""
Bulk parsing utilities for processing multiple documents concurrently with automatic result polling.

This module provides helpers for efficiently processing large batches of documents using
the Reducto API with semaphore-based concurrency control and automatic result polling.
"""
from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, List, Union, Callable, Optional, Awaitable
from collections import deque
from dataclasses import dataclass

from reducto import AsyncReducto
from reducto._types import Omit, omit
from reducto.types.shared.parse_response import ParseResponse
from reducto.types.shared_params.enhance import Enhance
from reducto.types.shared_params.settings import Settings
from reducto.types.shared_params.retrieval import Retrieval
from reducto.types.shared_params.formatting import Formatting
from reducto.types.shared_params.spreadsheet import Spreadsheet

logger = logging.getLogger(__name__)

__all__ = ["BulkParseManager", "BulkParseConfig", "JobResult"]


@dataclass
class BulkParseConfig:
    """Configuration for bulk parsing operations."""

    max_concurrent: int = 100
    """Maximum number of concurrent API requests (default: 100)."""

    poll_interval: float = 2.0
    """Interval in seconds between polling attempts for job results (default: 2.0)."""

    max_poll_time: Optional[float] = None
    """Maximum time in seconds to poll for a single job before timing out (default: None for no limit)."""

    enhance: Enhance | Omit = omit
    """Enhancement options for parsing."""

    retrieval: Retrieval | Omit = omit
    """Retrieval options for parsing."""

    formatting: Formatting | Omit = omit
    """Formatting options for parsing."""

    spreadsheet: Spreadsheet | Omit = omit
    """Spreadsheet options for parsing."""

    settings: Settings | Omit = omit
    """Settings for parsing."""


@dataclass
class JobResult:
    """Result of a completed job."""

    job_id: str
    """The job ID."""

    input_url: str
    """The original input URL."""

    status: str
    """Job status: 'Completed', 'Failed', 'Pending', or 'Idle'."""

    result: Optional[Union[ParseResponse, Any]] = None
    """The parse result if completed successfully."""

    error: Optional[str] = None
    """Error message if the job failed."""

    duration: Optional[float] = None
    """Duration of the job in seconds."""


@dataclass
class _PendingJob:
    """Internal representation of a pending job."""

    job_id: str
    input_url: str
    submitted_at: float
    poll_count: int = 0


class BulkParseManager:
    """
    Manager for bulk parsing operations with automatic result polling.

    This class handles submitting multiple documents for parsing, managing concurrency
    with a semaphore, and automatically polling for results in the background.

    Example:
        ```python
        import asyncio
        from reducto import AsyncReducto
        from reducto.lib.bulk import BulkParseManager, BulkParseConfig

        async def on_complete(result):
            print(f"Job {result.job_id} completed with status: {result.status}")

        async def main():
            client = AsyncReducto(api_key="your-api-key")
            config = BulkParseConfig(max_concurrent=50, poll_interval=1.0)

            manager = BulkParseManager(client, config, on_complete=on_complete)

            urls = ["https://example.com/doc1.pdf", "https://example.com/doc2.pdf"]
            await manager.submit_all(urls)

            results = await manager.wait_for_all()
            print(f"Processed {len(results)} documents")

        asyncio.run(main())
        ```
    """

    def __init__(
        self,
        client: AsyncReducto,
        config: Optional[BulkParseConfig] = None,
        on_complete: Optional[Callable[[JobResult], Awaitable[None]]] = None,
    ):
        """
        Initialize the BulkParseManager.

        Args:
            client: An AsyncReducto client instance.
            config: Configuration for bulk parsing operations. If None, uses default config.
            on_complete: Optional async callback function called when each job completes.
                        The callback receives a JobResult object.
        """
        self.client = client
        self.config = config or BulkParseConfig()
        self.on_complete = on_complete

        self._semaphore = asyncio.Semaphore(self.config.max_concurrent)
        self._pending_jobs: deque[_PendingJob] = deque()
        self._completed_jobs: List[JobResult] = []
        self._job_map: Dict[str, str] = {}  # job_id -> input_url
        self._polling_task: Optional[asyncio.Task[None]] = None
        self._shutdown = False
        self._lock = asyncio.Lock()

    async def submit(self, input_url: str) -> str:
        """
        Submit a single document for parsing.

        Args:
            input_url: The URL of the document to parse.

        Returns:
            The job ID for the submitted document.

        Raises:
            Exception: If the submission fails.
        """
        async with self._semaphore:
            response = await self.client.parse.run_job(
                input=input_url,
                enhance=self.config.enhance,
                retrieval=self.config.retrieval,
                formatting=self.config.formatting,
                spreadsheet=self.config.spreadsheet,
                settings=self.config.settings,
            )

            job_id = response.job_id
            logger.info(f"Submitted job {job_id} for {input_url}")

            async with self._lock:
                self._job_map[job_id] = input_url
                self._pending_jobs.append(
                    _PendingJob(
                        job_id=job_id,
                        input_url=input_url,
                        submitted_at=asyncio.get_event_loop().time(),
                    )
                )

                if self._polling_task is None or self._polling_task.done():
                    self._polling_task = asyncio.create_task(self._poll_jobs())

            return job_id

    async def submit_all(self, input_urls: List[str]) -> List[str]:
        """
        Submit multiple documents for parsing concurrently.

        Args:
            input_urls: List of document URLs to parse.

        Returns:
            List of job IDs for the submitted documents.
        """
        tasks = [self.submit(url) for url in input_urls]
        job_ids = await asyncio.gather(*tasks, return_exceptions=True)

        valid_job_ids: List[str] = []
        for i, result in enumerate(job_ids):
            if isinstance(result, Exception):
                logger.error(f"Failed to submit {input_urls[i]}: {result}")
            elif isinstance(result, str):
                valid_job_ids.append(result)

        return valid_job_ids

    async def _poll_jobs(self) -> None:
        """Background task that polls for job results."""
        logger.info("Started polling task")

        while not self._shutdown:
            async with self._lock:
                if not self._pending_jobs:
                    logger.info("No pending jobs, stopping polling task")
                    break

                pending_job = self._pending_jobs.popleft()

            try:
                async with self._semaphore:
                    job_response = await self.client.job.get(pending_job.job_id)

                status = job_response.status
                logger.debug(f"Job {pending_job.job_id} status: {status}")

                if status == "Completed":
                    result = JobResult(
                        job_id=pending_job.job_id,
                        input_url=pending_job.input_url,
                        status=status,
                        result=getattr(job_response, "result", None),
                        duration=getattr(job_response, "duration", None),
                    )

                    async with self._lock:
                        self._completed_jobs.append(result)

                    logger.info(f"Job {pending_job.job_id} completed successfully")

                    if self.on_complete:
                        try:
                            await self.on_complete(result)
                        except Exception as e:
                            logger.error(f"Error in on_complete callback for job {pending_job.job_id}: {e}")

                elif status == "Failed":
                    reason = getattr(job_response, "reason", "Unknown error")
                    result = JobResult(
                        job_id=pending_job.job_id,
                        input_url=pending_job.input_url,
                        status=status,
                        error=reason,
                    )

                    async with self._lock:
                        self._completed_jobs.append(result)

                    logger.warning(f"Job {pending_job.job_id} failed: {reason}")

                    if self.on_complete:
                        try:
                            await self.on_complete(result)
                        except Exception as e:
                            logger.error(f"Error in on_complete callback for job {pending_job.job_id}: {e}")

                else:
                    pending_job.poll_count += 1

                    if self.config.max_poll_time is not None:
                        elapsed = asyncio.get_event_loop().time() - pending_job.submitted_at
                        if elapsed > self.config.max_poll_time:
                            result = JobResult(
                                job_id=pending_job.job_id,
                                input_url=pending_job.input_url,
                                status="Failed",
                                error=f"Polling timeout after {elapsed:.1f} seconds",
                            )

                            async with self._lock:
                                self._completed_jobs.append(result)

                            logger.warning(f"Job {pending_job.job_id} timed out after {elapsed:.1f} seconds")

                            if self.on_complete:
                                try:
                                    await self.on_complete(result)
                                except Exception as e:
                                    logger.error(f"Error in on_complete callback for job {pending_job.job_id}: {e}")

                            continue

                    async with self._lock:
                        self._pending_jobs.append(pending_job)

            except Exception as e:
                logger.error(f"Error polling job {pending_job.job_id}: {e}")
                async with self._lock:
                    self._pending_jobs.append(pending_job)

            await asyncio.sleep(self.config.poll_interval)

        logger.info("Polling task finished")

    async def wait_for_all(self) -> List[JobResult]:
        """
        Wait for all submitted jobs to complete.

        Returns:
            List of JobResult objects for all completed jobs.
        """
        if self._polling_task and not self._polling_task.done():
            await self._polling_task

        return self._completed_jobs.copy()

    async def get_completed(self) -> List[JobResult]:
        """
        Get all completed jobs without waiting.

        Returns:
            List of JobResult objects for jobs that have completed so far.
        """
        async with self._lock:
            return self._completed_jobs.copy()

    async def get_pending_count(self) -> int:
        """
        Get the number of jobs still pending.

        Returns:
            Number of jobs still being polled.
        """
        async with self._lock:
            return len(self._pending_jobs)

    async def shutdown(self) -> None:
        """
        Shutdown the manager and stop polling.

        This will stop the polling task but will not cancel any in-flight API requests.
        """
        self._shutdown = True
        if self._polling_task and not self._polling_task.done():
            await self._polling_task


async def bulk_parse(
    client: AsyncReducto,
    input_urls: List[str],
    config: Optional[BulkParseConfig] = None,
    on_complete: Optional[Callable[[JobResult], Awaitable[None]]] = None,
) -> List[JobResult]:
    """
    Convenience function to parse multiple documents and wait for all results.

    This is a simpler interface for one-shot bulk parsing operations.

    Args:
        client: An AsyncReducto client instance.
        input_urls: List of document URLs to parse.
        config: Configuration for bulk parsing operations. If None, uses default config.
        on_complete: Optional async callback function called when each job completes.

    Returns:
        List of JobResult objects for all completed jobs.

    Example:
        ```python
        import asyncio
        from reducto import AsyncReducto
        from reducto.lib.bulk import bulk_parse, BulkParseConfig

        async def main():
            client = AsyncReducto(api_key="your-api-key")
            urls = ["https://example.com/doc1.pdf", "https://example.com/doc2.pdf"]

            results = await bulk_parse(client, urls, config=BulkParseConfig(max_concurrent=50))

            for result in results:
                if result.status == "Completed":
                    print(f"Successfully parsed {result.input_url}")
                else:
                    print(f"Failed to parse {result.input_url}: {result.error}")

        asyncio.run(main())
        ```
    """
    manager = BulkParseManager(client, config, on_complete)
    await manager.submit_all(input_urls)
    return await manager.wait_for_all()
