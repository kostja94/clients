# Create Article — 文档索引

> Alignify **每篇 flagship**：内容决定架构；质量全链路见 Gate / SelfCheck / Step 11 Final Audit。
> **目录形态（2026-09-09）**：全扁平、无 `rules/`、无步骤壳。本索引即全部规范文档清单。命名规则：**单步独立产出 = `NN-` 文档；多步 / 全站规范 = 裸名 SSOT**。

---

## 流程：先读步骤文档，按需加载规范

| 步骤 | 步骤文档 | 产出 / 说明 |
|------|----------|-------------|
| 01 | [`01-intake.md`](01-intake.md) | Gate A + 大纲草案（含 §Intake 问答） |
| 02 | [`02-research.md`](02-research.md) | Research Log + Brief + Gate 0R（含 §SERP Fit 模板） |
| 03 | [`03-keywords.md`](03-keywords.md) | Brief → 关键词表 + Hub README |
| 04 | [`04-screenshots.md`](04-screenshots.md) | 截图规范 + 操作（**仅** best-ranking / legacy） |
| 05–06 · 09–09c | [`content-locale.md`](content-locale.md) Part 2–5 | ZH 起草/地道化 · EN 独立成稿 + 对等对比 |
| 07 | [`internal-links.md`](internal-links.md) §Step 07 执行速查 | 内链 + Link Plan |
| 08 | [`08-meta-config.md`](08-meta-config.md) | Meta + JSON 侧车 + **publishDate/modifiedDate** + Final CTA（含 Taxonomy 赋值） |
| 10 | [`quality-gates.md`](quality-gates.md) §Step 10 | Gate C → audit-ready（含 Source Map 模板） |
| 11 | [`final-audit.md`](final-audit.md) | **新会话**终审 → publish-ready |

> **编号说明**：05–06 / 09–09c 宿主 [`content-locale.md`](content-locale.md)；07 → `internal-links.md`；10 → `quality-gates.md` §Step 10；11 → `final-audit.md`。

---

## 规范文档（按主题）

### 质检 / Gate / 终审

| 主题 | 位置 |
|------|------|
| Gate 总表（A/0R/B/3.5/C/5.5/Final Audit）· 状态语义 · G1–G7 · H0–H4 | [`quality-gates.md`](quality-gates.md) |
| Step 10 SelfCheck 12 维 + 自动化预检 + audit-ready 包 + Cross-Article 5.5 | 同文件 §Step 10 |
| Source Map 模板（送审包附件 · EEAT E1–E6） | 同文件 §Source Map 模板 |
| P0 / P1 综合质量检查表 · Gate 失败回溯表 · S 级清单 | 同文件 §综合质量检查表 / §回溯表 / §S 级 |
| 终审 rubric · 触发语 · 渐进加载（Step 11 唯一承载） | [`final-audit.md`](final-audit.md) |
| 同批 ≥2 篇交叉检查（Outline 3.5 + Cross 5.5） | [`cross-article-audit.md`](cross-article-audit.md) |
| 常见错误（E-code） | [`common-errors.md`](common-errors.md) |

### 内容 / 双语 / 文案质量

| 主题 | 文档 |
|------|------|
| 双语正文（ZH/EN 双轨 · Extractability §3.4） | [`content-locale.md`](content-locale.md) |
| 双语术语 SSOT | [`locale-glossary.md`](locale-glossary.md) · [`locale-glossary.json`](locale-glossary.json)（机器层） |
| GTM 禁腔 + 中文英混禁则 + voice | [`writing-voice.md`](writing-voice.md) |
| BLUF / 段落节奏 | [`presentation.md`](presentation.md) |
| 文案质量 · Swap Test · 五维（M1/M2/M3） | [`copy-quality.md`](copy-quality.md) |
| 字数硬底线（H4 判据） | [`word-counts.md`](word-counts.md) |

### 步骤支撑 / 选品

| 主题 | 文档 |
|------|------|
| Intake 问答 | [`01-intake.md`](01-intake.md) §Intake 问答 |
| Article Brief | [`article-brief.md`](article-brief.md) |
| Research 三角 · SERP Fit 模板 | [`02-research.md`](02-research.md) |
| 关键词映射 | [`03-keywords.md`](03-keywords.md) |
| 垂类选题 · 产品数量 · 全站独占 | [`product-coverage.md`](product-coverage.md) |

### 结构 / 模板 / Meta

| 主题 | 文档 |
|------|------|
| 内容优先结构原则（A 层硬底线 · childrenHtml） | [`anatomy.md`](anatomy.md) |
| 章节规范（含结论与 Final CTA） | [`sections.md`](sections.md) |
| 内链 + Link Plan（全站规范 + Step 07 执行速查） | [`internal-links.md`](internal-links.md) |
| 页面模板 + 四类型速查 + 路由/Meta 注册 | [`templates.md`](templates.md) |
| Meta 四要素 | [`meta.md`](meta.md) |
| 截图规范（URL 选型 · Manifest · Firecrawl · Markdown 引用） | [`04-screenshots.md`](04-screenshots.md) |

### slug 锁定（User 确认边界 · 强制对照）

| 主题 | 位置 |
|------|------|
| Marketing slug（creator-program / creator-challenge-program / egc / marketing-types） | [`slug-locks.md`](slug-locks.md) Part A |
| SEO slug（submit-website + Platform properties） | 同文件 Part B |

---

## 相关 skill / 外部

| 用途 | 路径 |
|------|------|
| 存量文审核 / 内链优化 / 刷新 | [`../audit-optimize/SKILL.md`](../audit-optimize/SKILL.md) |
| 中文地道化后置轮（可选） | [`../../../中文地道化规范.md`](../../../中文地道化规范.md) |
| OG 封面 | [`../ops/og-covers.md`](../ops/og-covers.md) |

---

*INDEX · 2026-09-09 · create-article 扁平化 + 分册并入宿主后单一索引（目录共 25 md + 1 术语 json，含 SKILL / INDEX 两入口）*
