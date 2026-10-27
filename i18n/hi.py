"""Hindi (hi) locale for Tool Use Cases.
Style: natural, conversational Devanagari the way Indian tech creators write. Product names and common
tech terms (vibe coding, AI agent, deploy, debugging, RAG, API, prompt...) stay in Latin script.
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "hi"
PREFIX = "hi/"
SHORT = "HI"
NATIVE = "हिन्दी"
ENGLISH_NAME = "Hindi"
INDIA = True
OG_LOCALE = "hi_IN"
RSS_LANG = "hi"

TAG = "किस काम के लिए कौन-सा AI टूल — vibe coders और builders के लिए।"

UI = {
 "nav_use_cases": "Use cases", "nav_tools": "टूल्स", "nav_new": "नए लॉन्च",
 "nav_newsletter": "न्यूज़लेटर", "nav_sponsor": "स्पॉन्सर", "nav_about": "हमारे बारे में",
 "home": "होम", "use_cases": "Use cases",
 "og_alt": "Tool Use Cases: AI टूल्स, आपके काम के हिसाब से रैंक किए गए",
 "footer": "Tool Use Cases · Lali Publications की पेशकश ·",
 "nl_h2": "Vibe coders के लिए हर हफ़्ते AI टूल्स की चुनिंदा लिस्ट",
 "nl_p": "नए टूल्स + कौन-सा टूल किस काम का है। बिल्कुल फ्री। अभी न्यूज़लेटर अंग्रेज़ी में आता है।",
 "nl_placeholder": "aap@example.com", "nl_aria": "ईमेल एड्रेस", "nl_button": "सब्सक्राइब करें",
 "nl_subject": "Tool Use Cases newsletter signup (hi)",
 "nl_small": "ईमेल Lali Publications की तरफ़ से आएगा। कोई spam नहीं, जब चाहें unsubscribe करें।",
 "nl_latest": "लेटेस्ट इश्यू पढ़ें: {LINK} (अंग्रेज़ी में)।",
 "verdict": "हमारी राय:", "our_picks": "हमारी पसंद", "related": "मिलते-जुलते use cases",
 "browse_all": "सारे use cases देखें →",
 "disclaimer": "ये पसंद हमारी अपनी है, इसके लिए किसी ने पैसे नहीं दिए। कीमतें और फ़ीचर्स अक्सर बदलते रहते हैं — हर टूल की ऑफ़िशियल साइट ज़रूर चेक करें।",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} {names} और बाकी टूल्स पर हमारी राय।",
 "review_name": "{tool} — {title}",
 "sponsored": "Sponsored", "sponsor_h3": "आपका टूल यहाँ",
 "sponsor_p": "यह फ़ीचर्ड स्लॉट उन टूल बनाने वालों के लिए है जिनका टूल इस use case में सच में फ़िट बैठता है। हमेशा साफ़ तौर पर लेबल किया जाता है और हमारी पसंद से हमेशा अलग रहता है।",
 "sponsor_link": "स्पॉन्सर करने के लिए ईमेल करें",
 "new_badge": "ख़ास / ट्रेंडिंग",
 "last_updated": 'आख़िरी अपडेट: {date}', "earlier_h2": 'पहले के लॉन्च', "earlier_p": 'इस अपडेट से पहले हमने जिन लॉन्च को दिखाया था। अब ये नए नहीं रहे, पर जानने लायक़ ज़रूर हैं।', "fits": 'Use case:', "source": 'स्रोत',
 "rss_title": "Tool Use Cases (हिन्दी)",
 "rss_desc": "Tool Picks Weekly के इश्यू (अंग्रेज़ी में) और ध्यान देने लायक नए AI टूल लॉन्च।",
 "rss_new_prefix": "नया और ट्रेंडिंग: ", "rss_issue_suffix": " (अंग्रेज़ी में)",
 "rss_cat_newsletter": "न्यूज़लेटर", "rss_cat_new": "नए लॉन्च",
 "llms_h2": "हिन्दी में (hi)",
 "llms_intro": "पूरी साइट हिन्दी में, वही use cases, वही पसंद और वही रैंकिंग जो अंग्रेज़ी वर्ज़न में है।",
 "llms_other": [("होम", ""), ("सारे AI टूल्स A से Z", "tools/"), ("नए लॉन्च और ट्रेंडिंग", "new/"), ("हमारे बारे में", "about/"), ("स्पॉन्सर", "sponsor/")],
}

TOOLS = {
 "cursor": "AI-first कोड एडिटर (VS Code का fork), जिसमें chat, inline edits और agent mode है।",
 "claude": "Anthropic का AI असिस्टेंट, लंबे डॉक्यूमेंट्स, लिखने और कोड में ज़बरदस्त।",
 "claude-code": "Anthropic का terminal में चलने वाला agentic coding टूल।",
 "chatgpt": "OpenAI का हर काम वाला AI असिस्टेंट, जिसमें chat, images, voice और search है।",
 "codex": "OpenAI का coding agent, जो cloud में या CLI से आपकी repos पर काम करता है।",
 "copilot": "AI pair programmer, जो VS Code, JetBrains और GitHub में बिल्ट-इन है।",
 "v0": "Vercel का AI app/UI builder, जो prompts से React + Tailwind ऐप्स बनाता है।",
 "lovable": "Prompt से full-stack वेब ऐप बनाने वाला builder, Supabase integration के साथ।",
 "replit": "ब्राउज़र वाला IDE, जिसका agent एक prompt से ऐप बनाकर deploy भी कर देता है।",
 "bolt": "StackBlitz का ब्राउज़र में चलने वाला prompt-to-app builder।",
 "windsurf": "Cognition का AI कोड एडिटर (पहले Windsurf): पूरा IDE, साथ में local और cloud coding agents चलाने का command center।",
 "opencode": "Terminal, desktop या IDE के लिए open-source (MIT) coding agent, जो local models समेत 75+ model providers के साथ चलता है।",
 "devin": "Cognition का autonomous software engineering agent।",
 "gemini": "Google का AI असिस्टेंट, बहुत बड़ी context windows और Google integration के साथ।",
 "perplexity": "AI answer engine, जो वेब सर्च करता है और sources भी बताता है।",
 "notebooklm": "Google की research notebook (पहले NotebookLM), जो आपके अपलोड किए sources के आधार पर ही जवाब देती है।",
 "elicit": "Academic papers ढूँढने और उनका सार निकालने के लिए AI research असिस्टेंट।",
 "notion-ai": "Notion workspaces के अंदर बिल्ट-इन AI writing और Q&A।",
 "grammarly": "आप जहाँ भी टाइप करें, वहीं grammar, tone और rewrites में मदद करने वाला writing असिस्टेंट।",
 "midjourney": "Image generator, जो अपने दमदार aesthetic और artistic आउटपुट के लिए जाना जाता है।",
 "dalle": "ChatGPT के अंदर OpenAI की image generation, instructions मानने और इमेज में text डालने में अच्छी।",
 "ideogram": "Image generator, जो इमेज में साफ़ पढ़ने लायक text डालने में ख़ास तौर पर अच्छा है।",
 "flux": "High-quality image models की फ़ैमिली, जिनमें से कुछ open weights के साथ आते हैं।",
 "firefly": "Adobe के generative image टूल्स, जिन्हें commercial इस्तेमाल के लिए सुरक्षित रहने के हिसाब से train किया गया है।",
 "sd": "Open image models की फ़ैमिली, जिसे आप लोकली चला सकते हैं (जैसे ComfyUI से)।",
 "runway": "AI वीडियो generation और editing suite (Gen-series models)।",
 "elevenlabs": "असली जैसी AI voiceover, voice cloning और dubbing।",
 "descript": "Transcript एडिट करके वीडियो और podcasts एडिट करें।",
 "heygen": "AI avatar वीडियो और वीडियो translation।",
 "capcut": "Free plan वाला वीडियो एडिटर; auto-captions और ज़्यादातर AI tools के लिए Pro चाहिए।",
 "opus": "लंबे वीडियो को अपने-आप छोटे vertical clips में बदल देता है।",
 "veo": "Google DeepMind का text-to-video model, native audio के साथ।",
 "rosebud": "Prompts से गेम बनाने का ब्राउज़र टूल (Three.js/Phaser)।",
 "scenario": "आपके अपने training sets से एक जैसे style वाले game art assets बनाता है।",
 "meshy": "Game assets के लिए text/image से 3D model generation।",
 "suno": "पूरे गाने बना देता है, गेम/वीडियो में placeholder म्यूज़िक के लिए काम का।",
 "sentry": "Error monitoring, AI root-cause analysis और fix के सुझावों के साथ।",
 "deepseek": "चीन की AI लैब, जिसके open-weight reasoning models दमदार और सस्ते हैं।",
 "ollama": "Open models (Llama, Qwen वगैरह) को एक command से लोकली चलाएँ।",
 "manus": "General-purpose autonomous agent, जो वेब ब्राउज़ करके कई स्टेप वाले काम पूरे करता है।",
 "kling": "Kuaishou का text/image-to-video generator।",
 "grok": "xAI का असिस्टेंट, X और वेब पर real-time search के साथ।",
 "mcp": "AI agents को टूल्स और डेटा से जोड़ने का open standard।",
 "n8n": "Open-source workflow automation, AI agent nodes के साथ; फ्री में self-host करें या उनका cloud इस्तेमाल करें।",
 "make": "Visual no-code automation builder, हज़ारों ऐप्स में कई स्टेप वाले scenarios के लिए।",
 "zapier": "सबसे ज़्यादा ऐप्स से जुड़ने वाला no-code automation प्लेटफ़ॉर्म, अब AI steps और agents के साथ।",
 "framer": "डिज़ाइनर्स के लिए वेबसाइट builder, AI page generation, CMS और hosting के साथ।",
 "stitch": "Google का prompt-to-UI डिज़ाइन टूल (पहले Galileo AI), जो Figma और कोड में export करता है।",
 "uizard": "शुरुआत करने वालों के लिए आसान AI UI mockup टूल; prompts और sketches को ऐप स्क्रीन में बदलता है।",
 "figma": "UI डिज़ाइन का standard टूल, बिल्ट-इन AI फ़ीचर्स और prompt-to-prototype के लिए Figma Make के साथ।",
 "openai-tts": "OpenAI की speech API: सस्ती, natural आवाज़ें, जिन्हें आप instructions से कंट्रोल कर सकते हैं।",
 "lyria": "Gemini ऐप में Google का music model: vocals या instrumental वाले करीब 3 मिनट तक के गाने, MP3 में डाउनलोड करें।",
 "aiva": "Instrumental, orchestral और soundtrack म्यूज़िक के लिए AI composer, MIDI export के साथ।",
 "surfer": "SEO और AI search visibility टूल (पहले SurferSEO), जिसका content editor आपके draft को top-ranking पेजों से तुलना करके स्कोर देता है।",
 "clearscope": "Keyword coverage और content grading के लिए premium content-optimization टूल।",
 "lavender": "Sales email coach, जो आपके inbox के अंदर ही cold emails को स्कोर करता है और दोबारा लिखता है।",
 "julius": "Spreadsheets और डेटा फ़ाइलों से chat करके analysis और charts पाएँ।",
 "excel-copilot": "Excel के अंदर Copilot, आपकी workbooks पर formulas, analysis और charts के लिए।",
 "powerpoint-copilot": "PowerPoint के अंदर Copilot: prompt या फ़ाइल से deck का draft बनाता है, slides जोड़ता है और content को दोबारा लिखता या री-ऑर्गनाइज़ करता है।",
 "gamma": "Prompt या outline से presentations, docs और वेब पेज बनाता है।",
 "beautiful-ai": "Smart templates वाला slide सॉफ़्टवेयर, जो content जोड़ते ही अपने-आप format हो जाता है।",
 "rodin": "Text या image से 3D बनाने वाला generator, साफ़ topology, PBR materials और Blender, Unity, Unreal के plugins के साथ।",
 "tripo": "तेज़ text/image-to-3D generator, auto-rigging और clean topology के ऑप्शन के साथ।",
 "fireflies": "AI meeting bot, जो Zoom/Meet/Teams कॉल्स को रिकॉर्ड, transcribe और summarize करता है।",
 "otter": "Real-time मीटिंग transcription और AI summaries, काम लायक free tier के साथ।",
 "grain": "Clips और highlights पर बना meeting recorder, sales और customer टीमों में पॉपुलर।",
 "langchain": "LLM ऐप्स बनाने का open-source framework: RAG, tools और integrations।",
 "llamaindex": "Open-source framework, जिसका फ़ोकस LLMs को आपके documents और डेटा से जोड़ने (RAG) पर है।",
 "vercel": "Frontend और Next.js hosting, git-push deploys, previews और AI SDK के साथ।",
 "netlify": "Static sites और वेब ऐप्स के लिए git-based hosting, functions और forms के साथ।",
 "railway": "लगभग बिना config के repo से backends, databases और workers deploy करें।",
 "fly": "Docker containers को दुनिया भर में users के पास चलाएँ; full-stack ऐप्स के लिए अच्छा (2026 से GPU machines बंद)।",
 "wxt": "TypeScript में cross-browser extensions बनाने का Vite-based open-source framework।",
 "canva": "Online डिज़ाइन टूल, Magic Studio AI फ़ीचर्स और रेडीमेड templates के साथ।",
 "langgraph": "LangChain का framework, stateful और कंट्रोल में रहने वाले multi-step agent graphs के लिए।",
 "crewai": "Role-based AI agents की टीमें बनाने का open-source Python framework।",
 "ms-agent-framework": "Python और .NET के लिए Microsoft का open-source agent framework, AutoGen और Semantic Kernel का उत्तराधिकारी।",
 "openai-agents": "OpenAI का हल्का SDK, agents के लिए tools, handoffs, guardrails और tracing के साथ।",
 "recraft": "डिज़ाइनर्स के लिए AI image generator, जो editable vector (SVG) graphics और icons देता है।",
 "looka": "AI logo maker, जो one-time fee में logo के साथ brand kit भी बनाता है।",
 "intercom-fin": "Intercom का AI support agent, जो आपके help content से कस्टमर्स के सवाल हल करता है।",
 "zendesk": "Zendesk help desk में बिल्ट-इन AI agents और agent-assist फ़ीचर्स।",
 "helpscout": "आसान shared inbox और help desk, AI drafts, summaries और AI Answers के साथ।",
 "firecrawl": "API जो वेबसाइट्स crawl करके LLMs के लिए साफ़ markdown या structured डेटा लौटाती है।",
 "browserbase": "AI agents के लिए hosted headless browsers, साथ में open-source Stagehand framework।",
 "apify": "Scraping प्लेटफ़ॉर्म, हज़ारों रेडीमेड scrapers ('Actors') और scheduling के साथ।",
 "postman": "Requests बनाने और टेस्ट करने का API प्लेटफ़ॉर्म, Agent Mode के साथ जो आपके सभी collections पर AI से काम करता है।",
 "bruno": "Open-source, offline API client, जो collections को git में सादी फ़ाइलों की तरह रखता है।",
 "coda": "Doc और spreadsheet का मेल वाला workspace (पहले Coda), tables, automations और बिल्ट-इन AI के साथ।",
 "mem": "AI notes ऐप, जो notes को अपने-आप organize करता है और आपको उनसे chat करने देता है।",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Vibe coding के लिए बेस्ट AI", "बताइए, चलाइए, सुधारिए। ऐसे टूल्स जिनसे आप ज़्यादातर बातचीत करके ही सॉफ़्टवेयर बना लेते हैं।", [
  "डिफ़ॉल्ट चॉइस: असली codebase और एडिटर आपके पास रहता है, पर ज़्यादातर टाइपिंग AI करता है।",
  "आइडिया से auth और database वाले चालू वेब ऐप तक पहुँचने का सबसे तेज़ रास्ता, बिना किसी setup के।",
  "तब बेस्ट जब आपको जल्दी से polished React/Next.js UI चाहिए और deploy Vercel पर करना है।",
  "Hosting समेत सब कुछ ब्राउज़र में — जल्दी बनने और शेयर होने वाले prototypes के लिए अच्छा।",
  "Lovable जैसा ही; एक ही टैब में full-stack demo खड़ा करने के लिए बढ़िया।",
  "Cursor का विकल्प, जो एक साथ कई agents चलाने के लिए बना है; अगर Cursor जम नहीं रहा तो एक बार ज़रूर आज़माएँ।"]),
 "best-ai-coding-agents": ("बेस्ट AI coding agents", "ऐसे agents जो टास्क लेते हैं, कई फ़ाइलें एडिट करते हैं, commands चलाते हैं और diff के साथ लौटते हैं।", [
  "Terminal से multi-file बदलावों में कमाल; बड़े agentic कामों के लिए लोगों का फ़ेवरेट।",
  "पूरे एडिटर के अंदर agent mode, ताकि आप हर बदलाव को देखकर रिव्यू कर सकें।",
  "टास्क cloud में parallel चलने के लिए सौंप दें और फिर बने हुए PRs रिव्यू करें।",
  "Copilot का coding agent GitHub issues से काम करता है — अगर आपकी टीम GitHub पर ही रहती है तो बिल्कुल सही फ़िट।",
  "पूरे-पूरे tickets शुरू से आख़िर तक सौंपने के लिए बना है; महँगा है और टीमों के लिए है।",
  "फ्री, open-source और लगातार develop हो रहा; कोई भी model इस्तेमाल करें, local भी, या अपना मौजूदा Claude, ChatGPT या Copilot plan।"]),
 "best-ai-for-fixing-broken-code": ("टूटा कोड और errors ठीक करने के लिए बेस्ट AI", "Stack trace पेस्ट करें, fix पाएँ। ऐसे टूल्स जो सिर्फ़ कोड बनाने में नहीं, debugging में भी अच्छे हैं।", [
  "Error के साथ ज़रूरी फ़ाइलें पेस्ट करें; असली root cause तक सोचकर पहुँचने में बहुत मज़बूत।",
  "पूरे प्रोजेक्ट का context लेकर वहीं fix करता है — बार-बार copy-paste की ज़रूरत नहीं।",
  "अच्छा general debugger, और issues reproduce करने के लिए Python भी चला सकता है।",
  "'Fix' और '/explain' सीधे एडिटर में, ठीक वहीं जहाँ लाल लाइन दिख रही है।",
  "Production में errors पकड़ता है और असली traces के आधार पर fix सुझाता है।",
  "उसे tests चलाने दें, failure पढ़ने दें, और सब green होने तक दोहराने दें।"]),
 "best-ai-for-game-prototyping": ("गेम prototyping के लिए बेस्ट AI", "खेलने लायक आइडिया जल्दी स्क्रीन पर लाएँ — कोड, art, 3D और म्यूज़िक।", [
  "एक prompt से ब्राउज़र गेम बनाएँ और दूसरों के गेम remix करें।",
  "असली engines (Godot, Unity, Phaser) के लिए: scripts AI लिखता है, play-test आप करते हैं।",
  "Game art को आपके अपने style में एक जैसा रखता है — गेम्स में AI art का सबसे मुश्किल हिस्सा यही है।",
  "Levels का blockout करने के लिए जल्दी से 3D props और characters।",
  "कुछ ही मिनटों में placeholder (या final) soundtrack।",
  "बिना recording booth के character voice lines और sound effects।"]),
 "best-ai-for-video-youtube": ("वीडियो और YouTube के लिए बेस्ट AI", "Footage बनाएँ, तेज़ी से एडिट करें, voice डालें और Shorts काटें।", [
  "Talking-head वीडियो को doc की तरह एडिट करें; filler words हटा देता है। YouTubers का बहुत सारा टाइम बचाता है।",
  "B-roll और effects के लिए pro-level AI वीडियो generation और editing टूल्स।",
  "आवाज़ के साथ high-quality generated clips; cinematic b-roll के लिए दमदार।",
  "Voiceover और दूसरी भाषाओं में dubbing में अपनी कैटेगरी में सबसे बेहतर।",
  "लंबे वीडियो या stream को अपने-आप Shorts/TikToks में बदल देता है।",
  "रोज़ के काम का practical एडिटर, जिसका free plan काम का है; auto-captions के लिए अब Pro चाहिए।",
  "Avatar presenters और lip-synced translation, जब आप कैमरे पर नहीं आना चाहते।"]),
 "best-ai-writing-assistants": ("बेस्ट AI writing assistants", "Drafting, editing और rewriting — docs, blog posts, READMEs, emails।", [
  "बड़े assistants में सबसे natural लगने वाली लिखावट; बढ़िया editor भी।",
  "हर काम में ठीक-ठाक all-rounder: drafts, rewrites और variations एक ही chat में।",
  "बेस्ट, अगर आपके notes और docs पहले से Notion में हैं।",
  "आप जहाँ भी टाइप करें वहीं polish — ब्राउज़र, ईमेल, docs।",
  "Google Docs और Gmail के अंदर काफ़ी सुविधाजनक।"]),
 "best-ai-for-research": ("रिसर्च के लिए बेस्ट AI", "Sources ढूँढें, पढ़ें और summarize करें — ऐसे citations के साथ जिन्हें आप चेक कर सकें।", [
  "Live वेब से तेज़, sources वाले जवाब; जल्दी की रिसर्च के लिए सबसे पहली पसंद।",
  "अपने sources अपलोड करें और उन्हीं पर आधारित जवाब (और audio overviews) पाएँ।",
  "Deep research mode किसी टॉपिक पर लंबी, citations वाली रिपोर्ट बनाता है।",
  "Deep Research के साथ Google Search integration।",
  "ख़ास तौर पर academic papers और literature reviews के लिए बना है।",
  "यह जानने के लिए काम का कि X पर अभी लोग क्या कह रहे हैं।"]),
 "best-ai-image-generation": ("Image generation के लिए बेस्ट AI", "Thumbnails, concept art, mockups, memes।", [
  "डिफ़ॉल्ट लुक सबसे अच्छा; art, moodboards और concept art के लिए बढ़िया।",
  "Detailed instructions मानने और बातचीत करके एडिट करने में सबसे अच्छा।",
  "इसे चुनें जब इमेज में पढ़ने लायक text चाहिए — logos, posters, thumbnails।",
  "Top-tier quality, और लोकल इस्तेमाल के लिए open-weight ऑप्शन भी।",
  "Commercial काम के लिए ज़्यादा सुरक्षित; Photoshop में बिल्ट-इन।",
  "फ्री और लोकल, अगर आपके पास GPU है और आपको tinkering पसंद है (ComfyUI)।"]),
 "best-ai-for-running-local-models": ("AI को लोकली चलाने के लिए बेस्ट टूल्स", "आपकी अपनी मशीन पर प्राइवेट AI, जिसे चलाने का कोई खर्च नहीं।", [
  "एक command से open models डाउनलोड करें और चलाएँ; शुरुआत का सबसे आसान तरीका।",
  "दमदार open-weight models, जिन्हें लोकली चला सकते हैं या API से सस्ते में इस्तेमाल कर सकते हैं।",
  "इसे Ollama में चल रहे model से जोड़ें और offline coding agent पाएँ।",
  "Local image models का क्लासिक ecosystem।"]),
 "best-ai-for-automation-workflows": ("Automation workflows के लिए बेस्ट AI", "अपने ऐप्स जोड़ें और बार-बार वाले स्टेप्स AI को संभालने दें — triggers, agents और glue code।", [
  "Builders के लिए टॉप पिक: AI agent nodes, ज़रूरत पड़े तो कोड, और self-host बिल्कुल फ्री।",
  "Complex branching flows के लिए सबसे अच्छा visual canvas; हर task पर Zapier से सस्ता।",
  "सबसे ज़्यादा ऐप्स और सबसे आसान setup; अगर वॉल्यूम ज़्यादा है तो छोड़ दें, क्योंकि खर्च तेज़ी से बढ़ता है।",
  "जब no-code से बात न बने, तो उससे script या webhook handler लिखवा लें।",
  "एक बार वाले multi-step वेब टास्क के लिए; भरोसेमंद scheduled workflows की जगह नहीं ले सकता।"]),
 "best-ai-for-landing-pages": ("Landing pages के लिए बेस्ट AI", "एक दोपहर में आइडिया से live और ठीक-ठाक दिखने वाले landing page तक।", [
  "टॉप पिक: prompt से forms और database वाला पूरा पेज बनाएँ, फिर एक क्लिक में publish करें।",
  "बेस्ट, अगर custom logic से ज़्यादा design polish और आसान hosting मायने रखते हैं; बाद में marketers भी इसे एडिट कर सकते हैं।",
  "Vercel पर deploy करते हैं तो बढ़िया React/Tailwind आउटपुट; थोड़ी कोडिंग की समझ चाहिए होगी।",
  "Lovable का तेज़ full-stack विकल्प; किसी आइडिया को जल्दी टेस्ट करने के लिए अच्छा।",
  "अगर codebase पहले से है तो builders छोड़ें — बस वहीं पेज जोड़ दें।"]),
 "best-ai-for-ui-design": ("UI design के लिए बेस्ट AI", "Prompt या sketch को screens में बदलें, फिर ऐसी चीज़ में जिसे आप बना सकें।", [
  "टॉप पिक, अगर आप designers के साथ काम करते हैं: standard टूल, अब AI और Figma Make बिल्ट-इन के साथ।",
  "Mockup का स्टेप ही हटा देता है: चालू UI कोड बनाता है जिसे आप तुरंत ship कर सकते हैं।",
  "Google का फ्री और तेज़ prompt-to-UI exploration टूल (पहले Galileo AI); Figma में export करता है।",
  "Wireframes बनाने वाले non-designers के लिए सबसे आसान; pixel-level कंट्रोल चाहिए तो छोड़ दें।",
  "जब 'डिज़ाइन' असल में एक clickable, चालू ऐप होना चाहिए।"]),
 "best-ai-voice-tts": ("बेस्ट AI voice और text-to-speech", "बिना mic के voiceovers, narration, cloned voices और ऐप speech।", [
  "टॉप पिक: सबसे natural आवाज़ें, cloning और dubbing। Creators के लिए डिफ़ॉल्ट।",
  "API से ऐप्स और bulk narration के लिए सबसे सस्ती अच्छी आवाज़ें; voices के ऑप्शन कम हैं।",
  "बेस्ट, जब आप recording भी एडिट कर रहे हों — गलत बोले शब्द अपनी ही cloned voice से ठीक करें।",
  "जब आपको बोलता हुआ avatar या lip-synced translation भी चाहिए।"]),
 "best-ai-for-music": ("म्यूज़िक के लिए बेस्ट AI", "Prompt से गाने, soundtracks और background म्यूज़िक।", [
  "टॉप पिक: vocals के साथ पूरे गाने कुछ ही सेकंड में; कुछ अच्छा पाने का सबसे आसान तरीका।",
  "सीधे Gemini ऐप में vocals वाले गाने, MP3 में डाउनलोड करें; जब Suno का आउटपुट generic लगे तब आज़माएँ।",
  "Instrumental और orchestral scores के लिए बेस्ट, MIDI export के साथ जिसे आप DAW में एडिट कर सकते हैं।",
  "Voice के साथ म्यूज़िक और sound-effect generation भी है, अगर आप पहले से इस्तेमाल करते हैं तो काम का।"]),
 "best-ai-for-seo-content": ("SEO content के लिए बेस्ट AI", "ऐसे पेजों की रिसर्च, outline और लिखाई जो rank कर सकें — बिना AI वाला कचरा publish किए।", [
  "असली लिखाई के लिए टॉप पिक: सबसे natural drafts और आपके अपने मटीरियल का सबसे अच्छा editor।",
  "आपके draft को rank करने वाले पेजों से तुलना करके स्कोर देता है; काम के guardrails, पर सिर्फ़ स्कोर के लिए न लिखें।",
  "टीमों और agencies के लिए premium content grading; अकेले की साइट के लिए ज़रूरत से ज़्यादा।",
  "किसी टॉपिक पर और competitors क्या कवर करते हैं उस पर तेज़, sources वाली रिसर्च।",
  "Briefs, outlines और meta descriptions के लिए मज़बूत all-rounder; topic gaps के लिए deep research।"]),
 "best-ai-for-sales-emails": ("Sales emails के लिए बेस्ट AI", "बेहतर cold और follow-up emails लिखें — personal, छोटे, और साफ़-साफ़ AI जैसे नहीं।", [
  "टॉप पिक: prospect का context दें और छोटा, इंसान जैसा लगने वाला draft पाएँ। हमेशा एडिट करें।",
  "Drafts और variants के लिए उतना ही अच्छा; अपनी आवाज़ सेट करने के लिए custom instructions इस्तेमाल करें।",
  "सीधे Gmail/Outlook में coaching और scoring; अगर आप रोज़ cold email भेजते हैं तो फ़ायदेमंद।",
  "पहली लाइन लिखने से पहले prospect और कंपनी की तेज़ रिसर्च।",
  "आप जहाँ भी टाइप करें वहीं tone और clarity पर final polish।"]),
 "best-ai-for-data-spreadsheets": ("डेटा और spreadsheets के लिए बेस्ट AI", "CSVs analyze करें, formulas लिखें और charts बनाएँ — बस आसान अंग्रेज़ी में पूछकर।", [
  "टॉप पिक: फ़ाइल अपलोड करें और यह analysis और charts के लिए असली Python चलाता है।",
  "डेटा समझाने और formulas लिखने में बढ़िया; अपलोड की गई फ़ाइलों पर analysis भी चला सकता है।",
  "सिर्फ़ data analysis के लिए बना है, non-coders के लिए ज़्यादा आसान workflow के साथ।",
  "बेस्ट, जब काम पहले से Excel में है; इसके लिए Microsoft 365 Copilot प्लान चाहिए।",
  "Google Sheets के अंदर सबसे स्वाभाविक चॉइस।"]),
 "best-ai-for-presentations": ("Presentations के लिए बेस्ट AI", "Outline से ठीक-ठाक slide deck तक, जल्दी।", [
  "टॉप पिक: prompt लिखें या notes पेस्ट करें और एक मिनट में अच्छा दिखने वाला deck पाएँ; PowerPoint में export होता है।",
  "उन टीमों के लिए बेस्ट जिन्हें एक जैसी, on-brand slides चाहिए जिनका format बना रहे।",
  "पहले story और outline लिखवाएँ, या उससे slide content और code-based decks बनवाएँ।",
  "Outlines और speaker notes के लिए अच्छा, और डाउनलोड करने लायक .pptx फ़ाइल भी बना सकता है।",
  "तब सही, जब आपके decks पहले से PowerPoint में हैं और आपके Microsoft 365 प्लान में Copilot शामिल है।"]),
 "best-ai-for-3d-assets": ("3D assets के लिए बेस्ट AI", "Text या images से props, characters और models बनाएँ।", [
  "टॉप पिक: textures के साथ बढ़िया text/image-to-3D, और game engines के लिए exports।",
  "Auto-rigging के साथ तेज़ generation; उन characters के लिए बढ़िया जिन्हें animate करना है।",
  "Text या image से detailed 3D, साफ़ topology के साथ; plugins से models सीधे Blender, Unity या Unreal में पहुँचते हैं।",
  "पूरे प्रोजेक्ट में एक जैसे style वाले game assets के लिए बेस्ट।",
  "2.5D/sprite गेम्स के लिए 3D छोड़ ही दें — concept art और textures लोकली बनाएँ।"]),
 "best-ai-for-meeting-notes": ("मीटिंग notes के लिए बेस्ट AI", "कॉल्स रिकॉर्ड, transcribe और summarize करें, ताकि किसी को notes न लेने पड़ें।", [
  "टॉप पिक: आपकी कॉल्स में अपने-आप जुड़ जाता है, बढ़िया summaries, search और CRM integrations के साथ।",
  "सबसे अच्छा free tier और live transcription; summaries थोड़े generic होते हैं।",
  "Sales और customer कॉल्स के लिए बेस्ट, जहाँ आप सिर्फ़ notes नहीं, clips शेयर करना चाहते हैं।",
  "अगर आपकी टीम पहले से Notion में रहती है तो बिल्ट-इन meeting notes — किसी अलग bot की ज़रूरत नहीं।",
  "कोई bot ही नहीं: transcript पेस्ट करें और ज़्यादा सटीक summaries और action items पाएँ। Automatic recording चाहिए तो छोड़ दें।"]),
 "best-ai-for-chatbots-rag": ("Chatbots और RAG के लिए बेस्ट AI", "ऐसा असिस्टेंट बनाएँ जो आपके अपने docs से जवाब दे — no-code से लेकर custom कोड तक।", [
  "शुरुआत के लिए टॉप पिक: आपके अपलोड किए docs पर आधारित Claude Project मिनटों में टीम असिस्टेंट बन जाता है। अगर अपनी साइट पर लगाना है तो छोड़ दें।",
  "आपकी फ़ाइलों वाला ChatGPT Project भी यही काम करता है। Custom GPTs 11 दिसंबर 2026 को बंद हो रहे हैं, इसलिए नया न बनाएँ।",
  "बेस्ट code framework, जब असली मुश्किल आपका डेटा ठीक से ingest और retrieve करना हो।",
  "Integrations का सबसे बड़ा ecosystem; आसान bots के लिए ज़रूरत से ज़्यादा abstraction।",
  "उससे एक हल्की custom RAG ऐप लिखवाएँ, और उसे अपने टूल्स से जोड़ने के लिए MCP इस्तेमाल करें।",
  "आपके sources पर zero-setup Q&A, embed करने के लिए नहीं बल्कि personal इस्तेमाल के लिए।"]),
 "best-ai-for-deploy-hosting": ("AI से बने ऐप्स के लिए बेस्ट hosting", "आपके AI टूल्स ने जो ऐप अभी बनाया, उसे कहाँ ship करें। ये AI टूल्स नहीं, hosting प्लेटफ़ॉर्म हैं — इन्हें इस हिसाब से चुना है कि ये AI की मदद से बनाने वालों के लिए कितने फ़िट हैं।", [
  "Next.js/React ऐप्स (और v0 से बनी किसी भी चीज़) के लिए टॉप पिक: git पर push करें, previews के साथ live URL पाएँ।",
  "Static sites और आसान ऐप्स के लिए बढ़िया, अच्छे-ख़ासे free tier और बिल्ट-इन forms के साथ।",
  "Backends, databases और background workers के लिए सबसे आसान जगह। सिर्फ़ static sites के लिए छोड़ दें।",
  "बेस्ट, जब आपको Docker या कई regions चाहिए; setup थोड़ा ज़्यादा लगता है। Fly ने 2026 में GPUs देना बंद कर दिया।",
  "एक ही जगह बनाएँ और host करें — सबसे आसान, अगर आप कभी deploy config छूना ही नहीं चाहते।"]),
 "best-ai-for-chrome-extensions": ("Chrome extensions बनाने के लिए बेस्ट AI", "'इसके लिए एक बटन होना चाहिए' से एक चालू browser extension तक।", [
  "टॉप पिक: manifest, scripts और popup बनाता है, और जब आप reload करके टेस्ट करते हैं तो context में errors ठीक करता है।",
  "पूरे extension का ढाँचा खड़ा करने और Manifest V3 permission issues पर बार-बार काम करने में बढ़िया।",
  "छोटे, एक फ़ाइल वाले extension के लिए ठीक है। चेक करें कि यह Manifest V3 इस्तेमाल कर रहा है, क्योंकि पुराने examples हर जगह मिलते हैं।",
  "ख़ुद AI टूल नहीं है, पर AI टूल के साथ अच्छा चलता है: Vite-based, actively maintained framework जो extension का boilerplate हटा देता है।",
  "अगर आप ख़ुद लिखना चाहते हैं तो Chrome APIs के लिए अच्छा autocomplete।"]),
 "best-ai-for-thumbnails-youtube-packaging": ("YouTube thumbnails और packaging के लिए बेस्ट AI", "Thumbnails, titles और वो hook जो क्लिक दिलाता है।", [
  "Thumbnails के लिए टॉप पिक, जिनमें बोल्ड और पढ़ने लायक text इमेज में ही बना हो।",
  "बातचीत से एडिट करने (\"चेहरा थोड़ा और हैरान दिखाओ\") और उसी chat में titles पर brainstorming के लिए बेस्ट।",
  "जहाँ आप असल में final thumbnail का layout बनाते हैं: templates, background removal और Magic टूल्स।",
  "सबसे शानदार backgrounds और scenes; text बाद में Canva में जोड़ें।",
  "Title और thumbnail-text की जोड़ियों पर brainstorm करें; कोई आइडिया clickbait जैसा हो तो साफ़ बता देता है।"]),
 "best-ai-for-agent-frameworks": ("बेस्ट AI agent frameworks", "Tools, memory और multi-step workflows वाले अपने agents बनाने के लिए code frameworks।", [
  "शुरुआत के लिए टॉप पिक: छोटी API, जिसमें tools, handoffs और tracing बिल्ट-इन हैं।",
  "बेस्ट, जब आपको साफ़ कंट्रोल चाहिए: state, retries, human-in-the-loop और production में भरोसा।",
  "Role-based multi-agent 'crews' का prototype बनाने का सबसे तेज़ तरीका; बड़े स्केल पर कंट्रोल में रखना मुश्किल।",
  "AutoGen और Semantic Kernel का Microsoft वाला उत्तराधिकारी: Python या .NET में agents और graph-based workflows; Azure पर स्वाभाविक पसंद।",
  "Framework नहीं है, पर किसी भी agent को tools देने का standard तरीका यही है। अपने tools को MCP servers की तरह बनाएँ।"]),
 "best-ai-for-logos-brand": ("Logos और branding के लिए बेस्ट AI", "Logo आइडियाज़, brand marks और शुरुआती brand kit, जल्दी।", [
  "टॉप पिक: असली vector (SVG) logos और icons बनाता है जिन्हें आप एडिट और scale कर सकते हैं।",
  "पढ़ने लायक wordmarks वाले logo concepts के लिए बेस्ट; जो चुनें उसे फिर भी vectorize करना पड़ेगा।",
  "Non-designers के लिए logo और brand kit वाला सबसे आसान all-in-one; नतीजे थोड़े template जैसे लग सकते हैं।",
  "Final logo files के बजाय brand का mood और visual direction एक्सप्लोर करने के लिए बढ़िया।",
  "बातचीत करके किसी concept पर काम करने के लिए काम का। कुछ भी trademark कराने से पहले चेक कर लें कि वह सच में अलग है।"]),
 "best-ai-for-customer-support": ("Customer support के लिए बेस्ट AI", "AI agents और AI से लिखे replies के साथ कस्टमर्स को जल्दी जवाब दें।", [
  "Tickets अपने-आप हल करने के लिए टॉप पिक; Intercom help desk के बिना भी चलता है। हर resolution के हिसाब से कीमत, यानी वॉल्यूम के साथ खर्च बढ़ता है।",
  "अगर आप पहले से Zendesk पर हैं तो स्वाभाविक चॉइस; छोटी टीमों के लिए setup और pricing भारी।",
  "छोटी टीमों के लिए बेस्ट, जिन्हें बड़ा प्लेटफ़ॉर्म नहीं, AI drafts और answers वाला आसान inbox चाहिए।",
  "किसी प्लेटफ़ॉर्म की ज़रूरत नहीं: ticket के साथ अपने docs पेस्ट करें और सोच-समझकर लिखा, friendly reply draft पाएँ।",
  "वही आइडिया; अपने docs और tone guide एक ChatGPT Project में रखें, ताकि हर draft उसी context से शुरू हो।"]),
 "best-ai-for-scraping": ("Web scraping के लिए बेस्ट AI", "वेबसाइट्स को ऐप्स, रिसर्च और AI pipelines के लिए साफ़ डेटा में बदलें। हर साइट की terms और robots.txt का सम्मान करें।", [
  "Builders के लिए टॉप पिक: एक API call से साइट का साफ़ markdown या structured JSON मिल जाता है।",
  "बेस्ट, जब रेडीमेड scraper पहले से मौजूद हो (maps, social, e-commerce); scheduling बिल्ट-इन।",
  "उन साइट्स के लिए जिन्हें असली logged-in ब्राउज़र या क्लिक करते रहना पड़ता है; इसे Stagehand के साथ इस्तेमाल करें।",
  "असली पेज पर custom scraper लिखता और debug करता है; एक बार वाली या अलग तरह की साइट्स के लिए बेस्ट।",
  "वही काम, आपके एडिटर के अंदर — अच्छा, जब scraper किसी मौजूदा प्रोजेक्ट का हिस्सा हो।"]),
 "best-ai-for-api-testing": ("API testing के लिए बेस्ट AI", "Requests लिखें, tests बनाएँ और फ़ेल हो रहे endpoints debug करें।", [
  "टॉप पिक, अगर आपकी टीम पहले से Postman इस्तेमाल करती है: Agent Mode आपके collections से tests लिखता है, टूटी requests ठीक करता है और APIs का documentation बनाता है।",
  "आपके API कोड के ठीक बगल में test suites (pytest, Jest वगैरह) बनाता और ठीक करता है।",
  "OpenAPI spec या फ़ेल हुआ response पेस्ट करें और वे test cases और edge cases पाएँ जो आपसे छूट गए।",
  "जल्दी वाले test scripts और mock डेटा के लिए अच्छा; चीज़ें आज़माने के लिए Python चला सकता है।",
  "ख़ुद AI नहीं है, पर इसकी सादी फ़ाइलों वाली collections को AI एडिटर्स आसानी से पढ़-लिख लेते हैं। Offline और git-native रहना है तो इसे चुनें।"]),
 "best-ai-for-notion-docs": ("Notes और docs के लिए बेस्ट AI", "AI से अपने notes और टीम docs लिखें, organize करें और सर्च करें।", [
  "टॉप पिक, अगर आपका workspace Notion में है: AI writing, सारे पेजों पर Q&A और meeting notes, सब एक जगह।",
  "Docs की असली लिखाई और एडिटिंग के लिए सबसे अच्छा; Projects reference मटीरियल को हाथ के पास रखते हैं।",
  "Docs का draft बनाने और उन्हें दोबारा structure करने में versatile, पहली outline से पूरे rewrite तक।",
  "इसे चुनें जब आपके docs असल में tables और automations वाले छोटे-छोटे ऐप्स हों।",
  "Personal notes जो अपने-आप organize हो जाते हैं; टीम wikis के लिए छोड़ दें।"]),
}

NEW = {
 "claude-code": "Anthropic का terminal coding agent — सबसे ज़्यादा चर्चा में रहने वाले dev टूल्स में से एक।",
 "codex": "OpenAI का दोबारा लॉन्च हुआ Codex coding agent (cloud + CLI)।",
 "veo": "Google का वीडियो model, जो अब synced audio भी बनाता है।",
 "manus": "Autonomous general agent, जो multi-step टास्क की वजह से वायरल हुआ।",
 "lovable": "तेज़ी से बढ़ता prompt-to-app builder।",
 "notebooklm": "Audio Overviews ने research notes को podcasts में बदल दिया।",
 "kling": "AI वीडियो generation में मज़बूत दावेदार।",
 "deepseek": "Open-weight reasoning models, जिन्होंने pricing में हलचल मचा दी।",
 "mcp": "वह open protocol जिसे अब ज़्यादातर agent टूल्स tools access के लिए सपोर्ट करते हैं।",
 "windsurf": "Agentic एडिटर, जो सीधे Cursor को टक्कर देता है।",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['जनवरी', 'फ़रवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितंबर', 'अक्टूबर', 'नवंबर', 'दिसंबर']
DATE_MD = '{d} {m}'
DATE_MDY = '{d} {m} {y}'
RELEASES = {
 'replit-cloud-agents-repos': 'Replit के Cloud Agents अब आपकी company के मौजूदा GitHub या GitLab repos पर काम करते हैं। team का कोई भी व्यक्ति बदलाव बताता है, agent उसे चल रहे app में test करता है और engineers के review के लिए screenshots और video के साथ pull request खोलता है। Pro और Enterprise plans पर।',
 'gpt-6-1-terra-copilot': 'OpenAI का सबसे नया model अब GitHub Copilot में सबके लिए उपलब्ध है, जो रोज़ की agentic coding और terminal के काम के लिए बना है और GPT-6.1 Sol से कम लागत पर चलता है। Copilot Pro, Pro+, Max, Business और Enterprise पर, धीरे-धीरे rollout हो रहा है।',
 'replit-monitoring-agent': 'Replit का Agent अब published app के alerts पर background में नज़र रखता है, production की समस्याओं की जाँच करता है और fix को test करता है। fix आप खुद review करके publish करते हैं, जब तक आप experimental Auto-republish setting चालू न करें।',
 'cursor-agent-sdk': 'अपना agent code के एक folder के रूप में बनाएँ (prompt, typed tools, skills और MCP connections), evals से test करें और Cursor या अपने servers पर deploy करें। agents GitHub, GitLab, Bitbucket, Slack, webhook या cron events पर चालू हो सकते हैं।',
 'lovable-supabase-create': 'Lovable अब बिना backend वाले app के लिए Supabase project बनाकर उसे जोड़ देता है। organization और region आप चुनते हैं (region बाद में नहीं बदला जा सकता), और Supabase उस project का बिल आपके अपने account में भेजता है।',
 'voxtral-3': 'Mistral के नए speech-to-text और text-to-speech models, साथ में फ़ोन और वेब पर real-time voice agents बनाने के लिए SDK। Mistral की API (EU-hosted विकल्प के साथ) से या self-hosted।',
 'kling-4': 'Kuaishou का नया वीडियो model: एक बार में 30 सेकंड तक के clips, तेज़ मूवमेंट और कैमरा मूव्स में ज़्यादा स्थिरता, और हर टास्क में 15 तक reference assets और 10 keyframes।',
 'muse-spark-open': 'Meta का open-weight model, coding और agent वाले काम के लिए (816B parameters, 42B active, 1M-token context)। Meta इसे दो Mac Studios पर चलाता है; ज़्यादातर लोगों के लिए hosted APIs ही आसान रास्ता हैं।',
 'claude-haiku-5-5': 'Anthropic का सबसे सस्ता और सबसे तेज़ model, ज़्यादा वॉल्यूम वाले काम के लिए बना: support bots, summaries और coding subagents। Anthropic के मुताबिक़ इसे चलाना Haiku 4.5 से लगभग 75% सस्ता है।',
 'nano-banana-2-1': 'Google का अपडेटेड image generation और editing model: बेहतर edits, characters में ज़्यादा consistency और इमेज में साफ़ टेक्स्ट। Gemini ऐप, AI Studio, Gemini API, Flow और Stitch में उपलब्ध।',
 'copilot-dynamic-workflows': 'Multi-agent काम को code में तय करें (parallel steps, एक-दूसरे को जाँचते subagents, review के लिए checkpoints) — Copilot CLI, Copilot ऐप और Copilot SDK में। Public preview, सभी plans में।',
 'heygen-video': 'HeyGen का पहला general-purpose वीडियो model: टेक्स्ट, इमेज या reference media से 5 से 15 सेकंड के clips, जिनमें डायलॉग और आवाज़ साथ में बनते हैं। HeyGen API से उपलब्ध।',
 'gpt-6-1-sol': 'OpenAI DevDay में आया GPT-6 Sol का अपग्रेड, जिसका फ़ोकस agentic coding, computer use और professional काम पर है। OpenAI के मुताबिक़ यह काफ़ी कम क़ीमत पर GPT-6 Astra के क़रीब पहुँचता है।',
 'openai-agents-api-computer-use': 'Agents API अब computer use से software चला सकती है, और Codex के multi-agent फ़ीचर्स, tool search और context compaction आपके ऐप में लाती है। Infrastructure OpenAI चलाता है।',
 'claude-sonnet-5-5': 'Anthropic का तेज़ और सस्ता Sonnet, जो साफ़ दायरे वाले रोज़मर्रा के टास्क और bug fixing में सबसे मज़बूत है। Sonnet 5 से 30%+ तेज़, उसी $2/$10 प्रति million tokens की क़ीमत पर।',
 'lovable-free-chat': 'Lovable से chat अब रोज़ की free सीमा के अंदर मुफ़्त है: features प्लान करें, अपने ऐप के code और database के बारे में पूछें या लॉन्च का टेक्स्ट लिखवाएँ। Build करने पर अब भी credits लगते हैं।',
 'cursor-projects': 'किसी feature या migration जैसे बड़े काम के लिए beta: एक coordinator agent cloud में चलता है, काम प्लान करता है, कई subagents में बाँटता है और समय के साथ shared context बनाए रखता है।',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — किस काम के लिए कौन-सा AI टूल", TAG + " AI टूल्स की चुनिंदा डायरेक्टरी, use case के हिसाब से।", """
