
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_storyboard(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_storyboard(data: Dict[str, Any], path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def scenes_for_duration(total_seconds: int, clip_seconds: int = 5) -> List[Dict[str, Any]]:
    if total_seconds <= 0:
        raise ValueError("total_seconds must be positive")
    if clip_seconds <= 0:
        raise ValueError("clip_seconds must be positive")

    n = total_seconds // clip_seconds
    if total_seconds % clip_seconds:
        n += 1

    scenes = []
    for i in range(n):
        scenes.append(
            {
                "scene_id": i + 1,
                "seconds": clip_seconds,
                "prompt": "",
                "negative_prompt": "",
                "overlay_text": "",
                "cta": "",
            }
        )
    return scenes
