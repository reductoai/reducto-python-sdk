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
from reductoai.types import UploadResponse
```

Methods:

- <code title="post /upload">client.<a href="./src/reductoai/_client.py">upload</a>(\*\*<a href="src/reductoai/types/client_upload_params.py">params</a>) -> <a href="./src/reductoai/types/upload_response.py">UploadResponse</a></code>

# Job

Types:

```python
from reductoai.types import JobCancelResponse, JobGetResponse
```

Methods:

- <code title="post /cancel/{job_id}">client.job.<a href="./src/reductoai/resources/job.py">cancel</a>(job_id) -> <a href="./src/reductoai/types/job_cancel_response.py">object</a></code>
- <code title="get /job/{job_id}">client.job.<a href="./src/reductoai/resources/job.py">get</a>(job_id) -> <a href="./src/reductoai/types/job_get_response.py">JobGetResponse</a></code>

# Split

Types:

```python
from reductoai.types import SplitRunJobResponse
```

Methods:

- <code title="post /split">client.split.<a href="./src/reductoai/resources/split.py">run</a>(\*\*<a href="src/reductoai/types/split_run_params.py">params</a>) -> <a href="./src/reductoai/types/shared/split_response.py">SplitResponse</a></code>
- <code title="post /split_async">client.split.<a href="./src/reductoai/resources/split.py">run_job</a>(\*\*<a href="src/reductoai/types/split_run_job_params.py">params</a>) -> <a href="./src/reductoai/types/split_run_job_response.py">SplitRunJobResponse</a></code>

# Parse

Types:

```python
from reductoai.types import ParseRunJobResponse
```

Methods:

- <code title="post /parse">client.parse.<a href="./src/reductoai/resources/parse.py">run</a>(\*\*<a href="src/reductoai/types/parse_run_params.py">params</a>) -> <a href="./src/reductoai/types/shared/parse_response.py">ParseResponse</a></code>
- <code title="post /parse_async">client.parse.<a href="./src/reductoai/resources/parse.py">run_job</a>(\*\*<a href="src/reductoai/types/parse_run_job_params.py">params</a>) -> <a href="./src/reductoai/types/parse_run_job_response.py">ParseRunJobResponse</a></code>

# Extract

Types:

```python
from reductoai.types import ExtractRunJobResponse
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/reductoai/resources/extract.py">run</a>(\*\*<a href="src/reductoai/types/extract_run_params.py">params</a>) -> <a href="./src/reductoai/types/shared/extract_response.py">ExtractResponse</a></code>
- <code title="post /extract_async">client.extract.<a href="./src/reductoai/resources/extract.py">run_job</a>(\*\*<a href="src/reductoai/types/extract_run_job_params.py">params</a>) -> <a href="./src/reductoai/types/extract_run_job_response.py">ExtractRunJobResponse</a></code>

# Webhook

Types:

```python
from reductoai.types import WebhookRunResponse
```

Methods:

- <code title="post /configure_webhook">client.webhook.<a href="./src/reductoai/resources/webhook.py">run</a>() -> str</code>
