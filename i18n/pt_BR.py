"""Brazilian Portuguese (pt-BR) locale for Tool Use Cases.

To add a language: copy this file (e.g. es.py), translate every value, keep every key,
and register it in LOCALES in build.py. build.py checks that every tool, use case,
verdict and new-release note is present and in the same order as the English source.
Body templates may use: @R/ (site root), @P (this locale's prefix, e.g. "pt/"),
{EMAIL}, {SPONSOR_CARD}, {NL_FORM}, {CARDS}, {NEWTEASER}, {ROWS}, {NEWCARDS}, {LAST_UPDATED}, {EARLIER_H2}, {EARLIER_P}, {EARLIER}, {SPONSOR_MAILTO}.
"""
CODE = "pt-BR"            # <html lang> and hreflang
PREFIX = "pt/"            # URL prefix
SHORT = "PT"              # language switcher label
NATIVE = "Português"           # language switcher label (own script)
OG_LOCALE = "pt_BR"
RSS_LANG = "pt-br"

TAG = "Qual ferramenta de IA usar para cada tarefa — para vibe coders e builders."

UI = {
 "nav_use_cases": "Casos de uso", "nav_tools": "Ferramentas", "nav_new": "Lançamentos",
 "nav_newsletter": "Newsletter", "nav_sponsor": "Patrocínio", "nav_about": "Sobre",
 "home": "Início", "use_cases": "Casos de uso",
 "og_alt": "Tool Use Cases: ferramentas de IA ranqueadas pela tarefa que você precisa resolver",
 "footer": "Tool Use Cases · por Lali Publications · patrocínios:",
 "nl_h2": "Indicações semanais de ferramentas de IA para vibe coders",
 "nl_p": "Ferramentas novas + para qual tarefa cada uma serve. Grátis. Por enquanto, a newsletter é enviada em inglês.",
 "nl_placeholder": "voce@exemplo.com", "nl_aria": "Endereço de e-mail", "nl_button": "Assinar",
 "nl_subject": "Tool Use Cases newsletter signup (pt-BR)",
 "nl_small": "Enviamos pela Lali Publications. Sem spam, cancele quando quiser.",
 "nl_latest": "Leia a última edição: {LINK} (em inglês).",
 "verdict": "Veredito:", "our_picks": "Nossas escolhas", "related": "Casos de uso relacionados",
 "browse_all": "Ver todos os casos de uso →",
 "disclaimer": "As escolhas são editoriais e não são pagas. Preços e recursos mudam com frequência — confira o site oficial de cada ferramenta.",
 "uc_title": "{title} (2026) — Tool Use Cases",
 "uc_desc": "{blurb} Veredito sobre {names} e outras ferramentas.",
 "review_name": "{tool} — {title}",
 "sponsored": "Patrocinado", "sponsor_h3": "Sua ferramenta aqui",
 "sponsor_p": "Este espaço em destaque está disponível para criadores de ferramentas que se encaixam neste caso de uso. Sempre identificado com clareza e sempre separado das nossas escolhas.",
 "sponsor_link": "Patrocinar por e-mail",
 "new_badge": "Em destaque / em alta",
 "last_checked": 'Última verificação', "byline": 'Publicado pela Lali Publications. Recomendações pesquisadas pelo nosso editor de IA e conferidas no site oficial de cada ferramenta.', "how_we_pick": 'Como escolhemos',
 "last_updated": 'Atualizado em {date}', "earlier_h2": 'Anteriores', "earlier_p": 'Lançamentos que destacamos antes desta atualização. Não são mais novidade, mas ainda vale conhecer.', "fits": 'Caso de uso:', "source": 'Fonte',
 "rss_title": "Tool Use Cases (português)",
 "rss_desc": "Edições da Tool Picks Weekly (em inglês) e lançamentos de ferramentas de IA que merecem atenção.",
 "rss_new_prefix": "Novo e em alta: ", "rss_issue_suffix": " (em inglês)",
 "rss_cat_newsletter": "Newsletter", "rss_cat_new": "Lançamentos",
 "llms_h2": "Em português (pt-BR)",
 "llms_intro": "Versão completa do site em português brasileiro, com os mesmos casos de uso, escolhas e rankings da versão em inglês.",
 "llms_other": [("Início", ""), ("Todas as ferramentas de A a Z", "tools/"), ("Lançamentos e tendências", "new/"), ("Sobre", "about/"), ("Patrocínio", "sponsor/")],
}

