"""This file is generated."""
from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

from thankyou.resources.generations.inputs import JsonValue, ReferenceAsset
from thankyou.resources.generations.outputs import AudioGenerationOutput, GenericGenerationOutput, ImageGenerationOutput, TextGenerationOutput, VideoGenerationOutput

BuiltInModelId: TypeAlias = Literal["bytedance/seedance/v1.5/pro/image-to-video", "bytedance/seedance/v1.5/pro/text-to-video", "bytedance/seedance/v1/lite/image-to-video", "bytedance/seedance/v1/lite/text-to-video", "bytedance/seedance/v1/pro/fast/text-to-video", "bytedance/seedance/v1/pro/image-to-video", "bytedance/seedance/v1/pro/text-to-video", "bytedance/seedance/v2/image-to-video", "bytedance/seedance/v2/text-to-video", "bytedance/seedream/v3/text-to-image", "bytedance/seedream/v4.5/text-to-image", "bytedance/seedream/v4/text-to-image", "bytedance/seedream/v5/lite/text-to-image", "bytedance/seedream/v5/text-to-image", "dreamactor-v2", "elevenlabs/sound-effect", "fish-audio/text-to-speech", "flux/v1/kontext/dev/edit", "flux/v1/kontext/max/edit", "flux/v1/kontext/pro/edit", "flux/v1/schnell/text-to-image", "flux/v2/dev/text-to-image", "flux/v2/flex/text-to-image", "flux/v2/pro/text-to-image", "glm/image/text-to-image", "google/gemini-3.1-flash/video-understanding", "google/gemini-3.1-pro/video-understanding", "google/nano-banana/edit", "google/nano-banana/pro/edit", "google/nano-banana/pro/text-to-image", "google/nano-banana/pro/vertex", "google/nano-banana/text-to-image", "google/nano-banana/v2/edit", "google/nano-banana/v2/text-to-image", "google/nano-banana/v2/vertex", "google/nano-banana/vertex", "google/veo/v3.1/first-last-frame-to-video", "google/veo/v3.1/image-to-video", "google/veo/v3.1/reference-to-video", "google/veo/v3.1/text-to-video", "heygen/video-translate", "hunyuan/image/v3/text-to-image", "hunyuan/video/fast/text-to-video", "kling/advanced-lip-sync", "kling/advanced-lip-sync/official", "kling/avatar/official", "kling/identify-face", "kling/identify-face/official", "kling/image-to-video", "kling/multi-image-to-video", "kling/o1/image-to-video", "kling/o1/text-to-video", "kling/o1/video-edit", "kling/o1/video-to-video", "kling/o3/4k/image-to-video", "kling/o3/4k/text-to-video", "kling/o3/pro/image-to-video", "kling/o3/pro/reference-to-video", "kling/o3/pro/reference-to-video@7-ref", "kling/o3/pro/text-to-video", "kling/o3/pro/video-edit", "kling/o3/pro/video-to-video", "kling/o3/standard/image-to-video", "kling/o3/standard/reference-to-video", "kling/o3/standard/reference-to-video@7-ref", "kling/o3/standard/text-to-video", "kling/o3/standard/video-edit", "kling/o3/standard/video-to-video", "kling/text-to-audio/official", "kling/text-to-video", "kling/v1.5/pro/image-to-video/official", "kling/v1.5/standard/image-to-video/official", "kling/v1.6/image-to-video", "kling/v1.6/pro/image-to-video/official", "kling/v1.6/pro/multi-image-to-video/official", "kling/v1.6/pro/text-to-video/official", "kling/v1.6/standard/image-to-video/official", "kling/v1.6/standard/multi-image-to-video/official", "kling/v1.6/standard/text-to-video/official", "kling/v1.6/text-to-video", "kling/v1/pro/image-to-video/official", "kling/v1/pro/text-to-video/official", "kling/v1/standard/image-to-video/official", "kling/v1/standard/text-to-video/official", "kling/v2-master/image-to-video/official", "kling/v2-master/text-to-video/official", "kling/v2.1-master/image-to-video/official", "kling/v2.1-master/text-to-video/official", "kling/v2.1/image-to-video", "kling/v2.1/master/image-to-video", "kling/v2.1/master/text-to-video", "kling/v2.1/pro/image-to-video/official", "kling/v2.1/standard/image-to-video/official", "kling/v2.5-turbo/pro/image-to-video/official", "kling/v2.5-turbo/pro/text-to-video/official", "kling/v2.5-turbo/standard/image-to-video/official", "kling/v2.5-turbo/standard/text-to-video/official", "kling/v2.5/turbo/image-to-video", "kling/v2.5/turbo/text-to-video", "kling/v2.6/pro/image-to-video", "kling/v2.6/pro/image-to-video/official", "kling/v2.6/pro/motion-control", "kling/v2.6/pro/motion-control/official", "kling/v2.6/pro/text-to-video", "kling/v2.6/pro/text-to-video/official", "kling/v2.6/standard/image-to-video/official", "kling/v2.6/standard/motion-control/official", "kling/v2.6/standard/text-to-video/official", "kling/v3-omni/4k/image-to-video/official", "kling/v3-omni/4k/text-to-video/official", "kling/v3-omni/pro/image-to-video/official", "kling/v3-omni/pro/reference-to-video@7-ref/official", "kling/v3-omni/pro/reference-to-video/official", "kling/v3-omni/pro/text-to-video/official", "kling/v3-omni/pro/video-edit/official", "kling/v3-omni/pro/video-to-video/official", "kling/v3-omni/standard/image-to-video/official", "kling/v3-omni/standard/reference-to-video@7-ref/official", "kling/v3-omni/standard/reference-to-video/official", "kling/v3-omni/standard/text-to-video/official", "kling/v3-omni/standard/video-edit/official", "kling/v3-omni/standard/video-to-video/official", "kling/v3.0/pro/image-to-video", "kling/v3.0/pro/text-to-video", "kling/v3.0/standard/image-to-video", "kling/v3.0/standard/text-to-video", "kling/v3/4k/image-to-video/official", "kling/v3/4k/text-to-video/official", "kling/v3/pro/image-to-video/official", "kling/v3/pro/motion-control/official", "kling/v3/pro/text-to-video/official", "kling/v3/standard/image-to-video/official", "kling/v3/standard/motion-control/official", "kling/v3/standard/text-to-video/official", "kling/video-effects/official", "kling/video-extension/official", "kling/video-o1/pro/image-to-video/official", "kling/video-o1/pro/text-to-video/official", "kling/video-o1/pro/video-edit/official", "kling/video-o1/pro/video-to-video/official", "kling/video-o1/standard/image-to-video/official", "kling/video-o1/standard/text-to-video/official", "kling/video-o1/standard/video-edit/official", "kling/video-o1/standard/video-to-video/official", "kling/video-to-audio/official", "minimax/hailuo/v2.3/fast/image-to-video", "minimax/hailuo/v2.3/image-to-video", "minimax/hailuo/v2.3/text-to-video", "minimax/hailuo/v2/image-to-video", "minimax/hailuo/v2/start-end-to-video", "minimax/hailuo/v2/text-to-video", "minimax/image/v1/live/image-to-image", "minimax/image/v1/text-to-image", "minimax/video-01/text-to-video", "novita/image-to-image", "novita/image-upscaler/upscale", "novita/image-upscaler/v2/upscale", "novita/image/background-removal", "novita/image/background-removal/v2", "novita/image/background-replacement", "novita/image/cleanup", "novita/image/erase", "novita/image/reimagine", "novita/image/text-removal", "novita/image/to-prompt", "novita/inpaint", "novita/text-to-image", "openai/gpt-image-2", "openai/gpt-image-2/edit", "pixverse/v4.5/image-to-video", "pixverse/v4.5/text-to-video", "qwen/image/edit", "qwen/image/text-to-image", "topaz/image/enhance", "topaz/image/enhance-gen", "topaz/image/tool", "video/face-swap", "vidu/q1/image-to-video", "vidu/q1/reference-to-video", "vidu/q1/start-end-to-video", "vidu/q1/text-to-video", "vidu/q2/pro/fast/image-to-video", "vidu/q2/pro/fast/start-end-to-video", "vidu/q2/pro/image-to-video", "vidu/q2/pro/multi-frame-to-video", "vidu/q2/pro/start-end-to-video", "vidu/q2/reference-to-video", "vidu/q2/template-to-video", "vidu/q2/text-to-video", "vidu/q2/turbo/image-to-video", "vidu/q2/turbo/multi-frame-to-video", "vidu/q2/turbo/start-end-to-video", "vidu/q3/pro/image-to-video", "vidu/q3/pro/text-to-video", "vidu/v2.0/image-to-video", "vidu/v2.0/reference-to-video", "vidu/v2.0/start-end-to-video", "vits-svc/voice-changer", "wan/image-to-video", "wan/text-to-video", "wan/v2.2/image-to-video", "wan/v2.2/text-to-video", "wan/v2.5/preview/image-to-video", "wan/v2.5/preview/text-to-video", "wan/v2.6/image-to-video", "wan/v2.6/text-to-video", "wan/v2.6/video-to-video", "wan/v2.7/edit", "wan/v2.7/extend-video", "wan/v2.7/image-to-video", "wan/v2.7/pro/edit", "wan/v2.7/pro/text-to-image", "wan/v2.7/reference-to-video", "wan/v2.7/text-to-image", "wan/v2.7/text-to-video", "wan/v2.7/video-edit", "wan2.2-animate-replace", "wan2.6-reference-to-video-flash", "youchuan/midjourney-v7-fast", "youchuan/midjourney-v7-turbo", "youchuan/midjourney-v7-upscale", "youchuan/midjourney-v7-variation", "z-image/turbo-lora/text-to-image", "z-image/turbo/text-to-image"]
BuiltInTaskId: TypeAlias = Literal["audio.kling.official.text_to_audio", "audio.kling.official.video_to_audio", "audio.sound_effect.generation", "audio.tts.generation", "audio.voice_changer.transform", "generate-content.google.gemini.video-understanding", "generate-content.google.vertex", "image.byteplus.seedream", "image.enhance", "image.generation", "image.google.generation", "image.minimax.generation", "image.novita.async_img2img", "image.novita.async_inpaint", "image.novita.async_txt2img", "image.novita.async_upscale", "image.novita.async_url", "image.novita.flux_schnell", "image.novita.generic", "image.novita.seedream.dual", "image.novita.seedream.sync", "image.novita.sync_edit", "image.openai.gpt-image-2.edit", "image.openai.gpt-image-2.generation", "image.wan_v27.edit", "image.wan_v27.text_to_image", "video.byteplus.generation", "video.face_merge", "video.generation", "video.google.generation", "video.google.reference_to_video", "video.hunyuan.fast_generation", "video.identify_face", "video.kling_o3.image_to_video", "video.kling_o3.reference_to_video", "video.kling_o3.reference_to_video_7_ref", "video.kling_o3.text_to_video", "video.kling_o3.video_edit", "video.kling_o3.video_to_video", "video.kling.image_to_video", "video.kling.multi_image_to_video", "video.kling.official.avatar", "video.kling.official.identify_face", "video.kling.official.image_to_video", "video.kling.official.lip_sync", "video.kling.official.motion_control", "video.kling.official.multi_image_to_video", "video.kling.official.omni.image_to_video", "video.kling.official.omni.reference_to_video", "video.kling.official.omni.text_to_video", "video.kling.official.omni.video_edit", "video.kling.official.omni.video_to_video", "video.kling.official.text_to_video", "video.kling.official.video_effects", "video.kling.official.video_extension", "video.kling.text_to_video", "video.lip_sync", "video.minimax.image_generation", "video.minimax.text_generation", "video.motion_control", "video.novita.image_generation", "video.novita.reference_image_generation_extra", "video.novita.text_generation", "video.reference_image_generation", "video.reference_video_generation", "video.translate", "video.video_edit", "video.wan_v27.extend_video", "video.wan_v27.image_to_video", "video.wan_v27.reference_to_video", "video.wan_v27.text_to_video", "video.wan_v27.video_edit", "video.wan.image_generation", "video.wan.reference_video_generation", "video.wan.text_generation", "video.wan.text_generation_flat", "video.wan.text_generation_with_loras", "youchuan.midjourney-v7.upscale", "youchuan.midjourney-v7.variation"]
BUILT_IN_MODEL_IDS: tuple[BuiltInModelId, ...] = ("bytedance/seedance/v1.5/pro/image-to-video", "bytedance/seedance/v1.5/pro/text-to-video", "bytedance/seedance/v1/lite/image-to-video", "bytedance/seedance/v1/lite/text-to-video", "bytedance/seedance/v1/pro/fast/text-to-video", "bytedance/seedance/v1/pro/image-to-video", "bytedance/seedance/v1/pro/text-to-video", "bytedance/seedance/v2/image-to-video", "bytedance/seedance/v2/text-to-video", "bytedance/seedream/v3/text-to-image", "bytedance/seedream/v4.5/text-to-image", "bytedance/seedream/v4/text-to-image", "bytedance/seedream/v5/lite/text-to-image", "bytedance/seedream/v5/text-to-image", "dreamactor-v2", "elevenlabs/sound-effect", "fish-audio/text-to-speech", "flux/v1/kontext/dev/edit", "flux/v1/kontext/max/edit", "flux/v1/kontext/pro/edit", "flux/v1/schnell/text-to-image", "flux/v2/dev/text-to-image", "flux/v2/flex/text-to-image", "flux/v2/pro/text-to-image", "glm/image/text-to-image", "google/gemini-3.1-flash/video-understanding", "google/gemini-3.1-pro/video-understanding", "google/nano-banana/edit", "google/nano-banana/pro/edit", "google/nano-banana/pro/text-to-image", "google/nano-banana/pro/vertex", "google/nano-banana/text-to-image", "google/nano-banana/v2/edit", "google/nano-banana/v2/text-to-image", "google/nano-banana/v2/vertex", "google/nano-banana/vertex", "google/veo/v3.1/first-last-frame-to-video", "google/veo/v3.1/image-to-video", "google/veo/v3.1/reference-to-video", "google/veo/v3.1/text-to-video", "heygen/video-translate", "hunyuan/image/v3/text-to-image", "hunyuan/video/fast/text-to-video", "kling/advanced-lip-sync", "kling/advanced-lip-sync/official", "kling/avatar/official", "kling/identify-face", "kling/identify-face/official", "kling/image-to-video", "kling/multi-image-to-video", "kling/o1/image-to-video", "kling/o1/text-to-video", "kling/o1/video-edit", "kling/o1/video-to-video", "kling/o3/4k/image-to-video", "kling/o3/4k/text-to-video", "kling/o3/pro/image-to-video", "kling/o3/pro/reference-to-video", "kling/o3/pro/reference-to-video@7-ref", "kling/o3/pro/text-to-video", "kling/o3/pro/video-edit", "kling/o3/pro/video-to-video", "kling/o3/standard/image-to-video", "kling/o3/standard/reference-to-video", "kling/o3/standard/reference-to-video@7-ref", "kling/o3/standard/text-to-video", "kling/o3/standard/video-edit", "kling/o3/standard/video-to-video", "kling/text-to-audio/official", "kling/text-to-video", "kling/v1.5/pro/image-to-video/official", "kling/v1.5/standard/image-to-video/official", "kling/v1.6/image-to-video", "kling/v1.6/pro/image-to-video/official", "kling/v1.6/pro/multi-image-to-video/official", "kling/v1.6/pro/text-to-video/official", "kling/v1.6/standard/image-to-video/official", "kling/v1.6/standard/multi-image-to-video/official", "kling/v1.6/standard/text-to-video/official", "kling/v1.6/text-to-video", "kling/v1/pro/image-to-video/official", "kling/v1/pro/text-to-video/official", "kling/v1/standard/image-to-video/official", "kling/v1/standard/text-to-video/official", "kling/v2-master/image-to-video/official", "kling/v2-master/text-to-video/official", "kling/v2.1-master/image-to-video/official", "kling/v2.1-master/text-to-video/official", "kling/v2.1/image-to-video", "kling/v2.1/master/image-to-video", "kling/v2.1/master/text-to-video", "kling/v2.1/pro/image-to-video/official", "kling/v2.1/standard/image-to-video/official", "kling/v2.5-turbo/pro/image-to-video/official", "kling/v2.5-turbo/pro/text-to-video/official", "kling/v2.5-turbo/standard/image-to-video/official", "kling/v2.5-turbo/standard/text-to-video/official", "kling/v2.5/turbo/image-to-video", "kling/v2.5/turbo/text-to-video", "kling/v2.6/pro/image-to-video", "kling/v2.6/pro/image-to-video/official", "kling/v2.6/pro/motion-control", "kling/v2.6/pro/motion-control/official", "kling/v2.6/pro/text-to-video", "kling/v2.6/pro/text-to-video/official", "kling/v2.6/standard/image-to-video/official", "kling/v2.6/standard/motion-control/official", "kling/v2.6/standard/text-to-video/official", "kling/v3-omni/4k/image-to-video/official", "kling/v3-omni/4k/text-to-video/official", "kling/v3-omni/pro/image-to-video/official", "kling/v3-omni/pro/reference-to-video@7-ref/official", "kling/v3-omni/pro/reference-to-video/official", "kling/v3-omni/pro/text-to-video/official", "kling/v3-omni/pro/video-edit/official", "kling/v3-omni/pro/video-to-video/official", "kling/v3-omni/standard/image-to-video/official", "kling/v3-omni/standard/reference-to-video@7-ref/official", "kling/v3-omni/standard/reference-to-video/official", "kling/v3-omni/standard/text-to-video/official", "kling/v3-omni/standard/video-edit/official", "kling/v3-omni/standard/video-to-video/official", "kling/v3.0/pro/image-to-video", "kling/v3.0/pro/text-to-video", "kling/v3.0/standard/image-to-video", "kling/v3.0/standard/text-to-video", "kling/v3/4k/image-to-video/official", "kling/v3/4k/text-to-video/official", "kling/v3/pro/image-to-video/official", "kling/v3/pro/motion-control/official", "kling/v3/pro/text-to-video/official", "kling/v3/standard/image-to-video/official", "kling/v3/standard/motion-control/official", "kling/v3/standard/text-to-video/official", "kling/video-effects/official", "kling/video-extension/official", "kling/video-o1/pro/image-to-video/official", "kling/video-o1/pro/text-to-video/official", "kling/video-o1/pro/video-edit/official", "kling/video-o1/pro/video-to-video/official", "kling/video-o1/standard/image-to-video/official", "kling/video-o1/standard/text-to-video/official", "kling/video-o1/standard/video-edit/official", "kling/video-o1/standard/video-to-video/official", "kling/video-to-audio/official", "minimax/hailuo/v2.3/fast/image-to-video", "minimax/hailuo/v2.3/image-to-video", "minimax/hailuo/v2.3/text-to-video", "minimax/hailuo/v2/image-to-video", "minimax/hailuo/v2/start-end-to-video", "minimax/hailuo/v2/text-to-video", "minimax/image/v1/live/image-to-image", "minimax/image/v1/text-to-image", "minimax/video-01/text-to-video", "novita/image-to-image", "novita/image-upscaler/upscale", "novita/image-upscaler/v2/upscale", "novita/image/background-removal", "novita/image/background-removal/v2", "novita/image/background-replacement", "novita/image/cleanup", "novita/image/erase", "novita/image/reimagine", "novita/image/text-removal", "novita/image/to-prompt", "novita/inpaint", "novita/text-to-image", "openai/gpt-image-2", "openai/gpt-image-2/edit", "pixverse/v4.5/image-to-video", "pixverse/v4.5/text-to-video", "qwen/image/edit", "qwen/image/text-to-image", "topaz/image/enhance", "topaz/image/enhance-gen", "topaz/image/tool", "video/face-swap", "vidu/q1/image-to-video", "vidu/q1/reference-to-video", "vidu/q1/start-end-to-video", "vidu/q1/text-to-video", "vidu/q2/pro/fast/image-to-video", "vidu/q2/pro/fast/start-end-to-video", "vidu/q2/pro/image-to-video", "vidu/q2/pro/multi-frame-to-video", "vidu/q2/pro/start-end-to-video", "vidu/q2/reference-to-video", "vidu/q2/template-to-video", "vidu/q2/text-to-video", "vidu/q2/turbo/image-to-video", "vidu/q2/turbo/multi-frame-to-video", "vidu/q2/turbo/start-end-to-video", "vidu/q3/pro/image-to-video", "vidu/q3/pro/text-to-video", "vidu/v2.0/image-to-video", "vidu/v2.0/reference-to-video", "vidu/v2.0/start-end-to-video", "vits-svc/voice-changer", "wan/image-to-video", "wan/text-to-video", "wan/v2.2/image-to-video", "wan/v2.2/text-to-video", "wan/v2.5/preview/image-to-video", "wan/v2.5/preview/text-to-video", "wan/v2.6/image-to-video", "wan/v2.6/text-to-video", "wan/v2.6/video-to-video", "wan/v2.7/edit", "wan/v2.7/extend-video", "wan/v2.7/image-to-video", "wan/v2.7/pro/edit", "wan/v2.7/pro/text-to-image", "wan/v2.7/reference-to-video", "wan/v2.7/text-to-image", "wan/v2.7/text-to-video", "wan/v2.7/video-edit", "wan2.2-animate-replace", "wan2.6-reference-to-video-flash", "youchuan/midjourney-v7-fast", "youchuan/midjourney-v7-turbo", "youchuan/midjourney-v7-upscale", "youchuan/midjourney-v7-variation", "z-image/turbo-lora/text-to-image", "z-image/turbo/text-to-image")
BUILT_IN_TASK_IDS: tuple[BuiltInTaskId, ...] = ("audio.kling.official.text_to_audio", "audio.kling.official.video_to_audio", "audio.sound_effect.generation", "audio.tts.generation", "audio.voice_changer.transform", "generate-content.google.gemini.video-understanding", "generate-content.google.vertex", "image.byteplus.seedream", "image.enhance", "image.generation", "image.google.generation", "image.minimax.generation", "image.novita.async_img2img", "image.novita.async_inpaint", "image.novita.async_txt2img", "image.novita.async_upscale", "image.novita.async_url", "image.novita.flux_schnell", "image.novita.generic", "image.novita.seedream.dual", "image.novita.seedream.sync", "image.novita.sync_edit", "image.openai.gpt-image-2.edit", "image.openai.gpt-image-2.generation", "image.wan_v27.edit", "image.wan_v27.text_to_image", "video.byteplus.generation", "video.face_merge", "video.generation", "video.google.generation", "video.google.reference_to_video", "video.hunyuan.fast_generation", "video.identify_face", "video.kling_o3.image_to_video", "video.kling_o3.reference_to_video", "video.kling_o3.reference_to_video_7_ref", "video.kling_o3.text_to_video", "video.kling_o3.video_edit", "video.kling_o3.video_to_video", "video.kling.image_to_video", "video.kling.multi_image_to_video", "video.kling.official.avatar", "video.kling.official.identify_face", "video.kling.official.image_to_video", "video.kling.official.lip_sync", "video.kling.official.motion_control", "video.kling.official.multi_image_to_video", "video.kling.official.omni.image_to_video", "video.kling.official.omni.reference_to_video", "video.kling.official.omni.text_to_video", "video.kling.official.omni.video_edit", "video.kling.official.omni.video_to_video", "video.kling.official.text_to_video", "video.kling.official.video_effects", "video.kling.official.video_extension", "video.kling.text_to_video", "video.lip_sync", "video.minimax.image_generation", "video.minimax.text_generation", "video.motion_control", "video.novita.image_generation", "video.novita.reference_image_generation_extra", "video.novita.text_generation", "video.reference_image_generation", "video.reference_video_generation", "video.translate", "video.video_edit", "video.wan_v27.extend_video", "video.wan_v27.image_to_video", "video.wan_v27.reference_to_video", "video.wan_v27.text_to_video", "video.wan_v27.video_edit", "video.wan.image_generation", "video.wan.reference_video_generation", "video.wan.text_generation", "video.wan.text_generation_flat", "video.wan.text_generation_with_loras", "youchuan.midjourney-v7.upscale", "youchuan.midjourney-v7.variation")

