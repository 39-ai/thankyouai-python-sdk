# ThankYou Python SDK

Official Python SDK for the ThankYou unified creative generation API.

```bash
pip install thankyouai
```

## Create a Client

```python
from thankyou import ThankYou

thankyou = ThankYou(api_key="tk_...")
```

The default base URL is `https://api.thankyouai.com/open/v1`.

## Text to Image

```python
result = thankyou.run(
    model="flux-2:pro/text-to-image",
    input={
        "prompt": "A mountain landscape at golden hour",
        "aspect_ratio": "16:9",
    },
)

print(result.output[0]["url"])
```

## Image to Video with an Uploaded File

```python
file = thankyou.files.upload(file="./photo.jpg")

generation = thankyou.generations.create(
    model="wan/v2.6/image-to-video",
    input={
        "prompt": "Gentle camera movement with soft evening light",
        "reference_assets": [{"url": file.url}],
    },
)

result = thankyou.generations.wait(
    generation.id,
    interval=3.0,
    timeout=10 * 60,
)
```

## Quote Before Execute

Use a quote when you want to estimate the cost and check whether a request can run before starting the generation. A quote returns the resolved input, estimated cost, blocking reasons, and an expiration time.

```python
quote = thankyou.generations.quote(
    model="wan/v2.6/text-to-video",
    input={"prompt": "A koi fish swimming", "duration": 5},
)

if quote.blocking_reasons:
    raise RuntimeError(", ".join(quote.blocking_reasons))

print(quote.estimated_cost, quote.currency, quote.expires_at)

generation = thankyou.generations.create(quote_id=quote.quote_id)
```

## Models

```python
models = thankyou.models.list()
detail = thankyou.models.detail("wan/v2.6/text-to-video")

print(len(models.models))
print(detail.input_schema)
```

Model IDs can contain `/`, so `models.detail()` calls `GET /models/detail?model_id=...`.

## Webhook Verification

```python
event = thankyou.webhooks.verify(
    raw_body=raw_body,
    signature=request.headers["x-thankyou-signature"],
    timestamp=request.headers["x-thankyou-timestamp"],
    secret="whsec_...",
)

if event.event == "generation.completed":
    print(event.generation.output[0]["url"] if event.generation else None)
```

The signature is HMAC-SHA256 over `{timestamp}.{raw_body}` and is formatted as `sha256=<hex>`.

## Error Handling

```python
from thankyou import (
    ThankYouAPIError,
    ThankYouAuthenticationError,
    ThankYouRateLimitError,
    ThankYouValidationError,
)

try:
    thankyou.generations.create(
        model="wan/v2.6/text-to-video",
        input={"prompt": "test"},
    )
except ThankYouRateLimitError as error:
    print("Rate limited", error.code, error.details)
except ThankYouValidationError as error:
    print("Invalid request", error.details)
except ThankYouAuthenticationError:
    print("Check your API key")
except ThankYouAPIError as error:
    print(error.status, error.code, error.retryable, error.details)
```

## Type Strategy

The SDK provides generated typed input and output hints for supported models, while still allowing generic JSON for dynamic model discovery.

