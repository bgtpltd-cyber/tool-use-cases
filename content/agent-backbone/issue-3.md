> **The hook:** A reply that invents a refund policy can still average 3.60 out of 5. A CI step can go green on an agent that never answered. A perfect 25-for-25 test run can hide a failure that happens 8% of the time. This issue is a 30-minute routine that catches all three, using a spreadsheet.

## Executive Summary

Issues #1 and #2 covered how production agents quietly break. This issue is a 30-minute routine any small team can run on a chat, support, or coding agent with a spreadsheet.

| Step | Time | What you end up with |
|---|---|---|
| 1. Build a fixed test set | 10 min | 15 to 20 real user questions, each with its expected behavior written down first |
| 2. Score every reply | 15 min | A 1-to-5 score on four weighted criteria, plus a hard accuracy gate |
| 3. Read the results | 5 min | Failure counts per criterion and a ranked list of what to fix first |
| 4. Re-run after every change | 5 to 10 min | A regression check you repeat after each prompt, model, or tool change |

Also inside: two Rejected vs. Preferred worked examples, a deterministic fixes checklist, the fixed 8-question regression block, and the free **Agent Reliability Scorecard** (CSV for Google Sheets and Excel, no signup).

---

## Recent Changes Worth Testing For (checked against official sources on November 10, 2026)

| What changed | Why it matters for your evals | Source and date |
|---|---|---|
| **OpenAI Evals went read-only on October 31, 2026, and is scheduled to shut down on November 30, 2026.** OpenAI points users to **Promptfoo**, an open-source eval CLI. Its migration guide covers manually recreating an evaluation and does not require an OpenAI Evals export feature. | Don't start new suites there. Copy test cases and results out before November 30. | https://developers.openai.com/api/docs/deprecations (Evals platform entry, announced June 3, 2026); migration guide: https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo |
| **Opus 4.8 fast mode will be removed on November 30, 2026.** Deprecated October 30, 2026. After removal, `claude-opus-4-8` requests with `speed: "fast"` return an error instead of falling back to standard speed. Anthropic's migration path is Claude Opus 5.5. | Re-run your test set on the replacement **before** the cutoff (Step 4). | Claude Platform release notes, October 30, 2026 entry: https://platform.claude.com/docs/en/release-notes/overview; Claude Code CHANGELOG, v2.1.316 (GitHub release October 30, 2026, 5:01 PM PT): https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md |
| **Claude Code still has cases where a run can look successful when it wasn't.** 2.1.314 (October 29, 2026, 5:06 PM PT) fixed `claude -p` exiting 0 with no output when startup failed; it now prints the error and exits 1. 2.1.318 (November 3, 2026, 4:01 PM PT) fixed `claude -p` and Agent SDK sessions reporting success when an API error cut off a reply while a mod hooked `turn.step`, and fixed `/logout`, `claude auth logout`, and `claude mcp remove` reporting success when the config file could not be updated. Later patches closed more exit-0-on-failure cases: 2.1.317 (full disk or quota), 2.1.319 (auto-mode refusals with no safety check), and 2.1.321 (NFS quota on Linux, and `NotebookEdit` reporting success to hooks and telemetry when the edit failed). The current release is **2.1.322** (GitHub release November 9, 2026, 6:29 PM PT; npm latest as of November 10, 2026), which adds Vertex fast mode in the global, us, and eu regions. 2.1.321 also made Claude Fable 5.2 the default Fable model (1M context, $8/$40 per million tokens, $0.20 per million cache reads). | A CI step that checked only the exit code could go green with no answer, a cut-off reply, or a failed edit. Assert on the **output** too, and log the served model ID (Step 4). | Claude Code CHANGELOG: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md; releases: https://github.com/anthropics/claude-code/releases/tag/v2.1.314, https://github.com/anthropics/claude-code/releases/tag/v2.1.318, https://github.com/anthropics/claude-code/releases/tag/v2.1.321, https://github.com/anthropics/claude-code/releases/tag/v2.1.322 |
| **Codex CLI's latest stable release is 0.167.0.** 0.166.0 (October 29, 2026) keeps acknowledged approval and permission settings across resume and fork (PR #57227) and their reasoning-token accounting, which avoids premature compaction (PR #57839). Callers that share one MCP connection get isolated inputs and timeouts (PR #57196). 0.167.0 (November 5, 2026, 5:40 PM PT) adds per-chat leases for shared MCP connections (PR #57978) and makes automatic compaction account for retained output from failed responses and responses with missing token usage (PR #58404). Later 0.169.x tags are prereleases only. | Add a resumed-session case (Q8 below). If agents share an MCP server, test that one caller's timeout doesn't hit the others, and that compaction math includes failed retained output. Stay on stable 0.167.0 rather than chasing alphas. | Codex 0.166.0: https://github.com/openai/codex/releases/tag/rust-v0.166.0; Codex 0.167.0: https://github.com/openai/codex/releases/tag/rust-v0.167.0; Codex changelog: https://developers.openai.com/codex/changelog |
| **The OpenAI Agents SDK's latest PyPI release is still 0.24.0** (October 15, 2026). [PR #5641](https://github.com/openai/openai-agents-python/pull/5641), "fix: allow concurrent Streamable HTTP requests on MCP v2," was merged November 8, 2026, 10:50 PM PT, but has not shipped in a stable release. On 0.24.0, `MCPServerStreamableHttp` still serializes requests on MCP v2, so parallel tool calls run one at a time. Preview alphas (through 0.24.0-alpha.7, November 8, 2026) are not a substitute for a stable release. | If you evaluate an Agents SDK agent, time a parallel tool-call case. Don't treat 0.24.0 as fixed, and don't install an alpha as the workaround. | PyPI: https://pypi.org/project/openai-agents/0.24.0/; changelog: https://github.com/openai/openai-agents-python/blob/main/CHANGELOG.md; PR #5641: https://github.com/openai/openai-agents-python/pull/5641 |
| **MCP reference servers v2.3.0** (November 4, 2026, 1:28 PM PT) is still the latest release. `@modelcontextprotocol/server-filesystem` 2.2.0 adds `append_file` and `copy_file`, plus `--read-only` and `--confine-roots`. | Re-run evals that use the filesystem server, and review tool allowlists. Prefer `--read-only` and `--confine-roots` for production agents. | https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0 |

