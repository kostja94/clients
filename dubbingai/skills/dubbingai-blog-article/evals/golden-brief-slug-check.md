# E16 — Slug: 内部架构词检测

## Input
Agent 提议 slug: `voice-changer-diagnosis-virtual-mic-not-working`

## Expected
- Gate B FAIL on A11（内部架构词 "diagnosis"）
- Agent 修复为: `voice-changer-discord-not-working` 或 `fix-virtual-mic-voice-changer`
- 竞品基准检查: primary keyword 搜 Google，前 5 竞品 slug 不含 "diagnosis"

## Severity: high
