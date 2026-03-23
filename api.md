# Parse

Types:

```python
from reducto.types import ParseResponse, ParseCreateResponse
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reducto/resources/parse.py">create</a>(\*\*<a href="src/reducto/types/parse_create_params.py">params</a>) -> <a href="./src/reducto/types/parse_create_response.py">ParseCreateResponse</a></code>

# ParseAsync

Types:

```python
from reducto.types import (
    AsyncConfigV3,
    AsyncParseConfig,
    AsyncParseResponse,
    Enhance,
    Formatting,
    Retrieval,
    Settings,
    Spreadsheet,
)
```

Methods:

- <code title="post /parse_async">client.parse_async.<a href="./src/reducto/resources/parse_async.py">create</a>(\*\*<a href="src/reducto/types/parse_async_create_params.py">params</a>) -> <a href="./src/reducto/types/async_parse_response.py">AsyncParseResponse</a></code>

# Extract

Types:

```python
from reducto.types import ExtractUsage, V3Extract, ExtractCreateResponse
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/reducto/resources/extract.py">create</a>(\*\*<a href="src/reducto/types/extract_create_params.py">params</a>) -> <a href="./src/reducto/types/extract_create_response.py">ExtractCreateResponse</a></code>

# ExtractAsync

Types:

```python
from reducto.types import (
    AsyncExtractConfig,
    AsyncExtractResponse,
    ExtractSettings,
    Instructions,
    ParseOptions,
)
```

Methods:

- <code title="post /extract_async">client.extract_async.<a href="./src/reducto/resources/extract_async.py">create</a>(\*\*<a href="src/reducto/types/extract_async_create_params.py">params</a>) -> <a href="./src/reducto/types/async_extract_response.py">AsyncExtractResponse</a></code>

# Split

Types:

```python
from reducto.types import (
    DeepSplitPageEvidence,
    ParseUsage,
    SplitCategory,
    SplitResponse,
    SplitTableOptions,
)
```

Methods:

- <code title="post /split">client.split.<a href="./src/reducto/resources/split.py">create</a>(\*\*<a href="src/reducto/types/split_create_params.py">params</a>) -> <a href="./src/reducto/types/split_response.py">SplitResponse</a></code>

# SplitAsync

Types:

```python
from reducto.types import SplitAsyncCreateResponse
```

Methods:

- <code title="post /split_async">client.split_async.<a href="./src/reducto/resources/split_async.py">create</a>(\*\*<a href="src/reducto/types/split_async_create_params.py">params</a>) -> <a href="./src/reducto/types/split_async_create_response.py">SplitAsyncCreateResponse</a></code>

# Edit

Types:

```python
from reducto.types import BoundingBox, EditOptions, EditResponse, EditWidget
```

Methods:

- <code title="post /edit">client.edit.<a href="./src/reducto/resources/edit.py">submit</a>(\*\*<a href="src/reducto/types/edit_submit_params.py">params</a>) -> <a href="./src/reducto/types/edit_response.py">EditResponse</a></code>

# EditAsync

Types:

```python
from reducto.types import EditAsyncCreateResponse
```

Methods:

- <code title="post /edit_async">client.edit_async.<a href="./src/reducto/resources/edit_async.py">create</a>(\*\*<a href="src/reducto/types/edit_async_create_params.py">params</a>) -> <a href="./src/reducto/types/edit_async_create_response.py">EditAsyncCreateResponse</a></code>

# Pipeline

Types:

```python
from reducto.types import PipelineResponse, PipelineSettings
```

Methods:

- <code title="post /pipeline">client.pipeline.<a href="./src/reducto/resources/pipeline.py">create</a>(\*\*<a href="src/reducto/types/pipeline_create_params.py">params</a>) -> <a href="./src/reducto/types/pipeline_response.py">PipelineResponse</a></code>

# PipelineAsync

Types:

```python
from reducto.types import PipelineAsyncCreateResponse
```

Methods:

- <code title="post /pipeline_async">client.pipeline_async.<a href="./src/reducto/resources/pipeline_async.py">create</a>(\*\*<a href="src/reducto/types/pipeline_async_create_params.py">params</a>) -> <a href="./src/reducto/types/pipeline_async_create_response.py">PipelineAsyncCreateResponse</a></code>

# Classify

Types:

```python
from reducto.types import ClassifyResponse, PageRange
```

Methods:

- <code title="post /classify">client.classify.<a href="./src/reducto/resources/classify.py">create</a>(\*\*<a href="src/reducto/types/classify_create_params.py">params</a>) -> <a href="./src/reducto/types/classify_response.py">ClassifyResponse</a></code>

# Cancel

Methods:

- <code title="post /cancel/{job_id}">client.cancel.<a href="./src/reducto/resources/cancel.py">cancel_job</a>(job_id) -> object</code>

# Upload

Types:

```python
from reducto.types import UploadResponse
```

Methods:

- <code title="post /upload">client.upload.<a href="./src/reducto/resources/upload.py">create</a>(\*\*<a href="src/reducto/types/upload_create_params.py">params</a>) -> <a href="./src/reducto/types/upload_response.py">UploadResponse</a></code>

# ConfigureWebhook

Types:

```python
from reducto.types import ConfigureWebhookCreateResponse
```

Methods:

- <code title="post /configure_webhook">client.configure_webhook.<a href="./src/reducto/resources/configure_webhook.py">create</a>() -> str</code>

# Version

Types:

```python
from reducto.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/reducto/resources/version.py">retrieve</a>() -> str</code>

# Job

Types:

```python
from reducto.types import ExtractResponse, JobRetrieveResponse, JobListResponse
```

Methods:

- <code title="get /job/{job_id}">client.job.<a href="./src/reducto/resources/job.py">retrieve</a>(job_id) -> <a href="./src/reducto/types/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /jobs">client.job.<a href="./src/reducto/resources/job.py">list</a>(\*\*<a href="src/reducto/types/job_list_params.py">params</a>) -> <a href="./src/reducto/types/job_list_response.py">JobListResponse</a></code>
