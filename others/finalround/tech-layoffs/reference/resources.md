# Final Round AI — Tech Layoffs 资源参考

> 本文档汇总与 Final Round AI 相关的 Tech Layoffs 资源性内容、数据源及竞品参考。裁员规模与公司明细见 [../data/layoff-data.md](../data/layoff-data.md)。板块架构与部署说明见 [architecture.md](./architecture.md)。
> 关联：[../data/layoff-data.md](../data/layoff-data.md) | [architecture.md](./architecture.md) | [../../finalround-project-tasks.md](../../finalround-project-tasks.md) | [../../finalround.md](../../finalround.md)

**Last updated**: 2026-06-03（新增架构总览文档引用；部署 URL 更新为 finalround-nextjs.vercel.app）

---

## 背景与选型逻辑

- 裁员潮带来求职需求上升，面试准备、AI 面试助手、简历优化等产品需求增加
- 资源性内容可吸引流量、建立权威、导流至产品 CTA

---

## 1. 裁员追踪平台

| 资源 | URL | 说明 | 来源置信度 |
|------|-----|------|-----------|
| **Layoffs.fyi** | https://layoffs.fyi/ | 2020 年起；截至 2026 年 5 月中超 110,000 人、144+ 家企业；最权威公开追踪源 | ✅ 已验证 |
| **TrueUp** | https://www.trueup.io/layoffs | 裁员追踪 + 职位对接 | ✅ 已验证 |
| **Comprehensive.io** | https://comprehensive.io/ | 6,000+ 公司薪资数据（Layoffs.fyi 关联项目） | ✅ 已验证 |
| **SkillSyncer** | https://skillsyncer.com/layoffs-tracker | 裁员追踪 + 简历优化 + 申请追踪 | ⚠️ 数据口径与 Layoffs.fyi 有差异 |
| **Layoffs App** | [App Store](https://apps.apple.com/us/app/layoffs-tech-job-tracker/id6758896276) | iOS 端追踪，162+ 公司，推送通知 | ✅ 已验证 |

> ⚠️ 以下来源在文档历史版本中出现，但 2026-05 外部验证未找到有效网页或数据不明确，暂移出推荐列表：LayoffBoard、LayoffTrends、Layoffs.Careers。如需恢复，请提供有效 URL 确认。

---

## 2. 功能竞品

| 竞品 | URL | 核心功能 | 差异化 |
|------|-----|----------|--------|
| **Careerflow** | https://www.careerflow.ai/ | 简历、Job Tracker、LinkedIn、**AI Mock Interview**、Cover Letter | **直接竞品**；1M+ 用户；含 Mock Interview；OpenAI 100 亿 token 认证 |
| **Fonzi** | https://fonzi.ai/ | AI/ML 人才 curated marketplace；Match Day；技能匹配 | 高端技术人才；Lightspeed 投资 |
| **CV-BY-JD** | https://www.cv-by-jd.com/ | CV-JD 匹配、ATS 优化、一键改写 | 简历为主；裁员生存指南；定期更新裁员深度分析 |

---

## 3. 内容竞品

| 来源 | 代表文章 | 可借鉴点 |
|------|----------|----------|
| **Careerflow** | [Amazon Layoffs 2026](https://careerflow.ai/blog/amazon-layoffs-2026) | 单公司专题 + 产品 CTA；12–18 月求职周期 |
| **Fonzi** | [What to Do If You Get Laid Off](https://fonzi.ai/blog/what-to-do-if-you-get-laid-off) | 结构化 checklist；裁员前准备 |
| **CV-BY-JD** | [AI Layoff Survival Guide 2026](https://www.cv-by-jd.com/blogs/ai-layoff-survival-guide-2026~ai-layoff-survival-guide-2026) | 245K 人、28.5% AI 驱动；数据引用 |
| **CV-BY-JD** | [May 2026 Layoff Cycle](https://www.cv-by-jd.com/blogs/may-2026-layoff-cycle-meta-oracle~2121) | Meta/Oracle 深度分析；offer 撤回等细节 |
| **BSWEN** | [Tech Layoffs 2026 Survival Guide](https://docs.bswen.com/blog/2026-03-14-tech-layoff-preparation-guide/) | 六点策略；2–8 月求职周期 |

---

## 4. Final Round 自有资源页

| 资源 | URL | 用途 |
|------|-----|------|
| Tech Layoffs（对外） | https://www.finalroundai.com/tech-layoffs | 用户访问入口；主域 Rewrite → 子站 |
| Tech Layoffs（子站 origin） | https://finalround-nextjs.vercel.app/tech-layoffs | Vercel 独立部署；Kostja 本地维护 |
| Explore 聚合 | https://www.finalroundai.com/explore | 内链聚合 |

> **历史**：此前 Tech Layoffs 部署于 `finalround.lovable.app/tech-layoffs`（Lovable 平台），已于 2026-06 迁移至独立 Vercel 子域名。架构详情见 [architecture.md](./architecture.md)。

---

## 5. 2026 年科技/AI 裁员数据

> 裁员规模、公司明细（180+ 家，含科技/金融/消费品/汽车/咨询/制药/零售/亚太/欧洲/大洋洲/加拿大/拉美/中东）、行业洞察、新闻源已拆至 **[finalround-layoff-data.md](./finalround-layoff-data.md)**，专供写作引用和事实核查。

---

## 6. 内容与 SEO 建议

| 场景 | 建议 |
|------|------|
| 资源页 | tech-layoffs 模式扩展；聚合 Layoffs.fyi / TrueUp / SkillSyncer |
| 博客主题 | 单公司专题（Oracle、Block、Amazon、Meta）；Survival Guide（财务/文档/人脉/技能/公司情报/心理）；AI 替代风险与面试准备 |
| 内链 CTA | 链至 /interview-copilot、/ai-mock-interview；参考 Careerflow 单公司裁员文内链 |
| 差异化 | 竞品侧重简历/求职；Final Round 强化**面试准备**（Mock Interview、AI 面试助手） |

### 6.1 可引用数据（用于写作）

| 数据点 | 来源 | 置信度 |
|--------|------|--------|
| 2025 年 ~245K 人裁员，28.5% AI 驱动 | CV-BY-JD、RationalFX | ⚠️ 二手引用 |
| 求职周期 11–22 周 / 2–8 月 | BS WEN、Careerflow 等 | ✅ 多源一致 |
| 98% Fortune 500 使用 ATS | Jobscan 2025 | ✅ 广泛验证 |
| 78% 简历在人工查看前被过滤 | ApplyGlide / SHRM 2026 | ✅ |
| ATS 并非自动拒绝（92% 不自动拒） | ResumeAdapter 2026 调研 | ✅ |
| 关键词匹配后回复率翻三倍 | Economic Times | ⚠️ 单一来源 |
| 高危岗位：中层管理、PM、协调型 | 多来源 | ✅ 广泛共识 |
| 安全岗位：创收、AI 操作、网络安全、AI/ML | CV-BY-JD、多来源 | ⚠️ 部分二手 |

---

## 7. 文档导航

| 文档 | 用途 |
|------|------|
| [finalround-project-tasks.md](../finalround-project-tasks.md) | 项目任务 |
| [finalround-blog.md](../blog/finalround-blog.md) | Blog 策略 |
| [finalround-keywords.md](../finalround-keywords.md) | 关键词映射 |
