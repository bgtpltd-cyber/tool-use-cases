"""Bengali (bn) locale for Tool Use Cases.
Style: natural, everyday Bengali (cholito bhasha) the way Indian tech creators write. Product names and common
tech terms (vibe coding, AI agent, deploy, debugging, RAG, API, prompt...) stay in Latin script.
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "bn"
PREFIX = "bn/"
SHORT = "BN"
NATIVE = "বাংলা"
ENGLISH_NAME = "Bengali"
INDIA = True
OG_LOCALE = "bn_IN"
RSS_LANG = "bn"

TAG = "কোন কাজের জন্য কোন AI টুল — vibe coders আর builders-দের জন্য।"

UI = {
 "nav_use_cases": "Use cases", "nav_tools": "টুলস", "nav_new": "নতুন লঞ্চ",
 "nav_newsletter": "নিউজলেটার", "nav_sponsor": "স্পনসর", "nav_about": "আমাদের কথা",
 "home": "হোম", "use_cases": "Use cases",
 "og_alt": "Tool Use Cases: আপনার কাজ অনুযায়ী র‍্যাঙ্ক করা AI টুলস",
 "footer": "Tool Use Cases · Lali Publications-এর উদ্যোগ ·",
 "nl_h2": "Vibe coders-দের জন্য প্রতি সপ্তাহে বাছাই করা AI টুলস",
 "nl_p": "নতুন টুলস + কোন টুল কোন কাজে লাগে। একদম ফ্রি। আপাতত নিউজলেটারটা ইংরেজিতে পাঠানো হয়।",
 "nl_placeholder": "apni@example.com", "nl_aria": "ইমেল অ্যাড্রেস", "nl_button": "সাবস্ক্রাইব করুন",
 "nl_subject": "Tool Use Cases newsletter signup (bn)",
 "nl_small": "ইমেল আসবে Lali Publications থেকে। কোনো spam নেই, যখন খুশি unsubscribe করতে পারবেন।",
 "nl_latest": "লেটেস্ট ইস্যু পড়ুন: {LINK} (ইংরেজিতে)।",
 "verdict": "আমাদের মত:", "our_picks": "আমাদের বাছাই", "related": "সম্পর্কিত use cases",
 "browse_all": "সব use cases দেখুন →",
 "disclaimer": "এই বাছাই আমাদের নিজেদের, এর জন্য কেউ টাকা দেয়নি। দাম আর ফিচার প্রায়ই বদলায় — প্রতিটা টুলের অফিশিয়াল সাইট দেখে নিন।",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} {names} আর অন্য টুলস নিয়ে আমাদের মত।",
 "review_name": "{tool} — {title}",
 "sponsored": "Sponsored", "sponsor_h3": "আপনার টুল এখানে",
 "sponsor_p": "এই ফিচার্ড স্লটটা সেইসব টুল নির্মাতাদের জন্য, যাদের টুল এই use case-এ সত্যিই মানানসই। সবসময় পরিষ্কারভাবে লেবেল করা থাকে এবং আমাদের বাছাই থেকে আলাদা রাখা হয়।",
 "sponsor_link": "স্পনসর করতে ইমেল করুন",
 "new_badge": "উল্লেখযোগ্য / ট্রেন্ডিং",
 "last_updated": 'সর্বশেষ আপডেট: {date}', "earlier_h2": 'আগের লঞ্চ', "earlier_p": 'এই আপডেটের আগে আমরা যে লঞ্চগুলো দেখিয়েছিলাম। এগুলো আর নতুন নয়, তবে জেনে রাখার মতো।', "fits": 'Use case:', "source": 'সূত্র',
 "rss_title": "Tool Use Cases (বাংলা)",
 "rss_desc": "Tool Picks Weekly-র ইস্যু (ইংরেজিতে) আর নজর রাখার মতো নতুন AI টুল লঞ্চ।",
 "rss_new_prefix": "নতুন ও ট্রেন্ডিং: ", "rss_issue_suffix": " (ইংরেজিতে)",
 "rss_cat_newsletter": "নিউজলেটার", "rss_cat_new": "নতুন লঞ্চ",
 "llms_h2": "বাংলায় (bn)",
 "llms_intro": "পুরো সাইট বাংলায়, ইংরেজি ভার্সনের মতোই একই use cases, একই বাছাই আর একই র‍্যাঙ্কিং।",
 "llms_other": [("হোম", ""), ("সব AI টুলস A থেকে Z", "tools/"), ("নতুন লঞ্চ ও ট্রেন্ডিং", "new/"), ("আমাদের কথা", "about/"), ("স্পনসর", "sponsor/")],
}

TOOLS = {
 "cursor": "AI-first কোড এডিটর (VS Code-এর fork), যাতে chat, inline edits আর agent mode আছে।",
 "claude": "Anthropic-এর AI অ্যাসিস্ট্যান্ট, লম্বা ডকুমেন্ট, লেখালেখি আর কোডে দারুণ।",
 "claude-code": "Anthropic-এর terminal-এ চলা agentic coding টুল।",
 "chatgpt": "OpenAI-এর সব কাজের AI অ্যাসিস্ট্যান্ট, chat, images, voice আর search সহ।",
 "codex": "OpenAI-এর coding agent, যা cloud-এ বা CLI থেকে আপনার repos-এ কাজ করে।",
 "copilot": "AI pair programmer, VS Code, JetBrains আর GitHub-এ বিল্ট-ইন।",
 "v0": "Vercel-এর AI app/UI builder, যা prompts থেকে React + Tailwind অ্যাপ বানায়।",
 "lovable": "Prompt থেকে full-stack ওয়েব অ্যাপ বানানোর builder, Supabase integration সহ।",
 "replit": "ব্রাউজারের IDE, যার agent একটা prompt থেকে অ্যাপ বানিয়ে deploy-ও করে দেয়।",
 "bolt": "StackBlitz-এর ব্রাউজারে চলা prompt-to-app builder।",
 "windsurf": "Cognition-এর AI কোড এডিটর (আগে Windsurf): পুরো IDE, সাথে local আর cloud coding agents চালানোর command center।",
 "opencode": "Terminal, desktop বা IDE-র জন্য open-source (MIT) coding agent, যা local models সহ 75+ model providers-এর সাথে চলে।",
 "devin": "Cognition-এর autonomous software engineering agent।",
 "gemini": "Google-এর AI অ্যাসিস্ট্যান্ট, বিশাল context windows আর Google integration সহ।",
 "perplexity": "AI answer engine, যা ওয়েবে সার্চ করে আর sources-ও দেখায়।",
 "notebooklm": "Google-এর research notebook (আগে NotebookLM), যা আপনার আপলোড করা sources থেকেই উত্তর দেয়।",
 "elicit": "Academic papers খোঁজা আর সারাংশ করার জন্য AI research অ্যাসিস্ট্যান্ট।",
 "notion-ai": "Notion workspaces-এর ভেতরে বিল্ট-ইন AI writing আর Q&A।",
 "grammarly": "যেখানেই টাইপ করুন, সেখানেই grammar, tone আর rewrites-এ সাহায্য করে এমন writing অ্যাসিস্ট্যান্ট।",
 "midjourney": "Image generator, যা জোরালো aesthetic আর artistic আউটপুটের জন্য পরিচিত।",
 "dalle": "ChatGPT-র ভেতরে OpenAI-এর image generation, instructions মানতে আর ছবিতে text বসাতে ভালো।",
 "ideogram": "Image generator, যা ছবিতে পরিষ্কার পড়া যায় এমন text বসাতে বিশেষভাবে ভালো।",
 "flux": "High-quality image models-এর একটা ফ্যামিলি, কয়েকটা open weights সহ।",
 "firefly": "Adobe-এর generative image টুলস, commercial ব্যবহারে নিরাপদ থাকার মতো করে train করা।",
 "sd": "Open image models-এর ফ্যামিলি, যা আপনি লোকালি চালাতে পারেন (যেমন ComfyUI দিয়ে)।",
 "runway": "AI ভিডিও generation আর editing suite (Gen-series models)।",
 "elevenlabs": "একদম আসলের মতো AI voiceover, voice cloning আর dubbing।",
 "descript": "Transcript এডিট করে ভিডিও আর podcasts এডিট করুন।",
 "heygen": "AI avatar ভিডিও আর ভিডিও translation।",
 "capcut": "Free plan সহ ভিডিও এডিটর; auto-captions আর বেশিরভাগ AI tools-এর জন্য Pro লাগে।",
 "opus": "লম্বা ভিডিওকে নিজে থেকেই ছোট vertical clips-এ বদলে দেয়।",
 "veo": "Google DeepMind-এর text-to-video model, native audio সহ।",
 "rosebud": "Prompts থেকে গেম বানানোর ব্রাউজার টুল (Three.js/Phaser)।",
 "scenario": "আপনার নিজের training sets থেকে একই স্টাইলের game art assets বানায়।",
 "meshy": "Game assets-এর জন্য text/image থেকে 3D model generation।",
 "suno": "পুরো গান বানিয়ে দেয়, গেম/ভিডিওর placeholder মিউজিকের জন্য কাজের।",
 "sentry": "Error monitoring, AI root-cause analysis আর fix-এর সাজেশন সহ।",
 "deepseek": "চীনের AI ল্যাব, যার open-weight reasoning models শক্তিশালী আর সস্তা।",
 "ollama": "Open models (Llama, Qwen ইত্যাদি) এক command-এ লোকালি চালান।",
 "manus": "General-purpose autonomous agent, যা ওয়েব ব্রাউজ করে কয়েক ধাপের কাজ শেষ করে।",
 "kling": "Kuaishou-র text/image-to-video generator।",
 "grok": "xAI-এর অ্যাসিস্ট্যান্ট, X আর ওয়েবে real-time search সহ।",
 "mcp": "AI agents-কে টুলস আর ডেটার সঙ্গে জোড়ার open standard।",
 "n8n": "Open-source workflow automation, AI agent nodes সহ; ফ্রিতে self-host করুন বা ওদের cloud ব্যবহার করুন।",
 "make": "Visual no-code automation builder, হাজার হাজার অ্যাপ জুড়ে কয়েক ধাপের scenarios-এর জন্য।",
 "zapier": "সবচেয়ে বেশি অ্যাপের সঙ্গে কানেক্ট করা no-code automation প্ল্যাটফর্ম, এখন AI steps আর agents সহ।",
 "framer": "ডিজাইনারদের জন্য ওয়েবসাইট builder, AI page generation, CMS আর hosting সহ।",
 "stitch": "Google-এর prompt-to-UI ডিজাইন টুল (আগে Galileo AI), যা Figma আর কোডে export করে।",
 "uizard": "নতুনদের জন্য সহজ AI UI mockup টুল; prompts আর sketches-কে অ্যাপ স্ক্রিনে বদলায়।",
 "figma": "UI ডিজাইনের standard টুল, বিল্ট-ইন AI ফিচার আর prompt-to-prototype-এর জন্য Figma Make সহ।",
 "openai-tts": "OpenAI-এর speech API: সস্তা, natural কণ্ঠ, যা instructions দিয়ে নিয়ন্ত্রণ করা যায়।",
 "lyria": "Gemini অ্যাপে Google-এর music model: vocals বা instrumental সহ প্রায় 3 মিনিট পর্যন্ত গান, MP3-তে ডাউনলোড করা যায়।",
 "aiva": "Instrumental, orchestral আর soundtrack মিউজিকের জন্য AI composer, MIDI export সহ।",
 "surfer": "SEO আর AI search visibility টুল (আগে SurferSEO), যার content editor আপনার draft-কে top-ranking পেজগুলোর সাথে তুলনা করে স্কোর দেয়।",
 "clearscope": "Keyword coverage আর content grading-এর জন্য premium content-optimization টুল।",
 "lavender": "Sales email coach, যা আপনার inbox-এর ভেতরেই cold emails স্কোর করে আর নতুন করে লেখে।",
 "julius": "Spreadsheets আর ডেটা ফাইলের সঙ্গে chat করে analysis আর charts পান।",
 "excel-copilot": "Excel-এর ভেতরে Copilot, আপনার workbooks-এ formulas, analysis আর charts-এর জন্য।",
 "powerpoint-copilot": "PowerPoint-এর ভেতরে Copilot: prompt বা ফাইল থেকে deck-এর draft বানায়, slides যোগ করে আর content নতুন করে লেখে বা সাজায়।",
 "gamma": "Prompt বা outline থেকে presentations, docs আর ওয়েব পেজ বানায়।",
 "beautiful-ai": "Smart templates সহ slide সফটওয়্যার, content যোগ করলেই নিজে থেকে format হয়ে যায়।",
 "rodin": "Text বা image থেকে 3D বানানোর generator, পরিষ্কার topology, PBR materials আর Blender, Unity, Unreal-এর plugins সহ।",
 "tripo": "দ্রুত text/image-to-3D generator, auto-rigging আর clean topology-র অপশন সহ।",
 "fireflies": "AI meeting bot, যা Zoom/Meet/Teams কল রেকর্ড, transcribe আর summarize করে।",
 "otter": "Real-time মিটিং transcription আর AI summaries, কাজে লাগার মতো free tier সহ।",
 "grain": "Clips আর highlights-কেন্দ্রিক meeting recorder, sales আর customer টিমে জনপ্রিয়।",
 "langchain": "LLM অ্যাপ বানানোর open-source framework: RAG, tools আর integrations।",
 "llamaindex": "Open-source framework, যার ফোকাস LLMs-কে আপনার documents আর ডেটার সঙ্গে জোড়া (RAG)।",
 "vercel": "Frontend আর Next.js hosting, git-push deploys, previews আর AI SDK সহ।",
 "netlify": "Static sites আর ওয়েব অ্যাপের জন্য git-based hosting, functions আর forms সহ।",
 "railway": "প্রায় কোনো config ছাড়াই repo থেকে backends, databases আর workers deploy করুন।",
 "fly": "Docker containers সারা দুনিয়ায় users-দের কাছাকাছি চালান; full-stack অ্যাপের জন্য ভালো (2026 থেকে GPU machines বন্ধ)।",
 "wxt": "TypeScript-এ cross-browser extensions বানানোর Vite-based open-source framework।",
 "canva": "অনলাইন ডিজাইন টুল, Magic Studio AI ফিচার আর রেডিমেড templates সহ।",
 "langgraph": "LangChain-এর framework, stateful আর নিয়ন্ত্রণে রাখা যায় এমন multi-step agent graphs-এর জন্য।",
 "crewai": "Role-based AI agents-এর টিম বানানোর open-source Python framework।",
 "ms-agent-framework": "Python আর .NET-এর জন্য Microsoft-এর open-source agent framework, AutoGen আর Semantic Kernel-এর উত্তরসূরি।",
 "openai-agents": "OpenAI-এর হালকা SDK, agents-এর জন্য tools, handoffs, guardrails আর tracing সহ।",
 "recraft": "ডিজাইনারদের জন্য AI image generator, যা editable vector (SVG) graphics আর icons দেয়।",
 "looka": "AI logo maker, যা one-time fee-তে logo-র সঙ্গে brand kit-ও বানিয়ে দেয়।",
 "intercom-fin": "Intercom-এর AI support agent, যা আপনার help content থেকে কাস্টমারদের প্রশ্নের সমাধান করে।",
 "zendesk": "Zendesk help desk-এ বিল্ট-ইন AI agents আর agent-assist ফিচার।",
 "helpscout": "সহজ shared inbox আর help desk, AI drafts, summaries আর AI Answers সহ।",
 "firecrawl": "API, যা ওয়েবসাইট crawl করে LLMs-এর জন্য পরিষ্কার markdown বা structured ডেটা ফেরত দেয়।",
 "browserbase": "AI agents-এর জন্য hosted headless browsers, সঙ্গে open-source Stagehand framework।",
 "apify": "Scraping প্ল্যাটফর্ম, হাজার হাজার রেডিমেড scrapers ('Actors') আর scheduling সহ।",
 "postman": "Requests বানানো আর টেস্ট করার API প্ল্যাটফর্ম, সাথে Agent Mode যা আপনার সব collections জুড়ে AI দিয়ে কাজ করে।",
 "bruno": "Open-source, offline API client, যা collections-কে git-এ সাধারণ ফাইল হিসেবে রাখে।",
 "coda": "Doc আর spreadsheet মেলানো workspace (আগে Coda), tables, automations আর বিল্ট-ইন AI সহ।",
 "mem": "AI notes অ্যাপ, যা নোটগুলো নিজে থেকেই গুছিয়ে রাখে আর সেগুলোর সঙ্গে chat করতে দেয়।",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Vibe coding-এর জন্য সেরা AI", "বলুন, চালান, ঠিকঠাক করুন। এমন টুলস যা দিয়ে বেশিরভাগটা কথা বলেই সফটওয়্যার বানানো যায়।", [
  "ডিফল্ট পছন্দ: আসল codebase আর এডিটর আপনার হাতেই থাকে, কিন্তু বেশিরভাগ টাইপিং করে AI।",
  "আইডিয়া থেকে auth আর database সহ চালু ওয়েব অ্যাপে পৌঁছানোর সবচেয়ে দ্রুত রাস্তা, কোনো setup ছাড়াই।",
  "সেরা, যখন দ্রুত একটা polished React/Next.js UI চাই আর Vercel-এ deploy করার প্ল্যান আছে।",
  "Hosting সহ সবকিছু ব্রাউজারে — দ্রুত বানানো আর শেয়ার করার মতো prototypes-এর জন্য ভালো।",
  "Lovable-এর মতোই; এক ট্যাবেই full-stack demo দাঁড় করাতে দারুণ।",
  "Cursor-এর বিকল্প, একসাথে কয়েকটা agent চালানোর জন্য তৈরি; Cursor জমছে না মনে হলে একবার ট্রাই করুন।"]),
 "best-ai-coding-agents": ("সেরা AI coding agents", "এমন agents যারা টাস্ক নেয়, একাধিক ফাইল এডিট করে, commands চালায় আর একটা diff নিয়ে ফেরে।", [
  "Terminal থেকে multi-file পরিবর্তনে দুর্দান্ত; বড় agentic কাজের জন্য অনেকেরই ফেভারিট।",
  "পুরো এডিটরের ভেতরে agent mode, তাই প্রতিটা পরিবর্তন চোখে দেখে রিভিউ করতে পারবেন।",
  "টাস্কগুলো cloud-এ parallel চালাতে দিয়ে দিন, তারপর তৈরি হওয়া PRs রিভিউ করুন।",
  "Copilot-এর coding agent GitHub issues থেকে কাজ করে — আপনার টিম যদি GitHub-এই থাকে তাহলে একদম মানানসই।",
  "পুরো tickets শুরু থেকে শেষ পর্যন্ত দিয়ে দেওয়ার জন্য বানানো; দামি, টিমের জন্য।",
  "ফ্রি, open-source আর নিয়মিত develop হচ্ছে; যেকোনো model ব্যবহার করুন, local-ও, বা আপনার আগের Claude, ChatGPT বা Copilot plan।"]),
 "best-ai-for-fixing-broken-code": ("ভাঙা কোড আর errors ঠিক করার সেরা AI", "Stack trace পেস্ট করুন, fix পান। এমন টুলস যারা শুধু কোড বানাতে নয়, debugging-এও ভালো।", [
  "Error-এর সঙ্গে দরকারি ফাইলগুলো পেস্ট করুন; আসল root cause নিয়ে ভাবতে খুব পোক্ত।",
  "পুরো প্রজেক্টের context নিয়ে সেখানেই fix করে — বারবার copy-paste করতে হয় না।",
  "ভালো general debugger, আর issues reproduce করতে Python-ও চালাতে পারে।",
  "'Fix' আর '/explain' সরাসরি এডিটরে, ঠিক যেখানে লাল দাগটা দেখাচ্ছে।",
  "Production-এ errors ধরে আর আসল traces দেখে fix সাজেস্ট করে।",
  "ওকে tests চালাতে দিন, failure পড়তে দিন, আর সব green না হওয়া পর্যন্ত চালিয়ে যেতে দিন।"]),
 "best-ai-for-game-prototyping": ("গেম prototyping-এর সেরা AI", "খেলার মতো একটা আইডিয়া দ্রুত স্ক্রিনে আনুন — কোড, art, 3D আর মিউজিক।", [
  "একটা prompt থেকে ব্রাউজার গেম বানান আর অন্যদের গেম remix করুন।",
  "আসল engines-এর জন্য (Godot, Unity, Phaser): scripts লেখে AI, play-test করেন আপনি।",
  "Game art আপনার নিজের স্টাইলে একরকম রাখে — গেমে AI art-এর সবচেয়ে কঠিন অংশ এটাই।",
  "Levels-এর blockout করতে দ্রুত 3D props আর characters।",
  "কয়েক মিনিটেই placeholder (বা final) soundtrack।",
  "Recording booth ছাড়াই character voice lines আর sound effects।"]),
 "best-ai-for-video-youtube": ("ভিডিও আর YouTube-এর সেরা AI", "Footage বানান, তাড়াতাড়ি এডিট করুন, voice দিন আর Shorts কাটুন।", [
  "Talking-head ভিডিও doc-এর মতো এডিট করুন; filler words সরিয়ে দেয়। YouTubers-দের অনেক সময় বাঁচায়।",
  "B-roll আর effects-এর জন্য pro-level AI ভিডিও generation আর editing টুলস।",
  "সাউন্ড সহ high-quality generated clips; cinematic b-roll-এর জন্য দারুণ।",
  "Voiceover আর অন্য ভাষায় dubbing-এ নিজের ক্যাটাগরিতে সেরা।",
  "লম্বা ভিডিও বা stream নিজে থেকেই Shorts/TikToks-এ বদলে দেয়।",
  "রোজকার কাজের practical এডিটর, যার free plan কাজে লাগে; auto-captions-এর জন্য এখন Pro লাগে।",
  "Avatar presenters আর lip-synced translation, যখন ক্যামেরার সামনে আসতে চান না।"]),
 "best-ai-writing-assistants": ("সেরা AI writing assistants", "Drafting, editing আর rewriting — docs, blog posts, READMEs, emails।", [
  "বড় assistants-দের মধ্যে সবচেয়ে natural শোনানো লেখা; দারুণ editor-ও।",
  "সব কাজে চলনসই all-rounder: drafts, rewrites আর variations এক chat-এই।",
  "সেরা, যদি আপনার notes আর docs আগে থেকেই Notion-এ থাকে।",
  "যেখানেই টাইপ করুন সেখানেই polish — ব্রাউজার, ইমেল, docs।",
  "Google Docs আর Gmail-এর ভেতরে বেশ সুবিধাজনক।"]),
 "best-ai-for-research": ("রিসার্চের জন্য সেরা AI", "Sources খুঁজুন, পড়ুন আর summarize করুন — এমন citations সহ যা যাচাই করা যায়।", [
  "Live ওয়েব থেকে দ্রুত, sources সহ উত্তর; ঝটপট রিসার্চের জন্য প্রথম পছন্দ।",
  "নিজের sources আপলোড করুন আর সেগুলোর ভিত্তিতেই উত্তর (আর audio overviews) পান।",
  "Deep research mode কোনো টপিকে লম্বা, citations সহ রিপোর্ট বানায়।",
  "Deep Research আর সঙ্গে Google Search integration।",
  "বিশেষ করে academic papers আর literature reviews-এর জন্য বানানো।",
  "X-এ এই মুহূর্তে লোকে কী বলছে, সেটা জানতে কাজের।"]),
 "best-ai-image-generation": ("Image generation-এর সেরা AI", "Thumbnails, concept art, mockups, memes।", [
  "ডিফল্ট লুক সবচেয়ে ভালো; art, moodboards আর concept art-এর জন্য দারুণ।",
  "Detailed instructions মানতে আর কথা বলে এডিট করতে সবচেয়ে ভালো।",
  "এটা বেছে নিন যখন ছবিতে পড়া যায় এমন text লাগবে — logos, posters, thumbnails।",
  "Top-tier quality, আর লোকাল ব্যবহারের জন্য open-weight অপশনও আছে।",
  "Commercial কাজের জন্য তুলনায় নিরাপদ; Photoshop-এ বিল্ট-ইন।",
  "ফ্রি আর লোকাল, যদি GPU থাকে আর tinkering করতে ভালো লাগে (ComfyUI)।"]),
 "best-ai-for-running-local-models": ("লোকালি AI চালানোর সেরা টুলস", "নিজের মেশিনে প্রাইভেট AI, চালাতে কোনো খরচ নেই।", [
  "এক command-এ open models ডাউনলোড করে চালান; শুরু করার সবচেয়ে সহজ উপায়।",
  "শক্তিশালী open-weight models, লোকালি চালানো যায় বা API দিয়ে সস্তায় ব্যবহার করা যায়।",
  "Ollama-তে চলা কোনো model-এর সাথে জুড়ে দিন, পেয়ে যাবেন offline coding agent।",
  "Local image models-এর ক্লাসিক ecosystem।"]),
 "best-ai-for-automation-workflows": ("Automation workflows-এর সেরা AI", "নিজের অ্যাপগুলো জুড়ে দিন আর একঘেয়ে ধাপগুলো AI-কে সামলাতে দিন — triggers, agents আর glue code।", [
  "Builders-দের জন্য টপ পিক: AI agent nodes, দরকারে কোড, আর self-host একদম ফ্রি।",
  "জটিল branching flows-এর জন্য সেরা visual canvas; প্রতি task-এ Zapier-এর চেয়ে সস্তা।",
  "সবচেয়ে বেশি অ্যাপ আর সবচেয়ে সহজ setup; ভলিউম বেশি হলে বাদ দিন, কারণ খরচ দ্রুত বাড়ে।",
  "No-code দিয়ে যখন আর হচ্ছে না, তখন ওকে দিয়ে script বা webhook handler লিখিয়ে নিন।",
  "একবারের multi-step ওয়েব কাজের জন্য; নির্ভরযোগ্য scheduled workflows-এর বিকল্প নয়।"]),
 "best-ai-for-landing-pages": ("Landing pages-এর সেরা AI", "এক বিকেলেই আইডিয়া থেকে live, দেখতে ভালো একটা landing page।", [
  "টপ পিক: prompt থেকে forms আর database সহ পুরো পেজ বানান, তারপর এক ক্লিকে publish করুন।",
  "সেরা, যদি custom logic-এর চেয়ে design polish আর সহজ hosting বেশি জরুরি হয়; পরে marketers-ও এটা এডিট করতে পারবেন।",
  "Vercel-এ deploy করলে দারুণ React/Tailwind আউটপুট; কোডিং নিয়ে একটু স্বচ্ছন্দ হতে হবে।",
  "Lovable-এর দ্রুত full-stack বিকল্প; কোনো আইডিয়া তাড়াতাড়ি টেস্ট করতে ভালো।",
  "Codebase আগে থেকে থাকলে builders বাদ দিন — শুধু সেখানেই পেজটা যোগ করুন।"]),
 "best-ai-for-ui-design": ("UI design-এর সেরা AI", "Prompt বা sketch থেকে screens, তারপর এমন কিছু যা আপনি বানাতে পারবেন।", [
  "টপ পিক, যদি ডিজাইনারদের সঙ্গে কাজ করেন: standard টুল, এখন AI আর Figma Make বিল্ট-ইন সহ।",
  "Mockup-এর ধাপটাই বাদ দেয়: চালু UI কোড বানায়, যা সঙ্গে সঙ্গে ship করা যায়।",
  "Google-এর ফ্রি আর দ্রুত prompt-to-UI exploration (আগে Galileo AI); Figma-তে export করে।",
  "Wireframes বানানো non-designers-দের জন্য সবচেয়ে সহজ; pixel-level কন্ট্রোল চাইলে বাদ দিন।",
  "যখন 'ডিজাইন'-টা আসলে একটা clickable, চালু অ্যাপ হতে হবে।"]),
 "best-ai-voice-tts": ("সেরা AI voice আর text-to-speech", "মাইক ছাড়াই voiceovers, narration, cloned voices আর অ্যাপের speech।", [
  "টপ পিক: সবচেয়ে natural কণ্ঠ, cloning আর dubbing। Creators-দের ডিফল্ট।",
  "API দিয়ে অ্যাপ আর bulk narration-এর জন্য সবচেয়ে সস্তা ভালো কণ্ঠ; voice-এর অপশন কম।",
  "সেরা, যখন রেকর্ডিংও এডিট করছেন — ভুল বলা শব্দ নিজের cloned voice দিয়েই ঠিক করুন।",
  "যখন কথা বলা avatar বা lip-synced translation-ও লাগবে।"]),
 "best-ai-for-music": ("মিউজিকের জন্য সেরা AI", "Prompt থেকে গান, soundtracks আর background মিউজিক।", [
  "টপ পিক: vocals সহ পুরো গান কয়েক সেকেন্ডে; ভালো কিছু পাওয়ার সবচেয়ে সহজ উপায়।",
  "সরাসরি Gemini অ্যাপে vocals সহ গান, MP3-তে ডাউনলোড করা যায়; Suno-র আউটপুট generic লাগলে ট্রাই করে দেখুন।",
  "Instrumental আর orchestral scores-এর জন্য সেরা, MIDI export সহ যা DAW-তে এডিট করা যায়।",
  "Voice-এর পাশাপাশি মিউজিক আর sound-effect generation-ও আছে, আগে থেকে ব্যবহার করলে কাজের।"]),
 "best-ai-for-seo-content": ("SEO content-এর সেরা AI", "Rank করতে পারে এমন পেজের রিসার্চ, outline আর লেখা — AI-এর আবর্জনা publish না করে।", [
  "আসল লেখার জন্য টপ পিক: সবচেয়ে natural drafts আর আপনার নিজের লেখার সেরা editor।",
  "যা rank করছে তার সঙ্গে তুলনা করে আপনার draft-কে স্কোর দেয়; কাজের guardrails, কিন্তু শুধু স্কোরের জন্য লিখবেন না।",
  "টিম আর agencies-এর জন্য premium content grading; একার সাইটের জন্য দরকারের চেয়ে বেশি।",
  "কোনো টপিক আর competitors কী কভার করছে, তা নিয়ে দ্রুত, sources সহ রিসার্চ।",
  "Briefs, outlines আর meta descriptions-এর জন্য পোক্ত all-rounder; topic gaps-এর জন্য deep research।"]),
 "best-ai-for-sales-emails": ("Sales emails-এর সেরা AI", "আরও ভালো cold আর follow-up emails লিখুন — personal, ছোট, আর দেখে বোঝা যাবে না যে AI লিখেছে।", [
  "টপ পিক: prospect-এর context দিন আর ছোট, মানুষের লেখার মতো draft পান। সবসময় এডিট করুন।",
  "Drafts আর variants-এর জন্য সমান ভালো; নিজের ভঙ্গি সেট করতে custom instructions ব্যবহার করুন।",
  "সরাসরি Gmail/Outlook-এ coaching আর scoring; রোজ cold email পাঠালে কাজে দেবে।",
  "প্রথম লাইন লেখার আগে prospect আর কোম্পানি নিয়ে দ্রুত রিসার্চ।",
  "যেখানেই টাইপ করুন সেখানে tone আর clarity-তে final polish।"]),
 "best-ai-for-data-spreadsheets": ("ডেটা আর spreadsheets-এর সেরা AI", "CSVs analyze করুন, formulas লিখুন আর charts বানান — সহজ ভাষায় জিজ্ঞেস করেই।", [
  "টপ পিক: ফাইল আপলোড করুন, analysis আর charts-এর জন্য এটা আসল Python চালায়।",
  "ডেটা বুঝিয়ে বলা আর formulas লেখায় দারুণ; আপলোড করা ফাইলে analysis-ও চালাতে পারে।",
  "শুধু data analysis-এর জন্য বানানো, non-coders-দের জন্য আরও সহজ workflow সহ।",
  "সেরা, যখন কাজটা আগে থেকেই Excel-এ; Microsoft 365 Copilot প্ল্যান লাগবে।",
  "Google Sheets-এর ভেতরে সবচেয়ে স্বাভাবিক পছন্দ।"]),
 "best-ai-for-presentations": ("Presentations-এর সেরা AI", "Outline থেকে মোটামুটি ভালো slide deck, তাড়াতাড়ি।", [
  "টপ পিক: prompt লিখুন বা notes পেস্ট করুন, এক মিনিটে দেখতে ভালো deck পান; PowerPoint-এ export হয়।",
  "সেইসব টিমের জন্য সেরা যাদের একরকম, on-brand slides চাই যার format ঠিক থাকে।",
  "আগে গল্প আর outline লিখিয়ে নিন, বা ওকে দিয়ে slide content আর code-based decks বানিয়ে নিন।",
  "Outlines আর speaker notes-এর জন্য ভালো, আর ডাউনলোড করার মতো .pptx ফাইলও বানাতে পারে।",
  "মানে হয়, যদি আপনার decks আগে থেকেই PowerPoint-এ থাকে আর আপনার Microsoft 365 প্ল্যানে Copilot থাকে।"]),
 "best-ai-for-3d-assets": ("3D assets-এর সেরা AI", "Text বা images থেকে props, characters আর models বানান।", [
  "টপ পিক: textures সহ পোক্ত text/image-to-3D, আর game engines-এর জন্য exports।",
  "Auto-rigging সহ দ্রুত generation; যে characters animate করতে হবে তাদের জন্য দারুণ।",
  "Text বা image থেকে detailed 3D, পরিষ্কার topology সহ; plugins দিয়ে models সরাসরি Blender, Unity বা Unreal-এ চলে যায়।",
  "পুরো প্রজেক্ট জুড়ে একই স্টাইলের game assets-এর জন্য সেরা।",
  "2.5D/sprite গেমে 3D পুরোটাই বাদ দিন — concept art আর textures লোকালি বানান।"]),
 "best-ai-for-meeting-notes": ("মিটিং notes-এর সেরা AI", "কল রেকর্ড, transcribe আর summarize করুন, যাতে কাউকে notes নিতে না হয়।", [
  "টপ পিক: নিজে থেকেই আপনার কলে জয়েন করে, ভালো summaries, search আর CRM integrations সহ।",
  "সেরা free tier আর live transcription; summaries একটু বেশি generic।",
  "Sales আর customer কলের জন্য সেরা, যেখানে শুধু notes নয়, clips শেয়ার করতে চান।",
  "আপনার টিম আগে থেকেই Notion-এ থাকলে বিল্ট-ইন meeting notes — আলাদা bot লাগে না।",
  "কোনো bot-ই নেই: transcript পেস্ট করুন আর আরও নিখুঁত summaries আর action items পান। Automatic recording চাইলে বাদ দিন।"]),
 "best-ai-for-chatbots-rag": ("Chatbots আর RAG-এর সেরা AI", "এমন অ্যাসিস্ট্যান্ট বানান যা আপনার নিজের docs থেকে উত্তর দেয় — no-code থেকে custom কোড পর্যন্ত।", [
  "শুরু করার জন্য টপ পিক: আপলোড করা docs-এর ভিত্তিতে একটা Claude Project কয়েক মিনিটেই টিম অ্যাসিস্ট্যান্ট হয়ে যায়। নিজের সাইটে বসাতে চাইলে বাদ দিন।",
  "আপনার ফাইল সহ একটা ChatGPT Project-ও একই কাজ করে। Custom GPTs 11 ডিসেম্বর 2026-এ বন্ধ হচ্ছে, তাই নতুন করে বানাবেন না।",
  "সেরা code framework, যখন আসল কঠিন কাজ হলো ডেটা ঠিকমতো ingest আর retrieve করা।",
  "Integrations-এর সবচেয়ে বড় ecosystem; সহজ bots-এর জন্য দরকারের চেয়ে বেশি abstraction।",
  "ওকে দিয়ে একটা হালকা custom RAG অ্যাপ লিখিয়ে নিন, আর নিজের টুলসের সঙ্গে জুড়তে MCP ব্যবহার করুন।",
  "আপনার sources-এর উপর zero-setup Q&A, embed করার জন্য নয়, ব্যক্তিগত ব্যবহারের জন্য।"]),
 "best-ai-for-deploy-hosting": ("AI দিয়ে বানানো অ্যাপের সেরা hosting", "আপনার AI টুলস এইমাত্র যে অ্যাপ বানাল, সেটা কোথায় ship করবেন। এগুলো AI টুল নয়, hosting প্ল্যাটফর্ম — AI-এর সাহায্যে যারা বানান তাদের সঙ্গে কতটা মানানসই, সেই হিসেবে বাছাই।", [
  "Next.js/React অ্যাপের (আর v0 থেকে আসা যেকোনো কিছুর) জন্য টপ পিক: git-এ push করুন, previews সহ live URL পান।",
  "Static sites আর সহজ অ্যাপের জন্য দারুণ, ভালো free tier আর বিল্ট-ইন forms সহ।",
  "Backends, databases আর background workers-এর জন্য সবচেয়ে সহজ জায়গা। শুধু static sites হলে বাদ দিন।",
  "Docker বা একাধিক regions লাগলে সেরা; setup একটু বেশি লাগে। Fly 2026-এ GPUs দেওয়া বন্ধ করেছে।",
  "এক জায়গাতেই বানান আর host করুন — সবচেয়ে সহজ, যদি কখনো deploy config ছুঁতেই না চান।"]),
 "best-ai-for-chrome-extensions": ("Chrome extensions বানানোর সেরা AI", "'এটার জন্য একটা বোতাম থাকা উচিত' থেকে চালু browser extension পর্যন্ত।", [
  "টপ পিক: manifest, scripts আর popup বানায়, আর আপনি reload করে টেস্ট করার সময় context ধরে errors ঠিক করে।",
  "পুরো extension-এর কাঠামো দাঁড় করাতে আর Manifest V3 permission issues নিয়ে বারবার কাজ করতে দারুণ।",
  "ছোট, এক ফাইলের extension-এর জন্য ঠিক আছে। দেখে নিন Manifest V3 ব্যবহার করছে কিনা, কারণ পুরনো examples সব জায়গায় ছড়িয়ে আছে।",
  "নিজে AI টুল নয়, তবে AI টুলের সাথে ভালো চলে: Vite-based, নিয়মিত maintain করা framework যা extension-এর boilerplate সরিয়ে দেয়।",
  "নিজে লিখতে চাইলে Chrome APIs-এর জন্য ভালো autocomplete।"]),
 "best-ai-for-thumbnails-youtube-packaging": ("YouTube thumbnails আর packaging-এর সেরা AI", "Thumbnails, titles আর সেই hook যা ক্লিক এনে দেয়।", [
  "Thumbnails-এর জন্য টপ পিক, যেখানে বোল্ড আর পড়া যায় এমন text ছবিতেই বসানো।",
  "কথা বলে এডিট করার জন্য (\"মুখটা আরেকটু অবাক দেখাও\") আর একই chat-এ titles নিয়ে brainstorming-এর জন্য সেরা।",
  "যেখানে আসলে final thumbnail-এর layout বানান: templates, background removal আর Magic টুলস।",
  "সবচেয়ে চোখ-ধাঁধানো backgrounds আর scenes; text পরে Canva-তে যোগ করুন।",
  "Title আর thumbnail-text-এর জোড়া নিয়ে brainstorm করুন; কোনো আইডিয়া clickbait-এর মতো হলে সোজাসুজি বলে দেয়।"]),
 "best-ai-for-agent-frameworks": ("সেরা AI agent frameworks", "Tools, memory আর multi-step workflows সহ নিজের agents বানানোর code frameworks।", [
  "শুরু করার জন্য টপ পিক: ছোট API, যাতে tools, handoffs আর tracing বিল্ট-ইন।",
  "সেরা, যখন পরিষ্কার কন্ট্রোল চাই: state, retries, human-in-the-loop আর production-এ নির্ভরযোগ্যতা।",
  "Role-based multi-agent 'crews'-এর prototype বানানোর সবচেয়ে দ্রুত উপায়; বড় স্কেলে নিয়ন্ত্রণে রাখা কঠিন।",
  "AutoGen আর Semantic Kernel-এর Microsoft-এর তৈরি উত্তরসূরি: Python বা .NET-এ agents আর graph-based workflows; Azure-এ স্বাভাবিক পছন্দ।",
  "Framework নয়, কিন্তু যেকোনো agent-কে tools দেওয়ার standard উপায় এটাই। নিজের tools MCP servers হিসেবে বানান।"]),
 "best-ai-for-logos-brand": ("Logos আর branding-এর সেরা AI", "Logo আইডিয়া, brand marks আর শুরুর brand kit, তাড়াতাড়ি।", [
  "টপ পিক: আসল vector (SVG) logos আর icons বানায়, যা এডিট আর scale করা যায়।",
  "পড়া যায় এমন wordmarks সহ logo concepts-এর জন্য সেরা; যেটা বাছবেন সেটা তবুও vectorize করতে হবে।",
  "Non-designers-দের জন্য logo আর brand kit-এর সবচেয়ে সহজ all-in-one; ফলাফল একটু template-এর মতো লাগতে পারে।",
  "Final logo files-এর চেয়ে brand-এর mood আর visual direction খুঁজে দেখার জন্য দারুণ।",
  "কথা বলে কোনো concept নিয়ে এগোনোর জন্য কাজের। কিছু trademark করার আগে দেখে নিন সেটা সত্যিই আলাদা কিনা।"]),
 "best-ai-for-customer-support": ("Customer support-এর সেরা AI", "AI agents আর AI-এর লেখা replies দিয়ে কাস্টমারদের আরও তাড়াতাড়ি উত্তর দিন।", [
  "Tickets নিজে থেকে সমাধান করার জন্য টপ পিক; Intercom help desk ছাড়াও চলে। দাম প্রতি resolution হিসেবে, তাই ভলিউমের সঙ্গে খরচ বাড়ে।",
  "আগে থেকেই Zendesk-এ থাকলে স্বাভাবিক পছন্দ; ছোট টিমের জন্য setup আর pricing ভারী।",
  "ছোট টিমের জন্য সেরা, যাদের বড় প্ল্যাটফর্ম নয়, AI drafts আর answers সহ একটা সহজ inbox দরকার।",
  "কোনো প্ল্যাটফর্ম লাগবে না: ticket আর নিজের docs পেস্ট করুন, যত্ন করে লেখা, বন্ধুত্বপূর্ণ reply draft পান।",
  "একই আইডিয়া; আপনার docs আর tone guide একটা ChatGPT Project-এ রাখুন, যাতে প্রতিটা draft একই context থেকে শুরু হয়।"]),
 "best-ai-for-scraping": ("Web scraping-এর সেরা AI", "ওয়েবসাইটগুলোকে অ্যাপ, রিসার্চ আর AI pipelines-এর জন্য পরিষ্কার ডেটায় বদলান। প্রতিটা সাইটের terms আর robots.txt মেনে চলুন।", [
  "Builders-দের জন্য টপ পিক: একটা API call-এ সাইট থেকে পরিষ্কার markdown বা structured JSON।",
  "সেরা, যখন রেডিমেড scraper আগে থেকেই আছে (maps, social, e-commerce); scheduling বিল্ট-ইন।",
  "যেসব সাইটে আসল logged-in ব্রাউজার বা বারবার ক্লিক লাগে; Stagehand-এর সঙ্গে ব্যবহার করুন।",
  "আসল পেজ দেখে custom scraper লেখে আর debug করে; একবারের বা অদ্ভুত সাইটের জন্য সেরা।",
  "একই কাজ, আপনার এডিটরের ভেতরে — ভালো, যখন scraper কোনো চালু প্রজেক্টের অংশ।"]),
 "best-ai-for-api-testing": ("API testing-এর সেরা AI", "Requests লিখুন, tests বানান আর ফেল করা endpoints debug করুন।", [
  "আপনার টিম আগে থেকেই Postman ব্যবহার করলে টপ পিক: Agent Mode আপনার collections থেকে tests লেখে, ভাঙা requests ঠিক করে আর APIs-এর documentation বানায়।",
  "আপনার API কোডের ঠিক পাশেই test suites (pytest, Jest ইত্যাদি) বানায় আর ঠিক করে।",
  "OpenAPI spec বা ফেল করা response পেস্ট করুন, আর আপনার চোখ এড়িয়ে যাওয়া test cases আর edge cases পান।",
  "ঝটপট test scripts আর mock ডেটার জন্য ভালো; জিনিস চালিয়ে দেখতে Python চালাতে পারে।",
  "নিজে AI নয়, কিন্তু এর সাধারণ ফাইলের collections AI এডিটররা সহজে পড়তে-লিখতে পারে। Offline আর git-native থাকতে চাইলে এটা বাছুন।"]),
 "best-ai-for-notion-docs": ("Notes আর docs-এর সেরা AI", "AI দিয়ে নিজের notes আর টিম docs লিখুন, গোছান আর সার্চ করুন।", [
  "টপ পিক, যদি আপনার workspace Notion-এ হয়: AI writing, সব পেজ জুড়ে Q&A আর meeting notes, সব এক জায়গায়।",
  "Docs-এর আসল লেখা আর এডিটিংয়ের জন্য সেরা; Projects রেফারেন্স মেটেরিয়াল হাতের কাছে রাখে।",
  "Docs-এর draft বানানো আর নতুন করে সাজানোয় versatile, প্রথম outline থেকে পুরো rewrite পর্যন্ত।",
  "এটা বাছুন যখন আপনার docs আসলে tables আর automations সহ ছোট ছোট অ্যাপ।",
  "ব্যক্তিগত notes যা নিজে থেকেই গুছিয়ে যায়; টিম wikis-এর জন্য বাদ দিন।"]),
}

NEW = {
 "claude-code": "Anthropic-এর terminal coding agent — সবচেয়ে বেশি আলোচিত dev টুলসের একটা।",
 "codex": "OpenAI-এর নতুন করে লঞ্চ করা Codex coding agent (cloud + CLI)।",
 "veo": "Google-এর ভিডিও model, এখন synced audio-ও বানায়।",
 "manus": "Autonomous general agent, multi-step কাজের জন্য যা ভাইরাল হয়েছিল।",
 "lovable": "দ্রুত বেড়ে চলা prompt-to-app builder।",
 "notebooklm": "Audio Overviews research notes-কে podcasts-এ বদলে দিয়েছে।",
 "kling": "AI ভিডিও generation-এ জোরালো প্রতিযোগী।",
 "deepseek": "Open-weight reasoning models, যা pricing-এ নাড়া দিয়েছে।",
 "mcp": "সেই open protocol, যা এখন বেশিরভাগ agent টুলস tools access-এর জন্য সাপোর্ট করে।",
 "windsurf": "Agentic এডিটর, যা সরাসরি Cursor-এর সঙ্গে টক্কর দেয়।",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['জানুয়ারি', 'ফেব্রুয়ারি', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগস্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর']
DATE_MD = '{d} {m}'
DATE_MDY = '{d} {m}, {y}'
RELEASES = {
 'replit-monitoring-agent': 'Replit-এর Agent এখন published app-এর alerts background-এ নজরে রাখে, production-এর সমস্যা খতিয়ে দেখে আর একটা fix test করে। fix আপনি নিজে review করে publish করেন, যদি না experimental Auto-republish setting চালু করেন।',
 'lovable-supabase-create': 'Lovable এখন backend ছাড়া app-এর জন্য Supabase project তৈরি করে সেটা জুড়ে দেয়। organization আর region আপনি বাছেন (region পরে বদলানো যায় না), আর Supabase সেই project-এর বিল আপনার নিজের account-এ পাঠায়।',
 'voxtral-3': 'Mistral-এর নতুন speech-to-text আর text-to-speech models, সঙ্গে ফোন ও ওয়েবে real-time voice agents বানানোর SDK। Mistral-এর API (EU-hosted অপশনসহ) দিয়ে বা self-hosted।',
 'kling-4': 'Kuaishou-র নতুন ভিডিও model: এক পাসে 30 সেকেন্ড পর্যন্ত clips, দ্রুত মুভমেন্ট আর ক্যামেরা মুভে বেশি স্থিরতা, আর প্রতি কাজে 15টা পর্যন্ত reference assets ও 10টা keyframes।',
 'muse-spark-open': 'Meta-র open-weight model, coding আর agent-এর কাজের জন্য (816B parameters, 42B active, 1M-token context)। Meta এটা দুটো Mac Studio-তে চালায়; বেশিরভাগ মানুষের জন্য hosted APIs-ই সহজ পথ।',
 'claude-haiku-5-5': 'Anthropic-এর সবচেয়ে সস্তা আর দ্রুত model, বেশি ভলিউমের কাজের জন্য তৈরি: support bots, summaries আর coding subagents। Anthropic বলছে, এটা চালাতে Haiku 4.5-এর চেয়ে প্রায় 75% কম খরচ।',
 'nano-banana-2-1': 'Google-এর আপডেটেড image generation আর editing model: আরও ভালো edits, চরিত্রে বেশি consistency আর ছবিতে পরিষ্কার লেখা। Gemini অ্যাপ, AI Studio, Gemini API, Flow আর Stitch-এ পাওয়া যায়।',
 'copilot-dynamic-workflows': 'Multi-agent কাজ code-এ সাজিয়ে নিন (parallel steps, একে অপরকে যাচাই করা subagents, রিভিউয়ের জন্য checkpoints) — Copilot CLI, Copilot অ্যাপ আর Copilot SDK-তে। Public preview, সব plan-এ।',
 'heygen-video': 'HeyGen-এর প্রথম general-purpose ভিডিও model: টেক্সট, ছবি বা reference media থেকে 5 থেকে 15 সেকেন্ডের clips, যেখানে সংলাপ আর শব্দ একসঙ্গে তৈরি হয়। HeyGen API দিয়ে পাওয়া যায়।',
 'gpt-6-1-sol': 'OpenAI DevDay-তে আসা GPT-6 Sol-এর আপগ্রেড, যার ফোকাস agentic coding, computer use আর পেশাদার কাজ। OpenAI বলছে, অনেক কম দামে এটা GPT-6 Astra-র কাছাকাছি পৌঁছায়।',
 'openai-agents-api-computer-use': 'Agents API এখন computer use দিয়ে software চালাতে পারে, আর Codex-এর multi-agent ফিচার, tool search ও context compaction আপনার অ্যাপে নিয়ে আসে। Infrastructure চালায় OpenAI।',
 'claude-sonnet-5-5': 'Anthropic-এর দ্রুত আর সস্তা Sonnet, নির্দিষ্ট পরিসরের রোজকার কাজ আর bug fixing-এ সবচেয়ে ভালো। Sonnet 5-এর চেয়ে 30%+ দ্রুত, একই $2/$10 প্রতি million tokens দামে।',
 'lovable-free-chat': 'Lovable-এর সঙ্গে chat এখন রোজকার free সীমার মধ্যে বিনামূল্যে: features প্ল্যান করুন, অ্যাপের code আর database নিয়ে প্রশ্ন করুন বা লঞ্চের লেখা ড্রাফট করুন। Build করতে এখনও credits লাগে।',
 'cursor-projects': 'কোনো feature বা migration-এর মতো বড় কাজের জন্য beta: একটা coordinator agent cloud-এ চলে, কাজ প্ল্যান করে, অনেক subagents-কে ভাগ করে দেয় আর সময়ের সঙ্গে shared context ধরে রাখে।',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — কোন কাজের জন্য কোন AI টুল", TAG + " Use case অনুযায়ী সাজানো AI টুলসের বাছাই করা ডিরেক্টরি।", """
