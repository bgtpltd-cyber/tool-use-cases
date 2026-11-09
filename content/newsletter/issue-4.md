Hi there,

If an agent opens PRs, calls the Gemini API, or runs overnight in CI, last week's releases changed what it does when nobody is watching. GitHub starts blocking a common PR trigger, Gemini 2.5 models reroute in December with breaking API changes, and Claude Code, OpenCode, and Codex all changed how refusals, background jobs, and approvals behave.

Theme this week: **your unattended agents changed this week. Check them before December.** Below: which change fits which job, what to test, and when **not** to rely on it. Picks verified Nov 9, 2026 on each official page. Picks are editorial and unpaid.

## This week's picks: Check your unattended agents before December

**1. Public-repo AI PR bots that still use `pull_request_target`: GitHub Actions default block (changelog Nov 2; enforced Dec 2)**
Starting **December 2, 2026**, GitHub Actions blocks `pull_request_target` by default in **public** repositories unless an Actions event policy explicitly allows it. Private and internal repos are unaffected. Many AI PR-review and auto-fix bots still trigger on `pull_request_target` so they can read base-repo secrets while reviewing a fork PR—exactly the pattern this rule targets ([GitHub changelog](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/)).
**Brownouts (checked Nov 9, 2026):** Nov 9 and Nov 16, **16:00–18:00 UTC** (**8–10 AM PT**). Today's brownout already happened; the next one is Nov 16, 8–10 AM PT.
**Pricing:** Applies on GitHub Free, Team, and Enterprise Cloud public repos; not GitHub Enterprise Server. No separate fee.
**Test:** Open a pull request **from a fork** into a public repo that still runs `pull_request_target` workflows **before Nov 16**, and confirm whether Insights shows them blocked or you need an explicit allow policy.
**When NOT to use it:** Don't keep `pull_request_target` just to get secrets into fork PRs. Prefer `pull_request` plus a safer trust model, or an explicit event policy that names only the workflows you still need.

**2. Agents and apps still pinned to Gemini 2.5 Pro / Flash: Dec 1 auto-reroute + breaking API changes**
Per the [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) (Nov 2, 2026 entry, re-checked Nov 9, 2026):

- **`gemini-2.5-pro`:** deprecated and no longer available to select in Google AI Studio. Effective **December 1, 2026**, all API requests to `gemini-2.5-pro` will automatically route to `gemini-3.8-flash` and be billed at Gemini 3.8 Flash rates. Breaking API changes include function calling and `thought_signature` validation, `thinking_level` replacing `thinking_budget`, and removed sampling parameters and prefilled model turns.
- **`gemini-2.5-flash`:** deprecated and no longer available to select in Google AI Studio. Effective **December 1, 2026**, all API requests to `gemini-2.5-flash` will automatically route to `gemini-3.5-flash-lite` and be billed at Gemini 3.5 Flash-Lite rates. Breaking API changes include function calling and `thought_signature` validation, `thinking_level` replacing `thinking_budget`, and removed sampling parameters and prefilled model turns.

**Test:** Point a staging client at `gemini-3.8-flash` / `gemini-3.5-flash-lite` **before Dec 1** and fail the suite on any call that still sends `thinking_budget`, sampling params, or prefilled model turns.
**When NOT to use it:** Don't wait for the silent Dec 1 route if your tool-calling or thinking config depends on 2.5 behavior—migrate the model string and the request shape now.

**3. Headless Claude Code jobs that must fail closed: Claude Code v2.1.319**
`claude -p` in auto mode now **exits 1** when its actions are refused because no safety check is available (it used to exit 0). New `permissions.denyInsteadOfPrompting` denies a tool call that would wait on a permission prompt and continues the turn. Long MCP task calls move to the background immediately (opt out with `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND`). Auto mode with telemetry/feature flags off (including behind LLM gateways) no longer falls back to the built-in classifier for calls the server can't check—set `CLAUDE_CODE_AUTO_MODE_SERVER=0` to keep the old local classifier path; Bedrock, Vertex, and Foundry are unchanged ([v2.1.319 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.319)).
**Pricing:** Uses your Claude / Console plan; no separate CLI fee on the release notes.
**Test:** In CI, run a `claude -p` auto-mode job that should be refused and assert **exit code 1**, then flip `permissions.denyInsteadOfPrompting` and confirm the turn continues without hanging on a prompt.
**When NOT to use it:** Interactive local sessions where you *want* a permission prompt, or gateways that still need the classifier—set `CLAUDE_CODE_AUTO_MODE_SERVER=0` only if you understand you are opting back into the local path.

**4. OpenCode scripted / CI runs that start background jobs: OpenCode v2.2.6**
`opencode run` now waits for the background shell commands, subagents, and image jobs its prompt started, then lets the model respond before exit. **There is no time limit**—a never-exiting job (dev server, file watcher) keeps the run open until Ctrl+C or SIGTERM, so **add a CI timeout**. SIGTERM cancels the session and background jobs and exits **143**. Also new: `opencode run -w` / `--worktree`, `--archived` (keeps CI sessions out of inbox/lists), and opt-in MCP `pool: true` to share one MCP connection across projects with the same setup ([v2.2.6 release](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)).
**Pricing:** Open-source CLI; model/provider costs are yours.
**Test:** Run a scripted prompt that starts a long-lived background job under a **job-level timeout**, send SIGTERM, and confirm exit **143** and that the watcher is gone.
**When NOT to use it:** Unbounded CI without a timeout wrapper, or `--worktree` combined with `--continue` / `--session` (not allowed).

