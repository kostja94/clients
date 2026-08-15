# Oginify 竞品分析

> **本文档职责**：覆盖三类竞品——直接竞品（OG 图生成工具）、间接竞品（设计工具手动流程）、内置方案（平台自带 OG 生成）。分析差异化定位，指导产品叙事。  
> **引用**：[主文档](./oginify.md) 概览 | [features](./oginify-features.md) 产品 | [keywords](./oginify-keywords.md) 关键词 | [growth-strategy](./oginify-growth-strategy.md) 增长

---

## 竞品分类总览

| 类型 | 代表 | 威胁级别 | 应对策略 |
|------|------|----------|----------|
| **直接竞品：API/SaaS 生成工具** | Bannerbear, OG Image API, MyOG.social, RendrKit | 高 | 6 张/天免费 + 混合管线（截图+模板）+ 产品矩阵差异化 |
| **截图竞品** | Urlbox, ScreenshotOne | 中 | Above the Fold 免费无账号替代 |
| **直接竞品：AI 生成工具** | OG Herro, OG:Image.site, Ogen | 中 | 先发 + 多风格 + 完整漏斗 |
| **间接竞品：设计工具** | Canva, Figma | 低 | 速度（10 秒 vs 30 分钟）+ 零学习成本 |
| **间接竞品：开发者工具** | @vercel/og, Satori | 中 | 开源 Skills 直接竞争；SaaS 覆盖非开发者 |
| **内置方案：平台自带** | WordPress, Ghost, Vercel, GitHub | 低 | 「有内置直接用，没内置用 Oginify」 |

---

## 1. 直接竞品：API / SaaS 生成工具

### 1.1 Bannerbear

| 维度 | Bannerbear | Oginify |
|------|-----------|---------|
| **定价** | $49–299/月（按 API 量） | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| **目标用户** | 开发者、企业（API 集成） | 站长、SEOer、营销人（浏览器直接使用） |
| **生成方式** | 模板编辑 + API 调用 | 截图 + 模板渲染（主流程）+ AI Regenerate |
| **单图成本** | ~$0.049（Automate 方案） | ~$0.005（主流程），~$0.030（AI Regenerate） |
| **产品矩阵** | API + 模板编辑器 | Generator + Validator + Gallery + Skills |
| **免费额度** | 30 张一次性试用 | 6 张/天 + Above the Fold 无配额 |

**Oginify 优势**：低门槛试用、AI 内容感知、完整产品矩阵（生成 + 截图 + 校验 + 灵感）
**Oginify 劣势**：Bannerbear 有成熟 API、企业客户、视频/PDF 多格式支持

### 1.2 OG Image API

| 维度 | OG Image API | Oginify |
|------|-------------|---------|
| **定价** | Freemium（25 张/月免费） | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| **生成方式** | POST JSON → PNG（模板） | 粘贴 URL → 截图+模板（主流程）+ AI Regenerate |
| **速度** | ~65ms | ~1–2s（主流程），~5–10s（AI Regenerate）|
| **产品矩阵** | 单一 API | 完整产品矩阵 |

**Oginify 优势**：AI 感知 > JSON 模板，零代码使用，产品矩阵
**Oginify 劣势**：速度慢（AI 生成路径长），无 API（目前）

### 1.3 MyOG.social

| 维度 | MyOG.social | Oginify |
|------|------------|---------|
| **定价** | ~$20/月 | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| **方式** | 1 个 meta 标签 + 服务端自动生成 | 主动粘贴 URL 手动生成 |
| **缓存** | 7 天 CDN 缓存 | 无（用户自主下载使用） |
| **集成** | Jekyll, Next.js, WordPress | 无平台集成（面向所有网站） |

**Oginify 优势**：免费、无需 meta 标签嵌入、AI 多风格
**Oginify 劣势**：无自动缓存/更新、无平台集成

### 1.4 RendrKit

| 维度 | RendrKit | Oginify |
|------|---------|---------|
| **定价** | Free（50/mo）→ $49–149/月 | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| **模板** | 80+ 内置 | 无模板，AI 感知 |
| **开源** | 部分 | social-cards-skills 全开源 MIT |
| **定位** | Bannerbear 开源替代 | OG 图全栈产品矩阵 |

**Oginify 优势**：6 张/天免费 + Above the Fold 无配额、混合管线（截图+模板+AI）、社区属性（Build in Public + 开源）
**Oginify 劣势**：无 API、模板少

### 1.5 其他直接竞品速览

