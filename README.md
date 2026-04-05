
# Prompt2PromoLab

Gere vídeos curtos e institucionais a partir de prompts, com foco em **marketing de baixo custo** e **modelos open-source que conseguem rodar em GPUs mais acessíveis**.

O projeto foi pensado para:
- Reels e vídeos curtos de **15s, 30s e 45s**
- Vídeos institucionais mais longos
- Campanhas para **Instagram**, **Facebook** e apresentações rápidas
- Fluxo prático para pequenos negócios, igrejas, autônomos e equipes com orçamento limitado

## Nome recomendado do repositório

**prompt2promolab**

Por que este nome?
- comunica claramente o fluxo `prompt -> promo`
- segue um padrão parecido com nomes comuns no ecossistema (`LTX-Video`, `Gen V`, `Text-To-Video-AI`, `viral2viral`)
- é mais específico para uso de marketing e divulgação do que nomes genéricos de T2V

Alternativas:
- `pocket-promo-video`
- `lowcost-video-lab`
- `nano-promo-video`

## Estratégia do projeto

Gerar vídeos longos diretamente em um único passe ainda é pesado e menos previsível em hardware modesto.
Por isso, este repositório adota a estratégia mais segura:

1. transformar a ideia em **storyboard**
2. gerar **clips curtos por cena** (ex.: 5 segundos)
3. concatenar os clips com `ffmpeg`
4. adicionar legendas, CTA e variações por canal

Esse fluxo é melhor para:
- reduzir custo computacional
- reaproveitar cenas
- testar diferentes prompts
- criar múltiplas versões do mesmo anúncio

## Modelos sugeridos

### Perfil 1 — GPU menor / custo mais baixo
**CogVideoX-2B quantizado**
- melhor ponto de partida
- adequado para testes locais e GPUs menores
- bom para prototipar campanhas

### Perfil 2 — equilíbrio entre velocidade e qualidade
**LTX-Video**
- mais rápido
- boa escolha para produção iterativa
- útil para gerar várias versões da mesma peça

### Perfil 3 — qualidade mais alta em GPU melhor
**HunyuanVideo-1.5**
- melhor quando você tiver mais VRAM
- indicado para peças institucionais e cenas mais refinadas

## Estrutura do repositório

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

## Instalação

### 1) Python e ambiente
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -U pip
pip install -r requirements.txt
```

### 2) FFmpeg
Instale o `ffmpeg` no sistema e garanta que ele esteja no PATH.

No Ubuntu:
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

No Windows:
- instalar via `winget`, `choco` ou binário oficial
- conferir com `ffmpeg -version`

## Uso rápido

### Smoke test
Abra:
- `notebooks/01_model_selector_and_smoke_test.ipynb`

### Geração de reels
Abra:
- `notebooks/02_generate_reel_15s.ipynb`
- `notebooks/03_generate_reel_30s.ipynb`
- `notebooks/04_generate_reel_45s.ipynb`

### Vídeo institucional
Abra:
- `notebooks/05_generate_institutional_long_video.ipynb`

### Laboratório de prompts NazaApp
Abra:
- `notebooks/06_prompt_lab_nazaapp.ipynb`

## Perfis de geração recomendados

### Reels de 15s
- 3 cenas de 5s
- 16 fps
- foco em hook + benefício + CTA

### Reels de 30s
- 6 cenas de 5s
- narrativa curta com problema -> solução -> prova -> CTA

### Reels de 45s
- 9 cenas de 5s
- mais espaço para mostrar módulos e contexto real de uso

### Institucional longo
- montar de 12 a 24 cenas de 5s
- incluir variações de:
  - web
  - mobile
  - equipe
  - operação diária
  - impacto e depoimento
  - encerramento institucional

## Dicas de marketing para pequenos negócios

- use cenas simples, bem iluminadas e com uma ação por take
- evite prompts muito longos
- gere várias versões curtas em vez de uma peça só
- priorize CTA claro nos últimos 3 a 5 segundos
- mantenha identidade visual consistente por campanha

## Saídas esperadas

Os notebooks geram:
- clips individuais `.mp4`
- lista de concatenação
- vídeo final consolidado
- JSON de storyboard usado na renderização

## Observações práticas

- em hardware modesto, a melhor estratégia costuma ser reduzir:
  - resolução
  - número de frames
  - número de passos
- para campanhas reais, gere 3 a 10 variações da mesma peça mudando:
  - abertura
  - CTA
  - enquadramento
  - texto da cena

## Licença

Escolha a licença que fizer mais sentido para seu uso. Este template acompanha uma licença MIT por simplicidade.

