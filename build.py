#!/usr/bin/env python3
"""Tiny static generator for Tool Use Cases. Run: python3 build.py -> ./site"""
import os, html, json, shutil
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
EMAIL = "larrys@lalipublications.com"
BASE = "https://tools.lalipublications.com/"
TAG = "Which AI tool for which job — for vibe coders and builders."

T = {  # slug: (name, url, what it is)
 "cursor": ("Cursor", "https://cursor.com", "AI-first code editor (VS Code fork) with chat, inline edits and an agent mode."),
 "claude": ("Claude", "https://claude.ai", "Anthropic's AI assistant, strong at long documents, writing and code."),
 "claude-code": ("Claude Code", "https://www.anthropic.com/claude-code", "Anthropic's terminal-based agentic coding tool."),
 "chatgpt": ("ChatGPT", "https://chatgpt.com", "OpenAI's general-purpose AI assistant with chat, images, voice and search."),
 "codex": ("OpenAI Codex", "https://openai.com/codex/", "OpenAI's coding agent that works on repos in the cloud or CLI."),
 "copilot": ("GitHub Copilot", "https://github.com/features/copilot", "AI pair programmer built into VS Code, JetBrains and GitHub."),
 "v0": ("v0", "https://v0.dev", "Vercel's AI app/UI builder that generates React + Tailwind apps from prompts."),
 "lovable": ("Lovable", "https://lovable.dev", "Prompt-to-full-stack web app builder with Supabase integration."),
 "replit": ("Replit Agent", "https://replit.com", "Browser IDE with an agent that builds and deploys apps from a prompt."),
 "bolt": ("Bolt.new", "https://bolt.new", "StackBlitz's in-browser prompt-to-app builder."),
 "windsurf": ("Windsurf", "https://windsurf.com", "AI code editor with an agentic 'Cascade' assistant."),
 "aider": ("Aider", "https://aider.chat", "Open-source AI pair programming in your terminal, git-aware."),
 "devin": ("Devin", "https://devin.ai", "Cognition's autonomous software engineering agent."),
 "gemini": ("Gemini", "https://gemini.google.com", "Google's AI assistant with huge context windows and Google integration."),
 "perplexity": ("Perplexity", "https://www.perplexity.ai", "AI answer engine that searches the web and cites sources."),
 "notebooklm": ("NotebookLM", "https://notebooklm.google.com", "Google's research notebook grounded in your own uploaded sources."),
 "elicit": ("Elicit", "https://elicit.com", "AI research assistant for finding and summarizing academic papers."),
 "notion-ai": ("Notion AI", "https://www.notion.com/product/ai", "AI writing and Q&A built into Notion workspaces."),
 "grammarly": ("Grammarly", "https://www.grammarly.com", "Writing assistant for grammar, tone and rewrites everywhere you type."),
 "midjourney": ("Midjourney", "https://www.midjourney.com", "Image generator known for strong aesthetic, artistic output."),
 "dalle": ("ChatGPT Images", "https://chatgpt.com", "OpenAI image generation inside ChatGPT, good at following instructions and text."),
 "ideogram": ("Ideogram", "https://ideogram.ai", "Image generator especially good at legible text in images."),
 "flux": ("FLUX (Black Forest Labs)", "https://bfl.ai", "Family of high-quality image models, some with open weights."),
 "firefly": ("Adobe Firefly", "https://firefly.adobe.com", "Adobe's generative image tools, trained for commercial-safe use."),
 "sd": ("Stable Diffusion", "https://stability.ai", "Open image model family you can run locally (e.g. via ComfyUI)."),
 "runway": ("Runway", "https://runwayml.com", "AI video generation and editing suite (Gen-series models)."),
 "elevenlabs": ("ElevenLabs", "https://elevenlabs.io", "Realistic AI voiceover, voice cloning and dubbing."),
 "descript": ("Descript", "https://www.descript.com", "Edit video and podcasts by editing the transcript."),
 "heygen": ("HeyGen", "https://www.heygen.com", "AI avatar videos and video translation."),
 "capcut": ("CapCut", "https://www.capcut.com", "Free-tier video editor with auto-captions and AI effects."),
 "opus": ("OpusClip", "https://www.opus.pro", "Turns long videos into short vertical clips automatically."),
 "veo": ("Google Veo", "https://deepmind.google/models/veo/", "Google DeepMind's text-to-video model with native audio."),
 "sora": ("Sora", "https://openai.com/sora", "OpenAI's text-to-video model and app."),
 "rosebud": ("Rosebud AI", "https://rosebud.ai", "Browser tool for making games from prompts (Three.js/Phaser)."),
 "scenario": ("Scenario", "https://www.scenario.com", "Generates style-consistent game art assets from your own training sets."),
 "meshy": ("Meshy", "https://www.meshy.ai", "Text/image-to-3D model generation for game assets."),
 "suno": ("Suno", "https://suno.com", "Generates full songs, handy for placeholder game/video music."),
 "sentry": ("Sentry (Seer)", "https://sentry.io", "Error monitoring with AI root-cause analysis and fix suggestions."),
 "deepseek": ("DeepSeek", "https://www.deepseek.com", "Chinese AI lab with strong, low-cost open-weight reasoning models."),
 "ollama": ("Ollama", "https://ollama.com", "Run open models (Llama, Qwen, etc.) locally with one command."),
 "manus": ("Manus", "https://manus.im", "General-purpose autonomous agent that browses and completes multi-step tasks."),
 "kling": ("Kling", "https://klingai.com", "Kuaishou's text/image-to-video generator."),
 "grok": ("Grok", "https://grok.com", "xAI's assistant with real-time X/web search."),
 "mcp": ("Model Context Protocol", "https://modelcontextprotocol.io", "Open standard for connecting AI agents to tools and data."),
}

