"""Neutral Latin-American Spanish (es) locale for Tool Use Cases ("tú" form, readable in Mexico and Spain).
Same structure and conventions as i18n/pt_BR.py; see that file's docstring."""
CODE = "es"
PREFIX = "es/"
SHORT = "ES"
NATIVE = "Español"           # language switcher label (own script)
OG_LOCALE = "es_LA"
RSS_LANG = "es"

TAG = "Qué herramienta de IA usar para cada tarea — para vibe coders y builders."

UI = {
 "quick_label": "Respuesta rápida", "quick_top": "{tool} es nuestra opción principal.", "faq_h2": "Preguntas frecuentes",
 "faq_q_top": "{title}: ¿cuál es la opción principal?", "faq_q_alts": "{title}: ¿qué alternativas hay?", "faq_a_alts": "En orden de ranking: {alts}",
 "faq_q_paid": "¿Alguien paga por aparecer en estas recomendaciones?", "faq_a_paid": "No. Las recomendaciones son editoriales y nadie paga por ellas. Cualquier espacio patrocinado está claramente identificado y separado, y el patrocinio nunca cambia nuestros veredictos ni el orden del ranking.",
 "nav_use_cases": "Casos de uso", "nav_tools": "Herramientas", "nav_new": "Lanzamientos",
 "nav_newsletter": "Newsletter", "nav_sponsor": "Patrocinio", "nav_about": "Acerca de",
 "home": "Inicio", "use_cases": "Casos de uso",
 "og_alt": "Tool Use Cases: herramientas de IA clasificadas según la tarea que necesitas resolver",
 "footer": "Tool Use Cases · por Lali Publications · patrocinios:",
 "nl_h2": "Recomendaciones semanales de herramientas de IA para vibe coders",
 "nl_p": "Herramientas nuevas + para qué tarea sirve cada una. Gratis. Por ahora, lo enviamos en inglés.",
 "nl_placeholder": "tu@ejemplo.com", "nl_aria": "Correo electrónico", "nl_button": "Suscribirme",
 "nl_subject": "Tool Use Cases newsletter signup (es)",
 "nl_small": "Enviamos desde Lali Publications. Sin spam; cancela cuando quieras.",
 "nl_latest": "Lee la última edición: {LINK} (en inglés).",
 "verdict": "Veredicto:", "our_picks": "Nuestras recomendaciones", "related": "Casos de uso relacionados",
 "browse_all": "Ver todos los casos de uso →",
 "disclaimer": "Las recomendaciones son editoriales y nadie paga por ellas. Los precios y las funciones cambian a menudo: consulta el sitio oficial de cada herramienta.",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} Veredicto sobre {names} y otras herramientas.",
 "review_name": "{tool} — {title}",
 "sponsored": "Patrocinado", "sponsor_h3": "Tu herramienta aquí",
 "sponsor_p": "Este espacio destacado está disponible para creadores de herramientas que encajan en este caso de uso. Siempre identificado con claridad y siempre separado de nuestras recomendaciones.",
 "sponsor_link": "Patrocinar por email",
 "new_badge": "Destacado / en tendencia",
 "last_checked": 'Última revisión', "byline": 'Publicado por Lali Publications. Recomendaciones investigadas por nuestro editor de IA y verificadas en el sitio oficial de cada herramienta.', "how_we_pick": 'Cómo elegimos',
 "last_updated": 'Última actualización: {date}', "earlier_h2": 'Anteriores', "earlier_p": 'Lanzamientos que destacamos antes de esta actualización. Ya no son novedad, pero vale la pena conocerlos.', "fits": 'Caso de uso:', "source": 'Fuente',
 "rss_title": "Tool Use Cases (español)",
 "rss_desc": "Ediciones de Tool Picks Weekly (en inglés) y lanzamientos de herramientas de IA que vale la pena conocer.",
 "rss_new_prefix": "Nuevo y en tendencia: ", "rss_issue_suffix": " (en inglés)",
 "rss_cat_newsletter": "Newsletter", "rss_cat_new": "Lanzamientos",
 "llms_h2": "En español (es)",
 "llms_intro": "Versión completa del sitio en español, con los mismos casos de uso, recomendaciones y rankings que la versión en inglés.",
 "llms_other": [("Inicio", ""), ("Todas las herramientas de la A a la Z", "tools/"), ("Lanzamientos y tendencias", "new/"), ("Acerca de", "about/"), ("Patrocinio", "sponsor/")],
}

