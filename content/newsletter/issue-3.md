Hi there,

Between October 26 and 28, GitHub, Replit, OpenAI, Google, Cursor, and Lovable shipped a wave of releases that move coding agents one level up: routing across models automatically, turning plain-Markdown repo jobs into sandboxed GitHub Actions, and letting non-engineers open tested pull requests. One quieter change affects your data: Gemini API now stores requests by default on new paid projects.

Below: which release fits which job, what it costs, and when **not** to use it. Picks verified Oct 28, 2026; privacy heads-up and "Also shipped" re-verified Oct 29, 2026 on each official page.

## This week's picks: The Oct 26–28 coding & repo agent wave

**1. Auto-routing coding tasks across models: GitHub Copilot Fusion (GA, Oct 28)**
Pick Copilot Fusion and GitHub routes each step of a job across models for you. GitHub reports Fusion Max landed within two points of Claude Code with Opus 5.5 Max on the Artificial Analysis Coding Agent Index at roughly half the average API cost per task ([GitHub changelog](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/)).
**Pricing (checked Oct 28, 2026 on [github.com/features/copilot/plans](https://github.com/features/copilot/plans)):** Free tier; Pro $10/mo, Pro+ $39/mo, Max $100/mo, plus Business and Enterprise.
**When NOT to use it:** Reproducible benchmarks or strict test-fix loops where a mid-task model switch changes tool-call behavior. Pin one model, or use [Claude Code](https://claude.com/product/claude-code) (Claude Pro $20/mo or Max from $100/mo).
More options: [Best AI coding agents](https://tools.lalipublications.com/use-cases/best-ai-coding-agents/)

**2. Repo maintenance in plain Markdown: GitHub Agentic Workflows (GA, Oct 28)**
Write recurring jobs such as issue triage, CI failure analysis, docs updates, and test generation as Markdown files. GitHub compiles them into standard Actions run by Copilot or your own agent, read-only and sandboxed by default ([GitHub changelog](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/) · [docs](https://github.github.com/gh-aw/)).
**Pricing (checked Oct 28, 2026):** Open source; uses your Actions minutes and Copilot or agent credentials.
**When NOT to use it:** Cross-SaaS business automations outside GitHub. Use [n8n](https://n8n.io) (free self-hosted; Cloud from €20/mo billed yearly) or [Make](https://www.make.com) (free: 1,000 credits/mo). Never grant unconstrained write access without a human PR review gate.
More options: [Best AI for workflow automation](https://tools.lalipublications.com/use-cases/best-ai-for-automation-workflows/) · [Best AI for fixing broken code](https://tools.lalipublications.com/use-cases/best-ai-for-fixing-broken-code/)

**3. Prototyping UI from your real design system: Replica by GitHub Design (open source, Oct 28)**
Describe a screen in the GitHub Copilot app and Replica builds an interactive prototype from your design system's actual components, with an optional self-hosted Replica Hub for team comments ([GitHub changelog](https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/) · [repo](https://github.com/github/replica)).
**Pricing (checked Oct 28, 2026):** Free, MIT license; needs Copilot and your component library.
**When NOT to use it:** Brand-new projects with no design system. Use [v0](https://v0.app) (free: 7 messages/day; Plus $30/user/mo) or [Lovable](https://lovable.dev) (free: 5 credits/day, up to 30/mo).
More options: [Best AI for UI design](https://tools.lalipublications.com/use-cases/best-ai-for-ui-design/) · [Best AI for vibe coding](https://tools.lalipublications.com/use-cases/best-ai-for-vibe-coding/)

**4. Letting non-engineers open tested PRs: Replit Cloud Agents for company codebases (Oct 27)**
Replit Cloud Agents now connect to your existing GitHub or GitLab repos. A PM or designer describes a change; the agent runs the app, tests its change, and opens a PR with screenshots and video for engineers to review ([Replit blog](https://replit.com/blog/anyone-can-bring-ideas-to-company-codebase)).
**Pricing (checked Oct 28, 2026 on [replit.com/pricing](https://replit.com/pricing)):** No free plan listed; Core $20/mo ($18/mo yearly). Company-codebase Cloud Agents require **Pro ($100/mo) or Enterprise**.
**When NOT to use it:** Solo builders who just want async PRs. Try [Jules](https://jules.google) (free beta, up to 15 tasks/day), [OpenAI Codex](https://openai.com/codex/) (limited free use; ChatGPT Plus $20/mo), or [GitHub Copilot](https://github.com/features/copilot) (Pro $10/mo).
More options: [Best AI coding agents](https://tools.lalipublications.com/use-cases/best-ai-coding-agents/)

**5. Cheaper everyday agentic coding + custom event-driven agents: GPT-6.1 Terra in Copilot (Oct 26) & Cursor Agent SDK (Oct 20)**
- **GPT-6.1 Terra in Copilot:** GA on Pro, Pro+, Max, Business, and Enterprise, tuned for everyday agentic coding at lower cost than GPT-6.1 Sol ([GitHub changelog](https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot/)). **When NOT to use it:** Gnarly cross-system root-cause debugging, where a heavier reasoning model saves hours. **Deadline (checked Oct 29, 2026):** Copilot retires Claude Opus 4.8, Claude Opus 5, and GPT-5.6 Terra on **Nov 16, 2026**; GitHub suggests Claude Opus 5.5, or GPT-6.1 Sol or GPT-6 Luna. Opus 4.8 stays for individual annual-plan subscribers ([GitHub changelog](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/)).
- **Cursor Agent SDK:** Package an agent as a folder (prompt, typed tools, skills, MCP servers), test it with evals, and deploy it to Cursor or your own infra, triggered by GitHub, Slack, webhook, or cron events ([Cursor changelog](https://cursor.com/changelog/agent-sdk)). **Pricing (checked Oct 28, 2026 on [cursor.com/pricing](https://cursor.com/pricing)):** Free plan; Plus $8/mo (Cursor models only); Premium $30/mo. **When NOT to use it:** You need a vendor-neutral orchestration framework. Use [LangGraph](https://github.com/langchain-ai/langgraph) or [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) (both free, MIT).
More options: [Best AI agent frameworks & MCP](https://tools.lalipublications.com/use-cases/best-ai-for-agent-frameworks/)

## Privacy heads-up: Gemini API now stores requests by default

Since Oct 26, new **paid-tier** Gemini API projects using the Generate Content API (generateContent, streamGenerateContent, batchGenerateContent) store requests by default (store=true), matching the Interactions API. Existing projects keep their current setting ([Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) · [Logs and datasets docs](https://ai.google.dev/gemini-api/docs/logs-datasets); checked Oct 29, 2026).
**What to do:** If you created a paid project on or after Oct 26 and send it customer data or private code, set **store=false** on each request, or turn off Generate Content API logging in the Settings panel of the Logs and Datasets dashboard.

## Also shipped (checked Oct 29, 2026)

- **Copilot Fusion local models (experimental preview, Oct 28):** Fusion can now route between on-device and cloud models in Copilot CLI, the Copilot app, and VS Code. One-click setup is Windows-only; on macOS and Linux you bring your own model through a local OpenAI-compatible server ([GitHub changelog](https://github.blog/changelog/2026-10-28-github-copilot-fusion-now-supports-selection-of-local-models/)). **Caveat:** It's opt-in and experimental, and your machine has to be able to run the model. Skip it for reproducible runs.
- **Copilot Automations: new triggers, tools, and cost controls (Oct 28):** Trigger automations through the REST API or 24 new GitHub events, chain them together, use 20 new tools or your own MCP servers, and cap AI credits per run, day, week, or month ([GitHub changelog](https://github.blog/changelog/2026-10-28-new-tools-triggers-and-cost-controls-for-copilot-automations/)). **Caveat:** Set the credit cap before you connect outside triggers like Sentry or PagerDuty. A noisy webhook can burn credits fast.
- **Codex CLI 0.165.0 (Oct 27):** Built-in Google Cloud Vertex AI provider, GPT-6.1 Terra in the model catalog, and memory v2 on by default for fresh profiles ([Codex changelog](https://developers.openai.com/codex/changelog)). **Caveat:** Fresh profiles now keep memory automatically. Check what it stores before you point it at repos with secrets, and pin the version in CI.
- **Gemini API CLI (gemini-api) beta (Oct 27):** A stateless, zero-dependency command-line client for coding agents, scripts, and CI pipelines, built on the Interactions API ([Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) · [CLI guide](https://ai.google.dev/gemini-api/docs/cli)). **Caveat:** It's beta, and the Interactions API stores requests by default, so check your logging settings before you pipe private code through it.
- **Lovable Events & Hooks + Gemini rerouting:** Business and Enterprise workspaces can now send project events to your HTTPS endpoint, and hooks can allow or block actions first (Oct 27). Separately, apps that called Gemini 2.5 were moved to Gemini 3.8 Flash or 3.1 Flash Lite after Oct 20 ([Lovable changelog](https://docs.lovable.dev/changelog)). **Caveat:** Hooks aren't on lower plans. Rerouted apps keep working, but cost per request and responses may change, so ask Lovable to switch you to a current model.

## Agent Reliability Tip of the Week: Stop Stage-Handoff Distrust & Verifier Rubber-Stamping

Multi-stage coding workflows (Agentic Workflows, Copilot Automations chains, or Cursor SDK agents that split work into `localising -> solving -> testing`) hit two failure modes fast:

1. **Stage-handoff distrust:** Pass the localization stage's findings inside a trailing tool result and the solving stage treats them as untrusted observation data, then re-runs full-repo search. **The deterministic fix:** Start the next stage with a fresh message array, inject a typed `<verified_stage_state>` JSON block (`target_files` with line ranges, `root_cause_hypothesis`, `completed_stages`, `current_stage`) into the system/developer header, and gate the toolset so the solving stage can't restart broad discovery.
2. **Verifier rubber-stamping:** A checker that shares the worker's conversation history gets anchored by its reasoning and approves bad patches. **The deterministic fix:** Give the verifier *only* the task spec, your rubric, and the raw diff/test outputs, never the worker's reasoning.

Read all five failure modes in **[Agent Backbone Issue #1: 5 Ways Production AI Agents Quietly Break (And the Deterministic Fixes)](https://tools.lalipublications.com/agent-backbone/issue-1/)**, or download the **[Free Printable Evaluation Rubric & 8-Question Regression Template (PDF)](https://tools.lalipublications.com/agent-backbone/agent-backbone-evaluation-rubric.pdf)**.
Coming in Agent Backbone #2: why MCP tool calls get sent twice when a connection drops mid-call, and how to retry only the calls that are safe to repeat.

## Tell us what to cover

Using a tool that deserves a spot, or hit an agent failure mode we should dissect next? Hit reply and tell us. And if a teammate is comparing coding agents right now, forward this issue to them.

All 30 use-case guides: [tools.lalipublications.com](https://tools.lalipublications.com/use-cases/)