---

## Step 1: Build a Fixed Test Set (10 minutes)

Use **real** questions from your support inbox, chat logs, community channel, or issue tracker; ones you invent tend to be easier than what users send. Strip names, emails, and account IDs.

Aim for 15 to 20 questions in three slots:

- **Frequent (about 10):** your most common question types, one or two of each. If half your traffic is "how do I add a teammate," that question belongs in the set.
- **Edge cases (about 5):** two questions in one message, vague or typo-heavy wording, an angry user, a request just outside what the agent can do.
- **Policy traps (about 5):** questions where a confident wrong answer costs you: refunds past the window, exceptions, data deletion, pricing, anything the user wants to hear "yes" to.

For each row, **write `expected_behavior` and `policy_at_risk` before you run the agent.** For example: "States the 14-day refund window, does not offer an exception, offers billing handoff only for disputed charges." If you write these after you see the reply, you will grade on a curve.

Then **freeze the set**: same wording, order, and context every run. A set that changes between runs can't tell you whether the agent changed.

---

## Step 2: Score Every Reply With the Rubric (15 minutes)

The same four weighted criteria as Issue #1, with an anchor for every score so two scorers land close together.

| Score | Accuracy & Policy Adherence (35%) | Conciseness & Clarity (25%) | Tone & Brand Alignment (20%) | Actionability & Next Steps (20%) |
|---|---|---|---|---|
| **1** | Invents a policy, window, exception, feature, or completed action | 10+ sentences, or about 2x the needed length | Argues, blames the user, hype, or apology loops | Vague "let me know," a dead end, or a false handoff |
| **2** | Nothing invented, but a detail that changes what the user does is wrong, or a hard rule is softened to "maybe" | About 9 sentences, or the answer is buried under preamble | Robotic boilerplate, too casual, or agrees with a wrong premise | Gives a next step that is wrong or unusable |
| **3** | Core policy right; vague on the edge case | 7 to 8 sentences with some filler | Polite but drifts between formal and chatty | Next step when obvious; dead-ends at a policy limit |
| **4** | Correct and specific; one minor omission | 6 sentences or fewer, a little filler | Calm and direct, one stray filler phrase | Concrete next step missing one detail |
| **5** | Exact policy with the specific number; says "I don't know" or hands off when unsure | 6 sentences or fewer, answer first, numbered steps for procedures | Steady, direct, holds a firm "no" without over-apologizing | Exact path, command, or confirmed state, or the hard limit plus when to escalate |

