# Market Research — Findings
### AI-tutor → school-ERP startup · Private + Govt K-12 · NCR beachhead (Haryana + New Delhi)
**Run date:** 2026-07-09 · Method: executed `market-research-methodology.md` · Adversarial pass: included

> **Read this first.** Numbers below are **web-sourced estimates**, labeled by confidence.
> Anything tagged 🔴 **VERIFY** must be pulled from **UDISE+** (dashboard.udiseplus.gov.in) before
> it goes in an investor deck — per the methodology's source-check rule, don't ship a number you
> can't trace. The playbook's warning stands: a fundable-looking TAM is not evidence.

---

## 0. Executive read

- The **wedge is real and timely.** AI in Indian schools just went from optional to **mandated**:
  AI + computational thinking become **compulsory from Class 3, starting AY 2026-27** (MoE, Oct 2025).
  ~70% of Indian teachers already use AI tools, mostly for lesson planning. You are entering *with*
  a regulatory + behavioral tailwind, not against one. 🟢
- The **B2B choice is right.** DPDP Act 2023 imposes one of the world's strictest child-data regimes
  (verifiable parental consent for under-18s, no profiling/targeted ads). But a vendor acting as a
  **Data Processor *for the school*** is largely shielded — this is a structural reason B2B-to-schools
  beats B2C-to-parents right now, and a moat vs. consumer AI apps. 🟢
- The **market is smaller and more skeptical than the headlines.** Real India K-12 *online* spend is
  ~**$2–3B**, not the $7.5–12B "EdTech market" figures. Post-BYJU's, parent/school sentiment shifted
  from FOMO to "fear of getting scammed." Willingness to *pay* is the constraint, not awareness. 🟡
- **The single biggest threat is not a competitor — it's "free."** 70% teacher AI adoption is mostly
  free ChatGPT/Gemini. Your paid tutor must beat *free + syllabus-unaligned*, not beat Teachmint. 🔴
- **Govt schools: do not underwrite the near-term.** Procurement is slow, tender-bound, thin-budget.
  Treat govt as an 18-36 mo option (via state AI mandates), **not** your pre-seed SOM.

**Verdict:** Proceed to customer discovery on the **private-school AI-tutor wedge in NCR**. Exclude
govt from the fundable SOM. The idea survives the adversarial pass **with two open risks** (pricing
power vs. free AI; DPDP compliance cost) that discovery must resolve before you build.

---

## 1. Market size — NCR beachhead (Haryana + Delhi)

### School counts
| Region | Total schools | Govt / aided | Private unaided | Students | Confidence |
|---|---|---|---|---|---|
| **Delhi** | ~5,500 | ~1,053 govt + ~201 aided | ~4,243 | ~45 lakh (4.5M); ~62% in govt/aided | 🟡 secondary sources |
| **Haryana** | ~23,500 (22 districts) | majority govt | ~8,500–9,000 est | ~55–60 lakh est | 🔴 VERIFY split in UDISE+ |
| **NCR total** | **~29,000** | — | **~13,000 serviceable** | **~1 crore (10M)** | 🔴 VERIFY |

