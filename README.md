# 🤖 AI Content Empire

> **Automated AI content creation, avatar personas, and digital product engine for passive income.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

## 🏗️ What This Is

AI Content Empire is an **orchestration framework** that wires together the best open-source AI tools into a single runnable system for automated passive income through content creation.

**Four revenue-generating layers:**

1. 🎬 **Video Content Pipeline** — Research trends → write scripts → produce short-form videos → auto-post to YouTube Shorts, TikTok, Instagram Reels
2. 🎭 **Avatar & Persona System** — Realistic human talking-head personas OR animated characters per niche (credit, finance, investing, budgeting)
3. 📚 **Digital Product Engine** — Auto-generate sellable ebooks and guides — no fulfillment, 100% margin
4. 📡 **Distribution & Monetization** — Schedule posts, manage referral links, affiliate partnerships, auto-list digital products

---

## 🚀 Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/jjisjazzed/ai-content-empire.git
cd ai-content-empire

# 2. Run setup (installs deps + clones sub-repos)
# Mac/Linux:
chmod +x setup/setup.sh && ./setup/setup.sh
# Windows:
setup\setup.bat

# 3. Configure API keys
cp config/config.example.env config/.env
# Fill in your keys in config/.env

# 4. Run the orchestrator
python orchestrator.py
```

---

## 📁 Repository Structure

```
ai-content-empire/
├── README.md                  ← You are here
├── orchestrator.py            ← Main pipeline runner
├── requirements.txt           ← Python dependencies
├── docker-compose.yml         ← One-command Docker deploy
│
├── config/
│   ├── config.example.env     ← API keys template
│   └── personas.example.json  ← Character definitions
│
├── setup/
│   ├── setup.sh               ← Mac/Linux installer
│   └── setup.bat              ← Windows installer
│
├── pipeline/                  ← Layer 1: Video Production
│   ├── researcher.py          ← Trend/keyword research
│   ├── scriptwriter.py        ← LLM script generation
│   ├── video_generator.py     ← MoneyPrinterTurbo API wrapper
│   ├── clipper.py             ← Auto-clip to Shorts format
│   └── scheduler.py           ← Post scheduling (n8n/CRON)
│
├── avatars/                   ← Layer 2: Persona System
│   ├── realistic/
│   │   ├── portrait_animator.py   ← LivePortrait integration
│   │   ├── lip_sync.py            ← MuseTalk / Wav2Lip
│   │   └── voice_clone.py         ← FishSpeech / CosyVoice
│   └── animated/
│       ├── vtuber_engine.py       ← Open-LLM-VTuber integration
│       └── persona_manager.py     ← Multi-persona management
│
├── products/                  ← Layer 3: Digital Products
│   ├── ebook_generator.py     ← gpt-author / Gemini ebook builder
│   ├── pdf_formatter.py       ← PDF output with cover
│   └── storefront_lister.py   ← Auto-list to Gumroad / Etsy
│
├── distribution/              ← Layer 4: Distribution
│   ├── uploader.py            ← Multi-platform video uploader
│   ├── social_poster.py       ← Cross-platform social posting
│   └── affiliate_tracker.py   ← Referral link management
│
└── docs/
    ├── STACK.md               ← Full tool reference
    ├── ROADMAP.md             ← 90-day monetization plan
    ├── SETUP_GUIDE.md         ← Detailed setup walkthrough
    └── PERSONAS.md            ← Persona building guide
