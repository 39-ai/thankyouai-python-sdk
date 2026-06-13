#!/usr/bin/env node
import { createRequire } from "node:module";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import { dirname, join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const sdkRoot = dirname(scriptDir);
const workspaceRoot = dirname(sdkRoot);
const catalogRoot = process.env.THANKYOU_MODEL_CATALOG_ROOT
  ? resolve(process.env.THANKYOU_MODEL_CATALOG_ROOT)
  : join(workspaceRoot, "thankyou-model-catalog");
const outputPath = join(sdkRoot, "thankyou/resources/generations/generated.py");
const generationsStubPath = join(sdkRoot, "thankyou/resources/generations/__init__.pyi");
const rootStubPath = join(sdkRoot, "thankyou/__init__.pyi");
const requireFromCatalog = createRequire(join(catalogRoot, "package.json"));
const { build } = requireFromCatalog("esbuild");

const SDK_HIDDEN_INPUT_FIELDS = new Set([
  "audio_studio_doc_id",
  "callback_url",
  "execution_expires_after",
  "external_task_id",
  "fast_pretreatment",
  "generation_origin",
  "off_peak",
  "response_format",
  "service_tier",
  "watermark_info",
  "wm_position",
  "wm_url"
]);
const SDK_HIDDEN_MODEL_ID_PREFIXES = ["dummy/"];
const SDK_HIDDEN_TASK_ID_PREFIXES = ["audio.dummy.", "image.dummy.", "video.dummy."];

function pyString(value) {
  return JSON.stringify(value);
}

function unique(values) {
  return [...new Map(values.map((value) => [JSON.stringify(value), value])).values()];
}

function typeNameFromId(id, suffix) {
  const words = id
    .replace(/@/g, " at ")
    .replace(/[^a-zA-Z0-9]+/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean);
  const name = words.map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join("");
  return `${/^\d/.test(name) ? "Model" : ""}${name}${suffix}`;
}

function includeField(rule) {
  return rule?.state !== "unsupported";
}

function includeModelSpec(spec) {
  return !SDK_HIDDEN_MODEL_ID_PREFIXES.some((prefix) => spec.id.startsWith(prefix))
    && !SDK_HIDDEN_TASK_ID_PREFIXES.some((prefix) => spec.fieldSpace.id.startsWith(prefix));
}

function isRequired(field, rule) {
  return rule?.state === "required" || field.required === true;
}

function ruleEnum(rule, field) {
  const values = Array.isArray(rule?.enumValues)
    ? rule.enumValues
    : Array.isArray(field?.values)
      ? field.values
      : undefined;
  return values && values.length > 0 ? values : undefined;
}

function enumType(values) {
  const clean = unique([...values].filter((value) => ["string", "number", "boolean"].includes(typeof value) || value === null));
  return clean.length > 0 ? `Literal[${clean.map(pyString).join(", ")}]` : null;
}

function fieldType(field, rule) {
  const values = ruleEnum(rule, field);
  const enumText = values ? enumType(values) : null;
  if (enumText) return enumText;
  const type = typeof rule?.type === "string" ? rule.type : undefined;
  switch (type ?? field.kind) {
    case "text":
    case "string":
      return "str";
    case "int":
      return "int";
    case "number":
      return "int | float";
    case "bool":
      return "bool";
    case "enum":
      return "str";
    case "assetList":
      return "list[ReferenceAsset]";
    case "object":
      return "dict[str, JsonValue]";
    case "array":
      return field.item ? `list[${fieldType(field.item, rule?.item)}]` : "list[JsonValue]";
    case "union": {
      const union = unique((field.options ?? []).map((option) => fieldType(option))).join(" | ");
      return union || "JsonValue";
    }
    default:
      return "JsonValue";
  }
}

function typedDictFor(name, spec) {
  const fields = [];
  for (const [fieldName, field] of Object.entries(spec.fieldSpace.fields ?? {})) {
    if (SDK_HIDDEN_INPUT_FIELDS.has(fieldName)) continue;
    const rule = spec.capability?.[fieldName];
    if (!includeField(rule)) continue;
    const wrapper = isRequired(field, rule) ? "Required" : "NotRequired";
    fields.push(`    ${pyString(fieldName)}: ${wrapper}[${fieldType(field, rule)}],`);
  }
  if (fields.length === 0) return `${name}: TypeAlias = GenericGenerationInput`;
  return [
    `${name} = TypedDict(`,
    `    ${pyString(name)},`,
    "    {",
    ...fields,
    "    },",
    "    total=False,",
    ")",
  ].join("\n");
}

function outputTypeForSpec(spec) {
  const text = [spec.operation, spec.defaultMode, spec.fieldSpace?.id, spec.id]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
  if (text.includes("audio")) return "AudioGenerationOutput";
  if (text.includes("video")) return "VideoGenerationOutput";
  if (text.includes("image")) return "ImageGenerationOutput";
  if (text.includes("text") || text.includes("generate-content") || text.includes("analyze")) return "TextGenerationOutput";
  return "GenericGenerationOutput";
}

async function readModelSpecs() {
  const tempDir = await mkdtemp(join(tmpdir(), "thankyou-python-sdk-model-types-"));
  const entryPath = join(tempDir, "entry.ts");
  const outputBundlePath = join(tempDir, "entry.mjs");
  try {
    await writeFile(
      entryPath,
      [
        `import { CENTRAL_PUBLIC_MODEL_SPECS } from ${JSON.stringify(join(catalogRoot, "src/model-catalog/models/index.ts"))};`,
        "console.log(JSON.stringify(CENTRAL_PUBLIC_MODEL_SPECS.map((spec) => ({",
        "  id: spec.id,",
        "  fieldSpace: spec.fieldSpace,",
        "  operation: spec.operation,",
        "  defaultMode: spec.defaultMode,",
        "  capability: spec.capability,",
        "}))));",
        ""
      ].join("\n")
    );
    await build({
      entryPoints: [entryPath],
      outfile: outputBundlePath,
      bundle: true,
      platform: "node",
      format: "esm",
      target: "node20",
      tsconfig: join(catalogRoot, "tsconfig.json"),
      logLevel: "silent"
    });
    const result = spawnSync(process.execPath, [outputBundlePath], {
      cwd: catalogRoot,
      encoding: "utf8",
      maxBuffer: 50 * 1024 * 1024
    });
    if (result.stderr) process.stderr.write(result.stderr);
    if (result.status !== 0) throw new Error(`catalog export failed with exit code ${result.status ?? "unknown"}`);
    return JSON.parse(result.stdout);
  } finally {
    await rm(tempDir, { recursive: true, force: true });
  }
}

function renderGenerated(specs) {
  const sortedSpecs = [...specs].filter(includeModelSpec).sort((a, b) => a.id.localeCompare(b.id));
  const taskById = new Map();
  for (const spec of sortedSpecs) if (!taskById.has(spec.fieldSpace.id)) taskById.set(spec.fieldSpace.id, spec);
  const tasks = [...taskById.entries()].sort(([a], [b]) => a.localeCompare(b));
  const modelNames = new Map(sortedSpecs.map((spec) => [spec.id, typeNameFromId(spec.id, "Input")]));
  const taskNames = new Map(tasks.map(([id]) => [id, typeNameFromId(id, "TaskInput")]));
  const modelOutputTypes = new Map(sortedSpecs.map((spec) => [spec.id, outputTypeForSpec(spec)]));
  const chunks = [];
  chunks.push('"""This file is generated."""');
  chunks.push("from __future__ import annotations");
  chunks.push("");
  chunks.push("from typing import Literal, NotRequired, Required, TypeAlias, TypedDict");
  chunks.push("");
  chunks.push("from thankyou.resources.generations.inputs import GenericGenerationInput, JsonValue, ReferenceAsset");
  chunks.push("from thankyou.resources.generations.outputs import AudioGenerationOutput, GenericGenerationOutput, ImageGenerationOutput, TextGenerationOutput, VideoGenerationOutput");
  chunks.push("");
  chunks.push(`BuiltInModelId: TypeAlias = Literal[${sortedSpecs.map((spec) => pyString(spec.id)).join(", ")}]`);
  chunks.push(`BuiltInTaskId: TypeAlias = Literal[${tasks.map(([id]) => pyString(id)).join(", ")}]`);
  chunks.push(`BUILT_IN_MODEL_IDS: tuple[BuiltInModelId, ...] = (${sortedSpecs.map((spec) => pyString(spec.id)).join(", ")}${sortedSpecs.length === 1 ? "," : ""})`);
  chunks.push(`BUILT_IN_TASK_IDS: tuple[BuiltInTaskId, ...] = (${tasks.map(([id]) => pyString(id)).join(", ")}${tasks.length === 1 ? "," : ""})`);
  chunks.push("");
  for (const [, spec] of tasks) chunks.push(typedDictFor(taskNames.get(spec.fieldSpace.id), spec), "");
  for (const spec of sortedSpecs) chunks.push(typedDictFor(modelNames.get(spec.id), spec), "");
  chunks.push("GeneratedModelInputMap: TypeAlias = dict[BuiltInModelId, object]");
  chunks.push("GeneratedTaskInputMap: TypeAlias = dict[BuiltInTaskId, object]");
  chunks.push("GeneratedModelOutputMap: TypeAlias = dict[BuiltInModelId, object]");
  chunks.push("GeneratedTaskOutputMap: TypeAlias = dict[BuiltInTaskId, object]");
  chunks.push("");
  return { text: chunks.join("\n"), sortedSpecs, tasks, modelNames, modelOutputTypes };
}

function renderGenerationsStub(rendered) {
  const chunks = [];
  chunks.push("from __future__ import annotations");
  chunks.push("");
  chunks.push("from collections.abc import Mapping");
  chunks.push("from typing import Literal, overload");
  chunks.push("");
  chunks.push("from thankyou._client import APIClient, RequestOptions");
  chunks.push("from thankyou.resources.generations.generated import *");
  chunks.push("from thankyou.resources.generations.inputs import GenericGenerationInput");
  chunks.push("from thankyou.resources.generations.outputs import AudioGenerationOutput, GenericGenerationOutput, ImageGenerationOutput, TextGenerationOutput, VideoGenerationOutput");
  chunks.push("from thankyou.types import GenerationListResponse, GenerationResponse, GenerationStatus, GenerationStatusResponse, QuoteResponse");
  chunks.push("");
  chunks.push("class GenerationsResource:");
  chunks.push("    def __init__(self, client: APIClient) -> None: ...");
  for (const spec of rendered.sortedSpecs) {
    const model = pyString(spec.id);
    const inputType = rendered.modelNames.get(spec.id);
    const outputType = rendered.modelOutputTypes.get(spec.id);
    chunks.push("    @overload");
    chunks.push(`    def create(self, *, model: Literal[${model}], input: ${inputType}, webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., request_options: RequestOptions | None = ...) -> GenerationResponse[Literal[${model}], ${outputType}, ${inputType}]: ...`);
  }
  chunks.push("    @overload");
  chunks.push("    def create(self, *, quote_id: str, idempotency_key: str | None = ..., request_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    @overload");
  chunks.push("    def create(self, *, model: str, input: Mapping[str, object], webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., request_options: RequestOptions | None = ...) -> GenerationResponse[str, object, object]: ...");
  chunks.push("");
  for (const spec of rendered.sortedSpecs) {
    const model = pyString(spec.id);
    const inputType = rendered.modelNames.get(spec.id);
    const outputType = rendered.modelOutputTypes.get(spec.id);
    chunks.push("    @overload");
    chunks.push(`    def run(self, *, model: Literal[${model}], input: ${inputType}, webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[Literal[${model}], ${outputType}, ${inputType}]: ...`);
  }
  chunks.push("    @overload");
  chunks.push("    def run(self, *, quote_id: str, idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    @overload");
  chunks.push("    def run(self, *, model: str, input: Mapping[str, object], webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[str, object, object]: ...");
  chunks.push("");
  chunks.push("    def retrieve(self, generation_id: str, *, request_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    def status(self, generation_id: str, *, request_options: RequestOptions | None = ...) -> GenerationStatusResponse: ...");
  chunks.push("    def wait(self, generation_id: str, *, interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., request_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  for (const spec of rendered.sortedSpecs) {
    const model = pyString(spec.id);
    const inputType = rendered.modelNames.get(spec.id);
    chunks.push("    @overload");
    chunks.push(`    def quote(self, *, model: Literal[${model}], input: ${inputType}, request_options: RequestOptions | None = ...) -> QuoteResponse[Literal[${model}], ${inputType}]: ...`);
  }
  chunks.push("    @overload");
  chunks.push("    def quote(self, *, model: str, input: Mapping[str, object], request_options: RequestOptions | None = ...) -> QuoteResponse[str, object]: ...");
  chunks.push("    def list(self, *, page: int | None = ..., page_size: int | None = ..., status: str | None = ..., model: str | None = ..., model_prefix: str | None = ..., request_options: RequestOptions | None = ...) -> GenerationListResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    def cancel(self, generation_id: str, *, request_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    def retry(self, generation_id: str, *, request_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("");
  return chunks.join("\n");
}

function renderRootStub(rendered) {
  const chunks = [];
  chunks.push("from __future__ import annotations");
  chunks.push("");
  chunks.push("from collections.abc import Mapping");
  chunks.push("from typing import Literal, overload");
  chunks.push("");
  chunks.push("from thankyou._client import RequestOptions, Transport");
  chunks.push("from thankyou.errors import *");
  chunks.push("from thankyou.resources.files import FilesResource");
  chunks.push("from thankyou.resources.generations import GenerationsResource");
  chunks.push("from thankyou.resources.generations.generated import *");
  chunks.push("from thankyou.resources.generations.inputs import *");
  chunks.push("from thankyou.resources.generations.outputs import *");
  chunks.push("from thankyou.resources.models import ModelsResource");
  chunks.push("from thankyou.resources.webhooks import WebhooksResource, compute_signature");
  chunks.push("from thankyou.types import *");
  chunks.push("");
  chunks.push("class ThankYou:");
  chunks.push("    generations: GenerationsResource");
  chunks.push("    models: ModelsResource");
  chunks.push("    files: FilesResource");
  chunks.push("    webhooks: WebhooksResource");
  chunks.push("    def __init__(self, *, api_key: str | None = ..., base_url: str = ..., workspace_id: str | None = ..., timeout: float = ..., max_retries: int = ..., transport: Transport | None = ..., default_headers: dict[str, str] | None = ...) -> None: ...");
  for (const spec of rendered.sortedSpecs) {
    const model = pyString(spec.id);
    const inputType = rendered.modelNames.get(spec.id);
    const outputType = rendered.modelOutputTypes.get(spec.id);
    chunks.push("    @overload");
    chunks.push(`    def run(self, *, model: Literal[${model}], input: ${inputType}, webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[Literal[${model}], ${outputType}, ${inputType}]: ...`);
  }
  chunks.push("    @overload");
  chunks.push("    def run(self, *, quote_id: str, idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]: ...");
  chunks.push("    @overload");
  chunks.push("    def run(self, *, model: str, input: Mapping[str, object], webhook: Mapping[str, object] | None = ..., idempotency_key: str | None = ..., interval: float = ..., timeout: float = ..., terminal_statuses: set[GenerationStatus] | None = ..., create_options: RequestOptions | None = ...) -> GenerationResponse[str, object, object]: ...");
  chunks.push("");
  return chunks.join("\n");
}

const specs = await readModelSpecs();
const rendered = renderGenerated(specs);
await writeFile(outputPath, rendered.text);
await writeFile(generationsStubPath, renderGenerationsStub(rendered));
await writeFile(rootStubPath, renderRootStub(rendered));
console.log(`Generated ${rendered.sortedSpecs.length} model input types and ${rendered.tasks.length} task input types.`);
console.log(outputPath);
console.log(generationsStubPath);
console.log(rootStubPath);
