"""Verified, dated extras for use-case pages (en, pt-BR, es only; noindexed locales show none).
PRICES: copied from each tool's official pricing page (or, for open-source tools, its official repo license) on price_date(tool). Re-check before changing the date.
GUIDES: 'how to choose' blocks for the top 5 pages, built only from the picks' verdicts and the verified prices/facts below."""
PRICES_CHECKED = "2026-10-22"  # default check date for PRICES entries not listed in PRICE_DATES
# tool: (en, pt-BR, es, official pricing source)
PRICES = {
 "cursor": ("Free plan with limited agent use. Plus $8/mo runs only Cursor's own models (Grok, Composer); Premium $30/mo adds cloud agents and Claude/GPT models billed at API list price. Sold as part of The X Subscription since Oct 2026.",
            "Plano grátis com uso limitado do agente. O Plus (US$ 8/mês) roda só os modelos do próprio Cursor (Grok, Composer); o Premium (US$ 30/mês) adiciona agentes na nuvem e modelos Claude/GPT cobrados pelo preço de tabela da API. Vendido como parte da The X Subscription desde out. de 2026.",
            "Plan gratuito con uso limitado del agente. Plus (8 US$/mes) solo usa los modelos propios de Cursor (Grok, Composer); Premium (30 US$/mes) añade agentes en la nube y modelos Claude/GPT cobrados a precio de lista de la API. Se vende dentro de The X Subscription desde oct. de 2026.",
            "https://cursor.com/pricing"),
 "lovable": ("Free plan: 5 build credits a day (up to 30 a month), and chatting is free within a daily allowance. Paid plans add a monthly credit balance.",
             "Plano grátis: 5 créditos de construção por dia (até 30 por mês), e o chat é grátis dentro de uma cota diária. Os planos pagos somam um saldo mensal de créditos.",
             "Plan gratuito: 5 créditos de construcción al día (hasta 30 al mes), y el chat es gratis dentro de un límite diario. Los planes de pago añaden un saldo mensual de créditos.",
             "https://lovable.dev/pricing"),
 "v0": ("Free plan: 7 messages a day. Plus $30 per user/mo, with $30 of monthly credits.",
        "Plano grátis: 7 mensagens por dia. Plus: US$ 30 por usuário/mês, com US$ 30 em créditos mensais.",
        "Plan gratuito: 7 mensajes al día. Plus: 30 US$ por usuario/mes, con 30 US$ en créditos mensuales.",
        "https://v0.app/pricing"),
 "replit": ("No free plan is listed on the pricing page. Core $20/mo ($18/mo billed yearly) with $20 of model credit; Pro $100/mo.",
            "A página de preços não lista plano grátis. Core: US$ 20/mês (US$ 18/mês no anual) com US$ 20 em créditos de modelos; Pro: US$ 100/mês.",
            "La página de precios no muestra plan gratuito. Core: 20 US$/mes (18 US$/mes en anual) con 20 US$ de crédito para modelos; Pro: 100 US$/mes.",
            "https://replit.com/pricing"),
 "bolt": ("Free plan: 1M tokens a month, with Bolt branding on sites. Pro $18/mo billed yearly (10M tokens, your own domain).",
          "Plano grátis: 1 milhão de tokens por mês, com a marca Bolt nos sites. Pro: US$ 18/mês no plano anual (10 milhões de tokens, domínio próprio).",
          "Plan gratuito: 1 millón de tokens al mes, con la marca Bolt en los sitios. Pro: 18 US$/mes en plan anual (10 millones de tokens, dominio propio).",
          "https://bolt.new/pricing"),
 "windsurf": ("Free plan with a light quota. Pro $20/mo includes frontier models from OpenAI, Anthropic and Google; Max $200/mo.",
              "Plano grátis com cota leve. O Pro (US$ 20/mês) inclui modelos de ponta da OpenAI, Anthropic e Google; o Max custa US$ 200/mês.",
              "Plan gratuito con una cuota ligera. Pro (20 US$/mes) incluye modelos punteros de OpenAI, Anthropic y Google; Max cuesta 200 US$/mes.",
              "https://devin.ai/pricing"),
 "devin": ("Free plan with a light quota. Cloud agents (Devin Cloud) start on Pro at $20/mo; Teams from $80/mo.",
           "Plano grátis com cota leve. Os agentes na nuvem (Devin Cloud) começam no Pro, a US$ 20/mês; Teams a partir de US$ 80/mês.",
           "Plan gratuito con una cuota ligera. Los agentes en la nube (Devin Cloud) empiezan en Pro, a 20 US$/mes; Teams desde 80 US$/mes.",
           "https://devin.ai/pricing"),
 "claude-code": ("Included with Claude Pro ($20/mo, or $17/mo billed yearly) and Max (from $100/mo). Not on the free plan.",
                 "Incluído no Claude Pro (US$ 20/mês, ou US$ 17/mês no anual) e no Max (a partir de US$ 100/mês). Não está no plano grátis.",
                 "Incluido en Claude Pro (20 US$/mes, o 17 US$/mes en anual) y en Max (desde 100 US$/mes). No está en el plan gratuito.",
                 "https://claude.com/pricing"),
 "claude": ("Free plan. Pro $20/mo ($17/mo billed yearly); Max from $100/mo.",
            "Plano grátis. Pro: US$ 20/mês (US$ 17/mês no anual); Max a partir de US$ 100/mês.",
            "Plan gratuito. Pro: 20 US$/mes (17 US$/mes en anual); Max desde 100 US$/mes.",
            "https://claude.com/pricing"),
 "codex": ("Limited use on ChatGPT's free plan; ChatGPT Plus ($20/mo) for regular coding sessions. With an API key, API pricing applies.",
           "Uso limitado no plano grátis do ChatGPT; o ChatGPT Plus (US$ 20/mês) cobre sessões de código frequentes. Com chave de API, vale o preço da API.",
           "Uso limitado en el plan gratuito de ChatGPT; ChatGPT Plus (20 US$/mes) cubre sesiones de código habituales. Con clave de API se aplica el precio de la API.",
           "https://developers.openai.com/codex/pricing"),
 "chatgpt": ("Free plan. Paid plans: Go, Plus ($20/mo) and Pro.",
             "Plano grátis. Planos pagos: Go, Plus (US$ 20/mês) e Pro.",
             "Plan gratuito. Planes de pago: Go, Plus (20 US$/mes) y Pro.",
             "https://chatgpt.com/pricing"),
 "copilot": ("Free plan with limited chat and agent use. Pro $10/mo, Pro+ $39/mo, Max $100/mo.",
             "Plano grátis com chat e agente limitados. Pro: US$ 10/mês; Pro+: US$ 39/mês; Max: US$ 100/mês.",
             "Plan gratuito con chat y agente limitados. Pro: 10 US$/mes; Pro+: 39 US$/mes; Max: 100 US$/mes.",
             "https://github.com/features/copilot/plans"),
 "opencode": ("Free and open source. It comes with free models, or you can connect any provider's models.",
              "Grátis e open source. Vem com modelos gratuitos, ou você conecta modelos de qualquer provedor.",
              "Gratis y de código abierto. Incluye modelos gratuitos, o puedes conectar modelos de cualquier proveedor.",
              "https://opencode.ai"),
 "sentry": ("Free Developer plan for one user. Team from $26/mo billed yearly.",
            "Plano Developer grátis para um usuário. Team a partir de US$ 26/mês no anual.",
            "Plan Developer gratuito para un usuario. Team desde 26 US$/mes en anual.",
            "https://sentry.io/pricing"),
 "rosebud": ("Free plan starts you with 8,000 credits, no card needed. Paid plans include Pro at $50/mo.",
             "O plano grátis começa com 8.000 créditos, sem cartão. Entre os planos pagos está o Pro, a US$ 50/mês.",
             "El plan gratuito empieza con 8.000 créditos, sin tarjeta. Entre los planes de pago está Pro, a 50 US$/mes.",
             "https://rosebud.ai/pricing"),
 "scenario": ("Free plan outputs are for personal and evaluation use only. Paid plans from $15/mo (Starter).",
              "O que você gera no plano grátis é só para uso pessoal e avaliação. Planos pagos a partir de US$ 15/mês (Starter).",
              "Lo que generas en el plan gratuito es solo para uso personal y de evaluación. Planes de pago desde 15 US$/mes (Starter).",
              "https://www.scenario.com/pricing"),
 "meshy": ("Free plan: 100 credits a month. Pro $20/mo.",
           "Plano grátis: 100 créditos por mês. Pro: US$ 20/mês.",
           "Plan gratuito: 100 créditos al mes. Pro: 20 US$/mes.",
           "https://www.meshy.ai/pricing"),
 "suno": ("Free plan with Suno's free models. Pro from $8/mo billed yearly.",
          "Plano grátis com os modelos gratuitos do Suno. Pro a partir de US$ 8/mês no anual.",
          "Plan gratuito con los modelos gratuitos de Suno. Pro desde 8 US$/mes en anual.",
          "https://suno.com/pricing"),
 "elevenlabs": ("Free plan: 10k credits a month. Starter $6/mo; Creator $22/mo.",
                "Plano grátis: 10 mil créditos por mês. Starter: US$ 6/mês; Creator: US$ 22/mês.",
                "Plan gratuito: 10.000 créditos al mes. Starter: 6 US$/mes; Creator: 22 US$/mes.",
                "https://elevenlabs.io/pricing"),
 "descript": ("Free plan. Hobbyist $16/mo billed yearly ($24 monthly); Creator $24/mo billed yearly ($35 monthly).",
              "Plano grátis. Hobbyist: US$ 16/mês no anual (US$ 24 no mensal); Creator: US$ 24/mês no anual (US$ 35 no mensal).",
              "Plan gratuito. Hobbyist: 16 US$/mes en anual (24 US$ mensual); Creator: 24 US$/mes en anual (35 US$ mensual).",
              "https://www.descript.com/pricing"),
 "runway": ("Free plan for trying the tools. Standard $15/mo ($12/mo billed yearly); Pro $35/mo ($28/mo billed yearly).",
            "Plano grátis para testar. Standard: US$ 15/mês (US$ 12/mês no anual); Pro: US$ 35/mês (US$ 28/mês no anual).",
            "Plan gratuito para probar. Standard: 15 US$/mes (12 US$/mes en anual); Pro: 35 US$/mes (28 US$/mes en anual).",
            "https://runway.com/pricing"),
 "veo": ("Video generation isn't on the free Gemini plan. Paid Google AI plans that include it start at $4.99/mo in the US.",
         "A geração de vídeo não está no plano grátis do Gemini. Nos EUA, os planos pagos do Google AI que a incluem começam em US$ 4,99/mês.",
         "La generación de vídeo no está en el plan gratuito de Gemini. En EE. UU., los planes de pago de Google AI que la incluyen empiezan en 4,99 US$/mes.",
         "https://gemini.google/subscriptions/"),
 "opus": ("Free trial, no card needed. Starter $15/mo; Pro $29/mo.",
          "Teste grátis, sem cartão. Starter: US$ 15/mês; Pro: US$ 29/mês.",
          "Prueba gratuita, sin tarjeta. Starter: 15 US$/mes; Pro: 29 US$/mes.",
          "https://www.opus.pro/pricing"),
 "capcut": ("Free plan with the basics. Auto-captions need a paid Pro plan.",
            "Plano grátis com o básico. As legendas automáticas exigem o plano pago Pro.",
            "Plan gratuito con lo básico. Los subtítulos automáticos requieren el plan de pago Pro.",
            "https://www.capcut.com/pricing"),
 "heygen": ("Free plan for trying it out. Creator from $29/mo; Pro from $49/mo.",
            "Plano grátis para testar. Creator a partir de US$ 29/mês; Pro a partir de US$ 49/mês.",
            "Plan gratuito para probar. Creator desde 29 US$/mes; Pro desde 49 US$/mes.",
            "https://www.heygen.com/pricing"),
 # --- added Oct 23, 2026 (dates in PRICE_DATES) ---
 "notion-ai": ("Free and Plus ($10 per member/mo billed yearly) include only a trial of Notion AI. Full Notion AI (Notion Agent, AI Meeting Notes) is on Business, $20 per member/mo billed yearly.",
   "Os planos Free e Plus (US$ 10 por membro/mês no anual) incluem só um teste do Notion AI. O Notion AI completo (Notion Agent, AI Meeting Notes) está no Business, a US$ 20 por membro/mês no anual.",
   "Los planes Free y Plus (10 US$ por miembro/mes en anual) solo incluyen una prueba de Notion AI. Notion AI completo (Notion Agent, AI Meeting Notes) está en Business, a 20 US$ por miembro/mes en anual.",
   "https://www.notion.com/pricing"),
 "gemini": ("Free plan with a Google Account (includes Canvas and Deep Research). In the US: Google AI Plus $4.99/mo, Google AI Pro $19.99/mo, Ultra from $99.99/mo.",
   "Plano grátis com uma Conta Google (inclui Canvas e Deep Research). Nos EUA: Google AI Plus US$ 4,99/mês, Google AI Pro US$ 19,99/mês, Ultra a partir de US$ 99,99/mês.",
   "Plan gratuito con una cuenta de Google (incluye Canvas y Deep Research). En EE. UU.: Google AI Plus 4,99 US$/mes, Google AI Pro 19,99 US$/mes, Ultra desde 99,99 US$/mes.",
   "https://gemini.google/subscriptions/"),
 "notebooklm": ("Included free with a Google Account. Google AI Pro ($19.99/mo in the US) gives 5x more Audio Overviews, notebooks and more.",
   "Incluído grátis com uma Conta Google. O Google AI Pro (US$ 19,99/mês nos EUA) dá 5x mais Audio Overviews, notebooks e mais.",
   "Incluido gratis con una cuenta de Google. Google AI Pro (19,99 US$/mes en EE. UU.) da 5 veces más Audio Overviews, cuadernos y más.",
   "https://gemini.google/subscriptions/"),
 "midjourney": ("No free plan: every plan is a subscription. Basic $10/mo ($8/mo billed yearly); Standard $30/mo adds unlimited Relax-mode images.",
   "Sem plano grátis: todos os planos são assinaturas. Basic: US$ 10/mês (US$ 8/mês no anual); o Standard (US$ 30/mês) adiciona imagens ilimitadas no modo Relax.",
   "Sin plan gratuito: todos los planes son suscripciones. Basic: 10 US$/mes (8 US$/mes en anual); Standard (30 US$/mes) añade imágenes ilimitadas en modo Relax.",
   "https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans"),
 "ideogram": ("Eligible free accounts get weekly credits. Plus $20/mo ($15/mo billed yearly); Pro $60/mo ($42/mo billed yearly).",
   "Contas grátis elegíveis recebem créditos semanais. Plus: US$ 20/mês (US$ 15/mês no anual); Pro: US$ 60/mês (US$ 42/mês no anual).",
   "Las cuentas gratuitas elegibles reciben créditos semanales. Plus: 20 US$/mes (15 US$/mes en anual); Pro: 60 US$/mes (42 US$/mes en anual).",
   "https://ideogram.ai/pricing"),
 "grammarly": ("Free plan for spelling and grammar. Pro from $12/mo adds full-sentence rewrites.",
   "Plano grátis para ortografia e gramática. O Pro, a partir de US$ 12/mês, reescreve frases inteiras.",
   "Plan gratuito para ortografía y gramática. Pro, desde 12 US$/mes, reescribe frases completas.",
   "https://www.grammarly.com/plans"),
 "elicit": ("Free Basic plan with limited Research Agent and report use. Plus from $11 per user/mo billed yearly.",
   "Plano Basic grátis, com uso limitado do Research Agent e dos relatórios. Plus a partir de US$ 11 por usuário/mês no anual.",
   "Plan Basic gratuito, con uso limitado del Research Agent y de los informes. Plus desde 11 US$ por usuario/mes en anual.",
   "https://elicit.com/pricing"),
 "grok": ("Paid plans are one subscription shared with X and Cursor: Plus $8/mo, Premium $30/mo, Super $100/mo, Ultra $200/mo (monthly billing; yearly is cheaper).",
   "Os planos pagos são uma assinatura só, compartilhada com o X e o Cursor: Plus US$ 8/mês, Premium US$ 30/mês, Super US$ 100/mês, Ultra US$ 200/mês (no mensal; o anual sai mais barato).",
   "Los planes de pago son una sola suscripción compartida con X y Cursor: Plus 8 US$/mes, Premium 30 US$/mes, Super 100 US$/mes, Ultra 200 US$/mes (pago mensual; el anual sale más barato).",
   "https://grok.com/plans"),
 "n8n": ("The self-hosted Community Edition is free. n8n Cloud: Starter €20/mo and Pro €50/mo billed yearly, with a free trial and no card needed.",
   "A Community Edition, auto-hospedada, é grátis. n8n Cloud: Starter € 20/mês e Pro € 50/mês no anual, com teste grátis sem cartão.",
   "La Community Edition, autoalojada, es gratis. n8n Cloud: Starter 20 €/mes y Pro 50 €/mes en anual, con prueba gratuita sin tarjeta.",
   "https://n8n.io/pricing/"),
 "make": ("Free plan: 1,000 credits a month.",
   "Plano grátis: 1.000 créditos por mês.",
   "Plan gratuito: 1.000 créditos al mes.",
   "https://www.make.com/en/pricing"),
 "zapier": ("Free forever: 100 tasks a month and two-step Zaps. Professional from $19.99/mo billed yearly adds multi-step Zaps.",
   "Grátis para sempre: 100 tarefas por mês e Zaps de dois passos. O Professional, a partir de US$ 19,99/mês no anual, libera Zaps com vários passos.",
   "Gratis para siempre: 100 tareas al mes y Zaps de dos pasos. Professional, desde 19,99 US$/mes en anual, añade Zaps de varios pasos.",
   "https://zapier.com/pricing"),
 "framer": ("Free plan on a Framer domain, meant for non-commercial use. Basic $10/mo and Pro $30/mo with yearly billing; a custom domain needs a paid plan.",
   "Plano grátis num domínio Framer, pensado para uso não comercial. Basic US$ 10/mês e Pro US$ 30/mês no anual; domínio próprio exige plano pago.",
   "Plan gratuito en un dominio de Framer, pensado para uso no comercial. Basic 10 US$/mes y Pro 30 US$/mes en anual; un dominio propio requiere plan de pago.",
   "https://www.framer.com/pricing"),
 "figma": ("Free Starter plan (up to 500 AI credits a month). Professional full seat $16/mo billed yearly, with 3,000 AI credits a month.",
   "Plano Starter grátis (até 500 créditos de IA por mês). Assento completo do Professional: US$ 16/mês no anual, com 3.000 créditos de IA por mês.",
   "Plan Starter gratuito (hasta 500 créditos de IA al mes). Asiento completo de Professional: 16 US$/mes en anual, con 3.000 créditos de IA al mes.",
   "https://www.figma.com/pricing/"),
 "uizard": ("Free plan. Pro $12/mo billed yearly (500 AI generations a month); Business $39/mo billed yearly.",
   "Plano grátis. Pro: US$ 12/mês no anual (500 gerações de IA por mês); Business: US$ 39/mês no anual.",
   "Plan gratuito. Pro: 12 US$/mes en anual (500 generaciones de IA al mes); Business: 39 US$/mes en anual.",
   "https://uizard.io/pricing/"),
 "aiva": ("Free plan for non-commercial use only: AIVA owns the copyright, you must credit it, 3 downloads a month. Standard €11/mo billed yearly (+VAT).",
   "Plano grátis só para uso não comercial: o copyright é da AIVA, é preciso dar crédito, 3 downloads por mês. Standard: € 11/mês no anual (+ impostos).",
   "Plan gratuito solo para uso no comercial: el copyright es de AIVA, hay que darle crédito y tienes 3 descargas al mes. Standard: 11 €/mes en anual (+ IVA).",
   "https://www.aiva.ai/pricing"),
 "clearscope": ("No free plan; 14-day free trial. Essentials $129/mo; Business $399/mo.",
   "Sem plano grátis; teste grátis de 14 dias. Essentials: US$ 129/mês; Business: US$ 399/mês.",
   "Sin plan gratuito; prueba gratuita de 14 días. Essentials: 129 US$/mes; Business: 399 US$/mes.",
   "https://www.clearscope.io/pricing"),
 "julius": ("Free plan with daily credits. Plus $20/mo ($16/mo billed yearly); Pro $45/mo.",
   "Plano grátis com créditos diários. Plus: US$ 20/mês (US$ 16/mês no anual); Pro: US$ 45/mês.",
   "Plan gratuito con créditos diarios. Plus: 20 US$/mes (16 US$/mes en anual); Pro: 45 US$/mes.",
   "https://julius.ai/pricing"),
 "beautiful-ai": ("14-day free trial. Pro $14.50/mo billed yearly for individuals; Team $40 per user/mo billed yearly.",
   "Teste grátis de 14 dias. Pro: US$ 14,50/mês no anual para uso individual; Team: US$ 40 por usuário/mês no anual.",
   "Prueba gratuita de 14 días. Pro: 14,50 US$/mes en anual para uso individual; Team: 40 US$ por usuario/mes en anual.",
   "https://www.beautiful.ai/pricing"),
 "tripo": ("Free plan. Pro $20/mo billed yearly; Max $90/mo billed yearly.",
   "Plano grátis. Pro: US$ 20/mês no anual; Max: US$ 90/mês no anual.",
   "Plan gratuito. Pro: 20 US$/mes en anual; Max: 90 US$/mes en anual.",
   "https://www.tripo3d.ai/pricing"),
 "rodin": ("Free to generate; you pay $1.50 per credit only when you keep a result. Subscription $30/mo ($24/mo billed yearly).",
   "Gerar é grátis; você paga US$ 1,50 por crédito só quando fica com o resultado. Assinatura: US$ 30/mês (US$ 24/mês no anual).",
   "Generar es gratis; pagas 1,50 US$ por crédito solo cuando te quedas con el resultado. Suscripción: 30 US$/mes (24 US$/mes en anual).",
   "https://hyper3d.ai/pricing"),
 "fireflies": ("Free forever plan. Pro $10 per seat/mo billed yearly ($18 monthly); Business $19 per seat/mo billed yearly.",
   "Plano grátis para sempre. Pro: US$ 10 por assento/mês no anual (US$ 18 no mensal); Business: US$ 19 por assento/mês no anual.",
   "Plan gratuito para siempre. Pro: 10 US$ por asiento/mes en anual (18 US$ mensual); Business: 19 US$ por asiento/mes en anual.",
   "https://fireflies.ai/pricing"),
 "otter": ("Free Basic plan. Pro $8.33 per user/mo billed yearly ($16.99 monthly); Business $19.99 per user/mo billed yearly.",
   "Plano Basic grátis. Pro: US$ 8,33 por usuário/mês no anual (US$ 16,99 no mensal); Business: US$ 19,99 por usuário/mês no anual.",
   "Plan Basic gratuito. Pro: 8,33 US$ por usuario/mes en anual (16,99 US$ mensual); Business: 19,99 US$ por usuario/mes en anual.",
   "https://otter.ai/pricing"),
 "grain": ("Free forever for individuals. Paid plans from $19 per seat/mo billed yearly.",
   "Grátis para sempre para uso individual. Planos pagos a partir de US$ 19 por assento/mês no anual.",
   "Gratis para siempre para uso individual. Planes de pago desde 19 US$ por asiento/mes en anual.",
   "https://grain.com/pricing"),
 "langchain": ("The open-source framework is free (MIT license).",
   "O framework open source é grátis (licença MIT).",
   "El framework de código abierto es gratis (licencia MIT).",
   "https://github.com/langchain-ai/langchain"),
 "llamaindex": ("The open-source framework is free (MIT license).",
   "O framework open source é grátis (licença MIT).",
   "El framework de código abierto es gratis (licencia MIT).",
   "https://github.com/run-llama/llama_index"),
 "langgraph": ("The open-source framework is free (MIT license).",
   "O framework open source é grátis (licença MIT).",
   "El framework de código abierto es gratis (licencia MIT).",
   "https://github.com/langchain-ai/langgraph"),
 "crewai": ("The open-source framework is free (MIT license). CrewAI's hosted Basic plan is free with 50 workflow executions a month.",
   "O framework open source é grátis (licença MIT). O plano Basic hospedado da CrewAI é grátis, com 50 execuções de workflow por mês.",
   "El framework de código abierto es gratis (licencia MIT). El plan Basic alojado de CrewAI es gratis, con 50 ejecuciones de workflow al mes.",
   "https://www.crewai.com/pricing"),
 "ms-agent-framework": ("Free and open source (MIT license).",
   "Grátis e open source (licença MIT).",
   "Gratis y de código abierto (licencia MIT).",
   "https://github.com/microsoft/agent-framework"),
 "openai-agents": ("Free and open source (MIT license). You pay only for the models you call.",
   "Grátis e open source (licença MIT). Você paga só pelos modelos que usar.",
   "Gratis y de código abierto (licencia MIT). Solo pagas por los modelos que uses.",
   "https://github.com/openai/openai-agents-python"),
 "ollama": ("Free and open source (MIT license); models run on your own hardware.",
   "Grátis e open source (licença MIT); os modelos rodam no seu próprio hardware.",
   "Gratis y de código abierto (licencia MIT); los modelos se ejecutan en tu propio hardware.",
   "https://github.com/ollama/ollama"),
 "wxt": ("Free and open source (MIT license).",
   "Grátis e open source (licença MIT).",
   "Gratis y de código abierto (licencia MIT).",
   "https://github.com/wxt-dev/wxt"),
 "vercel": ("Free Hobby plan for personal projects. Pro $20/mo, including $20 of usage credit.",
   "Plano Hobby grátis para projetos pessoais. Pro: US$ 20/mês, com US$ 20 de crédito de uso incluídos.",
   "Plan Hobby gratuito para proyectos personales. Pro: 20 US$/mes, con 20 US$ de crédito de uso incluidos.",
   "https://vercel.com/pricing"),
 "netlify": ("Free forever plan with hard monthly limits, so it can't run up charges. Personal $9/mo; Pro $20/mo for unlimited members.",
   "Plano grátis para sempre, com limites mensais rígidos, então não gera cobranças. Personal: US$ 9/mês; Pro: US$ 20/mês com membros ilimitados.",
   "Plan gratuito para siempre, con límites mensuales fijos, así que no genera cargos. Personal: 9 US$/mes; Pro: 20 US$/mes con miembros ilimitados.",
   "https://www.netlify.com/pricing/"),
 "railway": ("30-day free trial with $5 of credits, no card needed. Hobby has a $5/mo minimum that includes $5 of usage; Pro includes $20 of usage a month.",
   "Teste grátis de 30 dias com US$ 5 em créditos, sem cartão. O Hobby tem mínimo de US$ 5/mês, que inclui US$ 5 de uso; o Pro inclui US$ 20 de uso por mês.",
   "Prueba gratuita de 30 días con 5 US$ en créditos, sin tarjeta. Hobby tiene un mínimo de 5 US$/mes que incluye 5 US$ de uso; Pro incluye 20 US$ de uso al mes.",
   "https://railway.com/pricing"),
 "looka": ("Making and browsing logos is free. Logo files from $35 one-time (one PNG); Premium package $72; Brand Kit $96/yr.",
   "Criar e explorar logos é grátis. Arquivos do logo a partir de US$ 35 em pagamento único (um PNG); pacote Premium US$ 72; Brand Kit US$ 96/ano.",
   "Crear y explorar logos es gratis. Archivos del logo desde 35 US$ en pago único (un PNG); paquete Premium 72 US$; Brand Kit 96 US$/año.",
   "https://looka.com/pricing/"),
 "helpscout": ("Free plan: 5 users, 1 inbox and 1 Docs site.",
   "Plano grátis: 5 usuários, 1 caixa de entrada e 1 site de Docs.",
   "Plan gratuito: 5 usuarios, 1 bandeja de entrada y 1 sitio de Docs.",
   "https://www.helpscout.com/pricing/"),
 "firecrawl": ("Free plan: 1,000 credits a month, no card needed. Hobby $19/mo ($16/mo billed yearly) for 5,000 credits.",
   "Plano grátis: 1.000 créditos por mês, sem cartão. Hobby: US$ 19/mês (US$ 16/mês no anual) por 5.000 créditos.",
   "Plan gratuito: 1.000 créditos al mes, sin tarjeta. Hobby: 19 US$/mes (16 US$/mes en anual) por 5.000 créditos.",
   "https://www.firecrawl.dev/pricing"),
 "apify": ("Free plan with $5 a month to spend on Actors, no card needed. Starter $19/mo plus pay-as-you-go usage.",
   "Plano grátis com US$ 5 por mês para gastar em Actors, sem cartão. Starter: US$ 19/mês mais uso pago conforme o consumo.",
   "Plan gratuito con 5 US$ al mes para gastar en Actors, sin tarjeta. Starter: 19 US$/mes más uso de pago por consumo.",
   "https://apify.com/pricing"),
 "browserbase": ("Free plan for prototyping. Developer $20/mo (100 browser hours); Startup $99/mo.",
   "Plano grátis para protótipos. Developer: US$ 20/mês (100 horas de navegador); Startup: US$ 99/mês.",
   "Plan gratuito para prototipos. Developer: 20 US$/mes (100 horas de navegador); Startup: 99 US$/mes.",
   "https://www.browserbase.com/pricing"),
 "postman": ("Free plan for individuals. Solo $9/mo and Team $19 per user/mo, billed yearly.",
   "Plano grátis para uso individual. Solo: US$ 9/mês e Team: US$ 19 por usuário/mês, no anual.",
   "Plan gratuito para uso individual. Solo: 9 US$/mes y Team: 19 US$ por usuario/mes, en anual.",
   "https://www.postman.com/pricing/"),
 "bruno": ("The open-source app is free. Pro $6 and Ultimate $11 per user/mo, billed yearly.",
   "O app open source é grátis. Pro: US$ 6 e Ultimate: US$ 11 por usuário/mês, no anual.",
   "La app de código abierto es gratis. Pro: 6 US$ y Ultimate: 11 US$ por usuario/mes, en anual.",
   "https://www.usebruno.com/pricing"),
 "mem": ("Free plan. Mem Plus $9/mo; Mem Pro $29/mo.",
   "Plano grátis. Mem Plus: US$ 9/mês; Mem Pro: US$ 29/mês.",
   "Plan gratuito. Mem Plus: 9 US$/mes; Mem Pro: 29 US$/mes.",
   "https://get.mem.ai/pricing"),
}
PRICE_DATES = {k: "2026-10-23" for k in ['notion-ai', 'gemini', 'notebooklm', 'midjourney', 'ideogram', 'grammarly', 'elicit', 'grok', 'n8n', 'make', 'zapier', 'framer', 'figma', 'uizard', 'aiva', 'clearscope', 'julius', 'beautiful-ai', 'tripo', 'rodin', 'fireflies', 'otter', 'grain', 'langchain', 'llamaindex', 'langgraph', 'crewai', 'ms-agent-framework', 'openai-agents', 'ollama', 'wxt', 'vercel', 'netlify', 'railway', 'looka', 'helpscout', 'firecrawl', 'apify', 'browserbase', 'postman', 'bruno', 'mem']}  # entries checked on their official pricing page / repo on Oct 23, 2026
def price_date(t): return PRICE_DATES.get(t, PRICES_CHECKED)
LABELS = {"en": ("Price", "Prices checked", "on each tool's official pricing page. They change often, so the official page wins.", "How to choose"),
          "pt-BR": ("Preço", "Preços conferidos em", "na página oficial de preços de cada ferramenta. Eles mudam com frequência; vale sempre a página oficial.", "Como escolher"),
          "es": ("Precio", "Precios comprobados el", "en la página oficial de precios de cada herramienta. Cambian a menudo; manda siempre la página oficial.", "Cómo elegir")}
