# AiPPT — 增长策略

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)
> **本文档职责**：增长渠道、内容策略、实验方向、SEO/GEO 建议。  
> **引用**：[aippt.md](./aippt.md) 概览 | [aippt-keywords.md](./aippt-keywords.md) 关键词 | [aippt-site-structure.md](./aippt-site-structure.md) 站点结构 | [aippt-competitors.md](./aippt-competitors.md) 竞品

**最近更新**：2026-05-19

---

## 一、增长渠道全景

| 渠道 | 现状 | 机会 |
|------|------|------|
| **自然搜索（SEO）** | 品牌词可搜到；品类长尾词覆盖度待评估 | **高优先级**：功能页、场景页、vs 对比页、模板索引页 |
| **PR / 媒体发稿** | 活跃：PR Newswire、MarTech Series、Manila Times 等 | 持续；可同步转化内容为自有 blog |
| **Product Hunt** | 待确认是否上线 | 高：AI 工具类核心冷启动渠道 |
| **社交媒体** | 待确认（Twitter/X、LinkedIn、YouTube、小红书等） | 产品 Demo 视频、教程、模板展示 |
| **微信生态** | 小程序 + H5（aippt.cn） | 国内市场核心 |
| **应用商店** | iOS App（3000 万+ 用户宣称）、Android App | ASO 优化（标题、关键词、截图、评分） |
| **Google Ads / SEM** | 搜索广告跑品牌词 + 品类词 | 已知 Bing Ads URL 参数（`utm_source=Bing_Ads`） |
| **联盟 / 推荐** | 待确认 | 学生推荐、企业邀请机制 |
| **合作伙伴** | 待确认 | 与 Google Workspace、Microsoft 365 生态集成 |

---

## 二、内容策略建议

### 2.1 SEO 内容体系建设（按优先级）

| 层级 | 内容类型 | 数量目标 | 说明 |
|------|----------|----------|------|
| **核心** | 功能落地页 | 5-8 页 | `/features/prompt-to-ppt`、`/features/document-to-ppt` 等 |
| **核心** | 场景页 | 5-8 页 | `/use-cases/business`、`/use-cases/education`、`/use-cases/pitch-deck` 等 |
| **核心** | 竞品对比页 | 4-6 页 | `/vs/gamma`、`/vs/beautiful-ai`、`/alternatives/` 系列 |
| **增长** | 模板分类索引 | 按行业/风格分 | 200K 模板的 SEO 长尾资产 |
| **增长** | Blog / 教程 | 2-4 篇/月 | "*How to make a pitch deck with AI*"、产品更新解读 |
| **防御** | Help/Docs 中心 | 持续 | SEO 友好的帮助文档，拦截问题类搜索 |

### 2.2 内容节奏策略

产品迭代节奏快（2026 Q1–Q2 每 2-3 周一次核心更新）。每次更新可产出：

- 1 篇功能发布 blog
- 1 个社交媒体 Demo 视频
- 1 篇 PR Newswire 通稿
- 更新 `/log-update` 页面
- 更新相关功能落地页

### 2.3 竞品截流内容

Tome 已于 2025.03 关闭——这是明确的截流窗口：

- 建设 `/alternatives/tome` 页面
- 定向 *Tome alternative*、*Tome replacement* 等搜索词
- 在社区/社媒回应 "Tome 关了用什么" 类问题

---

## 三、SEO / GEO 专项建议

### 3.1 当前 SEO 优势

- 品牌域名 aippt.com 天然包含品类关键词（"AI PPT"）
- 多语言区域子站利于本地化 SEO
- aippt.cn 覆盖中文搜索生态
- Nano Banana / GPT Image 2 等知名模型可提升内容公信力

### 3.2 SEO 待改进

| 项目 | 问题 | 建议 |
|------|------|------|
| Blog 缺失 | 内容以 PR 通稿为主，无法持续获取长尾搜索 | 建立自有 blog，每周 1-2 篇 |
| 功能页索引 | `/features/` 路径未确认存在 | 建设独立功能落地页，H1 含目标关键词 |
| Schema 标记 | 待验证 | 添加 FAQ / HowTo / Product schema |
| 模板 SEO | 200K 模板若为动态加载，搜索引擎可能无法索引 | 静态 SSR 渲染分类索引页 |
| 内链结构 | 待评估 | 功能页 ↔ 场景页 ↔ 模板页 合理互链 |
| 竞品对比页 | 缺失 | 建设 vs 系列承接竞品搜索意图 |

### 3.3 GEO（AI 搜索优化）建议

- **结构化内容**：每页清晰的 H1-H3 层级 + 摘要段落（被 AI 模型引用概率更高）
- **FAQ 模块**：在功能页和场景页嵌入 FAQ schema
- **数据引用**：使用可被事实核查的数据（如 "200,000+ templates"）
- **对比表述**：在 vs 页使用结构化表格（竞品对比矩阵），易被 LLM 提取

---

## 四、增长实验方向

| 实验 | 假设 | 指标 |
|------|------|------|
| **Tome 截流页** | Tome 关闭后搜索 *Tome alternative* 的用户可转化 | 页面访问 → 注册转化率 |
| **模板预览分享** | 用户分享模板预览链接可带来新用户 | 分享带来的注册数 |
| **免费层每日次数调整** | 2 次/天 → 3 次/天可提升留存 | 免费用户次日/7 日留存 |
| **学生验证优惠** | 学生证验证送 Pro 试用，提升学术场景渗透 | 学生注册转化率 |
| **AI PPT 质量对比视频** | YouTube/TikTok 对比 AiPPT vs Gamma 导出效果 | 视频播放 → 站内访问 |
| **微信小程序裂变** | 模板分享 + 邀请机制（aippt.cn 侧） | 小程序新增用户 |

---

## 五、指标监测建议

| 维度 | 指标 | 工具 |
|------|------|------|
| 自然搜索 | 品类词排名、品牌词搜索量、点击率 | GSC / Semrush |
| 内容效率 | 落地页访问量、跳出率、转化率 | GA4 |
| 竞品截流 | vs/alternatives 页排名与流量 | GSC |
| 注册转化 | Free → Plus/Pro 转化漏斗 | 自有分析 |
| 留存 | 免费用户次日/7 日/30 日留存 | 自有分析 |
| 区域 | 印度/菲律宾/香港/马来西亚各区域搜索量与转化 | GSC（按国家） |

---

## 六、待办

- [ ] GSC 连接与基准数据采集（当前排名、点击量、覆盖关键词）
- [ ] 竞品 SEM 投放关键词分析（Gamma、Beautiful.ai 在投什么词）
- [ ] 功能落地页排期（按搜索量优先级）
- [ ] `vs/gamma`、`alternatives/tome` 页面立项
- [ ] Blog 系统选型与首月内容日历
- [ ] 微信小程序增长策略讨论（aippt.cn 侧，需产品团队参与）