```

---

## 🔑 Required API Keys

| Service | Free Tier | Used For | Link |
|---------|-----------|----------|------|
| OpenAI or Gemini | ✅ Yes | Scripts, ebooks, SEO | [OpenAI](https://platform.openai.com) / [Google AI](https://ai.google.dev) |
| Pexels | ✅ Yes | Stock footage | [Pexels API](https://www.pexels.com/api/) |
| ElevenLabs | ✅ Limited | Voice synthesis | [ElevenLabs](https://elevenlabs.io) |
| Pixabay | ✅ Yes | Stock footage backup | [Pixabay API](https://pixabay.com/api/docs/) |
| YouTube Data API | ✅ Yes | Auto-upload Shorts | [Google Console](https://console.cloud.google.com) |

> **Start for free**: The core video pipeline runs entirely on free API tiers. Add paid tiers as revenue grows.

---

## 🧩 The Full Tech Stack

### 🎬 Layer 1 — Video Production
| Tool | Stars | Role |
|------|-------|------|
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | ⭐ 95k | Core video factory — topic → finished short video with auto-upload |
| [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | ⭐ 31k | Business wrapper — YT Shorts, Amazon affiliate, cold outreach |
| [AI-Youtube-Shorts-Generator](https://github.com/SaarD00/AI-Youtube-Shorts-Generator) | ⭐ 157 | Gemini-powered faceless shorts with A/B dual-visual system |
| [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | ⭐ 2.8k | SEO ops, trend scouting, YouTube competitive analysis, content scoring |

### 🎭 Layer 2A — Realistic Human Avatars (UGC-style)
| Tool | Stars | Role |
|------|-------|------|
| [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | ⭐ 18.7k | Animate any photo into a realistic talking face |
| [EchoMimicV2](https://github.com/antgroup/echomimic_v2) | ⭐ 4.6k | Half-body audio-driven animation — CVPR 2025 |
| [MuseTalk](https://github.com/TMElyralab/MuseTalk) | ⭐ 6.1k | Real-time high-quality lip sync by Tencent |
| [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | ⭐ 13.1k | Battle-tested lip sync for any video + audio |
| [SadTalker](https://github.com/OpenTalker/SadTalker) | ⭐ 13.9k | Single photo → full talking head with expressions |
| [AIGCPanel](https://github.com/modstart-lib/aigcpanel) | ⭐ 5.2k | All-in-one desktop studio: lip sync + voice clone + 25+ tools |

### 🤖 Layer 2B — Animated Character Avatars
| Tool | Stars | Role |
|------|-------|------|
| [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | ⭐ 12.2k | Live2D animated persona + any LLM + full voice system |
| [Fay](https://github.com/xszyou/Fay) | ⭐ 12.9k | Digital human agent framework — multi-persona, multi-platform |
| [LiveTalking](https://github.com/lipku/LiveTalking) | ⭐ 8.1k | Real-time 24/7 streaming digital human via RTMP/WebRTC |
| [talking-avatar-with-ai](https://github.com/asanchezyali/talking-avatar-with-ai) | ⭐ 445 | 3D avatar with emotional expressions + body animations |
| [handcrafted-persona-engine](https://github.com/elevenyellow/handcrafted-persona-engine) | ⭐ 1.3k | Live2D + voice cloning for consistent brand personas |

### 📚 Layer 3 — Digital Products
| Tool | Stars | Role |
|------|-------|------|
| [gpt-author](https://github.com/mshumer/gpt-author) | ⭐ 2.5k | Full book/guide → EPUB from one prompt (~$4 per book) |
| [eBook-Generator-AI-Agent](https://github.com/UltronTheAI/eBook-Generator-AI-Agent) | ⭐ 7 | Gemini ebook → PDF with cover, TOC, and chapters |
| [income-agent](https://github.com/papacasper/income-agent) | ⭐ 2 | Multi-agent: market scan → create product → list → track revenue |
| [etsy-digital-mockup-tools](https://github.com/devonjhills/etsy-digital-mockup-tools) | ⭐ 8 | Auto-list products on Etsy with AI-written SEO titles/descriptions |

### 📡 Layer 4 — Distribution & Automation
| Tool | Stars | Role |
|------|-------|------|
| [ai-content-automation-n8n](https://github.com/theone-ctrl/ai-content-automation-n8n) | ⭐ 22 | n8n workflow: script → TTS → images → video → scheduled post |
| [AI-YouTube-Channel-Automation](https://github.com/FuturewithAI-us/AI-YouTube-Channel-Automation) | ⭐ 12 | Full YouTube channel lifecycle Dockerized blueprint |

---

## 💰 Revenue Streams

| Stream | Timeline | Est. Monthly (at scale) |
|--------|----------|------------------------|
| YouTube AdSense | 60-90 days to qualify | $500–$5,000+ |
| TikTok Creator Fund | 30 days to qualify | $200–$2,000+ |
| Affiliate Referrals (credit/finance) | Day 1 | $50–$200 per conversion |
| Digital Product Sales (Gumroad/Etsy) | Day 1 | $500–$5,000+ |
| Sponsored Content | 90+ days | Varies |

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 8 GB | 16 GB+ |
| CPU | 4 cores | 8 cores |
| GPU | Not required* | NVIDIA 8GB+ VRAM |
| Storage | 20 GB | 50 GB+ |
| Python | 3.11+ | 3.11+ |

> *GPU required for avatar tools (MuseTalk, EchoMimic, LivePortrait). Layer 1 video pipeline is CPU-only.

---

## 📖 Documentation

| File | Description |
|------|-------------|
| [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md) | Full step-by-step install for every tool |
| [docs/STACK.md](docs/STACK.md) | Every repo, what it does, and how to use it |
| [docs/ROADMAP.md](docs/ROADMAP.md) | 90-day monetization plan with milestones |
| [docs/PERSONAS.md](docs/PERSONAS.md) | How to create and manage your content personas |

---

## ⚠️ Important Guidelines

- **Copyright**: Only use royalty-free footage (Pexels, Pixabay, your own recordings). Never download and re-edit someone else's content.
- **AI Disclosure**: YouTube and TikTok require labeling AI-generated realistic content. Always comply with platform rules.
- **Start with Layer 1**: The video pipeline runs today on free API keys. Add avatar and product layers as you scale.
- **Build Original Content**: The goal is to recreate winning *formats* and *styles* — not copy anyone's content.

---

## 📄 License

MIT License — use freely, build your empire, share improvements.

---

*Built with 🤖 and a money-making mindset.*