AudioKlingOfficialTextToAudioTaskInput = TypedDict(
    "AudioKlingOfficialTextToAudioTaskInput",
    {
    "prompt": Required[str],
    "duration": Required[int | float],
    },
    total=False,
)

AudioKlingOfficialVideoToAudioTaskInput = TypedDict(
    "AudioKlingOfficialVideoToAudioTaskInput",
    {
    "video_id": NotRequired[str],
    "video_url": NotRequired[str],
    "sound_effect_prompt": NotRequired[str],
    "bgm_prompt": NotRequired[str],
    "asmr_mode": NotRequired[bool],
    },
    total=False,
)

AudioSoundEffectGenerationTaskInput = TypedDict(
    "AudioSoundEffectGenerationTaskInput",
    {
    "mode": NotRequired[str],
    "text": Required[str],
    "output_format": NotRequired[str],
    "duration_seconds": NotRequired[int],
    "prompt_influence": NotRequired[int | float],
    "loop": NotRequired[bool],
    },
    total=False,
)

AudioTtsGenerationTaskInput = TypedDict(
    "AudioTtsGenerationTaskInput",
    {
    "mode": NotRequired[str],
    "text": Required[str],
    "voice_id": Required[str],
    "format": NotRequired[str],
    "normalize": NotRequired[bool],
    "prosody": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "top_p": NotRequired[int | float],
    "latency": NotRequired[str],
    "sample_rate": NotRequired[int],
    "persist_asset": NotRequired[bool],
    },
    total=False,
)

