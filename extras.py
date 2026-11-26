"""Verified, dated extras for use-case pages (en, pt-BR, es only; noindexed locales show none).
PRICES: copied from each tool's official pricing page (or, for open-source tools, its official repo license) on price_date(tool). Re-check before changing the date.
GUIDES: 'how to choose' blocks for selected pages, built only from the picks' verdicts and the verified prices/facts below."""
PRICES_CHECKED = "2026-10-22"  # default check date for PRICES entries not listed in PRICE_DATES
# tool: (en, pt-BR, es, official pricing source)
PRICES = {
 "cursor": ("Free plan with limited agent use. Plus $8/mo runs only Cursor's own models (Grok, Composer); Premium $30/mo adds cloud agents and Claude/GPT models billed at API list price. Sold as part of The X Subscription since Oct 2026.",
            "Plano grátis com uso limitado do agente. O Plus (US$ 8/mês) roda só os modelos do próprio Cursor (Grok, Composer); o Premium (US$ 30/mês) adiciona agentes na nuvem e modelos Claude/GPT cobrados pelo preço de tabela da API. Vendido como parte da The X Subscription desde out. de 2026.",
            "Plan gratuito con uso limitado del agente. Plus (8 US$/mes) solo usa los modelos propios de Cursor (Grok, Composer); Premium (30 US$/mes) añade agentes en la nube y modelos Claude/GPT cobrados a precio de lista de la API. Se vende dentro de The X Subscription desde oct. de 2026.",
            "https://cursor.com/pricing"),
 "lovable": ("Free plan: 5 build credits a day (up to 30 a month). Paid plans add a monthly credit balance.",
             "Plano grátis: 5 créditos de construção por dia (até 30 por mês). Os planos pagos somam um saldo mensal de créditos.",
             "Plan gratuito: 5 créditos de construcción al día (hasta 30 al mes). Los planes de pago añaden un saldo mensual de créditos.",
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
 "claude-code": ("Included with Claude Pro ($20/mo, or $17/mo billed yearly), Max ($100/mo) and Ultra ($200/mo). Not on the free plan.",
                 "Incluído no Claude Pro (US$ 20/mês, ou US$ 17/mês no anual), no Max (US$ 100/mês) e no Ultra (US$ 200/mês). Não está no plano grátis.",
                 "Incluido en Claude Pro (20 US$/mes, o 17 US$/mes en anual), Max (100 US$/mes) y Ultra (200 US$/mes). No está en el plan gratuito.",
                 "https://claude.com/pricing"),
 "claude": ("Free plan. Pro $20/mo ($17/mo billed yearly); Max $100/mo; Ultra $200/mo.",
            "Plano grátis. Pro: US$ 20/mês (US$ 17/mês no anual); Max: US$ 100/mês; Ultra: US$ 200/mês.",
            "Plan gratuito. Pro: 20 US$/mes (17 US$/mes en anual); Max: 100 US$/mes; Ultra: 200 US$/mes.",
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
 "rosebud": ("Free plan starts you with 10,000 credits, no card needed. Paid plans include Pro at $50/mo.",
             "O plano grátis começa com 10.000 créditos, sem cartão. Entre os planos pagos está o Pro, a US$ 50/mês.",
             "El plan gratuito empieza con 10.000 créditos, sin tarjeta. Entre los planes de pago está Pro, a 50 US$/mes.",
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
 "perplexity": ("Free plan with limited Pro Search and Research. Pro $20/mo ($17/mo billed yearly / $200 a year); Max $200/mo ($167/mo billed yearly / $2,000 a year).",
   "Plano grátis com Pro Search e Research limitados. Pro: US$ 20/mês (US$ 17/mês no anual / US$ 200 por ano); Max: US$ 200/mês (US$ 167/mês no anual / US$ 2.000 por ano).",
   "Plan gratuito con Pro Search e Research limitados. Pro: 20 US$/mes (17 US$/mes en anual / 200 US$ al año); Max: 200 US$/mes (167 US$/mes en anual / 2.000 US$ al año).",
   "https://www.perplexity.ai/hub/pricing"),
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
 "gamma": ("Free plan with 400 one-time credits (up to 10 slides per prompt; exports to PDF, PPTX, PNG and Google Slides). Plus $9/mo and Pro $18/mo per seat, billed yearly ($108 and $216 a year).",
   "Plano grátis com 400 créditos únicos (até 10 slides por prompt; exporta para PDF, PPTX, PNG e Google Slides). Plus: US$ 9/mês e Pro: US$ 18/mês por usuário, no anual (US$ 108 e US$ 216 por ano).",
   "Plan gratuito con 400 créditos únicos (hasta 10 diapositivas por prompt; exporta a PDF, PPTX, PNG y Google Slides). Plus: 9 US$/mes y Pro: 18 US$/mes por usuario, en anual (108 US$ y 216 US$ al año).",
   "https://gamma.app/pricing"),
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
 "railway": ("30-day free trial with $5 of credits, no card needed, then a Free plan with $1 of usage a month. Hobby $5/mo including $5 of usage; Pro $20/mo per workspace including $20 of usage.",
   "Teste grátis de 30 dias com US$ 5 em créditos, sem cartão, e depois um plano Free com US$ 1 de uso por mês. Hobby: US$ 5/mês com US$ 5 de uso incluídos; Pro: US$ 20/mês por workspace com US$ 20 de uso incluídos.",
   "Prueba gratuita de 30 días con 5 US$ en créditos, sin tarjeta, y después un plan Free con 1 US$ de uso al mes. Hobby: 5 US$/mes con 5 US$ de uso incluidos; Pro: 20 US$/mes por workspace con 20 US$ de uso incluidos.",
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
 "mem": ("No new paid subscriptions and all charging paused: Mem is winding down. Notes go read-only Dec 18, 2026; Mem shuts down Jan 15, 2027.",
   "Sem novas assinaturas pagas e cobranças suspensas: o Mem está encerrando. As notas ficam só leitura em 18 de dez. de 2026; o Mem fecha em 15 de jan. de 2027.",
   "Sin nuevas suscripciones de pago y cobros pausados: Mem está cerrando. Las notas pasan a solo lectura el 18 de dic. de 2026; Mem cierra el 15 de ene. de 2027.",
   "https://get.mem.ai/pricing"),
 "onenote-word-copilot": ("Copilot in OneNote and Word is included with Microsoft 365 Personal ($9.99/mo or $99.99/yr) and Family ($12.99/mo or $129.99/yr; AI for the subscription owner only). Premium ($19.99/mo or $199.99/yr) and Pro ($99.99/mo, monthly billing only) include the same in-app Copilot with higher usage limits. Microsoft 365 Basic does not include AI features. For work, it is included with Business Standard with Copilot ($23.50 per user/mo billed yearly) and Business Premium with Copilot ($32.00 per user/mo billed yearly), or as the Microsoft 365 Copilot Business add-on ($21.00 per user/mo billed yearly).",
   "O Copilot no OneNote e no Word vem no Microsoft 365 Personal (US$ 9,99/mês ou US$ 99,99/ano) e no Family (US$ 12,99/mês ou US$ 129,99/ano; a IA é só para o dono da assinatura). O Premium (US$ 19,99/mês ou US$ 199,99/ano) e o Pro (US$ 99,99/mês, só cobrança mensal) incluem o mesmo Copilot nos apps, com limites de uso mais altos. O Microsoft 365 Basic não inclui recursos de IA. No trabalho, ele vem no Business Standard with Copilot (US$ 23,50 por usuário/mês no anual) e no Business Premium with Copilot (US$ 32,00 por usuário/mês no anual), ou como o adicional Microsoft 365 Copilot Business (US$ 21,00 por usuário/mês no anual).",
   "Copilot en OneNote y Word está incluido en Microsoft 365 Personal (9,99 US$/mes o 99,99 US$/año) y Family (12,99 US$/mes o 129,99 US$/año; la IA es solo para el titular de la suscripción). Premium (19,99 US$/mes o 199,99 US$/año) y Pro (99,99 US$/mes, solo facturación mensual) incluyen el mismo Copilot en las apps, con límites de uso más altos. Microsoft 365 Basic no incluye funciones de IA. En el trabajo, viene en Business Standard with Copilot (23,50 US$ por usuario/mes en anual) y Business Premium with Copilot (32,00 US$ por usuario/mes en anual), o como el complemento Microsoft 365 Copilot Business (21,00 US$ por usuario/mes en anual).",
   "https://www.microsoft.com/en-us/copilot/pricing/individuals"),
}
PRICE_DATES = {k: "2026-10-23" for k in ['notion-ai', 'midjourney', 'ideogram', 'grammarly', 'grok', 'n8n', 'make', 'zapier', 'framer', 'figma', 'uizard', 'aiva', 'clearscope', 'julius', 'beautiful-ai', 'tripo', 'rodin', 'fireflies', 'otter', 'grain', 'langchain', 'llamaindex', 'langgraph', 'crewai', 'ms-agent-framework', 'openai-agents', 'ollama', 'wxt', 'vercel', 'netlify', 'railway', 'looka', 'helpscout', 'firecrawl', 'apify', 'browserbase', 'postman', 'bruno', 'mem']}  # entries checked on their official pricing page / repo on Oct 23, 2026
PRICE_DATES.update({k: "2026-11-06" for k in ['claude', 'claude-code', 'perplexity', 'gemini', 'notebooklm', 'elicit']})  # re-checked Nov 6, 2026 on official pricing pages (Perplexity also confirmed via Perplexity Help Center plan prices)
PRICE_DATES.update({k: "2026-11-12" for k in ['vercel', 'netlify', 'railway']})  # re-checked Nov 12, 2026 on official pricing pages
PRICE_DATES.update({k: "2026-11-17" for k in ['postman', 'bruno']})  # re-checked Nov 17, 2026 on official pricing pages (prices unchanged; Postman Free lists 100 AI credits)
PRICE_DATES.update({k: "2026-11-18" for k in ['claude', 'langchain', 'llamaindex']})  # re-checked Nov 18, 2026: Claude prices unchanged on claude.com/pricing; LangChain and LlamaIndex MIT on official GitHub repos
PRICE_DATES.update({k: "2026-11-19" for k in ['n8n', 'make', 'zapier']})  # re-checked Nov 19, 2026 on official pricing pages (unchanged: n8n Cloud Starter 240/yr and Pro 10k 600/yr in EUR, Make Free 1,000 credits/mo, Zapier Free 100 tasks/mo and Professional from $19.99/mo)
PRICE_DATES.update({k: "2026-11-20" for k in ['wxt']})  # re-checked Nov 20, 2026: WXT still MIT on its official GitHub repo (latest release v0.21.5, Oct 26, 2026)
PRICE_DATES.update({k: "2026-11-23" for k in ['fireflies', 'otter', 'grain', 'notion-ai']})  # re-checked Nov 23, 2026 on official pricing pages (unchanged: Fireflies Pro $10/seat yearly or $18 monthly, Business $19 yearly; Otter Basic free with 300 min/mo, Pro $8.33 yearly or $16.99 monthly, Business $19.99 yearly; Grain free for individuals, team seats $19; Notion AI Meeting Notes on Business $20/member yearly)
PRICE_DATES.update({k: "2026-11-24" for k in ['mem', 'notion-ai', 'onenote-word-copilot']})  # re-checked Nov 24, 2026: get.mem.ai/pricing and the Nov 16, 2026 shutdown post (no new paid plans, read-only Dec 18, 2026, shutdown Jan 15, 2027); notion.com/pricing unchanged (Plus $10, Business $20 per member/mo billed yearly; Custom Agents free to try, then $10 per 1,000 Notion credits); Microsoft 365 Copilot on microsoft.com/en-us/copilot/pricing/individuals and /business (Personal $9.99/mo or $99.99/yr, Family $12.99/mo or $129.99/yr, Premium $19.99/mo or $199.99/yr, Pro $99.99/mo monthly billing only; Business Standard with Copilot $23.50 and Business Premium with Copilot $32.00 per user/mo billed yearly; Copilot Business add-on $21.00 per user/mo billed yearly). Copilot Pro is not listed for sale on those pages.
PRICE_DATES.update({k: "2026-11-25" for k in ['gamma', 'beautiful-ai']})  # checked Nov 25, 2026 on gamma.app/pricing (Free 400 one-time credits, 10 slides/prompt, PDF/PPTX/PNG/Google Slides export; Plus $9 and Pro $18 per seat/mo billed annually = $108/$216 a year; Ultra not quoted because the help center says it is monthly-only while the page shows an annual price) and beautiful.ai/pricing (14-day trial, card required; Pro $14.50/mo billed annually; Team $40 per user/mo billed annually per its FAQ)
PRICE_DATES.update({k: "2026-11-26" for k in ['claude', 'chatgpt', 'grammarly', 'gemini', 'notion-ai']})  # re-checked Nov 26, 2026: claude.com/pricing (Free with up to 5 Projects; Pro $17/mo yearly or $20 monthly; Max $100; Ultra $200), chatgpt.com/pricing (Free, Go, Plus, Pro listed) + OpenAI Help Center "What is ChatGPT Plus?" ($20/month), grammarly.com/plans (Free 100 AI prompts/mo; Pro $12 with 2,000 prompts/member/mo), gemini.google/subscriptions US (Plus $4.99/mo with Gemini in Gmail; Pro $19.99/mo with Gemini in Gmail and Docs; Ultra $99.99 or $199.99/mo), notion.com/pricing (Plus $10, Business $20 per seat/mo)
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
<p><b>Free from Google (checked Oct 23, 2026):</b> <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, an agent-first editor and CLI with a $0 individual plan (weekly rate limits).</p>
<p><b>Jules is shutting down (checked Oct 31, 2026):</b> Google is winding down <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>. Sessions can continue until Nov 11, 2026; after that it is read-only until it shuts down on Dec 31, 2026, so don't start new work there.</p>""",
  "pt-BR": """<p><b>Cursor vs Claude Code vs Codex:</b> escolha pelo lugar onde você quer trabalhar.</p><ul>
<li><b>No terminal, em mudanças em vários arquivos:</b> @T(claude-code). Exige Claude Pro (US$ 20/mês) ou Max; não está no plano grátis.</li>
<li><b>Num editor, revisando cada mudança:</b> @T(cursor). Os agentes na nuvem começam no Premium (US$ 30), e os modelos Claude ou GPT são cobrados pelo preço de tabela da API.</li>
<li><b>Delegar várias tarefas em paralelo e revisar PRs:</b> @T(codex). Dá para testar no plano grátis do ChatGPT, e o ChatGPT Plus (US$ 20/mês) cobre o uso frequente.</li>
<li><b>Seu time vive no GitHub:</b> @T(copilot). Tem plano grátis, e o Pro, a US$ 10/mês, é a opção paga mais barata desta lista.</li>
<li><b>Quer não pagar nada ou escolher seu próprio modelo:</b> @T(opencode). É grátis e open source.</li>
<li><b>Quer delegar tickets inteiros:</b> @T(devin). Os agentes na nuvem começam no Pro, a US$ 20/mês.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, um agente de código open source que roda no editor ou no terminal.</p>
<p><b>Grátis, do Google (conferido em 23 de out. de 2026):</b> o <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, editor e CLI centrado em agentes com plano individual de US$ 0 (limites semanais).</p>
<p><b>O Jules vai ser desativado (conferido em 31 de out. de 2026):</b> o Google está encerrando o <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>. Dá para continuar as sessões até 11 de nov. de 2026; depois disso, ele fica só para leitura até ser desativado em 31 de dez. de 2026. Por isso, não comece trabalhos novos nele.</p>""",
  "es": """<p><b>Cursor vs Claude Code vs Codex:</b> elige según dónde quieras trabajar.</p><ul>
<li><b>En la terminal, con cambios en varios archivos:</b> @T(claude-code). Requiere Claude Pro (20 US$/mes) o Max; no está en el plan gratuito.</li>
<li><b>En un editor, revisando cada cambio:</b> @T(cursor). Los agentes en la nube empiezan en Premium (30 US$), y los modelos Claude o GPT se cobran a precio de lista de la API.</li>
<li><b>Delegar varias tareas en paralelo y revisar PRs:</b> @T(codex). Puedes probarlo en el plan gratuito de ChatGPT, y ChatGPT Plus (20 US$/mes) cubre el uso habitual.</li>
<li><b>Tu equipo vive en GitHub:</b> @T(copilot). Tiene plan gratuito, y Pro, a 10 US$/mes, es la opción de pago más barata de esta lista.</li>
<li><b>No quieres pagar nada o quieres elegir tu propio modelo:</b> @T(opencode). Es gratis y de código abierto.</li>
<li><b>Quieres delegar tickets completos:</b> @T(devin). Los agentes en la nube empiezan en Pro, a 20 US$/mes.</li>
</ul>
<p><b>También vale la pena:</b> <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, un agente de código abierto que funciona en el editor o en la terminal.</p>
<p><b>Gratis, de Google (comprobado el 23 de oct. de 2026):</b> <a href="https://antigravity.google" rel="noopener" target="_blank">Google Antigravity</a>, un editor y CLI centrado en agentes con plan individual de 0 US$ (límites semanales).</p>
<p><b>Jules va a cerrar (comprobado el 31 de oct. de 2026):</b> Google está cerrando <a href="https://jules.google" rel="noopener" target="_blank">Jules</a>. Puedes seguir con tus sesiones hasta el 11 de nov. de 2026; después pasa a modo de solo lectura hasta que cierre el 31 de dic. de 2026. Por eso, no empieces trabajo nuevo ahí.</p>"""},
 "best-ai-for-fixing-broken-code": {
  "en": """<ul>
<li><b>One error and a few files:</b> paste them into @T(claude) or @T(chatgpt). Both have free plans.</li>
<li><b>Fix it where the red squiggle is:</b> @T(copilot) (free plan available) or @T(cursor).</li>
<li><b>Errors that only show up in production:</b> @T(sentry). Its Developer plan is free for one user.</li>
<li><b>A failing test suite:</b> @T(claude-code) can run the tests and iterate until they pass. It needs Claude Pro, Max or Ultra.</li>
</ul>""",
  "pt-BR": """<ul>
<li><b>Um erro e poucos arquivos:</b> cole tudo no @T(claude) ou no @T(chatgpt). Os dois têm plano grátis.</li>
<li><b>Corrigir onde está o sublinhado vermelho:</b> @T(copilot) (tem plano grátis) ou @T(cursor).</li>
<li><b>Erros que só aparecem em produção:</b> @T(sentry). O plano Developer é grátis para um usuário.</li>
<li><b>Uma suíte de testes falhando:</b> o @T(claude-code) roda os testes e repete até passarem. Exige Claude Pro, Max ou Ultra.</li>
</ul>""",
  "es": """<ul>
<li><b>Un error y pocos archivos:</b> pégalos en @T(claude) o en @T(chatgpt). Los dos tienen plan gratuito.</li>
<li><b>Arreglarlo donde está el subrayado rojo:</b> @T(copilot) (tiene plan gratuito) o @T(cursor).</li>
<li><b>Errores que solo aparecen en producción:</b> @T(sentry). Su plan Developer es gratis para un usuario.</li>
<li><b>Una batería de tests que falla:</b> @T(claude-code) ejecuta los tests y repite hasta que pasan. Requiere Claude Pro, Max o Ultra.</li>
</ul>"""},
 "best-ai-for-game-prototyping": {
  "en": """<ul>
<li><b>A playable browser game from a prompt:</b> @T(rosebud). The free plan starts you with 10,000 credits.</li>
<li><b>A real engine (Godot, Unity, Phaser):</b> @T(cursor) writes the scripts while you play-test.</li>
<li><b>Art you plan to sell:</b> @T(scenario) keeps a consistent style, but free-plan outputs are for personal and evaluation use only, so budget for a paid plan.</li>
<li><b>3D blockouts:</b> @T(meshy) (100 free credits a month). <b>Music:</b> @T(suno). <b>Voices and sound effects:</b> @T(elevenlabs). All three have free plans.</li>
</ul>
<p><b>Also worth a look:</b> <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, a free, open-source, no-code game engine with AI assistance, if you'd rather not write engine code at all.</p>
<p><b>Free quick tests from Google (checked Oct 23, 2026):</b> <a href="https://gemini.google/overview/canvas/" rel="noopener" target="_blank">Gemini Canvas</a>, available to all Gemini users, turns a prompt into a small working game you can share by link, and <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a>'s Build mode has a gallery of 2D and 3D games you can remix.</p>""",
  "pt-BR": """<ul>
<li><b>Um jogo jogável no navegador a partir de um prompt:</b> @T(rosebud). O plano grátis começa com 10.000 créditos.</li>
<li><b>Uma engine de verdade (Godot, Unity, Phaser):</b> o @T(cursor) escreve os scripts enquanto você testa.</li>
<li><b>Arte que você pretende vender:</b> o @T(scenario) mantém um estilo consistente, mas o que sai do plano grátis é só para uso pessoal e avaliação; reserve verba para um plano pago.</li>
<li><b>Blocos 3D:</b> @T(meshy) (100 créditos grátis por mês). <b>Música:</b> @T(suno). <b>Vozes e efeitos sonoros:</b> @T(elevenlabs). Os três têm plano grátis.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, uma engine de jogos grátis, open source e no-code, com assistência de IA, se você prefere não escrever código de engine.</p>
<p><b>Testes rápidos e grátis do Google (conferidos em 23 de out. de 2026):</b> o <a href="https://gemini.google/overview/canvas/" rel="noopener" target="_blank">Gemini Canvas</a>, disponível para todos os usuários do Gemini, transforma um prompt em um pequeno jogo funcionando que você compartilha por link, e o modo Build do <a href="https://aistudio.google.com/vibe-code" rel="noopener" target="_blank">Google AI Studio</a> tem uma galeria de jogos 2D e 3D para remixar.</p>""",
  "es": """<ul>
<li><b>Un juego jugable en el navegador a partir de un prompt:</b> @T(rosebud). El plan gratuito empieza con 10.000 créditos.</li>
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
 "best-ai-for-research": {
  "en": """<ul>
<li><b>Fast answers with citations from the live web:</b> @T(perplexity). Free plan available; Pro is $20/mo ($17/mo billed yearly).</li>
<li><b>Your own PDFs and notes:</b> @T(notebooklm) (free with a Google Account). Grounded answers and audio overviews from sources you upload.</li>
<li><b>Long, cited reports on one topic:</b> @T(chatgpt) Deep Research or @T(gemini) Deep Research. Both have free plans; Gemini Deep Research is on the free Gemini plan.</li>
<li><b>Academic papers and literature reviews:</b> @T(elicit). Free Basic plan; Plus from $11 per user/mo billed yearly.</li>
<li><b>What people are saying right now on X:</b> @T(grok).</li>
</ul>""",
  "pt-BR": """<ul>
<li><b>Respostas rápidas com citações da web ao vivo:</b> @T(perplexity). Tem plano grátis; o Pro custa US$ 20/mês (US$ 17/mês no anual).</li>
<li><b>Seus próprios PDFs e anotações:</b> @T(notebooklm) (grátis com uma Conta Google). Respostas ancoradas nas fontes que você envia, mais audio overviews.</li>
<li><b>Relatórios longos e citados sobre um tema:</b> Deep Research do @T(chatgpt) ou Deep Research do @T(gemini). Os dois têm plano grátis; o Deep Research do Gemini está no plano grátis do Gemini.</li>
<li><b>Artigos acadêmicos e revisões de literatura:</b> @T(elicit). Plano Basic grátis; Plus a partir de US$ 11 por usuário/mês no anual.</li>
<li><b>O que as pessoas estão dizendo agora no X:</b> @T(grok).</li>
</ul>""",
  "es": """<ul>
<li><b>Respuestas rápidas con citas de la web en vivo:</b> @T(perplexity). Tiene plan gratuito; Pro cuesta 20 US$/mes (17 US$/mes en anual).</li>
<li><b>Tus propios PDFs y notas:</b> @T(notebooklm) (gratis con una cuenta de Google). Respuestas ancladas a las fuentes que subes, más audio overviews.</li>
<li><b>Informes largos y citados sobre un tema:</b> Deep Research de @T(chatgpt) o Deep Research de @T(gemini). Ambos tienen plan gratuito; Deep Research de Gemini está en el plan gratuito de Gemini.</li>
<li><b>Artículos académicos y revisiones de literatura:</b> @T(elicit). Plan Basic gratuito; Plus desde 11 US$ por usuario/mes en anual.</li>
<li><b>Lo que la gente está diciendo ahora en X:</b> @T(grok).</li>
</ul>"""},
 "best-ai-for-agent-frameworks": {
  "en": """<ul>
<li><b>First agent, want to ship this week:</b> @T(openai-agents). Small API with tools, handoffs and tracing built in; it comes in Python and TypeScript.</li>
<li><b>Long-running agents that must survive retries and wait for a human:</b> @T(langgraph). You define the steps and state yourself, so it's more work up front but easier to debug in production. Also available in TypeScript.</li>
<li><b>Quick multi-agent prototype with roles like "researcher" and "writer":</b> @T(crewai). Fastest to a demo; plan to add guardrails before you rely on it.</li>
<li><b>Your team is on Azure or .NET:</b> @T(ms-agent-framework), Microsoft's successor to AutoGen and Semantic Kernel, in Python and .NET.</li>
<li><b>Whatever you pick:</b> build your tools as @T(mcp) servers so you can move them to another framework later.</li>
</ul>
<p><small>All four frameworks are open source under the MIT license, so the cost is the models you call. Licenses and languages checked on each project's official GitHub repository on Nov 9, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Primeiro agente, quer colocar no ar esta semana:</b> @T(openai-agents). API pequena com ferramentas, handoffs e tracing embutidos; existe em Python e TypeScript.</li>
<li><b>Agentes de longa duração que precisam sobreviver a novas tentativas e esperar uma pessoa:</b> @T(langgraph). Você define os passos e o estado, então dá mais trabalho no início, mas é mais fácil depurar em produção. Também existe em TypeScript.</li>
<li><b>Protótipo rápido com vários agentes em papéis como "pesquisador" e "redator":</b> @T(crewai). O caminho mais rápido para uma demo; adicione controles antes de depender dele.</li>
<li><b>Sua equipe usa Azure ou .NET:</b> @T(ms-agent-framework), sucessor da Microsoft para AutoGen e Semantic Kernel, em Python e .NET.</li>
<li><b>Seja qual for a escolha:</b> crie suas ferramentas como servidores @T(mcp) para poder levá-las a outro framework depois.</li>
</ul>
<p><small>Os quatro frameworks são open source sob a licença MIT; o custo são os modelos que você chama. Licenças e linguagens conferidas no repositório oficial de cada projeto no GitHub em 9 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Primer agente y quieres lanzarlo esta semana:</b> @T(openai-agents). API pequeña con herramientas, handoffs y tracing integrados; existe en Python y TypeScript.</li>
<li><b>Agentes de larga duración que deben sobrevivir a reintentos y esperar a una persona:</b> @T(langgraph). Tú defines los pasos y el estado, así que cuesta más al principio, pero es más fácil de depurar en producción. También existe en TypeScript.</li>
<li><b>Prototipo rápido con varios agentes en roles como "investigador" y "redactor":</b> @T(crewai). El camino más rápido a una demo; añade controles antes de depender de él.</li>
<li><b>Tu equipo usa Azure o .NET:</b> @T(ms-agent-framework), el sucesor de Microsoft para AutoGen y Semantic Kernel, en Python y .NET.</li>
<li><b>Elijas lo que elijas:</b> crea tus herramientas como servidores @T(mcp) para poder llevarlas a otro framework más adelante.</li>
</ul>
<p><small>Los cuatro frameworks son de código abierto con licencia MIT; el coste son los modelos que llamas. Licencias y lenguajes comprobados en el repositorio oficial de cada proyecto en GitHub el 9 de nov. de 2026.</small></p>"""},
 "best-ai-for-running-local-models": {
  "en": """<ul>
<li><b>First time running a model on your own machine:</b> @T(ollama). One command downloads and runs an open model, and it serves a local API other tools can use.</li>
<li><b>You want strong reasoning without sending data to a cloud API:</b> run an open-weight @T(deepseek) model through Ollama. Pick a model size that fits your RAM or GPU memory.</li>
<li><b>An offline coding agent:</b> point @T(opencode) at your Ollama server. Both projects document this setup.</li>
<li><b>Images, not text:</b> @T(sd). Most people run it through ComfyUI; plan on a capable GPU and some tinkering.</li>
</ul>
<p><small>Ollama and OpenCode are open source under the MIT license, and ComfyUI under GPL-3.0, so running them costs nothing beyond your hardware. Licenses checked on each project's official GitHub repository, and the Ollama setup on the Ollama and OpenCode docs, on Nov 10, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Primeira vez rodando um modelo na sua própria máquina:</b> @T(ollama). Um comando baixa e roda um modelo aberto, e ele oferece uma API local que outras ferramentas podem usar.</li>
<li><b>Você quer bom raciocínio sem enviar dados para uma API na nuvem:</b> rode um modelo de pesos abertos da @T(deepseek) pelo Ollama. Escolha um tamanho de modelo que caiba na sua RAM ou na memória da GPU.</li>
<li><b>Um agente de programação offline:</b> aponte o @T(opencode) para o seu servidor Ollama. Os dois projetos documentam essa configuração.</li>
<li><b>Imagens, não texto:</b> @T(sd). A maioria roda pelo ComfyUI; conte com uma boa GPU e algum ajuste.</li>
</ul>
<p><small>Ollama e OpenCode são open source sob a licença MIT, e o ComfyUI sob a GPL-3.0; rodar custa apenas o seu hardware. Licenças conferidas no repositório oficial de cada projeto no GitHub, e a configuração com Ollama na documentação do Ollama e do OpenCode, em 10 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Primera vez ejecutando un modelo en tu propia máquina:</b> @T(ollama). Un comando descarga y ejecuta un modelo abierto, y ofrece una API local que otras herramientas pueden usar.</li>
<li><b>Quieres buen razonamiento sin enviar datos a una API en la nube:</b> ejecuta un modelo de pesos abiertos de @T(deepseek) con Ollama. Elige un tamaño de modelo que quepa en tu RAM o en la memoria de la GPU.</li>
<li><b>Un agente de programación sin conexión:</b> conecta @T(opencode) a tu servidor Ollama. Ambos proyectos documentan esta configuración.</li>
<li><b>Imágenes, no texto:</b> @T(sd). La mayoría lo ejecuta con ComfyUI; cuenta con una buena GPU y algo de ajuste.</li>
</ul>
<p><small>Ollama y OpenCode son de código abierto con licencia MIT, y ComfyUI con GPL-3.0; ejecutarlos solo cuesta tu hardware. Licencias comprobadas en el repositorio oficial de cada proyecto en GitHub, y la configuración con Ollama en la documentación de Ollama y OpenCode, el 10 de nov. de 2026.</small></p>"""},
 "best-ai-for-scraping": {
  "en": """<ul>
<li><b>You need clean page text for an LLM or a RAG pipeline:</b> @T(firecrawl). It returns clean Markdown or structured data, and its docs list a keyless MCP server URL for Search, Scrape and Parse that Claude Code, Codex CLI, Cursor and OpenCode can add.</li>
<li><b>A common site (maps, social, e-commerce):</b> check the Apify Store first. @T(apify) listed 117,381 Actors on Nov 11, 2026, so a ready-made scraper may already exist.</li>
<li><b>The page needs a login, clicks or a real browser:</b> @T(browserbase) with its open-source Stagehand framework.</li>
<li><b>An unusual one-off site:</b> have @T(claude-code) or @T(cursor) write and debug a small scraper against the real page.</li>
<li><b>Whatever you pick:</b> read the site's terms and robots.txt before you scrape it.</li>
</ul>
<p><small>Firecrawl is open source under AGPL-3.0 and Stagehand under MIT (official GitHub repositories); the MCP setup is from the Firecrawl docs and the Actor count from the Apify Store. All checked Nov 11, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você precisa de texto limpo das páginas para um LLM ou um pipeline de RAG:</b> @T(firecrawl). Ele devolve Markdown limpo ou dados estruturados, e a documentação traz a URL de um servidor MCP sem chave para Search, Scrape e Parse, que Claude Code, Codex CLI, Cursor e OpenCode podem adicionar.</li>
<li><b>Um site comum (mapas, redes sociais, e-commerce):</b> veja primeiro a Apify Store. A @T(apify) listava 117.381 Actors em 11 de nov. de 2026, então talvez já exista um scraper pronto.</li>
<li><b>A página exige login, cliques ou um navegador de verdade:</b> @T(browserbase) com o framework open source Stagehand.</li>
<li><b>Um site incomum, de uso único:</b> peça ao @T(claude-code) ou ao @T(cursor) para escrever e depurar um pequeno scraper na página real.</li>
<li><b>Seja qual for a escolha:</b> leia os termos do site e o robots.txt antes de fazer scraping.</li>
</ul>
<p><small>O Firecrawl é open source sob a AGPL-3.0 e o Stagehand sob a MIT (repositórios oficiais no GitHub); a configuração MCP vem da documentação do Firecrawl e o número de Actors da Apify Store. Tudo conferido em 11 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Necesitas texto limpio de las páginas para un LLM o un pipeline de RAG:</b> @T(firecrawl). Devuelve Markdown limpio o datos estructurados, y su documentación indica la URL de un servidor MCP sin clave para Search, Scrape y Parse que Claude Code, Codex CLI, Cursor y OpenCode pueden añadir.</li>
<li><b>Un sitio común (mapas, redes sociales, e-commerce):</b> revisa primero la Apify Store. @T(apify) listaba 117.381 Actors el 11 de nov. de 2026, así que quizá ya exista un scraper listo.</li>
<li><b>La página requiere inicio de sesión, clics o un navegador real:</b> @T(browserbase) con su framework de código abierto Stagehand.</li>
<li><b>Un sitio poco común, de una sola vez:</b> pide a @T(claude-code) o a @T(cursor) que escriban y depuren un pequeño scraper contra la página real.</li>
<li><b>Elijas lo que elijas:</b> lee los términos del sitio y su robots.txt antes de hacer scraping.</li>
</ul>
<p><small>Firecrawl es de código abierto con licencia AGPL-3.0 y Stagehand con MIT (repositorios oficiales en GitHub); la configuración MCP proviene de la documentación de Firecrawl y el número de Actors de la Apify Store. Todo comprobado el 11 de nov. de 2026.</small></p>"""},
 "best-ai-for-api-testing": {
  "en": """<ul>
<li><b>Your team already keeps its APIs in Postman:</b> stay in @T(postman). The Free plan includes 100 AI credits; Solo ($9/mo billed yearly) gives 400 AI credits a month, and Team is $19 per user/mo billed yearly.</li>
<li><b>You want collections in git and no cloud account:</b> use @T(bruno). Its open-source app is free, and its plain-file collections sit next to your code, where an AI editor can read and update them.</li>
<li><b>The tests live in your codebase (pytest, Jest and similar):</b> have @T(cursor) write and fix them next to the API code, and run them in your normal test command.</li>
<li><b>You have a spec or a failing response but no tool set up:</b> paste the OpenAPI spec or the error into @T(claude) for test cases and edge cases, or into @T(chatgpt) for quick test scripts and mock data.</li>
<li><b>Before you trust generated tests:</b> run them against a test environment first and check each assertion matches the documented behavior, not just what the API returns today.</li>
</ul>
<p><small>Postman and Bruno plan details checked on each official pricing page on Nov 17, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Seu time já guarda as APIs no Postman:</b> continue no @T(postman). O plano Free inclui 100 créditos de IA; o Solo (US$ 9/mês no anual) dá 400 créditos de IA por mês, e o Team custa US$ 19 por usuário/mês no anual.</li>
<li><b>Você quer as coleções no git e sem conta na nuvem:</b> use o @T(bruno). O app open source é grátis, e as coleções em arquivos simples ficam junto do seu código, onde um editor com IA consegue lê-las e atualizá-las.</li>
<li><b>Os testes ficam no seu código (pytest, Jest e parecidos):</b> peça ao @T(cursor) para escrevê-los e corrigi-los ao lado do código da API e rode-os no seu comando de testes de sempre.</li>
<li><b>Você tem uma spec ou uma resposta com erro, mas nenhuma ferramenta configurada:</b> cole a spec OpenAPI ou o erro no @T(claude) para gerar casos de teste e casos-limite, ou no @T(chatgpt) para scripts de teste rápidos e dados de exemplo.</li>
<li><b>Antes de confiar em testes gerados:</b> rode-os primeiro num ambiente de teste e confira se cada asserção bate com o comportamento documentado, e não só com o que a API responde hoje.</li>
</ul>
<p><small>Detalhes dos planos do Postman e do Bruno conferidos na página oficial de preços de cada um em 17 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Tu equipo ya tiene sus APIs en Postman:</b> quédate en @T(postman). El plan Free incluye 100 créditos de IA; Solo (9 US$/mes en anual) da 400 créditos de IA al mes, y Team cuesta 19 US$ por usuario/mes en anual.</li>
<li><b>Quieres las colecciones en git y sin cuenta en la nube:</b> usa @T(bruno). Su app de código abierto es gratis, y sus colecciones en archivos simples viven junto a tu código, donde un editor con IA puede leerlas y actualizarlas.</li>
<li><b>Los tests viven en tu código (pytest, Jest y similares):</b> pide a @T(cursor) que los escriba y los corrija junto al código de la API, y ejecútalos con tu comando de tests habitual.</li>
<li><b>Tienes una spec o una respuesta con error, pero ninguna herramienta configurada:</b> pega la spec OpenAPI o el error en @T(claude) para obtener casos de prueba y casos límite, o en @T(chatgpt) para scripts de prueba rápidos y datos de ejemplo.</li>
<li><b>Antes de fiarte de tests generados:</b> ejecútalos primero en un entorno de pruebas y comprueba que cada aserción coincide con el comportamiento documentado, no solo con lo que la API responde hoy.</li>
</ul>
<p><small>Detalles de los planes de Postman y Bruno comprobados en la página oficial de precios de cada uno el 17 de nov. de 2026.</small></p>""",
 },
 "best-ai-for-deploy-hosting": {
  "en": """<ul>
<li><b>A Next.js or React app, or anything from v0:</b> @T(vercel). Its pricing page says <code>vercel deploy --temporary</code> deploys a project with no sign-up; the free Hobby plan is for personal, non-commercial use, so plan on Pro ($20/mo) for a business.</li>
<li><b>A static site or simple app on a budget:</b> @T(netlify). The Free plan has a 300-credit limit, and a production deploy costs 15 credits, so batch your changes instead of deploying every small edit.</li>
<li><b>A backend, database or background worker:</b> @T(railway). Billing is per second for what you use; the Free plan includes $1 of usage a month and Hobby $5.</li>
<li><b>A Docker app, or users in several regions:</b> @T(fly), if you're fine with a bit more setup.</li>
<li><b>You never want to touch deploy settings:</b> build and host in one place on @T(replit).</li>
</ul>
<p><small>Vercel, Netlify and Railway plan details checked on each official pricing page on Nov 12, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Um app Next.js ou React, ou qualquer coisa feita no v0:</b> @T(vercel). A página de preços diz que <code>vercel deploy --temporary</code> publica um projeto sem cadastro; o plano Hobby grátis é para uso pessoal e não comercial, então conte com o Pro (US$ 20/mês) para um negócio.</li>
<li><b>Um site estático ou app simples com pouco orçamento:</b> @T(netlify). O plano Free tem limite de 300 créditos, e cada deploy de produção custa 15 créditos, então junte as mudanças em vez de publicar cada pequena edição.</li>
<li><b>Um backend, banco de dados ou worker em segundo plano:</b> @T(railway). A cobrança é por segundo de uso; o plano Free inclui US$ 1 de uso por mês e o Hobby, US$ 5.</li>
<li><b>Um app em Docker, ou usuários em várias regiões:</b> @T(fly), se você aceitar um pouco mais de configuração.</li>
<li><b>Você nunca quer mexer em configuração de deploy:</b> crie e hospede no mesmo lugar com o @T(replit).</li>
</ul>
<p><small>Detalhes dos planos da Vercel, Netlify e Railway conferidos na página oficial de preços de cada uma em 12 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Una app Next.js o React, o cualquier cosa hecha con v0:</b> @T(vercel). Su página de precios dice que <code>vercel deploy --temporary</code> publica un proyecto sin registrarse; el plan Hobby gratuito es para uso personal y no comercial, así que cuenta con Pro (20 US$/mes) para un negocio.</li>
<li><b>Un sitio estático o una app sencilla con poco presupuesto:</b> @T(netlify). El plan Free tiene un límite de 300 créditos y cada deploy de producción cuesta 15 créditos, así que agrupa los cambios en lugar de publicar cada pequeña edición.</li>
<li><b>Un backend, una base de datos o un worker en segundo plano:</b> @T(railway). Cobra por segundo de uso; el plan Free incluye 1 US$ de uso al mes y Hobby, 5 US$.</li>
<li><b>Una app en Docker, o usuarios en varias regiones:</b> @T(fly), si no te importa algo más de configuración.</li>
<li><b>No quieres tocar nunca la configuración de deploy:</b> crea y aloja en un mismo sitio con @T(replit).</li>
</ul>
<p><small>Detalles de los planes de Vercel, Netlify y Railway comprobados en la página oficial de precios de cada una el 12 de nov. de 2026.</small></p>"""},
 "best-ai-for-chatbots-rag": {
  "en": """<ul>
<li><b>A team assistant over your docs, inside a chat app:</b> a @T(claude) Project. The free plan allows up to 5 Projects; sharing a Project with teammates needs a Team or Enterprise plan (Team from $20 per seat a month billed yearly, $25 billed monthly).</li>
<li><b>Your team already works in ChatGPT:</b> a @T(chatgpt) Project with your files and instructions. Don't build a new custom GPT: OpenAI plans to retire custom GPTs on Dec 11, 2026, and points ongoing work to Projects and shared, tool-connected GPTs to plugins.</li>
<li><b>Grounded answers for yourself, with zero setup:</b> @T(notebooklm), free with a Google Account. It is for personal research, not for embedding on a site.</li>
<li><b>A chatbot on your own site or app:</b> you need code. Use @T(llamaindex) when ingesting and retrieving messy documents is the hard part, and @T(langchain) when you need many integrations. Both are open source under the MIT license.</li>
<li><b>A small custom bot without a framework:</b> have @T(cursor) or @T(claude-code) write a lean RAG app, then test it with real questions from your users before launch.</li>
</ul>
<p><small>Claude Project limits and Team prices are from Claude's pricing page, the custom GPT retirement date from the OpenAI Help Center, and the MIT licenses from the official GitHub repositories. All checked Nov 18, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Um assistente da equipe que responde com base nos seus documentos, dentro de um app de chat:</b> um Project do @T(claude). O plano grátis permite até 5 Projects; compartilhar um Project com colegas exige o plano Team ou Enterprise (Team a partir de US$ 20 por usuário/mês no anual, US$ 25 no mensal).</li>
<li><b>Sua equipe já trabalha no ChatGPT:</b> um Project do @T(chatgpt) com seus arquivos e instruções. Não crie um GPT personalizado novo: a OpenAI planeja aposentar os GPTs personalizados em 11 de dez. de 2026 e indica Projects para trabalho contínuo e plugins para GPTs compartilhados ou conectados a ferramentas.</li>
<li><b>Respostas baseadas nas suas fontes, só para você, sem configurar nada:</b> @T(notebooklm), grátis com uma Conta do Google. Serve para pesquisa pessoal, não para incorporar num site.</li>
<li><b>Um chatbot no seu próprio site ou app:</b> aí precisa de código. Use @T(llamaindex) quando a parte difícil é ingerir e recuperar documentos bagunçados, e @T(langchain) quando você precisa de muitas integrações. Os dois são open source sob a licença MIT.</li>
<li><b>Um bot pequeno e sob medida, sem framework:</b> peça ao @T(cursor) ou ao @T(claude-code) um app de RAG enxuto e teste com perguntas reais dos seus usuários antes de lançar.</li>
</ul>
<p><small>Limites de Projects e preços do Team conferidos na página de preços do Claude, a data de aposentadoria dos GPTs personalizados na Central de Ajuda da OpenAI e as licenças MIT nos repositórios oficiais no GitHub. Tudo conferido em 18 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Un asistente de equipo que responde a partir de tus documentos, dentro de una app de chat:</b> un Project de @T(claude). El plan gratuito permite hasta 5 Projects; compartir un Project con compañeros requiere el plan Team o Enterprise (Team desde 20 US$ por usuario al mes en anual, 25 US$ en mensual).</li>
<li><b>Tu equipo ya trabaja en ChatGPT:</b> un Project de @T(chatgpt) con tus archivos e instrucciones. No crees un GPT personalizado nuevo: OpenAI planea retirar los GPT personalizados el 11 de dic. de 2026 y recomienda Projects para el trabajo continuo y plugins para los GPT compartidos o conectados a herramientas.</li>
<li><b>Respuestas basadas en tus fuentes, solo para ti y sin configurar nada:</b> @T(notebooklm), gratis con una Cuenta de Google. Sirve para investigación personal, no para integrarlo en un sitio.</li>
<li><b>Un chatbot en tu propio sitio o app:</b> ahí necesitas código. Usa @T(llamaindex) cuando lo difícil es ingerir y recuperar documentos desordenados, y @T(langchain) cuando necesitas muchas integraciones. Los dos son de código abierto con licencia MIT.</li>
<li><b>Un bot pequeño a medida, sin framework:</b> pide a @T(cursor) o a @T(claude-code) una app de RAG sencilla y pruébala con preguntas reales de tus usuarios antes de lanzarla.</li>
</ul>
<p><small>Límites de Projects y precios de Team comprobados en la página de precios de Claude, la fecha de retirada de los GPT personalizados en el Centro de ayuda de OpenAI y las licencias MIT en los repositorios oficiales de GitHub. Todo comprobado el 18 de nov. de 2026.</small></p>"""},
 "best-ai-for-automation-workflows": {
  "en": """<ul>
<li><b>You want the easiest setup and your apps are mainstream:</b> @T(zapier). The free plan gives 100 tasks a month with two-step Zaps; multi-step Zaps need Professional, from $19.99 a month. Costs climb with task volume, so check your monthly run count first.</li>
<li><b>Your flows branch a lot and budget matters:</b> @T(make). The free plan includes 1,000 credits a month. Most actions use 1 credit, while router and error-handler modules use none, so complex branching stays cheap.</li>
<li><b>You are a builder and want AI agents or your data on your own server:</b> @T(n8n). The self-hosted Community Edition is free. On n8n Cloud you pay per workflow execution rather than per step, and Starter and Pro are capped with no overage fees.</li>
<li><b>No-code hits a wall:</b> have @T(claude-code) write the script or webhook handler, then call it from your workflow.</li>
<li><b>A one-off, multi-step web task:</b> @T(manus) can do it once. Don't use it for anything that has to run reliably on a schedule.</li>
</ul>
<p><small>Plan details for Zapier, Make and n8n checked on each official pricing page on Nov 19, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você quer a configuração mais fácil e usa apps populares:</b> @T(zapier). O plano grátis dá 100 tarefas por mês com Zaps de dois passos; Zaps com vários passos exigem o Professional, a partir de US$ 19,99 por mês. O custo sobe com o volume de tarefas, então confira antes quantas execuções você faz por mês.</li>
<li><b>Seus fluxos têm muitas ramificações e o orçamento importa:</b> @T(make). O plano grátis inclui 1.000 créditos por mês. A maioria das ações usa 1 crédito, e os módulos de roteador e de tratamento de erros não usam nenhum, então fluxos complexos continuam baratos.</li>
<li><b>Você é builder e quer agentes de IA ou seus dados no seu próprio servidor:</b> @T(n8n). A Community Edition, auto-hospedada, é grátis. No n8n Cloud você paga por execução do workflow, não por passo, e os planos Starter e Pro têm limite fixo, sem cobrança de excedente.</li>
<li><b>O no-code chegou ao limite:</b> peça ao @T(claude-code) o script ou o handler de webhook e chame-o a partir do seu workflow.</li>
<li><b>Uma tarefa web pontual com vários passos:</b> o @T(manus) resolve uma vez. Não use para nada que precise rodar de forma confiável num agendamento.</li>
</ul>
<p><small>Detalhes dos planos do Zapier, do Make e do n8n conferidos na página oficial de preços de cada um em 19 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Quieres la configuración más fácil y usas apps populares:</b> @T(zapier). El plan gratuito da 100 tareas al mes con Zaps de dos pasos; los Zaps de varios pasos requieren Professional, desde 19,99 US$ al mes. El coste sube con el volumen de tareas, así que revisa antes cuántas ejecuciones haces al mes.</li>
<li><b>Tus flujos tienen muchas ramas y el presupuesto importa:</b> @T(make). El plan gratuito incluye 1.000 créditos al mes. La mayoría de las acciones usan 1 crédito, y los módulos de router y de gestión de errores no usan ninguno, así que los flujos complejos siguen siendo baratos.</li>
<li><b>Eres builder y quieres agentes de IA o tus datos en tu propio servidor:</b> @T(n8n). La Community Edition, autoalojada, es gratis. En n8n Cloud pagas por ejecución del workflow, no por paso, y los planes Starter y Pro tienen un tope fijo, sin cargos por exceso.</li>
<li><b>El no-code llega a su límite:</b> pide a @T(claude-code) el script o el handler de webhook y llámalo desde tu workflow.</li>
<li><b>Una tarea web puntual de varios pasos:</b> @T(manus) la resuelve una vez. No lo uses para nada que deba ejecutarse de forma fiable con una programación.</li>
</ul>
<p><small>Detalles de los planes de Zapier, Make y n8n comprobados en la página oficial de precios de cada uno el 19 de nov. de 2026.</small></p>"""},
 "best-ai-for-chrome-extensions": {
  "en": """<ul>
<li><b>You want a working extension today and will test it as you go:</b> @T(cursor). Ask for a Manifest V3 extension, load it unpacked from chrome://extensions, and paste any error from the extension's service worker console back into the chat.</li>
<li><b>You want the whole project scaffolded, permissions included:</b> @T(claude-code). Have it explain every entry in <code>permissions</code> and <code>host_permissions</code>, and remove what you don't need before you publish.</li>
<li><b>It's a tiny one-file tool for yourself:</b> @T(chatgpt) is enough. Reject any answer with <code>"manifest_version": 2</code> or a background page: Chrome has disabled Manifest V2 extensions for all users since Chrome 138, and the Chrome Web Store removed the remaining ones on Aug 31, 2026.</li>
<li><b>You plan to ship to more than one browser or keep it for years:</b> start from @T(wxt), then let your AI tool fill it in. It is MIT-licensed, supports all browsers and both MV2 and MV3, and its latest release is v0.21.5 (Oct 26, 2026).</li>
<li><b>You'd rather write the code yourself:</b> @T(copilot) autocompletes <code>chrome.*</code> API calls in VS Code.</li>
</ul>
<p>To publish on the Chrome Web Store you need a developer account and a one-time registration fee.</p>
<p><small>Manifest V2 timeline and Chrome Web Store registration checked on developer.chrome.com; WXT license, README and release on its official GitHub repo. All checked on Nov 20, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você quer uma extensão funcionando hoje e vai testando no caminho:</b> @T(cursor). Peça uma extensão Manifest V3, carregue-a sem compactação em chrome://extensions e cole no chat qualquer erro do console do service worker da extensão.</li>
<li><b>Você quer o projeto inteiro estruturado, com permissões:</b> @T(claude-code). Peça que explique cada item de <code>permissions</code> e <code>host_permissions</code> e remova o que você não usa antes de publicar.</li>
<li><b>É uma ferramenta pequena, de um arquivo, só para você:</b> o @T(chatgpt) basta. Descarte qualquer resposta com <code>"manifest_version": 2</code> ou background page: o Chrome desativou as extensões Manifest V2 para todos os usuários desde o Chrome 138, e a Chrome Web Store removeu as restantes em 31 de ago. de 2026.</li>
<li><b>Você pretende lançar em mais de um navegador ou manter por anos:</b> comece pelo @T(wxt) e deixe sua ferramenta de IA completar. Tem licença MIT, suporta todos os navegadores e tanto MV2 quanto MV3, e a versão mais recente é a v0.21.5 (26 de out. de 2026).</li>
<li><b>Você prefere escrever o código você mesmo:</b> o @T(copilot) autocompleta chamadas da API <code>chrome.*</code> no VS Code.</li>
</ul>
<p>Para publicar na Chrome Web Store você precisa de uma conta de desenvolvedor e de uma taxa de registro única.</p>
<p><small>Cronograma do Manifest V2 e registro na Chrome Web Store conferidos em developer.chrome.com; licença, README e versão do WXT no repositório oficial no GitHub. Tudo conferido em 20 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Quieres una extensión funcionando hoy y vas probando sobre la marcha:</b> @T(cursor). Pide una extensión Manifest V3, cárgala descomprimida desde chrome://extensions y pega en el chat cualquier error de la consola del service worker de la extensión.</li>
<li><b>Quieres todo el proyecto estructurado, permisos incluidos:</b> @T(claude-code). Pídele que explique cada entrada de <code>permissions</code> y <code>host_permissions</code> y quita lo que no necesites antes de publicar.</li>
<li><b>Es una herramienta pequeña de un solo archivo para ti:</b> con @T(chatgpt) basta. Descarta cualquier respuesta con <code>"manifest_version": 2</code> o una background page: Chrome tiene desactivadas las extensiones Manifest V2 para todos los usuarios desde Chrome 138, y la Chrome Web Store retiró las que quedaban el 31 de ago. de 2026.</li>
<li><b>Piensas publicarla en más de un navegador o mantenerla durante años:</b> empieza con @T(wxt) y deja que tu herramienta de IA la complete. Tiene licencia MIT, es compatible con todos los navegadores y con MV2 y MV3, y su versión más reciente es la v0.21.5 (26 de oct. de 2026).</li>
<li><b>Prefieres escribir el código tú mismo:</b> @T(copilot) autocompleta llamadas a la API <code>chrome.*</code> en VS Code.</li>
</ul>
<p>Para publicar en la Chrome Web Store necesitas una cuenta de desarrollador y pagar una tarifa de registro única.</p>
<p><small>Calendario de Manifest V2 y registro en la Chrome Web Store comprobados en developer.chrome.com; licencia, README y versión de WXT en su repositorio oficial de GitHub. Todo comprobado el 20 de nov. de 2026.</small></p>"""},
 "best-ai-for-meeting-notes": {
  "en": """<ul>
<li><b>You want every call recorded without thinking about it:</b> @T(fireflies). Its bot joins Zoom, Google Meet and Teams calls. The Free plan has unlimited transcription but only limited AI summaries and 400 minutes of storage per team, so most teams end up on Pro ($10 per seat/mo billed yearly, $18 monthly).</li>
<li><b>You want live captions and the most usable free plan:</b> @T(otter). Basic is free with 300 transcription minutes a month and 3 lifetime file imports; Pro is $8.33 per user/mo billed yearly ($16.99 monthly).</li>
<li><b>You run sales or customer calls and share moments, not full notes:</b> @T(grain). It is free for individuals; team seats start at $19 per seat/mo.</li>
<li><b>Your team already writes everything in Notion and doesn't want a bot in the call:</b> @T(notion-ai). AI Meeting Notes is fully included only on the Business plan ($20 per member/mo billed yearly); Free and Plus get a limited trial.</li>
<li><b>You already have a transcript and just want better notes:</b> paste it into @T(claude) and ask for decisions, owners and due dates. It won't record anything for you.</li>
</ul>
<p>Whatever you pick, tell people the call is being recorded and check your company's rules on storing transcripts. To turn notes into docs your team keeps, see <a href="@R/use-cases/best-ai-for-notion-docs/index.html">Best AI for notes and docs</a>.</p>
<p><small>Fireflies, Otter, Grain and Notion plans checked on each official pricing page on Nov 23, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você quer todas as chamadas gravadas sem precisar lembrar:</b> @T(fireflies). O bot entra em chamadas no Zoom, Google Meet e Teams. O plano Free tem transcrição ilimitada, mas resumos com IA limitados e 400 minutos de armazenamento por equipe, então a maioria das equipes acaba no Pro (US$ 10 por assento/mês no anual, US$ 18 no mensal).</li>
<li><b>Você quer legenda ao vivo e o plano grátis mais útil:</b> @T(otter). O Basic é grátis, com 300 minutos de transcrição por mês e 3 importações de arquivo no total; o Pro custa US$ 8,33 por usuário/mês no anual (US$ 16,99 no mensal).</li>
<li><b>Você faz chamadas de vendas ou com clientes e compartilha trechos, não a ata inteira:</b> @T(grain). É grátis para uso individual; os assentos de equipe começam em US$ 19 por assento/mês.</li>
<li><b>Sua equipe já escreve tudo no Notion e não quer um bot na chamada:</b> @T(notion-ai). O AI Meeting Notes completo só vem no plano Business (US$ 20 por membro/mês no anual); Free e Plus têm só um teste limitado.</li>
<li><b>Você já tem a transcrição e só quer notas melhores:</b> cole no @T(claude) e peça decisões, responsáveis e prazos. Ele não grava nada por você.</li>
</ul>
<p>Seja qual for a escolha, avise que a chamada está sendo gravada e confira as regras da sua empresa sobre guardar transcrições. Para transformar as notas em documentos da equipe, veja <a href="@R/pt/use-cases/best-ai-for-notion-docs/index.html">Melhor IA para notas e documentos</a>.</p>
<p><small>Planos do Fireflies, Otter, Grain e Notion conferidos na página oficial de preços de cada um em 23 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>Quieres grabar todas las llamadas sin tener que acordarte:</b> @T(fireflies). Su bot entra en llamadas de Zoom, Google Meet y Teams. El plan Free tiene transcripción ilimitada, pero resúmenes con IA limitados y 400 minutos de almacenamiento por equipo, así que la mayoría de los equipos termina en Pro (10 US$ por asiento/mes en anual, 18 US$ mensual).</li>
<li><b>Quieres subtítulos en vivo y el plan gratuito más útil:</b> @T(otter). Basic es gratis, con 300 minutos de transcripción al mes y 3 importaciones de archivos en total; Pro cuesta 8,33 US$ por usuario/mes en anual (16,99 US$ mensual).</li>
<li><b>Haces llamadas de ventas o con clientes y compartes fragmentos, no el acta completa:</b> @T(grain). Es gratis para uso individual; los asientos de equipo empiezan en 19 US$ por asiento/mes.</li>
<li><b>Tu equipo ya lo escribe todo en Notion y no quiere un bot en la llamada:</b> @T(notion-ai). AI Meeting Notes completo solo viene en el plan Business (20 US$ por miembro/mes en anual); Free y Plus tienen solo una prueba limitada.</li>
<li><b>Ya tienes la transcripción y solo quieres mejores notas:</b> pégala en @T(claude) y pide decisiones, responsables y fechas. No graba nada por ti.</li>
</ul>
<p>Elijas lo que elijas, avisa de que la llamada se está grabando y revisa las normas de tu empresa sobre guardar transcripciones. Para convertir las notas en documentos del equipo, mira <a href="@R/es/use-cases/best-ai-for-notion-docs/index.html">Mejor IA para notas y documentos</a>.</p>
<p><small>Planes de Fireflies, Otter, Grain y Notion comprobados en la página oficial de precios de cada uno el 23 de nov. de 2026.</small></p>"""},
 "best-ai-for-notion-docs": {
  "en": """<ul>
<li><b>Your team's wiki and docs already live in Notion:</b> @T(notion-ai). Free and Plus only include a trial; full Notion AI (Notion Agent, AI Meeting Notes) is on Business at $20 per member/mo billed yearly. Custom Agents are free to try, then $10 per 1,000 Notion credits.</li>
<li><b>Your docs are really trackers, tables and automations:</b> @T(coda). You pay only for Doc Makers; Editors and Viewers are free. Its Docs AI assistant is included on paid plans while in beta, with limited trials on Free.</li>
<li><b>You need one long doc written or rewritten well:</b> @T(claude). Put your reference files in a Project so every draft uses them, then paste the result into your wiki.</li>
<li><b>Your notes and Word documents already live in Microsoft 365:</b> @T(onenote-word-copilot). Copilot in OneNote and Word is included with Personal ($9.99/mo or $99.99/yr) and Family ($12.99/mo or $129.99/yr; AI for the subscription owner only). Premium ($19.99/mo or $199.99/yr) and Pro ($99.99/mo, monthly billing only) include the same in-app Copilot with higher usage limits. Microsoft 365 Basic does not include AI features. For work, it is on Business Standard with Copilot ($23.50 per user/mo billed yearly), Business Premium with Copilot ($32.00 per user/mo billed yearly), or the Microsoft 365 Copilot Business add-on ($21.00 per user/mo billed yearly).</li>
<li><b>You mostly restructure: outlines, summaries, tables from messy notes:</b> @T(chatgpt). It works with any tool because you paste in and paste out.</li>
<li><b>You wanted a personal notes app that organizes itself:</b> don't start on @T(mem). It stopped new paid plans, notes go read-only on Dec 18, 2026 and it shuts down on Jan 15, 2027. If you use it now, export from Settings → Exports before then. If you already work in Microsoft 365, OneNote and Word with Copilot is the closer fit than starting a new notes app.</li>
</ul>
<p>Pick the tool where your docs already live; moving a team wiki is the expensive part, not the AI. To turn calls into notes, see <a href="@R/use-cases/best-ai-for-meeting-notes/index.html">Best AI for meeting notes</a>.</p>
<p><small>Notion plans checked on notion.com/pricing, Superhuman Docs billing on coda.io/pricing, Microsoft 365 Copilot plans on microsoft.com/en-us/copilot/pricing/individuals and microsoft.com/en-us/copilot/pricing/business, and Mem's dates on its pricing page and Nov 16, 2026 shutdown post. All checked on Nov 24, 2026.</small></p>""",
  "pt-BR": """<ul>
<li><b>A wiki e os documentos do seu time já estão no Notion:</b> @T(notion-ai). Free e Plus têm só um teste; o Notion AI completo (Notion Agent, AI Meeting Notes) vem no Business, a US$ 20 por membro/mês no anual. Os Custom Agents são grátis para testar e depois custam US$ 10 por 1.000 créditos do Notion.</li>
<li><b>Seus documentos são, na prática, trackers, tabelas e automações:</b> @T(coda). Você só paga pelos Doc Makers; Editors e Viewers são grátis. O assistente Docs AI vem incluído nos planos pagos enquanto está em beta, com testes limitados no Free.</li>
<li><b>Você precisa de um documento longo bem escrito ou reescrito:</b> @T(claude). Coloque os arquivos de referência em um Project para que todo rascunho os use e depois cole o resultado na sua wiki.</li>
<li><b>Suas notas e documentos do Word já estão no Microsoft 365:</b> @T(onenote-word-copilot). O Copilot no OneNote e no Word vem no Personal (US$ 9,99/mês ou US$ 99,99/ano) e no Family (US$ 12,99/mês ou US$ 129,99/ano; a IA é só para o dono da assinatura). O Premium (US$ 19,99/mês ou US$ 199,99/ano) e o Pro (US$ 99,99/mês, só cobrança mensal) incluem o mesmo Copilot nos apps, com limites de uso mais altos. O Microsoft 365 Basic não inclui recursos de IA. No trabalho, ele vem no Business Standard with Copilot (US$ 23,50 por usuário/mês no anual), no Business Premium with Copilot (US$ 32,00 por usuário/mês no anual) ou no adicional Microsoft 365 Copilot Business (US$ 21,00 por usuário/mês no anual).</li>
<li><b>Você mais reorganiza: estruturas, resumos e tabelas a partir de notas bagunçadas:</b> @T(chatgpt). Funciona com qualquer ferramenta, porque você cola o texto e copia o resultado.</li>
<li><b>Você queria um app de notas pessoais que se organiza sozinho:</b> não comece pelo @T(mem). Ele parou de vender planos pagos, as notas ficam só leitura em 18 de dez. de 2026 e ele fecha em 15 de jan. de 2027. Se você usa hoje, exporte em Settings → Exports antes disso. Se você já trabalha no Microsoft 365, o OneNote e o Word com Copilot encaixam melhor do que começar um app de notas novo.</li>
</ul>
<p>Escolha a ferramenta onde seus documentos já estão; o caro é mudar a wiki do time de lugar, não a IA. Para transformar chamadas em notas, veja <a href="@R/pt/use-cases/best-ai-for-meeting-notes/index.html">Melhor IA para notas de reunião</a>.</p>
<p><small>Planos do Notion conferidos em notion.com/pricing, cobrança do Superhuman Docs em coda.io/pricing, planos do Microsoft 365 Copilot em microsoft.com/en-us/copilot/pricing/individuals e microsoft.com/en-us/copilot/pricing/business, e datas do Mem na página de preços e no anúncio de encerramento de 16 de nov. de 2026. Tudo conferido em 24 de nov. de 2026.</small></p>""",
  "es": """<ul>
<li><b>La wiki y los documentos de tu equipo ya están en Notion:</b> @T(notion-ai). Free y Plus solo incluyen una prueba; Notion AI completo (Notion Agent, AI Meeting Notes) viene en Business, a 20 US$ por miembro/mes en anual. Los Custom Agents se pueden probar gratis y luego cuestan 10 US$ por 1.000 créditos de Notion.</li>
<li><b>Tus documentos son en realidad trackers, tablas y automatizaciones:</b> @T(coda). Solo pagas por los Doc Makers; Editors y Viewers son gratis. El asistente Docs AI viene incluido en los planes de pago mientras está en beta, con pruebas limitadas en Free.</li>
<li><b>Necesitas un documento largo bien escrito o reescrito:</b> @T(claude). Pon tus archivos de referencia en un Project para que cada borrador los use y luego pega el resultado en tu wiki.</li>
<li><b>Tus notas y documentos de Word ya están en Microsoft 365:</b> @T(onenote-word-copilot). Copilot en OneNote y Word viene en Personal (9,99 US$/mes o 99,99 US$/año) y Family (12,99 US$/mes o 129,99 US$/año; la IA es solo para el titular de la suscripción). Premium (19,99 US$/mes o 199,99 US$/año) y Pro (99,99 US$/mes, solo facturación mensual) incluyen el mismo Copilot en las apps, con límites de uso más altos. Microsoft 365 Basic no incluye funciones de IA. En el trabajo, viene en Business Standard with Copilot (23,50 US$ por usuario/mes en anual), Business Premium with Copilot (32,00 US$ por usuario/mes en anual) o el complemento Microsoft 365 Copilot Business (21,00 US$ por usuario/mes en anual).</li>
<li><b>Sobre todo reorganizas: esquemas, resúmenes y tablas a partir de notas desordenadas:</b> @T(chatgpt). Funciona con cualquier herramienta, porque pegas el texto y copias el resultado.</li>
<li><b>Querías una app de notas personales que se organice sola:</b> no empieces con @T(mem). Dejó de vender planes de pago, las notas pasan a solo lectura el 18 de dic. de 2026 y cierra el 15 de ene. de 2027. Si lo usas hoy, exporta desde Settings → Exports antes de esa fecha. Si ya trabajas en Microsoft 365, OneNote y Word con Copilot encajan mejor que empezar una app de notas nueva.</li>
</ul>
<p>Elige la herramienta donde ya están tus documentos; lo caro es mudar la wiki del equipo, no la IA. Para convertir llamadas en notas, mira <a href="@R/es/use-cases/best-ai-for-meeting-notes/index.html">Mejor IA para notas de reuniones</a>.</p>
<p><small>Planes de Notion comprobados en notion.com/pricing, facturación de Superhuman Docs en coda.io/pricing, planes de Microsoft 365 Copilot en microsoft.com/en-us/copilot/pricing/individuals y microsoft.com/en-us/copilot/pricing/business, y fechas de Mem en su página de precios y en el anuncio de cierre del 16 de nov. de 2026. Todo comprobado el 24 de nov. de 2026.</small></p>"""},
 "best-ai-for-presentations": {
  "en": """<ul>
<li><b>You want a good-looking deck from notes or a prompt, fast:</b> @T(gamma). The free plan's 400 one-time credits are enough to try it, and it exports to PowerPoint, PDF and Google Slides. Plus ($9/mo per seat billed yearly) removes the Gamma badge and allows up to 100 slides per prompt.</li>
<li><b>Your team needs every deck to stay on brand:</b> @T(beautiful-ai). Smart Slides keep layouts formatted as you edit. There is no free plan, only a 14-day trial that needs a card; Pro is $14.50/mo billed yearly and Team $40 per user/mo billed yearly.</li>
<li><b>Your decks already live in PowerPoint:</b> @T(powerpoint-copilot). Copilot in PowerPoint is included with Microsoft 365 Personal ($9.99/mo) and Family ($12.99/mo; AI for the subscription owner only), with higher limits on Premium ($19.99/mo). For work it comes with Business Standard with Copilot ($23.50 per user/mo billed yearly) or the Microsoft 365 Copilot Business add-on ($21.00 per user/mo billed yearly).</li>
<li><b>The story is the hard part, not the slides:</b> @T(claude) or @T(chatgpt). Get the outline, slide text and speaker notes right first, then paste them into Gamma or PowerPoint. ChatGPT can also hand you a .pptx file to edit.</li>
</ul>
<p>Whatever you pick, write the outline yourself or with a chatbot first; every tool here makes better slides from a clear outline than from a one-line prompt. If your numbers start in a spreadsheet, see <a href="@R/use-cases/best-ai-for-data-spreadsheets/index.html">Best AI for data and spreadsheets</a>.</p>
<p><small>Gamma plans checked on gamma.app/pricing, Beautiful.ai plans on beautiful.ai/pricing, and Microsoft 365 Copilot plans on microsoft.com/en-us/copilot/pricing/individuals and microsoft.com/en-us/copilot/pricing/business, all on Nov 25, 2026. Regular prices shown; limited-time first-month offers are left out.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você quer uma apresentação bonita a partir de notas ou de um prompt, rápido:</b> @T(gamma). Os 400 créditos únicos do plano grátis bastam para testar, e ele exporta para PowerPoint, PDF e Google Slides. O Plus (US$ 9/mês por usuário no anual) tira o selo do Gamma e permite até 100 slides por prompt.</li>
<li><b>Seu time precisa que toda apresentação siga a marca:</b> @T(beautiful-ai). Os Smart Slides mantêm o layout formatado enquanto você edita. Não há plano grátis, só um teste de 14 dias que pede cartão; o Pro custa US$ 14,50/mês no anual e o Team, US$ 40 por usuário/mês no anual.</li>
<li><b>Suas apresentações já estão no PowerPoint:</b> @T(powerpoint-copilot). O Copilot no PowerPoint vem no Microsoft 365 Personal (US$ 9,99/mês) e no Family (US$ 12,99/mês; a IA é só para o titular da assinatura), com limites maiores no Premium (US$ 19,99/mês). No trabalho, vem no Business Standard with Copilot (US$ 23,50 por usuário/mês no anual) ou no complemento Microsoft 365 Copilot Business (US$ 21,00 por usuário/mês no anual).</li>
<li><b>O difícil é a história, não os slides:</b> @T(claude) ou @T(chatgpt). Acerte primeiro o roteiro, o texto dos slides e as notas do apresentador, depois cole tudo no Gamma ou no PowerPoint. O ChatGPT também pode gerar um arquivo .pptx para você editar.</li>
</ul>
<p>Qualquer que seja a escolha, escreva o roteiro antes, sozinho ou com um chatbot; todas as ferramentas daqui fazem slides melhores a partir de um roteiro claro do que de um prompt de uma linha. Se os seus números começam numa planilha, veja <a href="@R/pt/use-cases/best-ai-for-data-spreadsheets/index.html">Melhor IA para dados e planilhas</a>.</p>
<p><small>Planos do Gamma conferidos em gamma.app/pricing, do Beautiful.ai em beautiful.ai/pricing e do Microsoft 365 Copilot em microsoft.com/en-us/copilot/pricing/individuals e microsoft.com/en-us/copilot/pricing/business, todos em 25 de nov. de 2026. Mostramos os preços normais, sem ofertas temporárias do primeiro mês.</small></p>""",
  "es": """<ul>
<li><b>Quieres una presentación vistosa a partir de notas o de un prompt, rápido:</b> @T(gamma). Los 400 créditos únicos del plan gratuito bastan para probarlo, y exporta a PowerPoint, PDF y Google Slides. Plus (9 US$/mes por usuario en anual) quita el sello de Gamma y permite hasta 100 diapositivas por prompt.</li>
<li><b>Tu equipo necesita que cada presentación respete la marca:</b> @T(beautiful-ai). Las Smart Slides mantienen el diseño ordenado mientras editas. No hay plan gratuito, solo una prueba de 14 días que pide tarjeta; Pro cuesta 14,50 US$/mes en anual y Team, 40 US$ por usuario/mes en anual.</li>
<li><b>Tus presentaciones ya están en PowerPoint:</b> @T(powerpoint-copilot). Copilot en PowerPoint viene con Microsoft 365 Personal (9,99 US$/mes) y Family (12,99 US$/mes; la IA es solo para el titular de la suscripción), con límites más altos en Premium (19,99 US$/mes). En el trabajo, viene con Business Standard with Copilot (23,50 US$ por usuario/mes en anual) o con el complemento Microsoft 365 Copilot Business (21,00 US$ por usuario/mes en anual).</li>
<li><b>Lo difícil es la historia, no las diapositivas:</b> @T(claude) o @T(chatgpt). Primero deja bien el guion, el texto de cada diapositiva y las notas del orador, y luego pégalo en Gamma o PowerPoint. ChatGPT también puede darte un archivo .pptx para editar.</li>
</ul>
<p>Elijas lo que elijas, escribe antes el guion, tú o con un chatbot; todas estas herramientas hacen mejores diapositivas a partir de un guion claro que de un prompt de una línea. Si tus números empiezan en una hoja de cálculo, mira <a href="@R/es/use-cases/best-ai-for-data-spreadsheets/index.html">Mejor IA para datos y hojas de cálculo</a>.</p>
<p><small>Planes de Gamma comprobados en gamma.app/pricing, de Beautiful.ai en beautiful.ai/pricing y de Microsoft 365 Copilot en microsoft.com/en-us/copilot/pricing/individuals y microsoft.com/en-us/copilot/pricing/business, todo el 25 de nov. de 2026. Se muestran los precios normales, sin ofertas temporales del primer mes.</small></p>"""},
 "best-ai-writing-assistants": {
  "en": """<ul>
<li><b>You want prose that sounds like a person wrote it, and a strict editor:</b> @T(claude). The free plan is enough to try it on a real draft and allows up to 5 Projects, so you can keep a style guide and samples in one. Pro is $20/mo, or $17/mo billed yearly.</li>
<li><b>You want many versions fast: headlines, rewrites, tone changes:</b> @T(chatgpt). Ask for five options at once and keep the best lines. The free plan works for this; Plus ($20/mo) adds more messages and uploads.</li>
<li><b>Your drafts and notes already live in Notion:</b> @T(notion-ai). Free and Plus only include a trial of Notion AI; the full version is on Business at $20 per member/mo billed yearly.</li>
<li><b>You need polish everywhere you type, not a chat window:</b> @T(grammarly). Free fixes spelling and grammar and includes 100 AI prompts a month. Pro (from $12/mo) adds full-sentence rewrites, tone suggestions and 2,000 prompts per member a month.</li>
<li><b>You write in Gmail and Google Docs all day:</b> @T(gemini). The Gemini app is free with a Google Account. In the US, Google AI Plus ($4.99/mo) adds Gemini in Gmail; Gemini in Docs is listed from Google AI Pro ($19.99/mo).</li>
</ul>
<p>Whatever you pick, give it your own outline and a sample of your writing first, and read every line before you send or publish. For cold outreach, see <a href="@R/use-cases/best-ai-for-sales-emails/index.html">Best AI for sales emails</a>; for pages meant to rank, see <a href="@R/use-cases/best-ai-for-seo-content/index.html">Best AI for SEO content</a>.</p>
<p><small>Claude plans checked on claude.com/pricing, ChatGPT Plus on OpenAI's Help Center and chatgpt.com/pricing, Grammarly plans on grammarly.com/plans and Google AI plans on gemini.google/subscriptions, all on Nov 26, 2026; Notion plans on notion.com/pricing on Nov 24 and Nov 26, 2026. Regular US prices shown; limited-time offers are left out.</small></p>""",
  "pt-BR": """<ul>
<li><b>Você quer um texto que pareça escrito por uma pessoa, e um editor exigente:</b> @T(claude). O plano grátis basta para testar com um rascunho real e permite até 5 Projects, então dá para guardar um guia de estilo e exemplos em um deles. O Pro custa US$ 20/mês, ou US$ 17/mês no anual.</li>
<li><b>Você quer muitas versões rápido: títulos, reescritas, mudanças de tom:</b> @T(chatgpt). Peça cinco opções de uma vez e fique com as melhores frases. O plano grátis serve para isso; o Plus (US$ 20/mês) dá mais mensagens e uploads.</li>
<li><b>Seus rascunhos e notas já estão no Notion:</b> @T(notion-ai). Free e Plus têm só um teste do Notion AI; a versão completa vem no Business, a US$ 20 por membro/mês no anual.</li>
<li><b>Você precisa de revisão em todo lugar onde digita, não de uma janela de chat:</b> @T(grammarly). O Free corrige ortografia e gramática e inclui 100 prompts de IA por mês. O Pro (a partir de US$ 12/mês) reescreve frases inteiras, sugere ajustes de tom e dá 2.000 prompts por membro por mês.</li>
<li><b>Você escreve no Gmail e no Google Docs o dia todo:</b> @T(gemini). O app Gemini é grátis com uma Conta Google. Nos EUA, o Google AI Plus (US$ 4,99/mês) adiciona o Gemini no Gmail; o Gemini no Docs aparece a partir do Google AI Pro (US$ 19,99/mês).</li>
</ul>
<p>Seja qual for a escolha, entregue antes o seu roteiro e um exemplo do seu texto, e leia cada linha antes de enviar ou publicar. Para prospecção, veja <a href="@R/pt/use-cases/best-ai-for-sales-emails/index.html">Melhor IA para e-mails de vendas</a>; para páginas que precisam ranquear, veja <a href="@R/pt/use-cases/best-ai-for-seo-content/index.html">Melhor IA para conteúdo de SEO</a>.</p>
<p><small>Planos do Claude conferidos em claude.com/pricing, o ChatGPT Plus na Central de Ajuda da OpenAI e em chatgpt.com/pricing, os planos do Grammarly em grammarly.com/plans e os do Google AI em gemini.google/subscriptions, tudo em 26 de nov. de 2026; os planos do Notion em notion.com/pricing em 24 e 26 de nov. de 2026. Preços normais dos EUA; ofertas temporárias ficaram de fora.</small></p>""",
  "es": """<ul>
<li><b>Quieres textos que suenen escritos por una persona, y un editor exigente:</b> @T(claude). El plan gratuito basta para probarlo con un borrador real y permite hasta 5 Projects, así que puedes guardar una guía de estilo y ejemplos en uno. Pro cuesta 20 US$/mes, o 17 US$/mes en anual.</li>
<li><b>Quieres muchas versiones rápido: titulares, reescrituras, cambios de tono:</b> @T(chatgpt). Pide cinco opciones a la vez y quédate con las mejores frases. El plan gratuito sirve para esto; Plus (20 US$/mes) da más mensajes y subidas de archivos.</li>
<li><b>Tus borradores y notas ya están en Notion:</b> @T(notion-ai). Free y Plus solo incluyen una prueba de Notion AI; la versión completa está en Business, a 20 US$ por miembro/mes en anual.</li>
<li><b>Necesitas pulir el texto en todas partes donde escribes, no una ventana de chat:</b> @T(grammarly). Free corrige ortografía y gramática e incluye 100 prompts de IA al mes. Pro (desde 12 US$/mes) reescribe frases completas, sugiere ajustes de tono y da 2.000 prompts por miembro al mes.</li>
<li><b>Escribes en Gmail y Google Docs todo el día:</b> @T(gemini). La app de Gemini es gratis con una cuenta de Google. En EE. UU., Google AI Plus (4,99 US$/mes) añade Gemini en Gmail; Gemini en Docs aparece desde Google AI Pro (19,99 US$/mes).</li>
</ul>
<p>Elijas lo que elijas, dale antes tu propio esquema y una muestra de cómo escribes, y lee cada línea antes de enviar o publicar. Para prospección, mira <a href="@R/es/use-cases/best-ai-for-sales-emails/index.html">Mejor IA para emails de ventas</a>; para páginas que deben posicionar, mira <a href="@R/es/use-cases/best-ai-for-seo-content/index.html">Mejor IA para contenido SEO</a>.</p>
<p><small>Planes de Claude comprobados en claude.com/pricing, ChatGPT Plus en el Centro de ayuda de OpenAI y en chatgpt.com/pricing, los planes de Grammarly en grammarly.com/plans y los de Google AI en gemini.google/subscriptions, todo el 26 de nov. de 2026; los planes de Notion en notion.com/pricing el 24 y el 26 de nov. de 2026. Precios normales de EE. UU.; se dejan fuera las ofertas temporales.</small></p>"""},
}