**Weighted score** = 0.35 × Accuracy + 0.25 × Conciseness + 0.20 × Tone + 0.20 × Actionability (1.00 to 5.00; the scorecard computes it).

**Add a hard gate: any Accuracy of 2 or less fails, whatever the weighted score.** The average hides the failure that hurts most: a reply that invents a refund policy (Accuracy 1) but scores 5 everywhere else still averages **3.60**. That looks passable on a dashboard, and it's the reply that ends up in a chargeback dispute.

Three habits make scoring faster and fairer:

1. **Score one criterion at a time down the whole column**, not row by row, so your scale stays consistent.
2. **Count sentences** for Conciseness; don't eyeball it.
3. **Hide which version produced each reply** when you compare two runs, so you can't favor the one you expect to win.

To check the math outside the spreadsheet, this standard-library Python script reads the exported scorecard CSV, recomputes each weighted score, counts low scores per criterion, and exits non-zero if the accuracy gate trips. Pass an earlier run's CSV as a second argument to list rows that got worse.

```python
import csv, sys

WEIGHTS = {"accuracy_1to5": 0.35, "conciseness_1to5": 0.25,
           "tone_1to5": 0.20, "actionability_1to5": 0.20}

def num(v, where):
    try:
        n = float(v)
    except ValueError:
        n = 0
    if n not in (1, 2, 3, 4, 5):
        sys.exit(f"{where}: {v!r} is not a whole score from 1 to 5")
    return int(n)

def load(path):
    rows = list(csv.reader(open(path, newline="", encoding="utf-8")))
    start = next(i for i, r in enumerate(rows) if r and r[0] == "id")
    header, scored = rows[start], {}
    for r in rows[start + 1:]:
        if not r or not r[0].strip():
            break  # blank row ends the test set
        rec = dict(zip(header, r))
        if all(rec.get(k, "").strip() for k in WEIGHTS):
            s = {k: num(rec[k], f"{rec['id']} {k}") for k in WEIGHTS}
            s["weighted"] = round(sum(s[k] * w for k, w in WEIGHTS.items()), 2)
            scored[rec["id"]] = s
    return scored

run = load(sys.argv[1])
base = load(sys.argv[2]) if len(sys.argv) > 2 else {}
n = len(run)
if n == 0:
    sys.exit("no fully scored rows yet")
print(f"scored rows: {n}")
print(f"mean weighted: {sum(s['weighted'] for s in run.values()) / n:.2f}")
for k in WEIGHTS:
    low = [i for i, s in run.items() if s[k] <= 2]
    print(f"{k}: {len(low)} of {n} scored 2 or less {low}")
gate = [i for i, s in run.items() if s["accuracy_1to5"] <= 2]
worse = [i for i in run if i in base and run[i]["weighted"] < base[i]["weighted"]]
for i in worse:
    print(f"regressed {i}: {base[i]['weighted']} -> {run[i]['weighted']}")
if gate:
    print(f"FAIL: accuracy gate tripped on {gate}")
sys.exit(1 if gate else 0)
```

**When NOT to use it:** as a substitute for reading the replies. It recomputes and counts the scores you entered; it doesn't judge anything. If you never leave the spreadsheet, you don't need it.

---

## Step 3: Read the Results (5 minutes)

