# Shared Types

```python
from reducto.types import (
    AdvancedCitationsConfig,
    AdvancedProcessingOptions,
    ArrayExtractConfig,
    AsyncEditResponse,
    AsyncExtractResponse,
    AsyncParseResponse,
    AsyncPipelineResponse,
    AsyncSplitResponse,
    BaseProcessingOptions,
    Chunking,
    ChunkingConfig,
    ClassifyResponse,
    DirectWebhookConfig,
    EditResponse,
    EnrichConfig,
    ExperimentalProcessingOptions,
    ExtractResponse,
    FigureAgentic,
    FigureSummaryConfig,
    LargeTableChunkingConfig,
    ParseResponse,
    PipelineResponse,
    SplitLargeTables,
    SplitResponse,
    SvixWebhookConfig,
    TableAgentic,
    TableSummaryConfig,
    TextAgentic,
    Upload,
    WebhookConfigNew,
)
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
    Enhance,
    Formatting,
    Retrieval,
    Settings,
    Spreadsheet,
    ParseRunResponse,
)
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reducto/resources/parse.py">run</a>(\*\*<a href="src/reducto/types/parse_run_params.py">params</a>) -> <a href="./src/reducto/types/parse_run_response.py">ParseRunResponse</a></code>
- <code title="post /parse_async">client.parse.<a href="./src/reducto/resources/parse.py">run_job</a>(\*\*<a href="src/reducto/types/parse_run_job_params.py">params</a>) -> <a href="./src/reducto/types/shared/async_parse_response.py">AsyncParseResponse</a></code>

# Extract

Types:

```python
from reducto.types import (
    AsyncExtractConfig,
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
- <code title="post /extract_async">client.extract.<a href="./src/reducto/resources/extract.py">run_job</a>(\*\*<a href="src/reducto/types/extract_run_job_params.py">params</a>) -> <a href="./src/reducto/types/shared/async_extract_response.py">AsyncExtractResponse</a></code>

# Split

Types:

```python
from reducto.types import DeepSplitPageEvidence, ParseUsage, SplitCategory, SplitTableOptions
```

Methods:

- <code title="post /split">client.split.<a href="./src/reducto/resources/split.py">run</a>(\*\*<a href="src/reducto/types/split_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/split_response.py">SplitResponse</a></code>
- <code title="post /split_async">client.split.<a href="./src/reducto/resources/split.py">run_job</a>(\*\*<a href="src/reducto/types/split_run_job_params.py">params</a>) -> <a href="./src/reducto/types/shared/async_split_response.py">AsyncSplitResponse</a></code>

# Edit

Types:

```python
from reducto.types import BoundingBox, EditOptions, EditWidget
```

Methods:

- <code title="post /edit">client.edit.<a href="./src/reducto/resources/edit.py">run</a>(\*\*<a href="src/reducto/types/edit_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/edit_response.py">EditResponse</a></code>
- <code title="post /edit_async">client.edit.<a href="./src/reducto/resources/edit.py">run_job</a>(\*\*<a href="src/reducto/types/edit_run_job_params.py">params</a>) -> <a href="./src/reducto/types/shared/async_edit_response.py">AsyncEditResponse</a></code>

# Pipeline

Types:

```python
from reducto.types import PipelineSettings
```

Methods:

- <code title="post /pipeline">client.pipeline.<a href="./src/reducto/resources/pipeline.py">run</a>(\*\*<a href="src/reducto/types/pipeline_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/pipeline_response.py">PipelineResponse</a></code>
- <code title="post /pipeline_async">client.pipeline.<a href="./src/reducto/resources/pipeline.py">run_job</a>(\*\*<a href="src/reducto/types/pipeline_run_job_params.py">params</a>) -> <a href="./src/reducto/types/shared/async_pipeline_response.py">AsyncPipelineResponse</a></code>

# Classify

Types:

```python
from reducto.types import PageRange
```

Methods:

- <code title="post /classify">client.classify.<a href="./src/reducto/resources/classify.py">run</a>(\*\*<a href="src/reducto/types/classify_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/classify_response.py">ClassifyResponse</a></code>

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
from reducto.types import JobGetResponse, JobGetAllResponse
```

Methods:

- <code title="post /cancel/{job_id}">client.job.<a href="./src/reducto/resources/job.py">cancel</a>(job_id) -> object</code>
- <code title="get /job/{job_id}">client.job.<a href="./src/reducto/resources/job.py">get</a>(job_id) -> <a href="./src/reducto/types/job_get_response.py">JobGetResponse</a></code>
- <code title="get /jobs">client.job.<a href="./src/reducto/resources/job.py">get_all</a>(\*\*<a href="src/reducto/types/job_get_all_params.py">params</a>) -> <a href="./src/reducto/types/job_get_all_response.py">JobGetAllResponse</a></code>
