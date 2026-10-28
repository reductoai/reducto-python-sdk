#!/usr/bin/env python3
"""Parses a document with your r-1 endpoint on Amazon SageMaker.

Usage: python3 examples/sagemaker/parse.py ENDPOINT_NAME DOCUMENT [AWS_REGION]
See README.md in this folder for the options and errors.
"""

from __future__ import annotations

import sys

from reducto import PageParseError, ReductoSageMaker


def main(endpoint_name: str, document: str, aws_region: str | None = None) -> None:
    with ReductoSageMaker(endpoint_name=endpoint_name, aws_region=aws_region) as client:
        try:
            response = client.parse.run(input=document)
        except PageParseError as error:
            for failed in error.failed_pages:
                print(f"Page {failed.page} failed: {failed.reason}. {failed.detail or ''}".rstrip())
            sys.exit(str(error))

    for chunk in response.result.chunks:
        print(chunk.content, end="\n\n")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(*sys.argv[1:])
