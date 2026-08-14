---
title: "What Is a Burn Rate? — Definition, Formula, and Runway"
description: "A burn rate is how fast a company spends cash each month. Learn gross vs net burn, the runway formula, and why subscription revenue stability changes the math."
slug: "burn-rate"
date: "2026-07-27"
updated: "2026-07-27"
category: "Glossary"
author: "Clink Team"
readingMinutes: 10
---

## TL;DR

- Burn rate is the monthly speed at which a company consumes its cash reserves—gross burn is total cash outflow, net burn subtracts incoming revenue, and runway divides cash on hand by net burn to estimate how many months are left.
- For subscription businesses, net burn is not a fixed number: MRR moves with expansions, downgrades, and payment failures, so runway should be modeled on a range, not a single point.
- Gross burn answers the worst-case question (if all revenue stopped tomorrow), while net burn is the number founders and investors actually use to plan.
- Burn rate is a cash measure, not a profit measure—a profitable company can still burn cash during a growth phase.
- The single biggest cause of startup failure is running out of cash, cited by Stripe's resource pages at 38% of failures, which makes the burn-and-runway pair one of the few metrics a board meeting always revisits.

---

## What Is a Burn Rate? — A Working Definition

A burn rate is the rate at which a company spends its available cash reserves before reaching positive cash flow. The metric is typically expressed per month, and it answers a deceptively simple question: if nothing else changed, how long until the money runs out?

The term comes from venture-backed startup practice, where a company raises a finite pool of capital and then "burns" it to fund operations—salaries, rent, infrastructure, marketing—until revenue covers costs or the next round arrives. Investopedia, Carta, and Stripe all converge on the same core definition, which makes it one of the more stable terms in startup finance. The definition has stayed consistent for a reason: the underlying question it answers, *how much runway is left*, does not change with fashion.

What makes burn rate more interesting than its one-line definition is that it is really two numbers with very different uses. Gross burn is the total monthly cash outflow from operations, ignoring revenue entirely. Net burn subtracts whatever cash came in during the month, showing the actual rate at which the balance sheet shrinks. A pre-revenue startup has the same gross and net burn; a startup with meaningful monthly revenue can carry a large gross burn while a modest net burn—or even a positive one.

A concrete example makes the distinction immediate. Imagine a startup with $2.4M in the bank that spends $380K per month on payroll, cloud, and marketing while collecting $210K in monthly subscription revenue. Gross burn is $380K. Net burn is $170K. Runway at current spend is about fourteen months. The gross number is the one to watch if revenue collapses; the net number is the one the board uses when deciding whether to raise in Q3 or Q4.

---

## How to Calculate Burn Rate: Gross, Net, and a Worked Example

Calculating burn rate is arithmetic, but the accounting choices around it determine whether the number is useful. Gross burn equals total cash outflows in a period; net burn equals gross burn minus cash inflows in the same period. Both are typically annualized down to a monthly figure for planning.

Net burn rate = total monthly cash outflows − monthly revenue. Runway = cash balance ÷ net burn rate. These two formulas, reproduced consistently across Carta, Brex, and Mercury, are the entire toolkit most teams need—the skill is in choosing the right inputs rather than the math itself.

A worked example clarifies where teams go wrong. Consider a startup with $1.8M cash on hand. It pays $250K monthly across payroll, rent, and software, and collects $120K in recurring revenue with $20K in one-time services. Gross burn is $250K. Net burn is $250K − $120K = $130K. Runway is $1.8M ÷ $130K ≈ 13.8 months. If a $40K annual contract pays upfront in January, that month's net burn drops to $90K and runway appears to stretch to 20 months—an illusion that corrects itself by March when the same revenue must be spread across the year.

Three input rules keep the calculation honest. First, use cash-basis numbers, not accrual accounting: a recognized but unpaid invoice is not cash in the bank. Second, exclude one-time infusions like a new round or a grant from monthly revenue; they distort net burn precisely when the board needs a clean trend. Third, average at least three months when revenue is lumpy, because a single month of prepaid annual contracts will otherwise make the runway number look far healthier than it is.

