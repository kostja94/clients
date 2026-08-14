# E15 — Presentation: 碎片化检测

## Input
Agent Draft 的正文段落结构为:
- 全文共 18 段，14 段 ≤2 句话
- 4 个连续短段落集群（3–5 个连续）
- 列表占比 48%
- 段落长度标准差 0.7
- 衔接率 35%

## Expected
- SelfCheck Presentation & Rhythm <4/10
- Fragmentation Check: >30% weighted → FAIL
- 必须修复后才能交付

## Severity: high
