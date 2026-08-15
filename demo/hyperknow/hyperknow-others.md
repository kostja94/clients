# Hyperknow 杂项汇编（Others）

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)  
> **本文档职责**：路由明细、技术 SEO 占位、合规摘要、数据引用、定价备忘、GEO/Schema、项目任务与 Backlog。  
> 关联：[hyperknow.md](./hyperknow.md) | [hyperknow-keywords.md](./hyperknow-keywords.md) | [hyperknow-site-structure.md](./hyperknow-site-structure.md) | [hyperknow-growth-strategy.md](./hyperknow-growth-strategy.md)  
> 流程依据：[通用-多文件文档联动精炼与增量循环.md](../../client-template.md) **v8**

**Last updated**: 2026-03-20（与六主文档配套；**指南 v8 三轮联动**已更新 Routes 与 Backlog）

---

## Routes and sitemap（路由总表与索引占位）

### 路由总表（hyperknow.io）

| 路径 | 类型 | 对应文档 | 状态 |
|------|------|----------|------|
| / | 首页 | 主文档、growth | 已上线 |
| /pricing | 商业 | 本文 **Pricing** | 已上线 |
| /manifesto 或首页锚点 | 品牌叙事 | hyperknow.md | 已上线 |
| /product/agent | 产品 | features | 待建（现多在同页滚动） |
| /features/* | 功能落地 | features | 待建 |
| /integrations/canvas | 集成 | features、use-cases | 待建 |
| /for/finals | Use case | use-cases、keywords | 待建 |
| /for/open-book-exams | Use case | use-cases、keywords | 待建 |
| /for/*（其余） | Use case | use-cases | 待建 |
| /blog | 内容 | keywords / growth | 待建 |
| /compare/chatgpt | 对比 | competitors | 待建 |
| /privacy | 法律 | Trust | 頁脚 |
| /terms | 法律 | Trust | 頁脚 |
| /contact | 线索 | growth | 已有 Get in Touch |

### 索引与 canonical（占位）

| 类型 | 处理 |
|------|------|
| **staging** | `noindex` 或 Basic Auth |
| **博客分页** | canonical 策略 `待验证` |
| **多语言** | 第二语言上线前 hreflang；见 [SEO-多语言与-locale-指南.md](../../SEO/SEO-多语言与-locale-指南.md) |

*变更时同步 [hyperknow-keywords.md](./hyperknow-keywords.md)。*

---

## Trust and compliance（信任与合规）

**EdTech / AI 辅导**涉及学术诚信与未成年人场景，以下为**摘要**；对外以法务审定与产品实际限制为准。

### 1. 与官网 Manifesto 一致

- 品牌明确反对 **shortcuts or cheating**，主张更快学习、更深理解（官网原句精神）。  
- 市场与功能描述避免鼓励**学术不端**（代考、未授权协作等）。

### 2. 产品表述边界（占位）

| 陈述 | 说明 |
|------|------|
| **能力** | AI 学习辅助、材料组织、讲解与练习 |
| **非承诺** | 不保证分数、排名、录取结果；不替代教师/学校最终评价 |

### 3. 未成年人

- 访谈提及家长询问初中生使用；实际上线规则（年龄门、监护人同意）**待验证** 并以产品条款为准。

### 4. 隐私（与官网 FAQ 摘要一致）

- 声称**不访问完整对话历史**；**Report Issue** 可让团队查看**该次对话**排错。  
- 全文见官网 Privacy Policy。

---

## Proof and citations（可公开数据与引用）

| 数据/陈述 | 来源 | 日期 | 状态 |
|-----------|------|------|------|
| 定价 Free / Pro $12 | 官网 | 2026 | 以结账页为准 |
| 「5 个大版本、数百小版本」 | 创始人访谈 | `待填` | 叙事非审计数据 |
| 用户量、MAU、留存 | — | — | `待验证` |
| 「首个 proactive learning agent」 | 官网营销 | — | 需竞品核对后对外 |

**规则**：对比竞品功能、价格、用户数，须填 URL + 抓取日期；无来源则 **`待验证`** 且不得对外作事实陈述。

---

## Pricing（商业与定价）

| 档位 | 价格（官网展示） | 要点 |
|------|------------------|------|
| **Free** | $0 | 基础 Agent 额度；上传；quiz/flashcard；体验 proactive |
| **Pro** | **$12** | 约 10× 额度；Knowledge Base；Memory；高级功能早鸟等 |

- **Invite 用户**：FAQ 称无限 LLM、创始人 1v1 onboarding、Discord 等 — 以最新 FAQ 为准。  
- **创始人 Quick Chat**：可获 Discount Code（官网自述）。

---

## GEO schema and FAQ（GEO 与结构化数据）

### TL;DR

- **Organization** + **WebSite**（含 `SearchAction` 若站内搜索上线）为基线。  
- **SoftwareApplication** 或 **WebApplication**（若产品以 Web 为主）描述 Agent — 字段与截图 `待验证`。  
- **FAQPage**：首页 FAQ 可抽取；高利害声明与 Trust 一致。  
- 文章 / 博客上线后：**Article** + `datePublished` / `dateModified`（见 [GEO-落地操作与站内实施.md §四](../../GEO/GEO-落地操作与站内实施.md#四页面日期lastmod与前台展示)）。

### 待办

- [ ] Rich Results Test 过一遍首屏与 FAQ  
- [ ] 对比页、案例页是否需 **Review** schema — 仅当有真实可验证评价时  

---

## Project tasks and backlog（项目任务与调研）

### 版本与叙事

| 日期 | 事件 |
|------|------|
| 2025-11 | 通用学习智能体正式发布 |
| ~2026-02 | Hyperknow 3.0（主动规划、Deep Learn 等）— 以官宣为准 |

### 调研 Backlog（模板）

| ID | 从哪份文档引出 | 需查证 | 优先级 | 结果摘要 |
|----|----------------|--------|--------|----------|
| R1 | competitors | 「首个 proactive」可比表述 | P1 | |
| R2 | keywords | 美国 vs 华语搜索量差异 | P2 | |
| R3 | growth | 高校 newsletter 合作路径 | P2 | |
| R4 | features / site-structure | 单页应用 vs 独立 `/features/*`：SEO 与工程权衡 | P1 | 来源:推演 |
| R5 | keywords | 「不知问什么」意图是否有搜索量（英/中） | P2 | 来源:推演 |
| R6 | competitors | Khanmigo / 同类校内置 AI 的公开能力表 | P2 | |
| R7 | Trust | K-12 年龄门与监护人条款与产品实际是否一致 | P1 | |
| R8 | GEO | SoftwareApplication 字段与截图素材 | P2 | |

### Changelog（仓库级）

| 日期 | 说明 |
|------|------|
| 2026-03-20 | `hyperknow.md` 拆为六主文档 + **本 others**；对齐通用指南 v8；真格等**访谈长文原文**不存仓库，叙事要点已拆入 keywords / features / use-cases / growth / competitors（增量不压缩为单句） |
| 2026-03-20 | **指南 v8 三轮联动**：keywords/use-cases 路径对齐；site-structure §4 映射；features 补 Phase1 与 Canvas 路径；competitors 补教育 AI 占位；growth 增 E3 与已完成待办；本表 Routes、Backlog R4–R8 |

---

*Demo · others 单文件汇编*
