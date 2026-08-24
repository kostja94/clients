---
title: "How to Dispute Stripe Charge — Cardholder Steps, Timelines, and What Happens Next"
description: "How to dispute stripe charge: identify descriptors, contact merchant vs bank, Reg E/Reg Z timelines, evidence checklist, and what happens after you file."
slug: "how-to-dispute-stripe-charge"
date: "2026-09-05"
updated: "2026-09-05"
category: "Stripe Risk"
secondaryCategory: "HowTo"
author: "Clink Team"
readingMinutes: 13
---

## TL;DR

- To **dispute a Stripe charge**, contact your **card issuer or bank** — not Stripe directly. Stripe is the payment processor for the merchant; only your issuing bank can initiate a formal chargeback or billing-error claim under card-network and consumer-protection rules.
- Start by identifying the charge on your statement using the merchant's **statement descriptor** (often a recognizable business name, sometimes with a `*` prefix and transaction suffix), then contact the merchant for refunds or cancellations before escalating — unless the charge is clearly unauthorized or the merchant is unreachable.
- **US credit cards** fall under Regulation Z (Fair Credit Billing Act): you generally have **60 days** from the statement date to report a billing error; the issuer must acknowledge within **30 days** and resolve within **two billing cycles or 90 days**. **US debit cards** fall under Regulation E: the same **60-day** window applies for errors on statements, with investigation typically starting within **10 business days**.
- **UK chargebacks** are governed by card-scheme rules (Visa, Mastercard), not statute — consumers typically have around **120 days** to raise a claim, with extensions up to **540 days** in some future-delivery cases per scheme rules cited by the <a href="https://www.financial-ombudsman.org.uk/consumers/complaints-can-help/credit-borrowing-money/goods-services-bought-credit" rel="nofollow noopener">Financial Ombudsman Service</a>.
- After you file, your bank may issue **provisional credit** while investigating; the merchant receives a dispute notification through Stripe, funds are debited from their account, and the full lifecycle from filing to final decision commonly takes **two to three months** per <a href="https://docs.stripe.com/disputes/how-disputes-work" rel="nofollow noopener">Stripe's dispute documentation</a>.

---

## When to Contact the Merchant First — and When to Go Straight to Your Bank

If you searched **how to dispute stripe charge**, you probably see an unfamiliar line item, a duplicate subscription renewal, or a charge from a business you thought you canceled. The first decision is not which form to fill out — it is whether the problem is a billing mistake the merchant can fix in minutes or a formal dispute your bank must adjudicate.

Contact the merchant first when you recognize the business and the issue looks fixable: a subscription that renewed after cancellation, a refund that never posted, a duplicate charge, or damaged goods the seller can replace. Most merchants on Stripe can issue refunds from their Dashboard — faster for everyone and without dispute fees.

Go straight to your bank when the charge is clearly **unauthorized**, when you suspect **fraud**, when the merchant is unreachable, when they refused a legitimate refund, or when goods were never delivered. US consumer law does not require merchant contact before asserting a billing error on a credit card for undelivered goods — <a href="https://www.consumerfinance.gov/rules-policy/regulations/1026/13/" rel="nofollow noopener">Regulation Z official commentary</a> states that explicitly.

Stripe is the merchant's processor, not your bank. When a cardholder questions a payment with their issuer, the issuer creates a formal dispute on the card network, which reverses the payment and notifies Stripe. Stripe does not decide outcomes — the issuer does. Cardholders cannot dispute through Stripe the way merchants respond in the Stripe Dashboard.

---

## How to Identify a Stripe-Processed Charge on Your Statement

Stripe-processed charges rarely appear as the word "Stripe" on your bank statement. Instead, you see a **statement descriptor** — the text the merchant configured when they set up payments. Stripe's <a href="https://docs.stripe.com/get-started/account/statement-descriptors" rel="nofollow noopener">statement descriptor documentation</a> explains that merchants set a static prefix (their recognizable business name) and, for card payments, may append a dynamic suffix after an asterisk and space — for example, `CREATIVE CANDLES* ORDER 123`. The full descriptor, including the separator, is limited to **22 characters** on card networks.