Sources: [Delhi schools breakdown](https://grokipedia.com/page/List_of_schools_in_Delhi),
[Delhi planning/education dept](https://delhiplanning.delhi.gov.in/sites/default/files/Planning/15._education.pdf),
[Haryana UDISE+ (23,494 schools)](https://www.mahadevmaitri.org/education/haryana),
primary: [UDISE+ dashboard](https://dashboard.udiseplus.gov.in/).

### TAM / SAM / SOM (software revenue, not "market size")
Pricing anchor: Indian school SaaS runs **₹10k–₹1L/yr flat** or per-student; Teachmint lists
**$5/user/yr**; ERP per-student models common. Assume blended **₹300/student/yr** for the AI-tutor tier
(🟡 assumption — test in discovery).

| Layer | Definition | Estimate | Basis |
|---|---|---|---|
| **TAM** | All India K-12 software | ~248M students × ₹300 ≈ **₹7,400 Cr (~$900M)** | [Economic Survey: 24.8 cr students, 14.7L schools](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097864&reg=3&lang=2) |
| **SAM** | NCR private+aided K-12, digital-ready | ~4M students in ~13,000 schools × ₹300 ≈ **₹120 Cr (~$14M) ARR** | school counts above |
| **SOM (3 yr)** | Pre-seed, founder-led, private-only | ~150–300 schools, ~150k–300k students → **₹4–12 Cr (~$0.5–1.5M) ARR** | 🔴 conservative; excludes govt |

> **Adversarial check (done):** ① The assumption that collapses SOM = **₹/student willingness-to-pay**
> if free AI is "good enough." Downside: ₹0 for tutor, revenue only from ERP → different business.
> ② Market is **consolidating, not expanding** at the top (BYJU's imploded, PhysicsWallah IPO'd at
> $5.2B) — but **fragmenting at the bottom** (thousands of small school-SaaS vendors) = your opening.
> ③ Govt SOM in 18 mo = realistically **~0** without a channel partner or empanelment.

---

## 2. Competitive landscape

| Tier | Player | Model | Scale / signal | Weak spot (your opening) |
|---|---|---|---|---|
| **Direct** | [Teachmint](https://tracxn.com/d/companies/teachmint/__2OhzJsaQqn1Rx--LmV-MYhMY7hVCfzgx9GyitF_ntU8) | LMS/ERP, $5/user/yr, freemium | ~4,000 institutions, ₹102 Cr rev FY25, **staff 790→187** | Distress signal; thin AI; commodity LMS |
| **Direct** | [LEAD School](https://digitallearning.eletsonline.com/2024/08/lead-groups-fy24-revenue-reaches-%E2%82%B9370-cr-slashes-cash-burn-by-65/) | Full curriculum+pedagogy+tech bundle | ~8,000 schools, ₹370 Cr FY24, $740M val | Heavy, expensive, full-stack lock-in; not AI-tutor-first |
| **Direct** | Classplus / Extramarks | Coaching SaaS / content | large but coaching + content focus | Not teacher-workflow/ERP for schools |
| **Direct (ERP)** | [Fedena, MyClassCampus, Entab](https://fedena.com/pricing-and-plans) | School ERP, ₹10k–₹2L/yr | many small schools | **No real AI**, dated UX, opaque pricing |
| **Indirect (the real default)** | **WhatsApp + Excel + paper**, and **free ChatGPT/Gemini** | free | ~70% teachers already use free AI | Free, but not syllabus-aligned, not vernacular-tuned, no school workflow, **DPDP-noncompliant for schools** |
| **Potential acquirers** | LEAD, PhysicsWallah, Extramarks, Google/Microsoft edu | — | consolidating buyers | — |
| **Adjacent movers** | DIKSHA (govt), state AI curricula (Punjab, Odisha), telco edu | — | govt-backed, free | Slow, generic; not a school-ops product |

> **Adversarial (competitor-neglect antidote):** The strongest case *against* you — **free ChatGPT is
> already in 70% of teachers' hands** and improving monthly; a school may never pay for a tutor layer.
> The defensible answer must be **syllabus-alignment + vernacular + DPDP-compliant school workflow +
> ERP stickiness** — none of which raw ChatGPT provides. If discovery shows teachers won't pay for
> that gap, the tutor is a free acquisition wedge and **ERP is the actual revenue product.**

Sources: [Teachmint FY24 (Inc42)](https://inc42.com/buzz/teachmint-cuts-fy24-loss-to-inr-110-cr-revenue-soars-111/),
[LEAD unicorn (TechCrunch)](https://techcrunch.com/2022/01/12/lead-school-india-unicorn/),
[ERP pricing (Fedena / SchoolSoftwareIndia)](https://schoolsoftwareindia.com/pricing).

---

## 3. Trends & timing — are you early, on-time, or late?

| Trend | Type | Direction | Evidence |
|---|---|---|---|
| **AI + computational thinking mandatory Class 3+, AY 2026-27** | Regulatory | 🟢🟢 **strong tailwind** | [MoE announcement (aireadyschool)](https://aireadyschool.com/blog/indias-ai-curriculum-mandate-starts-2026-27-is-your-school-ready), [The Diplomat](https://thediplomat.com/2025/11/are-indian-classrooms-ready-for-the-ai-leap/) |
| **NEP 2020: FLN, mother-tongue/multilingual, tech-in-classroom** | Regulatory | 🟢 tailwind | [iDream / NEP FLN](https://www.idreameducation.org/blog/foundational-literacy-and-numeracy-under-nep-2020/), [LEAD NEP guide](https://leadschool.in/school-owner/national-education-policy-nep-2020/) |
| **70% teachers already use AI; 60% for lesson planning** | Behavioral | 🟢 tailwind (demand) / 🔴 headwind (they use *free*) | [The Diplomat](https://thediplomat.com/2025/11/are-indian-classrooms-ready-for-the-ai-leap/) |
| **Only 15% teachers "AI-fluent"; 8M need training** | Demographic | 🟢 tailwind (need for a guided tool) | same |
| **Private enrollment rising, govt falling (~86L shift 23-24→25-26)** | Demographic | 🟢 tailwind for private-B2B | [MoE/UDISE+ (ThePrint)](https://theprint.in/india/enrolment-in-govt-schools-fell-by-nearly-86-lakh-between-2023-24-and-2025-26-moe-report/2980332/) |
| **DPDP Act: verifiable parental consent for <18, no profiling; ₹200 Cr penalty** | Regulatory | 🟡 headwind (cost) / 🟢 moat (B2B processor exemption) | [DPDP edtech compliance (K&K)](https://ksandk.com/data-protection-and-data-privacy/dpdp-act-compliance-for-edtech-schools/), [ORF](https://www.orfonline.org/english/expert-speak/dpdp-rules-and-the-future-of-child-data-safety) |
| **Post-BYJU's: FOMO → "fear of getting scammed"; real K-12 online ~$2–3B** | Market | 🔴 headwind | [RAYSolute Indian EdTech 2026](https://www.raysolute.com/indian-edtech-analysis-2026.html), [MarketsandMarkets](https://www.marketsandmarkets.com/blog/ICT/India-EdTech-Market) |

> **Adversarial (early vs late):** Bigger risk is **"free-AI-good-enough"** (you're late to the
> capability, early to the *packaged product*), not being too early on adoption — adoption is proven.
> Timing verdict: **on-time-to-slightly-late on tech, on-time on regulation.** Move fast on the
> defensible layer (vernacular + syllabus + compliance + workflow), not on "AI in schools" broadly.

---

## 4. Buyer landscape

| | Private school | Govt school |
|---|---|---|
| Holds budget | Principal / owner / trust | State edu dept / district (block) |
| Influences | Senior teachers, parents | Teachers, Block Education Officer |
| Blocks / slows | Price sensitivity, trust (post-BYJU's) | **Tenders, empanelment, approval chains** |
| Pre-seed winnable? | **Yes — founder-led sales** | **No (near-term)** — needs channel/empanelment |

Target the **private-school principal/owner** as economic buyer; **teacher as champion** (they already
want AI). Govt = later, via state AI-curriculum mandates as the wedge.

---

## 5. The adversarial pass (pre-mortem)

*"It's 18 months out and it failed. Why?"* — ranked:
1. **Free ChatGPT was good enough**; schools wouldn't pay for the tutor. *(Mitigation: lead with ERP
   revenue + compliance; tutor as free wedge.)*
2. **Couldn't reach schools cheaply**; founder-led sales didn't scale past ~50 schools. *(Test CAC in discovery.)*
3. **DPDP compliance cost/complexity** sank a lean team. *(Mitigation: strict Data-Processor posture, no child profiling.)*
4. **Govt pilots ate time**, produced no revenue. *(Mitigation: exclude govt from plan; opportunistic only.)*
5. **Incumbent (LEAD/Teachmint) bundled AI free** and out-distributed you. *(Watch quarterly.)*

**Failed comparable — BYJU's:** died from aggressive D2C sales, cash burn, trust collapse. Your B2B,
lean, compliance-first model avoids the D2C trust trap — **but inherits the sector's trust hangover.**
Sell proof and pilots, not hype.

---

## 6. Exit-criteria status (are you cleared to build?)

| Gate | Status | What's still needed |
|---|---|---|
| 1. Problem real & specific? | 🟡 **Likely yes** | Confirm teacher pain (hrs/wk) + principal willingness-to-pay in NCR interviews |
| 2. Solution addresses the *actual* problem? | 🟡 **Open** | Is the paid need the *tutor* or the *ERP*? Discovery decides |
| 3. Enough signal to build? | 🟡 **Not yet** | Need ~15-20 NCR private-school interviews (principal + teacher) |

**Do not write production code yet.** One round of NCR customer discovery (methodology Step 5) closes
gates 2 and 3. The market is real; the open question is **pricing power vs. free AI** and **tutor vs.
ERP as the revenue product.**

---

## 7. What to put in the investor deck (traceable claims only)
- ✅ AI mandatory Class 3+ from 2026-27 (MoE) — timing.
- ✅ 70% teacher AI adoption — demand proven.
- ✅ DPDP B2B-processor posture — compliance moat vs consumer AI.
- ✅ NCR serviceable ~13,000 private schools (🔴 confirm split in UDISE+ first).
- ⚠️ Use SAM ≈ $14M NCR ARR, not a $12B "India EdTech" vanity TAM — post-BYJU's investors punish inflated TAM.

---

## Appendix — sources
- UDISE+ dashboard (primary, verify counts): https://dashboard.udiseplus.gov.in/
- Economic Survey 2024-25 (24.8 cr students / 14.72 L schools): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097864&reg=3&lang=2
- Delhi schools: https://grokipedia.com/page/List_of_schools_in_Delhi · https://delhiplanning.delhi.gov.in/sites/default/files/Planning/15._education.pdf
- Haryana schools: https://www.mahadevmaitri.org/education/haryana
- India EdTech size / post-BYJU's: https://www.raysolute.com/indian-edtech-analysis-2026.html · https://www.marketsandmarkets.com/blog/ICT/India-EdTech-Market
- Govt→private enrollment shift: https://theprint.in/india/enrolment-in-govt-schools-fell-by-nearly-86-lakh-between-2023-24-and-2025-26-moe-report/2980332/
- Teachmint: https://inc42.com/buzz/teachmint-cuts-fy24-loss-to-inr-110-cr-revenue-soars-111/ · https://tracxn.com/d/companies/teachmint/__2OhzJsaQqn1Rx--LmV-MYhMY7hVCfzgx9GyitF_ntU8
- LEAD School: https://digitallearning.eletsonline.com/2024/08/lead-groups-fy24-revenue-reaches-%E2%82%B9370-cr-slashes-cash-burn-by-65/
- ERP pricing: https://fedena.com/pricing-and-plans · https://schoolsoftwareindia.com/pricing
- AI in classrooms / mandate: https://thediplomat.com/2025/11/are-indian-classrooms-ready-for-the-ai-leap/ · https://aireadyschool.com/blog/indias-ai-curriculum-mandate-starts-2026-27-is-your-school-ready
- NEP 2020 FLN/tech: https://www.idreameducation.org/blog/foundational-literacy-and-numeracy-under-nep-2020/ · https://leadschool.in/school-owner/national-education-policy-nep-2020/
- DPDP & children's data: https://ksandk.com/data-protection-and-data-privacy/dpdp-act-compliance-for-edtech-schools/ · https://www.orfonline.org/english/expert-speak/dpdp-rules-and-the-future-of-child-data-safety
