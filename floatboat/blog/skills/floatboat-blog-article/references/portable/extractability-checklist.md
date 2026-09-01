# Extractability 检查（Draft 阶段）

> Phase 4 使用。覆盖 **BLUF · Claim 原子性 · Judgment**——人类 SEO 与 LLM 摘录共用。  
> **Schema JSON-LD 与 `blog/schema/` 目录已停用并删除（2026-09-01）**：不在此清单要求 Agent 产出 JSON-LD 或向仓库写入 Source Map 文件。  
> 与 `06-research` §6.1 IG-3、SelfCheck §5.3–§5.4 一致。**随 skill 分发。**

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

## Schema JSON-LD（已停用）

| 层级 | 要求 |
|------|------|
| **Agent** | **禁止**创建或写入 `floatboat/blog/schema/`（目录已删除） |
| **Source Map 等** | Phase 6 仅在对话中交付，不写入仓库 |
| **正文** | 仍须写好可抽取的 FAQ / 步骤（站点若注入 JSON-LD，可从正文对齐） |
| **站点** | 结构化数据由 CMS / 站点侧处理 |

---

## Answer Blocks（standard / flagship）

Brief 声明 3–5 个 `AnswerBlocks`；每个对应 major H2，须可独立成 **40–60 词**段（与 B2 一致）。

- [ ] 每个 Answer block ID 在 Outline 有对应 H2
- [ ] 随机抽 3 个 block，单拎可答一个子问题

---

*extractability-checklist · portable v2.0 · 2026-06-19*