Several patterns cause confusion. **Platform charges** — purchases through Shopify, a SaaS billing portal, or a marketplace — may show the seller's descriptor, the platform name, or a shortened legal entity name that differs from the brand you know. **Soft descriptors** appear immediately after authorization as pending charges; **hard descriptors** replace them after settlement, sometimes with a different amount if the merchant placed a temporary hold (common in hotels and rentals). **Recurring subscriptions** typically show the same prefix each cycle, which helps you match a charge to a service you signed up for months ago.

Before calling your bank, gather what you can from the statement itself: the exact descriptor text, transaction date, amount, currency, and whether the charge is pending or posted. Search your email for receipts using the descriptor text, check subscription settings in apps you use, and look for confirmation emails from the merchant. If you still cannot identify the charge, your bank's dispute intake form will ask whether the transaction is **unrecognized** — a different reason code from **goods not received** or **canceled subscription**, and the evidence requirements differ. Merchants reading this section should note that unclear descriptors are a leading driver of "I don't recognize this charge" disputes; Stripe's own guidance ties clear descriptors to lower chargeback rates.

---

## Step-by-Step: Filing a Dispute Through Your Card Issuer

Formal disputes always route through your **issuing bank** — the financial institution that issued your credit or debit card — not through Stripe's website or support channels. The steps below reflect common issuer workflows; your bank's mobile app, online banking portal, or phone line may label the process "dispute," "chargeback," "billing error," or "report unauthorized transaction."

Start by logging into your bank's app or website and locating the specific transaction. Most issuers let you tap the charge and select **Dispute this charge** or **Report a problem**. If the charge is pending, some banks will ask you to wait until it posts; others accept provisional reports on pending authorizations for fraud cases. When the intake form asks for a reason, choose the category that matches your situation: unauthorized/fraud, duplicate charge, canceled subscription, goods or services not received, not as described, or credit not processed for a return.

Prepare a concise written statement — even if you start by phone, many issuers require written confirmation within a few days. Include the transaction date, amount, merchant descriptor, your account or order number if known, what you expected versus what happened, and dates of any merchant contact. Attach evidence: order confirmations, cancellation screenshots, email threads, tracking numbers, or photos of damaged goods. For unauthorized charges, note whether you still have your card, whether you shared card details with anyone, and whether you used the card on the disputed merchant's site.

Submit the dispute and save your case reference number. Your issuer forwards eligible claims to the card network (Visa, Mastercard, American Express, or Discover), which notifies the merchant's processor — in this case, often Stripe. Per Stripe's <a href="https://docs.stripe.com/disputes/how-disputes-work" rel="nofollow noopener">how disputes work guide</a>, the merchant then receives notification through the Stripe Dashboard, email, and webhooks; Stripe debits the disputed amount plus a dispute fee from the merchant's balance. You will not interact with Stripe during this process unless the merchant contacts you directly.

If your issuer denies the dispute at intake — for example, because you missed a deadline — ask whether **Section 75** (UK credit cards over £100) or other local consumer protections apply, and whether you can escalate internally before filing a regulatory complaint.

---

## Dispute Timelines: US Reg E, US Reg Z, and UK Chargeback Rules

Timelines differ by card type, country, and dispute reason. Treat the table below as a planning guide; your issuer applies the rules that govern your specific account.

| Framework | Applies to | Cardholder filing window | Issuer investigation timeline | Provisional credit |
| --- | --- | --- | --- | --- |
| **Regulation Z** (FCBA) | US credit cards | **60 days** from statement showing the error | Acknowledge within **30 days**; resolve within **2 billing cycles or 90 days** | Creditor may credit account during investigation per <a href="https://www.consumerfinance.gov/rules-policy/regulations/1026/13/" rel="nofollow noopener">12 CFR §1026.13</a> |
| **Regulation E** | US debit cards & EFTs | **60 days** from statement showing unauthorized/error | Investigate within **10 business days** (extensions to **45–90 days** in defined cases) | Required in many cases within **10 business days** if investigation extends per <a href="https://www.consumerfinance.gov/rules-policy/regulations/1005/11/" rel="nofollow noopener">12 CFR §1005.11</a> |
| **UK chargeback** (scheme rules) | UK debit & credit cards | Typically **~120 days** from transaction or expected delivery date | Varies by scheme and issuer; not statutory | At issuer discretion — chargeback is not a legal right |
| **Card network rules** | Most card disputes globally | Often **120 days** from payment; longer for future-delivery purchases | Merchant response **7–21 days**; issuer decision **60–75 days** per Stripe | Issuer may credit account while case is open |

