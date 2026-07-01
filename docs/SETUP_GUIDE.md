# 🛠️ Setup Guide

> Complete step-by-step installation guide for AI Content Empire.
> Estimated time: 30-60 minutes for first full setup.

---

## Prerequisites

Before you start, make sure you have:

- **Python 3.11+** — [Download here](https://www.python.org/downloads/)
- **Git** — [Download here](https://git-scm.com/downloads)
- **ffmpeg** — [Download here](https://ffmpeg.org/download.html) (Mac: `brew install ffmpeg`)
- At least **8GB RAM** and **20GB free disk space**

---

## Step 1 — Clone the Repo

```bash
git clone https://github.com/jjisjazzed/ai-content-empire.git
cd ai-content-empire
```

---

## Step 2 — Run Setup Script

**Mac / Linux:**
```bash
chmod +x setup/setup.sh
./setup/setup.sh
```

**Windows:**
```bat
setup\setup.bat
```

This script will:
- Create a Python virtual environment (`.venv/`)
- Install all Python dependencies
- Clone MoneyPrinterTurbo, ai-marketing-skills, gpt-author into `tools/`
- Create output directories
- Copy `config/config.example.env` → `config/.env`

---

## Step 3 — Get Your FREE API Keys

Open `config/.env` in any text editor and fill in:

### 🔑 Required (to generate videos)

**Pexels API Key (FREE)**
1. Go to https://www.pexels.com/api/
2. Create a free account
3. Copy your API key
4. Set: `PEXELS_API_KEY=your_key_here`

**Gemini API Key (FREE)**
1. Go to https://ai.google.dev
2. Click 'Get API Key'
3. Create a project and copy the key
4. Set: `GEMINI_API_KEY=your_key_here`

### 🔑 Recommended (for better voice quality)

**ElevenLabs (FREE tier: 10,000 chars/month)**
1. Go to https://elevenlabs.io
2. Create a free account
3. Go to Profile → API Key
4. Set: `ELEVEN_LABS_API_KEY=your_key_here`

---

## Step 4 — Test the Video Pipeline

Activate your virtual environment:

```bash
# Mac/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate
```

Run your first test:

```bash
python orchestrator.py --niche credit_repair --layer 1
```

Expected output:
```
==================================================
  AI Content Empire Orchestrator
==================================================

--- Processing niche: credit_repair ---

[Layer 1] Generating video for niche: credit_repair
  Topic: How to raise your credit score 100 points in 90 days
  Output: ./output/videos/credit_repair/20260701_120000.mp4
  [+] Video generated successfully

==================================================
  Run Complete
==================================================
  Videos generated: 1
```

---

## Step 5 — Configure Your Niches

In `config/.env`, set your target niches:

```env
CONTENT_NICHES=credit_repair,personal_finance
```

Available niches (see `orchestrator.py` for full topic lists):
- `credit_repair`
- `personal_finance`
- `investing`

Add your own by editing the `NICHE_TOPICS` dict in `orchestrator.py`.

---

## Step 6 — Set Up Auto-Posting (Optional)

For YouTube auto-upload, you need YouTube Data API credentials:

1. Go to https://console.cloud.google.com
2. Create a new project
3. Enable 'YouTube Data API v3'
4. Create OAuth 2.0 credentials
5. Download the JSON and follow MoneyPrinterTurbo's upload guide:
   → `tools/MoneyPrinterTurbo/README.md`

Once configured, set in `config/.env`:
```env
AUTO_UPLOAD=true
```

---

## Step 7 — Set Up Avatar Layer (Optional, GPU Required)

For realistic human avatars:

```bash
# Clone AIGCPanel for easy GUI-based avatar production
git clone https://github.com/modstart-lib/aigcpanel.git tools/aigcpanel

# Follow AIGCPanel's own setup guide:
# https://github.com/modstart-lib/aigcpanel#installation
```

For animated VTuber characters:

```bash
git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber.git tools/Open-LLM-VTuber
# Follow: https://open-llm-vtuber.github.io/docs/quick-start
```

---

## Step 8 — Generate Digital Products

```bash
# Install Jupyter if not already installed
pip install jupyter

# Launch the gpt-author notebook
cd tools/gpt-author
jupyter notebook Claude_Author.ipynb
```

In the notebook, set your prompt to something like:
```
"A practical guide to repairing credit scores for beginners.
Focus on actionable steps, real examples, and common mistakes to avoid.
Target audience: adults 25-45 who have experienced financial hardship."
```

The output EPUB can be sold directly on Gumroad for $9-$27.

---

## Troubleshooting

**'ffmpeg not found' error**
- Mac: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`
- Windows: Download from https://ffmpeg.org/download.html and add to PATH

**'MoneyPrinterTurbo not found'**
- Run `./setup/setup.sh` again — it clones all tool repos

**Video generation timeout**
- The default timeout is 5 minutes. For slow connections, edit `timeout=300` in `orchestrator.py`

**API rate limit errors**
- Add delays between requests or upgrade to paid API tiers
- Gemini free tier: 15 requests/minute
- Pexels free tier: 200 requests/hour

---

## Next Steps

Once you have videos generating locally:
1. Read [ROADMAP.md](ROADMAP.md) for the 90-day monetization plan
2. Set up your YouTube and TikTok accounts
3. Sign up for affiliate programs (Credit Karma, Personal Capital, etc.)
4. Start posting daily — consistency is everything

---

*Questions? Open an issue on the repo.*
