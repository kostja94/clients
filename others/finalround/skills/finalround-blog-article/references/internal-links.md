# FinalRound Internal Links（Skill reference）

> **内链规则 + 锚文本标准。** Phase 3 / 3.5 / 5 加载。
> **SSOT**：`technical/internal-external-links-checklist.md`（全站规则）。本文件为创作速查。

---

## 1. 链接分层

| 类型 | 路径 / URL | 用途 |
|------|------------|------|
| **Blog 互链** | `/blog/{slug}` | 同主题/意图分流；不要在正文拼裸域名 |
| **核心产品入口** | `/interview-copilot`、`/ai-mock-interview` | 实时 Copilot、练习面试；**信息性**产品入口可链 |
| **平台与形式** | `/hirevue`、`/phone-interview` | HireVue/异步视频、电话面语境 |
| **人物与行业场景** | `/use-cases/software-engineers`、`/use-cases/product-managers`、`/use-cases/for-consultants`、`/use-cases/data-scientists`、`/use-cases/finance-professionals`、`/use-cases/remote-jobs` | 固定前缀 `/use-cases/`；无 `for-` 前缀（仅 consultants 例外）；与稿内受众一致时链 |
| **简历与求职工具** | `/ai-resume-builder`、`/ai-job-hunter`、`/auto-apply`、`/cover-letter-generator`、`/linkedin-profile-optimizer`、`/linkedin-resume-builder`、`/resume-checker`、`/career-coach` | 全流程叙事；按需 |
| **补充产品入口** | `/general-interview`、`/coding-copilot`、`/interview-notes`、`/qa-pairs`、`/salary-to-hourly-calculator`、`/recruiters-hotline` | 有页再链 |
| **对比与信任** | `/compare/final-round-ai-vs-{competitor}` | 27 竞品；评测/对比稿 |
| **面试准备 Hub** | `/interview-prep`、`/interview-prep/{company}-{type}` | 公司 × 题型程序化页 |
| **裁员追踪** | `/tech-layoffs`、`/tech-layoffs/{company}` | 25 家公司 |
| **面试真题** | `/interview-questions`、`/interview-questions/{slug}` | 150+ 篇 |
| **Glossary** | `/glossary`、`/glossary/{term}` | 12 术语 |
| **社区** | `/community/`、`/community/c/{slug}`、`/community/t/{slug}` | Discourse 论坛 |

> **⚠️ 转化类路径（正文禁链）**：`/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount` —— **不在正文内链**。转化由**独立按钮/CTA block**承载（2026-08-11 决策）。正文中如必须提及，用纯文本（如 "the desktop app"、"see plans"）不包链接。

---

## 2. Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **首段或第二段** | ≥1 条 | 相关 `/blog/{slug}` 意图分流，或核心产品（`/interview-copilot`）/ 与标题强相关的 use-case |
| **Body Blog 互链** | 每篇 **1–4 条** | 链至 `/blog/{slug}`；对比/评测类可额外链至站内 vs / alternatives 若已发布 |
| **产品 / 信息内链** | 按节分布 | `/interview-copilot`、`/ai-mock-interview` 宜落在不同 H2；同一 URL 全文各段落至多 1 次为主 |
| **use-cases 内链** | 与读者角色一致时 | 如 SWE 稿 → `/use-cases/software-engineers`；远程稿 → `/use-cases/remote-jobs`；未上线不链 |
| **文末 Next steps（可选）** | 2–6 条 | 至少含 1 条 blog + 1 条产品/场景页 |
| **frontmatter `related`** | **2026-08-11 起移除** | frontmatter 不含 `related`/`image`/`keywords`；互链以正文为准 |
| **锚文本** | 描述性 | 避免 click here / learn more 单独成锚 |
| **转化链接** | **正文禁链** | `/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount` 不出现在正文内链；由独立按钮承载 |

---

## 3. External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威 / 数据** | 2–6 条（视篇幅） | 劳动统计、教育/科技媒体、可核对数据；句内或脚注标明出处 |
| **竞品 / 对比对象** | 评测/对比稿必备 | `rel="nofollow noopener"`；锚文本用公司名/产品名 |
| **E-E-A-T** | 可验证 | 定价、功能以官网 + 成稿日期为据；避免不可证实的绝对化表述 |
| **招聘市场 / 新闻** | 行业稿 | 裁员、招聘趋势可引 Reuters、BLS、公司公告等 |

**常用权威外链**：
- U.S. Department of Labor [CareerOneStop](https://www.careeronestop.org/ToolKit/Interview/default.aspx)
- U.S. Department of Labor [Job interview tips](https://www.dol.gov/general/jobs/interview-tips)
- SHRM [talent acquisition](https://www.shrm.org/resourcesandtools/hr-topics/talent-acquisition/pages/default.aspx)
- FTC [job scams](https://www.consumer.ftc.gov/articles/0362-job-scams)
- NACE [career readiness competencies](https://www.naceweb.org/career-readiness-competencies)
- Google [helpful content principles](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

---

## 4. 内链红线（FinalRound 特有）

- 禁链 `/zh`（中文站）
- 禁链未上线路径（`/internships`、`/use-cases/for-enterprise` 等，见 project-config §2）
- **禁链转化路径**（`/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount`）——转化由独立按钮承载
- 评测稿内链 → `/compare/final-round-ai-vs-{competitor}`（线上实际路径，非 `/{competitor}-vs-final-round`）
- use-cases 路径无 `for-` 前缀（仅 `/use-cases/for-consultants` 例外）

---

*internal-links · FinalRound · v1.0.0*