**Regulation Z** implements the Fair Credit Billing Act for open-end credit. You must send a billing-error notice within **60 days after the creditor transmitted the first periodic statement** reflecting the alleged error. The creditor must mail written acknowledgment within **30 days** unless it completes resolution sooner, and must resolve within **two complete billing cycles but no later than 90 days**. During investigation, the creditor may not collect the disputed amount, report you as delinquent on that amount, or restrict your account because of the dispute — protections that do not apply if you dispute in bad faith.

**Regulation E** governs electronic fund transfers, including debit card transactions. For unauthorized transfers appearing on a periodic statement, you must report within **60 days** of the statement transmittal to limit liability on subsequent unauthorized transfers. The institution must investigate promptly — generally within **10 business days** — and report results within three business days after completing the investigation. If the institution needs more time, it may take up to **45 days** (or **90 days** for new accounts, point-of-sale debit transactions, or foreign-initiated transfers) but must provisionally recredit your account in many cases within **10 business days** while the investigation continues.

**UK chargebacks** operate differently. The <a href="https://www.fca.org.uk/publication/finalised-guidance/cancellations-refunds-helping-consumers-rights-routes-to-refunds.pdf" rel="nofollow noopener">FCA's chargeback guidance</a> notes that chargeback is **not a statutory right** — it is a voluntary scheme-administered process. Consumers normally have **120 days** from the expected delivery date for goods or services not provided. The Financial Ombudsman Service adds that time limits can extend up to **540 calendar days** from the original transaction in some future-delivery scenarios, depending on Visa or Mastercard rules. Credit card purchases over £100 may also qualify for **Section 75** of the Consumer Credit Act, a separate statutory protection from chargeback.

At the card-network level, Stripe documents that cardholders can typically initiate disputes within **120 days** of the original payment, with the window starting on the **event or delivery date** for future purchases like travel or tickets. After a chargeback is created, merchants usually have **7 to 21 days** to respond; issuers typically decide within **60 to 75 days**. The full lifecycle commonly spans **two to three months**.

---

## Evidence Customers Should Gather Before Filing

Strong evidence speeds issuer review and reduces back-and-forth. Organize documents before you call your bank — not after.

For **unrecognized charges**, provide proof you did not authorize the transaction. For **subscription disputes**, gather signup confirmation, cancellation screenshots with timestamps, and emails showing billing continued after cancellation. For **goods not received**, collect order confirmation, expected delivery date, and tracking (or proof none was provided). For **duplicate charges**, show two statement lines plus a single order confirmation. For **refund-not-received**, provide proof the merchant promised a refund and the date it should have posted.

Merchants should expect issuers to request this material. Stripe's dispute workflow asks for communication logs, delivery proof, and cancellation policies — so cardholders who request delivery status or refunds in writing before disputing create a fair paper trail for both sides.

---

## Subscription and Recurring Billing Disputes

Subscription charges generate a disproportionate share of payment disputes because renewal timing, free-trial conversions, and cancellation UX are easy to misunderstand. A charge that looks fraudulent to a cardholder is often a legally authorized renewal under terms the cardholder accepted at signup — which makes evidence and reason-code selection critical.

If you intended to cancel, dispute under **canceled recurring billing** or **credit not processed** rather than **fraud**, unless you genuinely believe someone else accessed your account. Fraud reason codes trigger stricter issuer review and can harm merchants disproportionately when the real issue is a missed cancellation click. Document the cancellation path you used: account settings URL, support ticket number, or chat timestamp. If the merchant shows that you did not complete cancellation — or that your plan was annual rather than monthly — the issuer may side with the merchant.

