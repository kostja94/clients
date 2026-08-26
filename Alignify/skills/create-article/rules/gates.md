# Gate 总表 — Alignify Flagship

> **版本**：v1.0 · 2026-08-26  
> **质量档位**：Alignify **每篇均为 flagship**，无 lite/standard 降级路径。

---

## 状态语义

| 状态 | 含义 | 达成条件 |
|------|------|----------|
| **draft** | 成稿中 | Step 05–09 进行中 |
| **audit-ready** | 可送终审 | Step 10 SelfCheck：H0–H4 + 12 维全 Pass + 脚本绿 |
| **publish-ready** | 可发布 | [`audit-article`](../../audit-article/SKILL.md)：P0 Pass + 十维 ≥**80** |
| **S 级（标杆）** | 旗舰标杆 | 十维 ≥**90** + Moat 兑现 + Excellence Yes + **零 P1** |

> Alignify 默认发布门槛：**publish-ready（≥80）**；季度标杆文追求 **S 级（≥90）**。

---

## Gate 速查

| Gate | Phase | Fail → 回退 |
|------|-------|------------|
| **Gate A** | Step 01 | STOP / MERGE → 改题或合并 slug |
| **Gate 0R** | Step 02 | Step 02（补 R2/R3/Synthesis）或 STOP |
| **Gate B** | Step 05 动笔前 | Step 01/02（改大纲或 Brief） |
| **Outline 3.5** | Step 05 前（同批 ≥2 篇） | Step 01 大纲 / MERGE |
| **Gate C** | Step 10 SelfCheck | 见 [`gate-rollback.md`](./gate-rollback.md) |
| **Cross 5.5** | Step 10 后（同批 ≥2 篇） | Step 05–06 |
| **Final Audit** | audit-article | Step 05–09 按 P0/P1 项修复 |
| **Publish** | 人类发布 | P1 清零或 documented waive |

---

## P0 Gate G1–G7（事实与合规）

| # | 阻断条件 |
|---|----------|
| **G1** | 产品能力/定价/状态与官方 docs 矛盾 |
| **G2** | 站内死链；站外链接大面积失效 |
| **G3** | 量化 claim（准确率、ROI、用户数）无 attribution |
| **G4** | 竞品 GA/Preview/Archived/被收购 标注错误 |
| **G5** | 自有或推荐产品能力夸大 |
| **G6** | 内链指向未上线页面 | 含 Brief「Planned links」中的规划 slug；未发布姊妹篇仅可文字提及 |
| **G7** | 贬低竞品、unsupported superlative、合规风险 |

Alignify 专属 P0 见 [`quality-checklist.md`](./quality-checklist.md) P0-1–P0-13（结构/Meta/FAQ/frontmatter 等）。

---

## Alignify 专属 Hard Gates H0–H4

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research / Gate 0R | Research Log + SERP Fit + Synthesis + IG 三问全填 |
| **H1** | P0 G1–G7 + Alignify P0 | 零触发 |
| **H2** | Article Brief | Brief 已锁定；Answer Blocks 3–5；Moat Asset ≥1 |
| **H3** | 双语结构 parity | ZH/EN section 类型、顺序、锚点 id 一致 |
| **H4** | Flagship 深度 | 见 [`selfcheck.md`](./selfcheck.md) 维度 3–5、11 |

---

*gates · v1.0 · 2026-08-26*
