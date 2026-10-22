"""Tamil (ta) locale for Tool Use Cases.
Style: natural, conversational modern Tamil the way Tamil tech creators write. Product names and common
tech terms (vibe coding, AI agent, deploy, debugging, RAG, API, prompt...) stay in Latin script.
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "ta"
PREFIX = "ta/"
SHORT = "TA"
NATIVE = "தமிழ்"
ENGLISH_NAME = "Tamil"
INDIA = True
OG_LOCALE = "ta_IN"
RSS_LANG = "ta"

TAG = "எந்த வேலைக்கு எந்த AI tool — vibe coders, builders-க்காக."

UI = {
 "nav_use_cases": "Use cases", "nav_tools": "Tools", "nav_new": "புதிய launches",
 "nav_newsletter": "Newsletter", "nav_sponsor": "Sponsor", "nav_about": "எங்களைப் பற்றி",
 "home": "முகப்பு", "use_cases": "Use cases",
 "og_alt": "Tool Use Cases: உங்கள் வேலைக்கு ஏற்ப rank செய்யப்பட்ட AI tools",
 "footer": "Tool Use Cases · Lali Publications வழங்குவது · sponsorship-க்கு:",
 "nl_h2": "Vibe coders-க்கு ஒவ்வொரு வாரமும் தேர்ந்தெடுத்த AI tools",
 "nl_p": "புதிய tools + எந்த tool எந்த வேலைக்குப் பொருந்தும். முற்றிலும் இலவசம். இப்போதைக்கு newsletter ஆங்கிலத்தில் வருகிறது.",
 "nl_placeholder": "neengal@example.com", "nl_aria": "Email முகவரி", "nl_button": "Subscribe செய்யுங்கள்",
 "nl_subject": "Tool Use Cases newsletter signup (ta)",
 "nl_small": "Email Lali Publications-இடமிருந்து வரும். Spam இல்லை, எப்போது வேண்டுமானாலும் unsubscribe செய்யலாம்.",
 "nl_latest": "சமீபத்திய issue-ஐப் படியுங்கள்: {LINK} (ஆங்கிலத்தில்).",
 "verdict": "எங்கள் கருத்து:", "our_picks": "எங்கள் தேர்வுகள்", "related": "தொடர்புடைய use cases",
 "browse_all": "எல்லா use cases-ஐயும் பாருங்கள் →",
 "disclaimer": "இந்தத் தேர்வுகள் எங்களுடையவை, இதற்காக யாரும் பணம் தரவில்லை. விலைகளும் features-உம் அடிக்கடி மாறும் — ஒவ்வொரு tool-இன் official site-ஐயும் சரிபாருங்கள்.",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} {names} மற்றும் மற்ற tools பற்றிய எங்கள் கருத்து.",
 "review_name": "{tool} — {title}",
 "sponsored": "Sponsored", "sponsor_h3": "உங்கள் tool இங்கே",
 "sponsor_p": "இந்த featured slot, இந்த use case-க்கு உண்மையிலேயே பொருந்தும் tools-ஐ உருவாக்குபவர்களுக்கானது. எப்போதும் தெளிவாக label செய்யப்பட்டிருக்கும், எங்கள் தேர்வுகளிலிருந்து தனியாக இருக்கும்.",
 "sponsor_link": "Sponsor செய்ய email அனுப்புங்கள்",
 "new_badge": "கவனிக்க வேண்டியவை / Trending",
 "last_updated": 'கடைசியாக update செய்தது: {date}', "earlier_h2": 'முந்தையவை', "earlier_p": 'இந்த update-க்கு முன் நாங்கள் காட்டிய launches. இப்போது இவை புதியவை அல்ல, ஆனால் தெரிந்துகொள்ள வேண்டியவை.', "fits": 'Use case:', "source": 'ஆதாரம்',
 "rss_title": "Tool Use Cases (தமிழ்)",
 "rss_desc": "Tool Picks Weekly issues (ஆங்கிலத்தில்) மற்றும் கவனிக்க வேண்டிய புதிய AI tool launches.",
 "rss_new_prefix": "புதியது, trending: ", "rss_issue_suffix": " (ஆங்கிலத்தில்)",
 "rss_cat_newsletter": "Newsletter", "rss_cat_new": "புதிய launches",
 "llms_h2": "தமிழில் (ta)",
 "llms_intro": "முழு site-உம் தமிழில், ஆங்கில version-இல் உள்ள அதே use cases, அதே தேர்வுகள், அதே rankings-உடன்.",
 "llms_other": [("முகப்பு", ""), ("எல்லா AI tools A முதல் Z வரை", "tools/"), ("புதிய launches, trending", "new/"), ("எங்களைப் பற்றி", "about/"), ("Sponsor", "sponsor/")],
}

TOOLS = {
 "cursor": "AI-first code editor (VS Code fork), chat, inline edits, agent mode உடன்.",
 "claude": "Anthropic-இன் AI assistant, நீளமான documents, எழுதுவது, code ஆகியவற்றில் வலுவானது.",
 "claude-code": "Anthropic-இன் terminal-இல் இயங்கும் agentic coding tool.",
 "chatgpt": "OpenAI-இன் எல்லா வேலைக்குமான AI assistant, chat, images, voice, search உடன்.",
 "codex": "OpenAI-இன் coding agent, cloud-இல் அல்லது CLI மூலம் உங்கள் repos-இல் வேலை செய்யும்.",
 "copilot": "VS Code, JetBrains, GitHub-இல் built-in ஆக இருக்கும் AI pair programmer.",
 "v0": "Vercel-இன் AI app/UI builder, prompts-இலிருந்து React + Tailwind apps-ஐ உருவாக்கும்.",
 "lovable": "Prompt-இலிருந்து full-stack web app உருவாக்கும் builder, Supabase integration உடன்.",
 "replit": "Browser-இல் IDE, அதன் agent ஒரு prompt-இலிருந்து app உருவாக்கி deploy-உம் செய்யும்.",
 "bolt": "StackBlitz-இன் browser-இலேயே இயங்கும் prompt-to-app builder.",
 "windsurf": "'Cascade' என்ற agentic assistant உள்ள AI code editor.",
 "aider": "Terminal-இல் open-source AI pair programming, git-ஐப் புரிந்துகொள்ளும்.",
 "devin": "Cognition-இன் autonomous software engineering agent.",
 "gemini": "Google-இன் AI assistant, மிகப் பெரிய context windows, Google integration உடன்.",
 "perplexity": "Web-இல் தேடி sources-ஐயும் காட்டும் AI answer engine.",
 "notebooklm": "Google-இன் research notebook, நீங்கள் upload செய்த sources-ஐ வைத்தே பதில் சொல்லும்.",
 "elicit": "Academic papers-ஐத் தேடவும் சுருக்கவும் உதவும் AI research assistant.",
 "notion-ai": "Notion workspaces-க்குள்ளேயே built-in AI writing, Q&A.",
 "grammarly": "நீங்கள் எங்கே type செய்தாலும் grammar, tone, rewrites-இல் உதவும் writing assistant.",
 "midjourney": "வலுவான aesthetic, artistic output-க்குப் பெயர்பெற்ற image generator.",
 "dalle": "ChatGPT-க்குள் OpenAI-இன் image generation, instructions-ஐப் பின்பற்றுவதிலும் படத்தில் text வைப்பதிலும் சிறந்தது.",
 "ideogram": "படங்களில் தெளிவாகப் படிக்கக்கூடிய text வைப்பதில் குறிப்பாகச் சிறந்த image generator.",
 "flux": "High-quality image models-இன் குடும்பம், சிலவற்றுக்கு open weights உண்டு.",
 "firefly": "Adobe-இன் generative image tools, commercial பயன்பாட்டுக்குப் பாதுகாப்பாக இருக்கும்படி train செய்யப்பட்டவை.",
 "sd": "நீங்களே local-ஆக run செய்யக்கூடிய open image models குடும்பம் (உதா. ComfyUI மூலம்).",
 "runway": "AI video generation, editing suite (Gen-series models).",
 "elevenlabs": "நிஜம் போலவே இருக்கும் AI voiceover, voice cloning, dubbing.",
 "descript": "Transcript-ஐ edit செய்தே videos, podcasts-ஐ edit செய்யுங்கள்.",
 "heygen": "AI avatar videos, video translation.",
 "capcut": "Free tier உள்ள video editor, auto-captions, AI effects உடன்.",
 "opus": "நீளமான videos-ஐத் தானாகவே சின்ன vertical clips-ஆக மாற்றும்.",
 "veo": "Google DeepMind-இன் text-to-video model, native audio உடன்.",
 "sora": "OpenAI-இன் text-to-video model மற்றும் app.",
 "rosebud": "Prompts-இலிருந்து games உருவாக்கும் browser tool (Three.js/Phaser).",
 "scenario": "உங்கள் சொந்த training sets-இலிருந்து ஒரே style-இல் game art assets உருவாக்கும்.",
 "meshy": "Game assets-க்கு text/image-இலிருந்து 3D model generation.",
 "suno": "முழுப் பாடல்களை உருவாக்கும், game/video-க்கு placeholder music-ஆகப் பயன்படும்.",
 "sentry": "Error monitoring, AI root-cause analysis, fix பரிந்துரைகளுடன்.",
 "deepseek": "சீனாவின் AI lab, இதன் open-weight reasoning models வலுவானவை, மலிவானவை.",
 "ollama": "Open models-ஐ (Llama, Qwen போன்றவை) ஒரே command-இல் local-ஆக run செய்யுங்கள்.",
 "manus": "Web-ஐ browse செய்து பல படிகள் கொண்ட வேலைகளை முடிக்கும் general-purpose autonomous agent.",
 "kling": "Kuaishou-இன் text/image-to-video generator.",
 "grok": "xAI-இன் assistant, X மற்றும் web-இல் real-time search உடன்.",
 "mcp": "AI agents-ஐ tools, data-உடன் இணைப்பதற்கான open standard.",
 "n8n": "Open-source workflow automation, AI agent nodes உடன்; இலவசமாக self-host செய்யலாம் அல்லது அவர்களின் cloud-ஐப் பயன்படுத்தலாம்.",
 "make": "ஆயிரக்கணக்கான apps முழுவதும் பல படி scenarios-க்கான visual no-code automation builder.",
 "zapier": "அதிக apps-உடன் இணையும் no-code automation platform, இப்போது AI steps, agents உடன்.",
 "framer": "Designers-க்கான website builder, AI page generation, CMS, hosting உடன்.",
 "stitch": "Google-இன் prompt-to-UI design tool (முன்பு Galileo AI), Figma-க்கும் code-க்கும் export செய்யும்.",
 "uizard": "புதியவர்களுக்கு எளிதான AI UI mockup tool; prompts, sketches-ஐ app screens-ஆக மாற்றும்.",
 "figma": "UI design-க்கான standard tool, built-in AI features, prompt-to-prototype-க்கு Figma Make உடன்.",
 "openai-tts": "OpenAI-இன் speech API: மலிவான, இயல்பான குரல்கள், instructions மூலம் கட்டுப்படுத்தலாம்.",
 "udio": "High-fidelity vocals, நுணுக்கமான remixing-க்குப் பெயர்பெற்ற AI song generator.",
 "aiva": "Instrumental, orchestral, soundtrack இசைக்கான AI composer, MIDI export உடன்.",
 "surfer": "உங்கள் draft-ஐ top-ranking pages-உடன் ஒப்பிட்டு score தரும் SEO content editor.",
 "clearscope": "Keyword coverage, content grading-க்கான premium content-optimization tool.",
 "lavender": "உங்கள் inbox-க்குள்ளேயே cold emails-க்கு score தந்து, திருத்தி எழுதும் sales email coach.",
 "julius": "Spreadsheets, data files-உடன் chat செய்து analysis, charts பெறுங்கள்.",
 "excel-copilot": "Excel-க்குள் Copilot, உங்கள் workbooks-இல் formulas, analysis, charts-க்கு.",
 "powerpoint-copilot": "PowerPoint-க்குள் Copilot: prompt அல்லது file-இலிருந்து deck draft செய்யும், slides சேர்க்கும், content-ஐ மாற்றி எழுதும் அல்லது மறுசீரமைக்கும்.",
 "gamma": "Prompt அல்லது outline-இலிருந்து presentations, docs, web pages உருவாக்கும்.",
 "beautiful-ai": "Smart templates உள்ள slide software, content சேர்க்கும்போதே தானாக format ஆகும்.",
 "luma": "Luma-வின் AI lab; Genie மூலம் text-to-3D, Dream Machine மூலம் video generation.",
 "tripo": "வேகமான text/image-to-3D generator, auto-rigging, clean topology options உடன்.",
 "fireflies": "Zoom/Meet/Teams calls-ஐ record, transcribe, summarize செய்யும் AI meeting bot.",
 "otter": "Real-time meeting transcription, AI summaries, பயனுள்ள free tier உடன்.",
 "grain": "Clips, highlights-ஐ மையமாகக் கொண்ட meeting recorder, sales, customer teams-இல் பிரபலம்.",
 "langchain": "LLM apps உருவாக்க open-source framework: RAG, tools, integrations.",
 "llamaindex": "LLMs-ஐ உங்கள் documents, data-உடன் இணைப்பதில் (RAG) கவனம் செலுத்தும் open-source framework.",
 "vercel": "Frontend, Next.js hosting, git-push deploys, previews, AI SDK உடன்.",
 "netlify": "Static sites, web apps-க்கு git-based hosting, functions, forms உடன்.",
 "railway": "கிட்டத்தட்ட config இல்லாமலே repo-இலிருந்து backends, databases, workers-ஐ deploy செய்யுங்கள்.",
 "fly": "Docker containers-ஐ உலகம் முழுவதும் users-க்கு அருகில் run செய்யுங்கள்; full-stack apps, GPUs-க்கு நல்லது.",
 "plasmo": "React, TypeScript மூலம் browser extensions உருவாக்க open-source framework.",
 "canva": "Online design tool, Magic Studio AI features, ready-made templates உடன்.",
 "langgraph": "Stateful, கட்டுப்பாட்டில் வைக்கக்கூடிய multi-step agent graphs-க்கான LangChain framework.",
 "crewai": "Role-based AI agents teams-க்கான open-source Python framework.",
 "autogen": "Multi-agent conversations, workflows-க்கான Microsoft-இன் open-source framework.",
 "openai-agents": "OpenAI-இன் lightweight SDK, agents-க்கு tools, handoffs, guardrails, tracing உடன்.",
 "recraft": "Designers-க்கான AI image generator, editable vector (SVG) graphics, icons தரும்.",
 "looka": "One-time fee-க்கு logo-வுடன் brand kit-ஐயும் உருவாக்கும் AI logo maker.",
 "intercom-fin": "Intercom-இன் AI support agent, உங்கள் help content-இலிருந்து வாடிக்கையாளர் கேள்விகளுக்குத் தீர்வு தரும்.",
 "zendesk": "Zendesk help desk-இல் built-in AI agents, agent-assist features.",
 "helpscout": "எளிய shared inbox, help desk, AI drafts, summaries, AI Answers உடன்.",
 "firecrawl": "Websites-ஐ crawl செய்து LLMs-க்கு clean markdown அல்லது structured data தரும் API.",
 "browserbase": "AI agents-க்கான hosted headless browsers, கூடவே open-source Stagehand framework.",
 "apify": "ஆயிரக்கணக்கான ready-made scrapers ('Actors'), scheduling உள்ள scraping platform.",
 "postman": "Requests உருவாக்கவும் test செய்யவும் API platform, Postbot AI assistant உடன்.",
 "bruno": "Open-source, offline API client, collections-ஐ git-இல் சாதாரண files-ஆக வைத்திருக்கும்.",
 "coda": "Doc-உம் spreadsheet-உம் கலந்த workspace, built-in Coda AI உடன்.",
 "mem": "Notes-ஐத் தானாக ஒழுங்குபடுத்தி, அவற்றுடன் chat செய்ய விடும் AI notes app.",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Vibe coding-க்கு சிறந்த AI", "சொல்லுங்கள், run செய்யுங்கள், tweak செய்யுங்கள். பெரும்பாலும் பேசிக்கொண்டே software உருவாக்க உதவும் tools.", [
  "Default தேர்வு: உண்மையான codebase-உம் editor-உம் உங்களிடமே இருக்கும், ஆனால் பெரும்பாலான typing-ஐ AI செய்யும்.",
  "Idea-விலிருந்து auth, database உள்ள வேலை செய்யும் web app வரை செல்ல மிக வேகமான வழி, எந்த setup-உம் இல்லாமல்.",
  "சீக்கிரமாக polished React/Next.js UI வேண்டும், Vercel-இல் deploy செய்யத் திட்டம் இருந்தால் இதுவே சிறந்தது.",
  "Hosting உட்பட எல்லாமே browser-இல் — சீக்கிரம் உருவாக்கி share செய்யக்கூடிய prototypes-க்கு நல்லது.",
  "Lovable மாதிரியே; ஒரே tab-இல் full-stack demo ஒன்றை உருவாக்க அருமை.",
  "வலுவான agent உள்ள Cursor மாற்று; Cursor உங்களுக்குச் சரிப்படவில்லை என்றால் ஒருமுறை try செய்து பாருங்கள்."]),
 "best-ai-coding-agents": ("சிறந்த AI coding agents", "Task-ஐ எடுத்து, பல files-ஐ edit செய்து, commands run செய்து, ஒரு diff-உடன் திரும்பும் agents.", [
  "Terminal-இலிருந்து multi-file மாற்றங்களில் அசத்தல்; பெரிய agentic வேலைகளுக்குப் பலரின் favourite.",
  "முழு editor-க்குள்ளேயே agent mode, அதனால் ஒவ்வொரு மாற்றத்தையும் கண்ணால் பார்த்து review செய்யலாம்.",
  "Tasks-ஐ cloud-இல் parallel-ஆக ஓட ஒப்படைத்துவிட்டு, வரும் PRs-ஐ review செய்யுங்கள்.",
  "Copilot-இன் coding agent GitHub issues-இலிருந்து வேலை செய்யும் — உங்கள் team GitHub-இலேயே இருந்தால் இயல்பாகப் பொருந்தும்.",
  "முழு tickets-ஐ ஆரம்பம் முதல் முடிவு வரை ஒப்படைக்க உருவாக்கப்பட்டது; விலை அதிகம், teams-க்கானது.",
  "இலவசம், open-source, உங்களுக்கு விருப்பமான model-ஐப் பயன்படுத்தலாம்; ஒவ்வொரு மாற்றத்துக்கும் clean git commit செய்யும்."]),
 "best-ai-for-fixing-broken-code": ("உடைந்த code, errors-ஐ சரிசெய்ய சிறந்த AI", "Stack trace-ஐ paste செய்யுங்கள், fix கிடைக்கும். Code உருவாக்குவதில் மட்டுமல்ல, debugging-இலும் சிறந்த tools.", [
  "Error-உடன் தொடர்புடைய files-ஐயும் paste செய்யுங்கள்; உண்மையான root cause-ஐ யோசித்துக் கண்டுபிடிப்பதில் வலுவானது.",
  "முழு project context-உடன் அங்கேயே fix செய்யும் — அங்கும் இங்கும் copy-paste தேவையில்லை.",
  "நல்ல general debugger, issues-ஐ reproduce செய்ய Python-உம் run செய்யும்.",
  "'Fix', '/explain' நேரடியாக editor-இலேயே, சிவப்புக் கோடு இருக்கும் இடத்திலேயே.",
  "Production-இல் errors-ஐப் பிடித்து, உண்மையான traces-ஐ வைத்து fixes பரிந்துரைக்கும்.",
  "அதையே tests run செய்ய விடுங்கள், failure-ஐப் படிக்க விடுங்கள், எல்லாம் green ஆகும் வரை திரும்பத் திரும்ப முயற்சிக்க விடுங்கள்."]),
 "best-ai-for-game-prototyping": ("Game prototyping-க்கு சிறந்த AI", "விளையாடக்கூடிய ஒரு idea-வை சீக்கிரமாக screen-க்குக் கொண்டு வாருங்கள் — code, art, 3D, music.", [
  "ஒரு prompt-இலிருந்து browser game உருவாக்குங்கள், மற்றவர்களின் games-ஐ remix செய்யுங்கள்.",
  "உண்மையான engines-க்கு (Godot, Unity, Phaser): scripts-ஐ AI எழுதும், play-test நீங்கள் செய்வீர்கள்.",
  "Game art-ஐ உங்கள் சொந்த style-இல் ஒரே மாதிரி வைத்திருக்கும் — games-இல் AI art-இன் கடினமான பகுதி இதுதான்.",
  "Levels-ஐ blockout செய்ய சீக்கிரமாக 3D props, characters.",
  "சில நிமிடங்களில் placeholder (அல்லது final) soundtrack.",
  "Recording booth இல்லாமலே character voice lines, sound effects."]),
 "best-ai-for-video-youtube": ("Video, YouTube-க்கு சிறந்த AI", "Footage உருவாக்குங்கள், வேகமாக edit செய்யுங்கள், voice சேருங்கள், Shorts-ஆக cut செய்யுங்கள்.", [
  "Talking-head videos-ஐ ஒரு doc மாதிரி edit செய்யுங்கள்; filler words-ஐ நீக்கிவிடும். YouTubers-க்கு நிறைய நேரம் மிச்சம்.",
  "B-roll, effects-க்கு pro-level AI video generation, editing tools.",
  "சத்தத்துடன் high-quality generated clips; cinematic b-roll-க்கு வலுவானது.",
  "Voiceover, மற்ற மொழிகளில் dubbing-இல் தன் category-யிலேயே சிறந்தது.",
  "நீளமான video அல்லது stream-ஐத் தானாகவே Shorts/TikToks-ஆக மாற்றும்.",
  "கிட்டத்தட்ட இலவச editor, நல்ல auto-captions உடன் — தினசரி வேலைக்கான practical tool.",
  "Camera முன் வர விருப்பமில்லாதபோது avatar presenters, lip-synced translation."]),
 "best-ai-writing-assistants": ("சிறந்த AI writing assistants", "Drafting, editing, rewriting — docs, blog posts, READMEs, emails.", [
  "பெரிய assistants-இல் மிக இயல்பாக ஒலிக்கும் எழுத்து; சிறந்த editor-உம் கூட.",
  "எல்லா வேலைக்கும் ஏற்ற all-rounder; நீளமான drafts-க்கு Canvas mode உதவும்.",
  "உங்கள் notes, docs ஏற்கனவே Notion-இல் இருந்தால் இதுவே சிறந்தது.",
  "நீங்கள் எங்கே type செய்தாலும் அங்கேயே polish — browser, email, docs.",
  "Google Docs, Gmail-க்குள் ரொம்ப வசதியானது."]),
 "best-ai-for-research": ("Research-க்கு சிறந்த AI", "Sources-ஐத் தேடுங்கள், படியுங்கள், summarize செய்யுங்கள் — சரிபார்க்கக்கூடிய citations உடன்.", [
  "Live web-இலிருந்து வேகமான, sources உள்ள பதில்கள்; சீக்கிர research-க்கு முதல் தேர்வு.",
  "உங்கள் சொந்த sources-ஐ upload செய்து, அவற்றின் அடிப்படையிலேயே பதில்கள் (audio overviews-உம்) பெறுங்கள்.",
  "Deep research mode ஒரு topic பற்றி நீளமான, citations உள்ள reports உருவாக்கும்.",
  "Deep Research, கூடவே Google Search integration.",
  "Academic papers, literature reviews-க்காகவே உருவாக்கப்பட்டது.",
  "இப்போது X-இல் மக்கள் என்ன பேசுகிறார்கள் என்று தெரிந்துகொள்ள பயனுள்ளது."]),
 "best-ai-image-generation": ("Image generation-க்கு சிறந்த AI", "Thumbnails, concept art, mockups, memes.", [
  "Default look மிகச் சிறப்பு; art, moodboards, concept art-க்கு அருமை.",
  "விரிவான instructions-ஐப் பின்பற்றுவதிலும், பேசிக்கொண்டே edit செய்வதிலும் சிறந்தது.",
  "படத்தில் படிக்கக்கூடிய text தேவைப்படும்போது இதைத் தேர்ந்தெடுங்கள் — logos, posters, thumbnails.",
  "Top-tier quality, local பயன்பாட்டுக்கு open-weight options-உம் உண்டு.",
  "Commercial வேலைக்குப் பாதுகாப்பானது; Photoshop-இல் built-in.",
  "உங்களிடம் GPU இருந்து, tinkering பிடிக்குமென்றால் இலவசமாக, local-ஆக (ComfyUI)."]),
 "best-ai-for-running-local-models": ("AI-ஐ local-ஆக run செய்ய சிறந்த tools", "உங்கள் சொந்த machine-இல் private AI, run செய்யச் செலவில்லை.", [
  "ஒரே command-இல் open models-ஐ download செய்து run செய்யுங்கள்; தொடங்க மிக எளிதான வழி.",
  "வலுவான open-weight models, local-ஆக run செய்யலாம் அல்லது API மூலம் மலிவாகப் பயன்படுத்தலாம்.",
  "ஏதாவது local model-உடன் இணைத்தால் offline coding assistant ரெடி.",
  "Local image models-இன் classic ecosystem."]),
 "best-ai-for-automation-workflows": ("Automation workflows-க்கு சிறந்த AI", "உங்கள் apps-ஐ இணைத்து, திரும்பத் திரும்ப வரும் steps-ஐ AI கவனிக்கட்டும் — triggers, agents, glue code.", [
  "Builders-க்கு top pick: AI agent nodes, தேவைப்பட்டால் code, self-host முற்றிலும் இலவசம்.",
  "சிக்கலான branching flows-க்கு சிறந்த visual canvas; ஒவ்வொரு task-க்கும் Zapier-ஐ விட மலிவு.",
  "அதிக apps coverage, மிக எளிதான setup; அதிக volume இருந்தால் தவிர்த்துவிடுங்கள், ஏனென்றால் செலவு வேகமாக ஏறும்.",
  "No-code-ஆல் முடியாதபோது, அதை வைத்து script அல்லது webhook handler எழுதிக்கொள்ளுங்கள்.",
  "ஒருமுறை செய்யும் multi-step web வேலைகளுக்கு; நம்பகமான scheduled workflows-க்கு மாற்று அல்ல."]),
 "best-ai-for-landing-pages": ("Landing pages-க்கு சிறந்த AI", "ஒரு மதியத்துக்குள் idea-விலிருந்து live-ஆன, நன்றாகத் தோன்றும் landing page வரை.", [
  "Top pick: prompt மூலம் forms, database உள்ள முழு page-ஐ உருவாக்கி, ஒரே click-இல் publish செய்யுங்கள்.",
  "Custom logic-ஐ விட design polish-உம் எளிதான hosting-உம் முக்கியம் என்றால் சிறந்தது; பிறகு marketers-உம் edit செய்யலாம்.",
  "Vercel-இல் deploy செய்தால் அருமையான React/Tailwind output; கொஞ்சம் coding பழக்கம் தேவை.",
  "Lovable-க்கு வேகமான full-stack மாற்று; ஒரு idea-வை சீக்கிரம் test செய்ய நல்லது.",
  "ஏற்கனவே codebase இருந்தால் builders வேண்டாம் — அங்கேயே page-ஐச் சேருங்கள்."]),
 "best-ai-for-ui-design": ("UI design-க்கு சிறந்த AI", "ஒரு prompt அல்லது sketch-ஐ screens-ஆக, பிறகு நீங்கள் build செய்யக்கூடியதாக மாற்றுங்கள்.", [
  "Designers-உடன் வேலை செய்தால் top pick: standard tool, இப்போது AI, Figma Make built-in உடன்.",
  "Mockup step-ஐயே தவிர்க்கும்: உடனே ship செய்யக்கூடிய வேலை செய்யும் UI code உருவாக்கும்.",
  "Google-இன் இலவச, வேகமான prompt-to-UI exploration (முன்பு Galileo AI); Figma-க்கு export செய்யும்.",
  "Wireframes செய்யும் non-designers-க்கு மிக எளிது; pixel-level control வேண்டுமென்றால் தவிர்த்துவிடுங்கள்.",
  "'Design' உண்மையில் click செய்யக்கூடிய, வேலை செய்யும் app-ஆக இருக்க வேண்டும் என்றால்."]),
 "best-ai-voice-tts": ("சிறந்த AI voice, text-to-speech", "Mic இல்லாமலே voiceovers, narration, cloned voices, app speech.", [
  "Top pick: மிக இயல்பான குரல்கள், cloning, dubbing. Creators-க்கு default.",
  "API மூலம் apps, bulk narration-க்கு மிக மலிவான நல்ல குரல்கள்; voice options குறைவு.",
  "Recording-ஐயும் edit செய்கிறீர்கள் என்றால் சிறந்தது — தவறாகச் சொன்ன வார்த்தைகளை உங்கள் சொந்த cloned voice-ஆலேயே சரிசெய்யுங்கள்.",
  "பேசும் avatar அல்லது lip-synced translation-உம் தேவைப்படும்போது."]),
 "best-ai-for-music": ("Music-க்கு சிறந்த AI", "Prompt-இலிருந்து பாடல்கள், soundtracks, background music.", [
  "Top pick: vocals உடன் முழுப் பாடல்கள் சில நொடிகளில்; நல்லதாக ஏதாவது பெற மிக எளிதான வழி.",
  "வலுவான vocals, remix-இல் இன்னும் நுணுக்கமான control; Suno output generic-ஆகத் தோன்றினால் try செய்யுங்கள்.",
  "Instrumental, orchestral scores-க்கு சிறந்தது, DAW-இல் edit செய்யக்கூடிய MIDI export உடன்.",
  "Voice-உடன் music, sound-effect generation-உம் உண்டு, ஏற்கனவே பயன்படுத்தினால் வசதி."]),
 "best-ai-for-seo-content": ("SEO content-க்கு சிறந்த AI", "Rank ஆகக்கூடிய pages-க்கான research, outline, எழுத்து — AI குப்பையை publish செய்யாமல்.", [
  "உண்மையான எழுத்துக்கு top pick: மிக இயல்பான drafts, உங்கள் சொந்த material-க்குச் சிறந்த editor.",
  "Rank ஆகும் pages-உடன் ஒப்பிட்டு உங்கள் draft-க்கு score தரும்; பயனுள்ள guardrails, ஆனால் score-க்காக மட்டும் எழுதாதீர்கள்.",
  "Teams, agencies-க்கான premium content grading; ஒருவர் நடத்தும் site-க்குத் தேவைக்கு அதிகம்.",
  "ஒரு topic பற்றியும், competitors என்ன cover செய்கிறார்கள் என்பது பற்றியும் வேகமான, sources உள்ள research.",
  "Briefs, outlines, meta descriptions-க்கு உறுதியான all-rounder; topic gaps-க்கு deep research."]),
 "best-ai-for-sales-emails": ("Sales emails-க்கு சிறந்த AI", "சிறந்த cold, follow-up emails எழுதுங்கள் — personal-ஆக, சுருக்கமாக, AI எழுதியது போல் வெளிப்படையாகத் தெரியாமல்.", [
  "Top pick: prospect-இன் context-ஐக் கொடுங்கள், சுருக்கமான, மனிதர் எழுதியது போன்ற draft கிடைக்கும். எப்போதும் edit செய்யுங்கள்.",
  "Drafts, variants-க்கு அதே அளவு நல்லது; உங்கள் tone-ஐ set செய்ய custom instructions-ஐப் பயன்படுத்துங்கள்.",
  "நேரடியாக Gmail/Outlook-இல் coaching, scoring; தினமும் cold email அனுப்பினால் பயனுள்ளது.",
  "முதல் வரியை எழுதும் முன் prospect, company பற்றி வேகமான research.",
  "நீங்கள் எங்கே type செய்தாலும் tone, clarity-க்கு final polish."]),
 "best-ai-for-data-spreadsheets": ("Data, spreadsheets-க்கு சிறந்த AI", "CSVs-ஐ analyze செய்யுங்கள், formulas எழுதுங்கள், charts உருவாக்குங்கள் — சாதாரண மொழியில் கேட்டாலே போதும்.", [
  "Top pick: file-ஐ upload செய்யுங்கள், analysis, charts-க்கு இது உண்மையான Python-ஐ run செய்யும்.",
  "Data-வை விளக்குவதிலும் formulas எழுதுவதிலும் அருமை; upload செய்த files-இல் analysis-உம் run செய்யும்.",
  "Data analysis-க்காக மட்டுமே உருவாக்கப்பட்டது, non-coders-க்கு இன்னும் எளிதான workflow உடன்.",
  "வேலை ஏற்கனவே Excel-இல் இருந்தால் சிறந்தது; Microsoft 365 Copilot plan தேவை.",
  "Google Sheets-க்குள் இயல்பான தேர்வு."]),
 "best-ai-for-presentations": ("Presentations-க்கு சிறந்த AI", "Outline-இலிருந்து நல்ல slide deck வரை, சீக்கிரமாக.", [
  "Top pick: prompt கொடுங்கள் அல்லது notes-ஐ paste செய்யுங்கள், ஒரு நிமிடத்தில் அழகான deck கிடைக்கும்; PowerPoint-க்கு export ஆகும்.",
  "ஒரே மாதிரியான, on-brand slides, format கலையாமல் வேண்டும் என்று நினைக்கும் teams-க்குச் சிறந்தது.",
  "முதலில் story, outline-ஐ எழுத வையுங்கள், அல்லது slide content, code-based decks-ஐ உருவாக்க வையுங்கள்.",
  "Outlines, speaker notes-க்கு நல்லது, download செய்யக்கூடிய .pptx file-உம் உருவாக்கும்.",
  "உங்கள் decks ஏற்கனவே PowerPoint-இல் இருந்து, உங்கள் Microsoft 365 plan-இல் Copilot இருந்தால் பொருத்தமானது."]),
 "best-ai-for-3d-assets": ("3D assets-க்கு சிறந்த AI", "Text அல்லது images-இலிருந்து props, characters, models உருவாக்குங்கள்.", [
  "Top pick: textures உடன் உறுதியான text/image-to-3D, game engines-க்கான exports.",
  "Auto-rigging உடன் வேகமான generation; animate செய்ய வேண்டிய characters-க்கு அருமை.",
  "சீக்கிர text-to-3D experiments; final production assets-ஐ விட concepting-க்கே சிறந்தது.",
  "முழு project-இலும் ஒரே style உள்ள game assets-க்குச் சிறந்தது.",
  "2.5D/sprite games-க்கு 3D-யை முழுதாகத் தவிர்த்துவிடுங்கள் — concept art, textures-ஐ local-ஆக உருவாக்குங்கள்."]),
 "best-ai-for-meeting-notes": ("Meeting notes-க்கு சிறந்த AI", "Calls-ஐ record, transcribe, summarize செய்யுங்கள், அப்போது யாரும் notes எடுக்க வேண்டியதில்லை.", [
  "Top pick: உங்கள் calls-இல் தானாகவே join ஆகும், நல்ல summaries, search, CRM integrations உடன்.",
  "சிறந்த free tier, live transcription; summaries கொஞ்சம் generic-ஆக இருக்கும்.",
  "வெறும் notes அல்ல, clips-ஐ share செய்ய விரும்பும் sales, customer calls-க்குச் சிறந்தது.",
  "உங்கள் team ஏற்கனவே Notion-இல் இருந்தால் built-in meeting notes — தனியாக bot தேவையில்லை.",
  "Bot-ஏ இல்லை: transcript-ஐ paste செய்து, கூர்மையான summaries, action items பெறுங்கள். Automatic recording வேண்டுமென்றால் தவிர்த்துவிடுங்கள்."]),
 "best-ai-for-chatbots-rag": ("Chatbots, RAG-க்கு சிறந்த AI", "உங்கள் சொந்த docs-இலிருந்து பதில் சொல்லும் assistant-ஐ உருவாக்குங்கள் — no-code முதல் custom code வரை.", [
  "தொடங்க top pick: upload செய்த files உடன் ஒரு Custom GPT சில நிமிடங்களில் ரெடி. உங்கள் சொந்த site-இல் வைக்க வேண்டுமென்றால் தவிர்த்துவிடுங்கள்.",
  "உங்கள் docs-ஐ அடிப்படையாகக் கொண்ட internal team assistant-க்கு Claude Projects அருமை.",
  "உங்கள் data-வை சரியாக ingest, retrieve செய்வதுதான் கடினமான பகுதி என்றால் சிறந்த code framework.",
  "Integrations-இன் மிகப் பெரிய ecosystem; எளிய bots-க்குத் தேவைக்கு அதிகமான abstraction.",
  "அதை வைத்து ஒரு lean custom RAG app எழுதுங்கள், உங்கள் tools-உடன் இணைக்க MCP-ஐப் பயன்படுத்துங்கள்.",
  "உங்கள் sources மீது zero-setup Q&A, embed செய்ய அல்ல, சொந்தப் பயன்பாட்டுக்கு."]),
 "best-ai-for-deploy-hosting": ("AI-ஆல் உருவான apps-க்கு சிறந்த hosting", "உங்கள் AI tools இப்போதுதான் உருவாக்கிய app-ஐ எங்கே ship செய்வது. இவை AI tools அல்ல, hosting platforms — AI உதவியுடன் build செய்பவர்களுக்கு எவ்வளவு பொருந்துகின்றன என்று பார்த்துத் தேர்ந்தெடுத்தவை.", [
  "Next.js/React apps-க்கு (v0-இலிருந்து வரும் எதற்கும்) top pick: git-க்கு push செய்யுங்கள், previews உடன் live URL கிடைக்கும்.",
  "Static sites, எளிய apps-க்கு அருமை, தாராளமான free tier, built-in forms உடன்.",
  "Backends, databases, background workers-க்கு மிக எளிதான இடம். வெறும் static sites என்றால் தவிர்த்துவிடுங்கள்.",
  "Docker, பல regions, அல்லது GPUs தேவைப்படும்போது சிறந்தது; setup கொஞ்சம் அதிகம்.",
  "ஒரே இடத்தில் build, host செய்யுங்கள் — deploy config-ஐத் தொடவே வேண்டாம் என்றால் மிக எளிது."]),
 "best-ai-for-chrome-extensions": ("Chrome extensions உருவாக்க சிறந்த AI", "'இதுக்கு ஒரு button இருந்தா நல்லா இருக்கும்' என்பதிலிருந்து வேலை செய்யும் browser extension வரை.", [
  "Top pick: manifest, scripts, popup-ஐ உருவாக்கும், நீங்கள் reload செய்து test செய்யும்போது context-இலேயே errors-ஐச் சரிசெய்யும்.",
  "முழு extension-ஐயும் scaffold செய்வதிலும், Manifest V3 permission issues-இல் திரும்பத் திரும்ப வேலை செய்வதிலும் அருமை.",
  "சின்ன, ஒரே file extension-க்குப் போதும். Manifest V3 பயன்படுத்துகிறதா என்று சரிபாருங்கள், ஏனென்றால் பழைய examples எங்கும் இருக்கின்றன.",
  "இது AI tool அல்ல, ஆனால் AI tool-உடன் நன்றாக ஒத்துப்போகும்: extension boilerplate-ஐ நீக்கும் React/TS framework.",
  "நீங்களே எழுத விரும்பினால் Chrome APIs-க்கு நல்ல autocomplete."]),
 "best-ai-for-thumbnails-youtube-packaging": ("YouTube thumbnails, packaging-க்கு சிறந்த AI", "Thumbnails, titles, click வாங்கித் தரும் அந்த hook.", [
  "படத்திலேயே bold-ஆக, படிக்கக்கூடிய text உள்ள thumbnails-க்கு top pick.",
  "பேசிக்கொண்டே edit செய்ய (\"முகத்தை இன்னும் கொஞ்சம் ஆச்சரியமா காட்டு\"), அதே chat-இல் titles brainstorm செய்யச் சிறந்தது.",
  "Final thumbnail-இன் layout-ஐ உண்மையில் செய்யும் இடம்: templates, background removal, Magic tools.",
  "மிகக் கவர்ச்சியான backgrounds, scenes; text-ஐப் பிறகு Canva-வில் சேருங்கள்.",
  "Title, thumbnail-text ஜோடிகளை brainstorm செய்யுங்கள்; ஒரு idea clickbait மாதிரி இருந்தால் நேர்மையாகச் சொல்லிவிடும்."]),
 "best-ai-for-agent-frameworks": ("சிறந்த AI agent frameworks", "Tools, memory, multi-step workflows உடன் உங்கள் சொந்த agents-ஐ உருவாக்க code frameworks.", [
  "தொடங்க top pick: சின்ன API, tools, handoffs, tracing built-in.",
  "தெளிவான control தேவைப்படும்போது சிறந்தது: state, retries, human-in-the-loop, production நம்பகத்தன்மை.",
  "Role-based multi-agent 'crews'-ஐ prototype செய்ய மிக வேகமான வழி; பெரிய scale-இல் கட்டுப்பாட்டில் வைப்பது கடினம்.",
  "Microsoft-இன் multi-agent framework; research பாணி agent conversations-க்கு வலுவானது.",
  "Framework அல்ல, ஆனால் எந்த agent-க்கும் tools கொடுக்க standard வழி இதுதான். உங்கள் tools-ஐ MCP servers-ஆக build செய்யுங்கள்."]),
 "best-ai-for-logos-brand": ("Logos, branding-க்கு சிறந்த AI", "Logo ideas, brand marks, ஆரம்ப brand kit, சீக்கிரமாக.", [
  "Top pick: edit, scale செய்யக்கூடிய உண்மையான vector (SVG) logos, icons உருவாக்கும்.",
  "படிக்கக்கூடிய wordmarks உள்ள logo concepts-க்குச் சிறந்தது; தேர்ந்தெடுத்ததை இன்னும் vectorize செய்ய வேண்டியிருக்கும்.",
  "Non-designers-க்கு logo, brand kit இரண்டையும் தரும் மிக எளிதான all-in-one; results கொஞ்சம் template மாதிரி தோன்றலாம்.",
  "Final logo files-ஐ விட brand mood, visual direction-ஐ explore செய்ய அருமை.",
  "பேசிக்கொண்டே ஒரு concept-ஐ மேம்படுத்த வசதி. எதையும் trademark செய்வதற்கு முன் அது உண்மையிலேயே தனித்துவமானதா என்று சரிபாருங்கள்."]),
 "best-ai-for-customer-support": ("Customer support-க்கு சிறந்த AI", "AI agents, AI எழுதிய replies மூலம் வாடிக்கையாளர்களுக்கு வேகமாகப் பதில் சொல்லுங்கள்.", [
  "Tickets-ஐத் தானாகத் தீர்க்க top pick; Intercom help desk இல்லாமலும் வேலை செய்யும். ஒவ்வொரு resolution-க்கும் விலை, அதனால் volume கூடக் கூட செலவும் கூடும்.",
  "ஏற்கனவே Zendesk-இல் இருந்தால் இயல்பான தேர்வு; சின்ன teams-க்கு setup, pricing கனமானவை.",
  "பெரிய platform அல்ல, AI drafts, answers உள்ள எளிய inbox வேண்டும் என்று நினைக்கும் சின்ன teams-க்குச் சிறந்தது.",
  "எந்த platform-உம் தேவையில்லை: ticket-ஐயும் உங்கள் docs-ஐயும் paste செய்து, கவனமான, நட்பான reply draft பெறுங்கள்.",
  "அதே idea, ஒரு Custom GPT உங்கள் team-க்கு share செய்யக்கூடிய internal support assistant-ஐத் தரும்."]),
 "best-ai-for-scraping": ("Web scraping-க்கு சிறந்த AI", "Websites-ஐ apps, research, AI pipelines-க்கான clean data-வாக மாற்றுங்கள். ஒவ்வொரு site-இன் terms, robots.txt-ஐ மதியுங்கள்.", [
  "Builders-க்கு top pick: ஒரே API call-இல் ஒரு site-இலிருந்து clean markdown அல்லது structured JSON.",
  "Ready-made scraper ஏற்கனவே இருக்கும்போது சிறந்தது (maps, social, e-commerce); scheduling built-in.",
  "உண்மையான logged-in browser அல்லது clicks தேவைப்படும் sites-க்கு; Stagehand-உடன் சேர்த்துப் பயன்படுத்துங்கள்.",
  "உண்மையான page-ஐ வைத்து custom scraper எழுதி debug செய்யும்; ஒருமுறை அல்லது வித்தியாசமான sites-க்குச் சிறந்தது.",
  "அதே வேலை, உங்கள் editor-க்குள் — scraper ஏற்கனவே உள்ள project-இன் பகுதியாக இருந்தால் நல்லது."]),
 "best-ai-for-api-testing": ("API testing-க்கு சிறந்த AI", "Requests எழுதுங்கள், tests உருவாக்குங்கள், fail ஆகும் endpoints-ஐ debug செய்யுங்கள்.", [
  "உங்கள் team ஏற்கனவே Postman பயன்படுத்தினால் top pick: Postbot உங்கள் requests-இலிருந்து tests, docs எழுதும்.",
  "உங்கள் API code-க்குப் பக்கத்திலேயே test suites (pytest, Jest போன்றவை) உருவாக்கிச் சரிசெய்யும்.",
  "OpenAPI spec அல்லது fail ஆன response-ஐ paste செய்து, நீங்கள் தவறவிட்ட test cases, edge cases பெறுங்கள்.",
  "சீக்கிர test scripts, mock data-க்கு நல்லது; முயற்சித்துப் பார்க்க Python run செய்யும்.",
  "இது AI அல்ல, ஆனால் இதன் சாதாரண file collections-ஐ AI editors எளிதாகப் படிக்கவும் எழுதவும் முடியும். Offline-ஆக, git-native-ஆக இருக்க இதைத் தேர்ந்தெடுங்கள்."]),
 "best-ai-for-notion-docs": ("Notes, docs-க்கு சிறந்த AI", "AI மூலம் உங்கள் notes, team docs-ஐ எழுதுங்கள், ஒழுங்குபடுத்துங்கள், search செய்யுங்கள்.", [
  "உங்கள் workspace Notion-இல் இருந்தால் top pick: AI writing, எல்லா pages-இலும் Q&A, meeting notes, எல்லாம் ஒரே இடத்தில்.",
  "Docs-ஐ உண்மையில் எழுதவும் edit செய்யவும் சிறந்தது; Projects reference material-ஐக் கையருகே வைத்திருக்கும்.",
  "Docs-ஐ draft செய்யவும் மறுசீரமைக்கவும் versatile; நீளமான எழுத்துக்கு Canvas உதவும்.",
  "உங்கள் docs உண்மையில் tables, automations உள்ள சின்ன apps என்றால் இதைத் தேர்ந்தெடுங்கள்.",
  "தானாக ஒழுங்காகும் personal notes; team wikis-க்குத் தவிர்த்துவிடுங்கள்."]),
}

NEW = {
 "claude-code": "Anthropic-இன் terminal coding agent — அதிகம் பேசப்படும் dev tools-இல் ஒன்று.",
 "codex": "OpenAI மீண்டும் launch செய்த Codex coding agent (cloud + CLI).",
 "veo": "Google-இன் video model, இப்போது synced audio-வும் உருவாக்கும்.",
 "sora": "OpenAI-இன் video model, இப்போது அதற்கென்றே ஒரு social app உடன்.",
 "manus": "Multi-step tasks-ஆல் viral ஆன autonomous general agent.",
 "lovable": "வேகமாக வளரும் prompt-to-app builder.",
 "notebooklm": "Audio Overviews, research notes-ஐ podcasts-ஆக மாற்றியது.",
 "kling": "AI video generation-இல் வலுவான போட்டியாளர்.",
 "deepseek": "Pricing-ஐயே அசைத்துப் பார்த்த open-weight reasoning models.",
 "mcp": "இப்போது பெரும்பாலான agent tools, tools access-க்கு support செய்யும் open protocol.",
 "windsurf": "Cursor-உடன் நேரடியாகப் போட்டியிடும் agentic editor.",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['ஜனவரி', 'பிப்ரவரி', 'மார்ச்', 'ஏப்ரல்', 'மே', 'ஜூன்', 'ஜூலை', 'ஆகஸ்ட்', 'செப்டம்பர்', 'அக்டோபர்', 'நவம்பர்', 'டிசம்பர்']
DATE_MD = '{m} {d}'
DATE_MDY = '{m} {d}, {y}'
RELEASES = {
 'voxtral-3': 'Mistral-இன் புதிய speech-to-text, text-to-speech models, கூடவே phone, web-இல் real-time voice agents உருவாக்க ஒரு SDK. Mistral API (EU-hosted option உடன்) வழியாக அல்லது self-hosted.',
 'kling-4': 'Kuaishou-வின் புதிய video model: ஒரே pass-இல் 30 வினாடிகள் வரை clips, வேகமான அசைவுகள், camera moves-இல் அதிக நிலைத்தன்மை, ஒவ்வொரு வேலைக்கும் 15 வரை reference assets, 10 keyframes.',
 'muse-spark-open': 'Coding, agent வேலைகளுக்கான Meta-வின் open-weight model (816B parameters, 42B active, 1M-token context). Meta இதை இரண்டு Mac Studios-இல் இயக்குகிறது; பெரும்பாலானோருக்கு hosted APIs-தான் எளிய வழி.',
 'claude-haiku-5-5': 'Anthropic-இன் மிக மலிவான, மிக வேகமான model; support bots, summaries, coding subagents போன்ற அதிக அளவு வேலைகளுக்கானது. Haiku 4.5-ஐ விட இயக்க சுமார் 75% குறைவான செலவு என்கிறது Anthropic.',
 'nano-banana-2-1': 'Google-இன் update செய்யப்பட்ட image generation, editing model: சிறந்த edits, கதாபாத்திரங்களில் அதிக consistency, images-இல் தெளிவான text. Gemini app, AI Studio, Gemini API, Flow, Stitch-இல் கிடைக்கிறது.',
 'copilot-dynamic-workflows': 'Multi-agent வேலைகளை code-இல் வரையறுக்கலாம் (parallel steps, ஒன்றையொன்று சரிபார்க்கும் subagents, நீங்கள் review செய்ய checkpoints) — Copilot CLI, Copilot app, Copilot SDK-இல். Public preview, எல்லா plans-இலும்.',
 'heygen-video': 'HeyGen-இன் முதல் general-purpose video model: text, image அல்லது reference media-விலிருந்து 5 முதல் 15 வினாடி clips; வசனமும் ஒலியும் சேர்ந்தே உருவாகின்றன. HeyGen API வழியாகக் கிடைக்கிறது.',
 'gpt-6-1-sol': 'OpenAI DevDay-இல் வந்த GPT-6 Sol upgrade; agentic coding, computer use, professional வேலைகளில் கவனம். மிகக் குறைந்த விலையில் GPT-6 Astra-வுக்கு நெருக்கமாக வருகிறது என்கிறது OpenAI.',
 'openai-agents-api-computer-use': 'Agents API இப்போது computer use மூலம் software-ஐ இயக்க முடியும்; Codex-இன் multi-agent features, tool search, context compaction-ஐ உங்கள் app-க்குக் கொண்டு வருகிறது. Infrastructure-ஐ OpenAI இயக்குகிறது.',
 'claude-sonnet-5-5': 'Anthropic-இன் வேகமான, மலிவான Sonnet; தெளிவான எல்லை கொண்ட அன்றாட வேலைகள், bug fixing-இல் வலிமையானது. Sonnet 5-ஐ விட 30%+ வேகம், அதே $2/$10 per million tokens விலையில்.',
 'lovable-free-chat': 'Lovable உடன் chat இப்போது தினசரி free அளவுக்குள் இலவசம்: features-ஐ plan செய்யலாம், app-இன் code, database பற்றிக் கேட்கலாம், launch text-ஐ draft செய்யலாம். Build செய்ய இன்னும் credits தேவை.',
 'cursor-projects': 'ஒரு feature அல்லது migration போன்ற பெரிய வேலைகளுக்கான beta: ஒரு coordinator agent cloud-இல் இயங்கி, வேலையை plan செய்து, பல subagents-க்குப் பிரித்துக் கொடுத்து, காலப்போக்கில் shared context-ஐப் பராமரிக்கிறது.',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — எந்த வேலைக்கு எந்த AI tool", TAG + " Use case வாரியாக ஒழுங்குபடுத்திய AI tools directory.", """