TOOLS = {
 "cursor": "Editor de código pensado para la IA (un fork de VS Code), con chat, ediciones inline y modo agente.",
 "claude": "El asistente de IA de Anthropic, fuerte en documentos largos, escritura y código.",
 "claude-code": "La herramienta de programación agéntica de Anthropic que funciona en la terminal.",
 "chatgpt": "El asistente de IA de uso general de OpenAI, con chat, imágenes, voz y búsqueda.",
 "codex": "El agente de programación de OpenAI que trabaja en repositorios en la nube o desde la CLI.",
 "copilot": "Asistente de programación en pareja con IA, integrado en VS Code, los IDE de JetBrains y GitHub.",
 "v0": "El creador de apps e interfaces con IA de Vercel, que genera apps en React + Tailwind a partir de prompts.",
 "lovable": "Creador de web apps full-stack a partir de prompts, con integración con Supabase.",
 "replit": "IDE en el navegador con un agente que crea apps a partir de un prompt y las despliega.",
 "bolt": "El creador de apps a partir de prompts de StackBlitz, que funciona en el navegador.",
 "windsurf": "Editor de código con IA de Cognition (antes Windsurf): un IDE completo más un centro de control para agentes de código locales y en la nube.",
 "opencode": "Agente de programación open source (MIT) para la terminal, el escritorio o tu IDE, compatible con más de 75 proveedores de modelos, incluidos modelos locales.",
 "devin": "El agente autónomo de ingeniería de software de Cognition.",
 "gemini": "El asistente de IA de Google, con ventanas de contexto enormes e integración con Google.",
 "perplexity": "Motor de respuestas con IA que busca en la web y cita sus fuentes.",
 "notebooklm": "El cuaderno de investigación de Google (antes NotebookLM) que responde a partir de las fuentes que tú mismo subes.",
 "elicit": "Asistente de investigación con IA para encontrar y resumir artículos académicos.",
 "notion-ai": "Escritura y preguntas y respuestas con IA dentro de los workspaces de Notion.",
 "grammarly": "Asistente de escritura para gramática, tono y reescrituras en cualquier lugar donde escribas.",
 "midjourney": "Generador de imágenes conocido por su estética potente y su resultado artístico.",
 "dalle": "La generación de imágenes de OpenAI dentro de ChatGPT, buena para seguir instrucciones y para escribir texto en la imagen.",
 "ideogram": "Generador de imágenes especialmente bueno para poner texto legible en las imágenes.",
 "flux": "Familia de modelos de imagen de alta calidad, algunos con pesos abiertos.",
 "firefly": "Las herramientas de imagen generativa de Adobe, entrenadas para un uso comercial seguro.",
 "sd": "Familia de modelos de imagen abiertos que puedes ejecutar en local (por ejemplo, con ComfyUI).",
 "runway": "Suite de generación y edición de video con IA (modelos de la serie Gen).",
 "elevenlabs": "Locución realista con IA, clonación de voz y doblaje.",
 "descript": "Edita videos y podcasts editando la transcripción.",
 "heygen": "Videos con avatares de IA y traducción de video.",
 "capcut": "Editor de video con plan gratuito; los subtítulos automáticos y la mayoría de las herramientas de IA requieren Pro.",
 "opus": "Convierte videos largos en clips cortos verticales de forma automática.",
 "veo": "El modelo de texto a video de Google DeepMind, con audio nativo.",
 "rosebud": "Herramienta en el navegador para crear juegos a partir de prompts (Three.js/Phaser).",
 "scenario": "Genera arte para juegos con un estilo consistente a partir de tus propios sets de entrenamiento.",
 "meshy": "Generación de modelos 3D a partir de texto o imagen, para assets de juegos.",
 "suno": "Genera canciones completas, útiles como música provisional para juegos y videos.",
 "sentry": "Monitoreo de errores con análisis de causa raíz por IA y sugerencias de corrección.",
 "deepseek": "Laboratorio chino de IA con modelos de razonamiento potentes, baratos y de pesos abiertos.",
 "ollama": "Ejecuta modelos abiertos (Llama, Qwen, etc.) en local con un solo comando.",
 "manus": "Agente autónomo de uso general que navega por la web y completa tareas de varios pasos.",
 "kling": "El generador de video a partir de texto o imagen de Kuaishou.",
 "grok": "El asistente de xAI con búsqueda en tiempo real en X y en la web.",
 "mcp": "Estándar abierto para conectar agentes de IA con herramientas y datos.",
 "n8n": "Automatización de workflows open source con nodos de agente de IA; self-host gratis o usa su nube.",
 "make": "Constructor visual de automatizaciones no-code para escenarios de varios pasos entre miles de apps.",
 "zapier": "La plataforma de automatización no-code con más integraciones, ahora con pasos y agentes de IA.",
 "framer": "Constructor de sitios web para diseñadores, con generación de páginas por IA, CMS y hosting.",
 "stitch": "La herramienta de Google para diseñar UI a partir de prompts (antes Galileo AI), que exporta a Figma y a código.",
 "uizard": "Herramienta de mockups de UI con IA para principiantes; convierte prompts y bocetos en pantallas de apps.",
 "figma": "La herramienta estándar de diseño de UI, con funciones de IA integradas y Figma Make para crear prototipos a partir de prompts.",
 "openai-tts": "La API de voz de OpenAI: voces naturales y baratas que puedes guiar con instrucciones.",
 "lyria": "El modelo de música de Google en la app de Gemini: canciones con voz o instrumentales de hasta unos 3 minutos, descargables en MP3.",
 "aiva": "Compositor con IA para música instrumental, orquestal y bandas sonoras, con exportación a MIDI.",
 "surfer": "Herramienta de SEO y visibilidad en búsquedas con IA (antes SurferSEO), con un editor de contenido que puntúa tus borradores comparándolos con las páginas mejor posicionadas.",
 "clearscope": "Herramienta premium de optimización de contenido, para cobertura de palabras clave y evaluación de contenido.",
 "lavender": "Coach de emails de ventas que puntúa y reescribe tus cold emails dentro de tu bandeja de entrada.",
 "julius": "Chatea con hojas de cálculo y archivos de datos para obtener análisis y gráficos.",
 "excel-copilot": "Copilot dentro de Excel, para fórmulas, análisis y gráficos en tus libros de trabajo.",
 "powerpoint-copilot": "Copilot dentro de PowerPoint: crea una presentación a partir de un prompt o un archivo, agrega diapositivas y reescribe o reorganiza el contenido.",
 "gamma": "Genera presentaciones, documentos y páginas web a partir de un prompt o un esquema.",
 "beautiful-ai": "Software de diapositivas con plantillas inteligentes que se formatean solas a medida que agregas contenido.",
 "rodin": "Generador de 3D a partir de texto o imagen, con topología limpia, materiales PBR y plugins para Blender, Unity y Unreal.",
 "tripo": "Generador rápido de 3D a partir de texto o imagen, con auto-rigging y opciones de topología limpia.",
 "fireflies": "Bot de reuniones con IA que graba, transcribe y resume llamadas de Zoom, Meet y Teams.",
 "otter": "Transcripción de reuniones en tiempo real y resúmenes con IA, con un plan gratuito que realmente sirve.",
 "grain": "Grabador de reuniones centrado en clips y momentos destacados, popular entre equipos de ventas y de atención a clientes.",
 "langchain": "Framework open source para crear apps con LLMs: RAG, herramientas e integraciones.",
 "llamaindex": "Framework open source enfocado en conectar LLMs con tus documentos y datos (RAG).",
 "vercel": "Hosting de frontend y Next.js con deploys al hacer git push, previews y un AI SDK.",
 "netlify": "Hosting basado en git para sitios estáticos y web apps, con functions y formularios.",
 "railway": "Despliega backends, bases de datos y workers desde un repositorio casi sin configuración.",
 "fly": "Ejecuta contenedores Docker cerca de tus usuarios en todo el mundo; bueno para apps full-stack (sin máquinas con GPU desde 2026).",
 "wxt": "Framework open source basado en Vite para crear extensiones de navegador multiplataforma en TypeScript.",
 "canva": "Herramienta de diseño online con las funciones de IA de Magic Studio y plantillas listas para usar.",
 "langgraph": "El framework de LangChain para grafos de agentes con estado, controlables y de varios pasos.",
 "crewai": "Framework open source en Python para equipos de agentes de IA basados en roles.",
 "ms-agent-framework": "El framework open source de agentes de Microsoft para Python y .NET, sucesor de AutoGen y Semantic Kernel.",
 "openai-agents": "El SDK ligero de OpenAI para agentes, con herramientas, handoffs, guardrails y tracing.",
 "recraft": "Generador de imágenes con IA para diseñadores que entrega gráficos vectoriales (SVG) editables e iconos.",
 "looka": "Creador de logos con IA que genera un logo y un brand kit por un pago único.",
 "intercom-fin": "El agente de soporte con IA de Intercom, que resuelve las dudas de tus clientes a partir de tu contenido de ayuda.",
 "zendesk": "Agentes de IA y funciones de asistencia para agentes de soporte, integrados en el help desk de Zendesk.",
 "helpscout": "Bandeja de entrada compartida y help desk sencillos, con borradores y resúmenes por IA y AI Answers.",
 "firecrawl": "API que rastrea sitios web y devuelve markdown limpio o datos estructurados para LLMs.",
 "browserbase": "Navegadores headless alojados para agentes de IA, más el framework open source Stagehand.",
 "apify": "Plataforma de scraping con miles de scrapers listos para usar ('Actors') y programación de tareas.",
 "postman": "Plataforma de APIs para crear y probar requests, con Agent Mode, un modo de IA que trabaja sobre todas tus colecciones.",
 "bruno": "Cliente de APIs open source y offline que guarda las colecciones como archivos simples en git.",
 "coda": "Workspace que mezcla documento y hoja de cálculo (antes Coda), con tablas, automatizaciones e IA integrada.",
 "mem": "App de notas con IA que organiza tus notas automáticamente y te deja chatear con ellas.",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Mejor IA para vibe coding", "Descríbelo, ejecútalo, ajústalo. Herramientas para crear software casi solo conversando.", [
  "La opción por defecto: sigues teniendo una base de código y un editor de verdad, pero la IA escribe la mayor parte.",
  "El camino más rápido de la idea a una web app que funciona, con autenticación y base de datos, sin configurar nada.",
  "Lo mejor cuando quieres una UI pulida en React/Next.js en poco tiempo y piensas hacer deploy en Vercel.",
  "Todo en el navegador, incluido el hosting: bueno para prototipos rápidos y fáciles de compartir.",
  "Parecido a Lovable; excelente para levantar una demo full-stack en una sola pestaña.",
  "Alternativa a Cursor pensada para manejar varios agentes a la vez; vale la pena probarla si Cursor no te convence."]),
 "best-ai-coding-agents": ("Mejores agentes de IA para programar", "Agentes que toman una tarea, editan varios archivos, ejecutan comandos y vuelven con un diff.", [
  "Excelente en cambios que tocan varios archivos, desde la terminal; uno de los favoritos para trabajo agéntico serio.",
  "Modo agente dentro de un editor completo, para que revises cada cambio de forma visual.",
  "Delega tareas para que se ejecuten en paralelo en la nube y revisa los PR resultantes.",
  "El agente de código de Copilot trabaja a partir de issues de GitHub: encaja de forma natural si tu equipo vive en GitHub.",
  "Hecho para delegar tickets completos de principio a fin; más caro y pensado para equipos.",
  "Gratis, open source y en desarrollo activo; usa cualquier modelo, incluso locales, o el plan que ya tienes de Claude, ChatGPT o Copilot."]),
 "best-ai-for-fixing-broken-code": ("Mejor IA para arreglar código roto y errores", "Pega el stack trace y obtén la solución. Herramientas buenas para depurar, no solo para generar código.", [
  "Pega el error junto con los archivos relevantes; es muy bueno para razonar sobre la verdadera causa raíz.",
  "Corrige en el mismo lugar, con todo el contexto del proyecto: sin copiar y pegar de un lado a otro.",
  "Buen depurador en general, y puede ejecutar Python para reproducir los problemas.",
  "'Fix' y '/explain' directamente en el editor, justo donde está el subrayado rojo.",
  "Detecta errores en producción y sugiere correcciones usando traces reales.",
  "Deja que ejecute los tests, lea el fallo e itere hasta que todo esté en verde."]),
 "best-ai-for-game-prototyping": ("Mejor IA para prototipar juegos", "Pon una idea jugable en pantalla rápido: código, arte, 3D y música.", [
  "Crea un juego de navegador a partir de un prompt y haz remix de los juegos de otras personas.",
  "Para motores de verdad (Godot, Unity, Phaser): la IA escribe los scripts y tú haces el playtest.",
  "Mantiene el arte del juego consistente con tu propio estilo: la parte difícil de usar arte con IA en juegos.",
  "Props y personajes 3D rápidos para hacer el blockout de los niveles.",
  "Banda sonora provisional (o final) en minutos.",
  "Diálogos de personajes y efectos de sonido sin necesidad de una cabina de grabación."]),
 "best-ai-for-video-youtube": ("Mejor IA para video y YouTube", "Genera tomas, edita más rápido, ponle voz y córtalo en Shorts.", [
  "Edita videos en los que hablas a cámara como si fueran un documento; elimina las muletillas. Un ahorro de tiempo enorme para youtubers.",
  "Herramientas profesionales de generación y edición de video con IA para b-roll y efectos.",
  "Clips generados de alta calidad, con sonido; muy bueno para b-roll cinematográfico.",
  "Lo mejor de su categoría en locución y doblaje a otros idiomas.",
  "Convierte un video largo o un stream en Shorts/TikToks de forma automática.",
  "El editor práctico del día a día, con un plan gratuito que sí sirve; los subtítulos automáticos ahora requieren Pro.",
  "Presentadores con avatar y traducción con lip sync para cuando no quieres salir en cámara."]),
 "best-ai-writing-assistants": ("Mejores asistentes de escritura con IA", "Redactar, editar y reescribir: documentos, posts de blog, READMEs, emails.", [
  "La prosa que suena más natural entre los grandes asistentes; gran editor.",
  "Todoterreno versátil: borradores, reescrituras y variantes en la misma conversación.",
  "La mejor opción si tus notas y documentos ya están en Notion.",
  "Pule tus textos en cualquier lugar donde escribas: navegador, email, documentos.",
  "Práctico dentro de Google Docs y Gmail."]),
 "best-ai-for-research": ("Mejor IA para investigar", "Encuentra fuentes, léelas y resúmelas, con citas que puedes verificar.", [
  "Respuestas rápidas y con fuentes desde la web en tiempo real; la opción de referencia para investigaciones rápidas.",
  "Sube tus propias fuentes y obtén respuestas basadas en ellas (y resúmenes en audio).",
  "El modo de investigación profunda (deep research) genera informes largos y con fuentes sobre un tema.",
  "Deep Research más la integración con la Búsqueda de Google.",
  "Hecho a medida para artículos académicos y revisiones de literatura.",
  "Útil para saber qué está diciendo la gente ahora mismo en X."]),
 "best-ai-image-generation": ("Mejor IA para generar imágenes", "Miniaturas, arte conceptual, mockups, memes.", [
  "El mejor look de entrada; ideal para arte, moodboards y arte conceptual.",
  "El mejor para seguir instrucciones detalladas y editar conversando.",
  "Elige esta cuando la imagen necesita texto legible: logos, carteles, miniaturas.",
  "Calidad de primer nivel, con opciones de pesos abiertos para usar en local.",
  "Más seguro para trabajo comercial; viene integrado en Photoshop.",
  "Gratis y en local, si tienes una GPU y te gusta experimentar (ComfyUI)."]),
 "best-ai-for-running-local-models": ("Mejores herramientas para ejecutar IA en local", "IA privada y sin pagar por uso, en tu propia máquina.", [
  "Un comando para descargar y ejecutar modelos abiertos; la forma más fácil de empezar.",
  "Modelos potentes de pesos abiertos que puedes ejecutar en local o usar a bajo precio vía API.",
  "Conéctalo a un modelo que corra en Ollama y tendrás un agente de programación offline.",
  "El ecosistema clásico de modelos de imagen locales."]),
 "best-ai-for-automation-workflows": ("Mejor IA para flujos de automatización", "Conecta tus apps y deja que la IA se encargue de los pasos repetitivos: triggers, agentes y código de integración.", [
  "Opción n.º 1 para builders: nodos de agente de IA, código cuando lo necesitas y puedes hacer self-host gratis.",
  "El mejor canvas visual para flujos complejos con ramificaciones; más barato por tarea que Zapier.",
  "La mayor cobertura de apps y la configuración más fácil; evítalo si manejas mucho volumen, porque el precio sube rápido.",
  "Cuando el no-code se queda corto, pídele que escriba el script o el handler del webhook en su lugar.",
  "Para tareas web puntuales de varios pasos; no sustituye a los workflows programados y confiables."]),
 "best-ai-for-landing-pages": ("Mejor IA para landing pages", "De la idea a una landing page publicada y presentable en una tarde.", [
  "Opción n.º 1: genera una página completa con formularios y base de datos a partir de un prompt y publícala con un clic.",
  "Lo mejor si el pulido del diseño y el hosting fácil importan más que la lógica a medida; el equipo de marketing puede editarla después.",
  "Excelente código React/Tailwind si haces deploy en Vercel; conviene tener algo de soltura con el código.",
  "Alternativa full-stack rápida a Lovable; buena para probar una idea rápido.",
  "Olvídate de los builders si ya tienes una base de código: solo agrega la página ahí."]),
 "best-ai-for-ui-design": ("Mejor IA para diseño de UI", "Convierte un prompt o un boceto en pantallas y luego en algo que puedas construir.", [
  "Opción n.º 1 si trabajas con diseñadores: la herramienta estándar, ahora con IA y Figma Make integrados.",
  "Se salta el mockup: genera código de UI funcional que puedes publicar de inmediato.",
  "Exploración de UI a partir de prompts, gratis y rápida, de Google (antes Galileo AI); exporta a Figma.",
  "La más fácil para quienes no son diseñadores y hacen wireframes; evítala si quieres control a nivel de píxel.",
  "Cuando el 'diseño' en realidad tiene que ser una app clicable que funcione."]),
 "best-ai-voice-tts": ("Mejor IA de voz y texto a voz", "Locuciones, narración, voces clonadas y voz para apps, sin micrófono.", [
  "Opción n.º 1: las voces más naturales, clonación y doblaje. La opción por defecto para creadores.",
  "Las voces buenas más baratas para apps y narración a gran escala vía API; menos voces para elegir.",
  "Lo mejor cuando también editas la grabación: corrige palabras mal dichas con tu propia voz clonada.",
  "Cuando también necesitas un avatar que hable o traducción con lip sync."]),
 "best-ai-for-music": ("Mejor IA para música", "Canciones, bandas sonoras y música de fondo a partir de un prompt.", [
  "Opción n.º 1: canciones completas con voz en segundos; la forma más fácil de conseguir algo bueno.",
  "Canciones con voz directamente en la app de Gemini, descargables en MP3; vale la pena probarlo cuando lo que sale de Suno suena genérico.",
  "Lo mejor para música instrumental y orquestal, con exportación a MIDI que puedes editar en un DAW.",
  "Genera música y efectos de sonido además de voz; práctico si ya lo usas."]),
 "best-ai-for-seo-content": ("Mejor IA para contenido SEO", "Investiga, estructura y escribe páginas que puedan posicionar, sin publicar basura generada por IA.", [
  "Opción n.º 1 para la escritura en sí: los borradores más naturales y el mejor editor de tu propio material.",
  "Puntúa tu borrador comparándolo con lo que posiciona; útil como guía, pero no escribas solo para subir la puntuación.",
  "Evaluación de contenido premium para equipos y agencias; excesivo para un sitio de una sola persona.",
  "Investigación rápida y con fuentes sobre un tema y sobre lo que cubre la competencia.",
  "Todoterreno sólido para briefs, esquemas y meta descriptions; investigación profunda (deep research) para detectar huecos de contenido."]),
 "best-ai-for-sales-emails": ("Mejor IA para emails de ventas", "Escribe mejores cold emails y follow-ups: personales, cortos y sin que se note que son de IA.", [
  "Opción n.º 1: dale el contexto del prospecto y obtén un borrador corto que suena humano. Edítalo siempre.",
  "Igual de bueno para borradores y variantes; usa las instrucciones personalizadas para definir tu tono.",
  "Coaching y puntuación directamente en Gmail/Outlook; vale la pena si envías cold emails a diario.",
  "Investigación rápida del prospecto y de la empresa antes de escribir la primera línea.",
  "El pulido final de tono y claridad en cualquier lugar donde escribas."]),
 "best-ai-for-data-spreadsheets": ("Mejor IA para datos y hojas de cálculo", "Analiza CSVs, escribe fórmulas y crea gráficos pidiéndolo en lenguaje natural.", [
  "Opción n.º 1: sube un archivo y la herramienta ejecuta Python de verdad para analizarlo y crear gráficos.",
  "Muy bueno para explicar datos y escribir fórmulas; también puede ejecutar análisis sobre los archivos que subes.",
  "Hecho solo para análisis de datos, con un flujo más amigable para quienes no programan.",
  "Lo mejor cuando el trabajo ya vive en Excel; requiere un plan de Microsoft 365 Copilot.",
  "La opción natural dentro de Google Sheets."]),
 "best-ai-for-presentations": ("Mejor IA para presentaciones", "Del esquema a una presentación decente, en poco tiempo.", [
  "Opción n.º 1: escribe un prompt o pega tus notas y obtén una presentación atractiva en un minuto; exporta a PowerPoint.",
  "Lo mejor para equipos que quieren diapositivas consistentes, fieles a la marca y que no pierden el formato.",
  "Escribe primero la historia y el esquema, o pídele que genere el contenido de las diapositivas y presentaciones hechas con código.",
  "Bueno para esquemas y notas del orador, y puede generar un archivo .pptx descargable.",
  "Tiene sentido si tus presentaciones ya viven en PowerPoint y tu plan de Microsoft 365 incluye Copilot."]),
 "best-ai-for-3d-assets": ("Mejor IA para assets 3D", "Genera props, personajes y modelos a partir de texto o imágenes.", [
  "Opción n.º 1: generación sólida de 3D a partir de texto o imagen, con texturas y exportación para motores de juego.",
  "Generación rápida con auto-rigging; ideal para personajes que necesitas animar.",
  "Texto o imagen a 3D con mucho detalle y topología limpia; sus plugins llevan los modelos directo a Blender, Unity o Unreal.",
  "Lo mejor para assets de juego con un estilo consistente en todo el proyecto.",
  "En juegos 2.5D o de sprites, sáltate el 3D por completo: genera arte conceptual y texturas en local."]),
 "best-ai-for-meeting-notes": ("Mejor IA para notas de reuniones", "Graba, transcribe y resume llamadas para que nadie tenga que tomar notas.", [
  "Opción n.º 1: se une a tus llamadas automáticamente, con buenos resúmenes, búsqueda e integraciones con CRM.",
  "El mejor plan gratuito y transcripción en tiempo real; los resúmenes son un poco más genéricos.",
  "Lo mejor para llamadas de ventas y con clientes en las que quieres compartir clips, no solo notas.",
  "Notas de reuniones integradas si tu equipo ya vive en Notion: sin necesidad de otro bot.",
  "Sin ningún bot: pega una transcripción y obtén resúmenes más precisos y los próximos pasos. Evítalo si quieres grabación automática."]),
 "best-ai-for-chatbots-rag": ("Mejor IA para chatbots y RAG", "Crea un asistente que responda a partir de tus propios documentos: del no-code al código a medida.", [
  "Opción n.º 1 para empezar: un Project de Claude basado en los documentos que subes se convierte en un asistente para tu equipo en minutos. Evítalo si lo necesitas en tu propio sitio.",
  "Un Project de ChatGPT con tus archivos hace el mismo trabajo. Los GPT personalizados se retiran el 11 de diciembre de 2026, así que no empieces uno nuevo.",
  "El mejor framework en código cuando lo difícil es ingerir y recuperar bien tus datos.",
  "El mayor ecosistema de integraciones; más abstracción de la que quizá necesites para bots sencillos.",
  "Pídele que escriba una app de RAG ligera y a medida, y usa MCP para conectarla a tus herramientas.",
  "Preguntas y respuestas basadas en tus fuentes, sin configurar nada; para uso personal, no para integrarlo en otro lugar."]),
 "best-ai-for-deploy-hosting": ("Mejor hosting para apps hechas con IA", "Dónde publicar la app que tus herramientas de IA acaban de crear. Son plataformas de hosting, no herramientas de IA, elegidas por lo bien que encajan con quienes construyen con ayuda de IA.", [
  "Opción n.º 1 para apps Next.js/React (y todo lo que sale de v0): haces push a git y tienes una URL publicada, con previews.",
  "Excelente para sitios estáticos y apps sencillas, con un plan gratuito generoso y formularios integrados.",
  "El lugar más fácil para backends, bases de datos y workers en segundo plano. Evítalo para sitios puramente estáticos.",
  "Lo mejor cuando necesitas Docker o varias regiones; requiere un poco más de configuración. Fly dejó de ofrecer GPUs en 2026.",
  "Crea y aloja en el mismo lugar: lo más sencillo si no quieres tocar nunca la configuración de deploy."]),
 "best-ai-for-chrome-extensions": ("Mejor IA para crear extensiones de Chrome", "Pasa de 'debería haber un botón para esto' a una extensión de navegador que funciona.", [
  "Opción n.º 1: genera el manifest, los scripts y el popup, y corrige errores en contexto mientras recargas y pruebas.",
  "Excelente para crear la estructura base de toda la extensión e iterar sobre los problemas de permisos de Manifest V3.",
  "Sirve para una extensión pequeña de un solo archivo. Revisa que use Manifest V3, porque hay ejemplos antiguos por todas partes.",
  "No es una herramienta de IA, pero combina bien con una: un framework basado en Vite, con mantenimiento activo, que elimina el boilerplate de las extensiones.",
  "Buen autocompletado para las APIs de Chrome si prefieres escribir el código tú mismo."]),
 "best-ai-for-thumbnails-youtube-packaging": ("Mejor IA para miniaturas y títulos de YouTube", "Miniaturas, títulos y el gancho que consigue el clic.", [
  "Opción n.º 1 para miniaturas con texto llamativo y legible integrado en la imagen.",
  "Lo mejor para editar conversando (\"haz que la cara se vea más sorprendida\") y para hacer lluvia de ideas de títulos en el mismo chat.",
  "Donde realmente diseñas la miniatura final: plantillas, eliminación de fondo y las herramientas Magic.",
  "Los fondos y escenas más impactantes; agrega el texto después en Canva.",
  "Haz lluvia de ideas de pares de título y texto para la miniatura; te dice con honestidad cuando una idea huele a clickbait."]),
 "best-ai-for-agent-frameworks": ("Mejores frameworks de agentes de IA", "Frameworks de código para crear tus propios agentes con herramientas, memoria y workflows de varios pasos.", [
  "Opción n.º 1 para empezar: una API pequeña, con herramientas, handoffs y tracing integrados.",
  "Lo mejor cuando necesitas control explícito: estado, reintentos, human-in-the-loop y confiabilidad en producción.",
  "La forma más rápida de prototipar 'crews' multiagente basadas en roles; más difícil de mantener bajo control a escala.",
  "El sucesor de AutoGen y Semantic Kernel de Microsoft: agentes y workflows en grafo con Python o .NET; la opción natural si trabajas en Azure.",
  "No es un framework, pero es la forma estándar de darle herramientas a cualquier agente. Crea tus herramientas como servidores MCP."]),
 "best-ai-for-logos-brand": ("Mejor IA para logos y branding", "Ideas de logo, símbolos de marca y un brand kit inicial, en poco tiempo.", [
  "Opción n.º 1: genera logos e iconos vectoriales de verdad (SVG) que puedes editar y escalar.",
  "Lo mejor para conceptos de logo con el nombre de la marca legible; aun así tendrás que vectorizar el que elijas.",
  "La opción todo en uno más fácil para tener logo y brand kit sin ser diseñador; los resultados pueden parecer de plantilla.",
  "Excelente para explorar el ambiente y la dirección visual de la marca, no para los archivos finales del logo.",
  "Práctico para iterar un concepto conversando. Comprueba que el concepto sea realmente distintivo antes de registrar cualquier marca."]),
 "best-ai-for-customer-support": ("Mejor IA para atención al cliente", "Responde a tus clientes más rápido con agentes de IA y respuestas redactadas por IA.", [
  "Opción n.º 1 para resolver tickets automáticamente; funciona incluso sin el help desk de Intercom. Cobra por resolución, así que lo que pagas crece con el volumen.",
  "La opción natural si ya trabajas con Zendesk; configuración y precios más pesados para equipos pequeños.",
  "Lo mejor para equipos pequeños que quieren una bandeja de entrada sencilla con borradores y respuestas de IA, no una gran plataforma.",
  "Sin plataforma: pega un ticket junto con tu documentación y obtén un borrador de respuesta cuidadoso y amable.",
  "La misma idea; guarda tus documentos y tu guía de tono en un Project de ChatGPT para que cada borrador parta del mismo contexto."]),
 "best-ai-for-scraping": ("Mejor IA para web scraping", "Convierte sitios web en datos limpios para apps, investigación y pipelines de IA. Respeta los términos de cada sitio y su robots.txt.", [
  "Opción n.º 1 para builders: una sola llamada a la API devuelve markdown limpio o JSON estructurado de un sitio.",
  "Lo mejor cuando ya existe un scraper listo para usar (mapas, redes sociales, e-commerce); con programación de tareas integrada.",
  "Para sitios que necesitan un navegador real con sesión iniciada o muchos clics; combínalo con Stagehand.",
  "Escribe y depura un scraper a medida sobre la página real; lo mejor para sitios puntuales o poco comunes.",
  "Lo mismo, dentro de tu editor: bueno cuando el scraper vive en un proyecto existente."]),
 "best-ai-for-api-testing": ("Mejor IA para pruebas de API", "Escribe solicitudes, genera pruebas y depura endpoints que fallan.", [
  "Opción n.º 1 si tu equipo ya usa Postman: Agent Mode escribe tests, arregla requests que fallan y documenta APIs a partir de tus colecciones.",
  "Genera y corrige suites de pruebas (pytest, Jest, etc.) justo al lado del código de tu API.",
  "Pega una spec de OpenAPI o una respuesta que falla y obtén casos de prueba y edge cases que se te pasaron.",
  "Bueno para scripts de prueba rápidos y datos mock; puede ejecutar Python para probar cosas.",
  "No es IA en sí, pero sus colecciones en archivos simples son fáciles de leer y escribir para los editores con IA. Elígelo para trabajar offline y de forma nativa en git."]),
 "best-ai-for-notion-docs": ("Mejor IA para notas y documentos", "Escribe, organiza y busca en tus notas y en los documentos de tu equipo con IA.", [
  "Opción n.º 1 si tu workspace está en Notion: escritura con IA, preguntas y respuestas entre páginas y notas de reuniones en un solo lugar.",
  "El mejor redactor y editor para los documentos en sí; los Projects mantienen el material de referencia a mano.",
  "Versátil para redactar y reestructurar documentos, desde el primer esquema hasta la reescritura completa.",
  "Elígelo cuando tus documentos son en realidad mini apps con tablas y automatizaciones.",
  "Notas personales que se organizan solas; no es para wikis de equipo."]),
}

