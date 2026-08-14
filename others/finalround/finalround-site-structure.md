# Final Round AI 网站结构与 URL（finalroundai.com）

> **站点根**：https://www.finalroundai.com/  
> **关联**：[finalround.md](./finalround.md) | [finalround-use-cases.md](./finalround-use-cases.md)（场景与 Persona，**非** URL 权威） | [finalround-features.md](./finalround-features.md)（功能卖点，**非** URL 权威） | [finalround-keywords.md](./finalround-keywords.md) | [finalround-blog.md](./blog/finalround-blog.md) | [finalround-production-routing.md](./technical/finalround-production-routing.md)（前端：Rewrite / 模式 A·B / `/_next`） | [internships/](./internships/)（实习 Hub / 公司指南 / pSEO · 独立子文件夹）  
> **Skills 对齐**：**website-structure**、**sitemap**、**internal-links**。

**用途**：描述 **规划与目标 URL、路径树、角色落地页文案、待拓展路径与内链树**，供 SEO、建站与文档对齐。**线上路由或 sitemap 变更后请更新本文**（并复核 [finalround-keywords.md](./finalround-keywords.md) 中目标页列）。

**信息来源**：内部规划 + **sitemap.xml 全量对账**（2026-05-12，用户直接提供 sitemap index + main_pages + tech_layoffs + compare + salary + interview_prep + glossary + community + interview_questions 子 sitemap，对账完毕）。

---

## 〇、站点层级与 URL 规则（总则）

### 〇.1 树状层级（2026-05-12 sitemap 对账）

```
www.finalroundai.com/
├── /（首页 EN）✅
├── /zh（首页 ZH）✅
│
├── 核心产品与转化页（20 页）
│   ├── /interview-copilot ✅
│   ├── /ai-mock-interview ✅
│   ├── /hirevue ✅
│   ├── /phone-interview ✅
│   ├── /qa-pairs ✅
│   ├── /general-interview ✅
│   ├── /coding-copilot ✅
│   ├── /interview-notes ✅
│   ├── /ai-resume-builder ✅
│   ├── /ai-job-hunter ✅
│   ├── /auto-apply ✅
│   ├── /cover-letter-generator ✅
│   ├── /linkedin-profile-optimizer ✅
│   ├── /linkedin-resume-builder ✅
│   ├── /resume-checker ✅
│   ├── /career-coach ✅
│   ├── /recruiters-hotline ✅
│   ├── /salary-to-hourly-calculator ✅
│   ├── /try ✅
│   └── /special-discount ✅
│
├── 通用页（10 页）
│   ├── /frequently-asked-questions ✅
│   ├── /about ✅
│   ├── /privacy-policy ✅
│   ├── /terms-of-use ✅
│   ├── /refund-policy ✅
│   ├── /careers ✅
│   ├── /referral-program ✅
│   ├── /influencer-program ✅
│   ├── /media-kit ✅
│   └── /explore ✅
│
├── Use Cases 场景（7 页，**无 `for-` 前缀**）
│   ├── /use-cases ✅（索引）
│   ├── /use-cases/software-engineers ✅
│   ├── /use-cases/product-managers ✅
│   ├── /use-cases/for-consultants ✅（注意：仅此项保留 `for-`）
│   ├── /use-cases/data-scientists ✅
│   ├── /use-cases/finance-professionals ✅
│   └── /use-cases/remote-jobs ✅
│
├── Blog（~100+ 篇程序化 + 草稿 + 分类）
│   ├── /blog ✅（索引）
│   ├── /blog/{slug}（产品/指南/评测/行业/薪资/简历/Cover Letter）✅
│   └── /category/{slug}（分类归档）✅
│
├── 面试准备 Hub（/interview-prep/）
│   ├── /interview-prep ✅（索引）
│   └── /interview-prep/{company}-{type}（7+ companies × 5 types）✅
│
├── 面试真题库（/interview-questions/）✅
│   ├── /interview-questions ✅（索引）
│   └── /interview-questions/{slug}（150+ 篇）✅
│
├── 竞品对比（/compare/）
│   └── /compare/final-round-ai-vs-{competitor}（27 竞品）✅
│
├── Tech Layoffs（/tech-layoffs/）✅
│   ├── /tech-layoffs ✅（索引）
│   └── /tech-layoffs/{company}（25 家公司）✅
│
├── 薪资数据（/salary/title/）✅
│   └── /salary/title/{seniority}-{title}-in-{location}（程序化页）
│
├── 其他内容板块
│   ├── /glossary ✅（索引 + 12 术语）
│   ├── /articles/{slug}（技术/DSA 内容）✅
│   └── /guide ✅
│
├── 社区（Discourse）✅
│   ├── /community/ ✅
│   └── /community/{c|t}/{slug}（6 分类 + 40+ 主题）✅
│
├── Internships / 实习指南（规划中）📋
│   ├── /internships（Hub）
│   └── /internships/{company-slug}
│
└── 子域名
    ├── app.finalroundai.com ✅（Web 应用）
    └── accounts.finalroundai.com ✅（登录/注册）

图例：✅ sitemap 确认 · 📝 项目 draft · 📋 仅规划
```

### 〇.2 URL 规则

