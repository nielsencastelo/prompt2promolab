
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List

from diffusers.utils import export_to_video

from .config import MODEL_REGISTRY, get_outputs_dir


def _resolve_scene_timing(
    *,
    profile_key: str,
    num_frames: int | None,
    fps: int | None,
    seconds: float | None,
) -> tuple[int, int]:
    profile = MODEL_REGISTRY[profile_key]
    resolved_fps = fps or profile.default_fps
    resolved_frames = num_frames or profile.default_num_frames

    if seconds is not None:
        if seconds <= 0:
            raise ValueError("Scene duration must be positive.")
        if profile.max_num_frames is not None:
            resolved_fps = min(resolved_fps, max(1, int(profile.max_num_frames / seconds)))
        resolved_frames = max(1, int(round(seconds * resolved_fps)))

    if profile.max_num_frames is not None:
        resolved_frames = min(resolved_frames, profile.max_num_frames)

    return resolved_frames, resolved_fps


def render_scene(
    pipe: Any,
    profile_key: str,
    prompt: str,
    negative_prompt: str,
    output_path: str | Path,
    *,
    num_frames: int | None = None,
    height: int | None = None,
    width: int | None = None,
    fps: int | None = None,
    seconds: float | None = None,
    num_inference_steps: int | None = None,
    guidance_scale: float | None = None,
) -> Path:
    profile = MODEL_REGISTRY[profile_key]
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_num_frames, resolved_fps = _resolve_scene_timing(
        profile_key=profile_key,
        num_frames=num_frames,
        fps=fps,
        seconds=seconds,
    )

    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_frames=resolved_num_frames,
        height=height or profile.default_height,
        width=width or profile.default_width,
        num_inference_steps=num_inference_steps or profile.recommended_steps,
        guidance_scale=guidance_scale if guidance_scale is not None else profile.guidance_scale,
    )

    frames = result.frames[0] if isinstance(result.frames, list) else result.frames
    export_to_video(frames, str(output_path), fps=resolved_fps)
    return output_path


def render_storyboard(
    pipe: Any,
    profile_key: str,
    storyboard: Dict[str, Any],
    output_dir: str | Path | None = None,
) -> List[Path]:
    output_dir = Path(output_dir or (get_outputs_dir() / storyboard["slug"]))
    output_dir.mkdir(parents=True, exist_ok=True)

    clip_paths: List[Path] = []
    default_scene_seconds = storyboard.get("clip_seconds")
    for scene in storyboard["scenes"]:
        out_path = output_dir / f"scene_{int(scene['scene_id']):02d}.mp4"
        clip_paths.append(
            render_scene(
                pipe=pipe,
                profile_key=profile_key,
                prompt=scene["prompt"],
                negative_prompt=scene.get("negative_prompt", ""),
                output_path=out_path,
                seconds=scene.get("seconds", default_scene_seconds),
            )
        )
    return clip_paths