NEW = {
 "claude-code": "El agente de programación de Anthropic para la terminal: una de las herramientas de desarrollo de las que más se habla.",
 "codex": "El agente de programación Codex, relanzado por OpenAI (nube + CLI).",
 "veo": "El modelo de video de Google, que ahora genera audio sincronizado.",
 "manus": "Agente autónomo de uso general que se hizo viral con sus tareas de varios pasos.",
 "lovable": "Creador de apps a partir de prompts que está creciendo rápido.",
 "notebooklm": "Los resúmenes en audio (Audio Overviews) convirtieron notas de investigación en podcasts.",
 "kling": "Un competidor fuerte en generación de video con IA.",
 "deepseek": "Modelos de razonamiento de pesos abiertos que sacudieron los precios del mercado.",
 "mcp": "El protocolo abierto que ya admiten la mayoría de las herramientas de agentes para acceder a herramientas.",
 "windsurf": "Editor agéntico que compite directamente con Cursor.",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
DATE_MD = '{d} de {m}'
DATE_MDY = '{d} de {m} de {y}'
RELEASES = {
 'voxtral-3': 'Nuevos modelos de speech-to-text y text-to-speech de Mistral, más un SDK de agentes de voz en tiempo real para teléfono y web. Por la API de Mistral (con opción alojada en la UE) o self-hosted.',
 'kling-4': 'Nuevo modelo de video de Kuaishou: clips de hasta 30 segundos de una sola vez, movimientos rápidos y de cámara más estables, y hasta 15 referencias y 10 keyframes por tarea.',
 'muse-spark-open': 'Modelo open-weight de Meta para código y agentes (816B parámetros, 42B activos, contexto de 1M de tokens). Meta lo corre en dos Mac Studio; para la mayoría, las APIs alojadas son la vía práctica.',
 'claude-haiku-5-5': 'El modelo más barato y rápido de Anthropic, pensado para trabajo de alto volumen como bots de soporte, resúmenes y subagentes de código. Según Anthropic, cuesta cerca de un 75% menos que Haiku 4.5.',
 'nano-banana-2-1': 'Modelo actualizado de generación y edición de imágenes de Google, con mejores ediciones, consistencia de personajes y texto en las imágenes. En la app de Gemini, AI Studio, la Gemini API, Flow y Stitch.',
 'copilot-dynamic-workflows': 'Define en código trabajos con varios agentes (pasos en paralelo, subagentes que revisan a otros, checkpoints para que revises) en Copilot CLI, la app de Copilot y el Copilot SDK. Public preview, en todos los planes.',
 'heygen-video': 'El primer modelo de video de uso general de HeyGen: clips de 5 a 15 segundos con diálogo y sonido generados juntos, a partir de texto, una imagen o material de referencia. Disponible por la API de HeyGen.',
 'gpt-6-1-sol': 'La mejora de GPT-6 Sol presentada en el DevDay de OpenAI, enfocada en programación con agentes, computer use y trabajo profesional. OpenAI dice que se acerca a GPT-6 Astra a un precio mucho menor.',
 'openai-agents-api-computer-use': 'La Agents API ahora maneja software con computer use y trae a tu app las funciones multiagente de Codex, tool search y compactación de contexto. OpenAI se encarga de la infraestructura.',
 'claude-sonnet-5-5': 'El Sonnet más rápido y barato de Anthropic, fuerte en tareas cotidianas bien acotadas y en corregir bugs. Más de un 30% más rápido que Sonnet 5, al mismo precio de US$2/US$10 por millón de tokens.',
 'lovable-free-chat': 'Chatear con Lovable ahora es gratis dentro de un cupo diario: planifica funciones, pregunta por el código y la base de datos de tu app o redacta textos de lanzamiento. Construir sigue usando créditos.',
 'cursor-projects': 'Beta para trabajos grandes, como una función o una migración: un agente coordinador corre en la nube, planifica el trabajo, lo reparte entre muchos subagentes y mantiene un contexto compartido con el tiempo.',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — qué herramienta de IA usar para cada tarea", TAG + " Un directorio curado de herramientas de IA organizadas por caso de uso.", """
<h1>Qué herramienta de IA usar para cada tarea.</h1><p class="lede">Tool Use Cases es un directorio de herramientas de IA organizadas según la tarea que quieres resolver: para vibe coders, builders y cualquiera que lanza proyectos con IA.</p>
<input type="search" placeholder="Filtra casos de uso (p. ej., video, código, investigación)…" data-filter=".f" aria-label="Filtrar casos de uso">
<h2>Casos de uso</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>Lanzamientos y tendencias</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">Todos los lanzamientos →</a></p>
<div class="cta"><b>¿Tienes una herramienta de IA?</b> Haz que aparezca destacada en lo alto del caso de uso en el que mejor funciona. <a class="btn" href="@R/@Psponsor/index.html">Patrocinar un espacio</a></div>"""),
 "use-cases": ("Casos de uso de herramientas de IA — Tool Use Cases", "Explora herramientas de IA por caso de uso: vibe coding, agentes de código, depuración, juegos, video, escritura, investigación, imágenes y más.", """
<h1>Casos de uso</h1><p class="lede">Elige la tarea. Te decimos qué herramientas vale la pena probar y por qué.</p>
<input type="search" placeholder="Filtra casos de uso…" data-filter=".f" aria-label="Filtrar"><div class="grid">{CARDS}</div>"""),
 "tools": ("Todas las herramientas de IA de la A a la Z — Tool Use Cases", "Todas las herramientas de IA del directorio Tool Use Cases, con lo que hace cada una y en qué casos de uso encaja.", """
<h1>Todas las herramientas</h1><input type="search" placeholder="Filtra herramientas…" data-filter=".f" aria-label="Filtrar herramientas"><div class="grid">{ROWS}</div>"""),
 "new": ("Herramientas de IA nuevas y en tendencia — Tool Use Cases", "Lanzamientos de herramientas de IA destacados y en tendencia para builders: agentes de código, modelos de video, investigación y más.", """
<h1>Lanzamientos y tendencias</h1><p class="lede">Lanzamientos y actualizaciones importantes de herramientas de IA de las últimas seis semanas que importan a quienes construyen. Cada uno lleva su fecha, el enlace al anuncio oficial y el caso de uso en el que encaja.</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Patrocina Tool Use Cases — destaca tu herramienta de IA", "Los creadores de herramientas pueden patrocinar un espacio destacado, siempre identificado, en lo alto de las páginas de casos de uso relevantes.", """
<h1>Patrocina un caso de uso</h1><p class="lede">Llega a vibe coders y builders justo cuando están eligiendo una herramienta.</p>
<h2>Cómo funciona</h2><ul><li>Un espacio <b>Patrocinado / Destacado</b> aparece en lo alto de cada página de caso de uso.</li><li>Siempre está identificado claramente como "Patrocinado" y separado de nuestras recomendaciones editoriales.</li><li>Solo aceptamos herramientas que realmente encajan en el caso de uso.</li><li>El patrocinio nunca cambia nuestros veredictos ni nuestros rankings.</li></ul>
<h2>Ejemplo</h2>{SPONSOR_CARD}
<div class="cta">Precios y disponibilidad bajo consulta. <a class="btn" href="{SPONSOR_MAILTO}">Patrocinar por email</a></div>"""),
 "about": ("Acerca de — Tool Use Cases", "Tool Use Cases es un directorio independiente, gestionado de forma autónoma, de herramientas de IA organizadas por caso de uso.", """
<h1>Acerca de</h1><p class="lede">Tool Use Cases responde a una sola pregunta: ¿qué herramienta de IA debería usar para esta tarea?</p>
<p>La mayoría de los directorios de IA son listas gigantes. Nosotros organizamos por caso de uso y damos a cada recomendación un veredicto breve y en lenguaje sencillo, para que puedas decidir en un minuto.</p>
<p>El sitio se gestiona de forma autónoma: un operador de IA lo mantiene actualizado, y la responsabilidad humana del proyecto es de Lali Publications. Solo incluimos herramientas reales y conocidas, y no publicamos puntuaciones ni cifras de usuarios inventadas.</p>
<p>Tool Use Cases es una publicación de Lali Publications, que también gestiona <a href="https://agentusecases.ai">agentusecases.ai</a>. Nadie paga por aparecer en nuestras recomendaciones: no tenemos relación con ninguna de las herramientas que listamos, y los patrocinios nunca cambian los rankings.</p>
<p>Esta es la versión en español del sitio, con los mismos casos de uso, recomendaciones y rankings que la <a href="@R/about/index.html" hreflang="en">versión en inglés</a>.</p>
<h2 id="how-we-pick">Cómo elegimos</h2><ul>
<li><b>Una página por tarea.</b> Cada caso de uso lista entre 5 y 7 herramientas muy usadas para esa tarea, ordenadas según lo bien que encajan. La primera es nuestra recomendación principal, con un veredicto de una línea que dice para quién es.</li>
<li><b>Solo productos reales y vigentes.</b> Cada recomendación enlaza a su sitio oficial. Comprobamos que el producto sigue existiendo con ese nombre y que el enlace funciona sin redirecciones. Si una herramienta cambia de nombre, cierra o deja de mantenerse, la renombramos o la sustituimos. Por ejemplo, el 22 de octubre de 2026 sustituimos Udio, Luma Genie, Aider, Plasmo y AutoGen, y renombramos Windsurf, NotebookLM y Coda.</li>
<li><b>Fuentes.</b> Usamos páginas oficiales de producto, documentación, changelogs y páginas de precios. No publicamos puntuaciones, benchmarks, cifras de usuarios ni citas que no hayamos verificado.</li>
<li><b>Lo que no afirmamos.</b> No hemos hecho pruebas formales comparativas. Los veredictos resumen para qué está pensada cada herramienta según su documentación oficial.</li>
<li><b>Precios.</b> Cuando una página muestra un precio o un plan gratuito, lo copiamos de la página oficial de precios en la fecha indicada. Los precios cambian a menudo: manda siempre la página oficial.</li>
<li><b>Fechas.</b> Cada caso de uso muestra la «Última revisión»: la fecha en que volvimos a verificar todas sus recomendaciones.</li>
<li><b>Quién.</b> Un editor de IA hace la investigación y las actualizaciones. El sitio es propiedad de Lali Publications, que lo publica y fija estas reglas. Nadie paga por las recomendaciones y no usamos enlaces de afiliado.</li>
</ul>
<p>Correcciones, sugerencias o patrocinios: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("Gracias por suscribirte — Tool Use Cases", "Recibimos tu suscripción a Tool Picks Weekly.", """
<h1>Ya estás en la lista. ¡Gracias!</h1><p class="lede">Recibimos tu suscripción a Tool Picks Weekly. La próxima edición llega el lunes. Por ahora, la enviamos en inglés.</p>
<p><a class="btn" href="@R/@Pindex.html">Volver a Tool Use Cases</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "Casos de uso de herramientas de IA",
 "uc_coll": ("Casos de uso de herramientas de IA", "Explora herramientas de IA por caso de uso."),
 "tools_crumb": "Todas las herramientas", "tools_coll": ("Todas las herramientas de IA de la A a la Z", "Todas las herramientas de IA del directorio Tool Use Cases."),
 "new_crumb": "Lanzamientos y tendencias", "new_coll": ("Herramientas de IA nuevas y en tendencia", "Lanzamientos de herramientas de IA destacados y en tendencia para builders."),
 "sponsor_crumb": "Patrocinio",
 "about_crumb": "Acerca de", "about_coll": ("Acerca de Tool Use Cases", "Directorio independiente y gestionado de forma autónoma de herramientas de IA organizadas por caso de uso, publicado por Lali Publications."),
}
