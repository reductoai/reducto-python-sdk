# Shared Types

```python
from reducto.types import (
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
    Upload,
    WebhookConfigNew,
)
```

# Reducto

Methods:

- <code title="get /version">client.<a href="./src/reducto/_client.py">api_version</a>() -> object</code>
- <code title="post /upload">client.<a href="./src/reducto/_client.py">upload</a>(\*\*<a href="src/reducto/types/client_upload_params.py">params</a>) -> <a href="./src/reducto/types/shared/upload.py">Upload</a></code>

# Job

Types:

```python
from reducto.types import JobGetResponse
```

Methods:

- <code title="post /cancel/{job_id}">client.job.<a href="./src/reducto/resources/job.py">cancel</a>(job_id) -> object</code>
- <code title="get /job/{job_id}">client.job.<a href="./src/reducto/resources/job.py">get</a>(job_id) -> <a href="./src/reducto/types/job_get_response.py">JobGetResponse</a></code>

# Split

Types:

```python
from reducto.types import SplitRunJobResponse
```

Methods:

- <code title="post /split">client.split.<a href="./src/reducto/resources/split.py">run</a>(\*\*<a href="src/reducto/types/split_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/split_response.py">SplitResponse</a></code>
- <code title="post /split_async">client.split.<a href="./src/reducto/resources/split.py">run_job</a>(\*\*<a href="src/reducto/types/split_run_job_params.py">params</a>) -> <a href="./src/reducto/types/split_run_job_response.py">SplitRunJobResponse</a></code>

# Parse

Types:

```python
from reducto.types import ParseRunJobResponse
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reducto/resources/parse.py">run</a>(\*\*<a href="src/reducto/types/parse_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/parse_response.py">ParseResponse</a></code>
- <code title="post /parse_async">client.parse.<a href="./src/reducto/resources/parse.py">run_job</a>(\*\*<a href="src/reducto/types/parse_run_job_params.py">params</a>) -> <a href="./src/reducto/types/parse_run_job_response.py">ParseRunJobResponse</a></code>

# Extract

Types:

```python
from reducto.types import ExtractRunJobResponse
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/reducto/resources/extract.py">run</a>(\*\*<a href="src/reducto/types/extract_run_params.py">params</a>) -> <a href="./src/reducto/types/shared/extract_response.py">ExtractResponse</a></code>
- <code title="post /extract_async">client.extract.<a href="./src/reducto/resources/extract.py">run_job</a>(\*\*<a href="src/reducto/types/extract_run_job_params.py">params</a>) -> <a href="./src/reducto/types/extract_run_job_response.py">ExtractRunJobResponse</a></code>

# Edit

Types:

```python
from reducto.types import EditRunResponse, EditRunJobResponse
```

Methods:

- <code title="post /edit">client.edit.<a href="./src/reducto/resources/edit.py">run</a>(\*\*<a href="src/reducto/types/edit_run_params.py">params</a>) -> <a href="./src/reducto/types/edit_run_response.py">EditRunResponse</a></code>
- <code title="post /edit_async">client.edit.<a href="./src/reducto/resources/edit.py">run_job</a>(\*\*<a href="src/reducto/types/edit_run_job_params.py">params</a>) -> <a href="./src/reducto/types/edit_run_job_response.py">EditRunJobResponse</a></code>

# Webhook

Types:

```python
from reducto.types import WebhookRunResponse
```

Methods:

- <code title="post /configure_webhook">client.webhook.<a href="./src/reducto/resources/webhook.py">run</a>() -> str</code>

# Config

Types:

```python
from reducto.types import ExtractConfig, ParseConfig
```