**5. Codex agents that need clearer network / MCP approvals: Codex CLI 0.167.0**
MCP approval metadata now includes **tool names** (and annotation hints). Concurrent network approval prompts to the **same endpoint** come **one at a time**, and prompts close when their requests end. Admins can require **fresh human approval** for chosen commands (`prompt-user` command rules; see app-server README / managed network docs). Also: agent **command center** (`codex agents --no-daemon`) and **inline patch review** while an approval prompt is open ([GitHub release](https://github.com/openai/codex/releases/tag/rust-v0.167.0) · [Codex changelog](https://developers.openai.com/codex/changelog)).
**Pricing (checked Nov 9, 2026):** Codex CLI is included across ChatGPT plans (including Free/Go) with plan limits; Codex Cloud needs Plus or higher. ChatGPT Plus is **$20/mo** ([OpenAI Help](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) · [Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus)).
**Test:** Trigger two concurrent network approvals to one endpoint and confirm they serialize; open an approval prompt and expand the patch inline before you accept.
**When NOT to use it:** Fully non-interactive CI that cannot answer approval prompts—pre-approve only the commands you trust, or run without network.

## Builder pick: Cursor Build Live Apps (Nov 5)

Tell a Cursor **cloud agent** you want to build an app and it can scaffold the web app, provision Postgres if needed, set auth behind Cursor SSO, and deploy a shareable link after you pick a domain. Publish stays explicit: security checks must pass first; admins can see apps/secrets and unpublish. Origin + GitHub today; GitLab later ([Cursor changelog](https://cursor.com/changelog/build-live-apps)).
**Pricing (checked Nov 9, 2026):** Changelog: available on **paid plans with cloud agents enabled**. On [cursor.com/pricing](https://cursor.com/pricing), cloud agents are listed from **Premium $30/mo** upward (not Free; not Plus $8/mo).
**Test:** On a Premium-or-higher seat with cloud agents on, ask for a tiny internal app, refuse publish until the security check fails, then fix and publish.
**When NOT to use it:** Customer-facing production outside Cursor's hosting/SSO, GitLab-only repos today, or Free/Plus seats without cloud agents.

## Also shipped (checked Nov 9, 2026)

- **Gemini Omni 1.2 Flash GA (Nov 5):** Up to 15-second video, conversational edit, 30% lower video output pricing (**$12.00 per 1M tokens** on the API changelog), doubled paid rate limits ([Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) · [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)). **Caveat:** From **Dec 3, 2026**, `gemini-omni-1.1-flash` auto-routes to `gemini-omni-1.2-flash` at 1.2 rates.
- **Dependabot + Agent Package Manager (Nov 3):** Version-update PRs for git deps in `apm.yml`, regenerates `apm.lock.yaml` when present; **version updates only, not security updates**; GA on github.com for all plans ([GitHub changelog](https://github.blog/changelog/2026-11-03-dependabot-version-updates-support-agent-package-manager/)).
- **LangGraph 1.2.20 strict resume mode (Nov 5):** Opt-in and experimental. Turned on through the private configurable key `__pregel_strict_resume` (`CONFIG_KEY_STRICT_RESUME`). With it set, a resume that names a non-pending interrupt id, sends an empty map, or sends one value while several interrupts are pending raises before writing; without the key, today's silent ignore behavior stays ([release](https://github.com/langchain-ai/langgraph/releases/tag/1.2.20) · [PR #9574](https://github.com/langchain-ai/langgraph/pull/9574)).

## From newsletters we read

**The Vibe Diff**: a free Monday email on what actually changed in AI coding tools like Cursor, Claude Code, Codex, Lovable and Replit, so vibe coders know what to try that week. [the-vibe-diff.vercel.app](https://the-vibe-diff.vercel.app)

(Unpaid one-for-one mention; no affiliate or tracking links. They linked Tool Picks Weekly in their Issue #003.)

## Agent Reliability Tip of the Week: Review agent-skill bumps like dependency PRs

Dependabot's APM support makes agent skills look like ordinary version bumps. They are not. A skill or prompt package is **executable instructions** for your coding agents. Prefer:

1. Require human review on `apm` Dependabot PRs (no auto-merge).
2. Diff the upstream git tags, not just the lockfile hash.
3. Run your Agent Backbone regression set (or a short smoke: "can this skill write outside the worktree?") before merge.

That pairs with **[Agent Backbone #2: 7 Ways MCP and Retry Plumbing Quietly Break Production Agents](https://tools.lalipublications.com/agent-backbone/issue-2/)**—especially duplicate tool calls and unsafe retries—and the **[free evaluation rubric PDF](https://tools.lalipublications.com/agent-backbone/agent-backbone-evaluation-rubric.pdf)**.

## Tell us what to cover

Running an unattended agent that still uses `pull_request_target`, Gemini 2.5, or unbounded `opencode run`? Hit reply and tell us. Forward this to whoever owns your Dec 1 / Dec 2 cutovers.

All 30 use-case guides: [tools.lalipublications.com](https://tools.lalipublications.com/use-cases/)
