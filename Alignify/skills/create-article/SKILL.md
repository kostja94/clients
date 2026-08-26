# Create Article — Alignify 统一文章创建 Skill

> **版本**：v2.0 · 2026-08-26  
> **质量档位**：**每篇均为 flagship** — 无 lite/standard 降级；Research、Moat、BLUF、SelfCheck、终审全链路必过。  
> **部署仓**：`E:\自有部署项目\alignify production`  
> **上下文仓**：`E:\clients\Alignify`  
> **终审**：Step 10 → audit-ready → [`../audit-article/SKILL.md`](../audit-article/SKILL.md) → publish-ready

---

## 核心原则

1. **Flagship 固定** — 每篇须 Moat、Answer Blocks、完整 Research、BLUF、12 维 SelfCheck；发布线终审 **≥80**，目标 **S 级 ≥90**。  
2. **内容决定架构** — 章节由题材决定；`anatomy.md` / `templates/` 为参考菜单。A 层硬底线不变。  
3. **先中文后英文** — ZH/EN section 类型、顺序、锚点 id 对齐。  
4. **知识块 ≠ 文章** — 素材须重写，禁止整段复制。  
5. **创作 / 终审分离** — Step 10 自审 → audit-ready；**另一 Agent 或人类** 跑 audit-article → publish-ready。  
6. **素材源可外置** — 个人知识库等外部 SSOT **可直接引用**，**不必**复制/同步到 `knowledge/{dir}/{slug}.md`；Brief 与 Research Log 须记录**绝对路径**。

---

## 何时使用

- [ ] 素材 SSOT 就绪，满足其一即可：
  - Alignify 知识块：`knowledge/{tools,seo,marketing,insights}/{slug}.md`
  - **外部知识库**（如 `E:\个人知识库\…\{slug}.md`）— 在 Brief 中登记路径，**不强制**迁入 `knowledge/`
- [ ] 新建或重写正式页；slug 未注册

**不适用**：素材未完成 · 仅内链优化 · 仅 Meta 微调 · 已 audit-ready 仅需终审（→ audit-article）

---

## 类型决策

| 知识块目录 | `articleType` | 路由 | 正文路径 |
|-----------|---------------|------|---------|
| `knowledge/tools/` | `best-ranking` | `/blog/{slug}` | `content/blog/` |
| `knowledge/tools/`（存量） | `best-ranking-legacy` | `/tools/{slug}` | `content/tools/` |
| `knowledge/seo/` | `seo-guide` | `/seo/{slug}` | `content/seo/` |
| `knowledge/marketing/` | `marketing-strategy` | `/marketing/{slug}` | `content/marketing/` |
| `knowledge/insights/` | `insights-analysis` | `/insights/{slug}` | `content/insights/` |

---

## 流程总览（Flagship）

```
01 Intake — Gate A（KEEP/MERGE/STOP）+ 大纲草案
    ↓ PASS
02 Research — Gate 0R（全类型必做）+ Article Brief 定稿
    ↓ PASS
03 Keywords + README
04 Screenshots（best-ranking / legacy）
05 中文 md — Outline 3.5（同批≥2）→ Gate B → 起草
06 中文润色 — BLUF + Extractability
07 内链 + Internal Link Plan
08 Meta + Config
09 英文 md — 双语 parity
10 SelfCheck — Gate C → audit-ready + 5.5（同批≥2）
    ↓
audit-article — Final ≥80 → publish-ready
    ↓
11 publishDate — 全站唯一日历日 → [`11-publish-dates.md`](./11-publish-dates.md) + `scripts/ops/next-publish-date.mjs`
OG 封面（Step 08 后 / publish 前）— fal GPT Image 2，EN/ZH 分图 → [`../ops/og-covers.md`](../ops/og-covers.md)
（12 legacy modifiedDate）
```

**Phase 0 首行强制输出**：

```
## QualityTier: flagship（固定）
## ArticleType: {type}
## InvestmentScore: {X.X} — {摘要}
## Gate A: KEEP | MERGE → {slug} | STOP
```

---

## 步骤文档

| 步骤 | 文档 | 产出 |
|------|------|------|
| 01 | [`01-intake.md`](./01-intake.md) | Gate A + 大纲草案 |
| 02 | [`02-research.md`](./02-research.md) | Research Log + Brief + Gate 0R |
| 03 | [`03-keywords.md`](./03-keywords.md) | 关键词 + README |
| 04 | [`04-screenshots.md`](./04-screenshots.md) | 截图 |
| 05 | [`05-zh-content.md`](./05-zh-content.md) | ZH md |
| 06 | [`06-localize-zh.md`](./06-localize-zh.md) | 润色 + BLUF |
| 07 | [`07-internal-links.md`](./07-internal-links.md) | 内链 + Link Plan |
| 08 | [`08-meta-config.md`](./08-meta-config.md) | Meta + config |
| 09 | [`09-en-content.md`](./09-en-content.md) | EN md |
| 10 | [`10-quality-gates.md`](./10-quality-gates.md) | Gate C → audit-ready |
| — | [`../audit-article/SKILL.md`](../audit-article/SKILL.md) | publish-ready |
| 11 | [`11-publish-dates.md`](./11-publish-dates.md) | publishDate |
| 12 | [`12-legacy-tools-dates.md`](./12-legacy-tools-dates.md) | legacy 日期 |

---

## 规范索引（Flagship 核心）

| 主题 | 文档 |
|------|------|
| Gate 语义 | [`rules/gates.md`](./rules/gates.md) |
| Gate 回溯 | [`rules/gate-rollback.md`](./rules/gate-rollback.md) |
| Article Brief | [`rules/article-brief.md`](./rules/article-brief.md) |
| Research 三角 | [`rules/research-triangle.md`](./rules/research-triangle.md) |
| SelfCheck 12 维 | [`rules/selfcheck.md`](./rules/selfcheck.md) |
| BLUF / 段落 | [`rules/presentation.md`](./rules/presentation.md) |
| Extractability | [`rules/extractability-checklist.md`](./rules/extractability-checklist.md) |
| S 级清单 | [`rules/perfect-article-checklist.md`](./rules/perfect-article-checklist.md) |
| 结构原则 | [`rules/anatomy.md`](./rules/anatomy.md) |
| 质量检查 | [`rules/quality-checklist.md`](./rules/quality-checklist.md) |

完整索引：[`rules/README.md`](./rules/README.md)

---

## 渐进式加载

默认只读本 `SKILL.md` + 当前 Step 文档。**一次最多再读 2 个** `rules/` 文件。禁止一次性加载全部 references。

---

## Gotchas

- ❌ Gate 未 Pass 交付 · ❌ 跳过 Step 02 Research · ❌ 无 Moat 动笔 · ❌ FAQ 复制正文  
- ❌ 自审后直接发布（须 audit-article）· ❌ Investment Score <3.0 仍 KEEP（须 MERGE/STOP 或改角）  
- ❌ P0 数字无 Source Map 行 · ❌ 为凑节加空章
- ❌ **新 slug** publishDate 与全站已有 slug 重复（须 `next-publish-date.mjs --check`）
- ❌ 把 skill 示例日期当「今天」——以执行 Step 08/11 的实际 UTC+8 日历日为准

---

*create-article · v2.0 · 2026-08-26 · complements audit-article*