UC = [
 ("best-ai-for-vibe-coding","Best AI for vibe coding","Describe it, run it, tweak it. Tools that let you build software mostly by talking.",[
  ("cursor","The default pick: you keep a real codebase and editor, but most of the typing is done by the AI."),
  ("lovable","Fastest path from idea to a working web app with auth and a database, no setup."),
  ("v0","Best when you want a polished React/Next.js UI fast and plan to deploy on Vercel."),
  ("replit","Everything in the browser, including hosting — good for quick shareable prototypes."),
  ("bolt","Similar to Lovable; great for spinning up a full-stack demo in one tab."),
  ("windsurf","Cursor alternative with a strong agent; worth trying if Cursor isn't clicking.")]),
 ("best-ai-coding-agents","Best AI coding agents","Agents that take a task, edit multiple files, run commands and come back with a diff.",[
  ("claude-code","Excellent at multi-file changes from the terminal; a favorite for serious agentic work."),
  ("cursor","Agent mode inside a full editor, so you can review every change visually."),
  ("codex","Hand off tasks to run in parallel in the cloud and review the resulting PRs."),
  ("copilot","Copilot's coding agent works from GitHub issues — natural fit if your team lives on GitHub."),
  ("devin","Built for delegating whole tickets end to end; pricier, aimed at teams."),
  ("aider","Free, open-source, bring-your-own-model; makes clean git commits for each change.")]),
 ("best-ai-for-fixing-broken-code","Best AI for fixing broken code and errors","Paste the stack trace, get a fix. Tools that are good at debugging, not just generating.",[
  ("claude","Paste the error plus the relevant files; strong at reasoning about the actual root cause."),
  ("cursor","Fixes in place with full project context — no copy-paste back and forth."),
  ("chatgpt","Good general debugger, and can run Python to reproduce issues."),
  ("copilot","'Fix' and '/explain' right in the editor where the red squiggle is."),
  ("sentry","Catches errors in production and suggests fixes using real traces."),
  ("claude-code","Let it run the tests, read the failure, and iterate until green.")]),
 ("best-ai-for-game-prototyping","Best AI for game prototyping","Get a playable idea on screen fast — code, art, 3D and music.",[
  ("rosebud","Prompt a browser game into existence and remix others' games."),
  ("cursor","For real engines (Godot, Unity, Phaser): AI writes the scripts, you play-test."),
  ("scenario","Keeps game art consistent in your own style — the hard part of AI art for games."),
  ("meshy","Quick 3D props and characters to block out levels."),
  ("suno","Placeholder (or final) soundtrack in minutes."),
  ("elevenlabs","Character voice lines and sound effects without a recording booth.")]),
 ("best-ai-for-video-youtube","Best AI for video and YouTube","Generate footage, edit faster, voice it, and cut it into Shorts.",[
  ("descript","Edit talking-head videos like a doc; removes filler words. Huge time saver for YouTubers."),
  ("runway","Pro-grade AI video generation and editing tools for b-roll and effects."),
  ("veo","High-quality generated clips with sound; strong for cinematic b-roll."),
  ("elevenlabs","Best-in-class voiceover and dubbing into other languages."),
  ("opus","Turns a long video or stream into Shorts/TikToks automatically."),
  ("capcut","Free-ish editor with solid auto-captions — the practical everyday tool."),
  ("heygen","Avatar presenters and lip-synced translation when you don't want to be on camera.")]),
 ("best-ai-writing-assistants","Best AI writing assistants","Drafting, editing and rewriting — docs, blog posts, READMEs, emails.",[
  ("claude","The most natural-sounding prose of the big assistants; great editor."),
  ("chatgpt","Versatile all-rounder; Canvas mode helps with longer drafts."),
  ("notion-ai","Best if your notes and docs already live in Notion."),
  ("grammarly","Polish anywhere you type — browser, email, docs."),
  ("gemini","Convenient inside Google Docs and Gmail.")]),
 ("best-ai-for-research","Best AI for research","Find sources, read them, and summarize — with citations you can check.",[
  ("perplexity","Fast cited answers from the live web; the go-to for quick research."),
  ("notebooklm","Upload your own sources and get grounded answers (and audio overviews)."),
  ("chatgpt","Deep research mode produces long, cited reports on a topic."),
  ("gemini","Deep Research plus Google Search integration."),
  ("elicit","Purpose-built for academic papers and literature reviews."),
  ("grok","Useful for what people are saying right now on X.")]),
 ("best-ai-image-generation","Best AI image generation","Thumbnails, concept art, mockups, memes.",[
  ("midjourney","Best default look; great for art, moodboards and concept art."),
  ("dalle","Best at following detailed instructions and editing by conversation."),
  ("ideogram","Pick this when the image needs readable text — logos, posters, thumbnails."),
  ("flux","Top-tier quality with open-weight options for local use."),
  ("firefly","Safer for commercial work; built into Photoshop."),
  ("sd","Free and local if you have a GPU and like tinkering (ComfyUI).")]),
 ("best-ai-for-running-local-models","Best tools for running AI locally","Private, free-to-run AI on your own machine.",[
  ("ollama","One command to download and run open models; the easiest start."),
  ("deepseek","Strong open-weight models you can run locally or cheaply via API."),
  ("aider","Pair it with a local model for an offline coding assistant."),
  ("sd","The classic local image model ecosystem.")]),
]

