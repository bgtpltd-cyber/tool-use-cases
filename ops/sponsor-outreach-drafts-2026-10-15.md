# Sponsor Outreach Drafts: Tool Use Cases (2026-10-15)

**STATUS: DRAFTS ONLY. Nothing has been sent.** Larry reviews every draft before it goes out.
**From:** Larry Surroach <larrys@lalipublications.com>
**Pricing:** one price per page, so every tool pitched on the same page gets the same rate: vibe coding $199/mo; image generation, video/YouTube and research $149/mo; game prototyping $99/mo. These are proposed introductory rates (revenue we'd charge). They are not on the site yet. The sponsor page currently says "Pricing and availability on request."

---

## ⚠️ Fix before sending: HTTPS is broken on the live site (checked 2026-10-15, ~3:45 PM PT)

- `https://tools.lalipublications.com/...` fails with a certificate error. GitHub Pages is serving its default `*.github.io` certificate, not one for `tools.lalipublications.com`. Most browsers will show a security warning, which is a bad first click for a sponsor.
- `http://tools.lalipublications.com/...` works. Every page linked below loaded over HTTP and shows the expected content and the "Sponsored · Your tool here" slot.
- **Fix:** in GitHub repo → Settings → Pages, confirm the custom domain `tools.lalipublications.com`, wait for the certificate to be issued, and tick **Enforce HTTPS**. Then open one https link in a browser before sending anything.
- The drafts below use `https://` links because that's what the site should serve. Don't send until HTTPS works. If you have to send sooner, change the links to `http://`.

## Link verification (each fetched 2026-10-15)

| Link | Over HTTP | What the page shows |
|---|---|---|
| /use-cases/best-ai-for-vibe-coding/ | ✅ loads | Lovable at #2, Bolt.new at #5 |
| /use-cases/best-ai-image-generation/ | ✅ loads | Ideogram at #3 |
| /use-cases/best-ai-for-video-youtube/ | ✅ loads | OpusClip at #5 |
| /use-cases/best-ai-for-game-prototyping/ | ✅ loads | Rosebud AI at #1, Scenario at #3, Meshy at #4 |
| /use-cases/best-ai-for-research/ | ✅ loads | Elicit at #5 |
| /sponsor/ | ✅ loads | How it works, labeling rules, sponsor mailto |

Every target is already listed on its page as an unpaid editorial pick. The emails say so honestly and make clear that paying doesn't change that.

Site footer updated 2026-10-15 to "by Lali Publications" (was "run autonomously"). OpusClip spelling fixed on the site.

## Contacts (send-to)

| # | Target | Send to | Source / confidence |
|---|---|---|---|
| 1 | Lovable | [CONTACT_FORM: https://lovable.dev/partners] (alt: community@lovable.dev) | community@lovable.dev is on lovable.dev/community for partnerships/content. press@ is press-only. /partners form loads. |
| 2 | Bolt.new | hello@stackblitz.com (alt: [CONTACT_FORM: https://bolt.new/contact]) | Verified in the stackblitz/bolt.new GitHub README. The contact page loads (200). |
| 3 | Ideogram | [CONTACT_FORM: https://ideogram.ai/enterprise/] | The enterprise page loads (200). No email is published on it. partnership@ideogram.ai is weakly sourced, so don't use it. |
| 4 | OpusClip | partnerships@opus.pro | Verified on OpusClip's official "Beware of Scams" blog post, which names it as the partnerships/sponsorship contact. |
| 5 | Meshy | [CONTACT_FORM: https://www.meshy.ai/partners] (fallback: partnerships@meshy.ai) | The partners page loads (200). Form replies come from partnerships@meshy.ai. influencer@meshy.ai is for KOL/creator deals. |
| 6 | Scenario | [CONTACT_FORM: https://www.scenario.com/contact-us] | The page loads (200). No email is published on it. contact@scenario.com is unconfirmed, so don't use it. |
| 7 | Rosebud AI | support@rosebudai.com | Verified on rosebud.ai. Site says this inbox covers press and partnerships. |
| 8 | Elicit | sales@elicit.com | Verified on Elicit's help center and SOC 2 blog post. It's a sales inbox, so the draft asks them to forward to marketing. |

For form submissions: paste the body, use the first subject line as the form's subject or message title if it has one, and give larrys@lalipublications.com as the reply address.

---

## 1. Lovable

**To:** [CONTACT_FORM: https://lovable.dev/partners] (alt: community@lovable.dev)
**Subject A:** Featured slot for Lovable on "Best AI for vibe coding"
**Subject B:** Lovable is already on our vibe coding page. Want the featured slot?

Hi Lovable team,

I'm Larry. I run Tool Use Cases, a small curated directory that sorts AI tools by the job you need done. It's written for vibe coders and builders deciding what to use.

Lovable is already one of our editorial picks on Best AI for vibe coding ("fastest path from idea to a working web app"):
https://tools.lalipublications.com/use-cases/best-ai-for-vibe-coding/

Each page has one featured slot at the top, labeled "Sponsored" and kept separate from our picks. Paying doesn't change rankings or verdicts.

We're early: the directory, use-case pages and a new-releases section are live, and traffic is still growing. So I'm offering an introductory **$199/month** for that slot, cancel anytime.

Details: https://tools.lalipublications.com/sponsor/

If this isn't your inbox, I'd be grateful if you'd forward it to whoever handles partnerships. Interested? Just reply and we'll talk.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 2. Bolt.new

**To:** hello@stackblitz.com (alt: [CONTACT_FORM: https://bolt.new/contact])
**Subject A:** Featured slot for Bolt.new on "Best AI for vibe coding"
**Subject B:** Bolt.new + Tool Use Cases: one clearly labeled sponsor slot

Hi StackBlitz team,

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by use case for vibe coders and builders.

Bolt.new is one of our editorial picks on Best AI for vibe coding ("great for spinning up a full-stack demo in one tab"):
https://tools.lalipublications.com/use-cases/best-ai-for-vibe-coding/

At the top of that page is one featured slot. It's labeled "Sponsored" and never affects our rankings or verdicts. It reaches people who are comparing prompt-to-app builders right when they're about to pick one.

Honest status: we're early. The directory, use-case pages and a new-releases section are live, and traffic is building. Introductory rate: **$199/month**, cancel anytime.

How it works: https://tools.lalipublications.com/sponsor/

If you'd like to talk about it, just reply. And if someone else handles partnerships, a forward would be much appreciated.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 3. Ideogram

**To:** [CONTACT_FORM: https://ideogram.ai/enterprise/]
**Subject A:** Featured slot for Ideogram on "Best AI image generation"
**Subject B:** Reaching builders who need readable text in images

Hi Ideogram team,

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by the job you need done. It's for builders and vibe coders making apps, thumbnails, logos and mockups.

Ideogram is already an editorial pick on Best AI image generation. Our verdict: "pick this when the image needs readable text."
https://tools.lalipublications.com/use-cases/best-ai-image-generation/

The page has one featured slot at the top. It's labeled "Sponsored," kept apart from our picks, and never changes rankings. For you it could also point builders to the API.

We're early: the directory and use-case pages are live, and traffic is still growing. Introductory rate: **$149/month**, cancel anytime.

Details: https://tools.lalipublications.com/sponsor/

If you'd like to discuss it, reply to larrys@lalipublications.com. I'd also appreciate a forward to your marketing or partnerships lead.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 4. OpusClip

**To:** partnerships@opus.pro
**Subject A:** Featured slot for OpusClip on "Best AI for video and YouTube"
**Subject B:** OpusClip + Tool Use Cases: a labeled sponsor spot for creators

Hi OpusClip team,

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by use case for creators, builders and vibe coders.

OpusClip is one of our editorial picks on Best AI for video and YouTube ("turns a long video or stream into Shorts/TikToks automatically"):
https://tools.lalipublications.com/use-cases/best-ai-for-video-youtube/

At the top of that page is a single featured slot. It's labeled "Sponsored" and separate from our picks, and it never changes rankings. It puts you in front of people choosing their video stack.

Being straight with you: we're early. The directory, use-case pages and a new-releases section are live, and traffic is growing. Introductory rate: **$149/month**, cancel anytime.

How it works: https://tools.lalipublications.com/sponsor/

If you'd like to discuss it, just reply.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 5. Meshy

**To:** [CONTACT_FORM: https://www.meshy.ai/partners] (fallback: partnerships@meshy.ai)
**Subject A:** Featured slot for Meshy on "Best AI for game prototyping"
**Subject B:** Meshy + indie game builders: one labeled sponsor slot

Hi Meshy team,

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by the job you need done, for builders and vibe coders.

Meshy is an editorial pick on Best AI for game prototyping ("quick 3D props and characters to block out levels"):
https://tools.lalipublications.com/use-cases/best-ai-for-game-prototyping/

The page has one featured slot at the top. It's labeled "Sponsored," kept separate from our picks, and never changes rankings. Readers are people trying to get a playable idea on screen fast, which is right where Meshy fits.

We're early: the directory and use-case pages are live, and traffic is still building. Introductory rate: **$99/month**, cancel anytime.

Details: https://tools.lalipublications.com/sponsor/

If you'd like to talk it through, reply to larrys@lalipublications.com.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 6. Scenario

**To:** [CONTACT_FORM: https://www.scenario.com/contact-us]
**Subject A:** Featured slot for Scenario on "Best AI for game prototyping"
**Subject B:** Scenario + Tool Use Cases: reaching indie game builders

Hi Scenario team,

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by use case for builders and vibe coders.

Scenario is an editorial pick on Best AI for game prototyping. Our verdict: "keeps game art consistent in your own style, the hard part of AI art for games."
https://tools.lalipublications.com/use-cases/best-ai-for-game-prototyping/

The top of that page has one featured slot. It's labeled "Sponsored," always separate from our picks, and it never affects rankings.

Honest status: we're early. The directory and use-case pages are live, and traffic is growing. Introductory rate: **$99/month**, cancel anytime.

How it works: https://tools.lalipublications.com/sponsor/

If you'd like to discuss it, reply to larrys@lalipublications.com. A forward to whoever runs marketing would also be appreciated.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 7. Rosebud AI

**To:** support@rosebudai.com
**Subject A:** Featured slot for Rosebud AI on "Best AI for game prototyping"
**Subject B:** Rosebud is our #1 game-prototyping pick. Quick sponsor idea

Hi Rosebud team,

I'm Larry. I run Tool Use Cases, a small curated directory that sorts AI tools by use case for vibe coders and builders.

Rosebud AI is the first pick on our Best AI for game prototyping page ("prompt a browser game into existence and remix others' games"):
https://tools.lalipublications.com/use-cases/best-ai-for-game-prototyping/

That spot is editorial and unpaid, and it stays that way whatever you decide. Separately, the page has one featured slot at the top, clearly labeled "Sponsored."

We're early: the directory and use-case pages are live, and traffic is still building. Introductory rate: **$99/month**, cancel anytime.

Details: https://tools.lalipublications.com/sponsor/

Could you pass this to whoever handles partnerships? If it's interesting, a reply is all it takes.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## 8. Elicit

**To:** sales@elicit.com
**Subject A:** Featured slot for Elicit on "Best AI for research" (please forward to marketing)
**Subject B:** Elicit + Tool Use Cases: one labeled sponsor slot

Hi Elicit team,

I know this is the sales inbox, so I'd be grateful if you'd forward this to marketing or partnerships.

I'm Larry. I run Tool Use Cases, a curated directory that sorts AI tools by the job you need done.

Elicit is an editorial pick on Best AI for research ("purpose-built for academic papers and literature reviews"):
https://tools.lalipublications.com/use-cases/best-ai-for-research/

The page has one featured slot at the top. It's labeled "Sponsored," separate from our picks, and it never changes rankings.

We're early: the directory and use-case pages are live, and traffic is growing. Introductory rate: **$149/month**, cancel anytime.

Details: https://tools.lalipublications.com/sponsor/

If you'd like to discuss it, just reply.

Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## Reusable follow-up (send ~7 days later, around 2026-10-22, as a reply in the same thread)

**Subject:** Re: [original subject]

Hi [TEAM/NAME],

Quick follow-up on my note about the featured slot for [TOOL] on [USE-CASE PAGE NAME]:
[USE-CASE URL]

To recap: it's one slot at the top of the page, clearly labeled "Sponsored." It never changes our editorial picks, and it's [$PRICE]/month at our introductory rate, cancel anytime.

If the timing's wrong or it isn't a fit, just let me know and I won't follow up again. If someone else on your team handles this, I'd appreciate a pointer.

Thanks,
Larry Surroach
Tool Use Cases / Lali Publications
larrys@lalipublications.com

---

## Pre-send checklist (re-checked by Joe 2026-10-15)

- [x] No traffic, subscriber, or click numbers. No press logos or testimonials.
- [x] Tool names match the products: Lovable, Bolt.new (StackBlitz), Ideogram, OpusClip, Meshy, Scenario, Rosebud AI, Elicit.
- [x] Each URL points to a page that exists and lists that tool (checked over HTTP).
- [x] Every email links to the sponsor page and states the price with "cancel anytime."
- [x] Contacts are either verified emails or official contact forms. No guessed addresses.
- [x] Site spelling OpusClip + footer "by Lali Publications" deployed to gh-pages.
- [ ] **HTTPS is working on tools.lalipublications.com (open one link in a browser).**
- [ ] Larry has approved each draft.
