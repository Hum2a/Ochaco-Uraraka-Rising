#!/usr/bin/env python3
"""
Downloads a free font for the Ochaco mod (optional).
Run: pip install requests && python scripts/download_font.py

Uses Google Fonts (OFL license). Picks a bold/anime-adjacent font.
"""
import os
import urllib.request

FONTS_DIR = os.path.join(os.path.dirname(__file__), "..", "fonts")
os.makedirs(FONTS_DIR, exist_ok=True)

# Bebas Neue - bold, impactful (OFL license)
# Alternative: Orbitron, Russo One, etc.
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/bebasneue/BebasNeue-Regular.ttf"
OUTPUT = os.path.join(FONTS_DIR, "ochaco.ttf")

print("Downloading Bebas Neue (bold, anime-adjacent)...")
try:
    urllib.request.urlretrieve(FONT_URL, OUTPUT)
    print(f"Created: {OUTPUT}")
    print("Add to manifest: \"fonts\": [{ \"id\": \"1\", \"name\": \"Ochaco\", \"path\": \"fonts/ochaco.ttf\" }]")
except Exception as e:
    print(f"Error: {e}")
    print("Manual: Download from https://fonts.google.com/specimen/Bebas+Neue, save as fonts/ochaco.ttf")
