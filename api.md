# Shared Types

```python
from reducto.types import Upload
```

# Reducto

Types:

```python
from reducto.types import APIVersionResponse
```

Methods:

- <code title="get /version">client.<a href="./src/reducto/_client.py">api_version</a>() -> str</code>
- <code title="post /upload">client.<a href="./src/reducto/_client.py">upload</a>(\*\*<a href="src/reducto/types/client_upload_params.py">params</a>) -> <a href="./src/reducto/types/shared/upload.py">Upload</a></code>

# Parse

Types:

```python
from reducto.types import (
    AsyncConfigV3,
    AsyncParseConfig,
    AsyncParseResponse,
    Enhance,
    Formatting,
    ParseResponse,
    Retrieval,
    Settings,
    Spreadsheet,
    ParseRunResponse,
)
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reducto/resources/parse.py">run</a>(\*\*<a href="src/reducto/types/parse_run_params.py">params</a>) -> <a href="./src/reducto/types/parse_run_response.py">ParseRunResponse</a></code>
- <code title="post /parse_async">client.parse.<a href="./src/reducto/resources/parse.py">run_job</a>(\*\*<a href="src/reducto/types/parse_run_job_params.py">params</a>) -> <a href="./src/reducto/types/async_parse_response.py">AsyncParseResponse</a></code>

# Extract

Types:

```python
from reducto.types import (
    AsyncExtractConfig,
    AsyncExtractResponse,
    ExtractSettings,
    ExtractUsage,
    Instructions,
    ParseOptions,
    V3Extract,
    ExtractRunResponse,
)
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/reducto/resources/extract.py">run</a>(\*\*<a href="src/reducto/types/extract_run_params.py">params</a>) -> <a href="./src/reducto/types/extract_run_response.py">ExtractRunResponse</a></code>
- <code title="post /extract_async">client.extract.<a href="./src/reducto/resources/extract.py">run_job</a>(\*\*<a href="src/reducto/types/extract_run_job_params.py">params</a>) -> <a href="./src/reducto/types/async_extract_response.py">AsyncExtractResponse</a></code>

# Split

Types:

```python
from reducto.types import (
    DeepSplitPageEvidence,
    ParseUsage,
    SplitCategory,
    SplitResponse,
    SplitTableOptions,
    SplitRunJobResponse,
)
```

Methods:

- <code title="post /split">client.split.<a href="./src/reducto/resources/split.py">run</a>(\*\*<a href="src/reducto/types/split_run_params.py">params</a>) -> <a href="./src/reducto/types/split_response.py">SplitResponse</a></code>
- <code title="post /split_async">client.split.<a href="./src/reducto/resources/split.py">run_job</a>(\*\*<a href="src/reducto/types/split_run_job_params.py">params</a>) -> <a href="./src/reducto/types/split_run_job_response.py">SplitRunJobResponse</a></code>

# Edit

Types:

```python
from reducto.types import BoundingBox, EditOptions, EditResponse, EditWidget, EditRunJobResponse
```

Methods:

- <code title="post /edit">client.edit.<a href="./src/reducto/resources/edit.py">run</a>(\*\*<a href="src/reducto/types/edit_run_params.py">params</a>) -> <a href="./src/reducto/types/edit_response.py">EditResponse</a></code>
- <code title="post /edit_async">client.edit.<a href="./src/reducto/resources/edit.py">run_job</a>(\*\*<a href="src/reducto/types/edit_run_job_params.py">params</a>) -> <a href="./src/reducto/types/edit_run_job_response.py">EditRunJobResponse</a></code>

# Pipeline

Types:

```python
from reducto.types import PipelineResponse, PipelineSettings, PipelineRunJobResponse
```

Methods:

- <code title="post /pipeline">client.pipeline.<a href="./src/reducto/resources/pipeline.py">run</a>(\*\*<a href="src/reducto/types/pipeline_run_params.py">params</a>) -> <a href="./src/reducto/types/pipeline_response.py">PipelineResponse</a></code>
- <code title="post /pipeline_async">client.pipeline.<a href="./src/reducto/resources/pipeline.py">run_job</a>(\*\*<a href="src/reducto/types/pipeline_run_job_params.py">params</a>) -> <a href="./src/reducto/types/pipeline_run_job_response.py">PipelineRunJobResponse</a></code>

# Classify

Types:

```python
from reducto.types import ClassifyResponse, PageRange
```

Methods:

- <code title="post /classify">client.classify.<a href="./src/reducto/resources/classify.py">run</a>(\*\*<a href="src/reducto/types/classify_run_params.py">params</a>) -> <a href="./src/reducto/types/classify_response.py">ClassifyResponse</a></code>

# Webhook

Types:

```python
from reducto.types import WebhookRunResponse
```

Methods:

- <code title="post /configure_webhook">client.webhook.<a href="./src/reducto/resources/webhook.py">run</a>() -> str</code>

# Job

Types:

```python
from reducto.types import ExtractResponse, JobGetResponse, JobGetAllResponse
```

# Classify

Types:

```python
from reducto.types import ClassifyCreateResponse
```

Methods:

- <code title="post /classify">client.classify.<a href="./src/reducto/resources/classify.py">create</a>(\*\*<a href="src/reducto/types/classify_create_params.py">params</a>) -> <a href="./src/reducto/types/classify_create_response.py">ClassifyCreateResponse</a></code>
