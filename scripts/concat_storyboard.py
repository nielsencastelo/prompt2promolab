
from __future__ import annotations

import argparse
from pathlib import Path

from prompt2promolab.ffmpeg_utils import concat_videos


def main() -> None:
    parser = argparse.ArgumentParser(description="Concatenate storyboard clips into a final MP4.")
    parser.add_argument("--input-dir", required=True, help="Directory containing scene_XX.mp4 files.")
    parser.add_argument("--output", required=True, help="Path to output mp4.")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    clips = sorted(input_dir.glob("scene_*.mp4"))
    if not clips:
        raise SystemExit(f"No clips found in: {input_dir}")

    out = Path(args.output)
    concat_videos(clips, out)
    print(f"Saved final video to: {out}")


if __name__ == "__main__":
    main()
