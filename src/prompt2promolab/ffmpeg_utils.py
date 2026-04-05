
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Iterable


def write_concat_file(video_paths: Iterable[Path], concat_file: Path) -> Path:
    concat_file.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for path in video_paths:
        lines.append(f"file '{Path(path).resolve().as_posix()}'")
    concat_file.write_text("\n".join(lines), encoding="utf-8")
    return concat_file


def concat_videos(video_paths: Iterable[Path], output_path: Path, overwrite: bool = True) -> Path:
    video_paths = list(video_paths)
    if not video_paths:
        raise ValueError("No video paths were provided for concatenation.")

    concat_file = output_path.with_suffix(".concat.txt")
    write_concat_file(video_paths, concat_file)

    cmd = [
        "ffmpeg",
        "-y" if overwrite else "-n",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(output_path),
    ]
    subprocess.run(cmd, check=True)
    return output_path