NEW = [
 ("claude-code","Anthropic's terminal coding agent — one of the most talked-about dev tools."),
 ("codex","OpenAI's relaunched Codex coding agent (cloud + CLI)."),
 ("veo","Google's video model, now generating synced audio."),
 ("sora","OpenAI's video model, now with its own social app."),
 ("manus","Autonomous general agent that went viral for multi-step tasks."),
 ("lovable","Fast-growing prompt-to-app builder."),
 ("notebooklm","Audio Overviews turned research notes into podcasts."),
 ("kling","Strong contender in AI video generation."),
 ("deepseek","Open-weight reasoning models that shook up pricing."),
 ("mcp","The open protocol most agent tools now support for tool access."),
 ("windsurf","Agentic editor competing directly with Cursor."),
]

CSS = """*{box-sizing:border-box}body{margin:0;font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1d1d1f;background:#fafaf7}
a{color:#0b5cad}header,footer{background:#1d2a36;color:#eee}header a,footer a{color:#fff}
.wrap{max-width:960px;margin:0 auto;padding:0 18px}header .wrap{display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;padding:12px 18px}
.logo{font-weight:800;text-decoration:none;font-size:1.15rem;margin-right:auto}nav a{text-decoration:none;font-size:.95rem}
h1{font-size:1.9rem;line-height:1.2;margin:28px 0 8px}.lede{color:#444;font-size:1.1rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin:18px 0}
.card{background:#fff;border:1px solid #ddd;border-radius:8px;padding:14px 16px}.card h3{margin:0 0 4px;font-size:1.08rem}
.card p{margin:4px 0}.what{color:#555;font-size:.93rem}.verdict b{color:#1d6b34}
.sponsored{border:2px dashed #c08a00;background:#fffaf0}.badge{display:inline-block;font-size:.72rem;font-weight:700;text-transform:uppercase;background:#c08a00;color:#fff;padding:2px 7px;border-radius:4px;margin-bottom:6px}
.btn{display:inline-block;background:#0b5cad;color:#fff;padding:9px 16px;border-radius:6px;text-decoration:none;font-weight:600}
input[type=search]{width:100%;padding:11px 14px;font-size:1rem;border:1px solid #bbb;border-radius:6px;margin:10px 0}
ol.tools{list-style:none;padding:0}ol.tools li{margin-bottom:12px}footer{margin-top:48px;padding:18px 0;font-size:.9rem}
.nl{background:#fff;border:2px solid #0b5cad;border-radius:8px;padding:16px;margin:28px 0}.nl h2{margin:0 0 4px}.nl form{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 4px}.nl input[type=email]{flex:1;min-width:200px;padding:10px 12px;font-size:1rem;border:1px solid #bbb;border-radius:6px}.nl button{background:#0b5cad;color:#fff;border:0;padding:10px 18px;border-radius:6px;font-weight:600;font-size:1rem;cursor:pointer}footer .nl{background:#26384a;border-color:#4a6a8a;color:#eee}footer .nl small{color:#ccc}
.cta{background:#eef4fb;border:1px solid #cbdcef;border-radius:8px;padding:16px;margin:28px 0}small,.muted{color:#666}"""

