# English-only page upgrades: dated comparison table, FAQ (rendered + FAQPage JSON-LD),
# 'What we checked' note and recent dated changes, keyed by use-case slug.
# Every price, free-tier and news claim here was checked on the official source listed with it on CHECKED.
# HARD RULE: no hands-on test results, benchmarks, quotes or numbers we did not verify. No affiliate links.
# Localized pages (pt-BR, es, Indian languages, ja) do not use this file; they keep their translated content.

CHECKED = "2026-11-04"  # date every row, FAQ fact and news item below was verified

# rows: (tool name, official pricing/source URL we checked, role or "", best for, free tier, entry price, when not to use it)
# news: (iso date, tool, plain-text fact, source name, source URL)
UPGRADES = {}

UPGRADES["best-ai-for-vibe-coding"] = {
 "quick": "Cursor is our top pick if you can work in a code editor or expect the project to grow. "
          "If you have never coded, start with Lovable or Bolt.new: both build a web app from a plain-English description in the browser, and both have free plans.",
 "rows": [
  ("Cursor", "https://cursor.com/pricing", "Top pick",
   "Building and growing a real codebase in an AI code editor",
   "Yes: limited agent and chat requests",
   "Plus $8/mo (Grok models only). Premium $30/mo adds cloud agents; third-party models such as Claude and GPT are billed separately at API list price.",
   "You have never used a code editor and want a hosted app without touching files."),
  ("Lovable", "https://docs.lovable.dev/introduction/subscription-plans", "Runner-up",
   "A full web app with login and a database from a description, without coding",
   "Yes: 5 build credits a day, up to 30 a month",
   "Pro from $25/mo for 100 credits a month",
   "You need full control of the code and stack, or the app is not a web app."),
  ("Bolt.new", "https://bolt.new/pricing", "Free option",
   "Trying an app idea for free in the browser, with hosting included",
   "Yes: 1M tokens a month with a daily limit; Bolt branding on sites",
   "Pro $25/mo billed monthly (less if billed yearly): 10M tokens a month and your own domain",
   "You need your own domain or no Bolt branding but don't want to pay: both need Pro."),
  ("v0", "https://v0.app/pricing", "",
   "A polished React/Next.js front end that deploys to Vercel",
   "Yes: 7 messages a day",
   "Plus $30 per user/mo, with $30 of monthly credits",
   "You don't want to deal with React code at all."),
  ("Replit Agent", "https://replit.com/pricing", "",
   "Building and hosting an app in one browser tab",
   "No free plan is listed on the pricing page",
   "Core $20/mo ($18/mo billed yearly), with $20 toward model usage",
   "You want to try an idea without paying."),
 ],
 "faq": [
  ("What is vibe coding?",
   "Building software mostly by describing what you want in plain language and letting an AI tool write, run and fix the code, while you test the result and ask for changes."),
  ("What is the best AI tool for vibe coding?",
   "Cursor, if you can work in a code editor or expect the project to grow. If you have never coded, start with Lovable or Bolt.new, which build a web app from a description in the browser."),
  ("Can I vibe code for free?",
   "Yes, to try an idea. As of Nov 4, 2026, Cursor, Lovable, Bolt.new and v0 all have free plans with limits: Bolt.new's includes 1M tokens a month, Lovable's gives 5 build credits a day (up to 30 a month), and v0's allows 7 messages a day. Replit's pricing page lists no free plan."),
  ("Lovable or Bolt.new: which should I use?",
   "Both build full web apps from a description, and both have free plans. Lovable Pro starts at $25/mo for 100 credits; Bolt.new Pro is $25/mo billed monthly with 10M tokens and your own domain. We have not run a head-to-head test, so try the same idea on both free plans and keep the one whose result you would rather keep editing."),
  ("When should I move from an app builder to Cursor?",
   "When you want to own and edit the code directly, work in an existing repository, or the project has outgrown what you can manage by chat. Cursor has a free plan; Plus ($8/mo) runs Grok models only, and Premium ($30/mo) adds cloud agents and third-party models billed at API list price."),
  ("Are these picks paid placements?",
   "No. Picks are editorial and not paid, and there are no affiliate links."),
 ],
 "news": [
  ("2026-10-30", "Bolt.new",
   "Database tables created after Oct 30 are private by default, so your app needs explicit permissions to read or write them. Existing databases are not affected.",
   "Bolt release notes", "https://support.bolt.new/release-notes"),
  ("2026-10-28", "Lovable",
   "Workspace admins and owners now get an email when credits are likely to run out before the monthly refill. No email is sent while auto top-up is on.",
   "Lovable changelog", "https://docs.lovable.dev/changelog"),
 ],
 "notes": [
  "Lovable's pricing page loads its prices in the browser, so we took the Pro entry price from Lovable's official Subscription plans documentation.",
 ],
}
