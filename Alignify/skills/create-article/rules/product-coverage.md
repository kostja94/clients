# 产品覆盖 · 垂类选题 · 独占规则（Tools · best-ranking）

> **版本**：v1.0 · 2026-08-28  
> **SSOT**：新文产品 **数量** + **全站独占** + **垂类 slug 动机**  
> **适用**：`articleType: best-ranking` / `best-ranking-legacy`；KB 选题见 [`../../../knowledge-block/SKILL.md`](../../knowledge-block/SKILL.md)

---

## 为什么做垂类 slug

Alignify **不做**「一个大类塞满 10+ 款工具」的重复盘点。

| 问题 | 垂类解法 |
|------|----------|
| 同一产品出现在多篇 Best 文 | **一产品 = 一篇 canonical**；他文只链回 |
| 为凑篇幅写浅盘 | **3 款写深** 优于 10 款套模板 |
| slug 太宽、产品池打架 | slug 跟 **SERP 头词 + 窄意图**（如 `blog-website-builder` 非泛 `cms`） |

**KB  spoke 条件**（与 [`cms/KEYWORD-RESEARCH.md`](../../../knowledge/tools/cms/KEYWORD-RESEARCH.md) 一致）：SERP 头词 · ≥2 款 **vertical** 产品 · 非纯品牌 slug · **且** 拟选产品未被其他 slug 占用。

---

## 产品数量（新文默认）

| 层级 | 规则 |
|------|------|
| **A 硬底线** | Best 产品 H3 区块 **≥2 款**（单款不构成「排名/推荐」） |
| **B 新文默认** | **3 款即可 Pass** — Brief 锁定 roster 后不必再加 |
| **C 软上限** | 新文（`/blog/`）默认 **≤5 款** H3；>5 须在 Brief `deliberate 省略/扩展` **+ 用户确认** |
| **存量** | 108 篇 `/tools/` legacy **不强制** retrofit 数量；**新写 / 大改**仍须过独占查重 |

**深度来源**：Moat、选型框架、工作流片段 — **不是**产品条数。禁止为 flagship 印象堆 H3。

---

## 产品独占（canonical）

**定义**：normalize 后的产品 id（官方英文名 / 部署仓 H3 `{#product-slug}`）在全站 **仅 1 篇** 拥有 **完整 Best H3 块**（截图 + ≥100 字 ZH 描述 + CTA）。

| 场景 | 允许 |
|------|------|
| **Canonical 文** | 完整 H3 · 可进 TL;DR / meta 代表产品 |
| **非 canonical 文** | 内链到 canonical slug；对比表 **≤1 行**；正文 **≤1 句** 点名（无 H3、无截图、无 CTA） |
| **Hub / 概念文** | 不写 Best H3；只分流到 spoke |
| **Tier 1/2 客户** | 仍遵守独占；该 slug **就是** canonical（见 [`sections.md`](./sections.md) §3.3.0） |

**Normalize**：大小写不敏感 · 去 Inc./Ltd. · `WordPress` = `WordPress.org` 路线按 KB 主卡 · 子品牌不自动合并（Shopify ≠ Hydrogen 除非 Brief 明示同一 canonical）。

---

## 查重（Step 02 必做）

部署仓（`alignify production`）：

1. `content/blog/` + `content/tools/` grep 拟选产品名 / `{#product-slug}`
2. 或查 `scripts/data/tools-screenshot-registry.json` 键 `{pageSlug}:{productId}`

Brief 必填：

```markdown
**Product roster**（canonical 候选，锁定后 Step 05 不得擅自增删）:
  1. {Product A} — canonical 预期：本 slug
  2. {Product B}
  3. {Product C}

**Product dedup check**（YYYY-MM-DD）:
  - {Product A}: clear | conflict → {existing-slug} → {MERGE | swap product}
  - …
```

**冲突处理**：换产品 · MERGE 进已有 canonical slug · STOP — **禁止**静默双 canonical。

---

## Gate 挂载

| 阶段 | 检查 |
|------|------|
| **Gate A**（Step 01） | 粗 roster 与邻 slug **意图**不重叠；已知占用产品 → 换角或 MERGE |
| **Gate 0R**（Step 02） | `Product roster` + `Product dedup check` 全 clear |
| **Step 05** | H3 列表 = Brief roster（±0） |
| **Step 04 截图** | **仅 roster 内产品**；3 款 = 3 张，不补无关截图 |
| **Cross 5.5** | 同批 slug 间 **产品集合不交** |
| **Step 10 / audit** | 全文 H3 ⊆ roster；站级无 duplicate canonical（E51） |

---

## 与 meta / 对比表

- Meta description：**2–3 个代表产品** — 必须来自 **本页 roster**（见 [`meta.md`](./meta.md)）
- 对比表：行数 **≤ roster 款数**；无 roster 外产品行
- FAQ：禁止用 roster 外产品作「首选推荐」

---

## Fail 信号（快速）

- ❌ 「2026 最好的 X」下 **6–10 款** 同句式 H3，无 Brief 扩展理由
- ❌ Webflow 在 `website-builder` 与 `portfolio-website-builder` **两篇**都有完整 H3
- ❌ 为过 Gate 临时加第 4、5 款，描述从竞品页粘贴
- ❌ Hub 文 `content-management-system` 开 Best 产品节

---

*product-coverage · v1.0 · 2026-08-28*
