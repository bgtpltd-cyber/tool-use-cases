# Daily builder log (English /new/ only)

Test run: weekdays, Nov 2–13, 2026. Only verified **breaking changes**, **deadlines** and **price changes**.
`daily_log.py` reads one JSON file per day from this folder and, after `build.py` writes the site, adds:

- the "Daily builder log" section at the top of `site/new/index.html` (note, Deadlines strip, days newest first, each with an `id="YYYY-MM-DD"` anchor and a Permalink)
- a `<link rel="alternate">` to the daily feed in that page's `<head>`
- `site/new/daily.xml`, an RSS 2.0 feed with one item per day linking to `https://tools.lalipublications.com/new/#YYYY-MM-DD`

Other locales' `/new/` pages are not changed. `daily.xml` is not added to the sitemap, the same as `feed.xml`, because the sitemap only lists HTML pages.

## Rules

- Every item comes from an **official source** (the vendor's changelog, docs, pricing page, blog or repo) that you opened that day. If a candidate doesn't check out, drop it. Never invent anything.
- Byline is Lali Publications only. No sponsored or affiliate items. The build fails if the user's surname appears in a file.
- 3–7 items per day, or a "no changes" day.

## Schema: `content/daily-log/YYYY-MM-DD.json`

```json
{
  "date": "2026-11-02",            // required, must equal the file name
  "preview": false,                // optional; true shows a "Format preview" badge
  "items": [                       // 3-7 items, unless no_changes is true
    {
      "type": "Deadline",          // required: "Breaking change" | "Deadline" | "Price change"
      "tool": "Jules",             // required: tool name as the vendor writes it
      "what": "One line: what changed.",  // required, one line, max 260 characters
      "source_name": "Jules changelog: Jules Turndown (Oct 29, 2026)",  // required: link text
      "source_url": "https://jules.google/docs/changelog/",             // required: official https URL
      "checked": "08:06 AM",       // required: Pacific Time when you checked the source, "HH:MM AM|PM"
      "test": "What a builder should test or do.",  // required; shown after "Test for this:"
      "use_case": "best-ai-coding-agents",          // optional: an existing use-case slug (build fails if unknown)
      "deadlines": [               // required for "Deadline", optional otherwise
        {"date": "2026-11-11", "label": "last day to continue sessions"}
      ]
    }
  ]
}
```

A day with nothing verified:

```json
{"date": "2026-11-03", "no_changes": true, "checked": "09:40 AM", "items": []}
```

This shows "No verified changes today." with the checked time.

Comments (`//`) above are for explanation only. Real files must be plain JSON.
Use-case slugs are the first field of each `UC` entry in `build.py` (for example `best-ai-for-vibe-coding`, `best-ai-coding-agents`).

**Deadlines strip.** Every `deadlines` entry from every day is gathered, soonest first. Entries dated before **today in Pacific Time** (at build time) are dropped automatically, so a rebuild cleans up passed deadlines. To preview the strip for another date, run `DAILY_LOG_TODAY=2026-11-05 python3 build.py` (don't commit that output).

## Steps for each weekday

1. **Add a file.** Copy the newest file in this folder to `content/daily-log/YYYY-MM-DD.json` (today's date in PT). Replace the items with 3–7 changes you verified today, or use the no-changes form. Open each `source_url` and record the time you checked it (PT).
2. **Build.** From the repo root, run `python3 build.py`. A validation error names the file and item; fix it and rebuild.
3. **Verify.**
   - `python3 /workspace/check_site.py site` should show `broken 0`.
   - `python3 -c "import xml.etree.ElementTree as E; E.parse('site/new/daily.xml'); E.parse('site/feed.xml'); print('feeds ok')"`
   - Open `site/new/index.html`. Check that the new day is at the top, its Permalink jumps to `#YYYY-MM-DD`, and passed deadlines are gone from the strip.
   - `grep -ri surroach site/` should print nothing.
4. **Commit.** `git add content/daily-log site && git commit -m "Daily log: YYYY-MM-DD"`.