---

## Burn Rate vs Runway vs Net Loss: Reading the Difference

Three numbers get conflated in board decks, and the conflation produces bad decisions. Burn rate is a speed, runway is a duration, and net loss is an accounting construct—they measure different things even though they move together.

Runway converts burn into a deadline: cash on hand divided by monthly net burn. It is the number that forces prioritization because it is expressed in months rather than dollars. A common benchmark in venture practice is to raise before runway drops below eighteen to twenty-four months, because a raise takes three to six months of diligence and the next eight to twelve months of that runway are needed to demonstrate the milestones the round prices. Runway is only as reliable as the burn number feeding it, which is why the same teams that recompute burn monthly often discover their runway was overstated by revenue lumpiness.

Net loss is a GAAP concept that mixes in non-cash items—depreciation, stock-based compensation, amortization—that do not touch the bank account. A company can report a large net loss while burning little cash, or show a paper profit while cash drains. Burn rate is deliberately cruder: it tracks the actual cash position, which is why investors treat it as the survival metric rather than the elegance metric.

The practical decision rule is to track all three but act on one. Watch gross burn to understand the fixed cost base and what a revenue shock would do. Watch net burn to set the raise calendar. Watch net loss only to reconcile with cash at board level, never to decide whether the company can make it to the next milestone.

---

## Why Burn Rate Matters More for Subscription Businesses

Subscription businesses read burn differently from one-off sellers, because their revenue has a structure: recurring, contracted, and—critically—only as stable as the payment infrastructure that collects it. For a SaaS company, monthly revenue is not a smooth input; it is the sum of renewals, expansions, downgrades, and churn, and each component moves on its own clock.

This is where burn analysis for SaaS diverges from the textbook version. The textbook treats revenue as a given and burn as the variable to manage. In subscriptions, the more dangerous variable is revenue stability. A cohort that fails to renew, a round of downgrades, or a spike in failed renewals all flow directly into net burn without a single cost change. The classic framing—"we spend less than we earn"—misses the second question: *will we earn it again next month?*

The failure mechanism is often invisible until it is large. Card expiry, insufficient funds, and soft declines produce failed payment attempts that, without retry logic, convert directly into involuntary churn—customers who did not choose to leave but stop paying anyway. Industry estimates commonly place payment-related loss at a material share of total SaaS churn, often cited in a 20–40% band depending on cohort and methodology. When that loss hits a startup near the end of its runway, the math is brutal: a 3% monthly revenue leak is not a rounding error, it is roughly a third of annual revenue walking out the door.

For subscription teams, the honest version of runway modeling looks like a range. Model one scenario where net burn holds at current levels, one where MRR grows at plan, and one where involuntary churn rises because renewal failures go unaddressed. The spread between those scenarios is the real risk the board should discuss—not the single number that fits on one slide.

---

## Common Misconceptions About Burn Rate

**"A profitable company has no burn rate."** Profit and cash are different ledgers. A company can be profitable on paper while its cash balance declines because receivables grow faster than collections, or because it is reinvesting cash into expansion ahead of revenue. Burn rate describes the cash trajectory, and profitable companies burn cash all the time.

**"Reducing burn means cutting headcount."** Cutting headcount is the bluntest instrument, but burn is a ratio of outflows and inflows. The same net burn reduction can come from improving collections, raising prices without losing customers, or reducing failed-renewal loss—changes that preserve the team while fixing the leak.

**"Runway = cash ÷ gross burn is the number to report."** Using gross burn instead of net burn understates runway, sometimes by half. The convention across Carta, Stripe, and Brex is net burn for planning and gross burn for stress-testing the worst case. Mixing the two is how a startup discovers, mid-raise, that its deck overstated runway by a quarter.

**"A high burn rate is always bad."** A high burn is a symptom, not a verdict. If spend is converting into product, distribution, or data that compounds, investors fund it deliberately. The problem is high burn without a clear conversion story—the cash goes out and the unit economics do not improve.

---

## How Burn Rate Connects to Payment Infrastructure

