# Collov AI 站点结构

> **本文档职责**：URL 层级、IA 导航、技术架构；与 sitemap 对账。  
> **引用**：[collov.md](./collov.md) 产品概览 | [collov-keywords.md](./collov-keywords.md) 关键词 | [collov-migration-seo-analysis.md](./collov-migration-seo-analysis.md) 框架迁移 | [collov-features.md](./collov-features.md) 功能页

**文档导航**：→ [collov.md](./collov.md) | [collov-features.md](./collov-features.md) | [collov-use-cases.md](./collov-use-cases.md) | [collov-keywords.md](./collov-keywords.md)

---

## 一、网站概览

| 项目 | 内容 |
|------|------|
| 主站 | https://collov.ai/ |
| 应用端 | https://app.collov.ai/ |
| 母公司站 | https://www.collov.com/（Collov Labs） |
| 框架 | Next.js（部分页面 via iframe；详见 [collov-migration-seo-analysis.md](./collov-migration-seo-analysis.md)） |
| Sitemap | https://collov.ai/sitemap.xml（Screaming Frog SEO Spider 22.0 抓取） |

---

## 二、导航结构

- **AI Virtual Staging**：Multi-Angle Staging、Design Styles、Design Types
- **AI Tools**：Add Furniture、Furniture Eraser、Room Declutter、Enhance Photo Quality、Change Seasons、Cabinet AI、Flooring AI、Home Redesign、Partial Remodel、**Furniture Finder**（待建）、**Design Callout**（待建）、**Moodboard Generator**（待建）、**AI Room Score**（待建）
- **AI Vizard**：嵌入式 AI 设计工具，可集成至第三方平台（`/ai-vizard/`），详见 [collov-ai-vizard.md](./collov-ai-vizard.md)
- **AI Desk**：线下门店 AI 设计 Kiosk（`/ai-desk`）
- **Solutions / Use Cases**：Real Estate Agent、Interior Designer、Home Owner；**待拓展** Vacation Rental、Commercial、Developers、Contractors、Furniture Retail（见 [collov-solutions.md §四](./collov-solutions.md#四待拓展-solutions)、[collov-use-cases.md §四](./collov-use-cases.md#四待拓展-use-cases)）
- **Resources**：Tutorials、API、Blog、Partners、Gallery、Idea Center、MLS Partnership
- **Pricing**

---

## 三、URL 层级

### 3.1 基础页面

| 路径 | 说明 |
|------|------|
| / | 首页 |
| /pricing | 定价 |
| /login | 登录 |
| /blog | 博客 |
| /gallery | 案例展示 |
| /idea-center | 灵感中心 |
| /tutorial | 教程 |
| /earn-photos | 上传照片赚 Credits |

### 3.2 产品主线

| 路径 | 说明 |
|------|------|
| /virtual-staging | 虚拟软装主页 |
| /virtual-staging-ai | 虚拟软装 AI |
| /design-center/virtual-staging | 虚拟软装设计（旧入口） |
| /design-center/virtual-tour | 虚拟看房（旧入口） |

### 3.3 AI 工具

| 路径 | 说明 |
|------|------|
| /add-furniture | 添加家具 |
| /change-seasons | 季节/天气变换 |
| /cabinet-ai | 橱柜设计 |
| /flooring-ai | 地板可视化 |
| /furniture-ai | 家具检测 |
| /home-redesign | 全屋改造 |
| /partial-remodel | 局部改造 |
| /ai-desk | AI 设计 Kiosk |

### 3.4 AI 产品（独立）

| 路径 | 说明 | 文档 |
|------|------|------|
| /ai-vizard/ | AI Vizard 嵌入式设计工具 | [collov-ai-vizard.md](./collov-ai-vizard.md) |
| /360-panorama-generator | 360° 全景生成 | ⚠ 页面存在但未收录于 sitemap.xml |
| /ai-virtual-tour-generator | AI 虚拟看房视频 | ⚠ 未在 sitemap 中，需确认是否仍在线 |

### 3.5 Solutions / Persona

| 路径 | 受众 | 状态 |
|------|------|------|
| /real-estate | 房产经纪 | 已上线 |
| /designer | 室内设计师 | 已上线 |
| /homeowner | 业主 | 已上线 |
| /vacation-rental | 度假租赁/物业管理 | 待拓展（P0） |
| /commercial | 商业地产 | 待拓展（P1） |
| /developers | 开发商 | 待拓展（P1） |
| /contractors | 装修承包商 | 待拓展（P1） |
| /furniture-retail | 家具零售 | 待拓展（P2） |

### 3.6 设计风格（`/virtual-staging/{style}`）

7 种风格：scandinavian、modern、luxury、industrial、farmhouse、coastal、midcentury

### 3.7 房间类型（`/virtual-staging/{room}`）

11 种房间类型：living-room、bedroom、kitchen、dining-room、bathroom、kids-room、home-office、outdoor、real-estate、house、home

### 3.8 待建功能

| 路径 | 功能 | 文档 |
|------|------|------|
| /furniture-finder | AI 家具识别+购物 | [collov-features.md §2.1](./collov-features.md#21-ai-furniture-finder--furniture-finder) |
| /design-callout | AI 设计标注 | [collov-features.md §2.2](./collov-features.md#22-ai-design-callout--design-callout) |
| /moodboard-generator | AI 灵感板 | [collov-features.md §2.3](./collov-features.md#23-moodboard-generator--moodboard-generator) |
| /ai-room-score | AI 房间评分 | [collov-ai-room-score.md](./collov-ai-room-score.md) |

### 3.9 其他页面

| 路径 | 说明 |
|------|------|
| app.collov.ai/manager/api/doc | API 文档 |
| /partners、/partnership、/affiliate | 合作与联盟 |
| /refund、/terms、/policy、/cookie-policy、/cancellation-policy、/contact-information | 法律与政策 |
| /schedule-meeting | 预约会议 |
| /features/virtual-staging-tool-comparison-2025 | 工具对比页 |
| /articles/{slug} | 文章 |

---

## 四、URL 模式总结

| 类型 | 模式 | 示例 |
|------|------|------|
| 虚拟软装主页 | /virtual-staging, /virtual-staging-ai | 核心产品 |
| 房间类型 | /virtual-staging/{room} | living-room, bedroom, kitchen |
| 设计风格 | /virtual-staging/{style} | scandinavian, modern, luxury |
| 解决方案 | /{persona} | real-estate, designer, homeowner |
| AI 工具 | /{tool} | add-furniture, change-seasons, cabinet-ai |
| 功能页 | /features/{slug} | best-virtual-staging-tools-for-realtors |
| 文章 | /articles/{slug} | ai-virtual-room-makeover-before-after |
| 资源 | /gallery, /tutorial, /earn-photos | 案例展示、教程、上传赚 Credits |
| AI 产品 | /ai-vizard/, /ai-desk | 嵌入式工具、线下 Kiosk |

---

## 五、技术架构

| 项目 | 内容 |
|------|------|
| 前端框架 | Next.js |
| 部署 | 部分页面 via iframe 嵌入（collov.ai ← app.collov.ai），详见 [collov-migration-seo-analysis.md](./collov-migration-seo-analysis.md) |
| CDN | Cloudflare 全球边缘网络 |
| AI 引擎 | Collov Labs Visual Intelligence Substrate（自研 DiT backbone） |
| 边缘部署 | Intel OpenVINO、Intel Core Ultra |
| API | app.collov.ai/manager/api/doc |

---

## 六、Sitemap 对账记录

| 发现 | 详情 | 状态 |
|------|------|------|
| /360-panorama-generator | 页面存在但未收录于 sitemap.xml（SEO Spider 抓取遗漏） | ⚠ 待修复 |
| /ai-virtual-tour-generator | 未在 sitemap 中 | ⚠ 待确认是否仍在线 |
| /virtual-staging-ai | sitemap 中有重复条目 | ⚠ 低优先级 |
| /change-seasons | sitemap 中有重复条目 | ⚠ 低优先级 |
| /furniture-finder 等 4 个 | 待建，正确未出现在 sitemap | ✅ |
| /vacation-rental 等 5 个 | 待拓展，正确未出现在 sitemap | ✅ |

---

## 七、内链规划

```
首页 (/)
  ├── /virtual-staging-ai
  ├── /add-furniture、/change-seasons、/cabinet-ai、/flooring-ai、/furniture-ai
  ├── /home-redesign、/partial-remodel
  ├── /ai-vizard/              ← AI Vizard 营销页
  │     └── app.collov.ai/manager/api/doc  ← API 文档
  ├── /ai-desk
  ├── /furniture-finder        ← 待建
  ├── /design-callout          ← 待建
  ├── /moodboard-generator     ← 待建
  ├── /ai-room-score           ← 待建
  ├── /360-panorama-generator
  ├── /ai-virtual-tour-generator
  ├── /real-estate、/designer、/homeowner
  ├── /pricing
  ├── /blog
  └── /gallery、/tutorial、/earn-photos

工具页互链：furniture-finder ↔ design-callout ↔ add-furniture ↔ virtual-staging-ai ↔ ai-room-score
```

---

**Last updated**: 2026-05-27
