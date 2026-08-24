---
title: "What Is a Stripe Dispute — How Chargebacks and Payment Disputes Work"
description: "What is a Stripe dispute? Learn chargeback vs inquiry terminology, money flow, Dashboard deadlines, reason codes, VAMP thresholds, and what merchants control."
slug: "what-is-stripe-dispute"
date: "2026-09-04"
updated: "2026-09-04"
category: "Stripe Risk"
secondaryCategory: "Guide"
author: "Clink Team"
readingMinutes: 13
---

## TL;DR

- A **Stripe dispute** is Stripe's merchant-facing record of a cardholder contesting a payment through their bank — the same event card networks call a **chargeback** — which triggers an immediate debit of the disputed amount plus a dispute fee from your Stripe balance, a response deadline (typically **7–21 days** per Stripe's documentation), and a lifecycle you manage in the Dashboard or Disputes API while the issuer decides the outcome.
- **Inquiries** (also called retrievals or requests for information) are a pre-dispute phase on some networks where the issuer asks for clarification before pulling funds; Stripe labels these with `warning_*` statuses in the API, and ignoring them can escalate to formal, harder-to-win chargebacks.
- Money flow is one-directional at opening: the network debits Stripe, Stripe debits you, funds stay withheld until the dispute resolves as **won** (funds return) or **lost** (permanent); you cannot issue a normal refund on an open dispute.
- Common reason-code categories include **fraudulent**, **product not received**, **subscription canceled**, **credit not processed**, and **duplicate** — each expects different evidence; Stripe organizes hundreds of network codes into eight categories in its [dispute categories guide](https://docs.stripe.com/disputes/categories).
- Elevated dispute and fraud rates feed card-network monitoring programs — Visa's **VAMP** program, as documented by Stripe, uses a **0.5% non-compliant** ratio threshold and **1.5% excessive** threshold in most regions — and sustained non-compliance can escalate toward account restrictions documented in [Stripe Account Suspended](/blog/stripe-account-suspended) and [Why Stripe Closes Accounts](/blog/why-stripe-closes-accounts).

---

## What a Stripe Dispute Is — Feature, Not Just a Customer Complaint

A Stripe dispute is how Stripe surfaces a cardholder's bank contesting one of your payments — a workflow you operate through the [Disputes section](https://dashboard.stripe.com/disputes) of the Dashboard, webhooks, email alerts, and the [Disputes API](https://docs.stripe.com/api/disputes). It is not a Stripe Support ticket, a customer email, or a refund request you initiate. When a dispute opens, Stripe has already been debited by the card network and has already debited your balance; your job is to accept the loss or submit evidence before a network-specific deadline.

Stripe remains the default processor for a large share of SaaS and indie businesses because its APIs, Radar fraud tools, and documentation are excellent — and disputes are the price of that scale. Card networks require issuers to offer dispute rights to cardholders; issuers create formal disputes on the network; networks immediately reverse the payment and pull dispute fees from the acquirer chain. Stripe sits in that chain as your aggregator and passes the financial impact to you while providing the interface to respond.

This article is the canonical explainer for what disputes are as a Stripe feature: terminology, money movement, Dashboard lifecycle, reason codes, and account-risk impact. It does not walk customers through disputing a charge on their statement — that belongs in [How to Dispute a Stripe Charge](/blog/how-to-dispute-stripe-charge) — and it does not deep-dive prevention tactics covered in [Stripe Chargeback Prevention](/blog/stripe-chargeback-prevention).

---

## Dispute vs Chargeback vs Inquiry — Terminology Merchants Confuse

Merchants use "chargeback," "dispute," and "payment dispute" interchangeably in conversation — and for card payments, that overlap is mostly correct. Stripe's [disputes overview](https://docs.stripe.com/disputes) states explicitly that a dispute is also known as a chargeback: the issuer creates a formal dispute on the card network, which immediately reverses the payment. Stripe's monitoring-program documentation treats the terms as interchangeable for program purposes.

The terminology splits when you move earlier or later in the lifecycle. **Inquiries** — Stripe's label for pre-dispute requests from issuers, sometimes called retrievals or requests for information — are not yet chargebacks. American Express and Discover use this phase frequently; Mastercard and Visa largely skip it for most merchants, though Mexico domestic disputes across card brands may still pass through inquiry first. During inquiry, the issuer asks for transaction clarification — often because the cardholder does not recognize the statement descriptor — before formally debiting funds. Stripe represents inquiries in the API with statuses prefixed by `warning`, such as `warning_needs_response` versus `needs_response` for a full chargeback.

Three practical distinctions matter for operators. First, inquiries may resolve without a dispute fee if you provide satisfactory evidence or issue a full refund before escalation — but partial refunds do not prevent escalation. Second, failing to respond to an inquiry can signal implicit acceptance and produce an **unwinnable chargeback**, per Stripe's inquiry documentation. Third, inquiries that close without escalation after 120 days do not produce a explicit "win" message from the network; Stripe marks them `warning_closed`.

**Early fraud warnings (EFWs)** are a separate signal entirely — informational messages from Visa TC40 and Mastercard SAFE reports flagging suspected fraud. They are not disputes, do not debit your balance, and do not appear in dispute-rate calculations the same way in your Dashboard — but Visa's VAMP program counts EFWs toward fraud metrics alongside TC15 disputes. Treat EFWs as upstream risk signals, not as disputes you can "win" or "lose."

---

## How Money Moves When a Dispute Opens

Understanding dispute money flow prevents the most expensive operational mistakes — especially attempting refunds on open disputes or assuming withheld funds will return quickly.

When a cardholder's bank files a formal dispute, the sequence documented in Stripe's [how disputes work](https://docs.stripe.com/disputes/how-disputes-work) guide runs as follows:

1. **Network debits Stripe** for the disputed payment amount and associated network dispute fees.
2. **Stripe debits your Stripe balance** for the disputed amount plus Stripe's dispute fee (pricing varies by country; see Stripe's [dispute fee documentation](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes)).
3. **Funds remain withheld** for the entire dispute duration — you cannot recover them by refunding outside the dispute workflow while the case is open.
4. **Your dispute rate** with that card network increases for monitoring-program calculations, regardless of eventual outcome.

The disputed amount is not always identical to the original charge. Currency conversion timing, partial disputes, recurring billing consolidated into one dispute, and partially refunded charges can all produce amounts that differ from the original PaymentIntent total — Stripe documents each scenario in its disputed-amount table.

If you **accept** the dispute in the Dashboard or API, you concede the loss; funds do not return. If you **counter** with evidence and **win**, the issuer returns the chargeback amount to Stripe, which passes it back to you — though dispute received fees are generally non-refundable outside specific regions such as Mexico. If you **lose**, the outcome is final from Stripe's perspective; the issuer credits the cardholder, and Stripe has already settled the network side.

The full lifecycle from initiation to final decision typically takes **two to three months**, per Stripe — you cannot reliably accelerate issuer review except by accepting the dispute. Issuer evaluation after evidence submission usually runs **60–75 days**, depending on the network.

---

## The Stripe Dashboard Dispute Lifecycle and Deadlines

Stripe's Dashboard and API mirror the card-network dispute state machine — but Stripe does not decide outcomes. Stripe notifies you, holds funds, accepts your evidence, and forwards it; the issuer and network rules govern deadlines and results.

### Status progression

For formal chargebacks, the Dispute object `status` field moves through stages such as:

| Status | Meaning |
| --- | --- |
| `needs_response` | Chargeback opened; evidence not yet submitted |
| `under_review` | Evidence submitted; awaiting issuer decision |
| `won` | Issuer overturned the dispute in your favor |
| `lost` | Issuer upheld the cardholder's claim — generally final |

Inquiry-phase statuses use the `warning_` prefix: `warning_needs_response`, `warning_under_review`, and `warning_closed`.

Stripe surfaces active disputes under the **Needs Response** tab in the Dashboard. Each dispute shows the reason category, network reason code, cardholder claim text, and — critically — **`evidence_details.due_by`**, the timestamp by which you must submit evidence or automatically lose.

### Response deadlines

After a chargeback is created, Stripe documents that you typically have **7–21 days** to respond, depending on the card network. This window is not uniform: American Express, domestic Mexico disputes, and certain local payment methods follow different calendars. **Always use the deadline shown on the specific dispute** in your Dashboard or API — not a rule-of-thumb from a blog post.

Missing the deadline means automatic loss. Stripe's [responding to disputes](https://docs.stripe.com/disputes/responding) guide states that if you do not respond before the deadline, you automatically lose and cannot retrieve the disputed funds.

If an inquiry escalates to a chargeback, you must submit a **separate response** for the formal dispute — inquiry evidence does not carry over automatically.

### Cardholder dispute initiation window

Card networks typically allow cardholders to initiate disputes within **120 days** of the original payment, with extensions for travel, events, and future-dated services where the dispute window may start on the service date rather than the payment date. SaaS merchants with annual prepay or long fulfillment lags should internalize that disputes can arrive months after the charge — long after the customer stopped using the product.

---

## Common Dispute Reason Codes and What They Mean

Card networks assign granular reason codes; Stripe groups them into eight categories to simplify evidence requirements. The category appears on the dispute in your Dashboard and on the `network_reason_code` field of the Dispute object. Stripe's [reason code categories](https://docs.stripe.com/disputes/categories) page maps Visa, Mastercard, and American Express codes to these buckets.

The categories SaaS and subscription merchants encounter most often:

| Stripe category | Typical cardholder claim | Evidence Stripe expects |
| --- | --- | --- |
| **Fraudulent** | "I did not authorize this charge" | Proof of cardholder participation — login logs, IP/device match, 3D Secure authentication data, delivery to billing address |
| **Product not received** | "I paid but never got the service" | Access logs, usage data, download timestamps, shipping tracking |
| **Subscription canceled** | "I canceled but was still charged" | Cancellation policy, cancellation timestamp, renewal terms shown at checkout |
| **Credit not processed** | "I returned it / was promised a refund" | Refund policy, refund attempt records, communication with customer |
| **Product unacceptable** | "Not as described" or defective | Product description accuracy, terms accepted, support correspondence |
| **Duplicate** | "Charged twice" | Separate authorization records showing distinct transactions |
| **Unrecognized** | "I don't know this charge" | Clear statement descriptor, receipt, customer communication |

Fraudulent disputes are the largest category for many online businesses — and the category where **3D Secure liability shift** can change outcomes. When authentication qualifies for liability shift, Stripe may automatically attach some evidence, but a dispute can still arrive.

Subscription businesses disproportionately see **subscription canceled** and **fraudulent** codes driven by trial confusion, unclear descriptors, and cancellation friction — operational patterns that show up in dispute text long before they show up in product analytics.

---

## How Dispute Rates Affect Stripe Account Risk

Individual disputes are operational events; **dispute rate** is a portfolio metric that card networks, acquirers, and Stripe watch continuously. Monitoring programs do not wait for dispute outcomes — they count disputes when funds move out, because networks prioritize prevention over win rates, as Stripe's [monitoring programs guide](https://docs.stripe.com/disputes/monitoring-programs) explains.

### Visa VAMP thresholds (official via Stripe)

Visa's **VAMP** (Visa Acquirer Monitoring Program) combines TC15 disputes and TC40 early fraud warnings into monthly ratios. Stripe publishes Visa's thresholds as of 2026:

| Criteria | Non-compliant | Excessive |
| --- | --- | --- |
| VAMP ratio | **0.5%** | **1.5%** in AP, Canada, EU, US, LAC; **2.2%** in CEMEA |
| VAMP count | **5** | **1,500** elsewhere; **150** in CEMEA (with volume floors) |

Visa calculates the VAMP ratio as disputed-and-fraud count divided by total captured payments in the same calendar month. EFWs count toward fraud even when they never become chargebacks — a common surprise for merchants who monitor only the Disputes tab.

Stripe provides a [VAMP dashboard](https://dashboard.stripe.com/radar/cbmp/vamp) under Radar showing program standing, daily ratio trends, and descriptor-level breakdowns. Visa's official data arrives with roughly a one-month delay; Stripe's estimates help you monitor in real time but may differ from Visa's final numbers.

### Why merchants see action below 1.5%

Visa's **1.5% excessive** threshold is the network's merchant line — not necessarily the line your acquirer enforces internally. Acquirers face portfolio-level VAMP limits documented by Stripe at **0.5% non-compliant** and tighter excessive bands, which creates pressure to restrict merchants well before they hit Visa's published excessive ratio. **Merchant reports** — on forums, Trustpilot, and founder communities as of 2026 — frequently describe Stripe payout holds or account reviews at dispute rates near **0.5–1.0%**, below Visa's 1.5% excessive merchant threshold but above acquirer comfort zones. Treat those accounts as qualitative pattern data, not as guaranteed Stripe policy.

Stripe's monitoring documentation warns that failure to comply with program remediation within specified periods can put **the ability to accept card payments at risk** — language on the same causal chain as the restrictions described in [Why Stripe Closes Accounts](/blog/why-stripe-closes-accounts). Sustained non-compliance escalates toward reserves, payout pauses, and closure under the Unacceptable Risk Policy covered in [Stripe Account Suspended](/blog/stripe-account-suspended).

Mastercard operates parallel programs with different calendar mechanics — disputes assigned to the month received but compared against **prior-month** sales volume — so a merchant can appear healthy on Visa VAMP while simultaneously breaching Mastercard thresholds.

---

## Stripe's Dispute Tools vs the Card-Network Chargeback Process

Stripe is the interface layer; the card network and issuer run the underlying chargeback process. Keeping that boundary clear prevents misplaced expectations about Stripe Support's authority.

**What Stripe provides:**

- Dashboard and API for viewing disputes, uploading evidence, and accepting or countering
- Webhooks (`charge.dispute.created`, `charge.dispute.updated`, `charge.dispute.closed`) for automation
- Reason-code categorization and evidence field guidance per category
- [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes) for eligible automated evidence collection
- Radar [early fraud warnings](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings) and optional [dispute prevention](https://docs.stripe.com/disputes/prevention-preview) integrations
- Communication relay to the network — Stripe "facilitates your case, but doesn't have influence over the outcome, which is at the sole discretion of the account owner's bank," per Stripe's documentation

**What Stripe does not control:**

- Issuer decision quality or speed
- Network arbitration escalation — Stripe does not support the arbitration phase
- Reason-code assignment by the issuer
- Whether a cardholder withdraws a dispute (you must still submit evidence even if the customer claims they withdrew)
- Monitoring-program enrollment thresholds set by Visa and Mastercard

Some disputes are **unchallengeable** under network rules — Stripe may close them as `lost` immediately with no evidence window. Discover inquiries that escalate without response, certain Cartes Bancaires disputes in SEPA, and Nigeria local-regulation disputes fall into this bucket.

The Disputes API and Dashboard are operationally equivalent for response purposes — choose based on your workflow. Programmatic teams often use the [Files API](https://docs.stripe.com/api/files/create) plus [Dispute update](https://docs.stripe.com/api/disputes/update) to attach evidence at scale; smaller merchants typically use the Dashboard counter-dispute flow.

---

## What Merchants Can and Cannot Control

Disputes feel arbitrary when a customer bypasses support and goes straight to their bank. Separating controllable levers from fixed network rules helps you allocate effort.

**Merchants can control:**

- **Evidence quality and timeliness** — submitting complete, category-appropriate documentation before `evidence_details.due_by`
- **Inquiry response speed** — resolving confusion before formal chargeback and fee assessment
- **Statement descriptors and checkout transparency** — reducing "unrecognized" and subscription confusion disputes
- **Refund timing** — issuing refunds before disputes when customer service identifies legitimate complaints (refunds after dispute opening follow the dispute workflow, not a normal refund path)
- **EFW response strategy** — proactive refunds on selected EFWs where the charge amount is near your dispute fee, per Stripe's analysis (with exceptions when account-level risk warrants more aggressive refunding)
- **Dispute rate over time** — through product, billing, and fraud-prevention practices detailed in the prevention article, not through arguing with network math after enrollment
- **Accept vs counter decision** — accepting saves counter-effort on unwinnable cases; countering is appropriate when you have strong proof

**Merchants cannot control:**

- Issuer interpretation of evidence
- Dispute deadlines set by network and issuer rules
- Automatic debit of disputed funds and fees at opening
- Inclusion in monitoring programs based on count and ratio thresholds
- Whether Stripe Support overrides a lost dispute outcome
- Cardholder behavior — disputing instead of contacting merchant support
- Network counting disputes regardless of eventual win/loss

One non-obvious constraint: while a dispute is open, you **cannot issue a refund outside the dispute process**. Attempting to treat it like a normal charge refund will fail or create reconciliation confusion. Use accept or counter within the dispute workflow.

---

## Early Fraud Warnings vs Disputes

Early fraud warnings are the most misunderstood signal in Stripe's dispute ecosystem because they arrive without debiting your balance and without creating a Disputes tab entry — yet they still affect Visa VAMP fraud counts.

EFWs originate from issuer fraud reports on Visa (TC40), Mastercard (SAFE), and JCB networks. Stripe surfaces them via Radar and the [Early Fraud Warnings API](https://docs.stripe.com/api/radar/early_fraud_warnings). They flag payments issuers suspect might be fraudulent; they do **not** require action.

Stripe's documentation notes that **80% of EFWs convert into fraud disputes if you do nothing** — unless the payment qualified for 3D Secure liability shift, in which case Stripe may auto-supply some evidence but a dispute can still arrive. Proactively refunding an EFW does not remove the fraud warning from network reporting; only a reversal within roughly two hours of capture can prevent the fraud report in some cases.

Stripe's suggested refund strategy for EFWs: refund charges roughly **less than or equal to your dispute fee** is often optimal — refunding every EFW is too aggressive and refunds high-value charges that might never dispute. The exception is when account-level risk — monitoring program proximity, prior restrictions — makes preventing any downstream dispute worth the refund cost. That tradeoff connects directly to the escalation paths in [Why Stripe Closes Accounts](/blog/why-stripe-closes-accounts).

EFWs and disputes use separate network systems that are not always synchronized — you can receive an EFW after already receiving a fraud dispute on the same charge. Treat them as correlated signals, not as duplicates to ignore.

---

## Conclusion

A Stripe dispute is the merchant-operable face of a card-network chargeback: funds leave your balance immediately, evidence deadlines are short and non-negotiable, and outcomes rest with issuers — not with Stripe Support advocacy. Inquiries and early fraud warnings sit upstream; reason-code categories determine what proof matters; and monthly dispute-and-fraud ratios feed Visa VAMP and parallel Mastercard programs that can escalate toward the account restrictions documented in this cluster.

Stripe's dispute tooling — Dashboard workflows, webhooks, Smart Disputes, and Radar signals — is among the best in the aggregator category, which is why so many SaaS teams depend on it for subscription revenue. That same dependency makes dispute rate a portfolio risk metric, not a support inconvenience. For customer-side dispute mechanics, see [How to Dispute a Stripe Charge](/blog/how-to-dispute-stripe-charge); for operational prevention, see [Stripe Chargeback Prevention](/blog/stripe-chargeback-prevention).

If dispute volume is already driving processor risk conversations, the architectural lesson is continuity: merchants who route all revenue through one Stripe account inherit a single point of failure for both cash flow and escalation. Payment orchestration across linked PSPs — with portable billing data — does not prevent disputes on Stripe charges, but it reduces the business impact when dispute rates trigger restrictions. Teams evaluating that setup can review [Smart Routing](/blog/smart-routing) or Contact Sales at [clinkbill.com](https://clinkbill.com/).

---

## FAQ

### What is a Stripe dispute in simple terms?

A Stripe dispute is a record that a cardholder's bank contested one of your charges — the same event called a chargeback on card networks — which causes Stripe to debit the disputed amount plus a fee from your balance and opens a window for you to accept the loss or submit evidence before an issuer-set deadline.

### Is a Stripe dispute the same as a chargeback?

For card payments, yes — Stripe uses "dispute" and "chargeback" interchangeably in its documentation. The distinction matters for **inquiries** (pre-dispute information requests with `warning_*` statuses) and **early fraud warnings** (fraud signals that are not yet disputes), which precede or parallel formal chargebacks.

### How long do I have to respond to a Stripe dispute?

Stripe documents **7–21 days** from chargeback creation for most card networks, but the exact deadline varies by network and case. Check `evidence_details.due_by` on the specific dispute in your Dashboard or API — missing that timestamp means automatic loss regardless of evidence quality.

### Does winning a dispute remove it from my dispute rate?

No for card-network monitoring programs. Stripe's monitoring documentation states that programs count disputes when funds move out, not based on eventual win/loss, because waiting for outcomes would delay ratio calculations by months. Prevention and pre-dispute resolution matter more than win rate for program compliance.

### What is the difference between an early fraud warning and a dispute?

An early fraud warning is an informational fraud signal from issuer network reports — it does not debit your balance or create a formal dispute record. Disputes are formal chargebacks that immediately withhold funds. EFWs still count toward Visa VAMP fraud metrics, and Stripe estimates roughly 80% convert to fraud disputes if unaddressed.

### Can Stripe Support overturn a dispute I lost?

No. Stripe facilitates evidence submission but does not decide outcomes — issuers do. Stripe also does not support network arbitration escalation. If you believe the issuer erred, your options are limited to rare late-win corrections driven by issuer-side adjustments, or accepting the loss and focusing on prevention — not Support escalation to reverse a final `lost` status.