| 规则 | 说明 |
|------|------|
| **大小写与分段** | 路径 **小写**；多词用 **kebab-case**（如 `for-software-engineers`）。 |
| **Use Cases 场景页** | **扁平单段**：固定前缀 **`/use-cases/`**，每条为一级子路径 `{slug}`（如 `/use-cases/software-engineers`）；**注意线上无 `for-` 前缀**（仅 `/use-cases/for-consultants` 例外保留了 `for-`）。 |
| **嵌套场景** | `/interview-copilot/*`、`/ai-mock-interview/*` 等为 **SEO 拓展规划**，上线前需与工程路由、canonical 策略一致。 |

### 〇.3 与营销文档对照

| 主题 | 权威文档 |
|------|----------|
| **谁在什么情境下用**、行业与阶段表 | [finalround-use-cases.md](./finalround-use-cases.md) |
| **路径、内链、落地文案** | **本文档** |
| **功能卖点与定价** | [finalround-features.md](./finalround-features.md) |
| **关键词 ↔ 目标页** | [finalround-keywords.md](./finalround-keywords.md) |

---

## 一、页面清单与目标关键词（2026-05-12 sitemap 对账）

> **状态**：`✅` = sitemap 收录 | `⚠️` = sitemap 未收录但已知存在 | `📋` = 仅规划。**注意**：`/getting-started`、`/download`、`/subscription`、`/faq`、`/contact`、`/scholarship` 在 main_pages sitemap 中**未出现**（可能被 noindex、JS 渲染或独立 sitemap 覆盖）。

### 1.1 核心产品与功能页（main_pages sitemap 收录）

| 页面 | URL | Priority | Changefreq | 目标关键词 |
|------|-----|----------|------------|------------|
| 首页 | / | 1 | monthly | AI interview assistant |
| Interview Copilot | /interview-copilot | 0.8 | weekly | interview copilot, real-time interview AI |
| AI Mock Interview | /ai-mock-interview | 0.8 | weekly | AI mock interview, interview practice AI |
| General Interview | /general-interview | 0.8 | weekly | AI interview help |
| HireVue 准备 | /hirevue | 0.8 | yearly | HireVue interview prep |
| Phone Interview | /phone-interview | 0.8 | yearly | phone interview AI |
| Q&A Pairs | /qa-pairs | 0.8 | yearly | interview questions and answers |
| Coding Copilot | /coding-copilot | 0.8 | yearly | coding interview AI copilot |
| Interview Notes | /interview-notes | 0.8 | yearly | interview notes AI |
| AI Resume Builder | /ai-resume-builder | 0.8 | weekly | AI resume builder |
| AI Job Hunter | /ai-job-hunter | 0.8 | yearly | AI job hunter, auto apply jobs |
| Auto Apply | /auto-apply | 0.8 | yearly | auto apply jobs AI |
| Cover Letter Generator | /cover-letter-generator | 0.8 | yearly | AI cover letter generator |
| LinkedIn Profile Optimizer | /linkedin-profile-optimizer | 0.8 | yearly | LinkedIn profile optimizer |
| LinkedIn Resume Builder | /linkedin-resume-builder | 0.8 | yearly | LinkedIn to resume |
| Resume Checker | /resume-checker | 0.8 | yearly | resume checker AI |
| Career Coach | /career-coach | 0.8 | yearly | AI career coach |
| Recruiters Hotline | /recruiters-hotline | 0.8 | yearly | recruiter interview tips |
| Salary to Hourly Calculator | /salary-to-hourly-calculator | 0.8 | yearly | salary to hourly calculator |
| Try | /try | 0.8 | yearly | try Final Round AI |
| Special Discount | /special-discount | 0.8 | weekly | Final Round AI discount |

### 1.2 通用页（main_pages sitemap 收录）

| 页面 | URL | Priority | Changefreq |
|------|-----|----------|------------|
| Explore 聚合页 | /explore | 0.9 | weekly |
| About | /about | 0.8 | weekly |
| Careers | /careers | 0.8 | weekly |
| Referral Program | /referral-program | 0.8 | weekly |
| Influencer Program | /influencer-program | 0.8 | weekly |
| Frequently Asked Questions | /frequently-asked-questions | 0.8 | yearly |
| Privacy Policy | /privacy-policy | 0.5 | yearly |
| Terms of Use | /terms-of-use | 0.5 | yearly |
| Refund Policy | /refund-policy | 0.5 | yearly |
| Media Kit | /media-kit | 0.5 | yearly |

### 1.3 `/use-cases/` 场景页（sitemap 确认，**线上无 `for-` 前缀**）

| 页面 | URL（线上实际） | Priority | 状态 |
|------|----------------|----------|------|
| Use Cases 索引 | /use-cases | 0.8 | ✅ |
| Software Engineers | /use-cases/software-engineers | 0.7 | ✅ |
| Product Managers | /use-cases/product-managers | 0.7 | ✅ |
| Consultants | /use-cases/for-consultants | 0.7 | ✅（唯一保留 `for-` 的项） |
| Data Scientists | /use-cases/data-scientists | 0.7 | ✅ |
| Finance Professionals | /use-cases/finance-professionals | 0.7 | ✅ |
| Remote Jobs | /use-cases/remote-jobs | 0.7 | ✅ |
| Enterprise | /use-cases/for-enterprise | — | ❌ 未收录 |

