## §SERP — SERP Fit 审计与 SEO 适配

> **Phase 0 / Phase 5 加载 · Hellyeah B2B SaaS 适配版**
> **来源**：templates/08-seo-serp.md v3.0 + Google Search Central 2025 + Featured Snippet 最佳实践

---

### 1. SERP Fit 审计模板（Phase 0 执行）

```markdown
## SERP Fit — {primary keyword}

**Primary keyword**:
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional  [ ] Mixed
**Target locale**: en-US (global)

### SERP Top 5 Analysis
| # | URL | DA est. | Covers | Misses |
|---|-----|---------|--------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

### Common Coverage Gaps
1. 
2. 

### Our Unique Contribution
1. 
2. 

### Snippet-Ready Definition (40–60 words)
{paste here}

### Competitive Intensity
- High DA domains in top 5: {count}/{5}
- Verdict: [ ] Differentiate strongly  [ ] Angle matters less (low competition)
```

---

### 2. 关键词覆盖检查

#### 2.1 位置覆盖

- [ ] H1 自然含 primary keyword（无需强制精确匹配，语义包含即可）
- [ ] H2/H3 含 2–3 个目标关键词簇变体
- [ ] keywords 规划 ≥5 个，覆盖长尾 + 变体（2026-08-11 起仅用于 SEO 规划，不入 frontmatter）
- [ ] 首 200 词内出现 primary keyword 或自然变体

#### 2.2 Hellyeah 特定关键词规则

| 话题 | Canonical 关键词 | 同义词（均需链 canonical） |
|------|------|------|
| GEO | programmatic GEO | generative engine optimization, AI search visibility, LLM SEO |
| AIMA | AI marketing assistant | AI ads manager（如 CommercialEducational）, WhatsApp marketing |
| Forge | agentic growth infrastructure | custom AI marketing workflow |
| Mutation | event-driven marketing | real-time marketing intelligence |
| Déjà Vu | continuous experimentation | A/B throughput platform（**private alpha**） |

---

### 3. Featured Snippet 优化

#### 3.1 Snippet 类型 × 适用场景

| Snippet 类型 | Hellyeah 适用场景 | 格式要求 |
|------|------|------|
| **Paragraph** | 定义类（"What is programmatic GEO?"） | 40–60 词紧凑段落，H2 后紧接，直接回答 |
| **List** | 步骤/策略（"How to divide SEO vs GEO labor"） | 编号列表，每项 ≤2 句 |
| **Table** | 对比类（"AIMA vs Agency vs SaaS tools"） | 3–5 行表格，不超 5 列 |

#### 3.2 Snippet-Ready 定义模板

```
## What is {topic}?

{A 40–60 word direct answer that a reader could copy-paste. 
Includes the primary keyword in the first 15 words. 
Ends with a bridge to the deeper content below.}
```

#### 3.3 People Also Ask 覆盖

- [ ] FAQ ≥3 题覆盖 Google PAA 中出现的 2+ 个问题
- [ ] FAQ 答案提供正文未覆盖的角度（非重复正文）
- [ ] FAQ 答案 40–80 词，适合被 Google 提取为 rich result

---

### 4. Meta 质量检查

#### 4.1 Title

| 检查项 | 标准 | Hellyeah 特定 |
|------|------|------|
| 长度 | 45–65 字符 | Pillar 可含 (2026) |
| Primary keyword | 前 40 字符内 | — |
| 品牌后缀 | 通常不加 `| Hellyeah` | Pillar 可无品牌后缀 |
| 点击吸引力 | 非纯关键词堆砌 | 含 benefit 或独特角度 |
| 与 H1 关系 | 可略有差异（title 更 SERP 优化，H1 更 editorial） | — |

#### 4.2 Description

| 检查项 | 标准 |
|------|------|
| 长度 | 140–160 字符 |
| Primary keyword | 前 80 字符内 |
| 内容 | benefit + intent 关键词；非模板填充 |
| CTA 暗示 | 可有可无（视类型而定） |

---

### 5. 结构化数据潜力

> **Hellyeah 博客当前无结构化数据实现——以下为创作时预留检查。**