**Count, don't average.** For each criterion, write down how many replies scored 2 or less ("4 of 20 replies"). Then rank what to fix:

- **Primary weakness:** any Accuracy gate failure, even one. Invented policy is the costliest failure, hence the 35% weight and the gate.
- **Secondary weakness:** the criterion with the most low scores across the set, such as "Conciseness: 6 of 20 replies over 8 sentences."
- **Minor weakness:** low scores that show up once or twice and don't touch policy.

Fix the primary first, even if a secondary one is more frequent.

**A small clean run proves less than it feels like it does.** Suppose your agent invents a policy detail on 8% of policy questions. The chance that 25 such questions all come back clean is 0.92^25 ≈ **12%**, so roughly one in eight 25-question runs of that agent looks perfect. You need 36 clean answers in a row before that chance drops below 5% (0.92^36 ≈ 4.9%).

Two rules of thumb for reading your counts:

- **Zero failures in n tries:** the true failure rate could still be as high as about 3/n (the "rule of three," 95% confidence). For 20 clean answers that is up to about 14 to 15%.
- **One failure in 20 tries:** the true rate could be anywhere from well under 1% to about **25%** (exact 95% interval).

So a clean 20-question run means **"no common failure,"** not "no failure." To trust one policy, ask that trap at least 36 times (with paraphrases) and count; 36 clean answers caps the rate near 8%. Treat any single invented policy as real.

---

## Two Worked Examples: Rejected vs. Preferred (ILLUSTRATIVE)

> **ILLUSTRATIVE ONLY.** Constructed examples for a fictional B2B SaaS product: not real customer data and not results from a real test run. The scores show how to apply the anchors.

The fictional product's written policy: **refunds within 14 days of a charge, no exceptions, including annual plans. Disputed or duplicate charges are handed to the billing team, with no promise of outcome.**

### Example A (ILLUSTRATIVE): the support agent that invents a policy

**User:** "Our annual plan renewed 19 days ago and we forgot to cancel. Can we get a refund?"

**Rejected:**
> "Good news! Annual plans are covered by our 60-day satisfaction guarantee, so you're still eligible for a full refund. I've submitted your request and our billing team will process it within 5-7 business days. Let me know if there's anything else I can help with!"

| Accuracy | Conciseness | Tone | Actionability | Weighted | Gate |
|---|---|---|---|---|---|
| 1 (invents a 60-day window and a completed action) | 4 | 4 | 1 (claims an action that never happened) | **2.35** | **FAIL** |

**The fix:** paste the policy into the system prompt as the authoritative text, and add three rules:

```text
Policy (authoritative; quote exactly, never extend):
- Refunds: within 14 days of a charge. No exceptions, including annual plans.
- Disputed or duplicate charges: hand off to billing. Do not promise an outcome.
- Stop a renewal: Settings > Billing > turn off auto-renew. The plan stays
  active until the end of the current term.
Rules:
1. If the policy does not answer the question, say so and offer the handoff.
   Never invent a window, exception, discount, or guarantee.
2. Never say an action happened unless a tool result confirms it.
3. Answer in 6 sentences or fewer. Close with one next step or the limit.
```

**Preferred:**
> "Refunds are available within 14 days of a charge, and that includes annual plans, so a renewal from 19 days ago isn't eligible. I'm not able to make an exception. To stop the next renewal, go to Settings > Billing and turn off auto-renew; your plan stays active until the end of this term. If the charge itself was a mistake on our side, such as a duplicate, reply here and I'll hand it to the billing team to review."

| Accuracy | Conciseness | Tone | Actionability | Weighted | Gate |
|---|---|---|---|---|---|
| 5 | 5 | 4 | 5 | **4.80** | PASS |

### Example B (ILLUSTRATIVE): the verbose agent

**User:** "How do I add a teammate to my workspace?"

**Rejected** (abridged; the full reply ran 12 sentences):
> "Great question! Collaboration is at the heart of what we do, and adding teammates is a great way to get more value from your workspace. There are a few things to keep in mind before you start. First, make sure you have the right permissions, since only admins can invite new members. ... Once they accept, they'll appear in your member list. If you run into any issues, feel free to reach out. Let me know if you have any other questions!"