TOOLS = {
 "cursor": "Editor de código pensado para IA (um fork do VS Code), com chat, edição inline e modo agente.",
 "claude": "Assistente de IA da Anthropic, forte em documentos longos, escrita e código.",
 "claude-code": "Ferramenta de programação agêntica da Anthropic que roda no terminal.",
 "chatgpt": "Assistente de IA de uso geral da OpenAI, com chat, imagens, voz e busca.",
 "codex": "Agente de programação da OpenAI que trabalha em repositórios na nuvem ou pela CLI.",
 "copilot": "Assistente de programação em par com IA, integrado ao VS Code, às IDEs da JetBrains e ao GitHub.",
 "v0": "Construtor de apps e UIs com IA da Vercel, que gera apps em React + Tailwind a partir de prompts.",
 "lovable": "Construtor de web apps full-stack a partir de prompts, com integração com o Supabase.",
 "replit": "IDE no navegador com um agente que cria apps a partir de um prompt e faz o deploy.",
 "bolt": "Construtor de apps a partir de prompts da StackBlitz, que roda no navegador.",
 "windsurf": "Editor de código com IA da Cognition (antigo Windsurf): uma IDE completa mais uma central para rodar agentes de código locais e na nuvem.",
 "opencode": "Agente de programação open source (MIT) para terminal, desktop ou IDE, que funciona com mais de 75 provedores de modelos, inclusive modelos locais.",
 "devin": "Agente autônomo de engenharia de software da Cognition.",
 "gemini": "Assistente de IA do Google, com janelas de contexto enormes e integração com o Google.",
 "perplexity": "Mecanismo de respostas com IA que pesquisa na web e cita as fontes.",
 "notebooklm": "Caderno de pesquisa do Google (antigo NotebookLM) que responde com base nas fontes que você envia.",
 "elicit": "Assistente de pesquisa com IA para encontrar e resumir artigos acadêmicos.",
 "notion-ai": "Escrita e perguntas e respostas com IA dentro dos workspaces do Notion.",
 "grammarly": "Assistente de escrita para gramática, tom e reescritas em qualquer lugar onde você digita.",
 "midjourney": "Gerador de imagens conhecido pelo resultado estético e artístico forte.",
 "dalle": "Geração de imagens da OpenAI dentro do ChatGPT, boa em seguir instruções e em escrever texto na imagem.",
 "ideogram": "Gerador de imagens especialmente bom em colocar texto legível nas imagens.",
 "flux": "Família de modelos de imagem de alta qualidade, alguns com pesos abertos.",
 "firefly": "Ferramentas de imagem generativa da Adobe, treinadas para uso comercial seguro.",
 "sd": "Família de modelos de imagem abertos que você pode rodar localmente (por exemplo, via ComfyUI).",
 "runway": "Suíte de geração e edição de vídeo com IA (modelos da série Gen).",
 "elevenlabs": "Locução realista com IA, clonagem de voz e dublagem.",
 "descript": "Edite vídeos e podcasts editando a transcrição.",
 "heygen": "Vídeos com avatares de IA e tradução de vídeo.",
 "capcut": "Editor de vídeo com plano gratuito; legendas automáticas e a maioria das ferramentas de IA exigem o Pro.",
 "opus": "Transforma vídeos longos em clipes curtos na vertical, automaticamente.",
 "veo": "Modelo de texto para vídeo do Google DeepMind, com áudio nativo.",
 "rosebud": "Ferramenta no navegador para criar jogos a partir de prompts (Three.js/Phaser).",
 "scenario": "Gera arte de jogo com estilo consistente a partir dos seus próprios conjuntos de treino.",
 "meshy": "Geração de modelos 3D a partir de texto ou imagem, para assets de jogos.",
 "suno": "Gera músicas completas, úteis como trilha provisória para jogos e vídeos.",
 "sentry": "Monitoramento de erros com análise de causa raiz por IA e sugestões de correção.",
 "deepseek": "Laboratório chinês de IA com modelos de raciocínio fortes, baratos e com pesos abertos.",
 "ollama": "Rode modelos abertos (Llama, Qwen etc.) localmente com um único comando.",
 "manus": "Agente autônomo de uso geral que navega na web e conclui tarefas de várias etapas.",
 "kling": "Gerador de vídeo a partir de texto ou imagem, da Kuaishou.",
 "grok": "Assistente da xAI com busca em tempo real no X e na web.",
 "mcp": "Padrão aberto para conectar agentes de IA a ferramentas e dados.",
 "n8n": "Automação de workflows open source com nodes de agente de IA; self-host grátis ou use a nuvem deles.",
 "make": "Construtor visual de automações no-code para cenários de várias etapas entre milhares de apps.",
 "zapier": "A plataforma de automação no-code com mais integrações, agora com etapas e agentes de IA.",
 "framer": "Construtor de sites para designers, com geração de páginas por IA, CMS e hospedagem.",
 "stitch": "Ferramenta do Google para criar UI a partir de prompts (antigo Galileo AI), que exporta para o Figma e para código.",
 "uizard": "Ferramenta de mockups de UI com IA para iniciantes; transforma prompts e esboços em telas de app.",
 "figma": "A ferramenta padrão de design de UI, com recursos de IA integrados e o Figma Make para criar protótipos a partir de prompts.",
 "openai-tts": "API de voz da OpenAI: vozes naturais e baratas que você pode direcionar com instruções.",
 "lyria": "O modelo de música do Google no app Gemini: músicas com vocais ou instrumentais de até uns 3 minutos, para baixar em MP3.",
 "aiva": "Compositor com IA para música instrumental, orquestral e trilhas sonoras, com exportação em MIDI.",
 "surfer": "Ferramenta de SEO e visibilidade em buscas com IA (antigo SurferSEO), com um editor de conteúdo que dá nota aos rascunhos comparando com as páginas mais bem ranqueadas.",
 "clearscope": "Ferramenta premium de otimização de conteúdo, para cobertura de palavras-chave e avaliação de conteúdo.",
 "lavender": "Coach de e-mails de vendas que dá nota e reescreve cold e-mails dentro da sua caixa de entrada.",
 "julius": "Converse com planilhas e arquivos de dados para obter análises e gráficos.",
 "excel-copilot": "O Copilot dentro do Excel, para fórmulas, análises e gráficos nas suas planilhas.",
 "powerpoint-copilot": "O Copilot dentro do PowerPoint: cria uma apresentação a partir de um prompt ou arquivo, adiciona slides e reescreve ou reorganiza o conteúdo.",
 "gamma": "Gera apresentações, documentos e páginas web a partir de um prompt ou de um roteiro.",
 "beautiful-ai": "Software de slides com templates inteligentes que se formatam sozinhos conforme você adiciona conteúdo.",
 "rodin": "Gerador de 3D a partir de texto ou imagem, com topologia limpa, materiais PBR e plugins para Blender, Unity e Unreal.",
 "tripo": "Gerador rápido de 3D a partir de texto ou imagem, com auto-rigging e opções de topologia limpa.",
 "fireflies": "Bot de reuniões com IA que grava, transcreve e resume chamadas no Zoom, Meet e Teams.",
 "otter": "Transcrição de reuniões em tempo real e resumos com IA, com um plano gratuito que dá para usar de verdade.",
 "grain": "Gravador de reuniões centrado em clipes e destaques, popular entre times de vendas e de relacionamento com clientes.",
 "langchain": "Framework open source para criar apps com LLMs: RAG, ferramentas e integrações.",
 "llamaindex": "Framework open source focado em conectar LLMs aos seus documentos e dados (RAG).",
 "vercel": "Hospedagem de frontend e Next.js com deploy via git push, previews e um AI SDK.",
 "netlify": "Hospedagem baseada em git para sites estáticos e web apps, com functions e formulários.",
 "railway": "Faça deploy de backends, bancos de dados e workers a partir de um repositório, quase sem configuração.",
 "fly": "Rode containers Docker perto dos usuários, no mundo todo; bom para apps full-stack (sem máquinas com GPU desde 2026).",
 "wxt": "Framework open source baseado em Vite para criar extensões de navegador multiplataforma em TypeScript.",
 "canva": "Ferramenta de design online com os recursos de IA do Magic Studio e templates prontos.",
 "langgraph": "Framework da LangChain para grafos de agentes com estado, controláveis e de várias etapas.",
 "crewai": "Framework open source em Python para times de agentes de IA baseados em papéis.",
 "ms-agent-framework": "Framework open source de agentes da Microsoft para Python e .NET, sucessor do AutoGen e do Semantic Kernel.",
 "openai-agents": "SDK leve da OpenAI para agentes, com ferramentas, handoffs, guardrails e tracing.",
 "recraft": "Gerador de imagens com IA para designers que entrega gráficos vetoriais (SVG) editáveis e ícones.",
 "looka": "Criador de logos com IA que gera um logo e um brand kit por um pagamento único.",
 "intercom-fin": "Agente de suporte com IA da Intercom que resolve as dúvidas dos clientes usando o seu conteúdo de ajuda.",
 "zendesk": "Agentes de IA e recursos de apoio aos atendentes integrados ao help desk da Zendesk.",
 "helpscout": "Caixa de entrada compartilhada e help desk simples, com rascunhos e resumos por IA e o AI Answers.",
 "firecrawl": "API que rastreia sites e devolve markdown limpo ou dados estruturados para LLMs.",
 "browserbase": "Navegadores headless hospedados para agentes de IA, mais o framework open source Stagehand.",
 "apify": "Plataforma de scraping com milhares de scrapers prontos ('Actors') e agendamento.",
 "postman": "Plataforma de APIs para montar e testar requisições, com o Agent Mode, um modo de IA que trabalha em todas as suas coleções.",
 "bruno": "Cliente de API open source e offline que guarda as coleções como arquivos simples no git.",
 "coda": "Workspace que mistura documento e planilha (antigo Coda), com tabelas, automações e IA integrada.",
 "mem": "App de notas com IA que organiza as notas automaticamente e deixa você conversar com elas.",
}

