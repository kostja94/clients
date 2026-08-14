# FinalRound Project Config（Skill reference）

> **本文件是 `finalround-blog-article` skill 的项目配置。** Phase 0R 加载；Phase 4/5 按需重载。
> **SSOT 文档**：项目主文档 `finalround.md`、站点结构 `finalround-site-structure.md`、功能 `finalround-features.md`、关键词 `finalround-keywords.md`、竞品 `finalround-competitors.md`、内链规范 `technical/internal-external-links-checklist.md`。本文件仅为 skill 创作时的事实速查，任何冲突以官网 + 上述 SSOT 文档为准。

---

## 1. 项目配置

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | FinalRound（全称 Final Round AI，正文统一 **FinalRound**；域名 finalroundai.com 小写） |
| **主域名** | https://www.finalroundai.com |
| **博客路径前缀** | `/blog/` |
| **核心产品** | **Interview CoPilot™**（桌面应用）——实时面试、练习面试、自动复盘、屏幕帮助、隐形模式均为其**能力**，非独立产品 |
| **产品形态** | 桌面应用承载实时会话/练习/报告/屏幕帮助；网站为营销与内容面；旧网页版与旧桌面版行为不同，不承诺一致 |
| **核心工作流** | Prepare → Perform or Practice → Review（一个 Goal 对应一份具体工作） |
| **Goal** | 一份具体工作：角色 + 公司 + 职位描述 + 简历/材料 + 练习场次 + 实时会话 + 复盘总结；含 Overview / Prep / Sessions 区域、就绪信号、面试倒计时 |
| **练习面试类型** | General · Coding · System design · Behavioral & leadership · Product & case · Data & ML · Salary negotiation · Recruiter screen（8 类） |
| **Preflight** | 上线/练习启动前检查：Goal 设置、本次会话可调简历/材料/回答语言/代码语言；Go Live/Practice → Preflight → Start session |
| **屏幕帮助** | Auto-capture（默认开启）、Solve screen（手动触发）、Results panel（完整技术方案 + 写入复盘） |
| **电话面试** | Preflight 中选 "This computer" 或 "Another device"（手机/第二笔记本）；一次性语音样本区分本人与面试官；免提靠近麦克风、安静房间 |
| **隐形模式 Stealth Mode** | 默认开启；隐藏悬浮 Copilot 窗口于 Zoom/Meet/Teams 屏幕共享或录制；Settings → Privacy & Stealth；无应用内验证徽章，建议私密共享自测一次 |
| **目标用户** | 求职者（技术、咨询、金融、产品、营销、销售、医疗、运营、远程） |
| **定价** | 免费计划（有限功能）+ 付费订阅；**无免费试用**；实时 Copilot 需付费订阅后首次会话才可用；Pro 解锁实时 Copilot、隐形模式、自动复盘、练习面试、高级面试类型 |
| **Proof** | 10M+ 用户（官方宣称）、10k+ 拿到 offer（官方宣称）、80+ 国家、91 种语言/口音、Trustpilot 3.6（US） |
| **Proof（禁写）** | 未经官网核实的 ARR/增长率、SOC 2 未列明时、其他未验证硬数据 |
| **署名默认** | `Kostja` |
| **语言** | 英文正文；中文仅沟通用 |
| **日期** | `date` 字段为发布日；一天一篇 |

---

## 2. 可链接 URL 白名单（G6 依据）