| 工具 | 定价 | 差异化 | 威胁 |
|------|------|--------|------|
| **OG Herro** | $9/月起 | AI + 品牌模板 + API | 低（付费，无产品矩阵） |
| **OG:Image.site** | $2.99/月起 | 多平台尺寸支持 | 低（付费，模板化） |
| **Ogen** | 未公开 | ChatGPT + Stable Diffusion | 低（信息不足） |
| **OG Generator Pro** | 免费 | 多框架代码导出 + meta 检查 | 中（免费 + meta checker 重叠） |
| **OpenGraphPro** | 免费 | meta 预览 + 生成合体 | 中（功能与 Validator 重叠） |

---

## 2. 间接竞品：设计工具

### 2.1 Canva / Figma

| 维度 | Canva / Figma | Oginify |
|------|--------------|---------|
| **流程** | 选模板 → 改文案 → 调样式 → 导出 PNG | 粘贴 URL → AI 生成 → 下载 |
| **时间** | 10–30 分钟 | ~10 秒 |
| **学习成本** | 中高（需设计基础） | 零 |
| **灵活性** | 极高（任意定制） | 中（AI 生成 + 6 风格库） |

**定位**：Oginify 不做设计工具，做「零操作出图」。Canva 用户要的是完全控制，Oginify 用户要的是快。

### 2.2 开发者工具：@vercel/og / Satori

| 维度 | @vercel/og / Satori | Oginify |
|------|---------------------|---------|
| **用户** | 开发者（需写代码） | 所有人（零代码） |
| **部署** | 自建 Edge Function | 直接用浏览器 |
| **维护** | 需要自己维护 | 零维护 |
| **开源 Skills** | — | social-cards-skills 基于 Satori 的上层封装 |

**定位**：@vercel/og 是底层引擎，不是竞品——social-cards-skills 构建在同类技术栈上。Oginify SaaS 覆盖不想写代码的人；Skills 覆盖想程序化出图的开发者。

---

## 3. 内置方案：平台自带 OG 生成

这些不是竞争对手，而是 Oginify 叙事的一部分——「你的平台内置了 OG 图吗？有 → 直接用。没有 → 用 Oginify」。

### 已内置 OG 生成的平台

| 平台 | 类型 | 说明 |
|------|------|------|
| Vercel | Hosting | @vercel/og，Edge + WASM 动态生成 |
| Next.js | Framework | ImageResponse API，App Router 约定文件 |
| WordPress | CMS | Jetpack Social Image Generator 插件 |
| Ghost | CMS | 内置，基于 feature image + 标题 |
| Substack | Newsletter | 自动生成含标题/作者/logo 的卡片 |
| Medium | Blog | 服务端自动渲染 OG 图 |
| GitHub | Code Host | Repo social preview，自动或手动设置 |
| Framer | No-code | 发布时自动生成 OG |
| Webflow | No-code | CMS 集合可模板化 OG |
| Notion | Docs | 公开页自动用 emoji + 标题生成 |
| Dev.to | Community | 自动生成含标题/头像/标签的卡片 |
| Hashnode | Blog | 自动动态 OG（标题+作者+品牌色） |

**Oginify 的价值**：如果用户已经在这些平台上，不需要 Oginify。但大量自建站、静态站、小众 CMS 没有内置 OG——这些是 Oginify 的目标用户。

---

## 4. 差异化定位总结

| 维度 | 竞品普遍做法 | Oginify |
|------|------------|---------|
| **定价** | 订阅制 $9–$299/月 | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| **生成方式** | 模板编辑 / JSON 配置 | 截图 + 模板渲染（主流程）+ AI Regenerate |
| **产品形态** | 单点工具（只生成） | 完整产品矩阵（生成 + 校验 + 灵感 + 开源） |
| **透明度** | 不公开内部运作 | Build in Public（成本、决策、踩坑全公开） |
| **目标用户** | 开发者 / 企业 | 所有人（重点是站长和 SEOer） |
| **开源** | 少数部分开源 | SaaS 6 张/天免费 + Skills MIT 永久免费 |

**核心叙事**：

> 其他工具按月收费，给你一个模板编辑器。Oginify 每天免费 6 张，贴 URL 就行——第 1 张截图保真，第 2 张模板渲染，不满意还能 AI Regenerate。会用命令行的还有 MIT 开源 Skills。

---

## 5. 截图竞品：Urlbox / ScreenshotOne

| 维度 | Urlbox / ScreenshotOne | Oginify Above the Fold |
|------|------------------------|------------------------|
| **定价** | 按次/API 月费 | 免费、无账号、无配额 |
| **用户** | 开发者（写代码、管 API key） | 浏览器粘贴 URL |
| **输出** | 可配置尺寸 | 固定 1200×630 OG 规格 |

---

*Last updated: 2026-05-31. 竞品定价和功能来自 2026-05-30 联网搜索，部分信息可能已有变化。每季度复查一次竞品动态。*
