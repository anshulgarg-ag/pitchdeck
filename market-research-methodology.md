# Market-Insight Research Methodology
### AI-tutor → school-ERP startup · Private + Govt K-12 · NCR beachhead (Haryana + New Delhi)

> **This is a HOW-TO, not findings.** It tells you *what* to research, *in what order*, *from which
> sources*, and *with which prompts*. No TAM numbers or competitor verdicts are filled in here —
> you (with Claude) generate those by running the steps. Built on the *Founder's Playbook* Idea
> stage. Re-run whenever your hypothesis changes — market research is a loop, not a one-time task.

---

## 0. How to use this doc

**The one rule that governs everything below:** every validation step is paired with a
**disconfirming step**. The playbook's core warning — *"Ask AI to size your market and it will
find the number that makes your TAM look fundable."* AI follows your direction. So you point it
in the opposite direction on purpose. If a step only has a "prove it" prompt and no "kill it"
prompt, you are doing it wrong.

**Which Claude surface for which job** (from the playbook):
| Job | Surface |
|---|---|
| Quick sanity check, rewrite, single question | **Chat** |
| Multi-source synthesis → a finished doc/sheet (competitive landscape, review synthesis, TAM model) | **Claude Cowork** |
| Pulling/scraping data, parsing raw review dumps, scripting UDISE+ data | **Claude Code** |

**Sequence:** Step 0 → 1 → 2 → 3 → 4 → 5, with Step 6 (adversarial) running *continuously* the
whole time. Do not skip to TAM (Step 3) before the hypothesis (Step 0) is testable — a fuzzy
hypothesis produces a fundable-looking but meaningless market size.

---

## Step 0 — Sharpen the hypothesis until it's testable

You can't research a vague idea. Turn the idea into a statement that names **who** has the
problem, **how often**, **how severely**, and **what they do about it today**.

- ❌ Not testable: *"Schools in India need better software."*
- ✅ Testable: *"Government and low-fee private schools in Haryana & Delhi have 35+ students per
  teacher and no tool that grades/plans lessons in Hindi on a low-end Android phone, so teachers
  spend [X] hrs/week on manual grading and admin, currently coping with paper registers + WhatsApp."*

You'll actually write **two** hypotheses — they have different buyers and economics:
1. **AI-tutor/teacher wedge** (who feels the pain: teachers, students).
2. **ERP expansion** (who pays and renews: principal / trust / govt dept).

> **Prompt (Chat):** "Here is my problem statement: [paste]. Force it to be testable: rewrite it
> so it names exactly who has the problem, how often, how severe it is, and their current
> workaround. Then list every word in it that is still vague or unmeasurable."
>
> **Disconfirming prompt:** "Now argue this problem is *not* real or not frequent enough to build a
> business on. What evidence would I expect to see if schools actually *don't* feel this pain?"

**Exit of Step 0:** two one-sentence hypotheses a stranger could go verify.

---

## Step 1 — Map the competitive landscape by tier

Beware **competitor neglect** — obsessing over your vision and under-weighting everyone else.
Map four tiers (playbook), and for **each** competitor run the adversarial prompt.

| Tier | Who (start list — verify + expand) |
|---|---|
| **Direct** | Teachmint, LEAD School, Classplus, Extramarks, Vedantu (school arm), Entab/Fedena/MyClassCampus (ERP), Google Classroom |
| **Indirect** (the real default) | WhatsApp + Excel + paper registers, private tuition centres, free ChatGPT/Gemini used ad-hoc by teachers |
| **Potential acquirers** | LEAD, PhysicsWallah, Extramarks, Google/Microsoft edu, large school chains |
| **Adjacent movers** | Telcos (Jio education), govt platforms (DIKSHA), generic AI vendors adding an edu skin |

Method: for each named player capture — what they do, who they sell to, price, distribution, and
their **weak spot** (from Step 2 reviews). Build it as one table in Claude Cowork.

> **Prompt (Cowork):** "Map my competitive landscape across four tiers — direct, indirect,
> potential acquirers, adjacent — for an AI-tutor + school-ERP product targeting private and govt
> K-12 schools in Haryana and Delhi. For each named competitor: what they do, buyer, pricing model,
> primary distribution channel."
>
> **Disconfirming prompt (the antidote to competitor neglect):** "For each competitor, make the
> *strongest possible* argument for why they win this market and I don't — why a school would choose
> them, and why my differentiators (AI-first, vernacular, land-and-expand) are less defensible than
> I think. Don't give me the easy-to-dismiss version of the threat."

---

## Step 2 — Mine competitor reviews (free qual research on THEIR customers)

Every complaint about an incumbent is a free interview with your future customer. Pull reviews,
synthesize the **top unresolved complaints**, then check: does my hypothesis fix any of them?