<h1>কোন কাজের জন্য কোন AI টুল।</h1><p class="lede">Tool Use Cases হলো AI টুলসের একটা ডিরেক্টরি, যা সাজানো হয়েছে আপনি কোন কাজটা করতে চাইছেন সেই অনুযায়ী — vibe coders, builders আর AI দিয়ে কিছু ship করা প্রত্যেকের জন্য।</p>
<input type="search" placeholder="Use cases ফিল্টার করুন (যেমন video, coding, research)…" data-filter=".f" aria-label="Use cases ফিল্টার করুন">
<h2>Use cases</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>নতুন লঞ্চ ও ট্রেন্ডিং</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">সব নতুন লঞ্চ দেখুন →</a></p>"""),
 "use-cases": ("AI টুল use cases — Tool Use Cases", "Use case অনুযায়ী AI টুলস দেখুন: vibe coding, coding agents, debugging, গেম prototyping, ভিডিও, লেখালেখি, রিসার্চ, images আর আরও অনেক কিছু।", """
<h1>Use cases</h1><p class="lede">কাজটা বেছে নিন। কোন টুলগুলো ট্রাই করার মতো আর কেন, আমরা বলে দেব।</p>
<input type="search" placeholder="Use cases ফিল্টার করুন…" data-filter=".f" aria-label="ফিল্টার করুন"><div class="grid">{CARDS}</div>"""),
 "tools": ("সব AI টুলস A থেকে Z — Tool Use Cases", "Tool Use Cases ডিরেক্টরির প্রতিটা AI টুল, সেটা কী করে আর কোন কোন use case-এ মানানসই।", """
<h1>সব টুলস</h1><input type="search" placeholder="টুলস ফিল্টার করুন…" data-filter=".f" aria-label="টুলস ফিল্টার করুন"><div class="grid">{ROWS}</div>"""),
 "new": ("নতুন আর ট্রেন্ডিং AI টুলস — Tool Use Cases", "Builders-দের জন্য উল্লেখযোগ্য আর ট্রেন্ডিং AI টুল লঞ্চ: coding agents, ভিডিও models, রিসার্চ টুলস আর আরও অনেক কিছু।", """
<h1>নতুন লঞ্চ ও ট্রেন্ডিং</h1><p class="lede">গত ছয় সপ্তাহের AI টুল লঞ্চ আর বড় আপডেট, যেগুলো builders-দের কাজে লাগে। প্রতিটির সঙ্গে তারিখ, অফিসিয়াল ঘোষণার লিংক আর কোন use case-এ এটা মানানসই, সেটা দেওয়া আছে।</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Tool Use Cases স্পনসর করুন — আপনার AI টুল ফিচার করান", "টুল নির্মাতারা মানানসই use-case পেজের একদম উপরে পরিষ্কারভাবে লেবেল করা একটা ফিচার্ড স্লট স্পনসর করতে পারেন।", """
<h1>একটা use case স্পনসর করুন</h1><p class="lede">Vibe coders আর builders-দের কাছে ঠিক সেই মুহূর্তে পৌঁছান, যখন তারা টুল বাছছেন।</p>
<h2>কীভাবে কাজ করে</h2><ul><li>প্রতিটা use-case পেজের একদম উপরে একটা <b>Sponsored / Featured</b> স্লট থাকে।</li><li>এতে সবসময় পরিষ্কারভাবে "Sponsored" লেখা থাকে আর এটা আমাদের editorial বাছাই থেকে আলাদা রাখা হয়।</li><li>আমরা শুধু সেইসব টুল নিই যা সত্যিই ওই use case-এ মানানসই।</li><li>স্পনসরশিপে আমাদের মত বা র‍্যাঙ্কিং কখনো বদলায় না।</li></ul>
<h2>উদাহরণ</h2>{SPONSOR_CARD}
<div class="cta">দাম আর কবে পাওয়া যাবে জানতে যোগাযোগ করুন। <a class="btn" href="{SPONSOR_MAILTO}">স্পনসর করতে ইমেল করুন</a></div>"""),
 "about": ("আমাদের কথা — Tool Use Cases", "Tool Use Cases একটা স্বাধীন, autonomously চলা ডিরেক্টরি, যেখানে AI টুলস use case অনুযায়ী সাজানো।", """
<h1>আমাদের কথা</h1><p class="lede">Tool Use Cases একটাই প্রশ্নের উত্তর দেয়: এই কাজের জন্য আমার কোন AI টুল ব্যবহার করা উচিত?</p>
<p>বেশিরভাগ AI ডিরেক্টরি শুধু বিশাল লিস্ট। আমরা use case অনুযায়ী সাজাই, আর প্রতিটা বাছাইয়ের সঙ্গে সহজ ভাষায় ছোট্ট একটা মত দিই, যাতে আপনি এক মিনিটেই ঠিক করে নিতে পারেন।</p>
<p>সাইটটা autonomously চলে — একটা AI operator এটা আপডেট রাখে, আর এর মানুষী দায়িত্ব Lali Publications-এর। আমরা শুধু আসল, পরিচিত টুলসই লিস্ট করি, আর বানানো স্কোর বা ইউজারের সংখ্যা publish করি না।</p>
<p>Tool Use Cases প্রকাশ করে Lali Publications, যারা <a href="https://agentusecases.ai">agentusecases.ai</a>-ও চালায়। আমরা যেসব টুল লিস্ট করি, তাদের কারও সঙ্গে আমাদের কোনো যোগ নেই।</p>
<p>এটা সাইটের বাংলা ভার্সন, যেখানে <a href="@R/about/index.html" hreflang="en">ইংরেজি ভার্সনের</a> মতোই একই use cases, একই বাছাই আর একই র‍্যাঙ্কিং।</p>
<p>সংশোধন বা পরামর্শের জন্য: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("সাবস্ক্রাইব করার জন্য ধন্যবাদ — Tool Use Cases", "Tool Picks Weekly-তে আপনার সাইনআপ পেয়ে গেছি।", """
<h1>আপনি লিস্টে যুক্ত হয়ে গেছেন। ধন্যবাদ!</h1><p class="lede">Tool Picks Weekly-তে আপনার সাইনআপ পেয়ে গেছি। পরের ইস্যু আসবে সোমবার। আপাতত নিউজলেটারটা ইংরেজিতে পাঠানো হয়।</p>
<p><a class="btn" href="@R/@Pindex.html">Tool Use Cases-এ ফিরে যান</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "AI টুল use cases",
 "uc_coll": ("AI টুল use cases", "Use case অনুযায়ী AI টুলস দেখুন।"),
 "tools_crumb": "সব টুলস", "tools_coll": ("সব AI টুলস A থেকে Z", "Tool Use Cases ডিরেক্টরির প্রতিটা AI টুল।"),
 "new_crumb": "নতুন লঞ্চ ও ট্রেন্ডিং", "new_coll": ("নতুন আর ট্রেন্ডিং AI টুলস", "Builders-দের জন্য উল্লেখযোগ্য আর ট্রেন্ডিং AI টুল লঞ্চ।"),
 "sponsor_crumb": "স্পনসর",
 "about_crumb": "আমাদের কথা", "about_coll": ("Tool Use Cases সম্পর্কে", "Use case অনুযায়ী সাজানো AI টুলসের স্বাধীন, autonomously চলা ডিরেক্টরি, Lali Publications-এর প্রকাশনা।"),
}