| Schema 类型 | 适用文章 | 关键字段 |
|------|------|------|
| **Article** | 全部 | headline, datePublished, dateModified, author (Person), image |
| **Organization** | Compliance / Enterprise | name, url, sameAs (social) |
| **Person** | 全部 | name (Kostja), url, sameAs |
| **FAQ** | FAQ section | Question + Answer（如实现 FAQ schema） |

**创作时注意事项**：
- author.name 统一 "Kostja"
- datePublished 与 frontmatter date 一致
- image（JSON-LD）：2026-08-11 起 frontmatter 不含 image，JSON-LD 的 image 由 CMS/OG 层填充

---

### 6. 竞争强度评估

| SERP 竞争等级 | 判断标准 | 策略 |
|------|------|------|
| **低** | Top 5 中 <2 高 DA 域名，内容普遍浅 | 合格概述文即可；信息增量要求可放宽 |
| **中** | Top 5 中 2–3 高 DA，有深有浅 | 需 ≥2 项信息增量 |
| **高** | Top 5 中 ≥4 高 DA，内容全面深入 | 需要明确的差异化角度，标题和首段可见 |

**DA 参考**：Ahrefs DR / Moz DA。注意 site:hellyeahai.com 当前 DR 低（新站），内容质量是唯一杠杆。

---

### 7. Information Gain 结构化审计 ⭐v1.1

> **Phase 0.2 输出模板。与 §1 SERP Fit 审计配套——SERP 审计回答 "他们在写什么"，IG 审计回答 "我们多写了什么"。**

#### 7.1 四维度审计

```markdown
## Information Gain Audit — {primary keyword}

### Dimension 1: Framework / Taxonomy
- Does this article introduce a classification system, framework, or mental model NOT found in SERP top 5?
- [ ] Yes — describe: {e.g. "Division-of-labor table by team size: Series A / mid-market / enterprise"}
- [ ] No — risk: article is summary-level only

### Dimension 2: Comparison / Evaluation Angle
- Does this article compare or evaluate options using dimensions NOT covered by SERP top 5?
- [ ] Yes — describe: {e.g. "Metric ownership map: which KPIs stay with SEO vs move to GEO ops"}
- [ ] No — risk: comparison is generic feature list

### Dimension 3: Thesis / Argument
- Can the core thesis be expressed in one sentence that does NOT appear in SERP top 5?
- [ ] Yes — quote: {e.g. "SEO isn't dead — it's been promoted to editor"}
- [ ] No — risk: article is a rewrite of existing positions

### Dimension 4: Redundancy Ratio
- What % of paragraphs contain information findable in SERP top 5?
- Redundancy: {X}% (target: <40%)
- [ ] <30% → Strong gain
- [ ] 30–40% → Acceptable
- [ ] >40% → **STOP** — insufficient differentiation; merge into existing article or find new angle
```

#### 7.2 信息增量底线

| 竞争等级 | 最低 Unique Dimension 数 | 目标冗余比 |
|------|:---:|:---:|
| 低 | ≥1 | <50% |
| 中 | ≥2 | <40% |
| 高 | ≥3 | <30% |

**Hellyeah 特殊规则**：GEO 话题必须 ≥3 项（SERP 竞争激烈）；Compliance 可放宽至 ≥1（Hellyeah 采购视角本身有差异化）。

---

### 8. Phase 5 SelfCheck — SERP 维度

| 分数 | 标准 |
|:---:|------|
| **10** | SERP Fit 完整；IG 审计 4 维度全 Unique；关键词覆盖到位；snippet-ready 定义；PAA 覆盖；meta 精准 |
| **7** | SERP Fit 基本完整；IG ≥2 项 Unique；关键词基本覆盖；meta 合格 |
| **4** | 关键词覆盖不全；IG 仅 1 项 Unique；meta 模板填充；无 SERP 审计 |
| **1** | 关键词缺失；IG 0 项 Unique；meta 为空或严重模板化 |

---

*serp-audit · v1.1 · 2026-06-15 · adapted from templates/08-seo-serp.md v3.0*