US and UK rules treat each renewal as a separate transaction for timing purposes. A subscription billed monthly creates a fresh dispute window with each charge, but waiting months before disputing the original signup rarely works if subsequent renewals were authorized. For free trials that converted to paid plans, gather the trial signup email showing when billing would begin and whether you received pre-charge notification as required by card-network rules and, in some jurisdictions, local consumer law.

Merchants processing subscriptions on Stripe should read this section as a map of customer frustration points. Unclear renewal emails, buried cancel links, and descriptor changes between trial and paid phases predict dispute volume. Prevention strategies — covered in [Stripe Chargeback Prevention](/blog/stripe-chargeback-prevention) — matter because once a cardholder files, the merchant's only lever is evidence submission through Stripe, not direct negotiation with the issuer.

---

## What Happens After You File: Provisional Credit and Merchant Notification

Once your issuer accepts the dispute, several parallel processes begin — and none of them involve Stripe communicating directly with you as the cardholder.

Your bank may issue **provisional credit** (sometimes called a temporary credit) while investigating. On US debit cards, Regulation E often requires this within 10 business days when investigation extends beyond the initial period. On credit cards, Regulation Z prohibits collection of the disputed amount during resolution. The credit may appear on your next statement; if the issuer ultimately rules against you, it can reverse the provisional credit and reapply the charge.

On the merchant side, Stripe notifies the business immediately. Stripe debits the disputed amount and a **dispute fee** from the merchant's Stripe balance, increases the merchant's dispute rate with that card network, and opens a response window — typically **7 to 21 days** depending on the network. The merchant submits evidence through the Stripe Dashboard or API; Stripe forwards it to the issuer but does not adjudicate. If the merchant misses the deadline, the dispute typically defaults in the cardholder's favor.

The issuer reviews evidence and decides — usually within **60 to 75 days** after the merchant responds. Outcomes are binary from the merchant's perspective: **won** (funds return to the merchant) or **lost** (funds stay with the cardholder). Stripe emails both parties when the case closes. The cardholder may not receive detailed merchant evidence; you learn the outcome as a final credit or re-charge on your statement.

During an open dispute, the merchant generally cannot issue a standard refund outside the dispute workflow for that charge. If you and the merchant reach an agreement mid-process, the merchant still needs you to **withdraw the dispute** with your bank — a verbal promise is not sufficient. Stripe's documentation on withdrawn disputes emphasizes that merchants must still submit evidence until the issuer formally closes the case in their favor.

For merchants, elevated dispute rates can trigger broader consequences — reserves, payout holds, and in extreme cases account restrictions documented in [Stripe Account Suspended](/blog/stripe-account-suspended). Understanding the cardholder journey explains why a single disputed charge creates urgent Dashboard notifications and balance debits even when the merchant believes the charge was legitimate.

---

## Legitimate Disputes vs Friendly Fraud: Where the Line Sits

The payments industry uses **friendly fraud** to describe disputes where a cardholder files a chargeback despite having authorized the purchase — for example, forgetting about a subscription, requesting a chargeback instead of going through the merchant's return process, or disputing a charge after receiving goods they later decided they did not want. Industry sources, including Stripe's <a href="https://stripe.com/guides/introduction-to-payment-disputes" rel="nofollow noopener">payment disputes guide</a>, note that fraudulent disputes account for a majority of disputes for many businesses — though exact percentages vary by vertical and are not uniformly audited.

Legitimate disputes include true unauthorized use, merchant failure to deliver, billing errors, duplicate charges, and canceled subscriptions that continued billing. The line blurs when a cardholder selects "fraud" for a charge they authorized but regret, or disputes a digital download after consuming the product. Issuers apply reason-code rules; merchants counter with authorization proof, IP addresses, login logs, and delivery confirmation.

This article takes no side in individual cases — cardholders have legal and scheme rights; merchants bear the cost of invalid chargebacks and the burden of proof when they contest. If you are a cardholder, filing an accurate reason code protects you from allegations of abuse and speeds legitimate resolution. If you are a merchant, treating every dispute as potential friendly fraud misses genuine service failures that refunds would have prevented. The conceptual framework for how disputes differ from broader risk events appears in [What Is a Stripe Dispute](/blog/what-is-stripe-dispute).

---

## Digital Goods vs Physical Goods: Different Dispute Paths