UC = {  # slug: (title, blurb, [verdicts in the same order as the English picks])
 "best-ai-for-vibe-coding": ("Melhor IA para vibe coding", "Descreva, rode, ajuste. Ferramentas para criar software basicamente conversando.", [
  "A escolha padrão: você continua com um codebase e um editor de verdade, mas quem digita a maior parte é a IA.",
  "O caminho mais rápido da ideia a um web app funcionando, com autenticação e banco de dados, sem configurar nada.",
  "Melhor quando você quer uma UI caprichada em React/Next.js rapidamente e pretende fazer o deploy na Vercel.",
  "Tudo no navegador, inclusive a hospedagem — bom para protótipos rápidos e fáceis de compartilhar.",
  "Parecido com o Lovable; ótimo para subir uma demo full-stack em uma aba só.",
  "Alternativa ao Cursor pensada para rodar vários agentes ao mesmo tempo; vale testar se você não se deu bem com o Cursor."]),
 "best-ai-coding-agents": ("Melhores agentes de IA para programação", "Agentes que pegam uma tarefa, editam vários arquivos, rodam comandos e voltam com um diff.", [
  "Excelente em mudanças que envolvem vários arquivos, direto do terminal; um dos favoritos para trabalho agêntico sério.",
  "Modo agente dentro de um editor completo, para você revisar cada mudança visualmente.",
  "Delegue tarefas para rodar em paralelo na nuvem e revise os PRs que saem delas.",
  "O agente de código do Copilot trabalha a partir de issues do GitHub — encaixe natural se o seu time vive no GitHub.",
  "Feito para delegar tickets inteiros de ponta a ponta; mais caro e voltado para times.",
  "Gratuito, open source e em desenvolvimento ativo; use qualquer modelo, inclusive locais, ou o plano que você já tem do Claude, ChatGPT ou Copilot."]),
 "best-ai-for-fixing-broken-code": ("Melhor IA para corrigir código quebrado e erros", "Cole o stack trace e receba a correção. Ferramentas boas em debugar, não só em gerar código.", [
  "Cole o erro junto com os arquivos relevantes; é forte em raciocinar sobre a verdadeira causa raiz.",
  "Corrige ali mesmo, com o contexto completo do projeto — sem ficar copiando e colando para lá e para cá.",
  "Bom para debug em geral, e consegue rodar Python para reproduzir os problemas.",
  "'Fix' e '/explain' direto no editor, bem onde está o sublinhado vermelho.",
  "Pega erros em produção e sugere correções usando traces reais.",
  "Deixe ele rodar os testes, ler a falha e iterar até ficar tudo verde."]),
 "best-ai-for-game-prototyping": ("Melhor IA para prototipar jogos", "Coloque uma ideia jogável na tela rápido — código, arte, 3D e música.", [
  "Crie um jogo de navegador a partir de um prompt e faça remix dos jogos de outras pessoas.",
  "Para engines de verdade (Godot, Unity, Phaser): a IA escreve os scripts e você faz o playtest.",
  "Mantém a arte do jogo consistente no seu próprio estilo — a parte difícil de usar arte de IA em jogos.",
  "Props e personagens 3D rápidos para fazer o blockout das fases.",
  "Trilha sonora provisória (ou final) em minutos.",
  "Falas de personagens e efeitos sonoros sem precisar de cabine de gravação."]),
 "best-ai-for-video-youtube": ("Melhor IA para vídeo e YouTube", "Gere cenas, edite mais rápido, coloque voz e corte tudo em Shorts.", [
  "Edite vídeos em que você fala para a câmera como se fosse um documento; remove os vícios de linguagem. Uma economia de tempo enorme para youtubers.",
  "Ferramentas profissionais de geração e edição de vídeo com IA para b-roll e efeitos.",
  "Clipes gerados de alta qualidade, com som; forte para b-roll cinematográfico.",
  "O melhor da categoria em locução e dublagem para outros idiomas.",
  "Transforma um vídeo longo ou uma live em Shorts/TikToks automaticamente.",
  "O editor prático do dia a dia, com um plano gratuito que dá para usar; as legendas automáticas agora exigem o Pro.",
  "Apresentadores em avatar e tradução com lip sync para quando você não quer aparecer na câmera."]),
 "best-ai-writing-assistants": ("Melhores assistentes de escrita com IA", "Rascunhar, editar e reescrever — documentos, posts de blog, READMEs, e-mails.", [
  "O texto que soa mais natural entre os grandes assistentes; ótimo editor.",
  "Versátil e bom em tudo: rascunhos, reescritas e variações na mesma conversa.",
  "A melhor opção se suas notas e documentos já estão no Notion.",
  "Dá um polimento no texto em qualquer lugar onde você digita — navegador, e-mail, documentos.",
  "Prático dentro do Google Docs e do Gmail."]),
 "best-ai-for-research": ("Melhor IA para pesquisa", "Encontre fontes, leia e resuma — com citações que você pode conferir.", [
  "Respostas rápidas e com fontes, direto da web em tempo real; a opção de sempre para pesquisas rápidas.",
  "Envie suas próprias fontes e receba respostas baseadas nelas (e resumos em áudio).",
  "O modo de pesquisa aprofundada (deep research) gera relatórios longos e com fontes sobre um tema.",
  "Deep Research mais a integração com a Pesquisa Google.",
  "Feito sob medida para artigos acadêmicos e revisões de literatura.",
  "Útil para saber o que as pessoas estão falando agora no X."]),
 "best-ai-image-generation": ("Melhor IA para gerar imagens", "Thumbnails, arte conceitual, mockups, memes.", [
  "O melhor visual de cara; ótimo para arte, moodboards e arte conceitual.",
  "O melhor em seguir instruções detalhadas e em editar conversando.",
  "Escolha este quando a imagem precisa de texto legível — logos, pôsteres, thumbnails.",
  "Qualidade de primeira, com opções de pesos abertos para rodar localmente.",
  "Mais seguro para trabalho comercial; vem integrado ao Photoshop.",
  "Grátis e local, se você tem uma GPU e curte fuçar (ComfyUI)."]),
 "best-ai-for-running-local-models": ("Melhores ferramentas para rodar IA localmente", "IA privada e sem custo de uso, na sua própria máquina.", [
  "Um comando para baixar e rodar modelos abertos; o jeito mais fácil de começar.",
  "Modelos fortes com pesos abertos que você pode rodar localmente ou usar a baixo custo via API.",
  "Conecte a um modelo rodando no Ollama e tenha um agente de código offline.",
  "O ecossistema clássico de modelos de imagem locais."]),
 "best-ai-for-automation-workflows": ("Melhor IA para fluxos de automação", "Conecte seus apps e deixe a IA cuidar das etapas repetitivas — triggers, agentes e código de integração.", [
  "Escolha nº 1 para builders: nodes de agente de IA, código quando você precisa, e dá para fazer self-host de graça.",
  "O melhor canvas visual para fluxos complexos e cheios de ramificações; mais barato por tarefa que o Zapier.",
  "A maior cobertura de apps e a configuração mais fácil; evite se o seu volume é alto, porque os custos sobem rápido.",
  "Quando o no-code bater no limite, peça para ele escrever o script ou o handler do webhook em vez disso.",
  "Para tarefas pontuais na web com várias etapas; não substitui workflows agendados e confiáveis."]),
 "best-ai-for-landing-pages": ("Melhor IA para landing pages", "Da ideia a uma landing page no ar e com cara decente em uma tarde.", [
  "Escolha nº 1: gere uma página completa com formulários e banco de dados a partir de um prompt e publique com um clique.",
  "Melhor opção se o acabamento do design e a hospedagem fácil importam mais que lógica sob medida; o pessoal de marketing consegue editar depois.",
  "Ótimo código React/Tailwind se você faz deploy na Vercel; é bom ter alguma intimidade com código.",
  "Alternativa full-stack rápida ao Lovable; boa para testar uma ideia rápido.",
  "Deixe os builders de lado quando você já tem um codebase — é só criar a página nele."]),
 "best-ai-for-ui-design": ("Melhor IA para design de UI", "Transforme um prompt ou esboço em telas e, depois, em algo que dá para construir.", [
  "Escolha nº 1 se você trabalha com designers: a ferramenta padrão, agora com IA e o Figma Make integrados.",
  "Pula o mockup: gera código de UI funcionando que você pode colocar no ar na hora.",
  "Exploração de UI a partir de prompts, grátis e rápida, do Google (antigo Galileo AI); exporta para o Figma.",
  "O mais fácil para quem não é designer fazer wireframes; evite se você quer controle no nível do pixel.",
  "Quando o 'design' na verdade precisa ser um app clicável e funcionando."]),
 "best-ai-voice-tts": ("Melhor IA de voz e texto para fala", "Locuções, narração, vozes clonadas e fala para apps, sem microfone.", [
  "Escolha nº 1: as vozes mais naturais, clonagem e dublagem. O padrão para criadores de conteúdo.",
  "As vozes boas mais baratas para apps e narração em grande volume via API; menos opções de voz.",
  "Melhor quando você também está editando a gravação — corrija palavras que saíram erradas com a sua própria voz clonada.",
  "Quando você também precisa de um avatar falando ou de tradução com lip sync."]),
 "best-ai-for-music": ("Melhor IA para música", "Músicas, trilhas sonoras e música de fundo a partir de um prompt.", [
  "Escolha nº 1: músicas completas com vocal em segundos; o jeito mais fácil de chegar em algo bom.",
  "Músicas com vocais direto no app Gemini, para baixar em MP3; vale testar quando o resultado do Suno parece genérico.",
  "Melhor para trilhas instrumentais e orquestrais, com exportação em MIDI que você edita numa DAW.",
  "Gera música e efeitos sonoros além de voz; prático se você já usa a ferramenta."]),
 "best-ai-for-seo-content": ("Melhor IA para conteúdo de SEO", "Pesquise, estruture e escreva páginas que podem ranquear — sem publicar lixo gerado por IA.", [
  "Escolha nº 1 para a escrita em si: os rascunhos mais naturais e o melhor editor do seu próprio material.",
  "Dá nota ao seu rascunho comparando com o que ranqueia; útil como guia, mas não escreva só para bater a nota.",
  "Avaliação de conteúdo premium para times e agências; exagero para um site de uma pessoa só.",
  "Pesquisa rápida e com fontes sobre um tema e sobre o que os concorrentes cobrem.",
  "Faz-tudo sólido para briefings, estruturas e meta descriptions; pesquisa aprofundada (deep research) para achar lacunas de conteúdo."]),
 "best-ai-for-sales-emails": ("Melhor IA para e-mails de vendas", "Escreva cold e-mails e follow-ups melhores — pessoais, curtos e sem cara de IA.", [
  "Escolha nº 1: passe o contexto do prospect e receba um rascunho curto e que soa humano. Sempre revise.",
  "Igualmente bom para rascunhos e variações; use as instruções personalizadas para definir o seu tom de voz.",
  "Coaching e nota direto no Gmail/Outlook; vale a pena se você manda cold e-mail todo dia.",
  "Pesquisa rápida sobre o prospect e a empresa antes de você escrever a primeira linha.",
  "Polimento final de tom e clareza em qualquer lugar onde você digita."]),
 "best-ai-for-data-spreadsheets": ("Melhor IA para dados e planilhas", "Analise CSVs, escreva fórmulas e crie gráficos pedindo em linguagem natural.", [
  "Escolha nº 1: envie um arquivo e ele roda Python de verdade para analisar os dados e gerar gráficos.",
  "Ótimo para explicar dados e escrever fórmulas; também consegue rodar análises nos arquivos que você envia.",
  "Feito só para análise de dados, com um fluxo mais amigável para quem não programa.",
  "Melhor quando o trabalho já está no Excel; exige um plano do Microsoft 365 Copilot.",
  "A escolha natural dentro do Google Sheets."]),
 "best-ai-for-presentations": ("Melhor IA para apresentações", "Do roteiro a uma apresentação decente, em pouco tempo.", [
  "Escolha nº 1: mande um prompt ou cole suas anotações e tenha uma apresentação bonita em um minuto; exporta para PowerPoint.",
  "Melhor para times que querem slides consistentes, dentro da identidade visual da marca e que não perdem a formatação.",
  "Escreva primeiro a narrativa e o roteiro, ou peça para ele gerar o conteúdo dos slides e apresentações feitas em código.",
  "Bom para roteiros e notas do apresentador, e consegue gerar um arquivo .pptx para download.",
  "Faz sentido se suas apresentações já ficam no PowerPoint e o seu plano do Microsoft 365 inclui o Copilot."]),
 "best-ai-for-3d-assets": ("Melhor IA para assets 3D", "Gere props, personagens e modelos a partir de texto ou imagens.", [
  "Escolha nº 1: geração sólida de 3D a partir de texto ou imagem, com texturas e exportação para engines de jogo.",
  "Geração rápida com auto-rigging; ótimo para personagens que você precisa animar.",
  "Texto ou imagem para 3D com bastante detalhe e topologia limpa; os plugins levam os modelos direto para Blender, Unity ou Unreal.",
  "Melhor para assets de jogo com estilo consistente ao longo de todo o projeto.",
  "Em jogos 2.5D ou de sprites, pule o 3D de vez — gere arte conceitual e texturas localmente."]),
 "best-ai-for-meeting-notes": ("Melhor IA para notas de reunião", "Grave, transcreva e resuma reuniões para ninguém precisar fazer anotações.", [
  "Escolha nº 1: entra nas suas reuniões automaticamente, com bons resumos, busca e integrações com CRM.",
  "Melhor plano gratuito e transcrição ao vivo; os resumos são um pouco mais genéricos.",
  "Melhor para reuniões de vendas e com clientes, quando você quer compartilhar clipes, e não só notas.",
  "Notas de reunião nativas se o seu time já vive no Notion — sem precisar de mais um bot.",
  "Sem bot nenhum: cole a transcrição e receba resumos mais afiados e os próximos passos. Evite se você quer gravação automática."]),
 "best-ai-for-chatbots-rag": ("Melhor IA para chatbots e RAG", "Crie um assistente que responde com base nos seus próprios documentos — do no-code ao código sob medida.", [
  "Escolha nº 1 para começar: um Project do Claude baseado nos documentos que você envia vira um assistente do time em minutos. Evite se você precisa dele no seu próprio site.",
  "Um Project do ChatGPT com seus arquivos faz o mesmo trabalho. Os GPTs personalizados serão desativados em 11 de dezembro de 2026, então não comece um novo.",
  "Melhor framework em código quando a parte difícil é ingerir e recuperar bem os seus dados.",
  "O maior ecossistema de integrações; mais abstração do que você talvez precise para bots simples.",
  "Peça para ele escrever um app de RAG enxuto e sob medida, e use MCP para conectá-lo às suas ferramentas.",
  "Perguntas e respostas baseadas nas suas fontes, sem configuração nenhuma; para uso pessoal, e não para embutir em outro lugar."]),
 "best-ai-for-deploy-hosting": ("Melhor hospedagem para apps feitos com IA", "Onde colocar no ar o app que suas ferramentas de IA acabaram de criar. Estas são plataformas de hospedagem, não ferramentas de IA — escolhidas pelo quanto combinam com quem constrói com ajuda de IA.", [
  "Escolha nº 1 para apps Next.js/React (e tudo que sai do v0): deu push no git, ganhou uma URL no ar, com previews.",
  "Ótima para sites estáticos e apps simples, com um plano gratuito generoso e formulários integrados.",
  "O lugar mais fácil para backends, bancos de dados e workers em segundo plano. Evite para sites puramente estáticos.",
  "Melhor quando você precisa de Docker ou de várias regiões; exige um pouco mais de configuração. O Fly deixou de oferecer GPUs em 2026.",
  "Crie e hospede no mesmo lugar — o mais simples se você não quer mexer nunca em configuração de deploy."]),
 "best-ai-for-chrome-extensions": ("Melhor IA para criar extensões do Chrome", "Do 'devia ter um botão pra isso' a uma extensão de navegador funcionando.", [
  "Escolha nº 1: gera o manifest, os scripts e o popup, e corrige erros no contexto enquanto você recarrega e testa.",
  "Ótimo para montar a estrutura da extensão inteira e iterar nos problemas de permissão do Manifest V3.",
  "Serve para uma extensão pequena, de um arquivo só. Confira se ele usa o Manifest V3, porque exemplos antigos estão por toda parte.",
  "Não é uma ferramenta de IA, mas combina bem com uma: framework baseado em Vite, com manutenção ativa, que elimina o boilerplate de extensões.",
  "Bom autocomplete para as APIs do Chrome se você prefere escrever o código você mesmo."]),
 "best-ai-for-thumbnails-youtube-packaging": ("Melhor IA para thumbnails e títulos no YouTube", "Thumbnails, títulos e o gancho que faz a pessoa clicar.", [
  "Escolha nº 1 para thumbnails com texto chamativo e legível já embutido na imagem.",
  "Melhor para editar conversando (\"deixa o rosto mais surpreso\") e para fazer brainstorming de títulos no mesmo chat.",
  "Onde você monta de fato a thumbnail final: templates, remoção de fundo e as ferramentas Magic.",
  "Os fundos e cenários mais impactantes; coloque o texto depois no Canva.",
  "Faça brainstorming de pares de título e texto da thumbnail; ele é sincero quando uma ideia está com cara de clickbait."]),
 "best-ai-for-agent-frameworks": ("Melhores frameworks de agentes de IA", "Frameworks em código para criar seus próprios agentes com ferramentas, memória e workflows de várias etapas.", [
  "Escolha nº 1 para começar: API enxuta, com ferramentas, handoffs e tracing já integrados.",
  "Melhor quando você precisa de controle explícito: estado, retries, human-in-the-loop e confiabilidade em produção.",
  "O jeito mais rápido de prototipar 'crews' multiagente baseadas em papéis; mais difícil de manter sob controle em escala.",
  "O sucessor do AutoGen e do Semantic Kernel feito pela Microsoft: agentes e workflows em grafo em Python ou .NET; a escolha natural no Azure.",
  "Não é um framework, mas é o jeito padrão de dar ferramentas a qualquer agente. Crie suas ferramentas como servidores MCP."]),
 "best-ai-for-logos-brand": ("Melhor IA para logos e branding", "Ideias de logo, símbolos de marca e um brand kit inicial, em pouco tempo.", [
  "Escolha nº 1: gera logos e ícones vetoriais de verdade (SVG) que você pode editar e redimensionar.",
  "Melhor para conceitos de logo com o nome da marca legível; você ainda vai precisar vetorizar o que escolher.",
  "A opção tudo-em-um mais fácil para quem não é designer ter logo e brand kit; os resultados podem ter cara de template.",
  "Ótimo para explorar o clima e a direção visual da marca, e não para os arquivos finais do logo.",
  "Prático para iterar um conceito conversando. Confira se o conceito é realmente distintivo antes de registrar qualquer marca."]),
 "best-ai-for-customer-support": ("Melhor IA para atendimento ao cliente", "Responda os clientes mais rápido com agentes de IA e respostas rascunhadas por IA.", [
  "Escolha nº 1 para resolver tickets automaticamente; funciona até sem o help desk da Intercom. Cobra por resolução, então o custo cresce com o volume.",
  "Escolha natural se você já usa o Zendesk; configuração e preço mais pesados para times pequenos.",
  "Melhor para times pequenos que querem uma caixa de entrada simples com rascunhos e respostas de IA, e não uma plataforma enorme.",
  "Sem plataforma nenhuma: cole o ticket com a sua documentação e receba um rascunho de resposta cuidadoso e simpático.",
  "Mesma ideia; deixe seus documentos e seu guia de tom em um Project do ChatGPT para que cada rascunho parta do mesmo contexto."]),
 "best-ai-for-scraping": ("Melhor IA para web scraping", "Transforme sites em dados limpos para apps, pesquisa e pipelines de IA. Respeite os termos de uso e o robots.txt de cada site.", [
  "Escolha nº 1 para builders: uma chamada de API devolve markdown limpo ou JSON estruturado de um site.",
  "Melhor quando já existe um scraper pronto (mapas, redes sociais, e-commerce); agendamento integrado.",
  "Para sites que exigem um navegador de verdade, com login feito, ou muitos cliques pela página; combine com o Stagehand.",
  "Escreve e debuga um scraper sob medida em cima da página real; melhor para sites pontuais ou fora do comum.",
  "O mesmo, dentro do seu editor — bom quando o scraper fica num projeto que já existe."]),
 "best-ai-for-api-testing": ("Melhor IA para testes de API", "Escreva requisições, gere testes e debugue endpoints que estão falhando.", [
  "Escolha nº 1 se o seu time já usa o Postman: o Agent Mode escreve testes, corrige requisições quebradas e documenta APIs a partir das suas coleções.",
  "Gera e corrige suítes de teste (pytest, Jest etc.) bem ao lado do código da sua API.",
  "Cole uma spec OpenAPI ou uma resposta com falha e receba casos de teste e edge cases que você deixou passar.",
  "Bom para scripts de teste rápidos e dados mock; consegue rodar Python para testar as coisas.",
  "Não é IA em si, mas suas coleções em arquivos simples são fáceis para editores com IA lerem e escreverem. Escolha se você quer ficar offline e nativo no git."]),
 "best-ai-for-notion-docs": ("Melhor IA para notas e documentos", "Escreva, organize e pesquise suas notas e os documentos do time com IA.", [
  "Escolha nº 1 se o seu workspace está no Notion: escrita com IA, perguntas e respostas entre páginas e notas de reunião num lugar só.",
  "O melhor redator e editor para os documentos em si; os Projects deixam o material de referência sempre à mão.",
  "Versátil para rascunhar e reestruturar documentos, do primeiro esboço à reescrita completa.",
  "Escolha quando seus documentos são, na prática, mini-apps com tabelas e automações.",
  "Notas pessoais que se organizam sozinhas; não é para wikis de time."]),
}