<h1>किस काम के लिए कौन-सा AI टूल।</h1><p class="lede">Tool Use Cases AI टूल्स की एक डायरेक्टरी है, जिसे इस हिसाब से बनाया गया है कि आप कौन-सा काम करना चाहते हैं — vibe coders, builders और AI के साथ कुछ भी ship करने वाले हर किसी के लिए।</p>
<input type="search" placeholder="Use cases फ़िल्टर करें (जैसे video, coding, research)…" data-filter=".f" aria-label="Use cases फ़िल्टर करें">
<h2>Use cases</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>नए लॉन्च और ट्रेंडिंग</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">सारे नए लॉन्च देखें →</a></p>"""),
 "use-cases": ("AI टूल use cases — Tool Use Cases", "Use case के हिसाब से AI टूल्स देखें: vibe coding, coding agents, debugging, गेम prototyping, वीडियो, writing, रिसर्च, images और भी बहुत कुछ।", """
<h1>Use cases</h1><p class="lede">काम चुनिए। हम बताएँगे कौन-से टूल आज़माने लायक हैं और क्यों।</p>
<input type="search" placeholder="Use cases फ़िल्टर करें…" data-filter=".f" aria-label="फ़िल्टर करें"><div class="grid">{CARDS}</div>"""),
 "tools": ("सारे AI टूल्स A से Z — Tool Use Cases", "Tool Use Cases डायरेक्टरी का हर AI टूल, वह क्या करता है और किन use cases में फ़िट बैठता है।", """
<h1>सारे टूल्स</h1><input type="search" placeholder="टूल्स फ़िल्टर करें…" data-filter=".f" aria-label="टूल्स फ़िल्टर करें"><div class="grid">{ROWS}</div>"""),
 "new": ("नए और ट्रेंडिंग AI टूल्स — Tool Use Cases", "Builders के लिए ख़ास और ट्रेंडिंग AI टूल लॉन्च: coding agents, वीडियो models, रिसर्च टूल्स और भी बहुत कुछ।", """
<h1>नए लॉन्च और ट्रेंडिंग</h1><p class="lede">पिछले छह हफ़्तों के AI टूल लॉन्च और बड़े अपडेट, जो builders के लिए मायने रखते हैं। हर एक के साथ तारीख़, आधिकारिक घोषणा का लिंक और वह use case दिया है जिसमें यह फ़िट बैठता है।</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Tool Use Cases को स्पॉन्सर करें — अपना AI टूल फ़ीचर कराएँ", "टूल बनाने वाले, सही use-case पेजों के सबसे ऊपर साफ़ तौर पर लेबल किया गया फ़ीचर्ड स्लॉट स्पॉन्सर कर सकते हैं।", """
<h1>किसी use case को स्पॉन्सर करें</h1><p class="lede">Vibe coders और builders तक ठीक उस वक़्त पहुँचें जब वे टूल चुन रहे होते हैं।</p>
<h2>यह कैसे काम करता है</h2><ul><li>हर use-case पेज के सबसे ऊपर एक <b>Sponsored / Featured</b> स्लॉट होता है।</li><li>इस पर हमेशा साफ़ तौर पर "Sponsored" लिखा होता है और यह हमारी editorial पसंद से अलग रहता है।</li><li>हम सिर्फ़ वही टूल लेते हैं जो सच में उस use case में फ़िट बैठते हैं।</li><li>स्पॉन्सरशिप से हमारी राय या रैंकिंग कभी नहीं बदलती।</li></ul>
<h2>उदाहरण</h2>{SPONSOR_CARD}
<div class="cta">कीमत और उपलब्धता के लिए संपर्क करें। <a class="btn" href="{SPONSOR_MAILTO}">स्पॉन्सर करने के लिए ईमेल करें</a></div>"""),
 "about": ("हमारे बारे में — Tool Use Cases", "Tool Use Cases एक स्वतंत्र, autonomously चलने वाली डायरेक्टरी है, जिसमें AI टूल्स use case के हिसाब से रखे गए हैं।", """
<h1>हमारे बारे में</h1><p class="lede">Tool Use Cases एक ही सवाल का जवाब देता है: इस काम के लिए मुझे कौन-सा AI टूल इस्तेमाल करना चाहिए?</p>
<p>ज़्यादातर AI डायरेक्टरीज़ बस लंबी-चौड़ी लिस्ट होती हैं। हम use case के हिसाब से चीज़ें रखते हैं, और हर पसंद के साथ आसान भाषा में छोटी-सी राय देते हैं, ताकि आप एक मिनट में फ़ैसला कर सकें।</p>
<p>यह साइट autonomously चलती है — एक AI operator इसे अपडेट रखता है, और इसकी इंसानी ज़िम्मेदारी Lali Publications की है। हम सिर्फ़ असली, जाने-माने टूल्स ही लिस्ट करते हैं और मनगढ़ंत स्कोर या यूज़र्स की गिनती पब्लिश नहीं करते।</p>
<p>Tool Use Cases को Lali Publications पब्लिश करता है, जो <a href="https://agentusecases.ai">agentusecases.ai</a> भी चलाता है। हम जिन टूल्स को लिस्ट करते हैं उनमें से किसी से हमारा कोई जुड़ाव नहीं है।</p>
<p>यह साइट का हिन्दी वर्ज़न है, जिसमें वही use cases, वही पसंद और वही रैंकिंग है जो <a href="@R/about/index.html" hreflang="en">अंग्रेज़ी वर्ज़न</a> में है।</p>
<p>सुधार या सुझाव के लिए: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("सब्सक्राइब करने के लिए शुक्रिया — Tool Use Cases", "Tool Picks Weekly के लिए आपका साइनअप मिल गया है।", """
<h1>आप लिस्ट में जुड़ गए हैं। शुक्रिया!</h1><p class="lede">Tool Picks Weekly के लिए आपका साइनअप मिल गया है। अगला इश्यू सोमवार को आएगा। अभी न्यूज़लेटर अंग्रेज़ी में आता है।</p>
<p><a class="btn" href="@R/@Pindex.html">Tool Use Cases पर वापस जाएँ</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "AI टूल use cases",
 "uc_coll": ("AI टूल use cases", "Use case के हिसाब से AI टूल्स देखें।"),
 "tools_crumb": "सारे टूल्स", "tools_coll": ("सारे AI टूल्स A से Z", "Tool Use Cases डायरेक्टरी का हर AI टूल।"),
 "new_crumb": "नए लॉन्च और ट्रेंडिंग", "new_coll": ("नए और ट्रेंडिंग AI टूल्स", "Builders के लिए ख़ास और ट्रेंडिंग AI टूल लॉन्च।"),
 "sponsor_crumb": "स्पॉन्सर",
 "about_crumb": "हमारे बारे में", "about_coll": ("Tool Use Cases के बारे में", "AI टूल्स की स्वतंत्र, autonomously चलने वाली डायरेक्टरी, use case के हिसाब से, Lali Publications की ओर से।"),
}
