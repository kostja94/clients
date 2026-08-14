# E18 — Cross-Article: Intro 模板化检测

## Input
Agent 同批产出 3 篇 Track S 文章（Comparison + Alternative + HowTo）。
三篇 Intro 的句子功能序列完全相同:
1. 定义句 "An AI voice changer is..."
2. 场景句 "For gamers and streamers..."
3. 路标句 "This article explains/comparses/shows you..."
4. 数据句 "With 500+ voices and 100,000+ sounds..."

## Expected
- Phase 5.5 CA4 Intro 模板化检测 → FAIL（3+ 篇共享同一功能序列）
- Agent 修复: 每篇使用不同的 Intro 入口类型
  - Comparison: 数据入口（market growth stats）
  - Alternative: 场景入口（specific Discord setup dilemma）
  - HowTo: 困境入口（common routing problem）

## Severity: high