Dispute reason codes and evidence standards diverge sharply between intangible and tangible purchases — and cardholders should choose the path that matches what they bought.

**Physical goods** disputes use reason codes such as merchandise not received or not as described. Issuers expect tracking numbers, delivery confirmation, and return documentation.

**Digital goods and services** — SaaS, courses, software licenses — rely on access logs, account records, and terms-of-service acceptance rather than shipping labels. Chargebacks for digital goods are harder for merchants to win without access proof.

**Services over time** — event tickets, annual memberships — often start the dispute clock from the **service date** rather than the payment date. Hybrid purchases may require evidence from both paths; state clearly whether the failure was missing shipment, defective product, or inaccessible software.

---

## Conclusion

Disputing a Stripe-processed charge is a **bank-side process**, not a Stripe support ticket. Identify the charge using statement descriptors, attempt merchant resolution when appropriate, gather evidence matched to your dispute reason, and file through your card issuer within the windows that Reg E, Reg Z, or UK scheme rules provide. After filing, expect provisional credit while your bank investigates, a multi-week timeline to final decision, and parallel merchant notification through Stripe that debits their account regardless of whether you and the seller have already talked.

Merchants reading this article on Clink's blog gain something cardholder-facing guides rarely provide: a clear map of what their customers experience before a dispute hits the Dashboard — and why refunds, clear descriptors, and cancellation UX are the cheapest dispute strategy. For the merchant-side dispute lifecycle and reason-code taxonomy, see [What Is a Stripe Dispute](/blog/what-is-stripe-dispute); for reducing dispute volume before it starts, see [Stripe Chargeback Prevention](/blog/stripe-chargeback-prevention). Teams whose dispute rates contribute to broader account restrictions should also read [Stripe Account Suspended](/blog/stripe-account-suspended) for how chargebacks connect to payout holds and risk reviews.

---

## FAQ

### Can I dispute a Stripe charge directly with Stripe?

No. Stripe processes payments for merchants but does not issue your card or decide chargeback outcomes. You must contact your **card issuer or bank** — the institution whose name appears on your card — to file a dispute or billing-error claim. Stripe's role begins after your bank initiates the chargeback on the card network.

### How long do I have to dispute a Stripe charge?

It depends on your card type and country. US credit card billing errors generally must be reported within **60 days** of the statement showing the charge under Regulation Z. US debit card errors on statements follow a similar **60-day** window under Regulation E. UK chargebacks typically allow around **120 days** under card-scheme rules, with possible extensions for undelivered future-delivery purchases. Card networks also enforce maximum windows — often **120 days** from payment or service date — regardless of local law.

### What will appear on my bank statement for a Stripe charge?

You will see the merchant's **statement descriptor**, not the word "Stripe." Merchants configure a prefix (their business name) and may add a dynamic suffix after an asterisk for card payments — for example, `BRANDNAME* INVOICE 42` — within a **22-character** limit. If you do not recognize the descriptor, search your email for matching receipts before assuming fraud.

### Should I dispute or ask the merchant for a refund first?

Ask the merchant first when you recognize the business and the issue looks like a billing mistake — canceled subscription, missing refund, duplicate charge, or defective product with a return policy. Go straight to your bank for clearly **unauthorized** charges, fraud, unreachable merchants, or unresolved disputes after good-faith merchant contact. Credit card law does not require merchant notification before disputing undelivered goods.

### Will I get my money back immediately after filing a dispute?

Not always, but many issuers provide **provisional credit** during investigation — especially on US debit cards where Regulation E may require recredit within **10 business days** when timelines extend. Credit card issuers cannot collect the disputed amount while investigating under Regulation Z. Final resolution typically takes **two to three months** including merchant response and issuer review.

### What happens to the merchant when I dispute a charge?

The card network reverses the payment and notifies Stripe, which debits the disputed amount plus a dispute fee from the merchant's Stripe balance and opens an evidence submission window — usually **7 to 21 days**. The merchant submits proof through Stripe; the issuer makes the final decision. High dispute rates can trigger reserves, payout pauses, or account reviews — the connection between disputes and account restrictions is covered in merchant-focused Stripe risk guides.
