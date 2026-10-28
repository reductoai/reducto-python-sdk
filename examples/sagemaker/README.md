# Parse with your r-1 endpoint on Amazon SageMaker

`ReductoSageMaker` parses documents with an r-1 endpoint that you deploy from AWS Marketplace to SageMaker
real-time inference. The client renders each page on your machine and sends it to your endpoint. Your documents
do not go to Reducto. Deploy the r-1 model package from AWS Marketplace.

## Install

```sh
pip install "reductoai[sagemaker]"
```

For HEIC photos, also install `reductoai[heic]`. That extra bundles LGPL libraries.

## Quick start

```python
from reducto import ReductoSageMaker

client = ReductoSageMaker(
    endpoint_name="my-r1-endpoint",
    aws_region="us-east-2",  # else AWS_REGION, AWS_DEFAULT_REGION, or your AWS profile
)

response = client.parse.run(input="report.pdf", settings={"page_range": {"start": 1, "end": 20}})
for chunk in response.result.chunks:
    print(chunk.content)
```

boto3 finds the AWS credentials. You can also pass `aws_profile`, or `aws_access_key`, `aws_secret_key`, and
`aws_session_token`. `AsyncReductoSageMaker` has the same API with `await`. [`parse.py`](parse.py) is a complete
script:

```sh
python3 examples/sagemaker/parse.py my-r1-endpoint report.pdf us-east-2
```

## Inputs and outputs

- **Input:** a path, bytes (or a bytearray or memoryview), or a binary file object of a PDF, PNG, JPEG, TIFF, WebP,
  GIF, BMP, or HEIC file. Each PDF page and each image frame is one page.
- **Output:** a `ParseResponse` with one chunk for each requested page, in page order. Each block has `type`, `bbox`
  (0 to 1 on the page), and `content`. A table is HTML.

## Options

`parse.run` takes the same keyword names as the hosted `parse.run`, but only `input`, `settings.page_range`, and
`settings.document_password` are supported. Any other option raises `UnsupportedOnProviderError` before the document
is read. That includes the hosted request options `async_`, `queue_priority`, `extra_headers`, `extra_query`,
`extra_body`, and `timeout` when you give them a value; at their defaults they are accepted. To limit the wait for each
page, set `timeout` on the client instead. A file type that the client does not support also raises `UnsupportedOnProviderError`, with the type name,
for example `DOCX files are not supported when you call your own r-1 endpoint. The hosted Reducto API parses them.`

## Errors

- **Failed pages:** when any page fails, `parse.run` raises `PageParseError` after the other pages finish. Its message
  names each failed page and reason, and ends with the `page_range` that retries them, for example
  `1 of 20 pages failed: page 7 (unprocessable). Retry them with settings={"page_range": [7]}.`
  - `error.failed_pages` gives the page number, the reason (`"unprocessable"` when the endpoint answers 422
    `input could not be processed`, else `"error"`), the status, and a detail.
  - `error.partial_response` is a `ParseResponse` with the pages that succeeded, or `None` when no page succeeded.
- **Errors that stop the document:**
  - A document that cannot be opened (corrupt, or a wrong `document_password`) raises `ReductoError` before any page
    is sent.
  - An endpoint that does not support this SDK, or an endpoint that rejects the request itself (a 400, or a 422
    with another detail), raises `ReductoError`.
  - A missing endpoint, a missing permission, or missing credentials raise the botocore exception unchanged, for
    example `botocore.exceptions.ClientError` or `NoCredentialsError`.
- **Retries:** the client retries a page `max_retries` times (default 2) after a 429, a 5xx other than 504, or a
  broken connection. It does not retry a 504, a connect or read timeout, a 422, or another 4xx.

## Retry failed pages

The page numbers in `error.failed_pages` are the 1-based document page (or image frame) numbers that `page_range`
takes, so you can retry only the failed pages:

```python
from reducto import PageParseError

try:
    response = client.parse.run(input="report.pdf")
except PageParseError as error:
    pages = [p.page for p in error.failed_pages]
    retried = client.parse.run(input="report.pdf", settings={"page_range": pages})
```

A retry can succeed for some pages. Some pages fail every time, so do not retry without a limit.

## Concurrency

`max_concurrency` (default 4) is the number of pages in flight per client, across every `parse.run` call and thread
that shares the client. Raise it when the endpoint has more instances. When you cancel an `AsyncReductoSageMaker`
call, it returns at once and sends no more pages. A page call that is in progress finishes in the background.

## Limits

- The client renders each page to fit the endpoint's documented default image size (3,145,728 pixels), up to
  300 DPI. It scales a larger image down to that size and never scales a page up.
- Each request body holds only the page image, as PNG, or as JPEG when the PNG body is over the 6 MB request limit.
  The client scales a page down further only when the lowest JPEG quality is still over the limit.
- The client does not decode an image over 100,000,000 pixels. A larger JPEG decodes at a reduced scale.
- `timeout` (default 65 seconds) is the read timeout of one call. A SageMaker real-time endpoint must answer within
  60 seconds.

## Hosted-only resources

The client has only `parse.run`. `client.extract`, `client.split`, `client.edit`, `client.pipeline`,
`client.upload`, `client.parse.run_job`, and the other hosted resources raise `UnsupportedOnProviderError`, which
points to the hosted API. To move to the hosted API, use `Reducto(api_key=...)`. `parse.run` takes the same options,
and `input` is a URL or the result of `client.upload`.
