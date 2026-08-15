# AiPPT — 站点结构

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)
> **本文档职责**：URL 层级、信息架构、技术栈推断。  
> **引用**：[aippt.md](./aippt.md) 概览 | [aippt-growth-strategy.md](./aippt-growth-strategy.md) 增长策略

**最近更新**：2026-05-19（初建，线上 URL 待抓取复核）

---

## 一、域名体系

| 域名 | 定位 | 语言 |
|------|------|------|
| [aippt.com](https://www.aippt.com/) | 英文主站 / 全球 | EN |
| [aippt.cn](https://www.aippt.cn/) | 中文站 | ZH |
| aippt.com/in | 印度子站（假设） | EN（本地化） |
| aippt.com/ph | 菲律宾子站（假设） | EN（本地化） |
| aippt.com/zh-hk | 香港子站 | ZH-HK |
| aippt.com/my | 马来西亚子站 | EN/BM（本地化） |

*区域子站路径格式以线上实际为准。已知 `/zh-hk/log-update`、`/ph/log-update`、`/my/log-update` 存在独立内容。*

---

## 二、导航结构（推断）

根据首页公开信息与搜索索引推断的主导航：

| 导航项 | 目标 | 状态 |
|--------|------|------|
| **Home** | `/` | 已确认 |
| **Templates** | `/templates`（假设） | 待确认（200K 模板库应存在独立入口） |
| **Features** | `/features`（假设） | 待确认 |
| **Pricing** | `/price` | 已确认 |
| **Log / Updates** | `/log-update` | 已确认 |
| **Blog** | 未知路径 | 未见公开 blog（以 PR Newswire 发稿为主） |
| **Help / Support** | 未知路径 | 待确认 |
| **Login / Sign Up** | 标准入口 | 已确认 |

---

## 三、已知 URL 清单

### 已确认路径

| 路径 | 内容 | 来源 |
|------|------|------|
| `/` | 首页 | 直接访问 |
| `/price` | 定价页 | 搜索索引 |
| `/log-update` | 功能更新日志（EN） | 搜索索引 |
| `/zh-hk/log-update` | 功能更新日志（香港繁中） | 搜索索引 |
| `/ph/log-update` | 功能更新日志（菲律宾） | 搜索索引 |
| `/my/log-update` | 功能更新日志（马来西亚） | 搜索索引 |

### 假设 / 待确认路径

| 路径 | 内容 | 优先级 |
|------|------|--------|
| `/templates` | 模板库 | 高（200K 模板需独立导航） |
| `/features` | 功能总览 | 高 |
| `/features/prompt-to-ppt` | Prompt 生成 | 中 |
| `/features/document-to-ppt` | 文档导入 | 中 |
| `/features/url-to-ppt` | URL 导入 | 中 |
| `/features/ai-image` | AI 图像生成 | 中 |
| `/features/nano-banana` | Nano Banana 模式 | 中 |
| `/use-cases` | 场景页 | 中 |
| `/use-cases/business` | 商务场景 | 中 |
| `/use-cases/education` | 教育场景 | 中 |
| `/use-cases/pitch-deck` | Pitch Deck | 低 |
| `/vs/gamma` | AiPPT vs Gamma | 中（SEO 竞品词） |
| `/vs/beautiful-ai` | AiPPT vs Beautiful.ai | 中 |
| `/alternatives/gamma` | Gamma 替代品 | 中 |
| `/alternatives/tome` | Tome 替代品 | 中 |
| `/blog` | 博客 | 低（目前以 PR 发稿为主） |
| `/download` | 桌面端/移动端下载 | 高 |
| `/login` | 登录 | 高 |
| `/signup` | 注册 | 高 |

---

## 三、技术栈推断

| 维度 | 推断 | 依据 |
|------|------|------|
| 前端框架 | React / Next.js 或 Vue | 典型 SaaS 选型；待 DevTools 确认 |
| AI 模型 | Nano Banana 2、GPT Image 2、Flux、Imagen、Seedream 4.0 | 官网公开 |
| 托管 | Cloudflare / AWS（推测） | 典型全球化 SaaS 选型 |
| 多语言 | i18n 子路径（`/zh-hk`、`/ph`、`/my`） | URL 结构 |
| 微信生态 | 小程序 + H5 | aippt.cn 国内站 |

---

## 四、内容机会

| 缺口 | 建议 | 优先级 |
|------|------|--------|
| **Blog** | 目前以 PR Newswire 媒体发稿为主，缺少自有 blog 做 SEO 长尾 | 高 |
| **功能落地页** | `/features/` 下各功能独立页可承载功能长尾词 | 高 |
| **场景页** | `/use-cases/` 下按行业/角色拆分，承接场景搜索词 | 中高 |
| **对比页** | `/vs/` 和 `/alternatives/` 承接竞品词量 | 中高 |
| **模板库索引** | 200K 模板可做分类索引页 + 搜索，强 SEO 资产 | 中 |
| **帮助中心** | 公开 URL 未确认；可优化为 SEO 友好的 docs 结构 | 中 |
| **区域本地化** | 印度/菲律宾子站的内容深度与本地化模板覆盖 | 低中 |
