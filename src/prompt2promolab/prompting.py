
from __future__ import annotations

from textwrap import dedent


PROMPT_RULES = dedent(
    """
    Write prompts in simple English.
    Keep one main action per scene.
    Prefer realistic camera motion.
    Avoid too many objects changing at the same time.
    Keep the brand message concrete and visible.
    """
).strip()


def build_marketing_prompt(
    subject: str,
    action: str,
    environment: str,
    camera: str,
    lighting: str,
    mood: str,
    brand_hint: str = "",
) -> str:
    parts = [
        subject,
        action,
        environment,
        camera,
        lighting,
        mood,
        brand_hint,
    ]
    return ", ".join([p.strip() for p in parts if p and p.strip()])


def default_negative_prompt() -> str:
    return (
        "blurry, low quality, extra fingers, deformed face, duplicated body, bad anatomy, "
        "warped text, unreadable UI, flicker, jitter, cropped hands, distorted phone screen"
    )