NEW = {
 "claude-code": "O agente de código da Anthropic que roda no terminal — uma das ferramentas de dev mais comentadas.",
 "codex": "O agente de código Codex, relançado pela OpenAI (nuvem + CLI).",
 "veo": "O modelo de vídeo do Google, que agora gera áudio sincronizado.",
 "manus": "Agente autônomo de uso geral que viralizou com tarefas de várias etapas.",
 "lovable": "Construtor de apps a partir de prompts que está crescendo rápido.",
 "notebooklm": "Os resumos em áudio (Audio Overviews) transformaram notas de pesquisa em podcasts.",
 "kling": "Concorrente forte em geração de vídeo com IA.",
 "deepseek": "Modelos de raciocínio com pesos abertos que mexeram com os preços do mercado.",
 "mcp": "O protocolo aberto que a maioria das ferramentas de agentes já suporta para acesso a ferramentas.",
 "windsurf": "Editor agêntico que concorre diretamente com o Cursor.",
}

# Dated releases on /new/ (same keys/order as RELEASES in build.py). Product names stay in English.
MONTHS = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
DATE_MD = '{d} de {m}'
DATE_MDY = '{d} de {m} de {y}'
RELEASES = {
 'voxtral-3': 'Novos modelos de speech-to-text e text-to-speech da Mistral, mais um SDK para agentes de voz em tempo real por telefone e na web. Pela API da Mistral (com opção hospedada na UE) ou self-hosted.',
 'kling-4': 'Novo modelo de vídeo da Kuaishou: clipes de até 30 segundos de uma vez, movimentos rápidos e de câmera mais estáveis e até 15 referências e 10 keyframes por tarefa.',
 'muse-spark-open': 'Modelo open-weight da Meta para código e agentes (816B de parâmetros, 42B ativos, contexto de 1M de tokens). A Meta roda em dois Mac Studios; para a maioria, APIs hospedadas são o caminho prático.',
 'claude-haiku-5-5': 'O modelo mais barato e rápido da Anthropic, feito para trabalho em alto volume como bots de suporte, resumos e subagentes de código. Segundo a Anthropic, custa cerca de 75% menos que o Haiku 4.5.',
 'nano-banana-2-1': 'Modelo atualizado de geração e edição de imagens do Google, com edições melhores, mais consistência de personagens e texto nas imagens. No app Gemini, AI Studio, Gemini API, Flow e Stitch.',
 'copilot-dynamic-workflows': 'Defina em código tarefas com vários agentes (etapas em paralelo, subagentes conferindo uns aos outros, checkpoints para você revisar) no Copilot CLI, no app do Copilot e no Copilot SDK. Public preview, em todos os planos.',
 'heygen-video': 'Primeiro modelo de vídeo de uso geral da HeyGen: clipes de 5 a 15 segundos com falas e som gerados juntos, a partir de texto, imagem ou mídia de referência. Disponível pela API da HeyGen.',
 'gpt-6-1-sol': 'Upgrade do GPT-6 Sol anunciado no DevDay da OpenAI, focado em código com agentes, computer use e trabalho profissional. A OpenAI diz que chega perto do GPT-6 Astra por um preço bem menor.',
 'openai-agents-api-computer-use': 'A Agents API agora opera softwares via computer use e traz para o seu app os recursos multiagente do Codex, tool search e compactação de contexto. A OpenAI cuida da infraestrutura.',
 'claude-sonnet-5-5': 'O Sonnet mais rápido e mais barato da Anthropic, melhor em tarefas do dia a dia bem definidas e correção de bugs. Mais de 30% mais rápido que o Sonnet 5, pelo mesmo preço de US$ 2/US$ 10 por milhão de tokens.',
 'lovable-free-chat': 'Conversar com o Lovable agora é grátis dentro de uma cota diária: planeje features, pergunte sobre o código e o banco de dados do app ou rascunhe textos de lançamento. Construir ainda consome créditos.',
 'cursor-projects': 'Beta para trabalhos grandes, como uma feature ou uma migração: um agente coordenador roda na nuvem, planeja o trabalho, distribui para muitos subagentes e mantém um contexto compartilhado ao longo do tempo.',
}