<h1>எந்த வேலைக்கு எந்த AI tool.</h1><p class="lede">Tool Use Cases என்பது நீங்கள் செய்ய விரும்பும் வேலையை வைத்து ஒழுங்குபடுத்திய AI tools directory — vibe coders, builders, AI மூலம் எதையாவது ship செய்யும் எல்லோருக்கும்.</p>
<input type="search" placeholder="Use cases-ஐ filter செய்யுங்கள் (உதா. video, coding, research)…" data-filter=".f" aria-label="Use cases-ஐ filter செய்யுங்கள்">
<h2>Use cases</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>புதிய launches, trending</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">எல்லா புதிய launches →</a></p>
<div class="cta"><b>AI tool உருவாக்குகிறீர்களா?</b> உங்கள் tool எந்த use case-இல் சிறப்பாக வேலை செய்கிறதோ, அங்கே மேலே feature ஆகுங்கள். <a class="btn" href="@R/@Psponsor/index.html">Slot-ஐ sponsor செய்யுங்கள்</a></div>"""),
 "use-cases": ("Use case வாரியாக AI tools — Tool Use Cases", "Use case வாரியாக AI tools-ஐப் பாருங்கள்: vibe coding, coding agents, debugging, game prototyping, video, writing, research, images இன்னும் பல.", """
