# 01 — 板块总览

> **读这一篇，搞清楚 Tech Layoffs 的整体情况。**  
> 下一步 → [02-sop.md](./02-sop.md)（日常做什么）

---

## 1. 板块定位

Tech Layoffs 是 Final Round AI 主站上的一个**资源性内容栏目**，通过追踪全球科技公司裁员数据吸引求职者流量，并引导他们使用 Final Round 的产品。

| 维度 | 说明 |
|------|------|
| **业务目标** | 承接「tech layoffs 2026」「company layoffs」「被裁后怎么找工作」等搜索流量 → 转化为产品注册/付费 |
| **目标用户** | 被裁员的求职者、担心裁员的在职者、关注行业动态的求职者 |
| **内容形态** | 聚合索引页 + 146 家公司详情页（静态 JSON 驱动，构建时生成） |
| **核心关键词** | tech layoffs 2026, company layoffs, laid off job search, tech job cuts, company name layoffs |

---

## 2. 页面结构

### 2.1 聚合索引页（Hub）

**对外 URL**：`https://www.finalroundai.com/tech-layoffs`

内容模块（由 React 组件渲染，数据来自 JSON 文件）：
- Hero 区（标题 + 统计概览 + 主 CTA）
- 时间线（2026 年裁员事件按月排列）
- 按公司浏览（146 家公司卡片，按行业分类筛选）
- 行业展望
- FAQ
- 底部 CTA

### 2.2 公司详情页（146 家）

**对外 URL**：`https://www.finalroundai.com/tech-layoffs/{company-slug}`

每家公司详情页包含以下模块（来自 JSON 中的 `content` 字段）：

| 模块 | JSON 字段 | 说明 |
|------|-----------|------|
| SEO 元数据 | `seo` | title、description、canonical、ogImage |
| Hero 区 | `hero` | 标题、副标题、主/次 CTA、信任标签 |
| 数据概览 | `statBar` | 裁员人数、时间、行业等图标化指标 |
| 快速事实 | `quickFacts` | 图标 + 标签 + 数值 + 详情，6–8 条 |
| 痛点分析 | `painPoints` | 被裁后的核心挑战 + 解决方案 |
| 产品模块 | `products` | Final Round 三产品推荐卡片 |
| 回归计划 | `comebackPlan` | 5 步求职路线图（含步骤链接） |
| FAQ | `faq` | 与该公司裁员直接相关的问题 |
| CTA | `cta` | 底部行动号召（标题 + 副标题 + 按钮） |
| 相关链接 | `relatedLinks` | Use Cases、产品页、同行业其他公司 |

---

## 3. 技术栈与部署

### 3.1 技术栈

| 层级 | 选型 |
|------|------|
| 框架 | Next.js 15（App Router） |
| 语言 | TypeScript |
| 样式 | Tailwind CSS + shadcn/ui 组件 |
| 动画 | Framer Motion |
| 字体 | Instrument Serif（标题）+ Roboto（正文） |
| 构建 | 151 个静态页面（SSG），构建时全量生成 |

### 3.2 部署形态

```
用户浏览器 → www.finalroundai.com/tech-layoffs
                    ↓（反向代理转发，Mohit 维护主站 Rewrite 规则）
           finalround-nextjs.vercel.app/tech-layoffs
                    ↑
               Bella 维护的 Vercel 项目（npm 包名：finalround-web）
```

- Vercel 生产 URL：`https://finalround-nextjs.vercel.app`
- 本地开发端口：**8080**（`npm run dev`）
- 根路径 `/` 自动重定向到 `/tech-layoffs`
- 产品页路径（如 `/ai-mock-interview`）自动 302 跳转到主站 `finalroundai.com`
- 主站 Rewrite 规则由 **Mohit** 维护，Bella 不需要修改

技术细节见 [reference/architecture.md](./reference/architecture.md)。

---

## 4. 数据架构（理解这个很重要）

### 4.1 数据存储

