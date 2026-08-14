# Internal & External Links Checklist（Final Round AI）

> **依据**：与 [Nori blog](../nori/blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md)、[ThetaWave blog](../thetawave/blog/internal-external-links-checklist.md)、[Collov blog](../collov/blog/internal-external-links-checklist.md) 同一套打法。**Blog 簇互链地图与对账**（非规则，含 10×10 矩阵）见 [blog-interlinks.md](../blog/blog-interlinks.md)。站点以 **https://www.finalroundai.com** 为准；**正文为英文**，本规范为 **中文**。  
> **权威 URL 树**：[finalround-site-structure.md](../finalround-site-structure.md) §〇～§五 · **功能与路径对照**：[finalround-features.md](../finalround-features.md) · **关键词 ↔ 页**：[finalround-keywords.md](../finalround-keywords.md) · **竞品索引**：[finalround-competitors.md](../finalround-competitors.md) · **评测稿模板**：[finalround-blog-article skill](../skills/finalround-blog-article/references/review-programmatic.md)  
> **注意**：线上实际路径以 [finalround-site-structure.md §六](../finalround-site-structure.md)（2026-05-12 sitemap 对账）为准；`features` 中规划的 `/resume-builder` 等线上未收录，实际为 `/ai-resume-builder`。

---

## 链接分层（Final Round AI）

| 类型 | 路径 / URL | 用途 |
|------|------------|------|
| **Blog 互链** | `https://www.finalroundai.com/blog/{slug}` 或站内相对路径 **`/blog/{slug}`** | 同主题/意图分流；**不要**在正文用裸 `finalroundai.com` 拼出完整文章 URL 导致重复样式 |
| **核心产品入口** | `/interview-copilot`、`/ai-mock-interview` | 实时面试 Copilot、模拟面试；多数评测/对比稿的主 CTA 承载 |
| **平台与形式** | `/hirevue`、`/phone-interview` | HireVue/异步视频、电话面语境 |
| **上手与下载** | `/getting-started`、`/download` | 新用户路径、桌面端/Stealth |
| **人物与行业场景** | `/use-cases/software-engineers`、`/use-cases/product-managers`、`/use-cases/for-consultants`、`/use-cases/data-scientists`、`/use-cases/finance-professionals`、`/use-cases/remote-jobs` | **固定前缀** `/use-cases/`；线上 **无 `for-` 前缀**（仅 consultants 例外）；与稿内受众一致时链 |
| **简历与求职工具** | `/ai-resume-builder`、`/ai-job-hunter`、`/auto-apply`、`/cover-letter-generator`、`/linkedin-profile-optimizer`、`/linkedin-resume-builder`、`/resume-checker`、`/career-coach` | 全流程叙事（准备→面试→投递）；与 [finalround-site-structure.md](../finalround-site-structure.md) §一 一致 |
| **补充产品入口** | `/general-interview`、`/coding-copilot`、`/interview-notes`、`/qa-pairs`、`/salary-to-hourly-calculator`、`/try`、`/special-discount`、`/recruiters-hotline` | 见 [finalround-features.md](../finalround-features.md)；**有页再链** |
| **对比与信任** | 站内 `/compare/final-round-ai-vs-{competitor}`（27 竞品） | 线上实际路径；非 `/{competitor}-vs-final-round` |
| **面试准备 Hub** | `/interview-prep`、`/interview-prep/{company}-{type}` | 公司 × 题型程序化页 |
| **裁员追踪** | `/tech-layoffs`、`/tech-layoffs/{company}` | 25 家公司 |
| **面试真题** | `/interview-questions`、`/interview-questions/{slug}` | 150+ 篇 |
| **Glossary** | `/glossary`、`/glossary/{term}` | 12 术语 |
| **社区** | `/community/`、`/community/c/{slug}`、`/community/t/{slug}` | Discourse 论坛 |
| **转化（首页/定价）** | `/`、若存在则 `/pricing` 或产品内计费页 | 视实际上线路由；与竞品稿「Try free / See pricing」呼应 |

**原则**：Pillar/产品页与 **use-cases** 承担不同意图；**同一篇内** 同一目标 URL 不宜在相邻段落反复出现，宜按 **H2** 分散。

---

## Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **首段或第二段** | ≥1 条 | **相关 `/blog/{slug}`** 意图分流，或 **核心产品**（如 `/interview-copilot`）/ **与标题强相关的 use-case**；避免与 pillar 抢同一查询意图 |
| **Body Blog 互链** | 每篇 **1–4 条**（随博文量增长） | 链至 **`/blog/{slug}`**；对比/评测类可额外链至站内 **vs / alternatives** 若已发布 |
| **产品 / 转化内链** | 按节分布 | **`/interview-copilot`、`/ai-mock-interview`** 宜落在不同 **H2**；同一 URL 全文 **各段落至多 1 次** 为主，避免 CTA 堆砌感 |
| **use-cases 内链** | 与读者角色一致时 | 如 SWE 稿 → `for-software-engineers`；通稿面向上岸 → `for-remote-jobs` 等；**未上线不链** |
| **文末 Next steps（可选）** | **2–6 条** | 至少含 **1 条 blog** + **1 条产品或场景页**；与正文已出现的链一致，避免挂名不落地 |
| **frontmatter `related`** | **2026-08-11 起移除** | frontmatter **不含** `related`（与 `image`、`keywords` 一并移除）；互链以正文为准，`related` 如需展示由 CMS 侧配置 |
| **锚文本** | 描述性 | 避免 *click here*、*learn more* 单独成锚；可混合 exact / partial / **Final Round AI** 品牌名 |

---

## External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威 / 数据** | **2–8 条**（视篇幅） | 劳动统计、教育/科技媒体、可核对数据；句内或脚注标明出处 |
| **竞品 / 对比对象** | 评测/对比稿必备 | 建议：`rel="nofollow noopener"`；锚文本用 **公司名、产品名或功能定位** |
| **E-E-A-T** | 可验证 | 定价、功能以**官网 + 成稿日期**为据；避免不可证实的「行业第一」等绝对化表述（除非有来源） |
| **招聘市场 / 新闻** | 行业稿 | 裁员、招聘趋势等可引 Reuters、BLS、公司公告等；注明相对公开讨论中常见说法的**新事实/可核对的点** |

**竞品与素材**：[finalround-competitors.md](../finalround-competitors.md)

---

## Blog 内链现状审计（仓库稿）

清点在 `blog/*.md` 源码中 Markdown 链接 `(...)` 且路径以 `/` 开头的站内目标；`related` 以 frontmatter 为准。

**10 篇 interview 系列 + 产品三篇**：正文 `/blog/{slug}` 已 **全簇互通**（每篇对其余 9 个 blog slug 均有出链），**完整矩阵、`related` 对账、新文入簇步骤** 见 [blog/blog-interlinks.md](../blog/blog-interlinks.md)（**以此文件为 SSOT**）。

### 总览：与 Checklist 对照

| 维度 | 规范目标 | 改稿后情况 |
|------|----------|------------|
| 首段 / 第二段内链 | ≥1 条 | 评测/行业稿开篇多链 `/blog/{slug}`；`types` 等 pillar 与簇内互指明确 |
| Body 额外 `/blog/*` | 1–4 条起（可含首段，长文可更多条若分散在节） | 长文、评测、选购稿按节分布，忌相邻段重复同 URL |
| 产品 / 场景 / 转化 | 按主题分布 | 各文含 `ai-mock` / `interview-copilot` 等与题相关的落地路径 |
| `related` | 与正文可点一致 | 与 [blog-interlinks.md](../blog/blog-interlinks.md) §5 对账 |

### 历史：早期 4×4 子矩阵

早期仅四篇时曾在本文件保留 4×4 表；十篇成簇后**不再**在此维护副本——请只用 [blog/blog-interlinks.md](../blog/blog-interlinks.md) §4。

### 持续改进（可选）

- 新上线路径 **alternatives / vs** 若与 `blog` 不同目录，在总清单中核对一次 canonical。  
- 长文可另加 **文末 “Further reading”** 块，仅当篇数 >5 时避免首段过挤。

---

## 博文互链矩阵（建议维护）

随选题增加，在此记录 **A → B** 的推荐互链，避免孤文；新文上线后**回写**旧文 `related` 与首屏一句锚文本。