<h1>Use cases</h1><p class="lede">வேலையைத் தேர்ந்தெடுங்கள். எந்த tools try செய்யத் தகுந்தவை, ஏன் என்று நாங்கள் சொல்கிறோம்.</p>
<input type="search" placeholder="Use cases-ஐ filter செய்யுங்கள்…" data-filter=".f" aria-label="Filter"><div class="grid">{CARDS}</div>"""),
 "tools": ("எல்லா AI tools A முதல் Z வரை — Tool Use Cases", "Tool Use Cases directory-யில் உள்ள ஒவ்வொரு AI tool-உம், அது என்ன செய்யும், எந்த use cases-க்குப் பொருந்தும்.", """
<h1>எல்லா tools</h1><input type="search" placeholder="Tools-ஐ filter செய்யுங்கள்…" data-filter=".f" aria-label="Tools-ஐ filter செய்யுங்கள்"><div class="grid">{ROWS}</div>"""),
 "new": ("புதிய, trending AI tools — Tool Use Cases", "Builders-க்கான கவனிக்க வேண்டிய, trending AI tool launches: coding agents, video models, research tools இன்னும் பல.", """
<h1>புதிய launches, trending</h1><p class="lede">கடந்த ஆறு வாரங்களில் வந்த, builders-க்கு முக்கியமான AI tool launches மற்றும் பெரிய updates. ஒவ்வொன்றுக்கும் தேதி, அதிகாரப்பூர்வ அறிவிப்பின் link, அது பொருந்தும் use case ஆகியவற்றைக் கொடுத்துள்ளோம்.</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Tool Use Cases-ஐ sponsor செய்யுங்கள் — உங்கள் AI tool-ஐ feature செய்யுங்கள்", "Tool உருவாக்குபவர்கள், தொடர்புடைய use-case pages-இன் மேலே தெளிவாக label செய்யப்பட்ட featured slot-ஐ sponsor செய்யலாம்.", """
<h1>ஒரு use case-ஐ sponsor செய்யுங்கள்</h1><p class="lede">Vibe coders, builders tool-ஐத் தேர்ந்தெடுக்கும் அந்த நேரத்திலேயே அவர்களைச் சென்றடையுங்கள்.</p>
<h2>இது எப்படி வேலை செய்கிறது</h2><ul><li>ஒவ்வொரு use-case page-இன் மேலேயும் ஒரு <b>Sponsored / Featured</b> slot இருக்கும்.</li><li>அதில் எப்போதும் தெளிவாக "Sponsored" என்று இருக்கும், எங்கள் editorial தேர்வுகளிலிருந்து தனியாக வைக்கப்படும்.</li><li>அந்த use case-க்கு உண்மையிலேயே பொருந்தும் tools-ஐ மட்டுமே ஏற்றுக்கொள்கிறோம்.</li><li>Sponsorship எங்கள் கருத்துகளையோ rankings-ஐயோ ஒருபோதும் மாற்றாது.</li></ul>
<h2>உதாரணம்</h2>{SPONSOR_CARD}
<div class="cta">விலை, availability பற்றி அறிய தொடர்புகொள்ளுங்கள். <a class="btn" href="{SPONSOR_MAILTO}">Sponsor செய்ய email அனுப்புங்கள்</a></div>"""),
 "about": ("எங்களைப் பற்றி — Tool Use Cases", "Tool Use Cases என்பது use case வாரியாக ஒழுங்குபடுத்திய AI tools-இன் சுயாதீனமான, autonomous-ஆக இயங்கும் directory.", """
