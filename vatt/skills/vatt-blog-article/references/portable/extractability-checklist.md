# Extractability 检查（Draft 阶段）

> Phase 4 使用。覆盖 **BLUF · Claim 原子性 · Judgment · Schema**——人类 SEO 与 LLM 摘录共用。  
> 与 IG-3、SelfCheck 一致。**随 skill 分发。**

---

## Different, not better

Draft 前对照 Synthesis one-line thesis：是在 **paraphrase Top3**，还是提供 **Top3 没有的决策维度**？

---

## BLUF 三处

| # | 位置 | Pass 标准 |
|---|------|----------|
| B1 | TL;DR 下 | 40–60 词直接回答 primary intent |
| B2 | 每个 major H2 首段 | 先答后铺背景，无「In today's…」式延迟 |
| B3 | FAQ 每问 | 首句即答；与正文非复制（相似度 <30%） |

---

## Claim 原子性

| 检查 | Pass |
|------|------|
| 段首 claim | 每段首 1–2 句即陈述该段唯一主张 |
| 指代可解析 | 段内 it/this/上述 在同段可还原 |
| Chunk 独立 | 随机抽 3 段，单段可回答一个子问题 |
| 一 claim 一段 | 不在一段内塞 3+ 个无结构并列结论 |

---

## Judgment 信号（J1–J2）

| # | Pass | Fail |
|---|------|------|
| J1 | "We find…" / "For {场景}…" / "In our deployment…" | 裸「最佳/唯一/明显更好」 |
| J2 | 判断句同段或前段有数据/案例/限定 | 无来源绝对化比较 |

---

## Answer Blocks（standard / flagship）

Brief 声明 3–5 个 `AnswerBlocks`；每个对应 major H2，须可独立成 **40–60 词**段（与 B2 一致）。

- [ ] 每个 Answer block ID 在 Outline 有对应 H2
- [ ] 随机抽 3 个 block，单拎可答一个子问题

---

*extractability-checklist · portable v2.0 · 2026-07-06*
