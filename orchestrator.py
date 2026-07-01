"""
AI Content Empire - Main Orchestrator

This script coordinates all layers of the pipeline:
  Layer 1: Video content generation (MoneyPrinterTurbo)
  Layer 2: Avatar/persona integration (MuseTalk, Open-LLM-VTuber)
  Layer 3: Digital product creation (gpt-author)
  Layer 4: Distribution & scheduling

Usage:
  python orchestrator.py                    # Run full pipeline
  python orchestrator.py --layer 1          # Run only video pipeline
  python orchestrator.py --layer 3          # Run only product generation
  python orchestrator.py --niche credit     # Run for specific niche
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config/.env")

# ============================================================
# Configuration
# ============================================================

CONFIG = {
    "niches": os.getenv("CONTENT_NICHES", "credit_repair,personal_finance").split(","),
    "videos_per_run": int(os.getenv("VIDEOS_PER_RUN", "2")),
    "video_format": os.getenv("VIDEO_FORMAT", "portrait"),
    "language": os.getenv("VIDEO_LANGUAGE", "en"),
    "output_dir": Path(os.getenv("OUTPUT_DIR", "./output")),
    "auto_upload": os.getenv("AUTO_UPLOAD", "false").lower() == "true",
    "llm_provider": os.getenv("LLM_PROVIDER", "gemini"),
}

# Topic seeds per niche — expand these with your own ideas
NICHE_TOPICS = {
    "credit_repair": [
        "How to raise your credit score 100 points in 90 days",
        "5 credit card mistakes destroying your score",
        "How to dispute errors on your credit report",
        "Best credit cards for building credit from scratch",
        "What is a good credit score and how to get there",
        "How credit utilization affects your score",
        "Secured credit cards explained for beginners",
        "How long negative items stay on your credit report",
    ],
    "personal_finance": [
        "The 50/30/20 budget rule explained simply",
        "How to build a 6-month emergency fund fast",
        "Index funds vs stocks - what beginners should know",
        "How to pay off $10,000 in debt in 12 months",
        "The truth about compound interest over 30 years",
        "5 money habits that separate rich from poor",
        "How to negotiate a higher salary at work",
        "Roth IRA vs Traditional IRA - which is better",
    ],
    "investing": [
        "What is dollar cost averaging and why it works",
        "How to start investing with just $50 per month",
        "ETFs for beginners - the complete guide",
        "How Warren Buffett picks stocks",
        "Real estate vs stock market - which builds more wealth",
    ],
}


# ============================================================
# Layer 1: Video Pipeline
# ============================================================

def run_video_pipeline(niche: str, topic: str = None):
    """Generate a short video using MoneyPrinterTurbo API."""
    print(f"\n[Layer 1] Generating video for niche: {niche}")
    
    topics = NICHE_TOPICS.get(niche, NICHE_TOPICS["personal_finance"])
    if not topic:
        # Pick next unused topic (simple rotation)
        used_file = CONFIG["output_dir"] / f"{niche}_used_topics.json"
        used = json.loads(used_file.read_text()) if used_file.exists() else []
        remaining = [t for t in topics if t not in used]
        if not remaining:
            remaining = topics  # Reset cycle
            used = []
        topic = remaining[0]
        used.append(topic)
        used_file.parent.mkdir(parents=True, exist_ok=True)
        used_file.write_text(json.dumps(used))
    
    print(f"  Topic: {topic}")
    
    # Call MoneyPrinterTurbo via its API
    mpt_path = Path("tools/MoneyPrinterTurbo")
    if not mpt_path.exists():
        print("  [!] MoneyPrinterTurbo not found. Run setup/setup.sh first.")
        return None
    
    # Build the config for MoneyPrinterTurbo
    video_config = {
        "video_subject": topic,
        "video_language": CONFIG["language"],
        "video_aspect": "9:16" if CONFIG["video_format"] == "portrait" else "16:9",
        "video_count": 1,
        "llm_provider": CONFIG["llm_provider"],
    }
    
    # Output path
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = CONFIG["output_dir"] / "videos" / niche / f"{timestamp}.mp4"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"  Output: {output_path}")
    
    # Run MoneyPrinterTurbo CLI
    cmd = [
        sys.executable,
        str(mpt_path / "cli.py"),
        "--video-subject", topic,
    ]
    
    try:
        result = subprocess.run(cmd, cwd=mpt_path, capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print(f"  [+] Video generated successfully")
            return str(output_path)
        else:
            print(f"  [!] Error: {result.stderr[:200]}")
            return None
    except subprocess.TimeoutExpired:
        print("  [!] Video generation timed out (5 min limit)")
        return None
    except Exception as e:
        print(f"  [!] Exception: {e}")
        return None


# ============================================================
# Layer 3: Digital Product Generation
# ============================================================

def run_product_pipeline(niche: str, product_type: str = "ebook"):
    """Generate a digital product (ebook/guide) for a niche."""
    print(f"\n[Layer 3] Generating {product_type} for niche: {niche}")
    
    ebook_topics = {
        "credit_repair": "The Complete Credit Repair Blueprint: How to Build an 800 Credit Score",
        "personal_finance": "Zero to Wealthy: The Beginner's Complete Personal Finance System",
        "investing": "The Index Fund Investor: Building Wealth on Autopilot",
    }
    
    title = ebook_topics.get(niche, f"The Ultimate Guide to {niche.replace('_', ' ').title()}")
    print(f"  Title: {title}")
    
    gpt_author_path = Path("tools/gpt-author")
    if not gpt_author_path.exists():
        print("  [!] gpt-author not found. Run setup/setup.sh first.")
        return None
    
    output_path = CONFIG["output_dir"] / "products" / niche
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"  Output dir: {output_path}")
    print(f"  [i] To generate: run tools/gpt-author/Claude_Author.ipynb in Jupyter")
    print(f"      with prompt: '{title}'")
    
    return str(output_path)


# ============================================================
# Main Orchestrator
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="AI Content Empire Orchestrator")
    parser.add_argument("--layer", type=int, choices=[1, 2, 3, 4],
                        help="Run specific layer only (1=video, 2=avatars, 3=products, 4=distribution)")
    parser.add_argument("--niche", type=str, help="Specific niche to run (e.g., credit_repair)")
    parser.add_argument("--topic", type=str, help="Specific topic for video generation")
    parser.add_argument("--list-niches", action="store_true", help="List available niches and topics")
    args = parser.parse_args()
    
    print("")
    print("==================================================")
    print("  AI Content Empire Orchestrator")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==================================================")
    
    if args.list_niches:
        print("\nAvailable niches and topics:")
        for niche, topics in NICHE_TOPICS.items():
            print(f"\n  {niche}:")
            for t in topics:
                print(f"    - {t}")
        return
    
    # Determine which niches to run
    niches = [args.niche] if args.niche else CONFIG["niches"]
    
    # Create output directory
    CONFIG["output_dir"].mkdir(parents=True, exist_ok=True)
    
    results = {"videos": [], "products": [], "errors": []}
    
    for niche in niches:
        niche = niche.strip()
        print(f"\n--- Processing niche: {niche} ---")
        
        # Layer 1: Video Pipeline
        if not args.layer or args.layer == 1:
            for _ in range(CONFIG["videos_per_run"]):
                video_path = run_video_pipeline(niche, args.topic)
                if video_path:
                    results["videos"].append(video_path)
        
        # Layer 3: Digital Products
        if args.layer == 3:
            product_path = run_product_pipeline(niche)
            if product_path:
                results["products"].append(product_path)
    
    # Summary
    print("\n==================================================")
    print("  Run Complete")
    print("==================================================")
    print(f"  Videos generated: {len(results['videos'])}")
    print(f"  Products staged:  {len(results['products'])}")
    if results["errors"]:
        print(f"  Errors:           {len(results['errors'])}")
    print("")


if __name__ == "__main__":
    main()