JS = """document.querySelectorAll('[data-filter]').forEach(function(i){var t=document.querySelectorAll(i.dataset.filter);
i.addEventListener('input',function(){var q=i.value.toLowerCase().trim();t.forEach(function(c){c.style.display=!q||c.textContent.toLowerCase().indexOf(q)>-1?'':'none'})})});"""

e = html.escape
def canon(path): return BASE + (path[:-len("index.html")] if path.endswith("index.html") else path)
def nl_form(id_attr=""):
    return f"""<section class="nl"{id_attr}><h2>Weekly AI tool picks for vibe coders</h2><p>New tools + which job they fit. Free.</p>
<form action="https://formsubmit.co/{EMAIL}" method="POST"><input type="email" name="email" required placeholder="you@example.com" aria-label="Email address">
<input type="hidden" name="_subject" value="Tool Use Cases newsletter signup"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{BASE}thanks/">
<button type="submit">Subscribe</button></form><small>We email from Lali Publications. No spam, unsubscribe anytime.</small></section>"""
def page(path, title, desc, body, ld=None):
    depth = path.count("/")
    r = "../" * depth
    cu = canon(path)
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in (ld or []))
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<link rel="canonical" href="{cu}"><meta property="og:url" content="{cu}"><meta property="og:type" content="website"><meta property="og:site_name" content="Tool Use Cases"><meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{r}style.css">{lds}</head><body>
<header><div class="wrap"><a class="logo" href="{r}index.html">Tool Use Cases</a><nav><a href="{r}use-cases/index.html">Use cases</a> · <a href="{r}tools/index.html">Tools</a> · <a href="{r}new/index.html">New releases</a> · <a href="{r}newsletter/index.html">Newsletter</a> · <a href="{r}sponsor/index.html">Sponsor</a> · <a href="{r}about/index.html">About</a></nav></div></header>
<main class="wrap">{body.replace('@R/', r)}</main>
<footer><div class="wrap">{nl_form()}Tool Use Cases · by Lali Publications · sponsorships: <a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
<script src="{r}app.js"></script></body></html>"""
    f = os.path.join(OUT, path); os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w").write(doc)

def tool_link(s): n,u,_=T[s]; return f'<a href="{u}" rel="noopener" target="_blank">{e(n)}</a>'
def uc_card(slug,title,blurb,tools):
    return f'<div class="card f"><h3><a href="@R/use-cases/{slug}/index.html">{e(title)}</a></h3><p class="what">{e(blurb)}</p><p><small>{", ".join(e(T[t][0]) for t,_ in tools)}</small></p></div>'
SPONSOR_CARD = f'<div class="card sponsored"><span class="badge">Sponsored</span><h3>Your tool here</h3><p class="what">This featured slot is available to tool makers who fit this use case. Clearly labeled, always separate from our picks.</p><p><a href="mailto:{EMAIL}?subject=Sponsor%20Tool%20Use%20Cases">Email to sponsor</a></p></div>'

if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT); open(f"{OUT}/style.css","w").write(CSS); open(f"{OUT}/app.js","w").write(JS); open(f"{OUT}/.nojekyll","w").write("")

cards = "".join(uc_card(*u) for u in UC)
newteaser = "".join(f'<li>{tool_link(s)} — {e(n)}</li>' for s,n in NEW[:5])
page("index.html","Tool Use Cases — which AI tool for which job",TAG+" A curated directory of AI tools organized by use case.",f"""
<h1>Which AI tool for which job.</h1><p class="lede">Tool Use Cases is a directory of AI tools organized by the job you're trying to do — for vibe coders, builders, and anyone shipping with AI.</p>
<input type="search" placeholder="Filter use cases (e.g. video, coding, research)…" data-filter=".f" aria-label="Filter use cases">
<h2>Use cases</h2><div class="grid">{cards}</div>
{nl_form(' id="newsletter"')}
<h2>New releases &amp; trending</h2><ul>{newteaser}</ul><p><a href="@R/new/index.html">All new releases →</a></p>
<div class="cta"><b>Make an AI tool?</b> Get featured at the top of the use case your tool is best at. <a class="btn" href="@R/sponsor/index.html">Sponsor a slot</a></div>""", ld=[
 {"@context":"https://schema.org","@type":"WebSite","name":"Tool Use Cases","url":BASE,"description":TAG,"publisher":{"@type":"Organization","name":"Lali Publications","email":EMAIL}},
 {"@context":"https://schema.org","@type":"ItemList","name":"AI tool use cases","itemListElement":[{"@type":"ListItem","position":i,"name":u[1],"url":f"{BASE}use-cases/{u[0]}/"} for i,u in enumerate(UC,1)]}])

page("use-cases/index.html","AI tool use cases — Tool Use Cases","Browse AI tools by use case: vibe coding, coding agents, debugging, game prototyping, video, writing, research, images and more.",f"""
<h1>Use cases</h1><p class="lede">Pick the job. We list the tools worth trying and why.</p>
<input type="search" placeholder="Filter use cases…" data-filter=".f" aria-label="Filter"><div class="grid">{cards}</div>""")

for slug,title,blurb,tools in UC:
    items = "".join(f'<li class="card f"><h3>{i}. {tool_link(t)}</h3><p class="what">{e(T[t][2])}</p><p class="verdict"><b>Verdict:</b> {e(v)}</p></li>' for i,(t,v) in enumerate(tools,1))
    page(f"use-cases/{slug}/index.html",f"{title} (2026) — Tool Use Cases",f"{title}: {blurb} Plain-English verdicts on {', '.join(T[t][0] for t,_ in tools[:4])} and more.",f"""
