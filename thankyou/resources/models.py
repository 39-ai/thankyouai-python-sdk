from __future__ import annotations

from typing import TypeVar, cast

from thankyou._client import APIClient, AsyncAPIClient, RequestConfig, RequestOptions
from thankyou._utils import as_dict
from thankyou.resources.generations.inputs import JsonObject
from thankyou.types import (
    ModelDetail,
    ModelListResponse,
    ModelPricing,
    ModelPricingOption,
    ModelSummary,
)

ModelT = TypeVar("ModelT", bound=str)


class ModelsResource:
    """Discover supported generation models and their input metadata."""

    def __init__(self, client: APIClient) -> None:
        self._client = client

    def list(self, *, request_options: RequestOptions | None = None) -> ModelListResponse[str]:
        """List available generation models."""
        response = self._client.request(
            RequestConfig(method="GET", path="/models", auth=False, options=request_options)
        )
        data = as_dict(response)
        return ModelListResponse(
            models=[_parse_model_summary(item) for item in data.get("models", [])]
        )

    def detail(
        self,
        model_id: ModelT,
        *,
        request_options: RequestOptions | None = None,
    ) -> ModelDetail[ModelT, JsonObject]:
        """Retrieve metadata, defaults, pricing, and input schema for a model."""
        response = self._client.request(
            RequestConfig(
                method="GET",
                path="/models/detail",
                auth=False,
                query={"model_id": model_id},
                options=request_options,
            )
        )
        return _parse_model_detail(response)


class AsyncModelsResource:
    """Async model discovery helpers."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> ModelListResponse[str]:
        """List available generation models."""
        response = await self._client.request(
            RequestConfig(method="GET", path="/models", auth=False, options=request_options)
        )
        data = as_dict(response)
        return ModelListResponse(
            models=[_parse_model_summary(item) for item in data.get("models", [])]
        )

    async def detail(
        self,
        model_id: ModelT,
        *,
        request_options: RequestOptions | None = None,
    ) -> ModelDetail[ModelT, JsonObject]:
        """Retrieve metadata, defaults, pricing, and input schema for a model."""
        response = await self._client.request(
            RequestConfig(
                method="GET",
                path="/models/detail",
                auth=False,
                query={"model_id": model_id},
                options=request_options,
            )
        )
        return _parse_model_detail(response)


def _parse_pricing(value: object) -> ModelPricing | None:
    if value is None:
        return None
    data = as_dict(value)
    return ModelPricing(
        category_key=str(data.get("category_key", "")),
        currency=str(data.get("currency", "")),
        unit=str(data.get("unit", "")),
        fallback=bool(data.get("fallback", False)),
        options=[
            ModelPricingOption(
                key=str(as_dict(item).get("key", "")),
                label=str(as_dict(item).get("label", "")),
                amount=float(as_dict(item).get("amount", 0)),
                metadata=cast(dict[str, object], as_dict(item).get("metadata", {})),
            )
            for item in data.get("options", [])
        ],
    )


def _parse_model_summary(value: object) -> ModelSummary[str]:
    data = as_dict(value)
    return ModelSummary(
        id=str(data["id"]),
        display_name=str(data.get("display_name", "")),
        description=str(data.get("description", "")),
        operation=str(data.get("operation", "")),
        category=str(data.get("category", "")),
        supported_modes=[str(item) for item in data.get("supported_modes", [])],
        providers=[str(item) for item in data.get("providers", [])],
        vendor=str(data.get("vendor", "")),
        audio_support=str(data.get("audio_support", "")),
        badges=[str(item) for item in data.get("badges", [])],
        features=[str(item) for item in data.get("features", [])],
        preview_image=str(data.get("preview_image", "")),
        pricing=_parse_pricing(data.get("pricing")),
    )


def _parse_model_detail(value: object) -> ModelDetail[ModelT, JsonObject]:
    data = as_dict(value)
    summary = _parse_model_summary(data)
    return ModelDetail(
        id=cast(ModelT, summary.id),
        display_name=summary.display_name,
        description=summary.description,
        operation=summary.operation,
        category=summary.category,
        supported_modes=summary.supported_modes,
        providers=summary.providers,
        vendor=summary.vendor,
        audio_support=summary.audio_support,
        badges=summary.badges,
        features=summary.features,
        preview_image=summary.preview_image,
        pricing=summary.pricing,
        default_mode=str(data.get("default_mode", "")),
        default_params=cast(JsonObject, data.get("default_params", {})),
        input_schema=cast(dict[str, object], data.get("input_schema", {})),
        primary_fields=cast(list[dict[str, object]], data.get("primary_fields", [])),
        advanced_fields=cast(list[dict[str, object]], data.get("advanced_fields", [])),
        resolution_map=cast(dict[str, object], data.get("resolution_map", {})),
    )