**Sources:**
- **Google Play + Apple App Store** reviews for the Teachmint, LEAD, Classplus, Extramarks apps
  (sort by recent + by lowest rating — the 1–2★ reviews are the goldmine).
- **G2, Capterra, SoftwareSuggest** (India-heavy) for the ERP tools.
- YouTube comments on demo/review videos; education Facebook groups; principal/teacher WhatsApp
  communities; Reddit (r/india, r/CBSE, r/Teachers).

Method: Claude Code scrapes/ingests the review text → Claude Cowork synthesizes recurring themes.

> **Prompt (Cowork):** "Here are [N] reviews of [competitor] apps [paste/attach]. Synthesize the
> top 10 recurring complaints existing solutions have NOT resolved. Rank by frequency and
> intensity. Flag which relate to (a) teacher workload, (b) language/vernacular, (c) low-end device
> performance, (d) price."
>
> **Disconfirming prompt:** "Which of these complaints are actually *minor* or *unfixable*, and
> which are things users say they hate but keep paying for anyway? Where am I over-reading a few
> loud reviews as a market-wide need?"

---

## Step 3 — Size the market (TAM/SAM/SOM), then try to break it

Build it **bottom-up** (defensible) *and* **top-down** (sanity check). Never trust one alone.

**Primary data source — use this, not vibes:**
- **UDISE+ dashboard** → `https://dashboard.udiseplus.gov.in` — authoritative count of schools,
  enrolment, teachers, by **state and district**, with **private vs government** split. Pull
  Haryana and Delhi specifically.
- Backups: Ministry of Education / UDISE+ annual reports, Haryana & Delhi state education dept
  sites, Census projections.
- Market $$ context: IBEF EdTech reports, RedSeer, Inc42, Tracxn, NEP 2020 document.

**Bottom-up (your real number):**
`(target schools in Haryana + Delhi) × (avg students per school) × (₹ per student per year)`
Split by segment — private vs govt have different school counts, budgets, and sales cycles.

**Top-down (sanity check):** India EdTech market $ × your addressable slice. If bottom-up and
top-down are off by 10×, an assumption is wrong — find it.

**Funnel:** TAM (all K-12 India) → SAM (private + govt K-12 in Haryana + Delhi that are digital-
ready) → **SOM** (what you can actually win in 3 years given a pre-seed budget and founder-led sales).

**Buyer-landscape map** (who to actually sell to):
| | Private school | Govt school |
|---|---|---|
| Holds budget | Principal / trust / owner | State edu dept / district (block) office |
| Influences | Senior teachers, parents | Teachers, block education officer |
| Blocks / slows | — | Tenders, procurement rules, approval chains |

> **Prompt (Cowork):** "Build a bottom-up and a top-down TAM/SAM/SOM for private + govt K-12
> schools in Haryana and Delhi, using UDISE+ school and enrolment counts [attach the pulled data].
> Show every assumption as a separate, editable line."
>
> **Disconfirming prompts (do all three):**
> 1. "Attack this model. Which single assumption, if wrong, collapses the SOM? What's the
>    realistic downside case?"
> 2. "Is this market expanding, consolidating, or mature? Factor in the post-BYJU'S EdTech funding
>    winter and school-software fatigue."
> 3. "Can a pre-seed, founder-led team realistically close **government** school procurement in
>    NCR within 18 months? If not, what SOM survives if I exclude govt for now?"

---

## Step 4 — Trend & timing analysis (are you early, on-time, or late?)

Surface **three** external trends (regulatory / technological / demographic) and tag each as a
**tailwind or headwind** for *your specific* hypothesis — not for "EdTech" in general.

