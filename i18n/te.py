"""Telugu (te) locale for Tool Use Cases.
Style: natural, conversational Telugu the way Telugu tech creators write. Product names and common
tech terms (vibe coding, AI agent, deploy, debugging, RAG, API, prompt...) stay in Latin script.
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "te"
PREFIX = "te/"
SHORT = "TE"
NATIVE = "తెలుగు"
ENGLISH_NAME = "Telugu"
INDIA = True
OG_LOCALE = "te_IN"
RSS_LANG = "te"

TAG = "ఏ పనికి ఏ AI టూల్ — vibe coders, builders కోసం."

UI = {
 "nav_use_cases": "Use cases", "nav_tools": "టూల్స్", "nav_new": "కొత్త లాంచ్‌లు",
 "nav_newsletter": "న్యూస్‌లెటర్", "nav_sponsor": "స్పాన్సర్", "nav_about": "మా గురించి",
 "home": "హోమ్", "use_cases": "Use cases",
 "og_alt": "Tool Use Cases: మీ పనిని బట్టి ర్యాంక్ చేసిన AI టూల్స్",
 "footer": "Tool Use Cases · Lali Publications నుంచి ·",
 "nl_h2": "Vibe coders కోసం ప్రతి వారం ఎంచుకున్న AI టూల్స్",
 "nl_p": "కొత్త టూల్స్ + ఏ టూల్ ఏ పనికి పనికొస్తుందో. పూర్తిగా ఫ్రీ. ప్రస్తుతానికి న్యూస్‌లెటర్ ఇంగ్లీష్‌లో వస్తుంది.",
 "nl_placeholder": "meeru@example.com", "nl_aria": "ఈమెయిల్ అడ్రస్", "nl_button": "సబ్‌స్క్రైబ్ చేయండి",
 "nl_subject": "Tool Use Cases newsletter signup (te)",
 "nl_small": "ఈమెయిల్ Lali Publications నుంచి వస్తుంది. Spam ఉండదు, ఎప్పుడైనా unsubscribe చేయొచ్చు.",
 "nl_latest": "లేటెస్ట్ ఇష్యూ చదవండి: {LINK} (ఇంగ్లీష్‌లో).",
 "verdict": "మా అభిప్రాయం:", "our_picks": "మా ఎంపికలు", "related": "సంబంధిత use cases",
 "browse_all": "అన్ని use cases చూడండి →",
 "disclaimer": "ఈ ఎంపికలు మావే, వీటికి ఎవరూ డబ్బులు ఇవ్వలేదు. ధరలు, ఫీచర్లు తరచూ మారుతుంటాయి — ప్రతి టూల్ అఫీషియల్ సైట్‌ను చెక్ చేయండి.",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} {names}, ఇంకా మరికొన్ని టూల్స్‌పై మా అభిప్రాయం.",
 "review_name": "{tool} — {title}",
 "sponsored": "Sponsored", "sponsor_h3": "మీ టూల్ ఇక్కడ",
 "sponsor_p": "ఈ ఫీచర్డ్ స్లాట్ ఈ use caseకి నిజంగా సరిపోయే టూల్స్ తయారు చేసేవారి కోసం. ఎప్పుడూ స్పష్టంగా లేబుల్ చేసి ఉంటుంది, మా ఎంపికల నుంచి వేరుగా ఉంటుంది.",
 "sponsor_link": "స్పాన్సర్ చేయడానికి ఈమెయిల్ చేయండి",
 "new_badge": "గమనించదగ్గవి / ట్రెండింగ్",
 "last_updated": 'చివరి అప్\u200cడేట్: {date}', "earlier_h2": 'ఇంతకు ముందువి', "earlier_p": 'ఈ అప్\u200cడేట్\u200cకు ముందు మేం చూపించిన లాంచ్\u200cలు. ఇప్పుడు కొత్తవి కావు, కానీ తెలుసుకోదగ్గవి.', "fits": 'Use case:', "source": 'మూలం',
 "rss_title": "Tool Use Cases (తెలుగు)",
 "rss_desc": "Tool Picks Weekly ఇష్యూలు (ఇంగ్లీష్‌లో), ఒక్కసారి చూడాల్సిన కొత్త AI టూల్ లాంచ్‌లు.",
 "rss_new_prefix": "కొత్తగా, ట్రెండింగ్‌లో: ", "rss_issue_suffix": " (ఇంగ్లీష్‌లో)",
 "rss_cat_newsletter": "న్యూస్‌లెటర్", "rss_cat_new": "కొత్త లాంచ్‌లు",
 "llms_h2": "తెలుగులో (te)",
 "llms_intro": "పూర్తి సైట్ తెలుగులో, ఇంగ్లీష్ వెర్షన్‌లో ఉన్న అవే use cases, అవే ఎంపికలు, అవే ర్యాంకింగ్‌లతో.",
 "llms_other": [("హోమ్", ""), ("అన్ని AI టూల్స్ A నుంచి Z", "tools/"), ("కొత్త లాంచ్‌లు, ట్రెండింగ్", "new/"), ("మా గురించి", "about/"), ("స్పాన్సర్", "sponsor/")],
}

TOOLS = {
 "cursor": "AI-first కోడ్ ఎడిటర్ (VS Code fork), chat, inline edits, agent mode తో.",
 "claude": "Anthropic AI అసిస్టెంట్, పెద్ద డాక్యుమెంట్లు, రాయడం, కోడ్‌లో చాలా బలంగా ఉంటుంది.",
 "claude-code": "Anthropic నుంచి terminalలో నడిచే agentic coding టూల్.",
 "chatgpt": "OpenAI ఆల్-పర్పస్ AI అసిస్టెంట్, chat, images, voice, search తో.",
 "codex": "OpenAI coding agent, cloudలో లేదా CLI నుంచి మీ reposపై పని చేస్తుంది.",
 "copilot": "VS Code, JetBrains, GitHubలో బిల్ట్-ఇన్‌గా ఉండే AI pair programmer.",
 "v0": "Vercel AI app/UI builder, prompts నుంచి React + Tailwind యాప్‌లు తయారు చేస్తుంది.",
 "lovable": "Prompt నుంచి full-stack వెబ్ యాప్ తయారుచేసే builder, Supabase integration తో.",
 "replit": "బ్రౌజర్‌లో IDE, దీని agent ఒక prompt నుంచి యాప్ తయారుచేసి deploy కూడా చేస్తుంది.",
 "bolt": "StackBlitz నుంచి బ్రౌజర్‌లోనే నడిచే prompt-to-app builder.",
 "windsurf": "Cognition AI కోడ్ ఎడిటర్ (గతంలో Windsurf): పూర్తి IDE, దానితో పాటు local, cloud coding agents రన్ చేసే command center.",
 "opencode": "Terminal, desktop లేదా IDE కోసం open-source (MIT) coding agent; local models సహా 75+ model providers తో పనిచేస్తుంది.",
 "devin": "Cognition నుంచి autonomous software engineering agent.",
 "gemini": "Google AI అసిస్టెంట్, చాలా పెద్ద context windows, Google integration తో.",
 "perplexity": "వెబ్‌లో సెర్చ్ చేసి sources కూడా చూపించే AI answer engine.",
 "notebooklm": "Google research notebook (గతంలో NotebookLM), మీరు అప్‌లోడ్ చేసిన sources ఆధారంగానే సమాధానాలు ఇస్తుంది.",
 "elicit": "Academic papers వెతకడానికి, వాటిని summarize చేయడానికి AI research అసిస్టెంట్.",
 "notion-ai": "Notion workspacesలోనే బిల్ట్-ఇన్ AI writing, Q&A.",
 "grammarly": "మీరు ఎక్కడ టైప్ చేసినా grammar, tone, rewrites లో సాయం చేసే writing అసిస్టెంట్.",
 "midjourney": "బలమైన aesthetic, artistic అవుట్‌పుట్‌కి పేరున్న image generator.",
 "dalle": "ChatGPT లోపల OpenAI image generation, instructions పాటించడంలో, ఇమేజ్‌లో text పెట్టడంలో బాగుంటుంది.",
 "ideogram": "ఇమేజ్‌లలో స్పష్టంగా చదవగలిగే text పెట్టడంలో ప్రత్యేకంగా బాగుండే image generator.",
 "flux": "High-quality image models ఫ్యామిలీ, వాటిలో కొన్ని open weights తో వస్తాయి.",
 "firefly": "Adobe generative image టూల్స్, commercial వాడకానికి సురక్షితంగా ఉండేలా train చేశారు.",
 "sd": "లోకల్‌గా రన్ చేయగలిగే open image models ఫ్యామిలీ (ఉదా. ComfyUI ద్వారా).",
 "runway": "AI వీడియో generation, editing suite (Gen-series models).",
 "elevenlabs": "నిజంలా అనిపించే AI voiceover, voice cloning, dubbing.",
 "descript": "Transcript ఎడిట్ చేసి వీడియోలు, podcasts ఎడిట్ చేయండి.",
 "heygen": "AI avatar వీడియోలు, వీడియో translation.",
 "capcut": "Free plan ఉన్న వీడియో ఎడిటర్; auto-captions, చాలా AI tools కోసం Pro కావాలి.",
 "opus": "పెద్ద వీడియోలను ఆటోమేటిక్‌గా చిన్న vertical clipsగా మారుస్తుంది.",
 "veo": "Google DeepMind text-to-video model, native audio తో.",
 "rosebud": "Prompts నుంచి గేమ్స్ తయారు చేసే బ్రౌజర్ టూల్ (Three.js/Phaser).",
 "scenario": "మీ సొంత training sets నుంచి ఒకే స్టైల్‌లో game art assets తయారు చేస్తుంది.",
 "meshy": "Game assets కోసం text/image నుంచి 3D model generation.",
 "suno": "పూర్తి పాటలు తయారు చేస్తుంది, గేమ్/వీడియోలకు placeholder మ్యూజిక్‌కి పనికొస్తుంది.",
 "sentry": "Error monitoring, AI root-cause analysis, fix సూచనలతో.",
 "deepseek": "చైనా AI ల్యాబ్, దీని open-weight reasoning models బలంగా, చౌకగా ఉంటాయి.",
 "ollama": "Open models (Llama, Qwen వంటివి) ఒక్క commandతో లోకల్‌గా రన్ చేయండి.",
 "manus": "వెబ్ బ్రౌజ్ చేసి, చాలా స్టెప్స్ ఉన్న పనులు పూర్తి చేసే general-purpose autonomous agent.",
 "kling": "Kuaishou text/image-to-video generator.",
 "grok": "xAI అసిస్టెంట్, X, వెబ్‌లో real-time search తో.",
 "mcp": "AI agentsని టూల్స్‌తో, డేటాతో కలపడానికి open standard.",
 "n8n": "Open-source workflow automation, AI agent nodes తో; ఫ్రీగా self-host చేయండి లేదా వాళ్ల cloud వాడండి.",
 "make": "వేలకొద్దీ యాప్‌లలో మల్టీ-స్టెప్ scenarios కోసం visual no-code automation builder.",
 "zapier": "అత్యధిక యాప్‌లతో కనెక్ట్ అయ్యే no-code automation ప్లాట్‌ఫామ్, ఇప్పుడు AI steps, agents తో.",
 "framer": "డిజైనర్ల కోసం వెబ్‌సైట్ builder, AI page generation, CMS, hosting తో.",
 "stitch": "Google prompt-to-UI డిజైన్ టూల్ (గతంలో Galileo AI), Figmaకి, కోడ్‌కి export చేస్తుంది.",
 "uizard": "కొత్తవాళ్లకు సులువైన AI UI mockup టూల్; prompts, sketchesని యాప్ స్క్రీన్‌లుగా మారుస్తుంది.",
 "figma": "UI డిజైన్‌కి standard టూల్, బిల్ట్-ఇన్ AI ఫీచర్లు, prompt-to-prototype కోసం Figma Make తో.",
 "openai-tts": "OpenAI speech API: చౌకగా, natural గా ఉండే వాయిస్‌లు, instructionsతో కంట్రోల్ చేయొచ్చు.",
 "lyria": "Gemini యాప్‌లో Google music model: vocals లేదా instrumental తో సుమారు 3 నిమిషాల వరకు పాటలు, MP3గా డౌన్‌లోడ్ చేసుకోవచ్చు.",
 "aiva": "Instrumental, orchestral, soundtrack మ్యూజిక్ కోసం AI composer, MIDI export తో.",
 "surfer": "SEO, AI search visibility టూల్ (గతంలో SurferSEO); దీని content editor మీ draftని top-ranking పేజీలతో పోల్చి స్కోర్ ఇస్తుంది.",
 "clearscope": "Keyword coverage, content grading కోసం premium content-optimization టూల్.",
 "lavender": "మీ inbox లోపలే cold emailsకి స్కోర్ ఇచ్చి, తిరిగి రాసే sales email coach.",
 "julius": "Spreadsheets, డేటా ఫైల్స్‌తో chat చేసి analysis, charts పొందండి.",
 "excel-copilot": "Excel లోపల Copilot, మీ workbooksపై formulas, analysis, charts కోసం.",
 "powerpoint-copilot": "PowerPoint లోపల Copilot: prompt లేదా ఫైల్ నుంచి deck draft చేస్తుంది, slides జోడిస్తుంది, content తిరిగి రాస్తుంది లేదా మళ్లీ సర్దుతుంది.",
 "gamma": "Prompt లేదా outline నుంచి presentations, docs, వెబ్ పేజీలు తయారు చేస్తుంది.",
 "beautiful-ai": "Smart templates ఉన్న slide సాఫ్ట్‌వేర్, content జోడిస్తుంటే దానంతటదే format అవుతుంది.",
 "rodin": "Text లేదా image నుంచి 3D తయారుచేసే generator; క్లీన్ topology, PBR materials, Blender, Unity, Unreal plugins తో.",
 "tripo": "వేగవంతమైన text/image-to-3D generator, auto-rigging, clean topology ఆప్షన్‌లతో.",
 "fireflies": "Zoom/Meet/Teams కాల్స్‌ని రికార్డ్, transcribe, summarize చేసే AI meeting bot.",
 "otter": "Real-time మీటింగ్ transcription, AI summaries, బాగా పనికొచ్చే free tier తో.",
 "grain": "Clips, highlights చుట్టూ తయారైన meeting recorder, sales, customer టీమ్స్‌లో పాపులర్.",
 "langchain": "LLM యాప్‌లు తయారు చేయడానికి open-source framework: RAG, tools, integrations.",
 "llamaindex": "LLMsని మీ documents, డేటాతో కలపడం (RAG) పై ఫోకస్ చేసే open-source framework.",
 "vercel": "Frontend, Next.js hosting, git-push deploys, previews, AI SDK తో.",
 "netlify": "Static sites, వెబ్ యాప్‌ల కోసం git-based hosting, functions, forms తో.",
 "railway": "దాదాపు config లేకుండానే repo నుంచి backends, databases, workers deploy చేయండి.",
 "fly": "Docker containersని ప్రపంచవ్యాప్తంగా users దగ్గరగా రన్ చేయండి; full-stack యాప్‌లకు బాగుంటుంది (2026 నుంచి GPU machines లేవు).",
 "wxt": "TypeScriptలో cross-browser extensions తయారు చేయడానికి Vite-based open-source framework.",
 "canva": "ఆన్‌లైన్ డిజైన్ టూల్, Magic Studio AI ఫీచర్లు, రెడీమేడ్ templates తో.",
 "langgraph": "Stateful, కంట్రోల్‌లో ఉండే multi-step agent graphs కోసం LangChain framework.",
 "crewai": "Role-based AI agents టీమ్స్ కోసం open-source Python framework.",
 "ms-agent-framework": "Python, .NET కోసం Microsoft open-source agent framework; AutoGen, Semantic Kernel తర్వాత వాటి స్థానంలో వచ్చినది.",
 "openai-agents": "OpenAI తేలికపాటి SDK, agents కోసం tools, handoffs, guardrails, tracing తో.",
 "recraft": "డిజైనర్ల కోసం AI image generator, editable vector (SVG) graphics, icons ఇస్తుంది.",
 "looka": "One-time feeకి logoతో పాటు brand kit కూడా తయారు చేసే AI logo maker.",
 "intercom-fin": "Intercom AI support agent, మీ help content నుంచి కస్టమర్ల ప్రశ్నలు పరిష్కరిస్తుంది.",
 "zendesk": "Zendesk help deskలో బిల్ట్-ఇన్‌గా ఉండే AI agents, agent-assist ఫీచర్లు.",
 "helpscout": "సింపుల్ shared inbox, help desk, AI drafts, summaries, AI Answers తో.",
 "firecrawl": "వెబ్‌సైట్లను crawl చేసి LLMs కోసం క్లీన్ markdown లేదా structured డేటా ఇచ్చే API.",
 "browserbase": "AI agents కోసం hosted headless browsers, దానితో పాటు open-source Stagehand framework.",
 "apify": "వేలకొద్దీ రెడీమేడ్ scrapers ('Actors'), scheduling ఉన్న scraping ప్లాట్‌ఫామ్.",
 "postman": "Requests తయారు చేసి టెస్ట్ చేసే API ప్లాట్‌ఫామ్, మీ collections అంతటా AIతో పనిచేసే Agent Modeతో.",
 "bruno": "Open-source, offline API client, collectionsని gitలో సాధారణ ఫైల్స్‌గా దాచుకుంటుంది.",
 "coda": "Doc, spreadsheet కలిసిన workspace (గతంలో Coda), tables, automations, బిల్ట్-ఇన్ AIతో.",
 "mem": "Notesని ఆటోమేటిక్‌గా సర్దిపెట్టి, వాటితో chat చేయనిచ్చే AI notes యాప్.",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Vibe coding కోసం బెస్ట్ AI", "చెప్పండి, రన్ చేయండి, సరిచేయండి. ఎక్కువగా మాట్లాడుతూనే సాఫ్ట్‌వేర్ తయారు చేయనిచ్చే టూల్స్.", [
  "డిఫాల్ట్ ఎంపిక: అసలైన codebase, ఎడిటర్ మీ దగ్గరే ఉంటాయి, కానీ ఎక్కువ టైపింగ్ AI చేస్తుంది.",
  "ఐడియా నుంచి auth, database ఉన్న పని చేసే వెబ్ యాప్ వరకు అత్యంత వేగమైన దారి, ఏ setup లేకుండా.",
  "త్వరగా polished React/Next.js UI కావాలి, Vercelలో deploy చేయాలనుకుంటే ఇదే బెస్ట్.",
  "Hosting తో సహా అంతా బ్రౌజర్‌లోనే — త్వరగా తయారయ్యే, షేర్ చేయగలిగే prototypes కి బాగుంటుంది.",
  "Lovable లాంటిదే; ఒకే ట్యాబ్‌లో full-stack demo రెడీ చేయడానికి సూపర్.",
  "Cursorకి ప్రత్యామ్నాయం, ఒకేసారి చాలా agents రన్ చేయడానికి తయారైంది; Cursor నచ్చకపోతే ఒకసారి ట్రై చేయండి."]),
 "best-ai-coding-agents": ("బెస్ట్ AI coding agents", "టాస్క్ తీసుకుని, చాలా ఫైల్స్ ఎడిట్ చేసి, commands రన్ చేసి, diff తో తిరిగొచ్చే agents.", [
  "Terminal నుంచి multi-file మార్పుల్లో అదిరిపోతుంది; పెద్ద agentic పనులకు చాలామందికి ఫేవరెట్.",
  "పూర్తి ఎడిటర్ లోపలే agent mode, కాబట్టి ప్రతి మార్పును కళ్లతో చూసి రివ్యూ చేయొచ్చు.",
  "టాస్క్‌లను cloudలో parallelగా రన్ అయ్యేలా అప్పగించి, తర్వాత వచ్చిన PRs రివ్యూ చేయండి.",
  "Copilot coding agent GitHub issues నుంచి పని చేస్తుంది — మీ టీమ్ GitHubలోనే ఉంటే సహజంగా సరిపోతుంది.",
  "పూర్తి ticketsని మొదటి నుంచి చివరి వరకు అప్పగించడానికి తయారైంది; ఖరీదైనది, టీమ్స్ కోసం.",
  "ఫ్రీ, open-source, చురుగ్గా develop అవుతోంది; local వాటితో సహా ఏ model అయినా, లేదా మీ ప్రస్తుత Claude, ChatGPT, Copilot plan వాడొచ్చు."]),
 "best-ai-for-fixing-broken-code": ("పాడైన కోడ్, errors సరిచేయడానికి బెస్ట్ AI", "Stack trace పేస్ట్ చేయండి, fix పొందండి. కోడ్ తయారు చేయడమే కాదు, debugging లో కూడా బాగుండే టూల్స్.", [
  "Errorతో పాటు సంబంధిత ఫైల్స్ పేస్ట్ చేయండి; అసలు root cause గురించి ఆలోచించడంలో చాలా బలంగా ఉంటుంది.",
  "పూర్తి ప్రాజెక్ట్ context తో అక్కడికక్కడే fix చేస్తుంది — అటూ ఇటూ copy-paste అవసరం లేదు.",
  "మంచి general debugger, issues reproduce చేయడానికి Python కూడా రన్ చేయగలదు.",
  "'Fix', '/explain' నేరుగా ఎడిటర్‌లోనే, ఎర్ర గీత ఉన్న చోటే.",
  "Productionలో errorsని పట్టుకుని, అసలైన traces ఆధారంగా fixes సూచిస్తుంది.",
  "దాన్ని tests రన్ చేయనివ్వండి, failure చదవనివ్వండి, అంతా green అయ్యేవరకు మళ్లీ మళ్లీ ప్రయత్నించనివ్వండి."]),
 "best-ai-for-game-prototyping": ("గేమ్ prototyping కోసం బెస్ట్ AI", "ఆడగలిగే ఐడియాను త్వరగా స్క్రీన్ మీదకు తీసుకురండి — కోడ్, art, 3D, మ్యూజిక్.", [
  "ఒక prompt తో బ్రౌజర్ గేమ్ తయారు చేయండి, ఇతరుల గేమ్స్‌ని remix చేయండి.",
  "అసలైన engines కోసం (Godot, Unity, Phaser): scripts AI రాస్తుంది, play-test మీరు చేస్తారు.",
  "Game art ని మీ సొంత స్టైల్‌లో ఒకేలా ఉంచుతుంది — గేమ్స్‌లో AI artలో అసలు కష్టమైన భాగం ఇదే.",
  "Levels blockout చేయడానికి త్వరగా 3D props, characters.",
  "నిమిషాల్లో placeholder (లేదా final) soundtrack.",
  "Recording booth లేకుండానే character voice lines, sound effects."]),
 "best-ai-for-video-youtube": ("వీడియో, YouTube కోసం బెస్ట్ AI", "Footage తయారు చేయండి, వేగంగా ఎడిట్ చేయండి, voice ఇవ్వండి, Shortsగా కట్ చేయండి.", [
  "Talking-head వీడియోలను doc లాగా ఎడిట్ చేయండి; filler words తీసేస్తుంది. YouTubers కి చాలా టైమ్ సేవ్ చేస్తుంది.",
  "B-roll, effects కోసం pro-level AI వీడియో generation, editing టూల్స్.",
  "సౌండ్‌తో high-quality generated clips; cinematic b-roll కి బలమైన ఎంపిక.",
  "Voiceover, ఇతర భాషల్లోకి dubbingలో తన కేటగిరీలో బెస్ట్.",
  "పెద్ద వీడియో లేదా streamని ఆటోమేటిక్‌గా Shorts/TikToksగా మారుస్తుంది.",
  "రోజువారీ పనికి practical ఎడిటర్, free plan బాగానే పనికొస్తుంది; auto-captions కోసం ఇప్పుడు Pro కావాలి.",
  "కెమెరా ముందుకు రావాలని లేనప్పుడు avatar presenters, lip-synced translation."]),
 "best-ai-writing-assistants": ("బెస్ట్ AI writing assistants", "Drafting, editing, rewriting — docs, blog posts, READMEs, emails.", [
  "పెద్ద assistantsలో అత్యంత natural గా అనిపించే రాత; గొప్ప editor కూడా.",
  "అన్ని పనులకూ సరిపోయే all-rounder: drafts, rewrites, variations అన్నీ ఒకే chatలో.",
  "మీ notes, docs ఇప్పటికే Notionలో ఉంటే ఇదే బెస్ట్.",
  "మీరు ఎక్కడ టైప్ చేసినా అక్కడే polish — బ్రౌజర్, ఈమెయిల్, docs.",
  "Google Docs, Gmail లోపల చాలా సౌకర్యంగా ఉంటుంది."]),
 "best-ai-for-research": ("రీసెర్చ్ కోసం బెస్ట్ AI", "Sources వెతకండి, చదవండి, summarize చేయండి — మీరు చెక్ చేయగలిగే citations తో.", [
  "Live వెబ్ నుంచి వేగంగా, sources తో సమాధానాలు; త్వరగా రీసెర్చ్ చేయాలంటే మొదటి ఎంపిక.",
  "మీ సొంత sources అప్‌లోడ్ చేసి, వాటి ఆధారంగానే సమాధానాలు (audio overviews కూడా) పొందండి.",
  "Deep research mode ఒక టాపిక్‌పై పెద్ద, citations ఉన్న రిపోర్ట్‌లు తయారు చేస్తుంది.",
  "Deep Research, దానితో పాటు Google Search integration.",
  "ప్రత్యేకంగా academic papers, literature reviews కోసం తయారైంది.",
  "ఇప్పుడు Xలో జనం ఏం మాట్లాడుకుంటున్నారో తెలుసుకోవడానికి ఉపయోగపడుతుంది."]),
 "best-ai-image-generation": ("Image generation కోసం బెస్ట్ AI", "Thumbnails, concept art, mockups, memes.", [
  "డిఫాల్ట్ లుక్ అన్నిటికంటే బాగుంటుంది; art, moodboards, concept art కి సూపర్.",
  "Detailed instructions పాటించడంలో, మాట్లాడుతూ ఎడిట్ చేయడంలో బెస్ట్.",
  "ఇమేజ్‌లో చదవగలిగే text కావాలంటే ఇది ఎంచుకోండి — logos, posters, thumbnails.",
  "Top-tier quality, లోకల్ వాడకానికి open-weight ఆప్షన్‌లు కూడా.",
  "Commercial పనికి సురక్షితం; Photoshopలో బిల్ట్-ఇన్.",
  "మీ దగ్గర GPU ఉండి, tinkering ఇష్టమైతే ఫ్రీగా, లోకల్‌గా (ComfyUI)."]),
 "best-ai-for-running-local-models": ("AIని లోకల్‌గా రన్ చేయడానికి బెస్ట్ టూల్స్", "మీ సొంత మెషీన్‌లో ప్రైవేట్ AI, రన్ చేయడానికి ఖర్చు లేదు.", [
  "ఒక్క commandతో open models డౌన్‌లోడ్ చేసి రన్ చేయండి; మొదలుపెట్టడానికి అత్యంత సులువైన మార్గం.",
  "బలమైన open-weight models, లోకల్‌గా రన్ చేయొచ్చు లేదా API ద్వారా చౌకగా వాడొచ్చు.",
  "Ollamaలో రన్ అవుతున్న modelకి కనెక్ట్ చేస్తే offline coding agent రెడీ.",
  "Local image models క్లాసిక్ ecosystem."]),
 "best-ai-for-automation-workflows": ("Automation workflows కోసం బెస్ట్ AI", "మీ యాప్‌లను కనెక్ట్ చేసి, మళ్లీ మళ్లీ చేసే స్టెప్స్ AIకి వదిలేయండి — triggers, agents, glue code.", [
  "Builders కోసం టాప్ పిక్: AI agent nodes, అవసరమైతే కోడ్, self-host పూర్తిగా ఫ్రీ.",
  "Complex branching flows కోసం బెస్ట్ visual canvas; ఒక్కో taskకి Zapier కంటే చౌక.",
  "అత్యధిక యాప్ కవరేజ్, అత్యంత సులువైన setup; ఎక్కువ volume ఉంటే వదిలేయండి, ఎందుకంటే ఖర్చు వేగంగా పెరుగుతుంది.",
  "No-codeతో పని కానప్పుడు, దానితో script లేదా webhook handler రాయించుకోండి.",
  "ఒక్కసారి చేసే multi-step వెబ్ పనులకు; నమ్మదగిన scheduled workflows కి ప్రత్యామ్నాయం కాదు."]),
 "best-ai-for-landing-pages": ("Landing pages కోసం బెస్ట్ AI", "ఒక మధ్యాహ్నంలో ఐడియా నుంచి live, బాగా కనిపించే landing page వరకు.", [
  "టాప్ పిక్: prompt తో forms, database ఉన్న పూర్తి పేజీ తయారు చేసి, ఒక్క క్లిక్‌తో publish చేయండి.",
  "Custom logic కంటే design polish, సులువైన hosting ముఖ్యమైతే బెస్ట్; తర్వాత marketers కూడా ఎడిట్ చేయొచ్చు.",
  "Vercelలో deploy చేస్తే అద్భుతమైన React/Tailwind అవుట్‌పుట్; కోడింగ్ మీద కొంచెం పట్టు ఉండాలి.",
  "Lovable కి వేగవంతమైన full-stack ప్రత్యామ్నాయం; ఐడియాను త్వరగా టెస్ట్ చేయడానికి బాగుంటుంది.",
  "ఇప్పటికే codebase ఉంటే builders వదిలేయండి — అక్కడే పేజీ జోడించండి."]),
 "best-ai-for-ui-design": ("UI design కోసం బెస్ట్ AI", "Prompt లేదా sketchని screensగా, తర్వాత మీరు build చేయగలిగేదిగా మార్చండి.", [
  "డిజైనర్లతో పని చేస్తుంటే టాప్ పిక్: standard టూల్, ఇప్పుడు AI, Figma Make బిల్ట్-ఇన్‌గా.",
  "Mockup స్టెప్‌నే దాటేస్తుంది: వెంటనే ship చేయగలిగే పని చేసే UI కోడ్ తయారు చేస్తుంది.",
  "Google నుంచి ఫ్రీ, వేగవంతమైన prompt-to-UI exploration (గతంలో Galileo AI); Figmaకి export చేస్తుంది.",
  "Wireframes చేసే non-designers కి అత్యంత సులువు; pixel-level కంట్రోల్ కావాలంటే వదిలేయండి.",
  "'డిజైన్' నిజానికి క్లిక్ చేయగలిగే, పని చేసే యాప్ కావాల్సినప్పుడు."]),
 "best-ai-voice-tts": ("బెస్ట్ AI voice, text-to-speech", "మైక్ లేకుండా voiceovers, narration, cloned voices, యాప్ speech.", [
  "టాప్ పిక్: అత్యంత natural వాయిస్‌లు, cloning, dubbing. Creators కి డిఫాల్ట్.",
  "API ద్వారా యాప్‌లు, bulk narration కోసం అత్యంత చౌకైన మంచి వాయిస్‌లు; వాయిస్ ఆప్షన్‌లు తక్కువ.",
  "రికార్డింగ్ కూడా ఎడిట్ చేస్తుంటే బెస్ట్ — తప్పుగా పలికిన పదాలను మీ సొంత cloned voice తోనే సరిచేయండి.",
  "మాట్లాడే avatar లేదా lip-synced translation కూడా కావాల్సినప్పుడు."]),
 "best-ai-for-music": ("మ్యూజిక్ కోసం బెస్ట్ AI", "Prompt నుంచి పాటలు, soundtracks, background మ్యూజిక్.", [
  "టాప్ పిక్: vocals తో పూర్తి పాటలు సెకన్లలో; మంచి అవుట్‌పుట్ పొందడానికి అత్యంత సులువైన మార్గం.",
  "నేరుగా Gemini యాప్‌లో vocals ఉన్న పాటలు, MP3గా డౌన్‌లోడ్ చేసుకోవచ్చు; Suno అవుట్‌పుట్ generic గా అనిపిస్తే ట్రై చేయండి.",
  "Instrumental, orchestral scores కి బెస్ట్, DAWలో ఎడిట్ చేయగలిగే MIDI export తో.",
  "Voiceతో పాటు మ్యూజిక్, sound-effect generation కూడా ఉంది, ఇప్పటికే వాడుతుంటే పనికొస్తుంది."]),
 "best-ai-for-seo-content": ("SEO content కోసం బెస్ట్ AI", "Rank అయ్యే పేజీల రీసెర్చ్, outline, రాత — AI చెత్తను publish చేయకుండా.", [
  "అసలు రాత కోసం టాప్ పిక్: అత్యంత natural drafts, మీ సొంత మెటీరియల్‌కి బెస్ట్ editor.",
  "Rank అవుతున్న వాటితో పోల్చి మీ draftకి స్కోర్ ఇస్తుంది; ఉపయోగపడే guardrails, కానీ స్కోర్ కోసమే రాయకండి.",
  "టీమ్స్, agencies కోసం premium content grading; ఒక్కరే నడిపే సైట్‌కి అవసరానికి మించినది.",
  "ఒక టాపిక్‌పై, competitors ఏం కవర్ చేస్తున్నారో దానిపై వేగంగా, sources తో రీసెర్చ్.",
  "Briefs, outlines, meta descriptions కోసం బలమైన all-rounder; topic gaps కోసం deep research."]),
 "best-ai-for-sales-emails": ("Sales emails కోసం బెస్ట్ AI", "మెరుగైన cold, follow-up emails రాయండి — personal గా, చిన్నగా, AI రాసినట్టు స్పష్టంగా తెలియకుండా.", [
  "టాప్ పిక్: prospect context ఇవ్వండి, చిన్నగా, మనిషి రాసినట్టు అనిపించే draft పొందండి. ఎప్పుడూ ఎడిట్ చేయండి.",
  "Drafts, variants కి అంతే బాగుంటుంది; మీ tone సెట్ చేయడానికి custom instructions వాడండి.",
  "నేరుగా Gmail/Outlookలో coaching, scoring; రోజూ cold email పంపుతుంటే విలువైనది.",
  "మొదటి లైన్ రాసే ముందు prospect, కంపెనీ గురించి వేగంగా రీసెర్చ్.",
  "మీరు ఎక్కడ టైప్ చేసినా tone, clarity పై final polish."]),
 "best-ai-for-data-spreadsheets": ("డేటా, spreadsheets కోసం బెస్ట్ AI", "CSVs analyze చేయండి, formulas రాయండి, charts తయారు చేయండి — మామూలు భాషలో అడిగితే చాలు.", [
  "టాప్ పిక్: ఫైల్ అప్‌లోడ్ చేయండి, analysis, charts కోసం ఇది అసలైన Python రన్ చేస్తుంది.",
  "డేటాను వివరించడంలో, formulas రాయడంలో సూపర్; అప్‌లోడ్ చేసిన ఫైల్స్‌పై analysis కూడా రన్ చేయగలదు.",
  "కేవలం data analysis కోసమే తయారైంది, non-coders కి మరింత సులువైన workflow తో.",
  "పని ఇప్పటికే Excelలో ఉంటే బెస్ట్; Microsoft 365 Copilot ప్లాన్ అవసరం.",
  "Google Sheets లోపల సహజమైన ఎంపిక."]),
 "best-ai-for-presentations": ("Presentations కోసం బెస్ట్ AI", "Outline నుంచి బాగుండే slide deck వరకు, త్వరగా.", [
  "టాప్ పిక్: prompt రాయండి లేదా notes పేస్ట్ చేయండి, ఒక్క నిమిషంలో బాగా కనిపించే deck పొందండి; PowerPointకి export అవుతుంది.",
  "ఒకేలా, on-brand గా ఉండి, format చెడిపోని slides కావాలనుకునే టీమ్స్ కి బెస్ట్.",
  "ముందు story, outline రాయించుకోండి, లేదా దానితో slide content, code-based decks తయారు చేయించండి.",
  "Outlines, speaker notes కి బాగుంటుంది, డౌన్‌లోడ్ చేయగలిగే .pptx ఫైల్ కూడా తయారు చేయగలదు.",
  "మీ decks ఇప్పటికే PowerPointలో ఉండి, మీ Microsoft 365 ప్లాన్‌లో Copilot ఉంటే అర్థవంతం."]),
 "best-ai-for-3d-assets": ("3D assets కోసం బెస్ట్ AI", "Text లేదా images నుంచి props, characters, models తయారు చేయండి.", [
  "టాప్ పిక్: textures తో బలమైన text/image-to-3D, game engines కోసం exports.",
  "Auto-rigging తో వేగవంతమైన generation; animate చేయాల్సిన characters కి సూపర్.",
  "Text లేదా image నుంచి detailed 3D, క్లీన్ topology తో; plugins ద్వారా models నేరుగా Blender, Unity లేదా Unrealలోకి వెళ్తాయి.",
  "మొత్తం ప్రాజెక్ట్‌లో ఒకే స్టైల్ ఉండే game assets కి బెస్ట్.",
  "2.5D/sprite గేమ్స్ అయితే 3D పూర్తిగా వదిలేయండి — concept art, textures లోకల్‌గా తయారు చేయండి."]),
 "best-ai-for-meeting-notes": ("మీటింగ్ notes కోసం బెస్ట్ AI", "కాల్స్ రికార్డ్, transcribe, summarize చేయండి, అప్పుడు ఎవరూ notes రాయాల్సిన పని లేదు.", [
  "టాప్ పిక్: మీ కాల్స్‌లో ఆటోమేటిక్‌గా జాయిన్ అవుతుంది, మంచి summaries, search, CRM integrations తో.",
  "బెస్ట్ free tier, live transcription; summaries కొంచెం generic గా ఉంటాయి.",
  "కేవలం notes కాదు, clips షేర్ చేయాలనుకునే sales, customer కాల్స్ కి బెస్ట్.",
  "మీ టీమ్ ఇప్పటికే Notionలో ఉంటే బిల్ట్-ఇన్ meeting notes — వేరే bot అవసరం లేదు.",
  "అసలు bot లేదు: transcript పేస్ట్ చేసి, మరింత పదునైన summaries, action items పొందండి. Automatic recording కావాలంటే వదిలేయండి."]),
 "best-ai-for-chatbots-rag": ("Chatbots, RAG కోసం బెస్ట్ AI", "మీ సొంత docs నుంచి సమాధానం చెప్పే అసిస్టెంట్ తయారు చేయండి — no-code నుంచి custom కోడ్ వరకు.", [
  "మొదలుపెట్టడానికి టాప్ పిక్: మీరు అప్‌లోడ్ చేసిన docs ఆధారంగా Claude Project నిమిషాల్లో టీమ్ అసిస్టెంట్ అవుతుంది. మీ సొంత సైట్‌లో పెట్టాలంటే వదిలేయండి.",
  "మీ ఫైల్స్‌తో ChatGPT Project కూడా ఇదే పని చేస్తుంది. Custom GPTs 2026 డిసెంబర్ 11న ఆగిపోతున్నాయి, కాబట్టి కొత్తది మొదలుపెట్టకండి.",
  "మీ డేటాను సరిగ్గా ingest, retrieve చేయడమే అసలు కష్టమైనప్పుడు బెస్ట్ code framework.",
  "Integrations లో అతిపెద్ద ecosystem; సింపుల్ bots కి అవసరానికి మించిన abstraction.",
  "దానితో తేలికపాటి custom RAG యాప్ రాయించుకోండి, మీ టూల్స్‌తో కనెక్ట్ చేయడానికి MCP వాడండి.",
  "మీ sourcesపై zero-setup Q&A, embed చేయడానికి కాదు, వ్యక్తిగత వాడకానికి."]),
 "best-ai-for-deploy-hosting": ("AIతో తయారైన యాప్‌లకు బెస్ట్ hosting", "మీ AI టూల్స్ ఇప్పుడే తయారు చేసిన యాప్‌ను ఎక్కడ ship చేయాలి. ఇవి AI టూల్స్ కాదు, hosting ప్లాట్‌ఫామ్‌లు — AI సాయంతో build చేసేవాళ్లకు ఎంత బాగా సరిపోతాయో చూసి ఎంచుకున్నాం.", [
  "Next.js/React యాప్‌లకు (v0 నుంచి వచ్చే దేనికైనా) టాప్ పిక్: gitకి push చేయండి, previews తో live URL పొందండి.",
  "Static sites, సింపుల్ యాప్‌లకు సూపర్, ఉదారమైన free tier, బిల్ట్-ఇన్ forms తో.",
  "Backends, databases, background workers కి అత్యంత సులువైన చోటు. కేవలం static sites అయితే వదిలేయండి.",
  "Docker లేదా ఎక్కువ regions కావాలంటే బెస్ట్; setup కొంచెం ఎక్కువ. Fly 2026లో GPUs ఇవ్వడం ఆపేసింది.",
  "ఒకే చోట build, host చేయండి — deploy config ని ఎప్పుడూ ముట్టుకోవద్దనుకుంటే అత్యంత సులువు."]),
 "best-ai-for-chrome-extensions": ("Chrome extensions తయారు చేయడానికి బెస్ట్ AI", "'దీనికో బటన్ ఉంటే బాగుండు' నుంచి పని చేసే browser extension వరకు.", [
  "టాప్ పిక్: manifest, scripts, popup తయారు చేస్తుంది, మీరు reload చేసి టెస్ట్ చేస్తుంటే context లోనే errors సరిచేస్తుంది.",
  "మొత్తం extension ని scaffold చేయడంలో, Manifest V3 permission issues పై మళ్లీ మళ్లీ పని చేయడంలో సూపర్.",
  "చిన్న, ఒకే ఫైల్ extension కి సరిపోతుంది. Manifest V3 వాడుతోందో లేదో చెక్ చేయండి, ఎందుకంటే పాత examples ఎక్కడ చూసినా ఉంటాయి.",
  "ఇది AI టూల్ కాదు, కానీ AI టూల్‌తో బాగా పనిచేస్తుంది: Vite-based, చురుగ్గా maintain అవుతున్న framework, extension boilerplateని తీసేస్తుంది.",
  "మీరే రాయాలనుకుంటే Chrome APIs కోసం మంచి autocomplete."]),
 "best-ai-for-thumbnails-youtube-packaging": ("YouTube thumbnails, packaging కోసం బెస్ట్ AI", "Thumbnails, titles, క్లిక్ తెప్పించే ఆ hook.", [
  "ఇమేజ్‌లోనే బోల్డ్‌గా, చదవగలిగేలా text ఉండే thumbnails కి టాప్ పిక్.",
  "మాట్లాడుతూ ఎడిట్ చేయడానికి (\"ముఖం ఇంకొంచెం ఆశ్చర్యంగా కనిపించేలా చేయి\"), అదే chatలో titles brainstorm చేయడానికి బెస్ట్.",
  "Final thumbnail layout నిజంగా చేసే చోటు: templates, background removal, Magic టూల్స్.",
  "అత్యంత ఆకట్టుకునే backgrounds, scenes; text తర్వాత Canvaలో జోడించండి.",
  "Title, thumbnail-text జతలను brainstorm చేయండి; ఏదైనా ఐడియా clickbait లా ఉంటే నిజాయితీగా చెప్పేస్తుంది."]),
 "best-ai-for-agent-frameworks": ("బెస్ట్ AI agent frameworks", "Tools, memory, multi-step workflows తో మీ సొంత agents తయారు చేయడానికి code frameworks.", [
  "మొదలుపెట్టడానికి టాప్ పిక్: చిన్న API, tools, handoffs, tracing బిల్ట్-ఇన్.",
  "స్పష్టమైన కంట్రోల్ కావాల్సినప్పుడు బెస్ట్: state, retries, human-in-the-loop, productionలో నమ్మకం.",
  "Role-based multi-agent 'crews' prototype చేయడానికి అత్యంత వేగవంతమైన మార్గం; పెద్ద scaleలో కంట్రోల్‌లో ఉంచడం కష్టం.",
  "AutoGen, Semantic Kernel స్థానంలో Microsoft తెచ్చినది: Python లేదా .NETలో agents, graph-based workflows; Azureలో సహజమైన ఎంపిక.",
  "Framework కాదు, కానీ ఏ agentకైనా tools ఇవ్వడానికి standard మార్గం ఇదే. మీ toolsని MCP serversగా build చేయండి."]),
 "best-ai-for-logos-brand": ("Logos, branding కోసం బెస్ట్ AI", "Logo ఐడియాలు, brand marks, మొదటి brand kit, త్వరగా.", [
  "టాప్ పిక్: ఎడిట్, scale చేయగలిగే అసలైన vector (SVG) logos, icons తయారు చేస్తుంది.",
  "చదవగలిగే wordmarks ఉన్న logo concepts కి బెస్ట్; మీరు ఎంచుకున్నదాన్ని ఇంకా vectorize చేయాల్సి ఉంటుంది.",
  "Non-designers కి logo, brand kit రెండూ ఇచ్చే అత్యంత సులువైన all-in-one; ఫలితాలు కొంచెం template లా అనిపించొచ్చు.",
  "Final logo files కంటే brand mood, visual direction ఎక్స్‌ప్లోర్ చేయడానికి సూపర్.",
  "మాట్లాడుతూ ఒక concept పై పని చేయడానికి పనికొస్తుంది. ఏదైనా trademark చేసే ముందు అది నిజంగా ప్రత్యేకమైనదో కాదో చెక్ చేయండి."]),
 "best-ai-for-customer-support": ("Customer support కోసం బెస్ట్ AI", "AI agents, AI రాసిన replies తో కస్టమర్లకు త్వరగా సమాధానం ఇవ్వండి.", [
  "Tickets ఆటోమేటిక్‌గా పరిష్కరించడానికి టాప్ పిక్; Intercom help desk లేకపోయినా పని చేస్తుంది. ధర ఒక్కో resolutionకి, కాబట్టి volume పెరిగితే ఖర్చు పెరుగుతుంది.",
  "ఇప్పటికే Zendesk వాడుతుంటే సహజమైన ఎంపిక; చిన్న టీమ్స్ కి setup, pricing బరువుగా ఉంటాయి.",
  "పెద్ద ప్లాట్‌ఫామ్ కాకుండా AI drafts, answers ఉన్న సింపుల్ inbox కావాలనుకునే చిన్న టీమ్స్ కి బెస్ట్.",
  "ఏ ప్లాట్‌ఫామ్ అవసరం లేదు: ticket, మీ docs పేస్ట్ చేసి, జాగ్రత్తగా, ఫ్రెండ్లీగా ఉండే reply draft పొందండి.",
  "అదే ఐడియా; మీ docs, tone guideని ChatGPT Projectలో పెట్టండి, అప్పుడు ప్రతి draft ఒకే context నుంచి మొదలవుతుంది."]),
 "best-ai-for-scraping": ("Web scraping కోసం బెస్ట్ AI", "వెబ్‌సైట్లను యాప్‌లు, రీసెర్చ్, AI pipelines కోసం క్లీన్ డేటాగా మార్చండి. ప్రతి సైట్ terms, robots.txt ని గౌరవించండి.", [
  "Builders కి టాప్ పిక్: ఒక్క API call తో సైట్ నుంచి క్లీన్ markdown లేదా structured JSON.",
  "రెడీమేడ్ scraper ఇప్పటికే ఉన్నప్పుడు బెస్ట్ (maps, social, e-commerce); scheduling బిల్ట్-ఇన్.",
  "అసలైన logged-in బ్రౌజర్ లేదా క్లిక్‌లు అవసరమైన సైట్ల కోసం; Stagehand తో కలిపి వాడండి.",
  "అసలైన పేజీపై custom scraper రాసి debug చేస్తుంది; ఒక్కసారి లేదా విభిన్నమైన సైట్లకు బెస్ట్.",
  "అదే పని, మీ ఎడిటర్ లోపల — scraper ఇప్పటికే ఉన్న ప్రాజెక్ట్‌లో భాగమైతే బాగుంటుంది."]),
 "best-ai-for-api-testing": ("API testing కోసం బెస్ట్ AI", "Requests రాయండి, tests తయారు చేయండి, ఫెయిల్ అవుతున్న endpoints ని debug చేయండి.", [
  "మీ టీమ్ ఇప్పటికే Postman వాడుతుంటే టాప్ పిక్: Agent Mode మీ collections నుంచి tests రాస్తుంది, పాడైన requests సరిచేస్తుంది, APIs documentation తయారుచేస్తుంది.",
  "మీ API కోడ్ పక్కనే test suites (pytest, Jest వంటివి) తయారు చేసి సరిచేస్తుంది.",
  "OpenAPI spec లేదా ఫెయిల్ అయిన response పేస్ట్ చేసి, మీరు మిస్ అయిన test cases, edge cases పొందండి.",
  "త్వరిత test scripts, mock డేటా కి బాగుంటుంది; ట్రై చేసి చూడటానికి Python రన్ చేయగలదు.",
  "ఇది AI కాదు, కానీ దీని సాధారణ ఫైల్ collections ని AI ఎడిటర్లు సులువుగా చదవగలవు, రాయగలవు. Offline గా, git-native గా ఉండాలంటే ఇది ఎంచుకోండి."]),
 "best-ai-for-notion-docs": ("Notes, docs కోసం బెస్ట్ AI", "AI తో మీ notes, టీమ్ docs రాయండి, సర్దండి, సెర్చ్ చేయండి.", [
  "మీ workspace Notionలో ఉంటే టాప్ పిక్: AI writing, అన్ని పేజీలపై Q&A, meeting notes, అన్నీ ఒకే చోట.",
  "Docs అసలు రాయడానికి, ఎడిట్ చేయడానికి బెస్ట్; Projects రెఫరెన్స్ మెటీరియల్‌ని దగ్గరగా ఉంచుతాయి.",
  "Docs draft చేయడానికి, మళ్లీ structure చేయడానికి versatile; మొదటి outline నుంచి పూర్తి rewrite వరకు.",
  "మీ docs నిజానికి tables, automations ఉన్న చిన్న యాప్‌లైతే ఇది ఎంచుకోండి.",
  "తమంతట తామే సర్దుకునే personal notes; టీమ్ wikis కి వదిలేయండి."]),
}

NEW = {
 "claude-code": "Anthropic terminal coding agent — ఎక్కువగా చర్చలో ఉన్న dev టూల్స్‌లో ఒకటి.",
 "codex": "OpenAI మళ్లీ లాంచ్ చేసిన Codex coding agent (cloud + CLI).",
 "veo": "Google వీడియో model, ఇప్పుడు synced audio కూడా తయారు చేస్తుంది.",
 "manus": "Multi-step పనులతో వైరల్ అయిన autonomous general agent.",
 "lovable": "వేగంగా పెరుగుతున్న prompt-to-app builder.",
 "notebooklm": "Audio Overviews తో research notes ని podcasts గా మార్చేసింది.",
 "kling": "AI వీడియో generation లో బలమైన పోటీదారు.",
 "deepseek": "Pricing ని కుదిపేసిన open-weight reasoning models.",
 "mcp": "ఇప్పుడు చాలా agent టూల్స్ tools access కోసం సపోర్ట్ చేసే open protocol.",
 "windsurf": "Cursor కి నేరుగా పోటీ ఇచ్చే agentic ఎడిటర్.",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['జనవరి', 'ఫిబ్రవరి', 'మార్చి', 'ఏప్రిల్', 'మే', 'జూన్', 'జులై', 'ఆగస్టు', 'సెప్టెంబర్', 'అక్టోబర్', 'నవంబర్', 'డిసెంబర్']
DATE_MD = '{m} {d}'
DATE_MDY = '{m} {d}, {y}'
RELEASES = {
 'replit-cloud-agents-repos': 'Replit Cloud Agents ఇప్పుడు మీ కంపెనీకి ఇప్పటికే ఉన్న GitHub లేదా GitLab repos పై పనిచేస్తాయి. టీమ్‌లో ఎవరైనా ఒక మార్పును వివరిస్తే, agent దాన్ని నడుస్తున్న app లో test చేసి, engineers review కోసం screenshots మరియు video తో pull request తెరుస్తుంది. Pro మరియు Enterprise plans లో.',
 'gpt-6-1-terra-copilot': 'OpenAI యొక్క సరికొత్త model ఇప్పుడు GitHub Copilot లో అందరికీ అందుబాటులో ఉంది, రోజువారీ agentic coding మరియు terminal పనుల కోసం రూపొందించబడింది, GPT-6.1 Sol కంటే తక్కువ ఖర్చుతో. Copilot Pro, Pro+, Max, Business మరియు Enterprise లో, క్రమంగా rollout అవుతోంది.',
 'replit-monitoring-agent': 'Replit Agent ఇప్పుడు published app alerts\u200cను background\u200cలో గమనిస్తుంది, production సమస్యలను పరిశీలించి ఒక fix\u200cను test చేస్తుంది. experimental Auto-republish setting ఆన్ చేయకపోతే fix\u200cను మీరే review చేసి publish చేస్తారు.',
 'cursor-agent-sdk': 'మీ సొంత agent ను ఒక code folder గా నిర్మించండి (prompt, typed tools, skills మరియు MCP connections), evals తో test చేసి, Cursor లేదా మీ సొంత servers లో deploy చేయండి. agents GitHub, GitLab, Bitbucket, Slack, webhook లేదా cron events పై మేల్కొనవచ్చు.',
 'lovable-supabase-create': 'Lovable ఇప్పుడు backend లేని app కోసం Supabase project సృష్టించి దాన్ని కనెక్ట్ చేస్తుంది. organization, region మీరే ఎంచుకుంటారు (region తర్వాత మార్చలేరు), ఆ project బిల్లును Supabase మీ సొంత account\u200cకు వేస్తుంది.',
 'voxtral-3': 'Mistral కొత్త speech-to-text, text-to-speech models, దానితో పాటు ఫోన్, వెబ్\u200cలో real-time voice agents కోసం SDK. Mistral API (EU-hosted ఆప్షన్\u200cతో) ద్వారా లేదా self-hosted.',
 'kling-4': 'Kuaishou కొత్త వీడియో model: ఒకే పాస్\u200cలో 30 సెకన్ల వరకు clips, వేగమైన కదలికలు, కెమెరా మూవ్స్\u200cలో ఎక్కువ స్థిరత్వం, ఒక్కో పనికి 15 వరకు reference assets, 10 keyframes.',
 'muse-spark-open': 'Coding, agent పనుల కోసం Meta open-weight model (816B parameters, 42B active, 1M-token context). Meta దీన్ని రెండు Mac Studios మీద నడుపుతుంది; చాలామందికి hosted APIs సులువైన దారి.',
 'claude-haiku-5-5': 'Anthropic అత్యంత చౌకైన, వేగమైన model, ఎక్కువ వాల్యూమ్ పనుల కోసం: support bots, summaries, coding subagents. Haiku 4.5 కంటే నడపడానికి దాదాపు 75% తక్కువ ఖర్చు అని Anthropic చెబుతోంది.',
 'nano-banana-2-1': 'Google అప్\u200cడేట్ చేసిన image generation, editing model: మెరుగైన edits, పాత్రల్లో ఎక్కువ consistency, ఇమేజ్\u200cలలో స్పష్టమైన టెక్స్ట్. Gemini యాప్, AI Studio, Gemini API, Flow, Stitch లో అందుబాటులో ఉంది.',
 'copilot-dynamic-workflows': 'Multi-agent పనులను code లో నిర్వచించండి (parallel steps, ఒకదాన్నొకటి చెక్ చేసే subagents, మీరు రివ్యూ చేయడానికి checkpoints) — Copilot CLI, Copilot యాప్, Copilot SDK లో. Public preview, అన్ని plans లో.',
 'heygen-video': 'HeyGen మొదటి general-purpose వీడియో model: టెక్స్ట్, ఇమేజ్ లేదా reference media నుంచి 5 నుంచి 15 సెకన్ల clips, డైలాగ్, సౌండ్ కలిసే తయారవుతాయి. HeyGen API ద్వారా అందుబాటులో ఉంది.',
 'gpt-6-1-sol': 'OpenAI DevDay లో వచ్చిన GPT-6 Sol అప్\u200cగ్రేడ్, agentic coding, computer use, ప్రొఫెషనల్ పనులపై ఫోకస్. చాలా తక్కువ ధరకే GPT-6 Astra కు దగ్గరగా ఉంటుందని OpenAI చెబుతోంది.',
 'openai-agents-api-computer-use': 'Agents API ఇప్పుడు computer use తో software ను నడపగలదు, Codex multi-agent ఫీచర్లు, tool search, context compaction ను మీ యాప్\u200cలోకి తెస్తుంది. Infrastructure ను OpenAI నడుపుతుంది.',
 'claude-sonnet-5-5': 'Anthropic వేగమైన, చౌకైన Sonnet; స్పష్టమైన పరిధి ఉన్న రోజువారీ పనులు, bug fixing లో బలమైనది. Sonnet 5 కంటే 30%+ వేగం, అదే $2/$10 per million tokens ధరకు.',
 'lovable-free-chat': 'Lovable తో chat ఇప్పుడు రోజువారీ free పరిమితిలో ఉచితం: features ప్లాన్ చేయండి, మీ యాప్ code, database గురించి అడగండి, లేదా లాంచ్ టెక్స్ట్ డ్రాఫ్ట్ చేయించండి. Build చేయడానికి ఇంకా credits ఖర్చవుతాయి.',
 'cursor-projects': 'ఒక feature లేదా migration లాంటి పెద్ద పనుల కోసం beta: ఒక coordinator agent cloud లో నడుస్తూ, పనిని ప్లాన్ చేసి, చాలా subagents కు పంచి, కాలక్రమేణా shared context ను కాపాడుతుంది.',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — ఏ పనికి ఏ AI టూల్", TAG + " Use case ప్రకారం సర్దిన AI టూల్స్ డైరెక్టరీ.", """
