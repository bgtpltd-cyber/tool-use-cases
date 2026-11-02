"""Daily builder log for English /new/ (test: weekdays Nov 2-13, 2026).

Reads one JSON file per day from content/daily-log/YYYY-MM-DD.json (schema and routine steps:
content/daily-log/README.md), validates it, then, after build.py has written the site:
  - inserts the 'Daily builder log' section (note, Deadlines strip, dated days, newest first) at the top of
    site/new/index.html, above the release list, and a <link rel="alternate"> to the daily feed in its <head>
  - writes site/new/daily.xml (RSS 2.0, one item per day, linking to the day's dated anchor)
  - appends the section's styles to site/style.css
Other locales' /new/ pages are not touched. Deadlines that have passed (before today in Pacific Time)
are dropped from the Deadlines strip at build time; set DAILY_LOG_TODAY=YYYY-MM-DD to preview another date.
"""
import os, re, json, glob, html
from datetime import datetime, date
from email.utils import format_datetime
from zoneinfo import ZoneInfo

PT = ZoneInfo("America/Los_Angeles")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "content", "daily-log")
TYPES = ("Breaking change", "Deadline", "Price change")
TYPE_COLOR = {"Breaking change": "#b42318", "Deadline": "#c08a00", "Price change": "#0b5cad"}
NO_CHANGES = "No verified changes today."
NOTE = "Daily log test, Nov 2\u201313, 2026. Weekdays only. Only verified breaking changes, deadlines and price changes."
FEED_PATH = "new/daily.xml"
FEED_TITLE = "Tool Use Cases: Daily builder log"
CHECKED_RE = re.compile(r"^(0[1-9]|1[0-2]):[0-5]\d (AM|PM)$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
CSS = """
.dl{background:#fff;border:1px solid #ddd;border-radius:8px;padding:6px 18px 12px;margin:18px 0 26px}.dl>h2{margin:14px 0 4px}
.dl-note{background:#f1f8f3;border-left:3px solid #1d6b34;padding:6px 12px;margin:8px 0;font-size:.95rem}
.dl-deadlines{background:#fffaf0;border:1px solid #ecd9a8;border-radius:8px;padding:8px 14px;margin:12px 0}.dl-deadlines h3{margin:2px 0 4px;font-size:1rem}.dl-deadlines ul{margin:4px 0;padding-left:20px}.dl-deadlines li{margin:3px 0}
.dl-day{border-top:1px solid #e3e3e3;margin-top:14px;padding-top:4px}.dl-day h3{font-size:1.12rem;margin:10px 0 6px}.dl-perma{font-size:.85rem;font-weight:400;margin-left:6px}
.dl-items{list-style:none;padding:0;margin:0}.dl-items li{margin-bottom:10px}.dl-items .badge{margin:0 6px 4px 0}.dl-test{font-size:.95rem}
"""

def e(s): return html.escape(str(s))
def x(s): return html.escape(str(s), quote=False)
def iso_date(s): return datetime.strptime(s, "%Y-%m-%d").date()
def mdy(d): return f"{MONTHS[d.month-1]} {d.day}, {d.year}"
def long_date(d): return f"{d.strftime('%A')}, {mdy(d)}"
def today_pt():
    o = os.environ.get("DAILY_LOG_TODAY")
    return iso_date(o) if o else datetime.now(PT).date()
def checked_dt(d, hhmm):  # PT wall-clock time on day d -> aware datetime
    return datetime.strptime(f"{d.isoformat()} {hhmm}", "%Y-%m-%d %I:%M %p").replace(tzinfo=PT)

def _fail(fn, msg): raise ValueError(f"daily log {os.path.basename(fn)}: {msg}")

def load(uc_titles):
    """Return validated days, newest first."""
    days = []
    for fn in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        stem = os.path.basename(fn)[:-5]
        if not ISO_RE.match(stem): _fail(fn, "file name must be YYYY-MM-DD.json")
        raw = open(fn, encoding="utf-8").read()
        if "surroach" in raw.lower(): _fail(fn, "personal surname must not appear on the site")
        d = json.loads(raw)
        if d.get("date") != stem: _fail(fn, f'"date" must equal the file name ({stem})')
        day = iso_date(stem)
        items = d.get("items", [])
        if d.get("no_changes"):
            if items: _fail(fn, '"no_changes": true days must have no items')
            if not CHECKED_RE.match(d.get("checked", "")): _fail(fn, '"checked" must look like "09:30 AM" (Pacific Time)')
        else:
            if not 3 <= len(items) <= 7: _fail(fn, f"a day needs 3-7 items (found {len(items)}), or use \"no_changes\": true")
            for i, it in enumerate(items, 1):
                for k in ("type", "tool", "what", "source_url", "source_name", "checked", "test"):
                    if not str(it.get(k, "")).strip(): _fail(fn, f"item {i} is missing \"{k}\"")
                if it["type"] not in TYPES: _fail(fn, f"item {i} type must be one of {TYPES}")
                if "\n" in it["what"] or len(it["what"]) > 260: _fail(fn, f"item {i} \"what\" must be one line (max 260 characters)")
                if not it["source_url"].startswith("https://") or "tools.lalipublications.com" in it["source_url"]:
                    _fail(fn, f"item {i} source_url must be an official https source")
                if not CHECKED_RE.match(it["checked"]): _fail(fn, f'item {i} "checked" must look like "09:30 AM" (Pacific Time)')
                if it.get("use_case") and it["use_case"] not in uc_titles: _fail(fn, f"item {i} use_case {it['use_case']!r} is not a use-case slug")
                dls = it.get("deadlines", [])
                if it["type"] == "Deadline" and not dls: _fail(fn, f"item {i} is a Deadline but has no \"deadlines\" entry")
                for dl in dls:
                    if not ISO_RE.match(dl.get("date", "")) or not dl.get("label"): _fail(fn, f"item {i} deadlines need \"date\" (YYYY-MM-DD) and \"label\"")
        days.append({"date": day, "preview": bool(d.get("preview")), "no_changes": bool(d.get("no_changes")), "checked": d.get("checked"), "items": items})
    return sorted(days, key=lambda d: d["date"], reverse=True)

def upcoming_deadlines(days, today):
    seen, out = set(), []
    for day in days:
        for it in day["items"]:
            for dl in it.get("deadlines", []):
                dd = iso_date(dl["date"])
                key = (it["tool"], dl["date"], dl["label"])
                if dd >= today and key not in seen:  # passed deadlines drop out at build time
                    seen.add(key); out.append((dd, it, dl, day["date"]))
    return sorted(out, key=lambda t: (t[0], t[1]["tool"]))

def item_html(it, uc_titles):
    c = TYPE_COLOR[it["type"]]
    fits = f' · Fits: <a href="../use-cases/{it["use_case"]}/">{e(uc_titles[it["use_case"]])}</a>' if it.get("use_case") else ""
    return (f'<li class="card"><span class="badge" style="background:{c}">{e(it["type"])}</span><b>{e(it["tool"])}</b>: {e(it["what"])}'
            f'<p class="dl-test"><b>Test for this:</b> {e(it["test"])}</p>'
            f'<p><small>Source: <a href="{e(it["source_url"])}" rel="noopener" target="_blank">{e(it["source_name"])}</a> · Checked {e(it["checked"])} PT{fits}</small></p></li>')

def section_html(days, today, uc_titles, base):
    ups = upcoming_deadlines(days, today)
    strip = "".join(f'<li><b><time datetime="{dd.isoformat()}">{mdy(dd)}</time></b>: {e(it["tool"])}, {e(dl["label"])} <small>(<a href="#{src.isoformat()}">log</a> · <a href="{e(it["source_url"])}" rel="noopener" target="_blank">source</a>)</small></li>' for dd, it, dl, src in ups) \
            or '<li class="muted">No upcoming dated deadlines in the log.</li>'
    out = [f'<section class="dl" id="daily-log" aria-labelledby="daily-log-h">',
           f'<h2 id="daily-log-h">Daily builder log</h2>',
           f'<p class="dl-note">{e(NOTE)}</p>',
           f'<p class="muted"><small>Each item is checked against the tool\'s official changelog, docs or pricing page, with the time we checked it (Pacific Time). Published by Lali Publications. No sponsored items. <a href="{base}{FEED_PATH}">RSS feed for the daily log</a></small></p>',
           f'<div class="dl-deadlines" id="deadlines"><h3>Deadlines</h3><ul>{strip}</ul><p class="muted"><small>Upcoming dated deadlines from the log, soonest first. Passed deadlines drop off automatically.</small></p></div>']
    for day in days:
        a = day["date"].isoformat()
        tag = ' <span class="badge" style="background:#555">Format preview</span>' if day["preview"] else ""
        out.append(f'<article class="dl-day" id="{a}" aria-label="Daily builder log, {mdy(day["date"])}"><h3><time datetime="{a}">{long_date(day["date"])}</time>{tag} <a class="dl-perma" href="#{a}">Permalink</a></h3>')
        if day["preview"]:
            out.append('<p class="muted"><small>Format preview, checked before the test starts. The daily log runs on weekdays from Nov 2 to Nov 13, 2026.</small></p>')
        if day["no_changes"]:
            out.append(f'<p>{NO_CHANGES} <small class="muted">Checked {e(day["checked"])} PT</small></p>')
        else:
            out.append('<ul class="dl-items">' + "".join(item_html(it, uc_titles) for it in day["items"]) + '</ul>')
        out.append('</article>')
    out.append('</section>')
    return "\n".join(out)

def day_pubdate(day):
    times = [day["checked"]] if day["no_changes"] else [it["checked"] for it in day["items"]]
    return max(checked_dt(day["date"], t) for t in times)

def feed_xml(days, base):
    items = []
    for day in days:
        url = f'{base}new/#{day["date"].isoformat()}'
        title = f'Daily builder log: {mdy(day["date"])}' + (" (format preview)" if day["preview"] else "")
        if day["no_changes"]:
            desc = NO_CHANGES
        else:
            desc = " | ".join(f'{it["type"]}: {it["tool"]}: {it["what"]} Test for this: {it["test"]} Source: {it["source_url"]} (checked {it["checked"]} PT)' for it in day["items"])
        items.append(f'  <item><title>{x(title)}</title><link>{url}</link><guid isPermaLink="true">{url}</guid><pubDate>{format_datetime(day_pubdate(day))}</pubDate><category>Daily builder log</category><description>{x(desc)}</description></item>\n')
    last = format_datetime(day_pubdate(days[0])) if days else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{x(FEED_TITLE)}</title>
  <link>{base}new/#daily-log</link>
  <atom:link href="{base}{FEED_PATH}" rel="self" type="application/rss+xml"/>
  <description>{x(NOTE)} Published by Lali Publications.</description>
  <language>en</language>
  <lastBuildDate>{last}</lastBuildDate>
{"".join(items)}</channel>
</rss>
"""

def build(out, base, uc_titles):
    days = load(uc_titles)
    if not days: return
    page = os.path.join(out, "new", "index.html")
    s = open(page, encoding="utf-8").read()
    feed_link = f'<link rel="alternate" type="application/rss+xml" title="Tool Use Cases" href="{base}feed.xml">'
    assert feed_link in s, "daily_log: /new/ <head> changed; update the feed link insertion in daily_log.build"
    s = s.replace(feed_link, feed_link + f'<link rel="alternate" type="application/rss+xml" title="{e(FEED_TITLE)}" href="{base}{FEED_PATH}">', 1)
    anchor = re.search(r'<h1>New releases &amp; trending</h1><p class="lede">.*?</p>\n', s)
    assert anchor, "daily_log: /new/ layout changed; update the section insertion point in daily_log.build"
    s = s[:anchor.end()] + section_html(days, today_pt(), uc_titles, base) + "\n" + s[anchor.end():]
    open(page, "w", encoding="utf-8").write(s)
    open(os.path.join(out, FEED_PATH), "w", encoding="utf-8").write(feed_xml(days, base))
    css = os.path.join(out, "style.css")
    c = open(css, encoding="utf-8").read()
    if ".dl{" not in c: open(css, "a", encoding="utf-8").write(CSS)