# slug: {lang: html}. Links to tools use @T(key) and are expanded by build.py.
GUIDES = {
 "best-ai-for-vibe-coding": {
  "en": """<ul>
<li><b>Never coded and want a web app with login and a database:</b> start with @T(lovable) or @T(bolt). Both have free plans to try the idea before you pay.</li>
<li><b>Want a polished React/Next.js front end that deploys to Vercel:</b> @T(v0).</li>
<li><b>Want everything, including hosting, in one browser tab:</b> @T(replit). Its pricing page lists no free plan.</li>
<li><b>Comfortable in a code editor, or the project will outgrow a builder:</b> @T(cursor) or @T(windsurf).</li>
</ul>
<p><b>Lovable vs Bolt vs v0:</b> Lovable and Bolt both turn a prompt into a full-stack app in the browser, with auth and a database. v0 is strongest on the UI layer and fits best if you already deploy on Vercel.</p>
<p><b>Cursor vs Devin Desktop:</b> both are full AI code editors. Since Oct 2026 Cursor's $8 Plus plan runs only Cursor's own models, and Claude or GPT cost extra at API rates from the $30 Premium plan up. Devin Desktop's $20 Pro plan includes frontier models from OpenAI, Anthropic and Google. If you want Claude or GPT inside your editor on a flat fee, compare the two before you subscribe.</p>
<p><b>Also worth a look:</b> <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, another prompt-to-app builder with a free plan (paid from $16/mo billed yearly).</p>
<p><b>Google's free options (checked Oct 23, 2026):</b> <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a>'s Build mode turns a prompt into a web app in the browser and can deploy it to Google Cloud Run; Google says AI Studio is free to use, with paid tiers for heavy traffic. <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a> is Google's agent-first code editor, with a $0 individual plan that has weekly rate limits. Want to design the screens first? @T(stitch) is our prompt-to-UI pick on <a href="@R/use-cases/best-ai-for-ui-design/index.html">Best AI for UI design</a>. Skip Firebase Studio for new projects: it <a href="https://firebase.google.com/docs/studio/migrating-project" rel="noopener" target="_blank">closed to new sign-ups on June 22, 2026 and shuts down on March 22, 2027</a>.</p>""",
  "pt-BR": """<ul>
<li><b>Nunca programou e quer um web app com login e banco de dados:</b> comece pelo @T(lovable) ou pelo @T(bolt). Os dois têm plano grátis para testar a ideia antes de pagar.</li>
<li><b>Quer um front-end React/Next.js caprichado com deploy na Vercel:</b> @T(v0).</li>
<li><b>Quer tudo, inclusive hospedagem, numa aba do navegador:</b> @T(replit). A página de preços não lista plano grátis.</li>
<li><b>Já se vira num editor de código, ou o projeto vai crescer além de um builder:</b> @T(cursor) ou @T(windsurf).</li>
</ul>
<p><b>Lovable vs Bolt vs v0:</b> Lovable e Bolt transformam um prompt em um app full-stack no navegador, com autenticação e banco de dados. O v0 se destaca na interface e encaixa melhor se você já faz deploy na Vercel.</p>
<p><b>Cursor vs Devin Desktop:</b> os dois são editores de código completos com IA. Desde out. de 2026, o plano Plus do Cursor (US$ 8) roda só os modelos do próprio Cursor, e Claude ou GPT são cobrados à parte, pelo preço da API, a partir do Premium (US$ 30). O Pro do Devin Desktop (US$ 20) inclui modelos de ponta da OpenAI, Anthropic e Google. Se você quer Claude ou GPT no editor por um valor fixo, compare os dois antes de assinar.</p>
<p><b>Vale olhar também:</b> o <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, outro builder de apps a partir de prompts, com plano grátis (pago a partir de US$ 16/mês no anual).</p>
<p><b>Opções grátis do Google (conferidas em 23 de out. de 2026):</b> o modo Build do <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a> transforma um prompt em um web app no navegador e pode fazer o deploy no Google Cloud Run; o Google diz que o AI Studio é grátis, com planos pagos para tráfego alto. O <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a> é o editor de código do Google centrado em agentes, com plano individual de US$ 0 e limites semanais de uso. Quer desenhar as telas antes? O @T(stitch) é a nossa escolha para ir do prompt à interface em <a href="@R/pt/use-cases/best-ai-for-ui-design/index.html">Melhor IA para design de UI</a>. Evite o Firebase Studio em projetos novos: ele <a href="https://firebase.google.com/docs/studio/migrating-project" rel="noopener" target="_blank">fechou para novos cadastros em 22 de junho de 2026 e será desligado em 22 de março de 2027</a>.</p>""",
  "es": """<ul>
<li><b>Nunca has programado y quieres una web app con login y base de datos:</b> empieza con @T(lovable) o @T(bolt). Los dos tienen plan gratuito para probar la idea antes de pagar.</li>
<li><b>Quieres un front-end pulido en React/Next.js con deploy en Vercel:</b> @T(v0).</li>
<li><b>Quieres todo, incluido el hosting, en una pestaña del navegador:</b> @T(replit). Su página de precios no muestra plan gratuito.</li>
<li><b>Te manejas en un editor de código, o el proyecto va a crecer más allá de un builder:</b> @T(cursor) o @T(windsurf).</li>
</ul>
<p><b>Lovable vs Bolt vs v0:</b> Lovable y Bolt convierten un prompt en una app full-stack en el navegador, con autenticación y base de datos. v0 destaca en la interfaz y encaja mejor si ya despliegas en Vercel.</p>
<p><b>Cursor vs Devin Desktop:</b> los dos son editores de código completos con IA. Desde oct. de 2026, el plan Plus de Cursor (8 US$) solo usa los modelos propios de Cursor, y Claude o GPT se cobran aparte, a precio de API, desde Premium (30 US$). El Pro de Devin Desktop (20 US$) incluye modelos punteros de OpenAI, Anthropic y Google. Si quieres Claude o GPT en el editor por una tarifa fija, compara los dos antes de suscribirte.</p>
<p><b>También vale la pena:</b> <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, otro creador de apps a partir de prompts, con plan gratuito (de pago desde 16 US$/mes en anual).</p>
<p><b>Opciones gratuitas de Google (comprobadas el 23 de oct. de 2026):</b> el modo Build de <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a> convierte un prompt en una web app en el navegador y puede desplegarla en Google Cloud Run; Google dice que AI Studio es gratis, con planes de pago para mucho tráfico. <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a> es el editor de código de Google centrado en agentes, con un plan individual de 0 US$ y límites de uso semanales. ¿Quieres diseñar las pantallas primero? @T(stitch) es nuestra opción para pasar del prompt a la interfaz en <a href="@R/es/use-cases/best-ai-for-ui-design/index.html">Mejor IA para diseño de UI</a>. Evita Firebase Studio para proyectos nuevos: <a href="https://firebase.google.com/docs/studio/migrating-project" rel="noopener" target="_blank">cerró a nuevos registros el 22 de junio de 2026 y se apagará el 22 de marzo de 2027</a>.</p>"""},
 "best-ai-coding-agents": {
  "en": """<p><b>Cursor vs Claude Code vs Codex:</b> pick by where you want to work.</p><ul>
<li><b>In the terminal, on multi-file changes:</b> @T(claude-code). It needs Claude Pro ($20/mo) or Max; it isn't on the free plan.</li>
<li><b>In an editor where you review each change:</b> @T(cursor). Cloud agents start on the $30 Premium plan, and Claude or GPT models are billed at API list price.</li>
<li><b>Hand off several tasks in parallel and review PRs:</b> @T(codex). You can try it on ChatGPT's free plan, and ChatGPT Plus ($20/mo) covers regular use.</li>
<li><b>Your team lives on GitHub:</b> @T(copilot). It has a free plan, and Pro at $10/mo is the cheapest paid option here.</li>
<li><b>Want to pay nothing or pick your own model:</b> @T(opencode). It's free and open source.</li>
<li><b>Want to delegate whole tickets:</b> @T(devin). Cloud agents start on the $20/mo Pro plan.</li>
</ul>
<p><b>Also worth a look:</b> <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, an open-source coding agent you can run in your editor or terminal.</p>
<p><b>Free from Google (checked Oct 23, 2026):</b> <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, an agent-first editor and CLI with a $0 individual plan (weekly rate limits), and <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>, a beta agent that works on your GitHub repo and opens pull requests, with 15 tasks a day free.</p>""",
  "pt-BR": """<p><b>Cursor vs Claude Code vs Codex:</b> escolha pelo lugar onde você quer trabalhar.</p><ul>
<li><b>No terminal, em mudanças em vários arquivos:</b> @T(claude-code). Exige Claude Pro (US$ 20/mês) ou Max; não está no plano grátis.</li>
<li><b>Num editor, revisando cada mudança:</b> @T(cursor). Os agentes na nuvem começam no Premium (US$ 30), e os modelos Claude ou GPT são cobrados pelo preço de tabela da API.</li>
<li><b>Delegar várias tarefas em paralelo e revisar PRs:</b> @T(codex). Dá para testar no plano grátis do ChatGPT, e o ChatGPT Plus (US$ 20/mês) cobre o uso frequente.</li>
<li><b>Seu time vive no GitHub:</b> @T(copilot). Tem plano grátis, e o Pro, a US$ 10/mês, é a opção paga mais barata desta lista.</li>
<li><b>Quer não pagar nada ou escolher seu próprio modelo:</b> @T(opencode). É grátis e open source.</li>
<li><b>Quer delegar tickets inteiros:</b> @T(devin). Os agentes na nuvem começam no Pro, a US$ 20/mês.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, um agente de código open source que roda no editor ou no terminal.</p>
<p><b>Grátis, do Google (conferido em 23 de out. de 2026):</b> o <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, editor e CLI centrado em agentes com plano individual de US$ 0 (limites semanais), e o <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>, agente em beta que trabalha no seu repositório do GitHub e abre pull requests, com 15 tarefas por dia grátis.</p>""",
  "es": """<p><b>Cursor vs Claude Code vs Codex:</b> elige según dónde quieras trabajar.</p><ul>
<li><b>En la terminal, con cambios en varios archivos:</b> @T(claude-code). Requiere Claude Pro (20 US$/mes) o Max; no está en el plan gratuito.</li>
<li><b>En un editor, revisando cada cambio:</b> @T(cursor). Los agentes en la nube empiezan en Premium (30 US$), y los modelos Claude o GPT se cobran a precio de lista de la API.</li>
<li><b>Delegar varias tareas en paralelo y revisar PRs:</b> @T(codex). Puedes probarlo en el plan gratuito de ChatGPT, y ChatGPT Plus (20 US$/mes) cubre el uso habitual.</li>
<li><b>Tu equipo vive en GitHub:</b> @T(copilot). Tiene plan gratuito, y Pro, a 10 US$/mes, es la opción de pago más barata de esta lista.</li>
<li><b>No quieres pagar nada o quieres elegir tu propio modelo:</b> @T(opencode). Es gratis y de código abierto.</li>
<li><b>Quieres delegar tickets completos:</b> @T(devin). Los agentes en la nube empiezan en Pro, a 20 US$/mes.</li>
</ul>
<p><b>También vale la pena:</b> <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, un agente de código abierto que funciona en el editor o en la terminal.</p>
<p><b>Gratis, de Google (comprobado el 23 de oct. de 2026):</b> <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, un editor y CLI centrado en agentes con plan individual de 0 US$ (límites semanales), y <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>, un agente en beta que trabaja en tu repositorio de GitHub y abre pull requests, con 15 tareas al día gratis.</p>"""},
 "best-ai-for-fixing-broken-code": {
  "en": """<ul>
<li><b>One error and a few files:</b> paste them into @T(claude) or @T(chatgpt). Both have free plans.</li>
<li><b>Fix it where the red squiggle is:</b> @T(copilot) (free plan available) or @T(cursor).</li>
<li><b>Errors that only show up in production:</b> @T(sentry). Its Developer plan is free for one user.</li>
<li><b>A failing test suite:</b> @T(claude-code) can run the tests and iterate until they pass. It needs Claude Pro or Max.</li>
</ul>""",
  "pt-BR": """<ul>
<li><b>Um erro e poucos arquivos:</b> cole tudo no @T(claude) ou no @T(chatgpt). Os dois têm plano grátis.</li>
<li><b>Corrigir onde está o sublinhado vermelho:</b> @T(copilot) (tem plano grátis) ou @T(cursor).</li>
<li><b>Erros que só aparecem em produção:</b> @T(sentry). O plano Developer é grátis para um usuário.</li>
<li><b>Uma suíte de testes falhando:</b> o @T(claude-code) roda os testes e repete até passarem. Exige Claude Pro ou Max.</li>
</ul>""",
  "es": """<ul>
<li><b>Un error y pocos archivos:</b> pégalos en @T(claude) o en @T(chatgpt). Los dos tienen plan gratuito.</li>
<li><b>Arreglarlo donde está el subrayado rojo:</b> @T(copilot) (tiene plan gratuito) o @T(cursor).</li>
<li><b>Errores que solo aparecen en producción:</b> @T(sentry). Su plan Developer es gratis para un usuario.</li>
<li><b>Una batería de tests que falla:</b> @T(claude-code) ejecuta los tests y repite hasta que pasan. Requiere Claude Pro o Max.</li>
</ul>"""},
 "best-ai-for-game-prototyping": {
  "en": """<ul>
<li><b>A playable browser game from a prompt:</b> @T(rosebud). The free plan starts you with 8,000 credits.</li>
<li><b>A real engine (Godot, Unity, Phaser):</b> @T(cursor) writes the scripts while you play-test.</li>
<li><b>Art you plan to sell:</b> @T(scenario) keeps a consistent style, but free-plan outputs are for personal and evaluation use only, so budget for a paid plan.</li>
<li><b>3D blockouts:</b> @T(meshy) (100 free credits a month). <b>Music:</b> @T(suno). <b>Voices and sound effects:</b> @T(elevenlabs). All three have free plans.</li>
</ul>
<p><b>Also worth a look:</b> <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, a free, open-source, no-code game engine with AI assistance, if you'd rather not write engine code at all.</p>
<p><b>Free quick tests from Google (checked Oct 23, 2026):</b> <a href="https://gemini.google/overview/canvas/" rel="noopener" target="_blank">Gemini Canvas</a>, available to all Gemini users, turns a prompt into a small working game you can share by link, and <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a>'s Build mode has a gallery of 2D and 3D games you can remix.</p>""",
  "pt-BR": """<ul>
<li><b>Um jogo jogável no navegador a partir de um prompt:</b> @T(rosebud). O plano grátis começa com 8.000 créditos.</li>
<li><b>Uma engine de verdade (Godot, Unity, Phaser):</b> o @T(cursor) escreve os scripts enquanto você testa.</li>
<li><b>Arte que você pretende vender:</b> o @T(scenario) mantém um estilo consistente, mas o que sai do plano grátis é só para uso pessoal e avaliação; reserve verba para um plano pago.</li>
<li><b>Blocos 3D:</b> @T(meshy) (100 créditos grátis por mês). <b>Música:</b> @T(suno). <b>Vozes e efeitos sonoros:</b> @T(elevenlabs). Os três têm plano grátis.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, uma engine de jogos grátis, open source e no-code, com assistência de IA, se você prefere não escrever código de engine.</p>
<p><b>Testes rápidos e grátis do Google (conferidos em 23 de out. de 2026):</b> o <a href="https://gemini.google/overview/canvas/" rel="noopener" target="_blank">Gemini Canvas</a>, disponível para todos os usuários do Gemini, transforma um prompt em um pequeno jogo funcionando que você compartilha por link, e o modo Build do <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a> tem uma galeria de jogos 2D e 3D para remixar.</p>""",
  "es": """<ul>
<li><b>Un juego jugable en el navegador a partir de un prompt:</b> @T(rosebud). El plan gratuito empieza con 8.000 créditos.</li>
<li><b>Un motor de verdad (Godot, Unity, Phaser):</b> @T(cursor) escribe los scripts mientras tú pruebas el juego.</li>
<li><b>Arte que piensas vender:</b> @T(scenario) mantiene un estilo coherente, pero lo que generas en el plan gratuito es solo para uso personal y de evaluación; reserva presupuesto para un plan de pago.</li>
<li><b>Bloques 3D:</b> @T(meshy) (100 créditos gratis al mes). <b>Música:</b> @T(suno). <b>Voces y efectos de sonido:</b> @T(elevenlabs). Los tres tienen plan gratuito.</li>
</ul>
<p><b>También vale la pena:</b> <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, un motor de juegos gratuito, de código abierto y no-code, con asistencia de IA, si prefieres no escribir código de motor.</p>
<p><b>Pruebas rápidas y gratis de Google (comprobadas el 23 de oct. de 2026):</b> <a href="https://gemini.google/overview/canvas/" rel="noopener" target="_blank">Gemini Canvas</a>, disponible para todos los usuarios de Gemini, convierte un prompt en un pequeño juego funcional que puedes compartir con un enlace, y el modo Build de <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a> tiene una galería de juegos 2D y 3D para remezclar.</p>"""},
 "best-ai-for-video-youtube": {
  "en": """<ul>
<li><b>Talking-head videos:</b> @T(descript) lets you edit the transcript like a doc. It has a free plan.</li>
<li><b>Generated b-roll:</b> @T(runway) has a free plan to try it. @T(veo) needs a paid Google AI plan (from $4.99/mo in the US).</li>
<li><b>Voiceover or dubbing:</b> @T(elevenlabs) (free plan: 10k credits a month).</li>
<li><b>Shorts from long videos:</b> @T(opus) (free trial, then from $15/mo).</li>
<li><b>Everyday edits on a $0 budget:</b> @T(capcut). Auto-captions need Pro.</li>
<li><b>No camera at all:</b> @T(heygen) avatars (free plan; Creator from $29/mo).</li>
</ul>""",
  "pt-BR": """<ul>
<li><b>Vídeos de pessoa falando para a câmera:</b> o @T(descript) deixa você editar a transcrição como um documento. Tem plano grátis.</li>
<li><b>B-roll gerado por IA:</b> o @T(runway) tem plano grátis para testar. O @T(veo) exige um plano pago do Google AI (a partir de US$ 4,99/mês nos EUA).</li>
<li><b>Narração ou dublagem:</b> @T(elevenlabs) (plano grátis: 10 mil créditos por mês).</li>
<li><b>Shorts a partir de vídeos longos:</b> @T(opus) (teste grátis, depois a partir de US$ 15/mês).</li>
<li><b>Edição do dia a dia sem gastar:</b> @T(capcut). As legendas automáticas exigem o Pro.</li>
<li><b>Sem aparecer na câmera:</b> avatares do @T(heygen) (plano grátis; Creator a partir de US$ 29/mês).</li>
</ul>""",
  "es": """<ul>
<li><b>Vídeos de alguien hablando a cámara:</b> @T(descript) te deja editar la transcripción como un documento. Tiene plan gratuito.</li>
<li><b>B-roll generado con IA:</b> @T(runway) tiene plan gratuito para probar. @T(veo) requiere un plan de pago de Google AI (desde 4,99 US$/mes en EE. UU.).</li>
<li><b>Locución o doblaje:</b> @T(elevenlabs) (plan gratuito: 10.000 créditos al mes).</li>
<li><b>Shorts a partir de vídeos largos:</b> @T(opus) (prueba gratuita y luego desde 15 US$/mes).</li>
<li><b>Edición diaria sin gastar:</b> @T(capcut). Los subtítulos automáticos requieren Pro.</li>
<li><b>Sin salir en cámara:</b> avatares de @T(heygen) (plan gratuito; Creator desde 29 US$/mes).</li>
</ul>"""},
}
