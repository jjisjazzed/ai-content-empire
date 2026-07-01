#!/bin/bash
# AI Content Empire - Mac/Linux Setup Script
# Run: chmod +x setup/setup.sh && ./setup/setup.sh

set -e

echo ""
echo "=================================================="
echo " AI Content Empire - Setup"
echo "=================================================="
echo ""

# Check Python 3.11+
if python3 -c 'import sys; assert sys.version_info >= (3,11)' 2>/dev/null; then
    echo "[+] Python 3.11+ confirmed"
else
    echo "[!] Python 3.11+ required. Install from https://python.org"
    exit 1
fi

# Check Git
if ! command -v git &> /dev/null; then
    echo "[!] Git not found. Install from https://git-scm.com"
    exit 1
fi
echo "[+] Git confirmed"

# Check ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "[!] ffmpeg not found. Installing via brew/apt..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ffmpeg
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y ffmpeg
    fi
else
    echo "[+] ffmpeg confirmed"
fi

# Virtual environment
echo ""
echo "[+] Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -q

echo "[+] Installing Python dependencies..."
pip install -r requirements.txt -q

# Clone tool repos
echo ""
echo "[+] Cloning tool repositories..."
mkdir -p tools

clone_if_missing() {
    if [ ! -d "tools/$2" ]; then
        echo "  Cloning $2..."
        git clone $1 tools/$2 -q
    else
        echo "  $2 already cloned"
    fi
}

clone_if_missing https://github.com/harry0703/MoneyPrinterTurbo.git MoneyPrinterTurbo
clone_if_missing https://github.com/ericosiu/ai-marketing-skills.git ai-marketing-skills
clone_if_missing https://github.com/mshumer/gpt-author.git gpt-author
clone_if_missing https://github.com/FujiwaraChoki/MoneyPrinterV2.git MoneyPrinterV2

# Install MoneyPrinterTurbo deps
echo "[+] Installing MoneyPrinterTurbo dependencies..."
pip install -r tools/MoneyPrinterTurbo/requirements.txt -q 2>/dev/null || true

# Create output dirs
mkdir -p output/videos output/avatars output/products

# Copy config template
if [ ! -f "config/.env" ]; then
    cp config/config.example.env config/.env
    echo ""
    echo "[!] ACTION REQUIRED: Fill in your API keys in config/.env"
else
    echo "[+] config/.env already exists"
fi

echo ""
echo "=================================================="
echo " Setup Complete!"
echo "=================================================="
echo ""
echo " Next steps:"
echo " 1. Edit config/.env with your API keys"
echo " 2. Run: source .venv/bin/activate"
echo " 3. Run: python orchestrator.py"
echo ""