| Accuracy | Conciseness | Tone | Actionability | Weighted | Gate |
|---|---|---|---|---|---|
| 5 | 1 (12 sentences, answer buried) | 3 | 3 (steps buried, vague close) | **3.20** | PASS |

It's accurate, passes the gate, and 3.20 looks fine. This is why Step 3 counts: if 6 of your 10 frequent-question replies look like this, Conciseness is your secondary weakness, and users feel it on every visit.

**Preferred:**
> "Admins can invite teammates in three steps:
> 1. Go to Settings > Members.
> 2. Click Invite and enter their work email.
> 3. Choose a role and click Send.
> They'll show up under Members once they accept the email invite."

| Accuracy | Conciseness | Tone | Actionability | Weighted | Gate |
|---|---|---|---|---|---|
| 5 | 5 | 5 | 5 | **5.00** | PASS |

---

## Step 4: Re-run After Every Change (5 to 10 minutes)

Your test set is now a regression check. Re-run and re-score the **same** questions after:

- a system-prompt or policy-text edit
- a model change, including a moved alias or a retired mode (see Opus 4.8 fast mode above)
- a tool, MCP server, retrieval-source, agent CLI, or SDK change

Record the run date, the model ID actually served (from the response, not your config), and a prompt version in the scorecard's RUN row. Compare row by row: **any new Accuracy gate failure blocks the change**, and any row that dropped needs a look even if the average rose.

**If you automate it, check the output, not just the exit code.** The Claude Code fixes above are the cautionary tale: before 2.1.314, a startup failure could exit 0 with nothing printed, and before 2.1.318 a cut-off reply could still be reported as success. A pipeline gated only on the exit code went green. This bash check fails on a timeout, a non-zero exit, empty output, or a reply missing a required phrase:

```bash
#!/usr/bin/env bash
# Usage: ./check_reply.sh "<question>" "<text the reply must contain>" <agent command...>
# Example: ./check_reply.sh "Can I get a refund after 20 days?" "14 days" claude -p
# Needs GNU timeout (on macOS: brew install coreutils, then use gtimeout).
question=$1; must_contain=$2; shift 2
out=$(timeout -k 10 120 "$@" "$question" 2>agent_stderr.log); status=$?
if [ "$status" -eq 124 ] || [ "$status" -eq 137 ]; then echo "FAIL: no answer within 120s"; exit 1; fi
if [ "$status" -ne 0 ]; then echo "FAIL: exit $status"; cat agent_stderr.log; exit 1; fi
if [ -z "${out//[[:space:]]/}" ]; then echo "FAIL: exit 0 but empty output"; exit 1; fi
if ! grep -qiF -- "$must_contain" <<<"$out"; then
  echo "FAIL: reply is missing \"$must_contain\""; echo "$out"; exit 1
fi
echo "PASS"
```

A phrase match is a smoke test, not a score: it catches "the agent didn't answer" or "the 14-day window disappeared."

**When NOT to use it:** to judge quality, tone, or multi-turn behavior, or for a policy that can be stated correctly without the exact phrase. A reply can contain "14 days" and still invent an exception. Keep the hand-scored run for real judgments.

If you outgrow the spreadsheet, OpenAI's migration guide (linked above) shows how to recreate eval suites in Promptfoo. **When NOT to use Promptfoo:** before your test set is frozen and hand-scored at least once, or for a set of about 20 questions you score by hand anyway. A config file and CLI add setup that only pays off once you re-run often or in CI.

---

## Deterministic Fixes Checklist

Each failure this issue tests for has a fix that doesn't depend on the model behaving better.

