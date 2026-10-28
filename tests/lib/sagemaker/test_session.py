from __future__ import annotations

import sys
from pathlib import Path

import pytest

from reducto import ReductoError, ReductoSageMaker
from reducto.lib.sagemaker._transport import RuntimeClient

from ._stubs import ENDPOINT, CREDENTIALS, LocalEndpoint, serve, runtime_meta
from .._page_parse._helpers import make_pdf, blocks_answer


def _client(aws_region: str | None = None, aws_profile: str | None = None) -> ReductoSageMaker:
    return ReductoSageMaker(endpoint_name=ENDPOINT, aws_region=aws_region, aws_profile=aws_profile, **CREDENTIALS)


@pytest.mark.parametrize(
    ("argument", "environment", "expected"),
    [
        ("ap-south-1", {"AWS_REGION": "eu-west-1", "AWS_DEFAULT_REGION": "us-west-2"}, "ap-south-1"),
        (None, {"AWS_REGION": "eu-west-1", "AWS_DEFAULT_REGION": "us-west-2"}, "eu-west-1"),
        (None, {"AWS_DEFAULT_REGION": "us-west-2"}, "us-west-2"),
        (None, {}, "ca-central-1"),
    ],
    ids=["argument", "AWS_REGION", "AWS_DEFAULT_REGION", "profile"],
)
def test_region_comes_from_the_first_source_that_sets_it(
    isolated_aws: Path,
    monkeypatch: pytest.MonkeyPatch,
    runtimes: list[RuntimeClient],
    argument: str | None,
    environment: dict[str, str],
    expected: str,
) -> None:
    """Catches a client that sends pages to another region than the one the user set, so the endpoint is missing."""
    isolated_aws.write_text("[default]\nregion = ca-central-1\n")
    for name, value in environment.items():
        monkeypatch.setenv(name, value)
    client = _client(argument)
    assert client.aws_region == expected
    assert runtime_meta(runtimes[0]).region_name == expected


def test_named_profile_gives_its_region(isolated_aws: Path) -> None:
    """Catches `aws_profile` ignored, which reads the region of the default profile."""
    isolated_aws.write_text("[default]\nregion = us-east-1\n\n[profile analytics]\nregion = eu-central-1\n")
    assert _client(aws_profile="analytics").aws_region == "eu-central-1"


def test_unknown_profile_raises_a_clear_error() -> None:
    """Catches a typo in `aws_profile` that escapes as a raw botocore error."""
    with pytest.raises(ReductoError, match="AWS profile 'typo' was not found"):
        _client("us-east-2", aws_profile="typo")


def test_no_region_raises_a_clear_error() -> None:
    """Catches a botocore NoRegionError on the first page, after the document is read, with no hint."""
    with pytest.raises(ReductoError, match="No AWS region was found. Pass `aws_region`"):
        _client()


@pytest.mark.parametrize(
    ("module", "package"),
    [("boto3", "boto3"), ("pypdfium2", "pypdfium2"), ("PIL.Image", "Pillow")],
)
def test_missing_package_names_the_install_command_at_construction(
    monkeypatch: pytest.MonkeyPatch, module: str, package: str
) -> None:
    """Catches a missing package found only later, as a bare ModuleNotFoundError in a worker thread."""
    monkeypatch.setitem(sys.modules, module, None)
    with pytest.raises(ImportError, match=rf'^{package} is not installed\. .*pip install "reductoai\[sagemaker\]"'):
        _client("us-east-2")


def test_session_token_is_sent(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches `aws_session_token` dropped, which makes temporary credentials fail with a signature error."""
    endpoint = LocalEndpoint(body=blocks_answer())
    with serve(endpoint, monkeypatch):
        client = ReductoSageMaker(
            endpoint_name=ENDPOINT, aws_region="us-east-2", aws_session_token="session-token", **CREDENTIALS
        )
        client.parse.run(input=make_pdf(1))
    assert endpoint.requests[0]["x-amz-security-token"] == "session-token"


@pytest.mark.parametrize(
    "given",
    [("aws_access_key",), ("aws_secret_key",), ("aws_session_token",), ("aws_access_key", "aws_session_token")],
    ids=["access-key", "secret-key", "session-token", "access-key-and-token"],
)
def test_incomplete_keys_raise(given: tuple[str, ...]) -> None:
    """Catches partial keys that boto3 mixes with credentials from another source, which fail on the first page."""
    keys = {
        name: "value" if name in given else None for name in ("aws_access_key", "aws_secret_key", "aws_session_token")
    }
    with pytest.raises(ReductoError, match="Pass both `aws_access_key` and `aws_secret_key`"):
        ReductoSageMaker(
            endpoint_name=ENDPOINT,
            aws_region="us-east-2",
            aws_access_key=keys["aws_access_key"],
            aws_secret_key=keys["aws_secret_key"],
            aws_session_token=keys["aws_session_token"],
        )
