#!/usr/bin/env python3
"""Generate the 1200x630 Open Graph share image -> static/og-image.png (run once; build.py copies static/ into site/)."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
INTER = "/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"
def font(size, weight):
    f = ImageFont.truetype(INTER, size)
    try: f.set_variation_by_axes([32, weight])  # opsz, wght
    except Exception: pass
    return f
W, H = 1200, 630
NAVY, INK, ACCENT, MUTED = (29, 42, 54), (255, 255, 255), (91, 168, 245), (190, 204, 218)
im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
d.rectangle([0, 0, 18, H], fill=ACCENT)                      # left accent bar
x = 96
d.text((x, 96), "TOOL PICKS BY JOB", font=font(30, 700), fill=ACCENT)
d.text((x, 160), "Tool Use Cases", font=font(104, 800), fill=INK)
d.text((x, 300), "AI tools ranked by", font=font(56, 500), fill=INK)
d.text((x, 372), "the job you need done", font=font(56, 500), fill=INK)
d.line([x, 486, W - 96, 486], fill=(70, 90, 110), width=2)
d.text((x, 512), "tools.lalipublications.com", font=font(36, 600), fill=MUTED)
f = font(28, 500); t = "Free · Editorial picks"; tw = d.textlength(t, font=f)
d.text((W - 96 - tw, 518), t, font=f, fill=MUTED)
out = os.path.join(HERE, "static", "og-image.png"); os.makedirs(os.path.dirname(out), exist_ok=True)
im.save(out, optimize=True); print(out, im.size)