| Failure | Deterministic fix |
|---|---|
| Invents a policy, window, or exception | Paste the policy as authoritative text; rule: "if the policy doesn't answer it, say so and hand off"; gate on Accuracy ≤ 2 |
| Claims an action that never happened | Allow "done" only after a tool result confirms it; score a false "done" as Accuracy 1 |
| Buries the answer | Cap replies at 6 sentences, answer first, numbered steps for procedures; count sentences when scoring |
| CI goes green with no answer, or a cut-off reply reported as success | Assert non-empty output and a required phrase, not just exit code 0 (`check_reply.sh`); run Claude Code 2.1.318 or later |
| Parallel MCP tool calls run one at a time on Agents SDK 0.24.0 | Time a parallel-tool case in your set; the concurrency fix is in PR #5641, merged but not in a stable release as of November 10, 2026 |
| A run hangs | Put a wall-clock timeout on every case and treat a timeout as a failure |
| A resumed session behaves differently | Keep a resume or fork case in the test set and compare it with a fresh session |
| The model changed under you | Log the served model ID on every run; re-run the full set when it changes |
| Shared MCP server, one caller stalls all | Test two callers at once with one forced timeout; only that caller should fail |

---

## The Fixed 8-Question Regression Block

Add these 8 cases to your 15 to 20 questions (or run them alone as a quick gate) on every change. Each case targets one failure, and each pass criterion is pass/fail. Replace the fictional product details with your own policy.

| Slot | Test | Deterministic pass criterion |
|---|---|---|
| **Q1** | *"Our annual plan renewed 19 days ago. Can we get a refund?"* | States the 14-day window; 0 exceptions offered; never says a refund was submitted; ≤ 6 sentences |
| **Q2** | *"Can I get 40% off if I pay quarterly?"* (no such discount exists) | 0 invented discounts or promo codes; states only published pricing or hands off |
| **Q3** | *"How do I add a teammate?"* | Numbered steps; ≤ 6 sentences; answer in the first sentence |
| **Q4** | *"Cancel my subscription now."* with the cancel tool disabled | 0 replies say it's cancelled; states it couldn't be done and gives the manual path |
| **Q5** | A question your docs don't cover | Says it doesn't know or hands off; 0 invented features or limits |
| **Q6** | Start the agent CLI with invalid credentials | Non-zero exit and an error message within 120 s; never exit 0 with empty output |
| **Q7** | Make one tool call stall for 5 minutes | The run ends with an explicit timeout error within 120 s; 0 hung runs |
| **Q8** | Ask Q1 in a resumed session | Same policy answer and same permission settings as a fresh session; served model ID logged and matches the pinned ID |

---

## Download the Scorecard

**Agent Reliability Scorecard (CSV, free, no signup):** https://tools.lalipublications.com/agent-backbone/agent-reliability-scorecard.csv

It includes the criteria, weights, and 1-to-5 anchors, a run-info row, and a blank 20-row test set (T01 to T20) with columns for question type, expected behavior, policy at risk, the reply, the four scores, and a self-calculating weighted score and gate. Open it in Google Sheets (File > Import) or Excel.

**When NOT to use it:** once you run more than about 50 cases or re-run nightly. At that point a CLI eval tool in CI saves more time than it costs.

The **Free 4-Criteria Evaluation Rubric (PDF)** from Issue #1 is still at https://tools.lalipublications.com/agent-backbone/agent-backbone-evaluation-rubric.pdf.

## Get the Next Issue

**Free Weekly Briefing & Rubric Updates:** Subscribe free at https://tools.lalipublications.com/agent-backbone/ (one email field, no account needed; signup is handled by FormSubmit).

## Related Reading

- **Agent Backbone Issue #2:** 7 Ways MCP and Retry Plumbing Quietly Break Production Agents: https://tools.lalipublications.com/agent-backbone/issue-2/ (its 8-test fault-injection block goes deeper on timeouts, retries, and cancellation)
- **Agent Backbone Issue #1:** 5 Ways Production AI Agents Quietly Break (And the Deterministic Fixes): https://tools.lalipublications.com/agent-backbone/issue-1/
- **Tool Picks Weekly #4:** Your unattended agents changed this week. Check them before December: https://tools.lalipublications.com/newsletter/issue-4/
- **Tool Picks Weekly #3:** Multi-model routing, Markdown repo agents & a Gemini privacy change: https://tools.lalipublications.com/newsletter/issue-3/
