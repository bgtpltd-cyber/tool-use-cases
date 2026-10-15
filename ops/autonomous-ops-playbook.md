# Tool Use Cases — Autonomous Ops Playbook (mirrors agentusecases.ai)
Owner: Joe (CEO bot) · Site: https://tools.lalipublications.com · Budget: $0 (no paid tools/sends without Larry OK)

## 1. What agentusecases.ai does (observed 2026-10-15)
- robots.txt: Allow /, Disallow /api/ /stats/ /review/, Sitemap line.
- /llms.txt: H1 + one-line summary, editorial policy (hand-reviewed, source-linked), URL patterns (/use-case/<id>, /category/<id>), topic list with counts + one-line descriptions.
- /sitemap.xml with daily lastmod on home, /new, /topics, per-agent pages (/agents/grok-bot etc.).
- RSS at /feed.xml ("new use cases"), advertised via <link rel="alternate"> on every page.
- JSON-LD WebSite + SearchAction; canonical URLs; OG tags; Google Search Console verification meta.
- /sponsor: one week site-wide sponsor bar + "Sponsored by" line in every "Daily 5" email that week; goes live on approval.
- From Alex Finn tweets (verified by parent): his bot (Milo) monitors replies to announcement posts and ships PRs from feedback; SEO (Google/Bing/Facebook/chatbots) is a major traffic source; newsletter + sponsorships started ~$500/wk, +$100 per sale; email capture from day one; Daily 5 newsletter.

## 2. Site files to add (GitHub Pages, all free)
- /robots.txt: `User-agent: *` / `Allow: /` / `Sitemap: https://tools.lalipublications.com/sitemap.xml`. Explicitly allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended.
- /sitemap.xml (replace sitemap.txt): every page, lastmod from build.py.
- /llms.txt + /llms-full.txt: summary, editorial policy, URL patterns (/tools/<id>, /use-cases/<id>), category list with counts, newsletter + sponsor links.
- /feed.xml RSS of new use cases; <link rel="alternate"> in every page head.
- Per page meta: unique <title> (≤60 chars), meta description (≤155), canonical, OG/Twitter card, og:image.
- JSON-LD: WebSite+SearchAction (home), ItemList (category/tool lists), Article or HowTo (use case pages), SoftwareApplication (tool pages), BreadcrumbList, FAQPage where a page has Q&A.
- Google Search Console + Bing Webmaster verification meta (free; Larry verifies).
- Email capture form on every page (see 3).

## 3. Newsletter MVP ("Daily 5" → start as "Tool Use Cases Weekly 5")
- Capture: free form endpoint. Options in order: Buttondown free tier (≤100 subs, no card; confirm at signup) → Google Form / Formspree free → mailto fallback. No paid platform without Larry OK.
- Drafting: Joe builds each issue as markdown + HTML in /workspace/tool-use-cases/newsletter/issues/YYYY-MM-DD.md, publishes a web archive page (/newsletter/<date>) for SEO, and emails Larry a draft for approval. Option: Larry approves claiming a Grok Bot inbox (e.g. news@mail.grokbot.com) for drafts/replies.
- Format: subject line, 1-line intro, 5 items (tool, what someone did, result, source link, site link), 1 "try this" prompt, sponsor slot ("Sponsored by …" or house ad for sponsorship), footer w/ unsubscribe.
- Cadence: weekly (Tue AM PT) until 250 subs, then 2–3x/week, then daily 5.
- First 3 issues:
  1. "5 tools people are actually using AI agents with this week" (best-sourced new entries).
  2. "Free-tier stack: 5 $0 tools that do real work" (high SEO/share value).
  3. "Reader-submitted: 5 use cases from X" (feedback loop; credits submitters → shares).

## 4. Monetization
- Rate card exists (ops/sponsor-rate-card.md). Mirror Alex: start low (~$100–$500/wk bundle site bar + newsletter), raise after each sale. Only activate when traffic/subs justify (e.g. >1k weekly visits or >300 subs). Outreach drafts go to Larry; no sends.

## 5. Routines to create (Joe creates after Larry OK; not created here)
| # | Name | Cadence | What it does |
|---|------|---------|--------------|
| 1 | newsletter-draft | Weekly Mon 4pm PT | Pick top 5 new entries, write issue, build archive page, email draft to Larry for approval |
| 2 | content-scan-add | Daily 7am PT | Search X/web for new real tool use cases, verify source, add to site via build.py, update sitemap/feed/llms.txt, commit |
| 3 | x-feedback-watch | Every 4h | Run X queries (sec. 6), log feedback/bugs/submissions to ops/feedback-log.md, draft replies/PRs; no posting without OK |
| 4 | bug-watch | Daily 6am PT | Run checklist (sec. 7), fix and commit small issues, report bigger ones |
| 5 | seo-geo-audit | Weekly Thu | Check meta/JSON-LD/canonical per page, validate sitemap/feed, test ChatGPT/Perplexity/Google for target queries, log citations, refresh llms.txt |
| 6 | distribution-drafts | 3x/week | Draft X posts/threads (new use cases, newsletter issue, milestones), reply targets, communities/directories to list in; Larry approves posts |
| 7 | sponsor-pipeline | Weekly Fri | Update traffic/sub stats, refresh targets, draft outreach for Larry |
| 8 | weekly-report | Weekly Sun | Traffic, subs, new entries, feedback, bugs, revenue → email Larry |

## 6. X watch queries
- `tools.lalipublications.com` · `"Tool Use Cases"` · `@<site handle>` mentions + replies to our announcement posts
- `"using claude code to" OR "used chatgpt to" OR "my agent" -is:retweet lang:en min_faves:20`
- `"I automated" (n8n OR zapier OR make.com) min_faves:10`
- `(cursor OR "grok" OR perplexity) "workflow" "saved me" min_faves:10`
- `from:AlexFinn` (watch competitor/peer strategy)
- Bug signals: `tools.lalipublications.com (broken OR 404 OR "doesn't work" OR bug)`

## 7. Bug watch checklist
- All sitemap URLs return 200; no broken internal/external links (lychee or curl loop).
- HTTPS/CNAME valid; GitHub Pages build succeeded.
- robots.txt, llms.txt, feed.xml, sitemap.xml parse.
- JSON-LD validates (schema.org parse); one canonical per page; no duplicate titles.
- Signup form submits; confirmation works.
- Mobile render + Lighthouse (perf/SEO/a11y ≥90).
- Search/filter in app.js works; no console errors (headless browser).
- Sponsor bar shows/hides correctly by date.