| slug（或主题） | 建议指向（正文中至少 1 次自然锚文本） |
|----------------|----------------------------------------|
| `verve-ai-review` | → `verve-ai-alternative`、→ `verve-ai-vs-final-round`（若已发布）· 产品 `/interview-copilot` |
| `parakeet-ai-review` | → `parakeet-ai-alternative`、→ `parakeet-ai-vs-final-round` · `/interview-copilot` |
| `tech-layoffs-ai` | → 同系列行业/职业稿（若已有）· `/use-cases/for-remote-jobs` 或 `for-enterprise` 视受众 |

**意图三角（示例）**：**单品牌评测** = 深描 + 定价/功能事实；**alternatives** = 多选项分流；**vs** = 参数对照，三者互链防 cannibalization 失控。

---

## 文章链接状态

新稿入库后在 [blog/README.md](../blog/README.md) 登记表补充一行，并更新下表。细则见上节 **「Blog 内链现状审计」**。

| # | 文章 slug | 首段内链 | Body `/blog/*` | 产品/场景/转化 | `related` | 与规范对齐 |
|---|-----------|----------|----------------|----------------|-----------|------------|
| 01 | `verve-ai-review` | ✅ 2 | + Quick Verdict `types` | ✅ + vs 段 `ai-mock` | 含 blog+产品+alt | **基本满足** |
| 02 | `parakeet-ai-review` | ✅ 2 | + Quick Verdict `types` | ✅ + vs 段 `ai-mock` | 含 blog+产品+alt | **基本满足** |
| 03 | `tech-layoffs-ai` | ✅ 2 | + closing `types` | ✅ remote + closing CTA | 含 3 篇 blog slug | **基本满足** |
| 04 | `types-of-job-interviews` | ✅ 2 | 多段 + Next 含 `dress` | ✅ mock/copilot/phone/hirevue/use-cases | 含 4 篇 blog + 产品 | **基本满足** — pillar |
| 05 | `how-to-dress-for-a-job-interview` | ✅ 2 | 多段含 types/评测 + 链 `questions` | ✅ mock/copilot/phone/hirevue/use-cases 等 | 含 5 篇 blog + 产品 | **基本满足** |
| 06 | `questions-to-ask-the-interviewer` | ✅ 2 `types`+`dress` + 首段 `tell-me` | Body + 评测 + finance/consulting uc | ✅ mock/copilot/getting-started + uc | 含 cluster + `tell-me` + 产品 | **基本满足** |
| 07 | `how-to-answer-tell-me-about-yourself` | ✅ 2 `types`+`questions` | 文内多段 + 表；电话/视频小节 | ✅ mock/copilot 与文内 CTA 一致 | 含 cluster + 评测 + 产品 + 新三篇 | **基本满足** — 开场题 pillar |
| 08 | `what-is-interview-copilot` | ✅ 2+ 簇内链 | 多段 + 表 + 外链 | ✅ copilot/mock/getting-started/uc | 含 pillar + 评测 + 09/10 + 产品 + 11 | **基本满足** — 产品释义无排名 |
| 09 | `ai-mock-interview-guide` | ✅ 2+ 簇内链 | 周计划 + 角色 + 外链 | ✅ mock/copilot/uc + DOL | 含 08/10 + 评测 + 产品 + 11 | **基本满足** — 练习 pillar |
| 10 | `best-ai-interview-tools` | ✅ 多簇 | 表 + 购买流程 + 外链 | ✅ copilot/mock/get-started/uc/FTC | 含 08/09 + 评测 + dress/tech | **基本满足** — 选购 pillar |
| 11 | `whats-new-interview-copilot` | ✅ 首段产品链 | Next steps 含 `what-is` | ✅ download/copilot/mock/coding/phone/getting-started/subscription | 含 08/09/10 blog + 产品 | **基本满足** — 更新公告；出链聚焦相关意图 |

---

## 规范总结

- **内链**：首段分流 + Body blog 1–4 + 产品/use-case 按 **H2** 穿插；**Related** 与正文一致可点击。  
- **外链**：权威可核对 + 竞品 **nofollow** + 成稿日定价/功能注记。  
- **与全站一致**：内链树以 [finalround-site-structure.md](../finalround-site-structure.md) §五 为准；路由变更时同步本表与 [finalround-keywords.md](../finalround-keywords.md)。  
- **新文上线后**：从 pillar/列表页、相关旧文补 1 条指入，形成可爬、可点击的**小型链接簇**。  
- **现状复盘**：大改内链或新增批量发文后，更新 §「**Blog 内链现状审计**」与「**文章链接状态**」表，避免规范与稿脱