<p><small><a href="@R/use-cases/index.html">Use cases</a> /</small></p><h1>{e(title)}</h1><p class="lede">{e(blurb)}</p>
{SPONSOR_CARD}<h2>Our picks</h2><ol class="tools">{items}</ol>
<p class="muted"><small>Picks are editorial and not paid. Pricing and features change often — check each official site.</small></p>""", ld=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
     {"@type":"ListItem","position":1,"name":"Home","item":BASE},{"@type":"ListItem","position":2,"name":"Use cases","item":BASE+"use-cases/"},{"@type":"ListItem","position":3,"name":title,"item":f"{BASE}use-cases/{slug}/"}]},
     {"@context":"https://schema.org","@type":"ItemList","name":title,"description":blurb,"url":f"{BASE}use-cases/{slug}/","itemListElement":[{"@type":"ListItem","position":i,"item":{"@type":"SoftwareApplication","name":T[t][0],"url":T[t][1],"description":T[t][2],"applicationCategory":"DeveloperApplication" if "cod" in slug or "vibe" in slug else "BusinessApplication",
       "review":{"@type":"Review","name":f"{T[t][0]} for {title}","reviewBody":v,"author":{"@type":"Organization","name":"Tool Use Cases (Lali Publications)"}}}} for i,(t,v) in enumerate(tools,1)]}])

uses = {}
for slug,title,_,tools in UC:
    for t,_ in tools: uses.setdefault(t,[]).append((slug,title))
rows = "".join(f'<div class="card f"><h3>{tool_link(s)}</h3><p class="what">{e(T[s][2])}</p><p><small>{" · ".join(f"<a href=@R/use-cases/{u}/index.html>{e(n)}</a>" for u,n in uses.get(s,[]))}</small></p></div>' for s in sorted(T,key=lambda k:T[k][0].lower()))
page("tools/index.html","All AI tools A–Z — Tool Use Cases","Every AI tool in the Tool Use Cases directory, with what it does and which use cases it fits.",f"""
<h1>All tools</h1><input type="search" placeholder="Filter tools…" data-filter=".f" aria-label="Filter tools"><div class="grid">{rows}</div>""")

nl = "".join(f'<div class="card f"><span class="badge" style="background:#1d6b34">Notable / trending</span><h3>{tool_link(s)}</h3><p class="what">{e(T[s][2])}</p><p>{e(n)}</p></div>' for s,n in NEW)
page("new/index.html","New & trending AI tools — Tool Use Cases","Notable and trending AI tool releases for builders: coding agents, video models, research tools and more.",f"""
<h1>New releases &amp; trending</h1><p class="lede">Recently launched or recently relaunched AI tools worth a look. We label these "notable / trending" rather than guessing exact launch dates.</p><div class="grid">{nl}</div>""")

page("sponsor/index.html","Sponsor Tool Use Cases — feature your AI tool","Tool makers can sponsor a clearly labeled featured slot at the top of relevant use-case pages.",f"""
<h1>Sponsor a use case</h1><p class="lede">Reach vibe coders and builders at the moment they're choosing a tool.</p>
<h2>How it works</h2><ul><li>One <b>Sponsored / Featured</b> slot sits at the top of each use-case page.</li><li>It's always clearly labeled "Sponsored" and kept separate from our editorial picks.</li><li>We only accept tools that genuinely fit the use case.</li><li>Sponsorship never changes our verdicts or rankings.</li></ul>
<h2>Example</h2>{SPONSOR_CARD}
<div class="cta">Pricing and availability on request. <a class="btn" href="mailto:{EMAIL}?subject=Sponsor%20Tool%20Use%20Cases">Email to sponsor</a></div>""")

page("about/index.html","About — Tool Use Cases","Tool Use Cases is an independent, autonomously run directory of AI tools organized by use case.",f"""
<h1>About</h1><p class="lede">Tool Use Cases answers one question: which AI tool should I use for this job?</p>
<p>Most AI directories are giant lists. We organize by use case instead, and give each pick a short plain-English verdict so you can decide in a minute.</p>
<p>The site is run autonomously — an AI operator keeps it updated, with human ownership by Lali Publications. We only list real, well-known tools and don't publish made-up scores or user counts.</p>
<p>Tool Use Cases is an independent directory and is not affiliated with any of the tools listed or with other "use cases" channels or publications.</p>
<p>Corrections, suggestions, or sponsorships: <a href="mailto:{EMAIL}">{EMAIL}</a></p>""")

page("newsletter/index.html","Tool Picks Weekly — free AI tool newsletter","Weekly AI tool picks for vibe coders, by job-to-be-done: new tools and which job they fit. Free, every Monday, from Lali Publications.",f"""
<h1>Tool Picks Weekly</h1><p class="lede">One short email every Monday: new AI tools and which job they actually fit.</p>
{nl_form(' id="newsletter"')}
<h2>What an issue covers</h2><ul><li><b>New &amp; notable:</b> 3–5 recent launches or big updates, each with the use case it fits.</li><li><b>Pick of the week:</b> one tool, one job, a plain-English verdict.</li><li><b>Workflow tip:</b> a concrete way to combine tools for vibe coding, video, or research.</li><li><b>Directory updates:</b> what changed on Tool Use Cases.</li></ul>
<p class="muted"><small>Picks are editorial. Any sponsored item is clearly labeled.</small></p>""")
page("thanks/index.html","Thanks for subscribing — Tool Use Cases","Your Tool Picks Weekly signup was received.",f"""
<h1>You're on the list. Thanks!</h1><p class="lede">Your signup for Tool Picks Weekly was received. Look out for the next issue on Monday.</p>
<p><a class="btn" href="@R/index.html">Back to Tool Use Cases</a></p>""")

urls = ["index.html","newsletter/index.html","use-cases/index.html","tools/index.html","new/index.html","sponsor/index.html","about/index.html"]+[f"use-cases/{u[0]}/index.html" for u in UC]
open(f"{OUT}/CNAME","w").write("tools.lalipublications.com\n")
full = [canon(u) for u in urls]
open(f"{OUT}/sitemap.txt","w").write("\n".join(full)+"\n")
open(f"{OUT}/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{u}</loc></url>\n" for u in full)+"</urlset>\n")
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
llms = [f"# Tool Use Cases", "", f"> {TAG} A curated, editorial directory of AI tools organized by the job you're trying to do. Published by Lali Publications.", "",
 "Our angle: tool choice by job-to-be-done for vibe coders. Each use-case page lists recommended tools with a one-line description and a plain-English verdict. Picks are editorial and not paid; sponsored slots are clearly labeled and separate.", "", "## Use cases", ""]
llms += [f"- [{t}]({BASE}use-cases/{s}/): {b}" for s,t,b,_ in UC]
llms += ["", "## Other pages", "", f"- [All tools A-Z]({BASE}tools/)", f"- [New & trending]({BASE}new/)", f"- [Newsletter]({BASE}newsletter/)", f"- [About]({BASE}about/)", "",
 "## Sponsor / contact", "", f"Sponsorships, corrections and suggestions: {EMAIL} (Lali Publications). See {BASE}sponsor/", "",
 "## How to cite", "", f'Tool Use Cases (Lali Publications), "[page title]", {BASE}[path]. Please link to the specific use-case page.', ""]
open(f"{OUT}/llms.txt","w").write("\n".join(llms))
print("built", len(urls), "pages ->", OUT)
