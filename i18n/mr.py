"""Marathi (mr) locale for Tool Use Cases.
Style: natural, conversational Marathi the way Marathi tech creators write. Product names and common
tech terms (vibe coding, AI agent, deploy, debugging, RAG, API, prompt...) stay in Latin script.
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "mr"
PREFIX = "mr/"
SHORT = "MR"
NATIVE = "मराठी"
ENGLISH_NAME = "Marathi"
INDIA = True
OG_LOCALE = "mr_IN"
RSS_LANG = "mr"

TAG = "कोणत्या कामासाठी कोणतं AI टूल — vibe coders आणि builders साठी."

UI = {
 "nav_use_cases": "Use cases", "nav_tools": "टूल्स", "nav_new": "नवीन लाँच",
 "nav_newsletter": "न्यूजलेटर", "nav_sponsor": "स्पॉन्सर", "nav_about": "आमच्याबद्दल",
 "home": "होम", "use_cases": "Use cases",
 "og_alt": "Tool Use Cases: तुमच्या कामानुसार रँक केलेली AI टूल्स",
 "footer": "Tool Use Cases · Lali Publications कडून ·",
 "nl_h2": "Vibe coders साठी दर आठवड्याला निवडक AI टूल्स",
 "nl_p": "नवीन टूल्स + कोणतं टूल कोणत्या कामाचं. पूर्णपणे फ्री. सध्या न्यूजलेटर इंग्रजीत पाठवलं जातं.",
 "nl_placeholder": "tumhi@example.com", "nl_aria": "ईमेल पत्ता", "nl_button": "सबस्क्राइब करा",
 "nl_subject": "Tool Use Cases newsletter signup (mr)",
 "nl_small": "ईमेल Lali Publications कडून येईल. Spam नाही, कधीही unsubscribe करा.",
 "nl_latest": "लेटेस्ट अंक वाचा: {LINK} (इंग्रजीत).",
 "verdict": "आमचं मत:", "our_picks": "आमची निवड", "related": "संबंधित use cases",
 "browse_all": "सगळे use cases पाहा →",
 "disclaimer": "ही निवड आमची स्वतःची आहे, त्यासाठी कोणीही पैसे दिलेले नाहीत. किंमती आणि फीचर्स वारंवार बदलतात — प्रत्येक टूलची ऑफिशियल साइट नक्की तपासा.",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} {names} आणि इतर टूल्सबद्दल आमचं मत.",
 "review_name": "{tool} — {title}",
 "sponsored": "Sponsored", "sponsor_h3": "तुमचं टूल इथे",
 "sponsor_p": "हा फीचर्ड स्लॉट अशा टूल बनवणाऱ्यांसाठी आहे ज्यांचं टूल या use case मध्ये खरंच फिट बसतं. नेहमी स्पष्टपणे लेबल केलेला असतो आणि आमच्या निवडीपासून कायम वेगळा ठेवला जातो.",
 "sponsor_link": "स्पॉन्सर करण्यासाठी ईमेल करा",
 "new_badge": "लक्षवेधी / ट्रेंडिंग",
 "last_updated": 'शेवटचं अपडेट: {date}', "earlier_h2": 'आधीचे लाँच', "earlier_p": 'या अपडेटआधी आम्ही दाखवलेले लाँच. आता ते नवीन नाहीत, पण माहीत असायला हवेत.', "fits": 'Use case:', "source": 'स्रोत',
 "rss_title": "Tool Use Cases (मराठी)",
 "rss_desc": "Tool Picks Weekly चे अंक (इंग्रजीत) आणि लक्ष देण्यासारखे नवीन AI टूल लाँच.",
 "rss_new_prefix": "नवीन आणि ट्रेंडिंग: ", "rss_issue_suffix": " (इंग्रजीत)",
 "rss_cat_newsletter": "न्यूजलेटर", "rss_cat_new": "नवीन लाँच",
 "llms_h2": "मराठीत (mr)",
 "llms_intro": "संपूर्ण साइट मराठीत, इंग्रजी व्हर्जनसारखेच use cases, तीच निवड आणि तेच रँकिंग.",
 "llms_other": [("होम", ""), ("सगळी AI टूल्स A ते Z", "tools/"), ("नवीन लाँच आणि ट्रेंडिंग", "new/"), ("आमच्याबद्दल", "about/"), ("स्पॉन्सर", "sponsor/")],
}

TOOLS = {
 "cursor": "AI-first कोड एडिटर (VS Code चा fork), ज्यात chat, inline edits आणि agent mode आहे.",
 "claude": "Anthropic चा AI असिस्टंट, मोठी डॉक्युमेंट्स, लेखन आणि कोडमध्ये जबरदस्त.",
 "claude-code": "Anthropic चं terminal मध्ये चालणारं agentic coding टूल.",
 "chatgpt": "OpenAI चा सगळ्या कामांसाठीचा AI असिस्टंट, chat, images, voice आणि search सह.",
 "codex": "OpenAI चा coding agent, जो cloud मध्ये किंवा CLI मधून तुमच्या repos वर काम करतो.",
 "copilot": "AI pair programmer, VS Code, JetBrains आणि GitHub मध्ये बिल्ट-इन.",
 "v0": "Vercel चा AI app/UI builder, जो prompts वरून React + Tailwind ॲप्स बनवतो.",
 "lovable": "Prompt वरून full-stack वेब ॲप बनवणारा builder, Supabase integration सह.",
 "replit": "ब्राउझरमधला IDE, ज्याचा agent एका prompt वरून ॲप बनवून deploy सुद्धा करतो.",
 "bolt": "StackBlitz चा ब्राउझरमध्ये चालणारा prompt-to-app builder.",
 "windsurf": "Cognition चा AI कोड एडिटर (पूर्वीचं Windsurf): पूर्ण IDE आणि local व cloud coding agents चालवण्यासाठी command center.",
 "opencode": "Terminal, desktop किंवा IDE साठी open-source (MIT) coding agent, जो local models सह 75+ model providers सोबत चालतो.",
 "devin": "Cognition चा autonomous software engineering agent.",
 "gemini": "Google चा AI असिस्टंट, खूप मोठ्या context windows आणि Google integration सह.",
 "perplexity": "AI answer engine, जो वेबवर सर्च करतो आणि sources पण दाखवतो.",
 "notebooklm": "Google ची research notebook (पूर्वीचं NotebookLM), जी तुम्ही अपलोड केलेल्या sources वरूनच उत्तरं देते.",
 "elicit": "Academic papers शोधण्यासाठी आणि त्यांचा सारांश काढण्यासाठी AI research असिस्टंट.",
 "notion-ai": "Notion workspaces मध्येच बिल्ट-इन AI writing आणि Q&A.",
 "grammarly": "तुम्ही जिथे टाइप कराल तिथे grammar, tone आणि rewrites मध्ये मदत करणारा writing असिस्टंट.",
 "midjourney": "Image generator, जो दमदार aesthetic आणि artistic आउटपुटसाठी ओळखला जातो.",
 "dalle": "ChatGPT मधली OpenAI ची image generation, instructions पाळण्यात आणि इमेजमध्ये text टाकण्यात चांगली.",
 "ideogram": "Image generator, जो इमेजमध्ये स्पष्ट वाचता येणारा text टाकण्यात खास चांगला आहे.",
 "flux": "High-quality image models ची फॅमिली, त्यातले काही open weights सह येतात.",
 "firefly": "Adobe ची generative image टूल्स, commercial वापरासाठी सुरक्षित राहतील अशा पद्धतीने train केलेली.",
 "sd": "Open image models ची फॅमिली, जी तुम्ही लोकली चालवू शकता (उदा. ComfyUI वापरून).",
 "runway": "AI व्हिडिओ generation आणि editing suite (Gen-series models).",
 "elevenlabs": "अगदी खऱ्यासारखा AI voiceover, voice cloning आणि dubbing.",
 "descript": "Transcript एडिट करून व्हिडिओ आणि podcasts एडिट करा.",
 "heygen": "AI avatar व्हिडिओ आणि व्हिडिओ translation.",
 "capcut": "Free plan असलेला व्हिडिओ एडिटर; auto-captions आणि बहुतेक AI tools साठी Pro लागतो.",
 "opus": "मोठे व्हिडिओ आपोआप छोट्या vertical clips मध्ये बदलतो.",
 "veo": "Google DeepMind चं text-to-video model, native audio सह.",
 "rosebud": "Prompts वरून गेम्स बनवण्याचं ब्राउझर टूल (Three.js/Phaser).",
 "scenario": "तुमच्या स्वतःच्या training sets वरून एकसारख्या स्टाइलचे game art assets बनवतं.",
 "meshy": "Game assets साठी text/image वरून 3D model generation.",
 "suno": "पूर्ण गाणी बनवतं, गेम/व्हिडिओसाठी placeholder म्युझिक म्हणून कामाचं.",
 "sentry": "Error monitoring, AI root-cause analysis आणि fix च्या सूचनांसह.",
 "deepseek": "चीनमधली AI लॅब, जिचे open-weight reasoning models दमदार आणि स्वस्त आहेत.",
 "ollama": "Open models (Llama, Qwen वगैरे) एका command ने लोकली चालवा.",
 "manus": "General-purpose autonomous agent, जो वेब ब्राउझ करून अनेक स्टेप्सची कामं पूर्ण करतो.",
 "kling": "Kuaishou चा text/image-to-video generator.",
 "grok": "xAI चा असिस्टंट, X आणि वेबवर real-time search सह.",
 "mcp": "AI agents ना टूल्स आणि डेटाशी जोडण्याचं open standard.",
 "n8n": "Open-source workflow automation, AI agent nodes सह; फ्रीमध्ये self-host करा किंवा त्यांचं cloud वापरा.",
 "make": "Visual no-code automation builder, हजारो ॲप्समध्ये अनेक स्टेप्सच्या scenarios साठी.",
 "zapier": "सगळ्यात जास्त ॲप्सशी जोडलेलं no-code automation प्लॅटफॉर्म, आता AI steps आणि agents सह.",
 "framer": "डिझायनर्ससाठी वेबसाइट builder, AI page generation, CMS आणि hosting सह.",
 "stitch": "Google चं prompt-to-UI डिझाइन टूल (आधीचं Galileo AI), जे Figma आणि कोडमध्ये export करतं.",
 "uizard": "नवशिक्यांसाठी सोपं AI UI mockup टूल; prompts आणि sketches ना ॲप स्क्रीनमध्ये बदलतं.",
 "figma": "UI डिझाइनचं standard टूल, बिल्ट-इन AI फीचर्स आणि prompt-to-prototype साठी Figma Make सह.",
 "openai-tts": "OpenAI ची speech API: स्वस्त, natural आवाज, जे instructions देऊन कंट्रोल करता येतात.",
 "lyria": "Gemini ॲपमधलं Google चं music model: vocals किंवा instrumental असलेली साधारण 3 मिनिटांपर्यंतची गाणी, MP3 मध्ये डाउनलोड करता येतात.",
 "aiva": "Instrumental, orchestral आणि soundtrack म्युझिकसाठी AI composer, MIDI export सह.",
 "surfer": "SEO आणि AI search visibility टूल (पूर्वीचं SurferSEO); त्याचा content editor तुमचा draft top-ranking पेजेसशी तुलना करून स्कोअर देतो.",
 "clearscope": "Keyword coverage आणि content grading साठी premium content-optimization टूल.",
 "lavender": "Sales email coach, जो तुमच्या inbox मध्येच cold emails ना स्कोर देतो आणि पुन्हा लिहितो.",
 "julius": "Spreadsheets आणि डेटा फाइल्सशी chat करून analysis आणि charts मिळवा.",
 "excel-copilot": "Excel मधला Copilot, तुमच्या workbooks वर formulas, analysis आणि charts साठी.",
 "powerpoint-copilot": "PowerPoint मधला Copilot: prompt किंवा फाइलवरून deck चा draft बनवतो, slides जोडतो आणि content पुन्हा लिहितो किंवा नव्याने मांडतो.",
 "gamma": "Prompt किंवा outline वरून presentations, docs आणि वेब पेजेस बनवतं.",
 "beautiful-ai": "Smart templates असलेलं slide सॉफ्टवेअर, content जोडताच आपोआप format होतं.",
 "rodin": "Text किंवा image पासून 3D बनवणारा generator; स्वच्छ topology, PBR materials आणि Blender, Unity, Unreal साठी plugins सह.",
 "tripo": "वेगवान text/image-to-3D generator, auto-rigging आणि clean topology च्या पर्यायांसह.",
 "fireflies": "AI meeting bot, जो Zoom/Meet/Teams कॉल्स रेकॉर्ड, transcribe आणि summarize करतो.",
 "otter": "Real-time मीटिंग transcription आणि AI summaries, कामाला येईल असा free tier सह.",
 "grain": "Clips आणि highlights भोवती बनलेला meeting recorder, sales आणि customer टीम्समध्ये लोकप्रिय.",
 "langchain": "LLM ॲप्स बनवण्यासाठी open-source framework: RAG, tools आणि integrations.",
 "llamaindex": "Open-source framework, ज्याचा फोकस LLMs ना तुमच्या documents आणि डेटाशी जोडण्यावर (RAG) आहे.",
 "vercel": "Frontend आणि Next.js hosting, git-push deploys, previews आणि AI SDK सह.",
 "netlify": "Static sites आणि वेब ॲप्ससाठी git-based hosting, functions आणि forms सह.",
 "railway": "जवळपास कोणत्याही config शिवाय repo मधून backends, databases आणि workers deploy करा.",
 "fly": "Docker containers जगभरात users च्या जवळ चालवा; full-stack ॲप्ससाठी चांगलं (2026 पासून GPU machines बंद).",
 "wxt": "TypeScript मध्ये cross-browser extensions बनवण्यासाठी Vite-based open-source framework.",
 "canva": "ऑनलाइन डिझाइन टूल, Magic Studio AI फीचर्स आणि रेडीमेड templates सह.",
 "langgraph": "LangChain चं framework, stateful आणि कंट्रोलमध्ये राहणाऱ्या multi-step agent graphs साठी.",
 "crewai": "Role-based AI agents च्या टीम्ससाठी open-source Python framework.",
 "ms-agent-framework": "Python आणि .NET साठी Microsoft चं open-source agent framework, AutoGen आणि Semantic Kernel चा उत्तराधिकारी.",
 "openai-agents": "OpenAI चं हलकं SDK, agents साठी tools, handoffs, guardrails आणि tracing सह.",
 "recraft": "डिझायनर्ससाठी AI image generator, जो editable vector (SVG) graphics आणि icons देतो.",
 "looka": "AI logo maker, जो one-time fee मध्ये logo सोबत brand kit पण बनवतो.",
 "intercom-fin": "Intercom चा AI support agent, जो तुमच्या help content वरून ग्राहकांचे प्रश्न सोडवतो.",
 "zendesk": "Zendesk help desk मध्ये बिल्ट-इन AI agents आणि agent-assist फीचर्स.",
 "helpscout": "सोपा shared inbox आणि help desk, AI drafts, summaries आणि AI Answers सह.",
 "firecrawl": "API जी वेबसाइट्स crawl करून LLMs साठी स्वच्छ markdown किंवा structured डेटा परत देते.",
 "browserbase": "AI agents साठी hosted headless browsers, सोबत open-source Stagehand framework.",
 "apify": "Scraping प्लॅटफॉर्म, हजारो रेडीमेड scrapers ('Actors') आणि scheduling सह.",
 "postman": "Requests बनवण्याचा आणि टेस्ट करण्याचा API प्लॅटफॉर्म, तुमच्या सगळ्या collections वर AI ने काम करणाऱ्या Agent Mode सह.",
 "bruno": "Open-source, offline API client, जो collections git मध्ये साध्या फाइल्सच्या रूपात ठेवतो.",
 "coda": "Doc आणि spreadsheet एकत्र करणारं workspace (पूर्वीचं Coda), tables, automations आणि बिल्ट-इन AI सह.",
 "mem": "AI notes ॲप, जे नोट्स आपोआप व्यवस्थित लावतं आणि त्यांच्याशी chat करू देतं.",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Vibe coding साठी बेस्ट AI", "सांगा, चालवा, सुधारा. अशी टूल्स ज्यांनी तुम्ही बहुतेक बोलूनच सॉफ्टवेअर बनवता.", [
  "डिफॉल्ट निवड: खरा codebase आणि एडिटर तुमच्याकडेच राहतो, पण बहुतेक टायपिंग AI करतं.",
  "आयडियापासून auth आणि database असलेल्या चालू वेब ॲपपर्यंत पोहोचण्याचा सगळ्यात वेगवान मार्ग, कोणत्याही setup शिवाय.",
  "पटकन polished React/Next.js UI हवं असेल आणि Vercel वर deploy करायचं असेल तर बेस्ट.",
  "Hosting सकट सगळं ब्राउझरमध्ये — पटकन बनणाऱ्या आणि शेअर करता येणाऱ्या prototypes साठी चांगलं.",
  "Lovable सारखंच; एकाच टॅबमध्ये full-stack demo उभा करायला उत्तम.",
  "Cursor चा पर्याय, एकाच वेळी अनेक agents चालवण्यासाठी बनवलेला; Cursor जमत नसेल तर एकदा नक्की वापरून पाहा."]),
 "best-ai-coding-agents": ("बेस्ट AI coding agents", "असे agents जे टास्क घेतात, अनेक फाइल्स एडिट करतात, commands चालवतात आणि diff घेऊन परत येतात.", [
  "Terminal मधून multi-file बदलांमध्ये कमाल; मोठ्या agentic कामांसाठी अनेकांचा फेव्हरिट.",
  "पूर्ण एडिटरमध्येच agent mode, त्यामुळे प्रत्येक बदल डोळ्यांनी पाहून रिव्ह्यू करता येतो.",
  "टास्क cloud मध्ये parallel चालवायला सोपवा आणि मग तयार झालेले PRs रिव्ह्यू करा.",
  "Copilot चा coding agent GitHub issues वरून काम करतो — तुमची टीम GitHub वरच असेल तर अगदी योग्य.",
  "पूर्ण tickets सुरुवातीपासून शेवटपर्यंत सोपवण्यासाठी बनवलेला; महाग, टीम्ससाठी.",
  "फ्री, open-source आणि सतत develop होणारा; हवं ते model वापरा, local सुद्धा, किंवा तुमचा सध्याचा Claude, ChatGPT किंवा Copilot plan."]),
 "best-ai-for-fixing-broken-code": ("बिघडलेला कोड आणि errors दुरुस्त करण्यासाठी बेस्ट AI", "Stack trace पेस्ट करा, fix मिळवा. अशी टूल्स जी फक्त कोड बनवण्यात नाही, तर debugging मध्येही चांगली आहेत.", [
  "Error सोबत संबंधित फाइल्स पेस्ट करा; खऱ्या root cause पर्यंत विचार करून पोहोचण्यात खूप मजबूत.",
  "पूर्ण प्रोजेक्टचा context घेऊन तिथेच fix करतो — इकडून तिकडे copy-paste नाही.",
  "चांगला general debugger, आणि issues reproduce करण्यासाठी Python पण चालवू शकतो.",
  "'Fix' आणि '/explain' थेट एडिटरमध्ये, नेमकं जिथे लाल रेघ दिसते तिथे.",
  "Production मधले errors पकडतो आणि खऱ्या traces वरून fix सुचवतो.",
  "त्याला tests चालवू द्या, failure वाचू द्या, आणि सगळं green होईपर्यंत पुन्हा पुन्हा प्रयत्न करू द्या."]),
 "best-ai-for-game-prototyping": ("गेम prototyping साठी बेस्ट AI", "खेळता येईल अशी आयडिया पटकन स्क्रीनवर आणा — कोड, art, 3D आणि म्युझिक.", [
  "एका prompt ने ब्राउझर गेम बनवा आणि इतरांचे गेम्स remix करा.",
  "खऱ्या engines साठी (Godot, Unity, Phaser): scripts AI लिहितं, play-test तुम्ही करता.",
  "Game art तुमच्या स्वतःच्या स्टाइलमध्ये एकसारखं ठेवतं — गेम्समध्ये AI art चा सगळ्यात कठीण भाग हाच.",
  "Levels चा blockout करण्यासाठी पटकन 3D props आणि characters.",
  "काही मिनिटांत placeholder (किंवा final) soundtrack.",
  "Recording booth शिवाय character voice lines आणि sound effects."]),
 "best-ai-for-video-youtube": ("व्हिडिओ आणि YouTube साठी बेस्ट AI", "Footage बनवा, पटापट एडिट करा, voice द्या आणि Shorts कापा.", [
  "Talking-head व्हिडिओ doc सारखे एडिट करा; filler words काढून टाकतो. YouTubers चा भरपूर वेळ वाचवतो.",
  "B-roll आणि effects साठी pro-level AI व्हिडिओ generation आणि editing टूल्स.",
  "आवाजासह high-quality generated clips; cinematic b-roll साठी दमदार.",
  "Voiceover आणि इतर भाषांमध्ये dubbing मध्ये आपल्या कॅटेगरीत सगळ्यात बेस्ट.",
  "मोठा व्हिडिओ किंवा stream आपोआप Shorts/TikToks मध्ये बदलतो.",
  "रोजच्या कामासाठी practical एडिटर, ज्याचा free plan उपयोगी आहे; auto-captions साठी आता Pro लागतो.",
  "कॅमेऱ्यासमोर यायचं नसेल तेव्हा avatar presenters आणि lip-synced translation."]),
 "best-ai-writing-assistants": ("बेस्ट AI writing assistants", "Drafting, editing आणि rewriting — docs, blog posts, READMEs, emails.", [
  "मोठ्या assistants मध्ये सगळ्यात natural वाटणारं लेखन; उत्तम editor पण.",
  "सगळ्या कामांसाठी चालणारा all-rounder: drafts, rewrites आणि variations एकाच chat मध्ये.",
  "तुमच्या notes आणि docs आधीच Notion मध्ये असतील तर बेस्ट.",
  "तुम्ही जिथे टाइप कराल तिथे polish — ब्राउझर, ईमेल, docs.",
  "Google Docs आणि Gmail मध्ये खूप सोयीचं."]),
 "best-ai-for-research": ("रिसर्चसाठी बेस्ट AI", "Sources शोधा, वाचा आणि summarize करा — तपासता येतील अशा citations सह.", [
  "Live वेबवरून पटकन, sources सह उत्तरं; झटपट रिसर्चसाठी पहिली पसंती.",
  "तुमचे स्वतःचे sources अपलोड करा आणि त्यांवर आधारित उत्तरं (आणि audio overviews) मिळवा.",
  "Deep research mode एखाद्या टॉपिकवर मोठे, citations असलेले रिपोर्ट्स बनवतो.",
  "Deep Research सोबत Google Search integration.",
  "खास academic papers आणि literature reviews साठी बनवलेलं.",
  "X वर आत्ता लोक काय बोलतायत हे जाणून घेण्यासाठी उपयोगी."]),
 "best-ai-image-generation": ("Image generation साठी बेस्ट AI", "Thumbnails, concept art, mockups, memes.", [
  "डिफॉल्ट लुक सगळ्यात छान; art, moodboards आणि concept art साठी उत्तम.",
  "Detailed instructions पाळण्यात आणि बोलून एडिट करण्यात सगळ्यात चांगलं.",
  "इमेजमध्ये वाचता येईल असा text हवा असेल तेव्हा हे निवडा — logos, posters, thumbnails.",
  "Top-tier quality, आणि लोकल वापरासाठी open-weight पर्याय पण.",
  "Commercial कामासाठी जास्त सुरक्षित; Photoshop मध्ये बिल्ट-इन.",
  "तुमच्याकडे GPU असेल आणि tinkering आवडत असेल तर फ्री आणि लोकल (ComfyUI)."]),
 "best-ai-for-running-local-models": ("AI लोकली चालवण्यासाठी बेस्ट टूल्स", "तुमच्या स्वतःच्या मशीनवर प्रायव्हेट AI, चालवायला काही खर्च नाही.", [
  "एका command ने open models डाउनलोड करून चालवा; सुरुवात करण्याचा सगळ्यात सोपा मार्ग.",
  "दमदार open-weight models, लोकली चालवा किंवा API ने स्वस्तात वापरा.",
  "Ollama मध्ये चालणाऱ्या model ला जोडा आणि offline coding agent मिळवा.",
  "Local image models ची क्लासिक ecosystem."]),
 "best-ai-for-automation-workflows": ("Automation workflows साठी बेस्ट AI", "तुमची ॲप्स जोडा आणि पुन्हा पुन्हा होणाऱ्या स्टेप्स AI ला सांभाळू द्या — triggers, agents आणि glue code.", [
  "Builders साठी टॉप पिक: AI agent nodes, गरज पडल्यास कोड, आणि self-host पूर्णपणे फ्री.",
  "Complex branching flows साठी सगळ्यात चांगला visual canvas; प्रत्येक task मागे Zapier पेक्षा स्वस्त.",
  "सगळ्यात जास्त ॲप्स आणि सगळ्यात सोपं setup; volume जास्त असेल तर टाळा, कारण खर्च पटकन वाढतो.",
  "No-code ने काम होत नसेल तेव्हा त्याच्याकडून script किंवा webhook handler लिहून घ्या.",
  "एकदाच करायच्या multi-step वेब कामांसाठी; भरवशाच्या scheduled workflows ची जागा घेऊ शकत नाही."]),
 "best-ai-for-landing-pages": ("Landing pages साठी बेस्ट AI", "एका दुपारीत आयडियापासून live आणि नीटनेटक्या landing page पर्यंत.", [
  "टॉप पिक: prompt वरून forms आणि database असलेलं पूर्ण पेज बनवा, मग एका क्लिकमध्ये publish करा.",
  "Custom logic पेक्षा design polish आणि सोपं hosting महत्त्वाचं असेल तर बेस्ट; नंतर marketers पण एडिट करू शकतात.",
  "Vercel वर deploy करत असाल तर उत्तम React/Tailwind आउटपुट; थोडी कोडिंगची सवय हवी.",
  "Lovable चा वेगवान full-stack पर्याय; एखादी आयडिया पटकन टेस्ट करायला चांगला.",
  "Codebase आधीच असेल तर builders सोडा — तिथेच पेज जोडा."]),
 "best-ai-for-ui-design": ("UI design साठी बेस्ट AI", "Prompt किंवा sketch चं screens मध्ये, आणि मग बनवता येईल अशा गोष्टीत रूपांतर करा.", [
  "डिझायनर्ससोबत काम करत असाल तर टॉप पिक: standard टूल, आता AI आणि Figma Make बिल्ट-इन.",
  "Mockup ची स्टेपच वगळतो: लगेच ship करता येईल असा चालू UI कोड बनवतो.",
  "Google चं फ्री आणि वेगवान prompt-to-UI exploration (आधीचं Galileo AI); Figma मध्ये export करतं.",
  "Wireframes बनवणाऱ्या non-designers साठी सगळ्यात सोपं; pixel-level कंट्रोल हवा असेल तर टाळा.",
  "जेव्हा 'डिझाइन' म्हणजे खरंतर क्लिक करता येणारं, चालू ॲप असायला हवं."]),
 "best-ai-voice-tts": ("बेस्ट AI voice आणि text-to-speech", "माइकशिवाय voiceovers, narration, cloned voices आणि ॲप speech.", [
  "टॉप पिक: सगळ्यात natural आवाज, cloning आणि dubbing. Creators साठी डिफॉल्ट.",
  "API ने ॲप्स आणि bulk narration साठी सगळ्यात स्वस्त चांगले आवाज; आवाजांचे पर्याय कमी.",
  "रेकॉर्डिंग पण एडिट करत असाल तेव्हा बेस्ट — चुकलेले शब्द तुमच्याच cloned voice ने दुरुस्त करा.",
  "जेव्हा बोलणारा avatar किंवा lip-synced translation पण हवं असेल."]),
 "best-ai-for-music": ("म्युझिकसाठी बेस्ट AI", "Prompt वरून गाणी, soundtracks आणि background म्युझिक.", [
  "टॉप पिक: vocals सह पूर्ण गाणी काही सेकंदांत; चांगलं काहीतरी मिळवण्याचा सगळ्यात सोपा मार्ग.",
  "थेट Gemini ॲपमध्ये vocals असलेली गाणी, MP3 मध्ये डाउनलोड करता येतात; Suno चं आउटपुट generic वाटलं तर वापरून पाहा.",
  "Instrumental आणि orchestral scores साठी बेस्ट, DAW मध्ये एडिट करता येईल अशा MIDI export सह.",
  "Voice सोबत म्युझिक आणि sound-effect generation पण आहे, आधीच वापरत असाल तर सोयीचं."]),
 "best-ai-for-seo-content": ("SEO content साठी बेस्ट AI", "Rank होऊ शकतील अशा पेजेसचा रिसर्च, outline आणि लेखन — AI चा कचरा publish न करता.", [
  "प्रत्यक्ष लेखनासाठी टॉप पिक: सगळ्यात natural drafts आणि तुमच्या स्वतःच्या मटेरियलचा सगळ्यात चांगला editor.",
  "जे rank होतंय त्याच्याशी तुलना करून तुमच्या draft ला स्कोर देतो; उपयोगी guardrails, पण फक्त स्कोरसाठी लिहू नका.",
  "टीम्स आणि agencies साठी premium content grading; एकट्याच्या साइटसाठी गरजेपेक्षा जास्त.",
  "एखाद्या टॉपिकवर आणि competitors काय कव्हर करतात यावर पटकन, sources सह रिसर्च.",
  "Briefs, outlines आणि meta descriptions साठी भक्कम all-rounder; topic gaps साठी deep research."]),
 "best-ai-for-sales-emails": ("Sales emails साठी बेस्ट AI", "चांगले cold आणि follow-up emails लिहा — personal, छोटे, आणि उघडपणे AI सारखे न वाटणारे.", [
  "टॉप पिक: prospect चा context द्या आणि छोटा, माणसासारखा वाटणारा draft मिळवा. नेहमी एडिट करा.",
  "Drafts आणि variants साठी तितकाच चांगला; तुमचा tone सेट करण्यासाठी custom instructions वापरा.",
  "थेट Gmail/Outlook मध्ये coaching आणि scoring; रोज cold email पाठवत असाल तर फायदेशीर.",
  "पहिली ओळ लिहिण्याआधी prospect आणि कंपनीचा पटकन रिसर्च.",
  "तुम्ही जिथे टाइप कराल तिथे tone आणि clarity वर final polish."]),
 "best-ai-for-data-spreadsheets": ("डेटा आणि spreadsheets साठी बेस्ट AI", "CSVs analyze करा, formulas लिहा आणि charts बनवा — फक्त साध्या भाषेत विचारून.", [
  "टॉप पिक: फाइल अपलोड करा, analysis आणि charts साठी हे खरं Python चालवतं.",
  "डेटा समजावून सांगण्यात आणि formulas लिहिण्यात उत्तम; अपलोड केलेल्या फाइल्सवर analysis पण चालवू शकतो.",
  "फक्त data analysis साठी बनवलेलं, non-coders साठी जास्त सोप्या workflow सह.",
  "काम आधीच Excel मध्ये असेल तर बेस्ट; Microsoft 365 Copilot प्लॅन लागतो.",
  "Google Sheets मध्ये सगळ्यात स्वाभाविक निवड."]),
 "best-ai-for-presentations": ("Presentations साठी बेस्ट AI", "Outline पासून बऱ्यापैकी slide deck पर्यंत, पटकन.", [
  "टॉप पिक: prompt लिहा किंवा notes पेस्ट करा आणि एका मिनिटात छान दिसणारा deck मिळवा; PowerPoint मध्ये export होतो.",
  "एकसारख्या, on-brand slides हव्या असणाऱ्या आणि ज्यांचा format टिकून राहावा अशा टीम्ससाठी बेस्ट.",
  "आधी story आणि outline लिहून घ्या, किंवा त्याच्याकडून slide content आणि code-based decks बनवून घ्या.",
  "Outlines आणि speaker notes साठी चांगला, आणि डाउनलोड करता येईल अशी .pptx फाइल पण बनवू शकतो.",
  "तुमचे decks आधीच PowerPoint मध्ये असतील आणि तुमच्या Microsoft 365 प्लॅनमध्ये Copilot असेल तर योग्य."]),
 "best-ai-for-3d-assets": ("3D assets साठी बेस्ट AI", "Text किंवा images वरून props, characters आणि models बनवा.", [
  "टॉप पिक: textures सह भक्कम text/image-to-3D, आणि game engines साठी exports.",
  "Auto-rigging सह वेगवान generation; ज्या characters ना animate करायचं आहे त्यांच्यासाठी उत्तम.",
  "Text किंवा image पासून detailed 3D, स्वच्छ topology सह; plugins मुळे models थेट Blender, Unity किंवा Unreal मध्ये जातात.",
  "संपूर्ण प्रोजेक्टमध्ये एकसारख्या स्टाइलच्या game assets साठी बेस्ट.",
  "2.5D/sprite गेम्ससाठी 3D पूर्ण सोडून द्या — concept art आणि textures लोकली बनवा."]),
 "best-ai-for-meeting-notes": ("मीटिंग notes साठी बेस्ट AI", "कॉल्स रेकॉर्ड, transcribe आणि summarize करा, म्हणजे कोणालाच notes घ्याव्या लागणार नाहीत.", [
  "टॉप पिक: तुमच्या कॉल्समध्ये आपोआप जॉइन होतो, चांगल्या summaries, search आणि CRM integrations सह.",
  "सगळ्यात चांगला free tier आणि live transcription; summaries थोड्या generic असतात.",
  "Sales आणि customer कॉल्ससाठी बेस्ट, जिथे फक्त notes नाही तर clips शेअर करायच्या असतात.",
  "तुमची टीम आधीच Notion मध्ये असेल तर बिल्ट-इन meeting notes — वेगळ्या bot ची गरज नाही.",
  "कोणताही bot नाही: transcript पेस्ट करा आणि जास्त नेमक्या summaries आणि action items मिळवा. Automatic recording हवं असेल तर टाळा."]),
 "best-ai-for-chatbots-rag": ("Chatbots आणि RAG साठी बेस्ट AI", "तुमच्या स्वतःच्या docs वरून उत्तर देणारा असिस्टंट बनवा — no-code पासून custom कोडपर्यंत.", [
  "सुरुवातीसाठी टॉप पिक: तुम्ही अपलोड केलेल्या docs वर आधारित Claude Project काही मिनिटांत टीम असिस्टंट बनतो. तुमच्या स्वतःच्या साइटवर लावायचा असेल तर टाळा.",
  "तुमच्या फाइल्स असलेला ChatGPT Project सुद्धा हेच काम करतो. Custom GPTs 11 डिसेंबर 2026 ला बंद होत आहेत, म्हणून नवीन बनवू नका.",
  "खरी अडचण डेटा नीट ingest आणि retrieve करण्याची असेल तेव्हा बेस्ट code framework.",
  "Integrations ची सगळ्यात मोठी ecosystem; साध्या bots साठी गरजेपेक्षा जास्त abstraction.",
  "त्याच्याकडून एक हलकी custom RAG ॲप लिहून घ्या, आणि ती तुमच्या टूल्सशी जोडण्यासाठी MCP वापरा.",
  "तुमच्या sources वर zero-setup Q&A, embed करण्यासाठी नाही तर वैयक्तिक वापरासाठी."]),
 "best-ai-for-deploy-hosting": ("AI ने बनवलेल्या ॲप्ससाठी बेस्ट hosting", "तुमच्या AI टूल्सनी आत्ताच बनवलेलं ॲप कुठे ship करायचं. ही AI टूल्स नाहीत, hosting प्लॅटफॉर्म्स आहेत — AI च्या मदतीने बनवणाऱ्यांना ती किती फिट बसतात यावरून निवडलेली.", [
  "Next.js/React ॲप्ससाठी (आणि v0 मधून येणाऱ्या कोणत्याही गोष्टीसाठी) टॉप पिक: git वर push करा, previews सह live URL मिळवा.",
  "Static sites आणि साध्या ॲप्ससाठी उत्तम, भरपूर free tier आणि बिल्ट-इन forms सह.",
  "Backends, databases आणि background workers साठी सगळ्यात सोपी जागा. फक्त static sites असतील तर टाळा.",
  "Docker किंवा अनेक regions हवे असतील तर बेस्ट; setup थोडा जास्त लागतो. Fly ने 2026 मध्ये GPUs देणं बंद केलं.",
  "एकाच जागी बनवा आणि host करा — deploy config ला कधीच हात लावायचा नसेल तर सगळ्यात सोपं."]),
 "best-ai-for-chrome-extensions": ("Chrome extensions बनवण्यासाठी बेस्ट AI", "'यासाठी एखादं बटण हवं होतं' पासून चालू browser extension पर्यंत.", [
  "टॉप पिक: manifest, scripts आणि popup बनवतो, आणि तुम्ही reload करून टेस्ट करताना context मध्ये errors दुरुस्त करतो.",
  "संपूर्ण extension चा ढाचा उभा करण्यात आणि Manifest V3 permission issues वर पुन्हा पुन्हा काम करण्यात उत्तम.",
  "छोट्या, एका फाइलच्या extension साठी ठीक. Manifest V3 वापरतोय ना ते तपासा, कारण जुनी examples सगळीकडे आहेत.",
  "स्वतः AI टूल नाही, पण AI टूलसोबत छान चालतं: Vite-based, सक्रियपणे maintain होणारं framework जे extension चा boilerplate काढून टाकतं.",
  "स्वतः लिहायचं असेल तर Chrome APIs साठी चांगलं autocomplete."]),
 "best-ai-for-thumbnails-youtube-packaging": ("YouTube thumbnails आणि packaging साठी बेस्ट AI", "Thumbnails, titles आणि क्लिक मिळवून देणारा तो hook.", [
  "इमेजमध्येच ठळक आणि वाचता येणारा text असलेल्या thumbnails साठी टॉप पिक.",
  "बोलून एडिट करण्यासाठी (\"चेहरा अजून थोडा आश्चर्यचकित दाखव\") आणि त्याच chat मध्ये titles वर brainstorming साठी बेस्ट.",
  "जिथे तुम्ही खरंतर final thumbnail चा layout करता: templates, background removal आणि Magic टूल्स.",
  "सगळ्यात लक्षवेधी backgrounds आणि scenes; text नंतर Canva मध्ये टाका.",
  "Title आणि thumbnail-text च्या जोड्यांवर brainstorm करा; एखादी आयडिया clickbait सारखी वाटली तर प्रामाणिकपणे सांगतो."]),
 "best-ai-for-agent-frameworks": ("बेस्ट AI agent frameworks", "Tools, memory आणि multi-step workflows असलेले स्वतःचे agents बनवण्यासाठी code frameworks.", [
  "सुरुवातीसाठी टॉप पिक: छोटी API, ज्यात tools, handoffs आणि tracing बिल्ट-इन आहेत.",
  "स्पष्ट कंट्रोल हवा असेल तेव्हा बेस्ट: state, retries, human-in-the-loop आणि production मध्ये भरवसा.",
  "Role-based multi-agent 'crews' चा prototype बनवण्याचा सगळ्यात वेगवान मार्ग; मोठ्या स्केलवर कंट्रोलमध्ये ठेवणं कठीण.",
  "AutoGen आणि Semantic Kernel चा Microsoft कडून आलेला उत्तराधिकारी: Python किंवा .NET मध्ये agents आणि graph-based workflows; Azure वर स्वाभाविक निवड.",
  "Framework नाही, पण कोणत्याही agent ला tools देण्याचा standard मार्ग हाच. तुमची tools MCP servers म्हणून बनवा."]),
 "best-ai-for-logos-brand": ("Logos आणि branding साठी बेस्ट AI", "Logo आयडिया, brand marks आणि सुरुवातीचं brand kit, पटकन.", [
  "टॉप पिक: खरे vector (SVG) logos आणि icons बनवतो, जे तुम्ही एडिट आणि scale करू शकता.",
  "वाचता येणाऱ्या wordmarks असलेल्या logo concepts साठी बेस्ट; निवडलेला logo तरीही vectorize करावा लागेल.",
  "Non-designers साठी logo आणि brand kit देणारं सगळ्यात सोपं all-in-one; रिझल्ट्स थोडे template सारखे वाटू शकतात.",
  "Final logo files पेक्षा brand चा mood आणि visual direction शोधण्यासाठी उत्तम.",
  "बोलून एखाद्या concept वर काम करण्यासाठी सोयीचं. काहीही trademark करण्याआधी ते खरंच वेगळं आहे का ते तपासा."]),
 "best-ai-for-customer-support": ("Customer support साठी बेस्ट AI", "AI agents आणि AI ने लिहिलेल्या replies ने ग्राहकांना पटकन उत्तर द्या.", [
  "Tickets आपोआप सोडवण्यासाठी टॉप पिक; Intercom help desk शिवायही चालतो. किंमत प्रत्येक resolution नुसार, म्हणजे volume सोबत खर्च वाढतो.",
  "आधीच Zendesk वर असाल तर स्वाभाविक निवड; छोट्या टीम्ससाठी setup आणि pricing जड.",
  "मोठं प्लॅटफॉर्म नको, तर AI drafts आणि answers असलेला सोपा inbox हवा असणाऱ्या छोट्या टीम्ससाठी बेस्ट.",
  "कोणत्याही प्लॅटफॉर्मची गरज नाही: ticket आणि तुमचे docs पेस्ट करा आणि विचारपूर्वक लिहिलेला, मैत्रीपूर्ण reply draft मिळवा.",
  "तीच कल्पना; तुमचे docs आणि tone guide एका ChatGPT Project मध्ये ठेवा, म्हणजे प्रत्येक draft त्याच context पासून सुरू होईल."]),
 "best-ai-for-scraping": ("Web scraping साठी बेस्ट AI", "वेबसाइट्सचं ॲप्स, रिसर्च आणि AI pipelines साठी स्वच्छ डेटामध्ये रूपांतर करा. प्रत्येक साइटच्या terms आणि robots.txt चा आदर करा.", [
  "Builders साठी टॉप पिक: एका API call मध्ये साइटचा स्वच्छ markdown किंवा structured JSON.",
  "रेडीमेड scraper आधीच असेल तेव्हा बेस्ट (maps, social, e-commerce); scheduling बिल्ट-इन.",
  "ज्या साइट्सना खरा logged-in ब्राउझर किंवा क्लिक करत राहणं लागतं त्यांच्यासाठी; Stagehand सोबत वापरा.",
  "खऱ्या पेजवर custom scraper लिहितो आणि debug करतो; एकदाच्या किंवा वेगळ्या साइट्ससाठी बेस्ट.",
  "तेच काम, तुमच्या एडिटरमध्ये — scraper एखाद्या चालू प्रोजेक्टचा भाग असेल तेव्हा चांगलं."]),
 "best-ai-for-api-testing": ("API testing साठी बेस्ट AI", "Requests लिहा, tests बनवा आणि फेल होणारे endpoints debug करा.", [
  "तुमची टीम आधीपासून Postman वापरत असेल तर टॉप पिक: Agent Mode तुमच्या collections वरून tests लिहितो, बिघडलेल्या requests दुरुस्त करतो आणि APIs चं documentation बनवतो.",
  "तुमच्या API कोडच्या अगदी बाजूला test suites (pytest, Jest वगैरे) बनवतो आणि दुरुस्त करतो.",
  "OpenAPI spec किंवा फेल झालेला response पेस्ट करा आणि तुमच्याकडून सुटलेले test cases आणि edge cases मिळवा.",
  "झटपट test scripts आणि mock डेटासाठी चांगला; गोष्टी वापरून पाहण्यासाठी Python चालवू शकतो.",
  "स्वतः AI नाही, पण त्याच्या साध्या फाइल्सच्या collections AI एडिटर्सना सहज वाचता-लिहिता येतात. Offline आणि git-native राहायचं असेल तर हे निवडा."]),
 "best-ai-for-notion-docs": ("Notes आणि docs साठी बेस्ट AI", "AI ने तुमच्या notes आणि टीम docs लिहा, व्यवस्थित लावा आणि सर्च करा.", [
  "तुमचं workspace Notion मध्ये असेल तर टॉप पिक: AI writing, सगळ्या पेजेसवर Q&A आणि meeting notes, सगळं एकाच ठिकाणी.",
  "Docs च्या प्रत्यक्ष लेखन आणि एडिटिंगसाठी सगळ्यात चांगला; Projects रेफरन्स मटेरियल हाताशी ठेवतात.",
  "Docs चा draft बनवण्यासाठी आणि त्यांची पुन्हा मांडणी करण्यासाठी versatile, पहिल्या outline पासून पूर्ण rewrite पर्यंत.",
  "तुमचे docs खरंतर tables आणि automations असलेली छोटी ॲप्स असतील तेव्हा हे निवडा.",
  "आपोआप व्यवस्थित होणाऱ्या personal notes; टीम wikis साठी टाळा."]),
}

NEW = {
 "claude-code": "Anthropic चा terminal coding agent — सगळ्यात जास्त चर्चेत असलेल्या dev टूल्सपैकी एक.",
 "codex": "OpenAI ने पुन्हा लाँच केलेला Codex coding agent (cloud + CLI).",
 "veo": "Google चं व्हिडिओ model, जे आता synced audio पण बनवतं.",
 "manus": "Autonomous general agent, जो multi-step कामांमुळे व्हायरल झाला.",
 "lovable": "वेगाने वाढणारा prompt-to-app builder.",
 "notebooklm": "Audio Overviews नी research notes ना podcasts मध्ये बदललं.",
 "kling": "AI व्हिडिओ generation मधला तगडा स्पर्धक.",
 "deepseek": "Open-weight reasoning models, ज्यांनी pricing मध्ये खळबळ उडवली.",
 "mcp": "ते open protocol जे आता बहुतेक agent टूल्स tools access साठी सपोर्ट करतात.",
 "windsurf": "Agentic एडिटर, जो थेट Cursor ला टक्कर देतो.",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['जानेवारी', 'फेब्रुवारी', 'मार्च', 'एप्रिल', 'मे', 'जून', 'जुलै', 'ऑगस्ट', 'सप्टेंबर', 'ऑक्टोबर', 'नोव्हेंबर', 'डिसेंबर']
DATE_MD = '{d} {m}'
DATE_MDY = '{d} {m} {y}'
RELEASES = {
 'voxtral-3': 'Mistral चे नवीन speech-to-text आणि text-to-speech models, सोबत फोन आणि वेबवरच्या real-time voice agents साठी SDK. Mistral च्या API मधून (EU-hosted पर्यायासह) किंवा self-hosted.',
 'kling-4': 'Kuaishou चं नवीन व्हिडिओ model: एकाच वेळी 30 सेकंदांपर्यंतच्या clips, वेगवान हालचाली आणि कॅमेरा मूव्ह्समध्ये जास्त स्थिरता, आणि प्रत्येक कामात 15 पर्यंत reference assets आणि 10 keyframes.',
 'muse-spark-open': 'Coding आणि agent कामांसाठी Meta चं open-weight model (816B parameters, 42B active, 1M-token context). Meta ते दोन Mac Studios वर चालवतं; बहुतेकांसाठी hosted APIs हाच सोपा मार्ग.',
 'claude-haiku-5-5': 'Anthropic चं सगळ्यात स्वस्त आणि वेगवान model, जास्त व्हॉल्यूमच्या कामांसाठी: support bots, summaries आणि coding subagents. Anthropic च्या मते ते चालवायला Haiku 4.5 पेक्षा सुमारे 75% कमी खर्च येतो.',
 'nano-banana-2-1': 'Google चं अपडेटेड image generation आणि editing model: चांगले edits, पात्रांमध्ये जास्त consistency आणि इमेजमध्ये स्पष्ट मजकूर. Gemini ॲप, AI Studio, Gemini API, Flow आणि Stitch मध्ये उपलब्ध.',
 'copilot-dynamic-workflows': 'Multi-agent कामं code मध्ये ठरवा (parallel steps, एकमेकांना तपासणारे subagents, तुम्ही review करण्यासाठी checkpoints) — Copilot CLI, Copilot ॲप आणि Copilot SDK मध्ये. Public preview, सर्व plans मध्ये.',
 'heygen-video': 'HeyGen चं पहिलं general-purpose व्हिडिओ model: मजकूर, इमेज किंवा reference media वरून 5 ते 15 सेकंदांच्या clips, ज्यात संवाद आणि आवाज एकत्र तयार होतात. HeyGen API मधून उपलब्ध.',
 'gpt-6-1-sol': 'OpenAI DevDay मध्ये आलेलं GPT-6 Sol चं अपग्रेड, ज्याचा फोकस agentic coding, computer use आणि प्रोफेशनल कामावर आहे. OpenAI च्या मते ते खूप कमी किमतीत GPT-6 Astra च्या जवळ पोहोचतं.',
 'openai-agents-api-computer-use': 'Agents API आता computer use ने software चालवू शकते, आणि Codex चे multi-agent फीचर्स, tool search आणि context compaction तुमच्या ॲपमध्ये आणते. Infrastructure OpenAI चालवतं.',
 'claude-sonnet-5-5': 'Anthropic चं वेगवान आणि स्वस्त Sonnet, ठरावीक व्याप्तीच्या रोजच्या कामांत आणि bug fixing मध्ये सगळ्यात चांगलं. Sonnet 5 पेक्षा 30%+ वेगवान, त्याच $2/$10 प्रति million tokens किमतीत.',
 'lovable-free-chat': 'Lovable सोबत chat आता रोजच्या free मर्यादेत मोफत: features प्लॅन करा, ॲपच्या code आणि database बद्दल विचारा किंवा लाँचचा मजकूर ड्राफ्ट करा. Build करायला अजूनही credits लागतात.',
 'cursor-projects': 'एखादं feature किंवा migration सारख्या मोठ्या कामांसाठी beta: एक coordinator agent cloud मध्ये चालतो, कामाचं नियोजन करतो, अनेक subagents ना वाटून देतो आणि काळानुसार shared context जपतो.',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — कोणत्या कामासाठी कोणतं AI टूल", TAG + " Use case नुसार मांडलेली AI टूल्सची निवडक डिरेक्टरी.", """
