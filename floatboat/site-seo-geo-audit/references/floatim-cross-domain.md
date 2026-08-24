# Floatboat ↔ FloatIM Cross-Domain Entity Rules

> Audit rules for brand consistency across floatboat.ai and im.floatboat.ai.
> **Last updated**: 2026-08-20

---

## Product Relationship

| Product | Role | Primary URL |
|---------|------|-------------|
| **Floatboat** | Desktop proactive agent OS — calendar runtime, Combo Skills, local execution | https://floatboat.ai |
| **FloatIM** | Agent-Native IM — humans and agents in shared groups; network layer | https://im.floatboat.ai |

**Narrative**: "Two apps, one network" — Floatboat produces on desktop; FloatIM coordinates socially. Not the same product; not duplicate content.

---

## On-Site Landing (`/floatim`)

| Check | Pass standard | P |
|-------|---------------|---|
| HTTP 200 + indexable | Page in sitemap (currently gap — P0 if missing) | P0 |
| Clear product distinction | Copy explains FloatIM ≠ Floatboat desktop | P0 |
| CTA to im.floatboat.ai | Visible link; opens app or signup | P0 |
| Title/Meta | FloatIM keywords — not diluting homepage Calendar-Driven positioning | P1 |
| Schema | Separate WebApplication or SoftwareApplication node if used | P1 |
| Blog support | `/blog/introducing-floatim` links here | P1 |

**FloatIM category keywords** (for `/floatim` page only — not homepage):
- agent-native messaging
- multi-agent collaboration
- chat with AI agents
- AI group chat
- human and AI agents collaborate

---

## Cross-Domain Linking

| From | To | Rule |
|------|-----|------|
| floatboat.ai/floatim | im.floatboat.ai | Use absolute HTTPS; descriptive anchor |
| floatboat.ai header/footer | Prefer /floatim landing before direct im link | Keeps entity on main domain |
| im.floatboat.ai | floatboat.ai/download | Return link for desktop app |
| Blog posts | Both when relevant | FloatIM posts → /floatim; workspace posts → /download |

**rel attribute**: Standard external link unless im is subdomain under same org — document if `rel="noopener"` only.

---

## Entity Consistency Checklist

| Fact | floatboat.ai | im.floatboat.ai | Must match |
|------|:------------:|:---------------:|:----------:|
| Company name | AOE Tech Labs Limited | Same | ✅ |
| Product names | Floatboat / FloatIM distinct | FloatIM primary | ✅ |
| Category | Calendar-Driven AI (FB) / Agent-Native IM (FIM) | — | ✅ |
| Pricing | Separate products — do not merge | Verify each | ✅ |
| Founder | Tan Shaoqing | If shown | ✅ |

---

## Duplicate Content Risk

| Risk | Mitigation |
|------|------------|
| Same hero copy on /floatim and im home | Differentiate — landing = SEO/education; app = product UI |
| Blog mirrored on both domains | One canonical on floatboat.ai |
| Shared FAQ with identical text | OK if canonical on floatboat.ai/floatim |

---

## Schema @id Boundaries

```
floatboat.ai/#organization     → parent org (AOE Tech Labs)
floatboat.ai/#software         → Floatboat desktop app
floatboat.ai/floatim#floatim   → FloatIM product page entity (optional)
im.floatboat.ai                → do not use as @id for Floatboat main software
```

---

## Audit Prompts (FloatIM-specific)

Run from prompt-library Category F +:

| Prompt | Expected primary cite |
|--------|----------------------|
| What is FloatIM? | /floatim or introducing-floatim blog |
| Agent native messaging app | /floatim |
| Slack for AI agents alternative | /floatim (careful with trademark) |

---

## Planned Routes (flag if missing)

| Route | Purpose |
|-------|---------|
| `/floatim/protocols` | IACT / Selfware protocol docs |
| `/floatim/vs-floatboat` | When to use which product |

---

## Fail Examples

| Finding | Severity |
|---------|:--------:|
| im.floatboat.ai blocked in robots while /floatim links prominently | P1 |
| Organization schema on /floatim missing legalName | P1 |
| FloatIM described as "Floatboat chat feature" only — loses category | P2 |
| Pricing for FloatIM conflated with Floatboat credits on /pricing | P0 |
