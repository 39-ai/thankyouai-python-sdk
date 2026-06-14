from __future__ import annotations

from datetime import datetime
from typing import assert_type

from thankyou import GenerationInput, GenerationOutput, JsonObject, ThankYou

client = ThankYou(api_key="tk_test")

common_input: GenerationInput = {
    "prompt": "Typed response",
    "aspect_ratio": "16:9",
    "reference_assets": [{"role": "primary", "url": "https://example.test/image.jpg"}],
}

model_specific_input: JsonObject = {
    "prompt": "Typed quote response",
    "duration": "5",
    "resolution": "1080P",
    "cfg_scale": 0.7,
}


async def check_client() -> None:
    image_response = await client.generations.create(
        model="google/nano-banana/text-to-image",
        input=common_input,
    )
    assert_type(image_response.model, str)
    assert_type(image_response.output[0], GenerationOutput)
    assert_type(image_response.created_at, datetime)
    assert_type(image_response.params_raw, JsonObject)

    quote = await client.generations.quote(
        model="wan/v2.6/text-to-video",
        input=model_specific_input,
    )
    assert_type(quote.expires_at, datetime)
    assert_type(quote.resolved_params, JsonObject)

    image_run_response = await client.run(
        model="google/nano-banana/text-to-image",
        input={
            "prompt": "A custom field path",
            "output_format": "png",
        },
    )
    assert_type(image_run_response.output[0], GenerationOutput)
