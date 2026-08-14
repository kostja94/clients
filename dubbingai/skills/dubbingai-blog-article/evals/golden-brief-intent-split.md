## Golden Brief — IntentSplit (#02 pattern)

> Eval E06 reference · Google Assistant vs live mic

### Expected Phase 0

```
## Topic Scope: Google Assistant TTS vs live microphone transformation
## Track: S
Article type: IntentSplit
KEEP/MERGE: KEEP
Information Gain:
1. Explicit "three jobs" disambiguation in lead
2. Menu paths for Assistant with as-of note
3. Bridge to real-time stack via how-to-change-your-voice
P3: Must link /blog/how-to-change-your-voice when discussing live mic
```

### Expected Brief fields

| Field | Value |
|-------|-------|
| Primary keyword | how to change Google Assistant voice |
| 正文互链（原 related） | best-ai-voice-changer, how-to-change-your-voice |
| Product mention | ≤25% |
| Forbidden | Dubbing download as Assistant fix |

### Expected slug

`how-to-change-google-assistant-voice` — no year in slug

### Gate checks

- P3 Pass if Assistant vs mic separated in first 2 paragraphs
- P3 Fail if article treats Assistant settings as Discord voice changer tutorial without split link