<h1>ఏ పనికి ఏ AI టూల్.</h1><p class="lede">Tool Use Cases అనేది మీరు చేయాలనుకుంటున్న పనిని బట్టి సర్దిన AI టూల్స్ డైరెక్టరీ — vibe coders, builders, AI తో ఏదైనా ship చేసే ప్రతి ఒక్కరి కోసం.</p>
<input type="search" placeholder="Use cases ఫిల్టర్ చేయండి (ఉదా. video, coding, research)…" data-filter=".f" aria-label="Use cases ఫిల్టర్ చేయండి">
<h2>Use cases</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>కొత్త లాంచ్‌లు, ట్రెండింగ్</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">అన్ని కొత్త లాంచ్‌లు →</a></p>"""),
 "use-cases": ("AI టూల్ use cases — Tool Use Cases", "Use case ప్రకారం AI టూల్స్ చూడండి: vibe coding, coding agents, debugging, గేమ్ prototyping, వీడియో, writing, రీసెర్చ్, images ఇంకా ఎన్నో.", """
<h1>Use cases</h1><p class="lede">పని ఎంచుకోండి. ఏ టూల్స్ ట్రై చేయదగ్గవో, ఎందుకో మేం చెబుతాం.</p>
<input type="search" placeholder="Use cases ఫిల్టర్ చేయండి…" data-filter=".f" aria-label="ఫిల్టర్"><div class="grid">{CARDS}</div>"""),
 "tools": ("అన్ని AI టూల్స్ A నుంచి Z — Tool Use Cases", "Tool Use Cases డైరెక్టరీలోని ప్రతి AI టూల్, అది ఏం చేస్తుంది, ఏ use cases కి సరిపోతుంది.", """
<h1>అన్ని టూల్స్</h1><input type="search" placeholder="టూల్స్ ఫిల్టర్ చేయండి…" data-filter=".f" aria-label="టూల్స్ ఫిల్టర్ చేయండి"><div class="grid">{ROWS}</div>"""),
 "new": ("కొత్త, ట్రెండింగ్ AI టూల్స్ — Tool Use Cases", "Builders కోసం గమనించదగ్గ, ట్రెండింగ్ AI టూల్ లాంచ్‌లు: coding agents, వీడియో models, రీసెర్చ్ టూల్స్ ఇంకా ఎన్నో.", """
<h1>కొత్త లాంచ్‌లు, ట్రెండింగ్</h1><p class="lede">గత ఆరు వారాల్లో వచ్చిన, builders కి ముఖ్యమైన AI టూల్ లాంచ్‌లు, పెద్ద అప్‌డేట్‌లు. ప్రతిదానికీ తేదీ, అధికారిక ప్రకటన లింక్, అది సరిపోయే use case ఇచ్చాం.</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Tool Use Cases ని స్పాన్సర్ చేయండి — మీ AI టూల్‌ను ఫీచర్ చేయండి", "టూల్ తయారీదారులు సంబంధిత use-case పేజీల పైన స్పష్టంగా లేబుల్ చేసిన ఫీచర్డ్ స్లాట్‌ను స్పాన్సర్ చేయొచ్చు.", """
<h1>ఒక use case ని స్పాన్సర్ చేయండి</h1><p class="lede">Vibe coders, builders టూల్ ఎంచుకుంటున్న సరిగ్గా ఆ సమయంలోనే వాళ్లను చేరుకోండి.</p>
<h2>ఇది ఎలా పని చేస్తుంది</h2><ul><li>ప్రతి use-case పేజీ పైన ఒక <b>Sponsored / Featured</b> స్లాట్ ఉంటుంది.</li><li>దానిపై ఎప్పుడూ స్పష్టంగా "Sponsored" అని ఉంటుంది, మా editorial ఎంపికల నుంచి వేరుగా ఉంటుంది.</li><li>ఆ use case కి నిజంగా సరిపోయే టూల్స్‌ని మాత్రమే తీసుకుంటాం.</li><li>స్పాన్సర్‌షిప్ వల్ల మా అభిప్రాయాలు, ర్యాంకింగ్‌లు ఎప్పుడూ మారవు.</li></ul>
<h2>ఉదాహరణ</h2>{SPONSOR_CARD}
<div class="cta">ధర, అందుబాటు వివరాల కోసం సంప్రదించండి. <a class="btn" href="{SPONSOR_MAILTO}">స్పాన్సర్ చేయడానికి ఈమెయిల్ చేయండి</a></div>"""),
 "about": ("మా గురించి — Tool Use Cases", "Tool Use Cases అనేది use case ప్రకారం సర్దిన AI టూల్స్‌తో, autonomous గా నడిచే స్వతంత్ర డైరెక్టరీ.", """
<h1>మా గురించి</h1><p class="lede">Tool Use Cases ఒకే ప్రశ్నకు సమాధానం ఇస్తుంది: ఈ పనికి నేను ఏ AI టూల్ వాడాలి?</p>
<p>చాలా AI డైరెక్టరీలు పెద్ద పెద్ద లిస్ట్‌లు మాత్రమే. మేం use case ప్రకారం సర్దుతాం, ప్రతి ఎంపికకు సింపుల్ భాషలో చిన్న అభిప్రాయం ఇస్తాం, అప్పుడు మీరు ఒక్క నిమిషంలో నిర్ణయం తీసుకోవచ్చు.</p>
<p>ఈ సైట్ autonomous గా నడుస్తుంది — ఒక AI operator దీన్ని అప్‌డేట్ చేస్తుంటుంది, దీని బాధ్యత వహించే మనుషులు Lali Publications. మేం నిజమైన, పేరున్న టూల్స్‌ని మాత్రమే లిస్ట్ చేస్తాం, కల్పిత స్కోర్‌లు లేదా యూజర్ సంఖ్యలు publish చేయం.</p>
<p>Tool Use Cases ని Lali Publications ప్రచురిస్తుంది, వాళ్లే <a href="https://agentusecases.ai">agentusecases.ai</a> కూడా నడుపుతారు. మేం లిస్ట్ చేసే ఏ టూల్‌తోనూ మాకు సంబంధం లేదు.</p>
<p>ఇది సైట్ తెలుగు వెర్షన్, <a href="@R/about/index.html" hreflang="en">ఇంగ్లీష్ వెర్షన్‌</a>లో ఉన్న అవే use cases, అవే ఎంపికలు, అవే ర్యాంకింగ్‌లతో.</p>
<p>సవరణలు లేదా సూచనల కోసం: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("సబ్‌స్క్రైబ్ చేసినందుకు ధన్యవాదాలు — Tool Use Cases", "Tool Picks Weekly కి మీ సైన్‌అప్ అందింది.", """
<h1>మీరు లిస్ట్‌లో చేరిపోయారు. ధన్యవాదాలు!</h1><p class="lede">Tool Picks Weekly కి మీ సైన్‌అప్ అందింది. తర్వాతి ఇష్యూ సోమవారం వస్తుంది. ప్రస్తుతానికి న్యూస్‌లెటర్ ఇంగ్లీష్‌లో వస్తుంది.</p>
<p><a class="btn" href="@R/@Pindex.html">Tool Use Cases కి తిరిగి వెళ్లండి</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "AI టూల్ use cases",
 "uc_coll": ("AI టూల్ use cases", "Use case ప్రకారం AI టూల్స్ చూడండి."),
 "tools_crumb": "అన్ని టూల్స్", "tools_coll": ("అన్ని AI టూల్స్ A నుంచి Z", "Tool Use Cases డైరెక్టరీలోని ప్రతి AI టూల్."),
 "new_crumb": "కొత్త లాంచ్‌లు, ట్రెండింగ్", "new_coll": ("కొత్త, ట్రెండింగ్ AI టూల్స్", "Builders కోసం గమనించదగ్గ, ట్రెండింగ్ AI టూల్ లాంచ్‌లు."),
 "sponsor_crumb": "స్పాన్సర్",
 "about_crumb": "మా గురించి", "about_coll": ("Tool Use Cases గురించి", "Use case ప్రకారం సర్దిన AI టూల్స్‌తో autonomous గా నడిచే స్వతంత్ర డైరెక్టరీ, Lali Publications ప్రచురణ."),
}