Candidates to investigate (don't assume — verify direction):
- **Regulatory:** NEP 2020 mandates (personalized, multilingual, tech-enabled learning); govt
  DIKSHA push; data-protection (DPDP Act) implications for handling minors' data.
- **Technological:** vernacular LLM maturity (Hindi/regional), AI inference cost collapse,
  low-end Android + cheap data penetration in Haryana/Tier-2.
- **Demographic / market:** private-school enrolment shifts, post-BYJU'S investor sentiment
  (headwind for fundraising, possible tailwind for cheap acqui-hires/talent).

**Where to listen for the real language users use:** r/india, r/CBSE, r/Teachers, r/Btechtards
(parents), LinkedIn school-admin & principal-association groups, edu Facebook groups. Capture the
*exact words* teachers/principals use for the pain — you'll reuse them in the deck and interviews.

> **Prompt (Chat/Cowork):** "Identify three external trends — one regulatory, one technological,
> one demographic — that will significantly affect AI school software in Haryana/Delhi over the
> next two years. For each, state whether it is a tailwind or a headwind for MY hypothesis
> specifically, and the evidence."
>
> **Disconfirming prompt:** "Make the case that I am too *late* (incumbents + free AI already
> own this) and separately that I am too *early* (schools/govt won't adopt AI at scale yet).
> Which is the bigger risk?"

---

## Step 5 — Design customer discovery (before you build anything)

Quality of learning = (quality of questions) × (talking to the right people).

**ICP / who to talk to** — name titles, not a vague list:
- Private: **principal, school owner/trustee, headmaster, senior/coordinator teacher.**
- Govt: **teacher, headmaster, Block Education Officer (BEO), district education official.**
Then map *where they're reachable* in NCR: principal associations, CBSE/school-cluster meets,
edu conferences, LinkedIn, school-vendor WhatsApp groups. Prioritize by closeness to the pain.

**What to ask** — the rookie mistake is future-hypotheticals. Ask about the **past**:
- ❌ "Would you use an AI tool like this?" → ✅ "Walk me through the last time you graded a class
  set of papers / chased fee defaulters. How long did it take? What did you use?"
Build **separate question sets per persona** — a teacher and a principal relate to the same
problem differently; a govt BEO differently again.

> **Prompt (Chat):** "Here are my draft discovery questions [paste]. Flag every question that is
> leading, future-facing, too broad, or likely to get a socially-desirable answer instead of an
> honest one. Then rewrite them as past-behavior questions, and give me a follow-up probe for the
> 3 moments most likely to produce a vague or deflecting answer."
>
> **After interviews (Cowork):** "Here are my notes from 5 interviews. Produce two lists: evidence
> that supports my hypothesis, and evidence that challenges it."
>
> **Disconfirming prompt:** "If the support list is much longer than the challenge list, tell me
> whether that reflects the data — or whether I'm pattern-matching to what I want to hear."

---

## Step 6 — The adversarial pass (runs the WHOLE time, not once)

The playbook's non-negotiable: *"AI will pressure-test an idea just as thoroughly as it validates
one."* Use it deliberately at every step above, plus these standing exercises:

- **Pre-mortem:** "It's 18 months from now and the startup failed. Write the post-mortem — the 5
  most likely reasons, ranked." (Expect: govt procurement too slow; free ChatGPT good enough;
  schools won't pay; teacher adoption stalls; can't reach schools cheaply.)
- **Failed comparables:** "What killed / stalled BYJU'S, and which of those failure modes could
  hit a B2B school-SaaS in NCR? What happened to past govt-EdTech procurement pushes?"
- **Steelman a competitor:** the Step 1 prompt, quarterly.
- **Confirmation-bias checklist** — before trusting any finding, ask:
  - Did I ask Claude to *prove* this or to *test* it?
  - Is my number from UDISE+/reviews (real) or from AI's plausible guess?
  - Would this survive a skeptical investor who wants to see the raw source?

---

## Exit criteria — are you allowed to build yet?

Leave the research/Idea stage only when you can answer **yes** to all three (playbook):
1. **Is the problem real and specific?** You can name exactly who has it, how often, how severe,
   and their current workaround — backed by real conversations, not assumptions.
2. **Does your solution address the *actual* problem** the research revealed (not the one you
   assumed going in)?
3. **Is there enough signal to justify building?** Not certainty — enough qualitative evidence
   that committing to the MVP is a reasoned decision, not faith.

If any answer is no, or the adversarial pass keeps surfacing the same unaddressed risk, that's the
signal to **adjust the hypothesis or pivot** — before writing production code, not after.

---

## Appendix A — Source list (India / NCR specific)

| Purpose | Source |
|---|---|
| School/enrolment/teacher counts, private vs govt, by district | **UDISE+ dashboard** — dashboard.udiseplus.gov.in |
| Reports & national data | Ministry of Education / UDISE+ reports; Haryana & Delhi state edu dept sites |
| EdTech market size & trends | IBEF, RedSeer, Inc42, Tracxn, KPMG/Google India EdTech reports |
| Policy | NEP 2020 document; DIKSHA; DPDP Act (data of minors) |
| Competitor reviews | Google Play, Apple App Store, G2, Capterra, SoftwareSuggest |
| User language / signals | Reddit (r/india, r/CBSE, r/Teachers), LinkedIn edu groups, FB/WhatsApp principal groups, YouTube |

## Appendix B — Master prompt pattern

For any step, structure the session as:
1. **Context:** paste hypothesis + segment (private+govt K-12, Haryana+Delhi) + stage (pre-seed).
2. **Validate:** ask for the analysis.
3. **Refute:** ask Claude to argue the opposite / find disconfirming evidence.
4. **Source-check:** "Which claims here are from real data I gave you vs. your own estimate? Label
   each."
5. **Log:** save the output; note what changed in your hypothesis.

> Repeat the loop whenever the hypothesis evolves. Research is continuous through MVP and Launch.
