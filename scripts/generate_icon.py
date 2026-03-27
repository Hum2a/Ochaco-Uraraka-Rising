#!/usr/bin/env python3
"""
512×512 mod icon from ochacojpg.jpg (fallback: procedural pink/brown).
Run: pip install Pillow && python scripts/generate_icon.py
"""
import os

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

SIZE = 512
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..")
OUTPUT = os.path.join(PROJECT_ROOT, "icon_512.png")
SRC = os.path.join(PROJECT_ROOT, "ochacojpg.jpg")


def icon_cover(img, size: int):
    src = img.convert("RGBA")
    w, h = src.size
    if w == h:
        return src.resize((size, size), Image.Resampling.LANCZOS)
    scale = max(size / w, size / h)
    nw, nh = int(w * scale), int(h * scale)
    resized = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - size) // 2
    top = (nh - size) // 2
    return resized.crop((left, top, left + size, top + size))


def procedural():
    img = Image.new("RGBA", (SIZE, SIZE), (62, 39, 35, 255))
    draw = ImageDraw.Draw(img)
    for r in range(240, 20, -28):
        a = min(100, 20 + (240 - r) // 3)
        draw.ellipse(
            (SIZE // 2 - r, SIZE // 2 - r, SIZE // 2 + r, SIZE // 2 + r),
            outline=(236, 64, 122, a),
            width=3,
        )
    draw.ellipse((96, 96, 416, 416), fill=(236, 64, 122, 90))
    draw.ellipse((176, 176, 336, 336), fill=(109, 76, 65, 180))
    return img


if os.path.isfile(SRC):
    icon = icon_cover(Image.open(SRC), SIZE)
else:
    icon = procedural()

icon.save(OUTPUT)
print(f"Created: {OUTPUT}")
