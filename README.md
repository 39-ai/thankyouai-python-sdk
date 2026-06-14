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
result = await thankyou.run(
    model="flux/v2/pro/text-to-image",
    input={
        "prompt": "A mountain landscape at golden hour",
        "aspect_ratio": "16:9",
    },
)

print(result.output[0]["url"])
```

## Image to Video with an Uploaded File

```python
file = await thankyou.files.upload(file="./photo.jpg")

generation = await thankyou.generations.create(
    model="wan/v2.6/image-to-video",
    input={
        "prompt": "Gentle camera movement with soft evening light",
        "reference_assets": [{"url": file.url}],
    },
)

result = await thankyou.generations.wait(
    generation.id,
    interval=3.0,
    timeout=10 * 60,
)
```

## Quote Before Execute

Use a quote when you want to estimate the cost and check whether a request can run before starting the generation. A quote returns the resolved input, estimated cost, blocking reasons, and an expiration time.

```python
quote = await thankyou.generations.quote(
    model="wan/v2.6/text-to-video",
    input={"prompt": "A koi fish swimming", "duration": 5},
)

if quote.blocking_reasons:
    raise RuntimeError(", ".join(quote.blocking_reasons))

print(quote.estimated_cost, quote.currency, quote.expires_at)

generation = await thankyou.generations.create(quote_id=quote.quote_id)
```

## Models

```python
models = await thankyou.models.list()
detail = await thankyou.models.detail("wan/v2.6/text-to-video")

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
    await thankyou.generations.create(
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

The SDK keeps generation request and response types close to the public API contract:

- top-level fields are `model`, `input`, `webhook`, `idempotency_key`, and `quote_id`;
- `input` includes common hints such as `prompt`, `text`, `negative_prompt`, `reference_assets`, `aspect_ratio`, `duration`, and `num_images`;
- generation responses use one common `GenerationOutput` item with `url`, `mime_type`, `width`, `height`, `duration`, and `fps`;
- model-specific fields should be discovered with `thankyou.models.detail(model_id).input_schema` and passed as a normal dict.

This keeps newly released model fields and model-specific output fields usable without waiting for an SDK release.

```python
from thankyou import GenerationInput, GenerationOutput, JsonObject, ThankYou

client = ThankYou(api_key="tk_test")

common_input: GenerationInput = {
    "prompt": "A mountain landscape at golden hour",
    "aspect_ratio": "16:9",
}

generation = await client.generations.create(
    model="google/nano-banana/text-to-image",
    input=common_input,
)
output: GenerationOutput = generation.output[0]
print(output.get("url"))

detail = await client.models.detail("wan/v2.6/text-to-video")
print(detail.input_schema)

model_specific_input: JsonObject = {
    "prompt": "Cinematic drone shot of a mountain lake at sunrise",
    "duration": "5",
    "resolution": "1080P",
    "camera_fixed": False,
}

quote = await client.generations.quote(
    model="wan/v2.6/text-to-video",
    input=model_specific_input,
)
```
