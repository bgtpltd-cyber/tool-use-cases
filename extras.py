"""Verified, dated extras for use-case pages (en, pt-BR, es only; noindexed locales show none).
PRICES: copied from each tool's official pricing page on PRICES_CHECKED. Re-check before changing the date.
GUIDES: 'how to choose' blocks for the top 5 pages, built only from the picks' verdicts and the verified prices/facts below."""
PRICES_CHECKED = "2026-10-22"
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
}
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
<p><b>Also worth a look:</b> <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, another prompt-to-app builder with a free plan (paid from $16/mo billed yearly).</p>""",
  "pt-BR": """<ul>
<li><b>Nunca programou e quer um web app com login e banco de dados:</b> comece pelo @T(lovable) ou pelo @T(bolt). Os dois têm plano grátis para testar a ideia antes de pagar.</li>
<li><b>Quer um front-end React/Next.js caprichado com deploy na Vercel:</b> @T(v0).</li>
<li><b>Quer tudo, inclusive hospedagem, numa aba do navegador:</b> @T(replit). A página de preços não lista plano grátis.</li>
<li><b>Já se vira num editor de código, ou o projeto vai crescer além de um builder:</b> @T(cursor) ou @T(windsurf).</li>
</ul>
<p><b>Lovable vs Bolt vs v0:</b> Lovable e Bolt transformam um prompt em um app full-stack no navegador, com autenticação e banco de dados. O v0 se destaca na interface e encaixa melhor se você já faz deploy na Vercel.</p>
<p><b>Cursor vs Devin Desktop:</b> os dois são editores de código completos com IA. Desde out. de 2026, o plano Plus do Cursor (US$ 8) roda só os modelos do próprio Cursor, e Claude ou GPT são cobrados à parte, pelo preço da API, a partir do Premium (US$ 30). O Pro do Devin Desktop (US$ 20) inclui modelos de ponta da OpenAI, Anthropic e Google. Se você quer Claude ou GPT no editor por um valor fixo, compare os dois antes de assinar.</p>
<p><b>Vale olhar também:</b> o <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, outro builder de apps a partir de prompts, com plano grátis (pago a partir de US$ 16/mês no anual).</p>""",
  "es": """<ul>
<li><b>Nunca has programado y quieres una web app con login y base de datos:</b> empieza con @T(lovable) o @T(bolt). Los dos tienen plan gratuito para probar la idea antes de pagar.</li>
<li><b>Quieres un front-end pulido en React/Next.js con deploy en Vercel:</b> @T(v0).</li>
<li><b>Quieres todo, incluido el hosting, en una pestaña del navegador:</b> @T(replit). Su página de precios no muestra plan gratuito.</li>
<li><b>Te manejas en un editor de código, o el proyecto va a crecer más allá de un builder:</b> @T(cursor) o @T(windsurf).</li>
</ul>
<p><b>Lovable vs Bolt vs v0:</b> Lovable y Bolt convierten un prompt en una app full-stack en el navegador, con autenticación y base de datos. v0 destaca en la interfaz y encaja mejor si ya despliegas en Vercel.</p>
<p><b>Cursor vs Devin Desktop:</b> los dos son editores de código completos con IA. Desde oct. de 2026, el plan Plus de Cursor (8 US$) solo usa los modelos propios de Cursor, y Claude o GPT se cobran aparte, a precio de API, desde Premium (30 US$). El Pro de Devin Desktop (20 US$) incluye modelos punteros de OpenAI, Anthropic y Google. Si quieres Claude o GPT en el editor por una tarifa fija, compara los dos antes de suscribirte.</p>
<p><b>También vale la pena:</b> <a href="https://base44.com" rel="noopener" target="_blank">Base44</a>, otro creador de apps a partir de prompts, con plan gratuito (de pago desde 16 US$/mes en anual).</p>"""},
 "best-ai-coding-agents": {
  "en": """<p><b>Cursor vs Claude Code vs Codex:</b> pick by where you want to work.</p><ul>
<li><b>In the terminal, on multi-file changes:</b> @T(claude-code). It needs Claude Pro ($20/mo) or Max; it isn't on the free plan.</li>
<li><b>In an editor where you review each change:</b> @T(cursor). Cloud agents start on the $30 Premium plan, and Claude or GPT models are billed at API list price.</li>
<li><b>Hand off several tasks in parallel and review PRs:</b> @T(codex). You can try it on ChatGPT's free plan, and ChatGPT Plus ($20/mo) covers regular use.</li>
<li><b>Your team lives on GitHub:</b> @T(copilot). It has a free plan, and Pro at $10/mo is the cheapest paid option here.</li>
<li><b>Want to pay nothing or pick your own model:</b> @T(opencode). It's free and open source.</li>
<li><b>Want to delegate whole tickets:</b> @T(devin). Cloud agents start on the $20/mo Pro plan.</li>
</ul>
<p><b>Also worth a look:</b> <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, an open-source coding agent you can run in your editor or terminal.</p>""",
  "pt-BR": """<p><b>Cursor vs Claude Code vs Codex:</b> escolha pelo lugar onde você quer trabalhar.</p><ul>
