# 内链优化规范（Internal Links SSOT）

> **用途**：Moras blog 内链的**创作、维护、审计**唯一操作手册。与 [`content-graph.md`](./content-graph.md) §4.5、`moras/blog/blog-structure-internal-links.md` 矩阵对齐；本文侧重**可执行的分布与均质规则**。
>
> **审计工具**：`python skills/blog-article/tools/link_audit.py`（在 `moras/blog/` 目录运行）

---

## 1. 硬性规则（R1–R7）

| # | 规则 | Pass 标准 |
|---|------|-----------|
| **R1** | 出站 ≥2 个**不同** `/blog/` slug | 正文（frontmatter 之后） |
| **R2** | 锚文本描述性 | 禁 `click here` / `learn more` / `this article` |
| **R3** | 同 slug 同篇 ≤2 次 | 第 2 次仅在结论段或最强语境 |
| **R4** | **禁链区域** | `## TL;DR` 与 `## Frequently asked questions` 内**零**内链 |
| **R5** | 禁 G6 路径 | `/use-cases/*` `/app/*` `/auth/*` `/admin/*` + forthcoming |
| **R6** | 自然优先 | 语境不通不加；入链为 0 的 spoke 仅在有段落时补 1 条 |
| **R7** | Pillar #01 | 须链向 Cluster A 全部 spoke（#02–#09） |

---

## 2. 均质与分布（Moras 成稿标准）

### 2.1 数量带（按文章类型）

| 类型 | 目标出站 slug 数 | 同 slug 上限 |
|------|:----------------:|:------------:|
| Pillar / Framework | 8–14 | 2 |
| Setup / Production / Strategy | 5–9 | 2 |
| Spoke / Diagnosis / Seasonal | 4–7 | 2 |
| Platform Ops 短稿 | 3–5 | 2 |

**原则**：宁少勿滥；超出上限的重复链改为**纯文字指称**（FAQ/TL;DR 亦同）。

### 2.2 垂直分布（均匀）

将正文（不含 TL;DR / FAQ / Sources）按 **H2 块**切分；内链应：

1. **首 1/3**：至少 1 条「上游/context」链（Pillar、Hub、选品、setup）
2. **中 1/3**：至少 1 条「同簇 execution」链（hooks、script、production、合规）
3. **后 1/3 / Conclusion**：至多 1 条「下游/diagnosis」或「回 Hub」链

**禁止**：连续两个 H2 各塞 3+ 条内链；禁止在单个段落内堆 2 条以上不同 slug。

### 2.3 锚文本均质

| ✅ 推荐 | ❌ 避免 |
|---------|---------|
| `our [TikTok Shop niche selection guide](/blog/tiktok-shop-niche-selection)` | `[click here](/blog/...)` |
| `the [hooks framework](/blog/tiktok-video-hooks)` | `[this article](/blog/...)` |
| 名词短语 = 目标文 H1 核心概念 | 泛化「相关阅读」「learn more」 |

同一篇文章内，链向同一 slug 的锚文本应**一致或近义**（勿同一 slug 换 4 种写法凑次数）。

### 2.4 相关性梯度

| 优先级 | 链向类型 | 语境 |
|:------:|----------|------|
| P0 | 同 Cluster Hub / 父 spoke | 章节开篇定边界 |
| P1 | §4 矩阵「应链向」列 | Outline 阶段规划 |
| P2 | 跨簇 Context Bridge | 见 `blog-structure-internal-links.md` §5 |
| P3 | 薄弱入链 spoke | 仅当段落自然提及 |

**禁**：为凑入链在无关段落硬插 seasonal spoke；Seasonal 链需出现 **window / promo / calendar / 排期** 等语义。

---

## 3. 入链维护

### 3.1 新稿发布后（每批 ≥3 篇）

1. 从 §7.3 高入链 Hub 挑 **2–3 篇**加 1 条自然入链到新 slug
2. 扫 `link_audit.py` 输出：**零入链** → 必补 1 条；**单入链** → 建议补第 2 条

### 3.2 高入链 Hub（优先出站源）

`how-to-make-money-on-tiktok` · `tiktok-video-hooks` · `tiktok-ai-content-rules` · `tiktok-video-formats` · `tiktok-product-research` · `tiktok-shop-niche-selection` · `tiktok-affiliate-side-hustle`

### 3.3 Cluster F Seasonal spoke 入链模板

| 语境位置 | 示例锚方向 |
|----------|------------|
| #49 niche 60-day 协议 | Labor Day / Jumpstart 排期 |
| #04 product-research 季节性 | September Restock / Summer Sale |
| #30 trends 窗口 | Back to School / Halloween |
| #08 no-sales Q4 准备 | Black Friday |
| #07 side hustle 日历 | Holiday Gifts / Jumpstart |
| #05 hooks 节日机制 | Halloween / Fall Deals |
| #01 Pillar 年度规划 | sales-calendar Hub + 1 spoke |

---

## 4. Phase 工作流嵌入

| Phase | 动作 |
|-------|------|
| **3 Outline** | 列出 4–7 个目标 slug + 计划落入的 H2 |
| **3.5 Cross-check** | 同批互链不重复同一锚；spoke 链回 Hub |
| **4 Draft** | 按 §2.2 分布写入；FAQ/TL;DR 用纯文字指称 |
| **5 SelfCheck** | `link_audit.py` + `link_checker.py` 双跑 |

### FAQ / TL;DR 无链写法

```markdown
<!-- ❌ -->
See our [sales calendar](/blog/tiktok-shop-sales-calendar) for dates.

<!-- ✅ -->
See our **2026 TikTok Shop sales calendar** article for full promo dates.
```

---

## 5. 审计命令

```bash
cd moras/blog
python ../skills/blog-article/tools/link_audit.py          # R1–R4 + 入链快照
python ../skills/blog-article/tools/link_checker.py {file} --forbidden "/use-cases/,/app/,/auth/,/admin/"
```

**发布 Gate**：`link_audit.py` 中 R3/R4 计数为 **0**，R1/R2/R7 **PASS**。

---

## 6. 文档同步

内链批次优化后更新：

1. `moras/blog/blog-structure-internal-links.md` §7 快照
2. `content-graph.md` §4.5 薄弱入链列表（若有变化）

---

*Moras blog-article skill · internal-links · v1.0 · 2026-08-24*
