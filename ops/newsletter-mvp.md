# Newsletter MVP — Tool Use Cases Weekly

Owner: Larry Surroach (Lali Publications) · larrys@lalipublications.com · Spend: $0

## Name & cadence
- Name: **Tool Use Cases Weekly**
- Cadence: weekly, Monday morning (PT)
- Promise: "Weekly AI tool picks for vibe coders — new tools + which job they fit. Free."

## How signups work today (FormSubmit, free, no account)
- Forms on the homepage (#newsletter), /newsletter/, and every page footer POST to
  `https://formsubmit.co/larrys@lalipublications.com`.
- Hidden fields: `_subject=Tool Use Cases newsletter signup`, `_captcha=false`, `_template=table`,
  `_next=https://tools.lalipublications.com/thanks/`.
- **First submission triggers a one-time FormSubmit activation email to larrys@lalipublications.com.
  Larry must click "Activate Form" once**; until then signups are not forwarded.
- After activation, each signup arrives as an email (table format) with subject
  "Tool Use Cases newsletter signup". Suggested: a Gmail filter on that subject -> label `newsletter-signups`.
- Keep a running list (sheet/CSV) of addresses from those emails; it imports into Beehiiv/Buttondown later.
- Limits: no double opt-in, no unsubscribe handling — fine for MVP; send issues manually via BCC
  only while the list is tiny, then move to a real ESP (below).

## Issue template
```
Subject: Tool Use Cases Weekly #N — <hook>

Hi — here's this week's AI tool picks, sorted by the job they fit.

1) New & notable (3–5)
   - <Tool> — <what it is>. Fits: <use case link>. Verdict: <one line>.
2) Pick of the week
   - <Tool> for <job>: why, who it's for, one caveat.
3) Workflow tip
   - <Tool A> + <Tool B> to <outcome>, in 3 steps.
4) Directory updates
   - New/changed pages on tools.lalipublications.com
[Sponsored slot — clearly labeled, only if sold]

— Tool Use Cases (Lali Publications)
Reply to unsubscribe or suggest a tool.
```

## First 3 issue angles
1. **"Your vibe-coding stack in 2026"** — Cursor vs Lovable vs v0 vs Replit: which one for which kind of project.
2. **"Hand off the ticket: coding agents compared"** — Claude Code, Codex, Copilot agent, Devin, Aider: when to delegate vs pair.
3. **"Ship a YouTube video with AI in an afternoon"** — Descript + ElevenLabs + Veo/Runway + OpusClip workflow.

## Next step (needs Larry's OK; still $0)
- Create a free Buttondown (free tier, small list) or Beehiiv (free Launch plan) account under Lali Publications.
- Import the collected signup list; switch the form `action` in build.py (`nl_form`) to the ESP's embed/endpoint,
  rebuild, deploy. Gains: double opt-in, unsubscribe links, archive pages (more SEO).
- No paid plan, no Stripe, until Larry approves.