AudioVoiceChangerTransformTaskInput = TypedDict(
    "AudioVoiceChangerTransformTaskInput",
    {
    "mode": NotRequired[str],
    "source_audio_url": Required[str],
    "reference_audio_url": Required[str],
    "source_asset_id": NotRequired[str],
    "target_voice_id": NotRequired[str],
    "noise_scale": NotRequired[int | float],
    "dither_src": NotRequired[bool],
    "dither_ref": NotRequired[bool],
    "streaming": NotRequired[bool],
    "chunk_size": NotRequired[int],
    },
    total=False,
)

GenerateContentGoogleGeminiVideoUnderstandingTaskInput = TypedDict(
    "GenerateContentGoogleGeminiVideoUnderstandingTaskInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    },
    total=False,
)

GenerateContentGoogleVertexTaskInput = TypedDict(
    "GenerateContentGoogleVertexTaskInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "topP": NotRequired[int | float],
    "topK": NotRequired[int],
    "maxOutputTokens": NotRequired[int],
    "seed": NotRequired[int],
    "candidateCount": NotRequired[int],
    "stopSequences": NotRequired[list[str]],
    "presencePenalty": NotRequired[int | float],
    "frequencyPenalty": NotRequired[int | float],
    "responseModalities": NotRequired[list[Literal["TEXT", "IMAGE"]]],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "responseLogprobs": NotRequired[bool],
    "logprobs": NotRequired[int],
    "aspectRatio": NotRequired[Literal["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]],
    "imageSize": NotRequired[Literal["1K", "2K", "4K"]],
    "searchMode": NotRequired[Literal["none", "web"]],
    "safetySettings": NotRequired[list[dict[str, JsonValue]]],
    "thinkingConfig": NotRequired[dict[str, JsonValue]],
    "toolConfig": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    "serviceTier": NotRequired[Literal["standard", "flex", "priority"]],
    },
    total=False,
)

ImageByteplusSeedreamTaskInput = TypedDict(
    "ImageByteplusSeedreamTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "watermark": NotRequired[bool],
    "reference_assets": NotRequired[list[ReferenceAsset]],
    },
    total=False,
)