> 站点结构完整树见 `finalround-site-structure.md`。以下为创作常用路径。

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}`（见 content-graph） |
| 核心产品 | `/interview-copilot`、`/ai-mock-interview` |
| 面试类型 | `/general-interview`、`/coding-copilot`、`/phone-interview`、`/hirevue` |
| 附加工具 | `/ai-resume-builder`、`/ai-job-hunter`、`/auto-apply`、`/cover-letter-generator`、`/linkedin-profile-optimizer`、`/linkedin-resume-builder`、`/resume-checker`、`/career-coach`、`/recruiters-hotline`、`/salary-to-hourly-calculator`、`/qa-pairs`、`/interview-notes` |
| Use Cases（无 `for-` 前缀） | `/use-cases`、`/use-cases/software-engineers`、`/use-cases/product-managers`、`/use-cases/for-consultants`（唯一保留 `for-`）、`/use-cases/data-scientists`、`/use-cases/finance-professionals`、`/use-cases/remote-jobs` |
| 对比 | `/compare/final-round-ai-vs-{competitor}` |
| 面试准备 Hub | `/interview-prep`、`/interview-prep/{company}-{type}` |
| 面试真题 | `/interview-questions`、`/interview-questions/{slug}` |
| Glossary | `/glossary`、`/glossary/{term}` |
| 社区 | `/community/`、`/community/c/{slug}`、`/community/t/{slug}` |
| 裁员 | `/tech-layoffs`、`/tech-layoffs/{company}` |

> **⚠️ 转化路径（正文禁链，2026-08-11 起）**：`/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount` —— 由**独立按钮/CTA block**承载，**不进入正文内链**。正文提及用纯文本。

**禁止内链**：`/zh`（中文站）、转化路径（见上）、未上线/规划路径（`/internships` 等，见 site-structure 标注）、`/use-cases/for-enterprise`（未收录）。

---

## 3. G1–G7 阻断规则（一票否决）

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 6 SelfCheck 首维逐项对照。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、状态、数据与官方文档/官网矛盾 | 逐 claim 对照本文件 §1 + 官方文档。功能不在当前版本 → 不能声称"已发布"。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查所有内链是否可达（产品页 + blog 互链）。外链可有 1–2 失效（外部不可控），但不能全挂。 |
| **G3** | 无来源数字 | 量化 claim 无 attribution | 每个数字必须可追溯到原始来源或标注内部数据基础（"based on internal analysis, n≈X"）。单案例不能写成复数趋势。 |
| **G4** | 竞品状态错误 | GA/Beta/Preview/Archived/被收购 与官方公告矛盾 | 打开竞品官网/docs 验证。特别注意：已 Archive 项目标为 "active competitor"。 |
| **G5** | 产品能力夸大 | 自有产品能力超出当前 GA 版本或已文档化 roadmap | 检查产品 docs / product page。定位语言（"designed to"、"aims to"）≠ 已实现功能。 |
| **G6** | 内链指向未上线页面 | 链到本文件 §2 "禁止内链" 列表或未发布路径 | 对照 §2 白名单——只链白名单内路径。forthcoming 内链上限 ≤1 且仅限正文脚注。 |
| **G7** | 重大品牌风险 | 内容可能引发法律/合规/竞品纠纷 | 贬低性措辞、暗示作弊、隐私/隐形承诺过度。 |

---

## 4. F1–F6 阻断规则（FinalRound 特有，一票否决）

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **F1** | 定价违规 | 产品无免费试用；实时 Copilot 需付费订阅 | 全文不得出现 "free trial / try free / start free trial / free live interview" 等 claim；CTA 用 Download App / Get Interview CoPilot™ / See Plans。 |
| **F2** | 旧产品形态词汇 | 不得把 Mock Interview、Career Coach、Coding Interview、Phone Interview、System Design 描述为独立网页产品；不得引用旧启动窗口/音频表/Listen Check/Scan Code/独立 Practice 标签页 | 全文扫描上述词；能力应归入 Interview CoPilot™ 下。 |
| **F3** | 桌面应用叙事 | 实时 Copilot、练习、报告、屏幕帮助为桌面应用能力 | 不得暗示"在网站上使用实时功能"；下载/安装内容为核心；不得宣称旧网页版与桌面版行为一致。 |
| **F4** | 内部决策泄漏 | 正文不得包含内部决策语言 | 不得出现 "SEO implication"、推荐表述清单、站点架构建议、内部定位讨论、执行摘要等。 |
| **F5** | Stealth 措辞 | 不得把 "undetectable" 当唯一/首要价值主张 | Stealth Mode 描述为具体功能（默认开启、Settings → Privacy & Stealth、建议私密共享自测一次）；不承诺完美隐形。 |
| **F6** | 转化内链 | 转化由独立按钮承载 | 正文不得链接转化路径（`/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount`）；正文提及用纯文本。 |

---

## 5. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **错开方向** | 从锚点日**往前**排，越重要的文章排越近 |
| **避让已占用日** | 对照 `references/content-graph.md` 已有日期表；已有文章的日期不重复使用 |

---

## 6. 创作事实速查（产品能力）

### 6.1 Interview CoPilot™（实时面试）

- 面试中实时获取结构化答案；基于简历 + 职位信息个性化
- 支持平台：Google Meet、Zoom、Microsoft Teams、LeetCode、HackerRank、CodeSignal、CoderPad 等
- **桌面应用**承载；需下载启用（含隐形模式）
- Answers That Sound Like You：根据简历与职位生成

### 6.2 Practice Interview（练习面试）

- 从 Goal 启动；Preflight 选择面试类型；对着 AI 面试官出声排练
- 8 类：General / Coding / System design / Behavioral & leadership / Product & case / Data & ML / Salary negotiation / Recruiter screen
- Re-drill：针对上轮复盘识别的弱项定向复练

### 6.3 Interview Debrief（自动复盘）

- 面试后自动生成：问了什么、你怎么回答、如何改进
- 含 AI 改进建议、语音模式、表达清晰度、参与度分析
- 关联到对应 Goal；随会话沉淀

### 6.4 Screen Help（屏幕帮助）

- Auto-capture：默认开启，需要时读屏（问题/图表/文档/电子表格/报错）
- Solve screen：用户触发的屏幕读取
- Results panel：完整编程/系统设计解决方案显示在答案流旁，并写入复盘
- 无手动"编程模式/系统设计模式"切换；Copilot 自动识别

### 6.5 Phone Interview（电话面试）

- Preflight 中选 "This computer" 或 "Another device"
- Another device：一次性语音样本，区分本人与面试官同麦
- 标签可能短暂自纠；建议免提靠近麦克风 + 安静房间

### 6.6 Stealth Mode（隐形模式）

- 默认开启；隐藏悬浮 Copilot 窗口于 Zoom/Meet/Teams 屏幕共享或录制
- Settings → Privacy & Stealth 控制
- 无应用内验证徽章；建议重要面试前私有屏幕共享自测一次

---

*本文件事实以官网为准；策略变更时同步更新。*
