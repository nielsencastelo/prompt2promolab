
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelProfile:
    key: str
    display_name: str
    pipeline_kind: str
    hf_repo: str
    torch_dtype: str
    default_height: int
    default_width: int
    default_fps: int
    default_num_frames: int
    recommended_steps: int
    guidance_scale: float
    notes: str


MODEL_REGISTRY = {
    "small_gpu": ModelProfile(
        key="small_gpu",
        display_name="CogVideoX-2B (small / lower cost)",
        pipeline_kind="cogvideox",
        hf_repo="zai-org/CogVideoX-2b",
        torch_dtype="float16",
        default_height=480,
        default_width=720,
        default_fps=16,
        default_num_frames=81,
        recommended_steps=35,
        guidance_scale=6.0,
        notes="Best entry point for smaller GPUs. Try quantization and CPU offload if memory is tight.",
    ),
    "balanced": ModelProfile(
        key="balanced",
        display_name="LTX-Video (balanced / faster iteration)",
        pipeline_kind="ltx",
        hf_repo="Lightricks/LTX-Video",
        torch_dtype="bfloat16",
        default_height=512,
        default_width=768,
        default_fps=16,
        default_num_frames=97,
        recommended_steps=30,
        guidance_scale=3.0,
        notes="Good balance between speed and quality for repeated ad testing.",
    ),
    "quality_14gb_plus": ModelProfile(
        key="quality_14gb_plus",
        display_name="HunyuanVideo-1.5 (higher quality)",
        pipeline_kind="hunyuan",
        hf_repo="Tencent-Hunyuan/HunyuanVideo-1.5",
        torch_dtype="bfloat16",
        default_height=544,
        default_width=960,
        default_fps=16,
        default_num_frames=81,
        recommended_steps=40,
        guidance_scale=5.0,
        notes="Use when you have more VRAM and want better institutional pieces.",
    ),
}


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_outputs_dir() -> Path:
    out = get_project_root() / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    return out
