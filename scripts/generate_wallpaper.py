#!/usr/bin/env python3
"""
Placeholder wallpaper: pink (quirk) → brown (hair) until you add your clip.

Run: pip install Pillow && python scripts/generate_wallpaper.py
"""
import os

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

WIDTH, HEIGHT = 1920, 1080
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "wallpaper")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Pink #f48fb1 left → warm brown #6d4c41 right
P0 = (0xF4, 0x8F, 0xB1)
P1 = (0x6D, 0x4C, 0x41)

img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()

for x in range(WIDTH):
    t = x / max(1, WIDTH - 1)
    r = int(P0[0] + (P1[0] - P0[0]) * t)
    g = int(P0[1] + (P1[1] - P0[1]) * t)
    b = int(P0[2] + (P1[2] - P0[2]) * t)
    for y in range(HEIGHT):
        pixels[x, y] = (r, g, b)

dark_path = os.path.join(OUTPUT_DIR, "dark.png")
img.save(dark_path)
print(f"Created: {dark_path}")

first_path = os.path.join(OUTPUT_DIR, "first_frame_ochaco.jpeg")
img.save(first_path, "JPEG", quality=92)
print(f"Created: {first_path}")