### 1.4 新增内容板块（sitemap 确认，此前未记录）

| 板块 | 索引页 | 子页面模式 | 规模 |
|------|--------|-----------|------|
| **面试准备 Hub** | /interview-prep | `/interview-prep/{company}-{type}` | 7+ companies × 5 types |
| **竞品对比** | — | `/compare/final-round-ai-vs-{competitor}` | 27 竞品 |
| **Tech Layoffs** | /tech-layoffs | `/tech-layoffs/{company}` | 25 家公司 |
| **面试真题库** | /interview-questions | `/interview-questions/{slug}` | 150+ 篇 |
| **薪资数据** | — | `/salary/title/{seniority}-{title}-in-{location}` | 程序化 |
| **Glossary** | /glossary | `/glossary/{term}` | 12 术语 |
| **社区** | /community/ | `/community/{c\|t}/{slug}` | 6 分类 + 40+ 主题 |
| **Articles** | — | `/articles/{slug}` | 技术/DSA 内容 |

### 1.5 Blog

| 页面 | URL | 状态 |
|------|-----|------|
| Blog 索引 | /blog | ✅ |
| Blog 文章 | /blog/{slug} | ✅（10 篇 draft + 50+ 程序化页） |
| Cover Letters 分类 | /category/cover-letters | ✅ |

### 1.6 仅规划（sitemap 未收录）

| 页面 | URL | 备注 |
|------|-----|------|
| Internships Hub | /internships | 📋 |
| 公司实习指南 | /internships/{company-slug} | 📋 |
| Getting Started | /getting-started | ⚠️ 可能存在但不在 main_pages sitemap |
| Download | /download | ⚠️ 同上 |
| Subscription | /subscription | ⚠️ 同上 |
| FAQ | /faq | ⚠️ 可能 301→/frequently-asked-questions |
| Contact | /contact | ⚠️ 同上 |
| Scholarship | /scholarship | ⚠️ 同上 |
| Interview Copilot 子路径 | /interview-copilot/{zoom\|coding\|...} | 📋 规划的嵌套页 |
| AI Mock Interview 子路径 | /ai-mock-interview/{coding\|hirevue} | 📋 同上 |

---

## 二、`/use-cases/` 场景页：关键词速查

> **线上 URL 已确认**（sitemap main_pages）。注意线上**无 `for-` 前缀**，仅 `/use-cases/for-consultants` 例外。

| 路径（线上实际） | 主关键词（英文） | 次要关键词 |
|------|--------------------------|------------|
| /use-cases/software-engineers | software engineer interview AI, coding interview help | system design interview, technical interview AI |
| /use-cases/product-managers | product manager interview prep, PM interview AI | product sense interview, behavioral interview PM |
| /use-cases/for-consultants | case interview AI, consulting interview prep | MBB interview prep, consulting case interview |
| /use-cases/data-scientists | data science interview prep, ML interview AI | statistics interview, data scientist mock interview |
| /use-cases/finance-professionals | finance interview prep, investment banking interview AI | banking technical interview, finance case interview |
| /use-cases/remote-jobs | remote interview AI, Zoom interview assistant | Google Meet interview help, HireVue prep |

---

## 三、待拓展路径（功能 × 关键词）

> 与 [finalround-features.md](./finalround-features.md) §七 逻辑一致；**示例 URL 以本表为执行清单**。新增路径时同步 [finalround-keywords.md](./finalround-keywords.md)。

| 功能 | 拓展维度 | 待建场景 | 示例 URL | 目标关键词 |
|------|----------|----------|----------|------------|
| Interview Copilot | 平台 | Zoom 面试 | /interview-copilot/zoom | real-time interview help Zoom |
| Interview Copilot | 平台 | Google Meet 面试 | /interview-copilot/google-meet | AI interview help Google Meet |
| Interview Copilot | 面试类型 | 编码面试 | /interview-copilot/coding | coding interview copilot |
| Interview Copilot | 面试类型 | 技术面试 | /interview-copilot/technical | technical interview AI |
| Interview Copilot | 技术平台 | LeetCode | /interview-copilot/leetcode | AI interview LeetCode |
| Interview Copilot | 行业 | 科技岗 | /interview-copilot/tech | AI interview for tech |
| AI Mock Interview | 面试类型 | 编码 Mock | /ai-mock-interview/coding | AI mock interview for coding |
| AI Mock Interview | 平台 | HireVue Mock | /ai-mock-interview/hirevue | HireVue interview prep |
| AI Resume Builder | 功能页 | 简历优化 | /resume-builder | AI resume builder |
| AI Job Hunter | 功能页 | 自动投递 | /job-hunter | AI job hunter, auto apply |
| Phone Interview | 设备 | 手机端 Copilot | /phone-interview | phone interview AI, phone interview copilot |

---

## 四、use-cases 场景落地页文案（英文，可粘贴建站）

> **产品映射**：实时面试 → **Interview Copilot**；练习与复盘 → **AI Mock Interview**、Interview Report；投递与简历 → **AI Job Hunter**、**AI Resume Builder**（按需提及）。

### 4.1 `/use-cases/software-engineers`

**页面定位（中文）**：软件工程师技术面试（算法、编码、系统设计、行为面）—强调 LeetCode/CodeSignal 类场景与实时解题辅助。

**H1**：Ace Your Software Engineering Interviews With Real-Time AI Help