ImageEnhanceTaskInput = TypedDict(
    "ImageEnhanceTaskInput",
    {
    "mode": NotRequired[Literal["enhance", "enhance-gen", "restore-gen", "tool"]],
    "model_name": NotRequired[Literal["Standard V2", "High Fidelity V2", "Low Resolution 2", "Art & CGI", "Text & Shapes", "Detail Faces", "Recover Faces", "Transparent Image Upscale"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "output_width": NotRequired[int],
    "output_height": NotRequired[int],
    "face_enhancement": NotRequired[bool],
    "face_enhancement_strength": NotRequired[int | float],
    "face_enhancement_creativity": NotRequired[int | float],
    "sharpen": NotRequired[int | float],
    "denoise": NotRequired[int | float],
    "fix_compression": NotRequired[int | float],
    "strength": NotRequired[int | float],
    "subject_detection": NotRequired[Literal["foreground", "background", "all"]],
    "prompt": NotRequired[str],
    "creativity": NotRequired[int],
    "texture": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageGenerationTaskInput = TypedDict(
    "ImageGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    },
    total=False,
)

ImageGoogleGenerationTaskInput = TypedDict(
    "ImageGoogleGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

ImageMinimaxGenerationTaskInput = TypedDict(
    "ImageMinimaxGenerationTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["1:1", "16:9", "4:3", "3:2", "2:3", "3:4", "9:16", "21:9"]],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

ImageNovitaAsyncImg2imgTaskInput = TypedDict(
    "ImageNovitaAsyncImg2imgTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageNovitaAsyncInpaintTaskInput = TypedDict(
    "ImageNovitaAsyncInpaintTaskInput",
    {
    "mode": NotRequired[Literal["inpaint"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageNovitaAsyncTxt2imgTaskInput = TypedDict(
    "ImageNovitaAsyncTxt2imgTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[str],
    "image_size": NotRequired[str],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    },
    total=False,
)

ImageNovitaAsyncUpscaleTaskInput = TypedDict(
    "ImageNovitaAsyncUpscaleTaskInput",
    {
    "mode": NotRequired[Literal["upscale"]],
    "model_name": NotRequired[str],
    "scale_factor": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageNovitaAsyncUrlTaskInput = TypedDict(
    "ImageNovitaAsyncUrlTaskInput",
    {
    "mode": NotRequired[Literal["upscale"]],
    "resolution": NotRequired[Literal["2k", "4k", "8k"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageNovitaFluxSchnellTaskInput = TypedDict(
    "ImageNovitaFluxSchnellTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "response_image_format": NotRequired[Literal["jpeg", "png", "webp"]],
    },
    total=False,
)

ImageNovitaGenericTaskInput = TypedDict(
    "ImageNovitaGenericTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

ImageNovitaSeedreamDualTaskInput = TypedDict(
    "ImageNovitaSeedreamDualTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "watermark": NotRequired[bool],
    "optimize_prompt_options": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

ImageNovitaSeedreamSyncTaskInput = TypedDict(
    "ImageNovitaSeedreamSyncTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "model": NotRequired[str],
    "watermark": NotRequired[bool],
    },
    total=False,
)

ImageNovitaSyncEditTaskInput = TypedDict(
    "ImageNovitaSyncEditTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageOpenaiGptImage2EditTaskInput = TypedDict(
    "ImageOpenaiGptImage2EditTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "quality": NotRequired[Literal["low", "medium", "high"]],
    "num_images": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageOpenaiGptImage2GenerationTaskInput = TypedDict(
    "ImageOpenaiGptImage2GenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "quality": NotRequired[Literal["low", "medium", "high"]],
    "num_images": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    },
    total=False,
)

ImageWanV27EditTaskInput = TypedDict(
    "ImageWanV27EditTaskInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "num_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ImageWanV27TextToImageTaskInput = TypedDict(
    "ImageWanV27TextToImageTaskInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "max_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_safety_checker": NotRequired[bool],
    },
    total=False,
)

VideoByteplusGenerationTaskInput = TypedDict(
    "VideoByteplusGenerationTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video", "reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "return_last_frame": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoFaceMergeTaskInput = TypedDict(
    "VideoFaceMergeTaskInput",
    {
    "reference_assets": Required[list[ReferenceAsset]],
    "enable_restore": NotRequired[bool],
    "enable_occlusion_prevention": NotRequired[bool],
    "response_video_type": NotRequired[Literal["mp4", "gif"]],
    },
    total=False,
)

VideoGenerationTaskInput = TypedDict(
    "VideoGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p"]],
    "size": NotRequired[str],
    "ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9", "adaptive"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[Literal[24]],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoGoogleGenerationTaskInput = TypedDict(
    "VideoGoogleGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 6, 8]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "seed": NotRequired[int],
    "reference_audio_url": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoGoogleReferenceToVideoTaskInput = TypedDict(
    "VideoGoogleReferenceToVideoTaskInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoHunyuanFastGenerationTaskInput = TypedDict(
    "VideoHunyuanFastGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "duration": NotRequired[Literal[5]],
    },
    total=False,
)

VideoIdentifyFaceTaskInput = TypedDict(
    "VideoIdentifyFaceTaskInput",
    {
    "mode": NotRequired[Literal["identify-face"]],
    "video_url": NotRequired[str],
    "video_id": NotRequired[str],
    },
    total=False,
)

VideoKlingO3ImageToVideoTaskInput = TypedDict(
    "VideoKlingO3ImageToVideoTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingO3ReferenceToVideoTaskInput = TypedDict(
    "VideoKlingO3ReferenceToVideoTaskInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingO3ReferenceToVideo7RefTaskInput = TypedDict(
    "VideoKlingO3ReferenceToVideo7RefTaskInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingO3TextToVideoTaskInput = TypedDict(
    "VideoKlingO3TextToVideoTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    },
    total=False,
)

VideoKlingO3VideoEditTaskInput = TypedDict(
    "VideoKlingO3VideoEditTaskInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingO3VideoToVideoTaskInput = TypedDict(
    "VideoKlingO3VideoToVideoTaskInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingImageToVideoTaskInput = TypedDict(
    "VideoKlingImageToVideoTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "model_name": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "mode_strategy": NotRequired[Literal["pro", "4k"]],
    "duration": NotRequired[str],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "watermark_enabled": NotRequired[bool],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingMultiImageToVideoTaskInput = TypedDict(
    "VideoKlingMultiImageToVideoTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "model_name": Required[str],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "mode_strategy": NotRequired[Literal["std", "pro"]],
    "duration": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "watermark_enabled": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoKlingOfficialAvatarTaskInput = TypedDict(
    "VideoKlingOfficialAvatarTaskInput",
    {
    "image": Required[str],
    "audio_id": NotRequired[str],
    "sound_file": NotRequired[str],
    "prompt": NotRequired[str],
    "mode": NotRequired[Literal["std", "pro"]],
    },
    total=False,
)

VideoKlingOfficialIdentifyFaceTaskInput = TypedDict(
    "VideoKlingOfficialIdentifyFaceTaskInput",
    {
    "video_url": NotRequired[str],
    "video_id": NotRequired[str],
    },
    total=False,
)

VideoKlingOfficialImageToVideoTaskInput = TypedDict(
    "VideoKlingOfficialImageToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialLipSyncTaskInput = TypedDict(
    "VideoKlingOfficialLipSyncTaskInput",
    {
    "session_id": Required[str],
    "face_choose": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialMotionControlTaskInput = TypedDict(
    "VideoKlingOfficialMotionControlTaskInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image_url": Required[str],
    "video_url": Required[str],
    "prompt": NotRequired[str],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[Literal["yes", "no"]],
    },
    total=False,
)

VideoKlingOfficialMultiImageToVideoTaskInput = TypedDict(
    "VideoKlingOfficialMultiImageToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal["5", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialOmniImageToVideoTaskInput = TypedDict(
    "VideoKlingOfficialOmniImageToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialOmniReferenceToVideoTaskInput = TypedDict(
    "VideoKlingOfficialOmniReferenceToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialOmniTextToVideoTaskInput = TypedDict(
    "VideoKlingOfficialOmniTextToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

VideoKlingOfficialOmniVideoEditTaskInput = TypedDict(
    "VideoKlingOfficialOmniVideoEditTaskInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialOmniVideoToVideoTaskInput = TypedDict(
    "VideoKlingOfficialOmniVideoToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoKlingOfficialTextToVideoTaskInput = TypedDict(
    "VideoKlingOfficialTextToVideoTaskInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

VideoKlingOfficialVideoEffectsTaskInput = TypedDict(
    "VideoKlingOfficialVideoEffectsTaskInput",
    {
    "effect_scene": Required[Literal["palm_sized_figure_pro", "prank_box", "perler_beads", "spring_bloom", "toss_run", "switch_to_silk", "get_rich_quick", "make_it_rain", "twist_shake", "the_hip_sway", "send_my_love", "funky_martian", "wealth_drive", "the_high_kick", "the_exercise", "lucky_veggie", "studio_look", "flash_drive", "shush_my_dreams", "french_elegance", "finger_swipe", "advent_of_flora", "smooth_transition", "kiss_pro", "raid_check", "snow_night_kiss", "eternal_kiss", "fortune_in_motion", "chinese_trend", "sedan_chair_dance", "skyfall", "good_luck_dance", "laicai_dance", "yangge_dance", "color_mixing", "palm_sized_figure", "lantern_festival_cuju", "unique_firework", "unique_spring_couplets", "horse_mask", "fortune_knocks_cartoon", "tangyuan_to_animal", "hot_feet_dance", "swag_dance", "pigeon_dance", "bloodline_dance", "chanel_dance", "cute_dance", "love_theme_song", "pumpitup_dance", "city_to_village", "fortune_god_transform", "new_year_feast", "ring_in_new", "horse_year_firework", "pet_vlogger", "crystal_horse", "lateral_shift_transition", "drunk_dance", "drunk_dance_pet", "daoma_dance", "bouncy_dance", "smooth_sailing_dance", "new_year_greeting", "lion_dance", "prosperity", "great_success", "golden_horse_fortune", "red_packet_box", "lucky_horse_year", "lucky_red_packet", "lucky_money_come", "lion_dance_pet", "dumpling_making_pet", "fish_making_pet", "pet_red_packet", "lantern_glow", "expression_challenge", "overdrive", "heart_gesture_dance", "poping", "martial_arts", "running", "nezha", "motorcycle_dance", "subject_3_dance", "ghost_step_dance", "phantom_jewel", "zoom_out", "cheers_2026", "fight_pro", "hug_pro", "heart_gesture_pro", "dollar_rain_pro", "pet_bee_pro", "countdown_teleport", "santa_random_surprise", "magic_match_tree", "bullet_time_360", "happy_birthday", "birthday_star", "thumbs_up_pro", "tiger_hug_pro", "pet_lion_pro", "surprise_bouquet", "bouquet_drop", "3d_cartoon_1_pro", "firework_2026", "glamour_photo_shoot", "box_of_joy", "first_toast_of_the_year", "my_santa_pic", "santa_gift", "steampunk_christmas", "snowglobe", "christmas_photo_shoot", "ornament_crash", "santa_express", "instant_christmas", "particle_santa_surround", "coronation_of_frost", "building_sweater", "spark_in_the_snow", "scarlet_and_snow", "cozy_toon_wrap", "bullet_time_lite", "magic_cloak", "balloon_parade", "jumping_ginger_joy", "bullet_time", "c4d_cartoon_pro", "pure_white_wings", "black_wings", "golden_wing", "pink_pink_wings", "venomous_spider", "throne_of_king", "luminous_elf", "woodland_elf", "japanese_anime_1", "american_comics", "guardian_spirit", "swish_swish", "snowboarding", "witch_transform", "vampire_transform", "pumpkin_head_transform", "demon_transform", "mummy_transform", "zombie_transform", "cute_pumpkin_transform", "cute_ghost_transform", "knock_knock_halloween", "halloween_escape", "baseball", "inner_voice", "a_list_look", "memory_alive", "trampoline", "trampoline_night", "pucker_up", "guess_what", "feed_mooncake", "rampage_ape", "flyer", "dishwasher", "pet_chinese_opera", "magic_fireball", "gallery_ring", "pet_moto_rider", "muscle_pet", "squeeze_scream", "pet_delivery", "running_man", "disappear", "mythic_style", "steampunk", "3d_cartoon_2", "eagle_snatch", "hug_from_past", "firework", "media_interview", "pet_chef", "santa_gifts", "santa_hug", "heart_gesture_1", "pet_wizard", "smoke_smoke", "instant_kid", "dollar_rain", "cry_cry", "building_collapse", "gun_shot", "mushroom", "double_gun", "pet_warrior", "lightning_power", "jesus_hug", "shark_alert", "long_hair", "lie_flat", "polar_bear_hug", "brown_bear_hug", "jazz_jazz", "office_escape_plow", "fly_fly", "watermelon_bomb", "pet_dance", "boss_coming", "wool_curly", "pet_bee", "marry_me", "swing_swing", "day_to_night", "piggy_morph", "wig_out", "car_explosion", "ski_ski", "siblings", "construction_worker", "let’s_ride", "snatched", "magic_broom", "felt_felt", "jumpdrop", "surfsurf", "fairy_wing", "angel_wing", "dark_wing", "skateskate", "plushcut", "jelly_press", "jelly_slice", "jelly_squish", "jelly_jiggle", "pixelpixel", "yearbook", "instant_film", "anime_figure", "rocketrocket", "bloombloom", "dizzydizzy", "fuzzyfuzzy", "squish", "expansion", "emoji"]],
    "input": Required[dict[str, JsonValue]],
    },
    total=False,
)

VideoKlingOfficialVideoExtensionTaskInput = TypedDict(
    "VideoKlingOfficialVideoExtensionTaskInput",
    {
    "video_id": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    },
    total=False,
)

VideoKlingTextToVideoTaskInput = TypedDict(
    "VideoKlingTextToVideoTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "model_name": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "mode_strategy": NotRequired[Literal["pro", "4k"]],
    "aspect_ratio": NotRequired[str],
    "duration": NotRequired[str],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "watermark_enabled": NotRequired[bool],
    },
    total=False,
)

VideoLipSyncTaskInput = TypedDict(
    "VideoLipSyncTaskInput",
    {
    "mode": NotRequired[Literal["lip-sync"]],
    "session_id": Required[str],
    "face_choose": Required[list[dict[str, JsonValue]]],
    "watermark_enabled": NotRequired[bool],
    },
    total=False,
)

VideoMinimaxImageGenerationTaskInput = TypedDict(
    "VideoMinimaxImageGenerationTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["512P", "768P", "1080P"]],
    "size": NotRequired[str],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoMinimaxTextGenerationTaskInput = TypedDict(
    "VideoMinimaxTextGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "size": NotRequired[str],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": NotRequired[list[ReferenceAsset]],
    },
    total=False,
)

VideoMotionControlTaskInput = TypedDict(
    "VideoMotionControlTaskInput",
    {
    "mode": NotRequired[Literal["motion-control"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoNovitaImageGenerationTaskInput = TypedDict(
    "VideoNovitaImageGenerationTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[str],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "fps": NotRequired[Literal[24]],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoNovitaReferenceImageGenerationExtraTaskInput = TypedDict(
    "VideoNovitaReferenceImageGenerationExtraTaskInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["1080p"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoNovitaTextGenerationTaskInput = TypedDict(
    "VideoNovitaTextGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

VideoReferenceImageGenerationTaskInput = TypedDict(
    "VideoReferenceImageGenerationTaskInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "resolution": NotRequired[Literal["1080p"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoReferenceVideoGenerationTaskInput = TypedDict(
    "VideoReferenceVideoGenerationTaskInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "resolution": NotRequired[str],
    "size": NotRequired[str],
    "seed": NotRequired[int],
    "keep_original_sound": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoTranslateTaskInput = TypedDict(
    "VideoTranslateTaskInput",
    {
    "mode": NotRequired[Literal["video-translate"]],
    "output_language": Required[Literal["English", "English (Australia)", "English (India)", "English (UK)", "English (US)", "Spanish", "Spanish (Mexico)", "Spanish (Spain)", "French", "French (Canada)", "French (France)", "Hindi", "Italian", "German", "Polish", "Portuguese", "Portuguese (Brazil)", "Portuguese (Portugal)", "Chinese", "Chinese (Cantonese, Traditional)", "Chinese (Mandarin, Simplified)", "Chinese (Mandarin, Traditional)", "Japanese", "Dutch", "Turkish", "Korean", "Danish", "Arabic", "Romanian", "Mandarin", "Filipino", "Swedish", "Indonesian", "Ukrainian", "Greek", "Czech", "Bulgarian", "Malay", "Slovak", "Croatian", "Tamil", "Finnish", "Russian"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoVideoEditTaskInput = TypedDict(
    "VideoVideoEditTaskInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "turbo_mode": NotRequired[bool],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanV27ExtendVideoTaskInput = TypedDict(
    "VideoWanV27ExtendVideoTaskInput",
    {
    "mode": NotRequired[Literal["extend-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanV27ImageToVideoTaskInput = TypedDict(
    "VideoWanV27ImageToVideoTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanV27ReferenceToVideoTaskInput = TypedDict(
    "VideoWanV27ReferenceToVideoTaskInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "multi_shots": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanV27TextToVideoTaskInput = TypedDict(
    "VideoWanV27TextToVideoTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    },
    total=False,
)

VideoWanV27VideoEditTaskInput = TypedDict(
    "VideoWanV27VideoEditTaskInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "audio_setting": NotRequired[Literal["auto", "origin"]],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[0, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanImageGenerationTaskInput = TypedDict(
    "VideoWanImageGenerationTaskInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "resolution": NotRequired[Literal["480P", "720P", "1080P"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanReferenceVideoGenerationTaskInput = TypedDict(
    "VideoWanReferenceVideoGenerationTaskInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "duration": Required[Literal[5, 10]],
    "aspect_ratio": NotRequired[str],
    "size": NotRequired[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "seed": NotRequired[int],
    "keep_original_sound": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoWanTextGenerationTaskInput = TypedDict(
    "VideoWanTextGenerationTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "size": NotRequired[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "960*960", "1088*832", "832*1088", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    },
    total=False,
)

VideoWanTextGenerationFlatTaskInput = TypedDict(
    "VideoWanTextGenerationFlatTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "width": NotRequired[Literal[480, 720, 832, 1280]],
    "height": NotRequired[Literal[480, 720, 832, 1280]],
    "num_inference_steps": NotRequired[int],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "flow_shift": NotRequired[int | float],
    "enable_safety_checker": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "loras": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

VideoWanTextGenerationWithLorasTaskInput = TypedDict(
    "VideoWanTextGenerationWithLorasTaskInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 8]],
    "size": Required[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "loras": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

YouchuanMidjourneyV7UpscaleTaskInput = TypedDict(
    "YouchuanMidjourneyV7UpscaleTaskInput",
    {
    "parent_task_id": Required[str],
    "image_index": Required[int],
    "type": NotRequired[Literal[0, 1, 2, 3]],
    },
    total=False,
)

YouchuanMidjourneyV7VariationTaskInput = TypedDict(
    "YouchuanMidjourneyV7VariationTaskInput",
    {
    "task_id": Required[str],
    "image_no": Required[int],
    "variation_type": NotRequired[Literal[0, 1]],
    "remix_prompt": NotRequired[str],
    },
    total=False,
)

BytedanceSeedanceV15ProImageToVideoInput = TypedDict(
    "BytedanceSeedanceV15ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p"]],
    "size": NotRequired[str],
    "ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9", "adaptive"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[Literal[24]],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

BytedanceSeedanceV15ProTextToVideoInput = TypedDict(
    "BytedanceSeedanceV15ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p"]],
    "size": NotRequired[str],
    "ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9", "adaptive"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[Literal[24]],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    },
    total=False,
)

BytedanceSeedanceV1LiteImageToVideoInput = TypedDict(
    "BytedanceSeedanceV1LiteImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video", "reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "return_last_frame": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

BytedanceSeedanceV1LiteTextToVideoInput = TypedDict(
    "BytedanceSeedanceV1LiteTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": Required[Literal[5, 10]],
    "resolution": Required[Literal["480p", "720p", "1080p"]],
    "size": NotRequired[str],
    "ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    },
    total=False,
)

BytedanceSeedanceV1ProFastTextToVideoInput = TypedDict(
    "BytedanceSeedanceV1ProFastTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video", "reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "return_last_frame": NotRequired[bool],
    },
    total=False,
)

BytedanceSeedanceV1ProImageToVideoInput = TypedDict(
    "BytedanceSeedanceV1ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p"]],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[str],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "fps": NotRequired[Literal[24]],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

BytedanceSeedanceV1ProTextToVideoInput = TypedDict(
    "BytedanceSeedanceV1ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video", "reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "ratio": NotRequired[Literal["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]],
    "return_last_frame": NotRequired[bool],
    },
    total=False,
)

BytedanceSeedanceV2ImageToVideoInput = TypedDict(
    "BytedanceSeedanceV2ImageToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "4:3", "3:4", "1:1", "21:9", "adaptive"]],
    "generate_audio": NotRequired[bool],
    "reference_audio_url": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

BytedanceSeedanceV2TextToVideoInput = TypedDict(
    "BytedanceSeedanceV2TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "4:3", "3:4", "1:1", "21:9", "adaptive"]],
    "generate_audio": NotRequired[bool],
    "reference_audio_url": NotRequired[str],
    "reference_assets": NotRequired[list[ReferenceAsset]],
    },
    total=False,
)

BytedanceSeedreamV3TextToImageInput = TypedDict(
    "BytedanceSeedreamV3TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "model": NotRequired[str],
    "watermark": NotRequired[bool],
    },
    total=False,
)

BytedanceSeedreamV45TextToImageInput = TypedDict(
    "BytedanceSeedreamV45TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "watermark": NotRequired[bool],
    "optimize_prompt_options": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

BytedanceSeedreamV4TextToImageInput = TypedDict(
    "BytedanceSeedreamV4TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "watermark": NotRequired[bool],
    "optimize_prompt_options": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

BytedanceSeedreamV5LiteTextToImageInput = TypedDict(
    "BytedanceSeedreamV5LiteTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "watermark": NotRequired[bool],
    "optimize_prompt_options": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

BytedanceSeedreamV5TextToImageInput = TypedDict(
    "BytedanceSeedreamV5TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "watermark": NotRequired[bool],
    "reference_assets": NotRequired[list[ReferenceAsset]],
    },
    total=False,
)

DreamactorV2Input = TypedDict(
    "DreamactorV2Input",
    {
    "mode": NotRequired[Literal["motion-control"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ElevenlabsSoundEffectInput = TypedDict(
    "ElevenlabsSoundEffectInput",
    {
    "mode": NotRequired[str],
    "text": Required[str],
    "output_format": NotRequired[str],
    "duration_seconds": NotRequired[int],
    "prompt_influence": NotRequired[int | float],
    "loop": NotRequired[bool],
    },
    total=False,
)

FishAudioTextToSpeechInput = TypedDict(
    "FishAudioTextToSpeechInput",
    {
    "mode": NotRequired[str],
    "text": Required[str],
    "voice_id": Required[str],
    "format": NotRequired[str],
    "normalize": NotRequired[bool],
    "prosody": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "top_p": NotRequired[int | float],
    "latency": NotRequired[str],
    "sample_rate": NotRequired[int],
    "persist_asset": NotRequired[bool],
    },
    total=False,
)

FluxV1KontextDevEditInput = TypedDict(
    "FluxV1KontextDevEditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

FluxV1KontextMaxEditInput = TypedDict(
    "FluxV1KontextMaxEditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

FluxV1KontextProEditInput = TypedDict(
    "FluxV1KontextProEditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

FluxV1SchnellTextToImageInput = TypedDict(
    "FluxV1SchnellTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "response_image_format": NotRequired[Literal["jpeg", "png", "webp"]],
    },
    total=False,
)

FluxV2DevTextToImageInput = TypedDict(
    "FluxV2DevTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

FluxV2FlexTextToImageInput = TypedDict(
    "FluxV2FlexTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

FluxV2ProTextToImageInput = TypedDict(
    "FluxV2ProTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GlmImageTextToImageInput = TypedDict(
    "GlmImageTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleGemini31FlashVideoUnderstandingInput = TypedDict(
    "GoogleGemini31FlashVideoUnderstandingInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    },
    total=False,
)

GoogleGemini31ProVideoUnderstandingInput = TypedDict(
    "GoogleGemini31ProVideoUnderstandingInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    },
    total=False,
)

GoogleNanoBananaEditInput = TypedDict(
    "GoogleNanoBananaEditInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaProEditInput = TypedDict(
    "GoogleNanoBananaProEditInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]],
    "image_size": NotRequired[Literal["1K", "2K", "4K"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaProTextToImageInput = TypedDict(
    "GoogleNanoBananaProTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]],
    "image_size": NotRequired[Literal["1K", "2K", "4K"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaProVertexInput = TypedDict(
    "GoogleNanoBananaProVertexInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "topP": NotRequired[int | float],
    "topK": NotRequired[int],
    "maxOutputTokens": NotRequired[int],
    "seed": NotRequired[int],
    "candidateCount": NotRequired[int],
    "stopSequences": NotRequired[list[str]],
    "presencePenalty": NotRequired[int | float],
    "frequencyPenalty": NotRequired[int | float],
    "responseModalities": NotRequired[list[Literal["TEXT", "IMAGE"]]],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "responseLogprobs": NotRequired[bool],
    "logprobs": NotRequired[int],
    "aspectRatio": NotRequired[Literal["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]],
    "imageSize": NotRequired[Literal["1K", "2K", "4K"]],
    "searchMode": NotRequired[Literal["none", "web"]],
    "safetySettings": NotRequired[list[dict[str, JsonValue]]],
    "thinkingConfig": NotRequired[dict[str, JsonValue]],
    "toolConfig": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    "serviceTier": NotRequired[Literal["standard", "flex", "priority"]],
    },
    total=False,
)

GoogleNanoBananaTextToImageInput = TypedDict(
    "GoogleNanoBananaTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaV2EditInput = TypedDict(
    "GoogleNanoBananaV2EditInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16", "4:1", "1:4", "8:1", "1:8"]],
    "image_size": NotRequired[Literal["0.5K", "1K", "2K", "4K"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaV2TextToImageInput = TypedDict(
    "GoogleNanoBananaV2TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16", "4:1", "1:4", "8:1", "1:8"]],
    "image_size": NotRequired[Literal["0.5K", "1K", "2K", "4K"]],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GoogleNanoBananaV2VertexInput = TypedDict(
    "GoogleNanoBananaV2VertexInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "topP": NotRequired[int | float],
    "topK": NotRequired[int],
    "maxOutputTokens": NotRequired[int],
    "seed": NotRequired[int],
    "candidateCount": NotRequired[int],
    "stopSequences": NotRequired[list[str]],
    "presencePenalty": NotRequired[int | float],
    "frequencyPenalty": NotRequired[int | float],
    "responseModalities": NotRequired[list[Literal["TEXT", "IMAGE"]]],
    "responseLogprobs": NotRequired[bool],
    "logprobs": NotRequired[int],
    "aspectRatio": NotRequired[Literal["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9", "1:4", "1:8", "4:1", "8:1"]],
    "imageSize": NotRequired[Literal["512", "1K", "2K", "4K"]],
    "searchMode": NotRequired[Literal["none", "web", "web+image"]],
    "safetySettings": NotRequired[list[dict[str, JsonValue]]],
    "thinkingConfig": NotRequired[dict[str, JsonValue]],
    "toolConfig": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    "serviceTier": NotRequired[Literal["standard", "flex", "priority"]],
    },
    total=False,
)

GoogleNanoBananaVertexInput = TypedDict(
    "GoogleNanoBananaVertexInput",
    {
    "messages": Required[list[dict[str, JsonValue]]],
    "systemInstruction": NotRequired[dict[str, JsonValue]],
    "temperature": NotRequired[int | float],
    "topP": NotRequired[int | float],
    "topK": NotRequired[int],
    "maxOutputTokens": NotRequired[int],
    "seed": NotRequired[int],
    "candidateCount": NotRequired[int],
    "stopSequences": NotRequired[list[str]],
    "presencePenalty": NotRequired[int | float],
    "frequencyPenalty": NotRequired[int | float],
    "responseModalities": NotRequired[list[Literal["TEXT", "IMAGE"]]],
    "responseMimeType": NotRequired[Literal["text/plain", "application/json", "text/x.enum"]],
    "responseSchema": NotRequired[dict[str, JsonValue]],
    "responseLogprobs": NotRequired[bool],
    "logprobs": NotRequired[int],
    "aspectRatio": NotRequired[Literal["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]],
    "safetySettings": NotRequired[list[dict[str, JsonValue]]],
    "thinkingConfig": NotRequired[dict[str, JsonValue]],
    "toolConfig": NotRequired[dict[str, JsonValue]],
    "mediaResolution": NotRequired[Literal["LOW", "MEDIUM", "HIGH"]],
    "cachedContent": NotRequired[str],
    "serviceTier": NotRequired[Literal["standard", "flex", "priority"]],
    },
    total=False,
)

GoogleVeoV31FirstLastFrameToVideoInput = TypedDict(
    "GoogleVeoV31FirstLastFrameToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 6, 8]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "seed": NotRequired[int],
    "reference_audio_url": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

GoogleVeoV31ImageToVideoInput = TypedDict(
    "GoogleVeoV31ImageToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 6, 8]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "seed": NotRequired[int],
    "reference_audio_url": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

GoogleVeoV31ReferenceToVideoInput = TypedDict(
    "GoogleVeoV31ReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[int],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

GoogleVeoV31TextToVideoInput = TypedDict(
    "GoogleVeoV31TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video", "image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 6, 8]],
    "resolution": NotRequired[Literal["720p", "1080p", "4k"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "seed": NotRequired[int],
    "reference_audio_url": NotRequired[str],
    },
    total=False,
)

HeygenVideoTranslateInput = TypedDict(
    "HeygenVideoTranslateInput",
    {
    "mode": NotRequired[Literal["video-translate"]],
    "output_language": Required[Literal["English", "English (Australia)", "English (India)", "English (UK)", "English (US)", "Spanish", "Spanish (Mexico)", "Spanish (Spain)", "French", "French (Canada)", "French (France)", "Hindi", "Italian", "German", "Polish", "Portuguese", "Portuguese (Brazil)", "Portuguese (Portugal)", "Chinese", "Chinese (Cantonese, Traditional)", "Chinese (Mandarin, Simplified)", "Chinese (Mandarin, Traditional)", "Japanese", "Dutch", "Turkish", "Korean", "Danish", "Arabic", "Romanian", "Mandarin", "Filipino", "Swedish", "Indonesian", "Ukrainian", "Greek", "Czech", "Bulgarian", "Malay", "Slovak", "Croatian", "Tamil", "Finnish", "Russian"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

HunyuanImageV3TextToImageInput = TypedDict(
    "HunyuanImageV3TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

HunyuanVideoFastTextToVideoInput = TypedDict(
    "HunyuanVideoFastTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16"]],
    "duration": NotRequired[Literal[5]],
    },
    total=False,
)

KlingAdvancedLipSyncInput = TypedDict(
    "KlingAdvancedLipSyncInput",
    {
    "mode": NotRequired[Literal["lip-sync"]],
    "session_id": Required[str],
    "face_choose": Required[list[dict[str, JsonValue]]],
    "watermark_enabled": NotRequired[bool],
    },
    total=False,
)

KlingAdvancedLipSyncOfficialInput = TypedDict(
    "KlingAdvancedLipSyncOfficialInput",
    {
    "session_id": Required[str],
    "face_choose": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingAvatarOfficialInput = TypedDict(
    "KlingAvatarOfficialInput",
    {
    "image": Required[str],
    "audio_id": NotRequired[str],
    "sound_file": NotRequired[str],
    "prompt": NotRequired[str],
    "mode": NotRequired[Literal["std", "pro"]],
    },
    total=False,
)

KlingIdentifyFaceInput = TypedDict(
    "KlingIdentifyFaceInput",
    {
    "mode": NotRequired[Literal["identify-face"]],
    "video_url": NotRequired[str],
    "video_id": NotRequired[str],
    },
    total=False,
)

KlingIdentifyFaceOfficialInput = TypedDict(
    "KlingIdentifyFaceOfficialInput",
    {
    "video_url": NotRequired[str],
    "video_id": NotRequired[str],
    },
    total=False,
)

KlingImageToVideoInput = TypedDict(
    "KlingImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "model_name": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "mode_strategy": NotRequired[Literal["pro", "4k"]],
    "duration": NotRequired[str],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "watermark_enabled": NotRequired[bool],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingMultiImageToVideoInput = TypedDict(
    "KlingMultiImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "model_name": Required[str],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "mode_strategy": NotRequired[Literal["std", "pro"]],
    "duration": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "watermark_enabled": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO1ImageToVideoInput = TypedDict(
    "KlingO1ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO1TextToVideoInput = TypedDict(
    "KlingO1TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingO1VideoEditInput = TypedDict(
    "KlingO1VideoEditInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "turbo_mode": NotRequired[bool],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO1VideoToVideoInput = TypedDict(
    "KlingO1VideoToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "resolution": NotRequired[str],
    "size": NotRequired[str],
    "seed": NotRequired[int],
    "keep_original_sound": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO34kImageToVideoInput = TypedDict(
    "KlingO34kImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO34kTextToVideoInput = TypedDict(
    "KlingO34kTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    },
    total=False,
)

KlingO3ProImageToVideoInput = TypedDict(
    "KlingO3ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3ProReferenceToVideoInput = TypedDict(
    "KlingO3ProReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3ProReferenceToVideoAt7RefInput = TypedDict(
    "KlingO3ProReferenceToVideoAt7RefInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3ProTextToVideoInput = TypedDict(
    "KlingO3ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    },
    total=False,
)

KlingO3ProVideoEditInput = TypedDict(
    "KlingO3ProVideoEditInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3ProVideoToVideoInput = TypedDict(
    "KlingO3ProVideoToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3StandardImageToVideoInput = TypedDict(
    "KlingO3StandardImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3StandardReferenceToVideoInput = TypedDict(
    "KlingO3StandardReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3StandardReferenceToVideoAt7RefInput = TypedDict(
    "KlingO3StandardReferenceToVideoAt7RefInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3StandardTextToVideoInput = TypedDict(
    "KlingO3StandardTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": NotRequired[str],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "generate_audio": NotRequired[bool],
    },
    total=False,
)

KlingO3StandardVideoEditInput = TypedDict(
    "KlingO3StandardVideoEditInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingO3StandardVideoToVideoInput = TypedDict(
    "KlingO3StandardVideoToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingTextToAudioOfficialInput = TypedDict(
    "KlingTextToAudioOfficialInput",
    {
    "prompt": Required[str],
    "duration": Required[int | float],
    },
    total=False,
)

KlingTextToVideoInput = TypedDict(
    "KlingTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "model_name": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "mode_strategy": NotRequired[Literal["pro", "4k"]],
    "aspect_ratio": NotRequired[str],
    "duration": NotRequired[str],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "watermark_enabled": NotRequired[bool],
    },
    total=False,
)

KlingV15ProImageToVideoOfficialInput = TypedDict(
    "KlingV15ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV15StandardImageToVideoOfficialInput = TypedDict(
    "KlingV15StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV16ImageToVideoInput = TypedDict(
    "KlingV16ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV16ProImageToVideoOfficialInput = TypedDict(
    "KlingV16ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV16ProMultiImageToVideoOfficialInput = TypedDict(
    "KlingV16ProMultiImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal["5", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV16ProTextToVideoOfficialInput = TypedDict(
    "KlingV16ProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV16StandardImageToVideoOfficialInput = TypedDict(
    "KlingV16StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV16StandardMultiImageToVideoOfficialInput = TypedDict(
    "KlingV16StandardMultiImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal["5", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV16StandardTextToVideoOfficialInput = TypedDict(
    "KlingV16StandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV16TextToVideoInput = TypedDict(
    "KlingV16TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV1ProImageToVideoOfficialInput = TypedDict(
    "KlingV1ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV1ProTextToVideoOfficialInput = TypedDict(
    "KlingV1ProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV1StandardImageToVideoOfficialInput = TypedDict(
    "KlingV1StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV1StandardTextToVideoOfficialInput = TypedDict(
    "KlingV1StandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV2MasterImageToVideoOfficialInput = TypedDict(
    "KlingV2MasterImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV2MasterTextToVideoOfficialInput = TypedDict(
    "KlingV2MasterTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV21MasterImageToVideoOfficialInput = TypedDict(
    "KlingV21MasterImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV21MasterTextToVideoOfficialInput = TypedDict(
    "KlingV21MasterTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV21ImageToVideoInput = TypedDict(
    "KlingV21ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV21MasterImageToVideoInput = TypedDict(
    "KlingV21MasterImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV21MasterTextToVideoInput = TypedDict(
    "KlingV21MasterTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV21ProImageToVideoOfficialInput = TypedDict(
    "KlingV21ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV21StandardImageToVideoOfficialInput = TypedDict(
    "KlingV21StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV25TurboProImageToVideoOfficialInput = TypedDict(
    "KlingV25TurboProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV25TurboProTextToVideoOfficialInput = TypedDict(
    "KlingV25TurboProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV25TurboStandardImageToVideoOfficialInput = TypedDict(
    "KlingV25TurboStandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV25TurboStandardTextToVideoOfficialInput = TypedDict(
    "KlingV25TurboStandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV25TurboImageToVideoInput = TypedDict(
    "KlingV25TurboImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV25TurboTextToVideoInput = TypedDict(
    "KlingV25TurboTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV26ProImageToVideoInput = TypedDict(
    "KlingV26ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV26ProImageToVideoOfficialInput = TypedDict(
    "KlingV26ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV26ProMotionControlInput = TypedDict(
    "KlingV26ProMotionControlInput",
    {
    "mode": NotRequired[Literal["motion-control"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV26ProMotionControlOfficialInput = TypedDict(
    "KlingV26ProMotionControlOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image_url": Required[str],
    "video_url": Required[str],
    "prompt": NotRequired[str],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[Literal["yes", "no"]],
    },
    total=False,
)

KlingV26ProTextToVideoInput = TypedDict(
    "KlingV26ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV26ProTextToVideoOfficialInput = TypedDict(
    "KlingV26ProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV26StandardImageToVideoOfficialInput = TypedDict(
    "KlingV26StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV26StandardMotionControlOfficialInput = TypedDict(
    "KlingV26StandardMotionControlOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image_url": Required[str],
    "video_url": Required[str],
    "prompt": NotRequired[str],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[Literal["yes", "no"]],
    },
    total=False,
)

KlingV26StandardTextToVideoOfficialInput = TypedDict(
    "KlingV26StandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["5", "10"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV3Omni4kImageToVideoOfficialInput = TypedDict(
    "KlingV3Omni4kImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3Omni4kTextToVideoOfficialInput = TypedDict(
    "KlingV3Omni4kTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

KlingV3OmniProImageToVideoOfficialInput = TypedDict(
    "KlingV3OmniProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniProReferenceToVideoAt7RefOfficialInput = TypedDict(
    "KlingV3OmniProReferenceToVideoAt7RefOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniProReferenceToVideoOfficialInput = TypedDict(
    "KlingV3OmniProReferenceToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniProTextToVideoOfficialInput = TypedDict(
    "KlingV3OmniProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

KlingV3OmniProVideoEditOfficialInput = TypedDict(
    "KlingV3OmniProVideoEditOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniProVideoToVideoOfficialInput = TypedDict(
    "KlingV3OmniProVideoToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniStandardImageToVideoOfficialInput = TypedDict(
    "KlingV3OmniStandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniStandardReferenceToVideoAt7RefOfficialInput = TypedDict(
    "KlingV3OmniStandardReferenceToVideoAt7RefOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniStandardReferenceToVideoOfficialInput = TypedDict(
    "KlingV3OmniStandardReferenceToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniStandardTextToVideoOfficialInput = TypedDict(
    "KlingV3OmniStandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

KlingV3OmniStandardVideoEditOfficialInput = TypedDict(
    "KlingV3OmniStandardVideoEditOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3OmniStandardVideoToVideoOfficialInput = TypedDict(
    "KlingV3OmniStandardVideoToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV30ProImageToVideoInput = TypedDict(
    "KlingV30ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[3, 5, 10, 15]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV30ProTextToVideoInput = TypedDict(
    "KlingV30ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV30StandardImageToVideoInput = TypedDict(
    "KlingV30StandardImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

KlingV30StandardTextToVideoInput = TypedDict(
    "KlingV30StandardTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

KlingV34kImageToVideoOfficialInput = TypedDict(
    "KlingV34kImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV34kTextToVideoOfficialInput = TypedDict(
    "KlingV34kTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV3ProImageToVideoOfficialInput = TypedDict(
    "KlingV3ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3ProMotionControlOfficialInput = TypedDict(
    "KlingV3ProMotionControlOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image_url": Required[str],
    "video_url": Required[str],
    "prompt": NotRequired[str],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[Literal["yes", "no"]],
    },
    total=False,
)

KlingV3ProTextToVideoOfficialInput = TypedDict(
    "KlingV3ProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingV3StandardImageToVideoOfficialInput = TypedDict(
    "KlingV3StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image": NotRequired[str],
    "image_tail": NotRequired[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "voice_list": NotRequired[list[dict[str, JsonValue]]],
    "static_mask": NotRequired[str],
    "dynamic_masks": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingV3StandardMotionControlOfficialInput = TypedDict(
    "KlingV3StandardMotionControlOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "image_url": Required[str],
    "video_url": Required[str],
    "prompt": NotRequired[str],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "character_orientation": Required[Literal["image", "video"]],
    "keep_original_sound": NotRequired[Literal["yes", "no"]],
    },
    total=False,
)

KlingV3StandardTextToVideoOfficialInput = TypedDict(
    "KlingV3StandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": NotRequired[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "sound": NotRequired[Literal["on", "off"]],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "camera_control": NotRequired[dict[str, JsonValue]],
    },
    total=False,
)

KlingVideoEffectsOfficialInput = TypedDict(
    "KlingVideoEffectsOfficialInput",
    {
    "effect_scene": Required[Literal["palm_sized_figure_pro", "prank_box", "perler_beads", "spring_bloom", "toss_run", "switch_to_silk", "get_rich_quick", "make_it_rain", "twist_shake", "the_hip_sway", "send_my_love", "funky_martian", "wealth_drive", "the_high_kick", "the_exercise", "lucky_veggie", "studio_look", "flash_drive", "shush_my_dreams", "french_elegance", "finger_swipe", "advent_of_flora", "smooth_transition", "kiss_pro", "raid_check", "snow_night_kiss", "eternal_kiss", "fortune_in_motion", "chinese_trend", "sedan_chair_dance", "skyfall", "good_luck_dance", "laicai_dance", "yangge_dance", "color_mixing", "palm_sized_figure", "lantern_festival_cuju", "unique_firework", "unique_spring_couplets", "horse_mask", "fortune_knocks_cartoon", "tangyuan_to_animal", "hot_feet_dance", "swag_dance", "pigeon_dance", "bloodline_dance", "chanel_dance", "cute_dance", "love_theme_song", "pumpitup_dance", "city_to_village", "fortune_god_transform", "new_year_feast", "ring_in_new", "horse_year_firework", "pet_vlogger", "crystal_horse", "lateral_shift_transition", "drunk_dance", "drunk_dance_pet", "daoma_dance", "bouncy_dance", "smooth_sailing_dance", "new_year_greeting", "lion_dance", "prosperity", "great_success", "golden_horse_fortune", "red_packet_box", "lucky_horse_year", "lucky_red_packet", "lucky_money_come", "lion_dance_pet", "dumpling_making_pet", "fish_making_pet", "pet_red_packet", "lantern_glow", "expression_challenge", "overdrive", "heart_gesture_dance", "poping", "martial_arts", "running", "nezha", "motorcycle_dance", "subject_3_dance", "ghost_step_dance", "phantom_jewel", "zoom_out", "cheers_2026", "fight_pro", "hug_pro", "heart_gesture_pro", "dollar_rain_pro", "pet_bee_pro", "countdown_teleport", "santa_random_surprise", "magic_match_tree", "bullet_time_360", "happy_birthday", "birthday_star", "thumbs_up_pro", "tiger_hug_pro", "pet_lion_pro", "surprise_bouquet", "bouquet_drop", "3d_cartoon_1_pro", "firework_2026", "glamour_photo_shoot", "box_of_joy", "first_toast_of_the_year", "my_santa_pic", "santa_gift", "steampunk_christmas", "snowglobe", "christmas_photo_shoot", "ornament_crash", "santa_express", "instant_christmas", "particle_santa_surround", "coronation_of_frost", "building_sweater", "spark_in_the_snow", "scarlet_and_snow", "cozy_toon_wrap", "bullet_time_lite", "magic_cloak", "balloon_parade", "jumping_ginger_joy", "bullet_time", "c4d_cartoon_pro", "pure_white_wings", "black_wings", "golden_wing", "pink_pink_wings", "venomous_spider", "throne_of_king", "luminous_elf", "woodland_elf", "japanese_anime_1", "american_comics", "guardian_spirit", "swish_swish", "snowboarding", "witch_transform", "vampire_transform", "pumpkin_head_transform", "demon_transform", "mummy_transform", "zombie_transform", "cute_pumpkin_transform", "cute_ghost_transform", "knock_knock_halloween", "halloween_escape", "baseball", "inner_voice", "a_list_look", "memory_alive", "trampoline", "trampoline_night", "pucker_up", "guess_what", "feed_mooncake", "rampage_ape", "flyer", "dishwasher", "pet_chinese_opera", "magic_fireball", "gallery_ring", "pet_moto_rider", "muscle_pet", "squeeze_scream", "pet_delivery", "running_man", "disappear", "mythic_style", "steampunk", "3d_cartoon_2", "eagle_snatch", "hug_from_past", "firework", "media_interview", "pet_chef", "santa_gifts", "santa_hug", "heart_gesture_1", "pet_wizard", "smoke_smoke", "instant_kid", "dollar_rain", "cry_cry", "building_collapse", "gun_shot", "mushroom", "double_gun", "pet_warrior", "lightning_power", "jesus_hug", "shark_alert", "long_hair", "lie_flat", "polar_bear_hug", "brown_bear_hug", "jazz_jazz", "office_escape_plow", "fly_fly", "watermelon_bomb", "pet_dance", "boss_coming", "wool_curly", "pet_bee", "marry_me", "swing_swing", "day_to_night", "piggy_morph", "wig_out", "car_explosion", "ski_ski", "siblings", "construction_worker", "let’s_ride", "snatched", "magic_broom", "felt_felt", "jumpdrop", "surfsurf", "fairy_wing", "angel_wing", "dark_wing", "skateskate", "plushcut", "jelly_press", "jelly_slice", "jelly_squish", "jelly_jiggle", "pixelpixel", "yearbook", "instant_film", "anime_figure", "rocketrocket", "bloombloom", "dizzydizzy", "fuzzyfuzzy", "squish", "expansion", "emoji"]],
    "input": Required[dict[str, JsonValue]],
    },
    total=False,
)

KlingVideoExtensionOfficialInput = TypedDict(
    "KlingVideoExtensionOfficialInput",
    {
    "video_id": Required[str],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "cfg_scale": NotRequired[int | float],
    },
    total=False,
)

KlingVideoO1ProImageToVideoOfficialInput = TypedDict(
    "KlingVideoO1ProImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoO1ProTextToVideoOfficialInput = TypedDict(
    "KlingVideoO1ProTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

KlingVideoO1ProVideoEditOfficialInput = TypedDict(
    "KlingVideoO1ProVideoEditOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoO1ProVideoToVideoOfficialInput = TypedDict(
    "KlingVideoO1ProVideoToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoO1StandardImageToVideoOfficialInput = TypedDict(
    "KlingVideoO1StandardImageToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    "image_list": Required[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoO1StandardTextToVideoOfficialInput = TypedDict(
    "KlingVideoO1StandardTextToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": NotRequired[str],
    "multi_shot": NotRequired[bool],
    "shot_type": NotRequired[Literal["customize", "intelligence"]],
    "multi_prompt": NotRequired[list[dict[str, JsonValue]]],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[Literal["on", "off"]],
    },
    total=False,
)

KlingVideoO1StandardVideoEditOfficialInput = TypedDict(
    "KlingVideoO1StandardVideoEditOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoO1StandardVideoToVideoOfficialInput = TypedDict(
    "KlingVideoO1StandardVideoToVideoOfficialInput",
    {
    "model_name": Required[str],
    "mode": Required[Literal["std", "pro"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal["3", "4", "5", "6", "7", "8", "9", "10"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "image_list": NotRequired[list[dict[str, JsonValue]]],
    "element_list": NotRequired[list[dict[str, JsonValue]]],
    "video_list": Required[list[dict[str, JsonValue]]],
    },
    total=False,
)

KlingVideoToAudioOfficialInput = TypedDict(
    "KlingVideoToAudioOfficialInput",
    {
    "video_id": NotRequired[str],
    "video_url": NotRequired[str],
    "sound_effect_prompt": NotRequired[str],
    "bgm_prompt": NotRequired[str],
    "asmr_mode": NotRequired[bool],
    },
    total=False,
)

MinimaxHailuoV23FastImageToVideoInput = TypedDict(
    "MinimaxHailuoV23FastImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

MinimaxHailuoV23ImageToVideoInput = TypedDict(
    "MinimaxHailuoV23ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

MinimaxHailuoV23TextToVideoInput = TypedDict(
    "MinimaxHailuoV23TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

MinimaxHailuoV2ImageToVideoInput = TypedDict(
    "MinimaxHailuoV2ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["512P", "768P", "1080P"]],
    "size": NotRequired[str],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

MinimaxHailuoV2StartEndToVideoInput = TypedDict(
    "MinimaxHailuoV2StartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

MinimaxHailuoV2TextToVideoInput = TypedDict(
    "MinimaxHailuoV2TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[6, 10]],
    "resolution": NotRequired[Literal["768P", "1080P"]],
    "size": NotRequired[str],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": NotRequired[list[ReferenceAsset]],
    },
    total=False,
)

MinimaxImageV1LiveImageToImageInput = TypedDict(
    "MinimaxImageV1LiveImageToImageInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["1:1", "16:9", "4:3", "3:2", "2:3", "3:4", "9:16", "21:9"]],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

MinimaxImageV1TextToImageInput = TypedDict(
    "MinimaxImageV1TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["1:1", "16:9", "4:3", "3:2", "2:3", "3:4", "9:16", "21:9"]],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

MinimaxVideo01TextToVideoInput = TypedDict(
    "MinimaxVideo01TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    },
    total=False,
)

NovitaImageToImageInput = TypedDict(
    "NovitaImageToImageInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "image_size": NotRequired[str],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageUpscalerUpscaleInput = TypedDict(
    "NovitaImageUpscalerUpscaleInput",
    {
    "mode": NotRequired[Literal["upscale"]],
    "model_name": NotRequired[str],
    "scale_factor": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageUpscalerV2UpscaleInput = TypedDict(
    "NovitaImageUpscalerV2UpscaleInput",
    {
    "mode": NotRequired[Literal["upscale"]],
    "resolution": NotRequired[Literal["2k", "4k", "8k"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageBackgroundRemovalInput = TypedDict(
    "NovitaImageBackgroundRemovalInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageBackgroundRemovalV2Input = TypedDict(
    "NovitaImageBackgroundRemovalV2Input",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageBackgroundReplacementInput = TypedDict(
    "NovitaImageBackgroundReplacementInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageCleanupInput = TypedDict(
    "NovitaImageCleanupInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageEraseInput = TypedDict(
    "NovitaImageEraseInput",
    {
    "mode": NotRequired[Literal["inpaint"]],
    "prompt": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageReimagineInput = TypedDict(
    "NovitaImageReimagineInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageTextRemovalInput = TypedDict(
    "NovitaImageTextRemovalInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaImageToPromptInput = TypedDict(
    "NovitaImageToPromptInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "negative_prompt": NotRequired[str],
    "image_size": NotRequired[str],
    "seed": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaInpaintInput = TypedDict(
    "NovitaInpaintInput",
    {
    "mode": NotRequired[Literal["inpaint"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

NovitaTextToImageInput = TypedDict(
    "NovitaTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "num_images": NotRequired[int],
    "aspect_ratio": NotRequired[str],
    "image_size": NotRequired[str],
    "model_name": NotRequired[str],
    "num_inference_steps": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sampler_name": NotRequired[str],
    },
    total=False,
)

OpenaiGptImage2Input = TypedDict(
    "OpenaiGptImage2Input",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "quality": NotRequired[Literal["low", "medium", "high"]],
    "num_images": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    },
    total=False,
)

OpenaiGptImage2EditInput = TypedDict(
    "OpenaiGptImage2EditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "quality": NotRequired[Literal["low", "medium", "high"]],
    "num_images": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

PixverseV45ImageToVideoInput = TypedDict(
    "PixverseV45ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

PixverseV45TextToVideoInput = TypedDict(
    "PixverseV45TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    "watermark": NotRequired[bool],
    },
    total=False,
)

QwenImageEditInput = TypedDict(
    "QwenImageEditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": NotRequired[str],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

QwenImageTextToImageInput = TypedDict(
    "QwenImageTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

TopazImageEnhanceInput = TypedDict(
    "TopazImageEnhanceInput",
    {
    "mode": NotRequired[Literal["enhance", "enhance-gen", "restore-gen", "tool"]],
    "model_name": NotRequired[Literal["Standard V2", "High Fidelity V2", "Low Resolution 2", "Art & CGI", "Text & Shapes", "Detail Faces", "Recover Faces", "Transparent Image Upscale"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "output_width": NotRequired[int],
    "output_height": NotRequired[int],
    "face_enhancement": NotRequired[bool],
    "face_enhancement_strength": NotRequired[int | float],
    "face_enhancement_creativity": NotRequired[int | float],
    "sharpen": NotRequired[int | float],
    "denoise": NotRequired[int | float],
    "fix_compression": NotRequired[int | float],
    "strength": NotRequired[int | float],
    "subject_detection": NotRequired[Literal["foreground", "background", "all"]],
    "prompt": NotRequired[str],
    "creativity": NotRequired[int],
    "texture": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

TopazImageEnhanceGenInput = TypedDict(
    "TopazImageEnhanceGenInput",
    {
    "mode": NotRequired[Literal["enhance", "enhance-gen", "restore-gen", "tool"]],
    "model_name": NotRequired[Literal["Standard Max", "Wonder", "Wonder 2", "Redefine: Realistic", "Redefine: Creative", "Recover 3", "Bloom Creative", "Bloom Realism"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "output_width": NotRequired[int],
    "output_height": NotRequired[int],
    "face_enhancement": NotRequired[bool],
    "face_enhancement_strength": NotRequired[int | float],
    "face_enhancement_creativity": NotRequired[int | float],
    "sharpen": NotRequired[int | float],
    "denoise": NotRequired[int | float],
    "fix_compression": NotRequired[int | float],
    "strength": NotRequired[int | float],
    "subject_detection": NotRequired[Literal["foreground", "background", "all"]],
    "prompt": NotRequired[str],
    "creativity": NotRequired[int],
    "texture": NotRequired[int],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

TopazImageToolInput = TypedDict(
    "TopazImageToolInput",
    {
    "mode": NotRequired[Literal["enhance", "enhance-gen", "restore-gen", "tool"]],
    "model_name": NotRequired[Literal["Sharpen", "Sharpen Strong", "Denoise Normal", "Denoise Strong", "Background Removal", "Colorization", "Balance Color", "Adjust Lighting"]],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "face_enhancement": NotRequired[bool],
    "face_enhancement_strength": NotRequired[int | float],
    "sharpen": NotRequired[int | float],
    "denoise": NotRequired[int | float],
    "fix_compression": NotRequired[int | float],
    "strength": NotRequired[int | float],
    "subject_detection": NotRequired[Literal["foreground", "background", "all"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VideoFaceSwapInput = TypedDict(
    "VideoFaceSwapInput",
    {
    "reference_assets": Required[list[ReferenceAsset]],
    "enable_restore": NotRequired[bool],
    "enable_occlusion_prevention": NotRequired[bool],
    "response_video_type": NotRequired[Literal["mp4", "gif"]],
    },
    total=False,
)

ViduQ1ImageToVideoInput = TypedDict(
    "ViduQ1ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ1ReferenceToVideoInput = TypedDict(
    "ViduQ1ReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "resolution": NotRequired[Literal["1080p"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ1StartEndToVideoInput = TypedDict(
    "ViduQ1StartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ1TextToVideoInput = TypedDict(
    "ViduQ1TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    "watermark": NotRequired[bool],
    },
    total=False,
)

ViduQ2ProFastImageToVideoInput = TypedDict(
    "ViduQ2ProFastImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2ProFastStartEndToVideoInput = TypedDict(
    "ViduQ2ProFastStartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2ProImageToVideoInput = TypedDict(
    "ViduQ2ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2ProMultiFrameToVideoInput = TypedDict(
    "ViduQ2ProMultiFrameToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2ProStartEndToVideoInput = TypedDict(
    "ViduQ2ProStartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2ReferenceToVideoInput = TypedDict(
    "ViduQ2ReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["1080p"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2TemplateToVideoInput = TypedDict(
    "ViduQ2TemplateToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": Required[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2TextToVideoInput = TypedDict(
    "ViduQ2TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    "watermark": NotRequired[bool],
    },
    total=False,
)

ViduQ2TurboImageToVideoInput = TypedDict(
    "ViduQ2TurboImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2TurboMultiFrameToVideoInput = TypedDict(
    "ViduQ2TurboMultiFrameToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ2TurboStartEndToVideoInput = TypedDict(
    "ViduQ2TurboStartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ3ProImageToVideoInput = TypedDict(
    "ViduQ3ProImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduQ3ProTextToVideoInput = TypedDict(
    "ViduQ3ProTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[5]],
    "resolution": NotRequired[Literal["1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "style": NotRequired[str],
    "turbo_mode": NotRequired[bool],
    "watermark": NotRequired[bool],
    },
    total=False,
)

ViduV20ImageToVideoInput = TypedDict(
    "ViduV20ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "duration": NotRequired[Literal[4, 8]],
    "resolution": NotRequired[Literal["360p", "720p"]],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduV20ReferenceToVideoInput = TypedDict(
    "ViduV20ReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4]],
    "seed": NotRequired[int],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "resolution": NotRequired[Literal["360p", "720p"]],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

ViduV20StartEndToVideoInput = TypedDict(
    "ViduV20StartEndToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "duration": NotRequired[Literal[4, 8]],
    "resolution": NotRequired[Literal["360p", "720p", "1080p"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "watermark": NotRequired[bool],
    "movement_amplitude": NotRequired[Literal["auto", "small", "medium", "large"]],
    "bgm": NotRequired[bool],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "audio_asset_id": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

VitsSvcVoiceChangerInput = TypedDict(
    "VitsSvcVoiceChangerInput",
    {
    "mode": NotRequired[str],
    "source_audio_url": Required[str],
    "reference_audio_url": Required[str],
    "source_asset_id": NotRequired[str],
    "target_voice_id": NotRequired[str],
    "noise_scale": NotRequired[int | float],
    "dither_src": NotRequired[bool],
    "dither_ref": NotRequired[bool],
    "streaming": NotRequired[bool],
    "chunk_size": NotRequired[int],
    },
    total=False,
)

WanImageToVideoInput = TypedDict(
    "WanImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanTextToVideoInput = TypedDict(
    "WanTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "width": NotRequired[Literal[480, 720, 832, 1280]],
    "height": NotRequired[Literal[480, 720, 832, 1280]],
    "num_inference_steps": NotRequired[int],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "flow_shift": NotRequired[int | float],
    "enable_safety_checker": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "loras": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

WanV22ImageToVideoInput = TypedDict(
    "WanV22ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 8]],
    "resolution": NotRequired[Literal["480p", "720p", "1080p"]],
    "seed": NotRequired[int],
    "guidance_scale": NotRequired[int | float],
    "sound": NotRequired[bool],
    "cfg_scale": NotRequired[int | float],
    "enable_prompt_expansion": NotRequired[bool],
    "turbo_mode": NotRequired[bool],
    "style": NotRequired[str],
    "ratio": NotRequired[str],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV22TextToVideoInput = TypedDict(
    "WanV22TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 8]],
    "size": Required[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "loras": NotRequired[list[dict[str, JsonValue]]],
    },
    total=False,
)

WanV25PreviewImageToVideoInput = TypedDict(
    "WanV25PreviewImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "resolution": NotRequired[Literal["480P", "720P", "1080P"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV25PreviewTextToVideoInput = TypedDict(
    "WanV25PreviewTextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "size": NotRequired[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "960*960", "1088*832", "832*1088", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    },
    total=False,
)

WanV26ImageToVideoInput = TypedDict(
    "WanV26ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10, 15]],
    "resolution": NotRequired[Literal["720P", "1080P"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[Literal["single", "multi"]],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV26TextToVideoInput = TypedDict(
    "WanV26TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10, 15]],
    "size": NotRequired[Literal["1280*720", "720*1280", "960*960", "1088*832", "832*1088", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "ratio": NotRequired[str],
    "aspect_ratio": NotRequired[str],
    "seed": NotRequired[int],
    "fps": NotRequired[int],
    "camera_fixed": NotRequired[bool],
    "generate_audio": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "reference_audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[Literal["single", "multi"]],
    "audio": NotRequired[bool],
    "model": NotRequired[str],
    "template": NotRequired[str],
    },
    total=False,
)

WanV26VideoToVideoInput = TypedDict(
    "WanV26VideoToVideoInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": NotRequired[str],
    "negative_prompt": NotRequired[str],
    "duration": Required[Literal[5, 10]],
    "aspect_ratio": NotRequired[str],
    "size": NotRequired[Literal["832*480", "480*832", "624*624", "1280*720", "720*1280", "1920*1080", "1080*1920", "1440*1440", "1632*1248", "1248*1632"]],
    "seed": NotRequired[int],
    "keep_original_sound": NotRequired[bool],
    "watermark": NotRequired[bool],
    "audio_url": NotRequired[str],
    "enable_prompt_expansion": NotRequired[bool],
    "shot_type": NotRequired[str],
    "audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27EditInput = TypedDict(
    "WanV27EditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "num_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27ExtendVideoInput = TypedDict(
    "WanV27ExtendVideoInput",
    {
    "mode": NotRequired[Literal["extend-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27ImageToVideoInput = TypedDict(
    "WanV27ImageToVideoInput",
    {
    "mode": NotRequired[Literal["image-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27ProEditInput = TypedDict(
    "WanV27ProEditInput",
    {
    "mode": NotRequired[Literal["image-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "num_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27ProTextToImageInput = TypedDict(
    "WanV27ProTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "max_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_safety_checker": NotRequired[bool],
    },
    total=False,
)

WanV27ReferenceToVideoInput = TypedDict(
    "WanV27ReferenceToVideoInput",
    {
    "mode": NotRequired[Literal["reference-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "multi_shots": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

WanV27TextToImageInput = TypedDict(
    "WanV27TextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "max_images": NotRequired[int],
    "image_size": NotRequired[Literal["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"] | dict[str, JsonValue]],
    "enable_safety_checker": NotRequired[bool],
    },
    total=False,
)

WanV27TextToVideoInput = TypedDict(
    "WanV27TextToVideoInput",
    {
    "mode": NotRequired[Literal["text-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "seed": NotRequired[int],
    "audio_url": NotRequired[str],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "enable_prompt_expansion": NotRequired[bool],
    "enable_safety_checker": NotRequired[bool],
    },
    total=False,
)

WanV27VideoEditInput = TypedDict(
    "WanV27VideoEditInput",
    {
    "mode": NotRequired[Literal["video-edit"]],
    "prompt": Required[str],
    "audio_setting": NotRequired[Literal["auto", "origin"]],
    "seed": NotRequired[int],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "duration": NotRequired[Literal[0, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "enable_safety_checker": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

Wan22AnimateReplaceInput = TypedDict(
    "Wan22AnimateReplaceInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

Wan26ReferenceToVideoFlashInput = TypedDict(
    "Wan26ReferenceToVideoFlashInput",
    {
    "mode": NotRequired[Literal["video-to-video"]],
    "prompt": Required[str],
    "negative_prompt": NotRequired[str],
    "duration": NotRequired[Literal[5, 10]],
    "aspect_ratio": NotRequired[Literal["16:9", "9:16", "1:1", "4:3", "3:4"]],
    "resolution": NotRequired[Literal["720p", "1080p"]],
    "seed": NotRequired[int],
    "enable_prompt_expansion": NotRequired[bool],
    "audio": NotRequired[bool],
    "reference_assets": Required[list[ReferenceAsset]],
    },
    total=False,
)

YouchuanMidjourneyV7FastInput = TypedDict(
    "YouchuanMidjourneyV7FastInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    },
    total=False,
)

YouchuanMidjourneyV7TurboInput = TypedDict(
    "YouchuanMidjourneyV7TurboInput",
    {
    "mode": NotRequired[Literal["text-to-image", "image-to-image"]],
    "prompt": Required[str],
    },
    total=False,
)

YouchuanMidjourneyV7UpscaleInput = TypedDict(
    "YouchuanMidjourneyV7UpscaleInput",
    {
    "parent_task_id": Required[str],
    "image_index": Required[int],
    "type": NotRequired[Literal[0, 1, 2, 3]],
    },
    total=False,
)

YouchuanMidjourneyV7VariationInput = TypedDict(
    "YouchuanMidjourneyV7VariationInput",
    {
    "task_id": Required[str],
    "image_no": Required[int],
    "variation_type": NotRequired[Literal[0, 1]],
    "remix_prompt": NotRequired[str],
    },
    total=False,
)

ZImageTurboLoraTextToImageInput = TypedDict(
    "ZImageTurboLoraTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

ZImageTurboTextToImageInput = TypedDict(
    "ZImageTurboTextToImageInput",
    {
    "mode": NotRequired[Literal["text-to-image"]],
    "prompt": Required[str],
    "image_size": NotRequired[str],
    "width": NotRequired[int],
    "height": NotRequired[int],
    "seed": NotRequired[int],
    "output_format": NotRequired[Literal["jpeg", "png", "webp"]],
    "safety_tolerance": NotRequired[Literal["1", "2", "3", "4", "5", "6"]],
    "enable_web_search": NotRequired[bool],
    "thinking_level": NotRequired[Literal["minimal", "high"]],
    },
    total=False,
)

GeneratedModelInputMap: TypeAlias = dict[BuiltInModelId, object]
GeneratedTaskInputMap: TypeAlias = dict[BuiltInTaskId, object]
GeneratedModelOutputMap: TypeAlias = dict[BuiltInModelId, object]
GeneratedTaskOutputMap: TypeAlias = dict[BuiltInTaskId, object]