For founders and finance teams running subscription models, the burn conversation increasingly ends in the same place: revenue quality. Every percentage point of recurring revenue that fails to collect reliably is a permanent reduction in the monthly inflow side of the net burn equation, and it compounds across every future month of runway.

This is the angle that product-focused reading of burn rate tends to miss. When teams fix the inflow side—recovering failed renewals before they become involuntary churn, retrying soft declines on a second path, keeping cards on file current—they change net burn without a single cost cut. Payment infrastructure choices therefore show up in runway math, not just in acceptance rates. The full mechanics of multi-path retry and how teams typically frame the revenue recovery band (often cited in a low-single-digit range, always contingent on mix) are covered in Clink's [smart routing article](/blog/smart-routing); this glossary entry only needs the causal chain: failed collection → lower MRR → higher net burn → shorter runway.

Teams evaluating infrastructure that unifies billing and payment routing—like Clink, which connects multiple processors under one subscription layer—should ask a runway-focused question rather than a features question: what happens to net burn when renewal collection improves? Because subscription data and processor connections are separable in that model, the same retry policies apply across markets, which is a governance question finance teams can actually audit. Clink does not publish a public rate card as of June 2026; packaging is discussed through [Contact Sales](https://clinkbill.com/contact). For the broader framework on who owns the payment relationship, see [MoR vs PSP](/blog/mor-vs-psp).

---

## Conclusion

Burn rate is the simplest survival metric in startup finance and the easiest to misread. Gross burn shows how fast the fixed cost base consumes cash; net burn shows the real depletion after revenue; runway turns both into a deadline the board can act on. For subscription businesses, the twist is that the revenue side is not static—it moves with renewals, expansions, downgrades, and failed collections—so the most useful burn model is a range, not a point.

The operational insight follows directly: improving collection reliability improves net burn without a single layoff or budget cut. Teams that model runway on realistic revenue scenarios, track gross and net burn separately, and treat failed renewals as a revenue-leak problem rather than a customer-acceptance problem will find the metric becomes a planning tool instead of a quarterly surprise. Start with the cash position, the three-month outflow trend, and the honest renewal number—everything else in the burn conversation builds from there.

---

## FAQ

**What is a good burn rate for a startup?**

There is no universal good number—the right burn rate is one that converts cash into durable growth and preserves at least eighteen to twenty-four months of runway through the next raise, which is the benchmark most venture teams plan against. A high burn is acceptable when it demonstrably accelerates product, distribution, or data advantages; the red flag is high burn without improving unit economics.

**What is the difference between gross burn and net burn?**

Gross burn is total monthly cash outflow from operations, ignoring revenue, and it answers the worst-case question of how fast the company would drain cash if revenue stopped. Net burn subtracts incoming revenue and shows the actual rate the balance shrinks, which is the number used to calculate runway and set the raise calendar.

**Can a profitable company still have a burn rate?**

Yes—profit and cash are different ledgers. A company can report a profit while its cash balance declines because receivables outpace collections, or while it reinvests cash into expansion ahead of revenue; burn rate tracks the cash trajectory, not the accounting result.

**Does burn rate include one-time expenses like hardware or legal fees?**

It should, when they are cash outflows in the period—burn is a cash-basis measure, so any cash leaving the account counts. The nuance is in the revenue side: one-time infusions like a funding round or grant should be excluded from monthly revenue, otherwise they inflate net burn's mirror image and distort the runway trend.

**How often should a company recalculate its burn rate?**

Monthly, at minimum, and whenever a material event changes the picture—a funding round, a large annual contract, a round of downgrades, or a change in renewal performance. The runway number decays with every month of operations, and the teams that recompute on the same cadence as their cash statements are the ones whose board decks hold up under diligence.

**Why does burn rate matter more for subscription businesses?**

Because the revenue side is not static—MRR moves with renewals, expansions, downgrades, and failed collections, so net burn changes even when costs stay flat. A spike in failed renewals converts directly into involuntary churn and shorter runway, which is why subscription teams should model burn and runway as a range across revenue scenarios rather than a single point.
