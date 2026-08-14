# Series Canonical Ownership — Anti-Clone Contract

> Brief only. Guides rewrites of 05–09. Slugs frozen. Updated 2026-07-23.

## Ownership table

| Concept | Canonical article | Other articles may only |
|---------|-------------------|-------------------------|
| Full Clink integrate path (skills / CLI / catalog / webhooks) | **05** `how-to-add-payments-lovable-app` | 1–2 sentences + link to 05 |
| Lovable built-in Paddle vs Stripe choice | **05** | 06 deep-dives Stripe only |
| Lovable Stripe ops (built-in / legacy / go-live) | **06** `integrate-stripe-lovable` | 05 links out; no step dump |
| Bolt webhook four failure modes | **07** `how-to-add-payments-bolt-app` | Reference, do not copy |
| v0 middleware signature trap | **08** `how-to-add-payments-v0-app` | Reference, do not copy |
| Replit paid gate / Whop / Agent one-prompt Stripe | **09** `how-to-add-payments-replit-app` | Reference, do not copy |
| MoR vs PSP framework | **02** `mor-vs-psp` | Cite framework, no full table rewrite |
| Smart routing 3–5% recovery | **03** `smart-routing` | Cite, no case dump |
| What is Clink / four products | **01** `what-is-clink` | 1–2 sentences + link |

## Beyond {Platform} rule (05–09)

Each Beyond section must contain:

1. **3–5 platform-specific graduation signals** (original to that platform)
2. **One sentence** pointing to 05 for the full Clink path
3. **No** shared boilerplate that only swaps the platform name

Forbidden pattern: “Integrate once, connect Stripe underneath, keep subscription data portable… Contact Sales… clinkbill.com” copied across 07/08/09.

## Title strategy A

Keep primary SearchCapture keywords; use em dash ` — `; prefer 45–70 characters; slug frozen.
