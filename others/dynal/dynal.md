# Dynal - Product Marketing Context

> 遵循 [dynal-文档编写规范](./dynal-文档编写规范.md) | 基于 [https://dynal.ai/](https://dynal.ai/) 与公开信息  
> **关联**：[dynal-features.md](./dynal-features.md)（**主产品功能**） | [dynal-use-cases.md](./dynal-use-cases.md) | [dynal-keywords.md](./dynal-keywords.md) | [dynal-competitors.md](./dynal-competitors.md) | [dynal-site-structure.md](./dynal-site-structure.md)（**URL / sitemap 权威**） | [dynal-production-routing.md](./dynal-production-routing.md)（**主域 Rewrite、子站、多语言前缀**） | [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)（**Post Generator / 工具 #1**）| [dynal-tools.md](./dynal-tools.md)（**`/tools/` 引流小工具**，边界 §0） | [README.md](./README.md)（索引权威）

**文档性质**：以营销上下文与产品叙事为主；**§10 执行清单**为 SEO/技术附录，与本包合并维护（例外：多主题合一文档）。**§11** 为增长与市场侧重（与 Dynal 触达一致的假设），不替代 §10。

**Last updated**: 2026-05-11 — Solutions → Product 页；新增 /agent；与 2026-05-09 sitemap 对齐。

专项细节见各子文档；关键词摘要、竞品摘要、品牌与信任、vs ChatGPT 落地、执行清单见本文 **§6–§10**。

---

## 文档体系（与 [README.md](./README.md) 索引一致）

| 文档 | 职责 |
|------|------|
| [README.md](./README.md) | **文档索引权威**；维护时与下表同步 |
| **dynal.md**（本文） | 概览、定位、ICP 一句、信任与语气、关键词/竞品**摘要**、vs ChatGPT SEO、**§10 执行清单**、**§11 增长与市场侧重** |
| [dynal-features.md](./dynal-features.md) | **主产品功能**（工作流、**功能模块拆解**、官网 Outcome、**Dynal vs ChatGPT** 表、Solutions、Playbook/FAQ）；**非** `/tools/` 小工具权威 |
| [dynal-use-cases.md](./dynal-use-cases.md) | **目标用户 × 场景**（权威）、Persona 对照、情境故事线 |
| [dynal-keywords.md](./dynal-keywords.md) | 词→URL、**搜索量/竞争度表**（权威）、落地建议 |
| [dynal-competitors.md](./dynal-competitors.md) | 品类概览、**竞品格局表**（权威）、差异化、拦截 |
| [dynal-site-structure.md](./dynal-site-structure.md) | **网站结构、多语言 URL、sitemap、robots**（权威） |
| [dynal-production-routing.md](./dynal-production-routing.md) | **生产路由**：dynal.ai → **dynal-nextjs**（Vercel）Rewrite；**`/linkedin-post-generator` hub 留主应用**、子路径转子站；**`/{locale}/...`** 与子站路由平行配置 |
| [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md) | **LinkedIn Post Generator**（子文件夹）：路由与定位、**工具 #1**；关键词/竞品/topic 详表见子文档 |
| [dynal-tools.md](./dynal-tools.md) | **`/tools/` 引流小工具**（**#2–#12** 详表）；职责与边界见文首、**§0**；**§1.7**（#1 指专档）；**规划项** |

---

## 1. Product Overview

**One-line description**（**主产品定位**）:
```
Dynal is your AI LinkedIn agent — it learns your brand, plans your content, creates posts in your voice, and grows your presence.
```

**执行层补充**（与首页能力表述一致，用于文案展开而非替代主一句）: 从 notes、links、files、ideas 等多源素材生成草稿与周计划，发布前保留审核与声音/定位一致。

| 项目 | 内容 |
|------|------|
| **品类** | B2B/B2C SaaS / LinkedIn AI / 内容工作流 / Social selling |
| **官网** | [https://dynal.ai/](https://dynal.ai/) |
| **标题（官网）** | AI LinkedIn Agent & Post Generator for Viral Posts \| Dynal（**SEO 标题**；**主叙事**以 §1 一句为准：agent / learn brand / plan / your voice / grow presence，避免对外只等同「爆款生成器」） |
| **社会证明** | Product Hunt **#1 Product of the Day**；Trusted by **1000+** founders, consultants, marketers, and teams；Learned from **600K+** viral posts（官网表述） |
| **支持** | support@dynal.ai |
| **多语言（站点多语言切换）** | English、Español、Français、Deutsch、Português、Italiano |

**核心承诺（与主定位对齐，可落首页）**:
- **Learn your brand**（Brand DNA / 边界与上下文）
- **Plan your content**（周节奏与主题，非单次生成）
- **Posts in your voice**（多源素材 → 像你本人发声的草稿）
- **Grow your presence**（可持续存在感与发布闭环）
- **执行层**（与官网四步一致）：notes, links, files, ideas → **write, plan, review** → 审核后再发布

---

## 2. Positioning Statement

> **For** founders, consultants, marketers, executives, and agencies **who** need to **grow on LinkedIn** without losing **their brand** or **voice**—and without a manual blank-page grind—**our** Dynal **is** **your AI LinkedIn agent** **that** **learns your brand**, **plans your content**, **creates posts in your voice**, and **grows your presence**. **Under the hood**, it **ingests** multi-source material, **generates** drafts, **runs** a weekly plan, and **requires approval** before publish. **Unlike** generic chat AI or single-shot post generators, **we** pair **Brand DNA** with a **repeatable weekly system** and **approval-first** publishing **because** presence is built as a system, not from scattered prompts.

---

## 3. Value Proposition & Key Messages

- **Primary（主定位）**: **你的**领英 AI 代理——学你的品牌、计划内容、用你的声音发帖、放大存在感。
- **Secondary（执行差异化）**: 多源摄取；周计划与日历；审批优先；LinkedIn 原生工作流；多账号与协作。
- **与 ChatGPT 差异（事实表）**: 见 [dynal-features.md](./dynal-features.md) **第三节**「Dynal vs ChatGPT」。  
- **功能模块**: 见 [dynal-features.md](./dynal-features.md) **第一节**。

---

## 4. Target Audience / ICP

**权威详情**（人群 × 使用场景调研、官网 Persona 对照、情境故事线）→ [dynal-use-cases.md](./dynal-use-cases.md)。

**ICP 摘要**：目标用户含**构建个人 IP**、偏**高净值**人群。**地域、渠道与增长侧重**（海外主战场、SEO/KOL/投放等）**只在 §11 展开**，本节不重复。

**Jobs to be done**: 在领英上**可持续增长存在感**；让 AI **记住品牌与声音**；**计划**而不仅是单次生成；降低起笔成本；发布前可控。

---

## 5. Existing Website & Routes

**主站**: [https://dynal.ai/](https://dynal.ai/)

**路径、sitemap、多语言规则、robots Disallow** → [dynal-site-structure.md](./dynal-site-structure.md)（权威）。下表仅保留**导航语义**；**实际 slug** 可能不同（例如对比页为 **`/vs-chatgpt`**，Use Case 为 **`/use-case/...`**）。

| 类型 | 说明 |
|------|------|
| **主导航** | Agent、Features、Playbook、Use Cases、Pricing、About Us、Blog |
| **入口** | Sign in、Sign up |
| **Product（原 Solutions）** | LinkedIn Content System、LinkedIn AI Writer、LinkedIn Post Generator（独立路由） |
| **Compare** | VS ChatGPT |
| **Company** | About Us、Contact us、Roadmap |
| **Policy** | Privacy Policy、Terms of Service |
| **社交** | LinkedIn、X、YouTube |

正式路径以 [dynal-site-structure.md](./dynal-site-structure.md) §〇.3 对照表与 sitemap 为准。站点结构变更时同步更新 site-structure、[dynal-keywords.md](./dynal-keywords.md) 与 §10 执行清单。

---

## 6. Keywords（摘要）

主文档仅保留意图摘要；**词表、搜索量/竞争度、落地建议**以 [dynal-keywords.md](./dynal-keywords.md) 为准（尤其 **§1–§2**）。**LinkedIn post generator** 类词、Solutions 与工具 #1 专档 → [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)。

---

## 7. Competitors（摘要）

主文档仅保留品类提示；**竞品格局、品牌级差异、拦截策略**以 [dynal-competitors.md](./dynal-competitors.md) 为准（**§2 调研表**、**§4 拦截**）。

---

## 8. Brand、语气与信任标识

**语气**: 专业增长、可操作；优先强调 *your AI LinkedIn agent*、*learn your brand*、*plan*、*your voice*、*grow your presence*；辅以 *workflow*、*approval*。  
**避免**: 把产品**仅**说成「帖子生成器」或「爆款工具」而弱化代理、品牌学习与增长结果；只强调「viral」而无方法论；暗示不经审核的自动发帖（与 approval-first 矛盾）。

**信任与背书（首页常见）**:
- Product Hunt「#1 Product of the Day」徽章  
- 量化：1000+ teams；600K+ viral posts learned from（营销表述）  
- Logo 条：Instagram、YouTube、Stripe、LinkedIn、Google、Reddit、Product Hunt 等  

**页面与无障碍**: 示例 LinkedIn 截图需有意义的 `alt`；含文字的徽章旁保留同等可读文案。

---

## 9. vs ChatGPT 对比页（SEO 要点）

- **事实表**以 [dynal-features.md](./dynal-features.md) **第三节**为准；对比页路径见 [dynal-site-structure.md](./dynal-site-structure.md) §5（**`/vs-chatgpt`**）。  
- **Title/Meta**: 自然包含 ChatGPT、LinkedIn；避免关键词堆砌。  
- **内链**: 首页、Features、FAQ 与对比页互链。  
- **Schema**: 可用 `WebPage`；若页含 FAQ 则加 `FAQPage`。  
- **表述**: 陈述可验证的产品差异，避免贬低竞品。

---

## 10. 执行清单（SEO / 技术摘要）

| 优先级 | 项 | 说明 |
|--------|-----|------|
| P1 | Canonical | 全站唯一 canonical；与 hreflang 一致 |
| P1 | Title / Meta | 首页与 Solutions 差异化；核心词分配不重复堆砌 |
| P1 | Heading | 每页单 H1；层级不跳级 |
| P1 | OG + Twitter Card | og:image 绝对 URL；多语言 `og:locale` |
| P1 | Schema | Organization、WebSite、`SoftwareApplication`；首页 FAQ 可考虑 `FAQPage` |
| P1 | Solutions 三页 | 不同 H1/角度，防重复内容 |
| P1 | Core Web Vitals | LCP / INP / CLS；大图与 embed 优化 |
| P2 | Hreflang | en/es/fr/de/pt/it 互链 + x-default |
| P2 | Blog / Playbook | 栏目与内链至 Pricing、Features、对比页 |
| P2 | 认证页 | Sign in/up：`noindex`；**勿**用 robots.txt `Disallow` 同路径挡掉 noindex；勿进 sitemap |
| P2 | Sitemap / robots | 仅收录价值 URL；AI 训练爬虫策略按品牌策略单独定 |

---

## 11. 增长与市场侧重

> **性质**：与 Dynal 触达一致的**假设与通用增长注意点**，供叙事与优先级讨论；**非** §10 执行清单。口述或工具外的**投放单价**等对外与预算前须与**合同、后台**核对。

| 主题 | 说明 |
|------|------|
| **区域** | 主战场偏**海外**（北美、南美、日韩等）；国内短视频/社群引流**预期不高**。 |
| **SEO** | **长期**投入；落地页、内链（SPA 前端 SEO、反代、运营可自主发布营销页等）。 |
| **KOL** | **LinkedIn、YouTube**；短期**弱化 X（推特）**（流量质量参差），除非**品牌向**有明确目标。 |
| **投放** | 通用云广告可适量试错；**LinkedIn 广告**较 Google、Meta **更贵**，获客成本常**更高**（**须用后台数据核对**）；领英广告**素材生成/优化**可作为产品需求评估。 |
| **竞品与定价参照** | 品类内存在**高价套餐 + 重服务交付**；也存在**小工具流量大、转化低、合规/下架风险**的路径——Dynal 若做免费工具矩阵需权衡**人力、调研与转化**。 |
| **免费工具矩阵** | **#1** → [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)；**#2–#12** → [dynal-tools.md](./dynal-tools.md) **§2、§1.7、§3**（**勿**与当前线上 sitemap 混用）。 |

---

## 12. 引用来源

- 产品信息与结构：[Dynal 官网](https://dynal.ai/)（截至 2026-03-31 的公开文案与导航）  
- 关键词搜索量、竞争度与竞品格局：**权威数据与表** → [dynal-keywords.md](./dynal-keywords.md) §2（post generator 子集见 [dynal-pg-keywords.md](./linkedin-post-generator/dynal-pg-keywords.md)）、[dynal-competitors.md](./dynal-competitors.md) §2（须用 Ahrefs / Semrush / GSC 复核）