PAGES = {  # key: (title, meta description, body)
 "home": ("Tool Use Cases — qual ferramenta de IA para cada tarefa", TAG + " Um diretório curado de ferramentas de IA organizadas por caso de uso.", """
<h1>Qual ferramenta de IA para cada tarefa.</h1><p class="lede">O Tool Use Cases é um diretório de ferramentas de IA organizadas pela tarefa que você quer resolver — para vibe coders, builders e qualquer pessoa que coloca projetos no ar com IA.</p>
<input type="search" placeholder="Filtrar casos de uso (ex.: vídeo, código, pesquisa)…" data-filter=".f" aria-label="Filtrar casos de uso">
<h2>Casos de uso</h2><div class="grid">{CARDS}</div>
{NL_FORM}
<h2>Lançamentos e tendências</h2><ul>{NEWTEASER}</ul><p><a href="@R/@Pnew/index.html">Todos os lançamentos →</a></p>
<div class="cta"><b>Criou uma ferramenta de IA?</b> Apareça em destaque no topo do caso de uso em que a sua ferramenta é melhor. <a class="btn" href="@R/@Psponsor/index.html">Patrocinar um espaço</a></div>"""),
 "use-cases": ("Casos de uso de ferramentas de IA — Tool Use Cases", "Encontre ferramentas de IA por caso de uso: vibe coding, agentes de código, debug, protótipos de jogos, vídeo, escrita, pesquisa, imagens e mais.", """
<h1>Casos de uso</h1><p class="lede">Escolha a tarefa. A gente lista as ferramentas que valem a pena testar e explica por quê.</p>
<input type="search" placeholder="Filtrar casos de uso…" data-filter=".f" aria-label="Filtrar"><div class="grid">{CARDS}</div>"""),
 "tools": ("Todas as ferramentas de IA de A a Z — Tool Use Cases", "Todas as ferramentas de IA do diretório Tool Use Cases, com o que cada uma faz e em quais casos de uso ela se encaixa.", """
<h1>Todas as ferramentas</h1><input type="search" placeholder="Filtrar ferramentas…" data-filter=".f" aria-label="Filtrar ferramentas"><div class="grid">{ROWS}</div>"""),
 "new": ("Ferramentas de IA novas e em alta — Tool Use Cases", "Lançamentos de ferramentas de IA que merecem atenção e estão em alta entre builders: agentes de código, modelos de vídeo, pesquisa e mais.", """
<h1>Lançamentos e tendências</h1><p class="lede">Lançamentos e grandes atualizações de ferramentas de IA das últimas seis semanas que importam para quem constrói. Cada um tem data, link para o anúncio oficial e o caso de uso em que se encaixa.</p>
<p class="muted">{LAST_UPDATED}</p><div class="grid">{NEWCARDS}</div>
<h2>{EARLIER_H2}</h2><p class="muted"><small>{EARLIER_P}</small></p><ul>{EARLIER}</ul>"""),
 "sponsor": ("Patrocine o Tool Use Cases — destaque sua ferramenta de IA", "Criadores de ferramentas podem patrocinar um espaço em destaque, sempre identificado, no topo das páginas de casos de uso relevantes.", """
<h1>Patrocine um caso de uso</h1><p class="lede">Alcance vibe coders e builders no momento em que eles estão escolhendo uma ferramenta.</p>
<h2>Como funciona</h2><ul><li>Um espaço <b>Patrocinado / Em destaque</b> fica no topo de cada página de caso de uso.</li><li>Ele é sempre identificado com clareza como "Patrocinado" e fica separado das nossas escolhas editoriais.</li><li>Só aceitamos ferramentas que realmente se encaixam no caso de uso.</li><li>O patrocínio nunca muda nossos vereditos nem nossos rankings.</li></ul>
<h2>Exemplo</h2>{SPONSOR_CARD}
<div class="cta">Preços e disponibilidade sob consulta. <a class="btn" href="{SPONSOR_MAILTO}">Patrocinar por e-mail</a></div>"""),
 "about": ("Sobre — Tool Use Cases", "O Tool Use Cases é um diretório independente, operado de forma autônoma, de ferramentas de IA organizadas por caso de uso.", """
<h1>Sobre</h1><p class="lede">O Tool Use Cases responde a uma pergunta: qual ferramenta de IA eu uso para esta tarefa?</p>
<p>A maioria dos diretórios de IA é uma lista gigante. A gente organiza por caso de uso e dá a cada escolha um veredito curto e em linguagem simples, para você decidir em um minuto.</p>
<p>O site é operado de forma autônoma — um operador de IA mantém tudo atualizado, e a responsabilidade humana pelo projeto é da Lali Publications. Só listamos ferramentas reais e conhecidas, e não publicamos notas inventadas nem números de usuários.</p>
<p>O Tool Use Cases é publicado pela Lali Publications, que também mantém o <a href="https://agentusecases.ai">agentusecases.ai</a>. As escolhas não são pagas: não temos vínculo com nenhuma ferramenta que listamos, e patrocínios nunca mudam os rankings.</p>
<p>Esta é a versão em português do site, com os mesmos casos de uso, escolhas e rankings da <a href="@R/about/index.html" hreflang="en">versão em inglês</a>.</p>
<h2 id="how-we-pick">Como escolhemos</h2><ul>
<li><b>Uma página por tarefa.</b> Cada caso de uso lista de 5 a 7 ferramentas muito usadas para aquela tarefa, em ordem de quanto se encaixam nela. A primeira é a nossa recomendação principal, com um veredito de uma linha dizendo para quem ela serve.</li>
<li><b>Só produtos reais e atuais.</b> Cada recomendação leva ao site oficial. Conferimos se o produto ainda existe com esse nome e se o link funciona sem redirecionamentos. Quando uma ferramenta muda de nome, é descontinuada ou deixa de ser mantida, nós a renomeamos ou substituímos. Em 22 de outubro de 2026, por exemplo, substituímos Udio, Luma Genie, Aider, Plasmo e AutoGen e renomeamos Windsurf, NotebookLM e Coda.</li>
<li><b>Fontes.</b> Usamos páginas oficiais de produto, documentação, changelogs e páginas de preços. Não publicamos notas, benchmarks, números de usuários nem citações que não tenhamos verificado.</li>
<li><b>O que não afirmamos.</b> Não fizemos testes comparativos formais. Os vereditos resumem para que cada ferramenta foi feita, com base na documentação oficial.</li>
<li><b>Preços.</b> Quando uma página mostra um preço ou plano gratuito, ele foi copiado da página oficial de preços na data indicada. Preços mudam com frequência; vale sempre a página oficial.</li>
<li><b>Datas.</b> Cada caso de uso mostra a «Última verificação»: a data em que conferimos de novo todas as recomendações dele.</li>
<li><b>Quem.</b> Um editor de IA faz a pesquisa e as atualizações. O site pertence à Lali Publications, que o publica e define estas regras. Ninguém paga pelas recomendações e não usamos links de afiliado.</li>
</ul>
<p>Correções, sugestões ou patrocínios: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""),
 "thanks": ("Obrigado por assinar — Tool Use Cases", "Recebemos sua inscrição na Tool Picks Weekly.", """
<h1>Você está na lista. Obrigado!</h1><p class="lede">Recebemos sua inscrição na Tool Picks Weekly. Fique de olho na próxima edição, na segunda-feira. Por enquanto, a newsletter é enviada em inglês.</p>
<p><a class="btn" href="@R/@Pindex.html">Voltar para o Tool Use Cases</a></p>"""),
}

LD = {  # structured-data names
 "itemlist_home": "Casos de uso de ferramentas de IA",
 "uc_coll": ("Casos de uso de ferramentas de IA", "Encontre ferramentas de IA por caso de uso."),
 "tools_crumb": "Todas as ferramentas", "tools_coll": ("Todas as ferramentas de IA de A a Z", "Todas as ferramentas de IA do diretório Tool Use Cases."),
 "new_crumb": "Lançamentos e tendências", "new_coll": ("Ferramentas de IA novas e em alta", "Lançamentos de ferramentas de IA em destaque e em alta para builders."),
 "sponsor_crumb": "Patrocínio",
 "about_crumb": "Sobre", "about_coll": ("Sobre o Tool Use Cases", "Diretório independente e operado de forma autônoma de ferramentas de IA organizadas por caso de uso, publicado pela Lali Publications."),
}
