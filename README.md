# Tool Use Cases
Static AI-tools-by-use-case directory. Edit data in `build.py`, then:
    python3 build.py && cd site && python3 -m http.server 8000
Deploy: publish the `site/` folder (GitHub Pages via Actions, Cloudflare Pages, Netlify — all free).
Share image: `python3 make_og.py` regenerates static/og-image.png (1200x630); build.py copies static/ into site/ and writes feed.xml + the IndexNow key file.