公司数据不是 Markdown 文件——是 146 个独立的 JSON 文件，存储在 `src/data/companies/{slug}.json`：

```
src/data/companies/
├── amazon.json
├── meta.json
├── oracle.json
├── ...
├── zoominfo.json       ← 146 个文件
└── index.ts            ← 自动生成的 barrel 文件，不要手动编辑
```

每个 JSON 文件结构：

```json
{
  "slug": "amazon",
  "company_name": "Amazon",
  "total_count": "30,000",
  "date_range": "Oct 2025 – Jan 2026",
  "industry": "Big Tech",
  "updated_at": "2026-05-21",
  "content": {
    "seo": { "title": "...", "description": "...", "canonical": "...", "ogImage": "..." },
    "hero": { ... },
    "statBar": { ... },
    "quickFacts": { ... },
    "painPoints": { ... },
    "products": { ... },
    "comebackPlan": { ... },
    "faq": { ... },
    "cta": { ... },
    "relatedLinks": { ... }
  }
}
```

### 4.2 数据流

```
{slug}.json  →  index.ts（barrel，自动生成）
                    ↓
            company-layoffs.ts（loader）
                    ↓
            [slug]/page.tsx（SSG 页面）
                    ↓
          CompanyLayoffPage.tsx（React 组件渲染）
```

完整字段定义见 `src/types/company-layoff-content.ts`。

### 4.3 新增公司流程

1. 在 `src/data/companies/` 下创建 `{slug}.json`
2. 运行 `node scripts/generate-company-index.mjs` 重新生成 barrel
3. 运行 `npm run build` 验证构建通过
4. 提交 `.json` 文件和更新后的 `index.ts`

---

## 5. 流量与 SEO

### 5.1 搜索流量来源

| 搜索类型 | 示例 | 对应页面 |
|----------|------|----------|
| 行业宏观词 | "tech layoffs 2026" | 聚合索引页 |
| 公司 + 裁员 | "Amazon layoffs 2026"、"Meta 裁员" | 公司详情页 |
| 求职 + 裁员 | "laid off what to do" | 聚合页（求职资源区） |

### 5.2 转化路径

```
搜索 "Amazon layoffs 2026"
  → 进入 /tech-layoffs/amazon
  → 阅读裁员信息 + 5 步回归计划
  → 点击产品 CTA（如 "Start For Free"）
  → /ai-mock-interview 或 /ai-resume-builder
  → 注册 / 付费
```

### 5.3 已有 SEO 基础设施

- 每个公司页自动生成 **BreadcrumbList + FAQPage + NewsArticle** 三种 JSON-LD
- canonical 指向 `https://www.finalroundai.com/tech-layoffs/{slug}`
- `metadataBase` 为主站域名
- 聚合页 Title：`2026 Tech Layoffs Tracker — 146 Companies | Final Round AI`

---

## 6. 与主站其他板块的关系

| 链接方向 | 说明 |
|----------|------|
| **公司页 → 产品页** | 每个公司页含 3 产品推荐卡片 + comebackPlan 含产品链接 + 底部 CTA |
| **聚合页 → 公司页** | 146 家公司卡片，按行业分类可浏览 |
| **产品页路径** | `/ai-mock-interview` 等 13 个路径自动 302 跳转到主站 `finalroundai.com` |
| **根路径 `/`** | 自动 redirect 到 `/tech-layoffs` |

---

## 7. 内容质量标准（每家公司页上线前）

- [ ] JSON 中 6 个必填字段完整（slug、company_name、total_count、date_range、content、updated_at）
- [ ] `content.seo` 中 title / description 已填写
- [ ] FAQ 至少 3 条，且与该公司相关
- [ ] 所有数字有来源、可溯源
- [ ] JSON 文件与 barrel `index.ts` 同步（通过 `npm run build` 验证）
- [ ] 通过数据验证（Python 脚本或手动检查 JSON）

---

*下一步 → [02-sop.md](./02-sop.md) 了解日常工作节奏*