<h1>எங்களைப் பற்றி</h1><p class="lede">Tool Use Cases ஒரே ஒரு கேள்விக்குப் பதில் சொல்கிறது: இந்த வேலைக்கு நான் எந்த AI tool-ஐப் பயன்படுத்த வேண்டும்?</p>
<p>பெரும்பாலான AI directories வெறும் பெரிய lists தான். நாங்கள் use case வாரியாக ஒழுங்குபடுத்துகிறோம், ஒவ்வொரு தேர்வுக்கும் எளிய மொழியில் ஒரு சின்னக் கருத்தைத் தருகிறோம், அதனால் நீங்கள் ஒரு நிமிடத்தில் முடிவெடுக்கலாம்.</p>
<p>இந்த site autonomous-ஆக இயங்குகிறது — ஒரு AI operator இதை update செய்கிறது, இதற்கான மனிதப் பொறுப்பு Lali Publications-இடம் உள்ளது. உண்மையான, நன்கு அறியப்பட்ட tools-ஐ மட்டுமே list செய்கிறோம், கற்பனையான scores அல்லது user எண்ணிக்கைகளை publish செய்வதில்லை.</p>
<p>Tool Use Cases-ஐ Lali Publications வெளியிடுகிறது, அவர்களே <a href="https://agentusecases.ai">agentusecases.ai</a>-ஐயும் நடத்துகிறார்கள். நாங்கள் list செய்யும் எந்த tool-உடனும் எங்களுக்குத் தொடர்பு இல்லை, sponsorships rankings-ஐ ஒருபோதும் மாற்றாது.</p>
<p>இது site-இன் தமிழ் version, <a href="@R/about/index.html" hreflang="en">ஆங்கில version</a>-இல் உள்ள அதே use cases, அதே தேர்வுகள், அதே rankings-உடன்.</p>
<p>திருத்தங்கள், பரிந்துரைகள் அல்லது sponsorships-க்கு: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("Subscribe செய்ததற்கு நன்றி — Tool Use Cases", "Tool Picks Weekly-க்கான உங்கள் signup கிடைத்துவிட்டது.", """
<h1>நீங்கள் list-இல் சேர்ந்துவிட்டீர்கள். நன்றி!</h1><p class="lede">Tool Picks Weekly-க்கான உங்கள் signup கிடைத்துவிட்டது. அடுத்த issue திங்கட்கிழமை வரும். இப்போதைக்கு newsletter ஆங்கிலத்தில் வருகிறது.</p>
<p><a class="btn" href="@R/@Pindex.html">Tool Use Cases-க்குத் திரும்புங்கள்</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "AI tool use cases",
 "uc_coll": ("AI tool use cases", "Use case வாரியாக AI tools-ஐப் பாருங்கள்."),
 "tools_crumb": "எல்லா tools", "tools_coll": ("எல்லா AI tools A முதல் Z வரை", "Tool Use Cases directory-யில் உள்ள ஒவ்வொரு AI tool-உம்."),
 "new_crumb": "புதிய launches, trending", "new_coll": ("புதிய, trending AI tools", "Builders-க்கான கவனிக்க வேண்டிய, trending AI tool launches."),
 "sponsor_crumb": "Sponsor",
 "about_crumb": "எங்களைப் பற்றி", "about_coll": ("Tool Use Cases பற்றி", "Use case வாரியாக ஒழுங்குபடுத்திய AI tools-இன் சுயாதீனமான, autonomous-ஆக இயங்கும் directory, Lali Publications வெளியீடு."),
}
