# Shared Types

```python
from reductoai.types import (
    AdvancedProcessingOptions,
    ArrayExtractConfig,
    BaseProcessingOptions,
    BoundingBox,
    ExperimentalProcessingOptions,
    ExtractResponse,
    PageRange,
    ParseResponse,
    ParseUsage,
    SplitCategory,
    SplitResponse,
    WebhookConfigNew,
)
```

# Reductoai

Types:

```python
from reductoai.types import (
    CancelJobResponse,
    ConfigureWebhookResponse,
    CreateExtractAsyncResponse,
    CreateParseAsyncResponse,
    CreateSplitAsyncResponse,
    CreateUploadResponse,
    GetVersionResponse,
    RetrieveJobResponse,
)
```

Methods:

- <code title="post /cancel/{job_id}">client.<a href="./src/reductoai/_client.py">cancel_job</a>(job_id) -> <a href="./src/reductoai/types/cancel_job_response.py">object</a></code>
- <code title="post /configure_webhook">client.<a href="./src/reductoai/_client.py">configure_webhook</a>() -> str</code>
- <code title="post /extract">client.<a href="./src/reductoai/_client.py">create_extract</a>(\*\*<a href="src/reductoai/types/client_create_extract_params.py">params</a>) -> <a href="./src/reductoai/types/shared/extract_response.py">ExtractResponse</a></code>
- <code title="post /extract_async">client.<a href="./src/reductoai/_client.py">create_extract_async</a>(\*\*<a href="src/reductoai/types/client_create_extract_async_params.py">params</a>) -> <a href="./src/reductoai/types/create_extract_async_response.py">CreateExtractAsyncResponse</a></code>
- <code title="post /parse">client.<a href="./src/reductoai/_client.py">create_parse</a>(\*\*<a href="src/reductoai/types/client_create_parse_params.py">params</a>) -> <a href="./src/reductoai/types/shared/parse_response.py">ParseResponse</a></code>
- <code title="post /parse_async">client.<a href="./src/reductoai/_client.py">create_parse_async</a>(\*\*<a href="src/reductoai/types/client_create_parse_async_params.py">params</a>) -> <a href="./src/reductoai/types/create_parse_async_response.py">CreateParseAsyncResponse</a></code>
- <code title="post /split">client.<a href="./src/reductoai/_client.py">create_split</a>(\*\*<a href="src/reductoai/types/client_create_split_params.py">params</a>) -> <a href="./src/reductoai/types/shared/split_response.py">SplitResponse</a></code>
- <code title="post /split_async">client.<a href="./src/reductoai/_client.py">create_split_async</a>(\*\*<a href="src/reductoai/types/client_create_split_async_params.py">params</a>) -> <a href="./src/reductoai/types/create_split_async_response.py">CreateSplitAsyncResponse</a></code>
- <code title="post /upload">client.<a href="./src/reductoai/_client.py">create_upload</a>(\*\*<a href="src/reductoai/types/client_create_upload_params.py">params</a>) -> <a href="./src/reductoai/types/create_upload_response.py">CreateUploadResponse</a></code>
- <code title="get /version">client.<a href="./src/reductoai/_client.py">get_version</a>() -> <a href="./src/reductoai/types/get_version_response.py">object</a></code>
- <code title="get /job/{job_id}">client.<a href="./src/reductoai/_client.py">retrieve_job</a>(job_id) -> <a href="./src/reductoai/types/retrieve_job_response.py">RetrieveJobResponse</a></code>