**Subhead**：From live coding rounds to system design and behavioral screens—get structured answers in seconds, tailored to your stack and resume.

**Body**

Whether you are interviewing for backend, frontend, full-stack, or infrastructure roles, engineering interviews move fast. You need to explain trade-offs, write correct code under time pressure, and walk through system design without rambling.

**Final Round AI for software engineers** helps you:

- **During live technical interviews** — Interview Copilot listens to the question and surfaces concise talking points, pseudocode, and structure so you stay clear when nerves kick in.
- **Coding and take-home style rounds** — Get help framing your approach before you dive into implementation (Big-O, edge cases, test ideas).
- **System design** — Organize your answer around scalability, data stores, APIs, and failure modes instead of jumping around.
- **Behavioral and “tell me about a time”** — Turn your experience into tight STAR-style responses that still sound like you.

Practice between rounds with **AI Mock Interview**, then review **Interview Report** to see what was asked and how to tighten your answers next time. Your content is grounded in **your resume and job description** so suggestions fit the role you are actually interviewing for.

**Closing CTA line**：Ship confident answers in every round—live, invisible assistance when it counts.

---

### 4.2 `/use-cases/product-managers`

**页面定位（中文）**：产品经理面试—产品 sense、度量、利益相关方、案例式产品题、行为与领导力故事。

**H1**：Interview Like a PM—Structured Answers for Product Manager Rounds

**Subhead**：Product sense, metrics, prioritization, and stakeholder scenarios—answered clearly when interviewers expect crisp thinking.

**Body**

PM interviews reward clarity: you must diagnose problems, propose frameworks, and defend trade-offs without drowning in detail. Whether the format is hypothetical product design, execution deep-dives, or behavioral leadership questions, rambling costs you the round.

**Final Round AI for product managers** helps you:

- **Product sense and “design X” prompts** — Outline user segments, goals, success metrics, and a phased roadmap in a logical order.
- **Metrics and prioritization** — Structure answers around north-star metrics, guardrails, and how you would validate assumptions.
- **Execution and stakeholder questions** — Communicate trade-offs with engineering, design, sales, and leadership in a calm, executive tone.
- **Behavioral and cross-functional stories** — Compress messy real projects into memorable narratives that highlight judgment and outcomes.

Use **Interview Copilot** during live video interviews for real-time structure, and **AI Mock Interview** to rehearse common PM patterns until your defaults feel natural. Post-interview feedback helps you refine how you open, frame, and close each answer.

**Closing CTA line**：Sound like the PM who can own ambiguity—and still land the message.

---

### 4.3 `/use-cases/for-consultants`

**页面定位（中文）**：咨询案例面试—框架、心算、图表解读、行为与 fit；强调 case 节奏与结构化输出。

**H1**：Case Interviews, Done With Structure—Consulting Interview Prep With AI

**Subhead**：McKinsey-, BCG-, Bain-style cases demand speed and frameworks. Get live support to stay organized without losing the thread.

**Body**

Consulting interviews are a different sport: market sizing, profitability, M&A, and growth cases all expect a clear issue tree, hypothesis-driven thinking, and clean math checks. Under pressure, it is easy to skip clarifying questions or mix up the storyline.

**Final Round AI for consultants** helps you:

- **Opening and clarifying** — Lock the client objective, scope, and constraints before you charge into analysis.
- **Frameworks without sounding robotic** — Lay out buckets that fit the case (revenue/cost, 3Cs, profitability tree) and adapt as new data appears.
- **Quant and sanity checks** — Walk through assumptions step by step so your numbers hold up in follow-ups.
- **Synthesis and recommendation** — Close with a CEO-level answer: recommendation, risks, and next steps.

**Interview Copilot** runs invisibly during live video interviews so you can keep pace with the interviewer’s prompts. Between sessions, **AI Mock Interview** lets you drill case narration until your default structure is automatic.

**Closing CTA line**：Keep your storyline tight from “clarify” to “recommend”—even when the case twists.

---

### 4.4 `/use-cases/data-scientists`

**页面定位（中文）**：数据科学家/ML 岗—统计与实验、建模思路、SQL/案例、与工程师协作的行为面。

**H1**：Data Science & ML Interviews—Clear Thinking, Live and Under Pressure

**Subhead**：From experimentation and modeling trade-offs to SQL-style drills and stakeholder communication—stay structured when the bar is technical *and* ambiguous.

**Body**

Data science interviews blend statistics, machine learning intuition, coding, and product judgment. You might be asked to design an experiment, compare models, debug a metric, or explain how you would partner with engineering—often in the same loop.

**Final Round AI for data scientists** helps you:

- **Experimentation and causal thinking** — Frame hypotheses, metrics, power, and pitfalls (selection bias, peeking, Simpson’s paradox) in interview-sized chunks.
- **Modeling and ML design** — Compare algorithms, features, offline vs online evaluation, and when simplicity beats complexity.
- **SQL and analytical storytelling** — Organize your approach before you write or narrate a query; highlight joins, filters, and edge cases.
- **Behavioral and cross-functional** — Explain how you influenced decisions with data without getting lost in notebook-level detail.

**Interview Copilot** supports you in live rounds; **AI Mock Interview** helps you rehearse how you *open* and *close* answers so hiring managers hear judgment, not jargon.