<li><b>No terminal, em mudanças em vários arquivos:</b> @T(claude-code). Exige Claude Pro (US$ 20/mês) ou Max; não está no plano grátis.</li>
<li><b>Num editor, revisando cada mudança:</b> @T(cursor). Os agentes na nuvem começam no Premium (US$ 30), e os modelos Claude ou GPT são cobrados pelo preço de tabela da API.</li>
<li><b>Delegar várias tarefas em paralelo e revisar PRs:</b> @T(codex). Dá para testar no plano grátis do ChatGPT, e o ChatGPT Plus (US$ 20/mês) cobre o uso frequente.</li>
<li><b>Seu time vive no GitHub:</b> @T(copilot). Tem plano grátis, e o Pro, a US$ 10/mês, é a opção paga mais barata desta lista.</li>
<li><b>Quer não pagar nada ou escolher seu próprio modelo:</b> @T(opencode). É grátis e open source.</li>
<li><b>Quer delegar tickets inteiros:</b> @T(devin). Os agentes na nuvem começam no Pro, a US$ 20/mês.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, um agente de código open source que roda no editor ou no terminal.</p>""",
  "es": """<p><b>Cursor vs Claude Code vs Codex:</b> elige según dónde quieras trabajar.</p><ul>
<li><b>En la terminal, con cambios en varios archivos:</b> @T(claude-code). Requiere Claude Pro (20 US$/mes) o Max; no está en el plan gratuito.</li>
<li><b>En un editor, revisando cada cambio:</b> @T(cursor). Los agentes en la nube empiezan en Premium (30 US$), y los modelos Claude o GPT se cobran a precio de lista de la API.</li>
<li><b>Delegar varias tareas en paralelo y revisar PRs:</b> @T(codex). Puedes probarlo en el plan gratuito de ChatGPT, y ChatGPT Plus (20 US$/mes) cubre el uso habitual.</li>
<li><b>Tu equipo vive en GitHub:</b> @T(copilot). Tiene plan gratuito, y Pro, a 10 US$/mes, es la opción de pago más barata de esta lista.</li>
<li><b>No quieres pagar nada o quieres elegir tu propio modelo:</b> @T(opencode). Es gratis y de código abierto.</li>
<li><b>Quieres delegar tickets completos:</b> @T(devin). Los agentes en la nube empiezan en Pro, a 20 US$/mes.</li>
</ul>
<p><b>También vale la pena:</b> <a href="https://cline.bot" rel="noopener" target="_blank">Cline</a>, un agente de código abierto que funciona en el editor o en la terminal.</p>"""},
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
<p><b>Also worth a look:</b> <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, a free, open-source, no-code game engine with AI assistance, if you'd rather not write engine code at all.</p>""",
  "pt-BR": """<ul>
<li><b>Um jogo jogável no navegador a partir de um prompt:</b> @T(rosebud). O plano grátis começa com 8.000 créditos.</li>
<li><b>Uma engine de verdade (Godot, Unity, Phaser):</b> o @T(cursor) escreve os scripts enquanto você testa.</li>
<li><b>Arte que você pretende vender:</b> o @T(scenario) mantém um estilo consistente, mas o que sai do plano grátis é só para uso pessoal e avaliação; reserve verba para um plano pago.</li>
<li><b>Blocos 3D:</b> @T(meshy) (100 créditos grátis por mês). <b>Música:</b> @T(suno). <b>Vozes e efeitos sonoros:</b> @T(elevenlabs). Os três têm plano grátis.</li>
</ul>
<p><b>Vale olhar também:</b> o <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, uma engine de jogos grátis, open source e no-code, com assistência de IA, se você prefere não escrever código de engine.</p>""",
  "es": """<ul>
<li><b>Un juego jugable en el navegador a partir de un prompt:</b> @T(rosebud). El plan gratuito empieza con 8.000 créditos.</li>
<li><b>Un motor de verdad (Godot, Unity, Phaser):</b> @T(cursor) escribe los scripts mientras tú pruebas el juego.</li>
<li><b>Arte que piensas vender:</b> @T(scenario) mantiene un estilo coherente, pero lo que generas en el plan gratuito es solo para uso personal y de evaluación; reserva presupuesto para un plan de pago.</li>
<li><b>Bloques 3D:</b> @T(meshy) (100 créditos gratis al mes). <b>Música:</b> @T(suno). <b>Voces y efectos de sonido:</b> @T(elevenlabs). Los tres tienen plan gratuito.</li>
</ul>
<p><b>También vale la pena:</b> <a href="https://gdevelop.io" rel="noopener" target="_blank">GDevelop</a>, un motor de juegos gratuito, de código abierto y no-code, con asistencia de IA, si prefieres no escribir código de motor.</p>"""},
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
