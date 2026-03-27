#!/usr/bin/env python3
"""
Pink → brown gradient cursor (optional; global webmodding handles most UX).
Run: pip install Pillow && python scripts/generate_cursor.py
"""
import base64
import os

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

SIZE = 32
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "cursor")
WEBMODS_DIR = os.path.join(os.path.dirname(__file__), "..", "webmodding")
os.makedirs(OUTPUT_DIR, exist_ok=True)

PINK = (236, 64, 122)
BROWN = (109, 76, 65)

img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
pixels = img.load()

for y in range(SIZE):
    for x in range(SIZE):
        dist = abs((x - y) - 0)
        if dist <= 3 and 4 <= x <= 26 and 4 <= y <= 26:
            t = max(0, min(1, (x + y) / 52))
            r = int(PINK[0] + (BROWN[0] - PINK[0]) * t)
            g = int(PINK[1] + (BROWN[1] - PINK[1]) * t)
            b = int(PINK[2] + (BROWN[2] - PINK[2]) * t)
            pixels[x, y] = (r, g, b, 255)
        elif x >= 20 and y >= 20 and (x - 20) + (y - 20) <= 14:
            t = ((x - 20) + (y - 20)) / 14
            r = int(PINK[0] + (BROWN[0] - PINK[0]) * t)
            g = int(PINK[1] + (BROWN[1] - PINK[1]) * t)
            b = int(PINK[2] + (BROWN[2] - PINK[2]) * t)
            pixels[x, y] = (r, g, b, 255)

png_path = os.path.join(OUTPUT_DIR, "default.png")
img.save(png_path)
print(f"Created: {png_path}")

try:
    from win_cur.cursor import Cursor

    cur = Cursor()
    cur.add_cursor(img.width, img.height, 28, 28, img.tobytes())
    cur_path = os.path.join(OUTPUT_DIR, "default.cur")
    cur.save_file(cur_path)
    print(f"Created: {cur_path}")
except ImportError:
    print("Optional: pip install win-cur for default.cur")

# Optional standalone cursor.css (not in manifest — Ann-style uses global CSS only)
with open(png_path, "rb") as f:
    data_url = "data:image/png;base64," + base64.b64encode(f.read()).decode()

cursor_css = f'''/* Ochaco Uraraka: Rising — optional embedded cursor (not loaded by default manifest) */

html,
body {{
  cursor: url("{data_url}") 0 0, auto !important;
}}
'''

optional = os.path.join(WEBMODS_DIR, "cursor-optional.css")
with open(optional, "w", encoding="utf-8") as f:
    f.write(cursor_css)
print(f"Wrote (optional): {optional}")