<h1>कोणत्या कामासाठी कोणतं AI टूल.</h1><p class="lede">Tool Use Cases ही AI टूल्सची डिरेक्टरी आहे, जी तुम्हाला कोणतं काम करायचं आहे त्यानुसार मांडलेली आहे — vibe coders, builders आणि AI वापरून काहीही ship करणाऱ्या प्रत्येकासाठी.</p>
<input type="search" placeholder="Use cases फिल्टर करा (उदा. video, coding, research)…" data-filter=".f" aria-label="Use cases फिल्टर करा">
<h2>Use cases</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>नवीन लाँच आणि ट्रेंडिंग</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">सगळे नवीन लाँच पाहा →</a></p>"""),
 "use-cases": ("AI टूल use cases — Tool Use Cases", "Use case नुसार AI टूल्स पाहा: vibe coding, coding agents, debugging, गेम prototyping, व्हिडिओ, लेखन, रिसर्च, images आणि बरंच काही.", """
<h1>Use cases</h1><p class="lede">काम निवडा. कोणती टूल्स वापरून पाहण्यासारखी आहेत आणि का, ते आम्ही सांगतो.</p>
<input type="search" placeholder="Use cases फिल्टर करा…" data-filter=".f" aria-label="फिल्टर करा"><div class="grid">{CARDS}</div>"""),
 "tools": ("सगळी AI टूल्स A ते Z — Tool Use Cases", "Tool Use Cases डिरेक्टरीमधलं प्रत्येक AI टूल, ते काय करतं आणि कोणत्या use cases मध्ये फिट बसतं.", """
<h1>सगळी टूल्स</h1><input type="search" placeholder="टूल्स फिल्टर करा…" data-filter=".f" aria-label="टूल्स फिल्टर करा"><div class="grid">{ROWS}</div>"""),
 "new": ("नवीन आणि ट्रेंडिंग AI टूल्स — Tool Use Cases", "Builders साठी लक्षवेधी आणि ट्रेंडिंग AI टूल लाँच: coding agents, व्हिडिओ models, रिसर्च टूल्स आणि बरंच काही.", """
<h1>नवीन लाँच आणि ट्रेंडिंग</h1><p class="lede">गेल्या सहा आठवड्यांतले, builders साठी महत्त्वाचे AI टूल लाँच आणि मोठे अपडेट्स. प्रत्येकासोबत तारीख, अधिकृत घोषणेची लिंक आणि ते कोणत्या use case मध्ये बसतं ते दिलं आहे.</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Tool Use Cases स्पॉन्सर करा — तुमचं AI टूल फीचर करा", "टूल बनवणारे संबंधित use-case पेजेसच्या सगळ्यात वर स्पष्टपणे लेबल केलेला फीचर्ड स्लॉट स्पॉन्सर करू शकतात.", """
<h1>एखादा use case स्पॉन्सर करा</h1><p class="lede">Vibe coders आणि builders टूल निवडत असतानाच त्यांच्यापर्यंत पोहोचा.</p>
<h2>हे कसं काम करतं</h2><ul><li>प्रत्येक use-case पेजच्या सगळ्यात वर एक <b>Sponsored / Featured</b> स्लॉट असतो.</li><li>त्यावर नेहमी स्पष्टपणे "Sponsored" लिहिलेलं असतं आणि तो आमच्या editorial निवडीपासून वेगळा ठेवला जातो.</li><li>आम्ही फक्त तीच टूल्स घेतो जी त्या use case मध्ये खरंच फिट बसतात.</li><li>स्पॉन्सरशिपमुळे आमचं मत किंवा रँकिंग कधीच बदलत नाही.</li></ul>
<h2>उदाहरण</h2>{SPONSOR_CARD}
<div class="cta">किंमत आणि उपलब्धतेसाठी संपर्क करा. <a class="btn" href="{SPONSOR_MAILTO}">स्पॉन्सर करण्यासाठी ईमेल करा</a></div>"""),
 "about": ("आमच्याबद्दल — Tool Use Cases", "Tool Use Cases ही use case नुसार मांडलेल्या AI टूल्सची स्वतंत्र, autonomously चालणारी डिरेक्टरी आहे.", """
<h1>आमच्याबद्दल</h1><p class="lede">Tool Use Cases एकाच प्रश्नाचं उत्तर देतं: या कामासाठी मी कोणतं AI टूल वापरू?</p>
<p>बहुतेक AI डिरेक्टरीज म्हणजे फक्त भलीमोठी लिस्ट. आम्ही use case नुसार मांडणी करतो, आणि प्रत्येक निवडीसोबत सोप्या भाषेत छोटंसं मत देतो, म्हणजे तुम्ही एका मिनिटात निर्णय घेऊ शकता.</p>
<p>ही साइट autonomously चालते — एक AI operator ती अपडेट ठेवतो, आणि तिची मानवी जबाबदारी Lali Publications ची आहे. आम्ही फक्त खरी, नावाजलेली टूल्सच लिस्ट करतो आणि बनावट स्कोर किंवा युजर्सचे आकडे publish करत नाही.</p>
<p>Tool Use Cases हे Lali Publications प्रकाशित करतं, जे <a href="https://agentusecases.ai">agentusecases.ai</a> पण चालवतं. आम्ही लिस्ट करत असलेल्या कोणत्याही टूलशी आमचा संबंध नाही.</p>
<p>हे साइटचं मराठी व्हर्जन आहे, ज्यात <a href="@R/about/index.html" hreflang="en">इंग्रजी व्हर्जन</a>सारखेच use cases, तीच निवड आणि तेच रँकिंग आहे.</p>
<p>दुरुस्त्या किंवा सूचनांसाठी: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("सबस्क्राइब केल्याबद्दल धन्यवाद — Tool Use Cases", "Tool Picks Weekly साठी तुमचा साइनअप मिळाला आहे.", """
<h1>तुम्ही लिस्टमध्ये आलात. धन्यवाद!</h1><p class="lede">Tool Picks Weekly साठी तुमचा साइनअप मिळाला आहे. पुढचा अंक सोमवारी येईल. सध्या न्यूजलेटर इंग्रजीत पाठवलं जातं.</p>
<p><a class="btn" href="@R/@Pindex.html">Tool Use Cases वर परत जा</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "AI टूल use cases",
 "uc_coll": ("AI टूल use cases", "Use case नुसार AI टूल्स पाहा."),
 "tools_crumb": "सगळी टूल्स", "tools_coll": ("सगळी AI टूल्स A ते Z", "Tool Use Cases डिरेक्टरीमधलं प्रत्येक AI टूल."),
 "new_crumb": "नवीन लाँच आणि ट्रेंडिंग", "new_coll": ("नवीन आणि ट्रेंडिंग AI टूल्स", "Builders साठी लक्षवेधी आणि ट्रेंडिंग AI टूल लाँच."),
 "sponsor_crumb": "स्पॉन्सर",
 "about_crumb": "आमच्याबद्दल", "about_coll": ("Tool Use Cases बद्दल", "Use case नुसार मांडलेल्या AI टूल्सची स्वतंत्र, autonomously चालणारी डिरेक्टरी, Lali Publications प्रकाशित."),
}
