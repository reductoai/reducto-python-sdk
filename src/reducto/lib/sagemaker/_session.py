from __future__ import annotations

import os
from typing import TYPE_CHECKING, cast
from typing_extensions import Protocol

from ..._exceptions import ReductoError
from .._page_parse._deps import LazyModule

if TYPE_CHECKING:
    import boto3  # pyright: ignore[reportMissingTypeStubs]
    import botocore.exceptions as botocore_exceptions  # pyright: ignore[reportMissingTypeStubs]
else:
    boto3 = LazyModule("boto3", "boto3", "sagemaker")
    botocore_exceptions = LazyModule("botocore.exceptions", "boto3", "sagemaker")

__all__ = ["Boto3Session", "boto3_session"]


class Boto3Session(Protocol):
    """The typed part of a boto3 session, because boto3 ships no types."""

    @property
    def region_name(self) -> str | None: ...

    def client(self, service_name: str, *, config: object) -> object: ...


def boto3_session(
    *,
    aws_region: str | None,
    aws_profile: str | None,
    aws_access_key: str | None,
    aws_secret_key: str | None,
    aws_session_token: str | None,
) -> tuple[Boto3Session, str]:
    """The session and its region: `aws_region`, else `AWS_REGION` or `AWS_DEFAULT_REGION`, else the profile's region.
    Explicit keys take priority over `aws_profile`, as in boto3. Bad AWS arguments raise ReductoError."""
    if (aws_access_key is None) != (aws_secret_key is None) or (
        aws_session_token is not None and aws_access_key is None
    ):
        raise ReductoError("Pass both `aws_access_key` and `aws_secret_key`, or neither. A session token needs both.")
    try:
        session = cast(
            Boto3Session,
            boto3.Session(
                region_name=aws_region or os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION"),
                profile_name=aws_profile,
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                aws_session_token=aws_session_token,
            ),
        )
    except botocore_exceptions.ProfileNotFound as error:
        raise ReductoError(f"The AWS profile {aws_profile!r} was not found.") from error
    region = session.region_name
    if not region:
        raise ReductoError(
            "No AWS region was found. Pass `aws_region`, set the `AWS_REGION` environment variable, "
            "or set a region in your AWS profile."
        )
    return session, region
