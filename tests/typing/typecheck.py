from __future__ import annotations

from datetime import datetime
from typing import Literal, assert_type

from thankyou import ThankYou
from thankyou.resources.generations.generated import (
    GoogleNanoBananaTextToImageInput,
    WanV26TextToVideoInput,
)
from thankyou.resources.generations.outputs import ImageGenerationOutput

client = ThankYou(api_key="tk_test")

image_input: GoogleNanoBananaTextToImageInput = {
    "prompt": "Typed response",
    "output_format": "png",
}
image_response = client.generations.create(
    model="google/nano-banana/text-to-image",
    input=image_input,
)
assert_type(image_response.model, Literal["google/nano-banana/text-to-image"])
assert_type(image_response.output[0], ImageGenerationOutput)
assert_type(image_response.created_at, datetime)
assert_type(image_response.params_raw, GoogleNanoBananaTextToImageInput)

image_run_response = client.run(
    model="google/nano-banana/text-to-image",
    input=image_input,
)
assert_type(image_run_response.output[0], ImageGenerationOutput)

quote_input: WanV26TextToVideoInput = {
    "prompt": "Typed quote response",
}
quote = client.generations.quote(
    model="wan/v2.6/text-to-video",
    input=quote_input,
)
assert_type(quote.expires_at, datetime)
assert_type(quote.resolved_params, WanV26TextToVideoInput)

client.generations.create(
    model="google/nano-banana/text-to-image",
    input={"prompt": 123},  # pyright: ignore[reportArgumentType]
)  # type: ignore[call-overload]
client.run(
    model="google/nano-banana/text-to-image",
    input={"prompt": 123},  # pyright: ignore[reportArgumentType]
)  # type: ignore[call-overload]
client.generations.quote(
    model="wan/v2.6/text-to-video",
    input={"prompt": 123},  # pyright: ignore[reportArgumentType]
)  # type: ignore[call-overload]