**Closing CTA line**：Make your rigor obvious—without burying the takeaway.

---

### 4.5 `/use-cases/finance-professionals`

**页面定位（中文）**：金融/投行/PE 相关面试—技术题、市场与交易 sense、案例与行为、高压表达。

**H1**：Finance Interviews—Stay Sharp on Technicals, Cases, and Behavioral Fit

**Subhead**：Banking, markets, and investing interviews reward precision. Get real-time structure for technical drills, short cases, and “why this firm” moments.

**Body**

Finance recruiting often stacks technical questions, market awareness, mini-cases, and intense behavioral screens in a single process. Small slips in definitions, order of operations, or storyline can derail an otherwise strong profile.

**Final Round AI for finance professionals** helps you:

- **Technical refresh** — Keep answers to valuation, accounting links, markets, and classic IB/PE prompts tight and correctly sequenced.
- **Short cases and market questions** — Organize drivers (macro, company-specific, sentiment) before you commit to a view.
- **Behavioral and “walk me through your resume”** — Connect your experience to the desk or team you are targeting.
- **Stress and follow-ups** — Stay composed when interviewers push on assumptions; re-anchor to your thesis calmly.

Use **Interview Copilot** when you need live, invisible assistance on video calls; use **AI Mock Interview** to rehearse pacing and polish between superdays and phone screens.

**Closing CTA line**：Sound prepared for the technicals—and credible on the narrative.

---

### 4.6 `/use-cases/remote-jobs`

**页面定位（中文）**：远程岗位面试—Zoom/Google Meet/Teams、异步视频、跨时区与表达清晰度；跨角色通用。

**H1**：Remote Job Interviews—Real-Time AI Help for Zoom, Meet, and Teams

**Subhead**：When you are on camera from home, every pause feels louder. Get structured answers in seconds—100% invisible on screen share.

**Body**

Remote interviews add friction: lag, bad audio, panel formats, and one-way video (HireVue-style) recordings. You still need to sound confident, structured, and authentic—without staring at notes or freezing when a question shifts.

**Final Round AI for remote jobs** helps you:

- **Live video interviews** — Interview Copilot works alongside Zoom, Google Meet, Microsoft Teams, and common browser-based tools so you can keep eye contact with the panel while support stays off-camera and undetectable on screen share.
- **One-way and async video** — Practice and real-time assistance for recorded prompts where timing and clarity matter as much as content.
- **Cross-time-zone fatigue** — Lean on structured defaults when you are interviewing early morning or late night in your time zone.
- **Any role, any industry** — The same workflow supports technical, behavioral, and case-style questions; content personalizes from your resume and job posting.

Pair live assistance with **AI Mock Interview** to rehearse in the same environment you will use on interview day—headset, lighting, and tab discipline included.

**Closing CTA line**：Make remote your advantage—clear answers, natural delivery, no visible crutches.

---

### 4.7 `/use-cases/for-enterprise`（⚠️ sitemap 未收录，线上可能未上线或路径不同）

**页面定位（中文）**：大型非科技雇主、传统企业、泛职能岗—行为与情景面、胜任力模型、小组/多轮业务面占比较高。

**H1**：Enterprise Job Interviews—Behavioral and Competency Rounds, Handled With Confidence

**Subhead**：Fortune 500 and corporate hiring still run on structured behavioral screens, situational judgment, and panel-style loops. Get STAR-ready answers in real time—aligned to your resume.

**Body**

Enterprise interviews rarely look like FAANG coding loops. You will face competency frameworks, “tell me about a time” prompts, conflict and leadership scenarios, and cross-functional panels that reward polish and consistency over puzzle speed.

**Final Round AI for enterprise candidates** helps you:

- **Behavioral and STAR prompts** — Turn scattered experience into clear situation–action–result arcs that still sound human.
- **Situational and judgment questions** — Organize trade-offs, stakeholders, and ethics before you commit to an answer.
- **Panel and marathon days** — Keep energy and structure across back-to-back rounds without rambling.
- **Role-specific narratives** — Ground answers in your résumé and the job description so you match the level of the role (IC vs. manager track).

Use **AI Mock Interview** to rehearse until your defaults feel natural; use **Interview Copilot** when you need invisible, real-time structure on live video calls—even if the format is formal and buttoned-up.

**Closing CTA line**：Sound executive-ready in every competency round—not memorized, just unmistakably prepared.

---

## 五、内链树（2026-05-12 sitemap 对账后）

以下为主站结构；博客与外部页面应回链至对应功能页或 **`/use-cases/`** 场景页。标注与 §一、§〇.1 一致。

```
/（首页）✅
├── /explore ✅（聚合发现页，priority 0.9）
│
├── 核心面试产品
│   ├── /interview-copilot ✅
│   ├── /ai-mock-interview ✅
│   ├── /general-interview ✅
│   ├── /coding-copilot ✅
│   ├── /hirevue ✅
│   ├── /phone-interview ✅
│   ├── /interview-notes ✅
│   └── /qa-pairs ✅
│
├── 简历与求职工具
│   ├── /ai-resume-builder ✅
│   ├── /ai-job-hunter ✅
│   ├── /auto-apply ✅
│   ├── /cover-letter-generator ✅
│   ├── /linkedin-profile-optimizer ✅
│   ├── /linkedin-resume-builder ✅
│   ├── /resume-checker ✅
│   ├── /career-coach ✅
│   ├── /recruiters-hotline ✅
│   └── /salary-to-hourly-calculator ✅
│
├── 转化
│   ├── /try ✅
│   └── /special-discount ✅
│
├── Use Cases（无 `for-` 前缀）
│   ├── /use-cases ✅（索引）
│   ├── /use-cases/software-engineers ✅
│   ├── /use-cases/product-managers ✅
│   ├── /use-cases/for-consultants ✅
│   ├── /use-cases/data-scientists ✅
│   ├── /use-cases/finance-professionals ✅
│   └── /use-cases/remote-jobs ✅
│
├── 内容板块
│   ├── /blog ✅ → /blog/{slug}（10 draft + 程序化）
│   ├── /interview-prep ✅ → /interview-prep/{company}-{type}
│   ├── /interview-questions ✅ → /interview-questions/{slug}（150+）
│   ├── /glossary ✅ → /glossary/{term}（12 术语）
│   ├── /articles/{slug} ✅
│   └── /guide ✅
│
├── 竞品对比
│   └── /compare/final-round-ai-vs-{competitor} ✅（27 竞品）
│
├── 行业趋势
│   └── /tech-layoffs ✅ → /tech-layoffs/{company}（25 家）
│
├── 薪资数据
│   └── /salary/title/{seniority}-{title}-in-{location} ✅（程序化）
│
├── 社区
│   └── /community/ ✅ → /community/{c|t}/{slug}（Discourse）
│
├── 通用
│   ├── /about ✅
│   ├── /careers ✅
│   ├── /referral-program ✅
│   ├── /influencer-program ✅
│   ├── /media-kit ✅
│   ├── /frequently-asked-questions ✅
│   ├── /privacy-policy ✅
│   ├── /terms-of-use ✅
│   └── /refund-policy ✅
│
└── [规划] 📋
    ├── /internships → /internships/{company-slug}
    ├── /interview-copilot/{zoom|coding|...}
    └── /ai-mock-interview/{coding|hirevue}
```

*勿在 [finalround-use-cases.md](./finalround-use-cases.md) 再维护一份同构 URL 表。*

---

## 六、线上 URL 全量清单（2026-05-12 sitemap 对账完毕）

> **数据来源**：用户直接提供 sitemap index（15 个子 sitemap）+ main_pages（50 条）+ interview_questions（150+ 条）+ tech_layoffs（25 条）+ compare（27 条）+ salary（程序化）+ interview_prep（26 条）+ glossary（12+1 条）+ community（~45 条）。**robots.txt** 待补。

### 6.1 Sitemap Index 结构

| # | 子 Sitemap | 条目数 | 说明 |
|---|-----------|--------|------|
| 1 | `main_pages` | 50 | 核心产品 + 功能 + 通用 + use-cases + 转化 |
| 2 | `interview_questions` | 150+ | 面试真题逐题页（`/interview-questions/{slug}`） |
| 3 | `interview_question_categories` | 待确认 | 题目分类页 |
| 4 | `compare` | 27 | 竞品对比（`/compare/final-round-ai-vs-{competitor}`） |
| 5 | `companies` | 待确认 | 公司专项页 |
| 6 | `blog_categories` | 待确认 | Blog 分类归档 |
| 7 | `blog` | 待确认 | Blog 文章（含 draft + 程序化） |
| 8 | `authors` | 待确认 | 作者归档页 |
| 9 | `language` | 待确认 | 多语言页（含 `/zh` 等） |
| 10 | `salary` | 大量 | 薪资程序化页（`/salary/title/{seniority}-{title}-in-{location}`） |
| 11 | `articles` | 待确认 | 技术/DSA 文章 |
| 12 | `interview_prep` | 26 | 面试准备 Hub（`/interview-prep/{company}-{type}`） |
| 13 | `glossary` | 13 | Glossary 术语（`/glossary/{term}`） |
| 14 | `community` | ~45 | Discourse 社区（`/community/{c\|t}/{slug}`） |
| 15 | `tech_layoffs` | 146 | 裁员追踪（`/tech-layoffs/{company}`） |

### 6.2 main_pages 完整清单（50 条，按 priority 排序）

| # | URL | Priority | Changefreq | 此前记录 |
|---|-----|----------|------------|----------|
| 1 | `/` | 1 | monthly | ✅ |
| 2 | `/explore` | 0.9 | weekly | ❌→✅ 新增 |
| 3 | `/ai-mock-interview` | 0.8 | weekly | ✅ |
| 4 | `/interview-copilot` | 0.8 | weekly | ✅ |
| 5 | `/general-interview` | 0.8 | weekly | ❌ 新增 |
| 6 | `/ai-resume-builder` | 0.8 | weekly | ❌ 新增 |
| 7 | `/referral-program` | 0.8 | weekly | ✅ |
| 8 | `/influencer-program` | 0.8 | weekly | ✅ |
| 9 | `/special-discount` | 0.8 | weekly | ❌ 新增 |
| 10 | `/about` | 0.8 | weekly | ✅ |
| 11 | `/careers` | 0.8 | weekly | ✅ |
| 12 | `/interview-prep` | 0.8 | weekly | ❌ 新增 |
| 13 | `/use-cases` | 0.8 | weekly | ❌ 新增 |
| 14 | `/career-coach` | 0.8 | yearly | ❌ 新增 |
| 15 | `/recruiters-hotline` | 0.8 | yearly | ❌ 新增 |
| 16 | `/cover-letter-generator` | 0.8 | yearly | ❌ 新增 |
| 17 | `/linkedin-profile-optimizer` | 0.8 | yearly | ❌ 新增 |
| 18 | `/linkedin-resume-builder` | 0.8 | yearly | ❌ 新增 |
| 19 | `/resume-checker` | 0.8 | yearly | ❌ 新增 |
| 20 | `/hirevue` | 0.8 | yearly | ✅ |
| 21 | `/phone-interview` | 0.8 | yearly | ✅ |
| 22 | `/try` | 0.8 | yearly | ❌ 新增 |
| 23 | `/auto-apply` | 0.8 | yearly | ❌ 新增 |
| 24 | `/qa-pairs` | 0.8 | yearly | ✅ |
| 25 | `/interview-notes` | 0.8 | yearly | ❌ 新增 |
| 26 | `/coding-copilot` | 0.8 | yearly | ❌ 新增 |
| 27 | `/ai-job-hunter` | 0.8 | yearly | ❌ 新增 |
| 28 | `/frequently-asked-questions` | 0.8 | yearly | ✅ |
| 29 | `/salary-to-hourly-calculator` | 0.8 | yearly | ❌ 新增 |
| 30 | `/media-kit` | 0.5 | yearly | ❌ 新增 |
| 31 | `/terms-of-use` | 0.5 | yearly | ✅ |
| 32 | `/privacy-policy` | 0.5 | yearly | ✅ |
| 33 | `/refund-policy` | 0.5 | yearly | ❌ 新增 |
| 34 | `/use-cases/software-engineers` | 0.7 | weekly | ❌（路径无 `for-`） |
| 35 | `/use-cases/product-managers` | 0.7 | weekly | ❌（路径无 `for-`） |
| 36 | `/use-cases/for-consultants` | 0.7 | weekly | ⚠️（仅此项保留 `for-`） |
| 37 | `/use-cases/data-scientists` | 0.7 | weekly | ❌（路径无 `for-`） |
| 38 | `/use-cases/finance-professionals` | 0.7 | weekly | ❌（路径无 `for-`） |
| 39 | `/use-cases/remote-jobs` | 0.7 | weekly | ❌（路径无 `for-`） |

**未在 main_pages sitemap 出现的已知页面**：`/getting-started`、`/download`、`/subscription`、`/subscription-simple`、`/faq`、`/contact`、`/scholarship`、`/zh` — 可能被 noindex、JS 渲染、或在其他 sitemap（如 language）中。

### 6.3 compare — 竞品对比（27 条）

所有对比页使用统一模式 `/compare/final-round-ai-vs-{competitor}`（**非**之前规划的 `/{competitor}-vs-final-round`）：

AlgoMonster、Exponent、HireVue、Interview Cake、Formation、Simple Programming、Scaler、Interview Kickstart、Careerflow、Paradox AI、Cluely、Interview Coder、Interviews Chat、LockedIn AI、Parakeet AI、Sensei AI、Ultracode、Verve AI、Pramp、interviewing.io、Theresanaiforthat、OfferGoose、Interview Hammer、Teal HQ、Kickresume、Jobscan、Arytic、Interview Copilot AI

> 全部 priority 0.8、changefreq yearly。详细竞品分析见 [finalround-competitors.md](./finalround-competitors.md)；Review 程序化规范见 [finalround-blog-article skill](./skills/finalround-blog-article/references/review-programmatic.md)。

### 6.4 tech_layoffs — 裁员追踪（146 家公司）

| 索引页 | 子页面 |
|--------|----------------|
| `/tech-layoffs` (daily, 0.8) | 146 家公司详情页 `/tech-layoffs/{company}` (weekly, 0.7)，覆盖科技、金融、咨询、制药、零售等行业 |

> 主站仅 Rewrite `/tech-layoffs` 路径至独立 Vercel 子站（`finalround-nextjs.vercel.app`）。运营手册见 [tech-layoffs/README.md](./tech-layoffs/README.md)。

### 6.5 interview_prep — 面试准备 Hub（26 条）

索引页 `/interview-prep` (weekly, 0.8)。子页模式 `/interview-prep/{company}-{type}`（weekly, 0.7）：

| 公司 | 覆盖题型 |
|------|----------|
| Google | system-design、behavioral、tell-me-about-yourself、strengths、teamwork |
| Meta | system-design、behavioral、tell-me-about-yourself、strengths、teamwork |
| Uber | system-design、behavioral、tell-me-about-yourself、strengths、teamwork |
| LinkedIn | behavioral、tell-me-about-yourself、strengths |
| Nvidia | system-design、behavioral、tell-me-about-yourself |
| Apple | behavioral、tell-me-about-yourself |
| Amazon | behavioral、system-design、tell-me-about-yourself |

### 6.6 interview_questions — 面试真题库

索引页 `/interview-questions` (weekly, priority 1)。150+ 篇真题逐题页 `/interview-questions/{slug}` (monthly, 0.8)，示例：
- `/interview-questions/google-pm-product-preference`
- `/interview-questions/meta-coding-interview-array`
- `/interview-questions/amazon-behavioral-customer-needs`
- 覆盖 Google、Meta、Amazon、Microsoft、Apple、Netflix、Stripe、DoorDash、Uber、Lyft、LinkedIn、TikTok、JPMorgan 等公司

### 6.7 glossary（13 条）

索引页 `/glossary` (weekly, 0.8)。术语页 (weekly, 0.7)：
AI Interview Assistant、AI Mock Interview、Behavioral Interview、Case Interview、Coding Interview、Competency-Based Interview、HireVue Interview Help、AI Interview Copilot、Real-Time Interview Help、STAR Method、System Design Interview、Technical Interview

### 6.8 community — Discourse 社区（~45 条）

路径模式 `/community/` (weekly, 0.8)：
- 分类 `/community/c/{slug}/{id}`：general/4、interview-prep/5、product-feedback/8、resume-career/6、site-feedback/2、success-stories/7
- 主题 `/community/t/{slug}/{id}`：40+ 篇（Amazon LP 行为面、ATS 简历格式、STAR 方法结构、薪资谈判等）

> 与 [finalround-community-forum.md](./community/finalround-community-forum.md) 方案对比：实际采用了 `/community/` 子路径（非子域），平台为 Discourse。

### 6.9 salary — 薪资数据（程序化）

模式 `/salary/title/{seniority}-{title}-in-{location}` (yearly, 0.8)：
- 职级维度：entry-level、average、senior、staff、principal
- 职位示例：aerospace-engineer、computer-engineer
- 地区示例：boston、california、florida、houston、los-angeles、massachusetts、michigan、new-york、ohio、san-francisco、seattle、texas、the-united-states

### 6.10 子域名

| 子域名 | 用途 |
|--------|------|
| `app.finalroundai.com` | Web 应用 |
| `accounts.finalroundai.com/sign-in` | 登录 |
| `accounts.finalroundai.com/sign-up` | 注册 |

### 6.11 待补项

- [ ] `robots.txt` 内容（Allow/Disallow/Sitemap 声明）
- [ ] `interview_question_categories` 子 sitemap 内容
- [ ] `companies` 子 sitemap 内容
- [ ] `blog_categories` 子 sitemap 内容
- [ ] `blog` 子 sitemap 条目数
- [ ] `authors` 子 sitemap 内容
- [ ] `language` 子 sitemap 内容（含 `/zh` 等）
- [ ] `articles` 子 sitemap 条目数
- [ ] `/getting-started`、`/download`、`/subscription` 等未在 main_pages 出现的原因（noindex? JS 渲染? 其他 sitemap?）
- [ ] `/use-cases/for-enterprise` 线上是否存在（main_pages sitemap 未收录）

---

## 七、维护清单

- [x] **sitemap 对账**（已完成 2026-05-12）：main_pages 50 条 + compare 27 + tech_layoffs 26 + interview_prep 26 + glossary 13 + community ~45 + interview_questions 150+ + salary 程序化已写入 §六。  
- [ ] **补完剩余子 sitemap**：blog、blog_categories、authors、language、articles、companies、interview_question_categories — 用户提供后补入 §6.1 和 §6.11。  
- [ ] **robots.txt 补录**：从浏览器获取 `https://www.finalroundai.com/robots.txt`，摘录 Allow/Disallow/Sitemap 行填入 §六。  
- [ ] **use-cases 路径修正**：文档中 `for-` 前缀需批量修正为线上实际路径（§二、§四、[internal-external-links-checklist.md](./technical/internal-external-links-checklist.md)、[finalround-keywords.md](./finalround-keywords.md)）。  
- [ ] **竞品对比路径修正**：[internal-external-links-checklist.md](./technical/internal-external-links-checklist.md) 中 `/{competitor}-vs-final-round` → `/compare/final-round-ai-vs-{competitor}`（Review 规范已随 skill 迁移同步修正）。  
- [ ] **新增页面补入关键词映射**：[finalround-keywords.md](./finalround-keywords.md) 补充 /general-interview、/coding-copilot、/ai-resume-builder 等 18 个新页面的关键词。  
- [ ] **内链规范更新**：[internal-external-links-checklist.md](./technical/internal-external-links-checklist.md) 链接分层表补入 /compare/、/tech-layoffs/、/interview-prep/、/glossary/、/community/ 等新板块。  
- [ ] 新增或变更路由后，更新 **§〇～§三** 与 **§五** 内链树。  
- [ ] 场景落地文案变更时，更新 **§四**（并与实际上线 Title/H1 对齐）。  
- [ ] [finalround-keywords.md](./finalround-keywords.md) 中「目标页」列与 **§一、§二** 一致。  
- [ ] **Internships**：上线后更新 §〇.1、§一、§五、§六。

**Last updated**: 2026-05-12（sitemap.xml 全量对账完毕：15 子 sitemap 覆盖，§〇～§七 全面重写。核心发现：/explore 确认上线、use-cases 无 `for-` 前缀、/compare/ 目录模式而非根路径 vs、/community/ 子路径 Discourse 已上线、新增 18 个 core page、/tech-layoffs/ 25家、/interview-prep/ 7公司×5题型、/glossary/ 12术语、/interview-questions/ 150+篇、/salary/title/ 程序化页）
