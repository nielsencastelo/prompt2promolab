
# Prompt2PromoLab

Generate short-form and institutional videos from prompts, with a focus on **low-cost marketing** and **open-source models that can run on more accessible GPUs**.

This project is designed for:
- **15s, 30s, and 45s** reels and short videos
- Longer institutional videos
- Campaigns for **Instagram**, **Facebook**, and quick presentations
- A practical workflow for small businesses, churches, solo professionals, and teams with limited budgets

## Repository

**prompt2promolab**

Why this name?
- It clearly communicates the `prompt -> promo` workflow
- It follows a naming pattern similar to common ecosystem names (`LTX-Video`, `Gen V`, `Text-To-Video-AI`, `viral2viral`)
- It is more specific for marketing and promotional use than generic T2V names

Alternatives:
- `pocket-promo-video`
- `lowcost-video-lab`
- `nano-promo-video`

## Project Strategy

Generating long videos directly in a single pass is still demanding and less predictable on modest hardware.
Because of that, this repository adopts a safer strategy:

1. Turn the idea into a **storyboard**
2. Generate **short clips per scene** (for example, 5 seconds each)
3. Concatenate the clips with `ffmpeg`
4. Add subtitles, CTA, and channel-specific variations

This workflow is better for:
- reducing compute cost
- reusing scenes
- testing different prompts
- creating multiple versions of the same ad

## Suggested Models

### Profile 1 - Smaller GPU / lower cost
**Quantized CogVideoX-2B**
- best starting point
- suitable for local testing and smaller GPUs
- good for campaign prototyping

### Profile 2 - Balanced speed and quality
**LTX-Video**
- faster
- a good choice for iterative production
- useful for generating multiple versions of the same creative

### Profile 3 - Higher quality on stronger GPUs
**HunyuanVideo-1.5**
- better when you have more VRAM
- recommended for institutional content and more refined scenes

## Repository Structure

```text
prompt2promolab/
├── notebooks/
│   ├── 00_repo_overview.ipynb
│   ├── 01_model_selector_and_smoke_test.ipynb
│   ├── 02_generate_reel_15s.ipynb
│   ├── 03_generate_reel_30s.ipynb
│   ├── 04_generate_reel_45s.ipynb
│   ├── 05_generate_institutional_long_video.ipynb
│   └── 06_prompt_lab_nazaapp.ipynb
├── prompts/
│   ├── brands/
│   │   ├── nazaapp_brand_pack.yaml
│   │   └── nazaapp_examples.md
│   └── templates/
│       ├── institutional_template.md
│       ├── reel_15s_template.md
│       ├── reel_30s_template.md
│       └── reel_45s_template.md
├── storyboards/
│   ├── nazaapp_15s.json
│   ├── nazaapp_30s.json
│   ├── nazaapp_45s.json
│   └── nazaapp_institutional.json
├── src/prompt2promolab/
│   ├── __init__.py
│   ├── config.py
│   ├── ffmpeg_utils.py
│   ├── pipelines.py
│   ├── prompting.py
│   ├── render.py
│   └── storyboard.py
├── docs/
│   └── research_notes.md
├── scripts/
│   └── concat_storyboard.py
├── requirements.txt
└── .gitignore
```

## Installation

### 1) Python and environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -U pip
pip install -r requirements.txt
```

### 2) FFmpeg
Install `ffmpeg` on your system and make sure it is available in your PATH.

On Ubuntu:
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

On Windows:
- install via `winget`, `choco`, or the official binary
- verify with `ffmpeg -version`

## Quick Start

### Smoke test
Open:
- `notebooks/01_model_selector_and_smoke_test.ipynb`

### Reel generation
Open:
- `notebooks/02_generate_reel_15s.ipynb`
- `notebooks/03_generate_reel_30s.ipynb`
- `notebooks/04_generate_reel_45s.ipynb`

### Institutional video
Open:
- `notebooks/05_generate_institutional_long_video.ipynb`

### NazaApp prompt lab
Open:
- `notebooks/06_prompt_lab_nazaapp.ipynb`

## Recommended Generation Profiles

### 15s reels
- 3 scenes of 5 seconds each
- 16 fps
- focus on hook + benefit + CTA

### 30s reels
- 6 scenes of 5 seconds each
- short narrative with problem -> solution -> proof -> CTA

### 45s reels
- 9 scenes of 5 seconds each
- more room to show modules and real usage context

### Long institutional format
- assemble 12 to 24 scenes of 5 seconds each
- include variations of:
  - web
  - mobile
  - team
  - daily operation
  - impact and testimonial
  - institutional closing

## Marketing Tips for Small Businesses

- use simple, well-lit scenes with one action per shot
- avoid overly long prompts
- generate several short variations instead of a single piece
- prioritize a clear CTA in the last 3 to 5 seconds
- keep visual identity consistent across the campaign

## Expected Outputs

The notebooks generate:
- individual `.mp4` clips
- a concatenation list
- a final merged video
- the storyboard JSON used for rendering

## Practical Notes

- on modest hardware, the best strategy is usually to reduce:
  - resolution
  - number of frames
  - number of steps
- for real campaigns, generate 3 to 10 variations of the same asset by changing:
  - opening
  - CTA
  - framing
  - scene text

## License

Choose the license that makes the most sense for your use case. This template includes an MIT license for simplicity.
