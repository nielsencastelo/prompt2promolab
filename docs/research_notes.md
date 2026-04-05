
# Research notes

This project was shaped around open-source repositories and official docs that are relevant to local or lower-cost video generation:

## Repositories and docs reviewed
- Lightricks / LTX-Video
- LTX Desktop
- ZAI / CogVideoX
- Tencent / HunyuanVideo-1.5
- Hugging Face Diffusers video generation docs
- Google Marketing Solutions / Gen V
- Awesome-Video-Diffusion list

## Why these influenced the design

### 1) Focus on short clips first
The most practical open workflows still revolve around short clips and then assembling a larger piece.
That is why this repository uses storyboard + short scene generation + ffmpeg concat.

### 2) Small-GPU first path
CogVideoX-2B is included as the most realistic starting point for smaller GPU users.
It is the safest initial path for low-budget experimentation.

### 3) Faster iteration path
LTX-Video is included for faster experimentation and repeated creative testing.

### 4) Better-quality path
HunyuanVideo-1.5 is included as an upgrade option for stronger GPUs.

### 5) Marketing orientation
Google's Gen V is a useful reference that brand/promo workflows can be organized around product shots, text overlays, brand assets and platform-specific outputs.
This repo mirrors that thinking, but with an open local-first implementation path.

## Naming rationale
Names in the space often follow these patterns:
- technology-first (`LTX-Video`)
- function-first (`Text-To-Video-AI`)
- campaign-first (`Gen V`)
- outcome-first (`viral2viral`)

Based on that pattern, `prompt2promolab` is a good fit because it reflects:
- prompt input
- promotional outcome
- experimentation workflow
