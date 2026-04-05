
from __future__ import annotations

import os
from typing import Any

import torch

from .config import MODEL_REGISTRY


def _resolve_dtype(dtype_name: str) -> torch.dtype:
    mapping = {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }
    if dtype_name not in mapping:
        raise ValueError(f"Unsupported dtype: {dtype_name}")
    return mapping[dtype_name]


def load_pipeline(profile_key: str) -> Any:
    """
    Load a supported diffusers pipeline according to the selected profile.

    Notes:
    - This function prefers official pipeline classes when possible.
    - The Hugging Face repo may require authentication or license acceptance.
    - Long video generation is best handled by stitching multiple short clips.
    """
    profile = MODEL_REGISTRY[profile_key]
    dtype = _resolve_dtype(profile.torch_dtype)

    if profile.pipeline_kind == "cogvideox":
        from diffusers import CogVideoXPipeline

        pipe = CogVideoXPipeline.from_pretrained(profile.hf_repo, torch_dtype=dtype)
        pipe.enable_model_cpu_offload()
        return pipe

    if profile.pipeline_kind == "ltx":
        from diffusers import LTXPipeline

        pipe = LTXPipeline.from_pretrained(profile.hf_repo, torch_dtype=dtype)
        pipe.enable_model_cpu_offload()
        return pipe

    if profile.pipeline_kind == "hunyuan":
        try:
            from diffusers import HunyuanVideoPipeline  # type: ignore
        except Exception as exc:  # pragma: no cover
            raise RuntimeError(
                "This diffusers version may not expose HunyuanVideoPipeline directly yet. "
                "Upgrade diffusers or swap to a supported profile."
            ) from exc

        pipe = HunyuanVideoPipeline.from_pretrained(profile.hf_repo, torch_dtype=dtype)
        pipe.enable_model_cpu_offload()
        return pipe

    raise ValueError(f"Unsupported pipeline kind: {profile.pipeline_kind}")
