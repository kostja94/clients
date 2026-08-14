# Final Round AI — Tech Layoffs 板块总览

> **本文定位**：Tech Layoffs 板块的架构总览、部署形态、维护边界与路由说明。裁员数据见 [finalround-layoff-data.md](./finalround-layoff-data.md)，竞品与资源参考见 [finalround-resources.md](./finalround-resources.md)。  
> **关联**：[finalround.md](../finalround.md)（产品总览） · [finalround-site-structure.md](../finalround-site-structure.md)（URL 树） · [finalround-production-routing.md](../technical/finalround-production-routing.md)（主域 Rewrite 通用方案） · [finalround-project-tasks.md](../finalround-project-tasks.md)（资源内容任务）

**Last updated**: 2026-06-03（新建：Tech Layoffs 迁移至独立 Vercel 子域名，本地维护）

---

## 一、板块定位

Tech Layoffs 是 Final Round AI 的一项**资源性内容资产**，通过追踪全球科技裁员数据吸引求职者流量，并导流至产品 CTA（AI Mock Interview、Resume Builder、Interview Copilot）。

| 维度 | 说明 |
|------|------|
| **业务目标** | 承接「裁员」「被裁后求职」类搜索流量 → 产品注册/付费 |
| **内容形态** | 聚合索引页 + 25 家公司详情页（程序化生成） |
| **数据源** | Layoffs.fyi、TrueUp、公司公开披露、新闻媒体报道 |
| **目标关键词** | tech layoffs 2026、company layoffs、laid off job search、AI interview prep after layoff |

---

## 二、部署架构

### 2.1 子域名与来源

Tech Layoffs 板块的聚合页和详情页通过主站反向代理转发到一个**独立的 Vercel 子域名**：

| 项 | 值 |
|----|-----|
| **对外 URL（用户访问）** | `https://www.finalroundai.com/tech-layoffs`、`/tech-layoffs/{company}` |
| **真实来源（origin）** | **`https://finalround-nextjs.vercel.app/tech-layoffs`** |
| **部署平台** | Vercel（独立项目，非 `finalround.vercel.app` 营销子站） |
| **技术栈** | Next.js（App Router） |
| **维护者** | Kostja（本地维护，独立仓库） |

### 2.2 与营销子站的区别

Tech Layoffs 板块使用**独立的 Vercel 项目与子域名**，不同于 [finalround-production-routing.md](../technical/finalround-production-routing.md) 中描述的通用营销子站（`finalround.vercel.app`）：

| | 通用营销子站 | Tech Layoffs 子站 |
|---|---|---|
| **Vercel 域名** | `finalround.vercel.app` | `finalround-nextjs.vercel.app` |
| **主域路径** | `/<segment>`（通用前缀） | `/tech-layoffs` |
| **内容范围** | Blog、Use Cases、Interview Prep 等 | 仅 Tech Layoffs 聚合页 + 公司详情页 |
| **维护仓库** | 营销子站仓库 | Kostja 本地独立仓库 |

### 2.3 Rewrite 规则

主站（`www.finalroundai.com`）通过反向代理将 `/tech-layoffs` 路径转发到子站 origin，地址栏保持不变：

```
用户请求: https://www.finalroundai.com/tech-layoffs
         → Rewrite →
后端请求: https://finalround-nextjs.vercel.app/tech-layoffs
```

用户请求: `https://www.finalroundai.com/tech-layoffs/amazon`
         → Rewrite →
后端请求: `https://finalround-nextjs.vercel.app/tech-layoffs/amazon`

#### 配置示例（`vercel.json` 或 `next.config` rewrites）

```json
{
  "rewrites": [
    {
      "source": "/tech-layoffs",
      "destination": "https://finalround-nextjs.vercel.app/tech-layoffs"
    },
    {
      "source": "/tech-layoffs/:path*",
      "destination": "https://finalround-nextjs.vercel.app/tech-layoffs/:path*"
    }
  ]
}
```

若 Tech Layoffs 子站也使用 Next.js 且需要加载 `/_next/static/*` 资源，需评估是否与主站 `/_next` 冲突。如冲突，优先考虑：

- Tech Layoffs 子站的静态资源走独立子域名直连（避免经过主站 `/_next`）
- 或主站为非 Next 栈，可全局转发 `/_next`

具体以主站实际托管栈和线上表现为准。

#### Nginx 等价配置

```nginx
location /tech-layoffs/ {
    proxy_pass https://finalround-nextjs.vercel.app/tech-layoffs/;
    proxy_ssl_server_name on;
    proxy_set_header Host finalround-nextjs.vercel.app;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

---

## 三、页面清单

### 3.1 聚合索引页

| 页面 | 对外 URL | 子站路由 |
|------|---------|----------|
| Tech Layoffs 首页 | `/tech-layoffs` | `/tech-layoffs` |

含：裁员规模概览、公司卡片列表、搜索/筛选、产品 CTA 模块。

### 3.2 公司详情页（25 家）

所有公司页使用统一模式 `/tech-layoffs/{company}`（全小写）：

Amazon、Oracle、Meta、Microsoft、Block、Intel、Salesforce、Dell、Atlassian、Pinterest、GoPro、Autodesk、Google、Verizon、Target、Walmart、Wells Fargo、Chevron、IBM、Disney、Ford、Cisco、Nike、PwC

每页含：裁员规模、时间线、原因分析、求职资源、产品 CTA。

---

## 四、本地维护工作流

### 4.1 仓库与代码

Tech Layoffs 子站代码在 Kostja 本地独立仓库中维护，部署到 Vercel 项目 `finalround-nextjs`。

### 4.2 内容更新流程

```
1. 数据采集
   - 监控 Layoffs.fyi、TrueUp、公司公开披露
   - 更新 [finalround-layoff-data.md](./finalround-layoff-data.md)（中文参考数据）

2. 代码更新
   - 在本地仓库编辑页面内容（数据、文案、新公司页）
   - 本地预览确认

3. 部署
   - 推送至 Vercel 项目（自动部署或手动触发）
   - 验证 https://finalround-nextjs.vercel.app/tech-layoffs 生效

4. 主域验证
   - 通过 https://www.finalroundai.com/tech-layoffs 访问
   - 确认 Rewrite 正常、地址栏不变
   - 抽测 2-3 家公司详情页

5. 文档同步
   - 更新本文「Last updated」
   - 若新增公司页，同步更新 §3.2 清单
```

### 4.3 数据刷新频率

| 内容 | 频率 | 备注 |
|------|------|------|
| 裁员数据 | 每周或事件驱动 | 大公司裁员公告后 24–48 小时内更新 |
| 聚合页统计 | 每月 | YTD 总人数、公司数 |
| 新增公司页 | 按需 | 裁员规模 ≥1,000 人或高知名度公司 |

---

## 五、与主站文档的关系

### 5.1 本文档在文档体系中的位置

```
finalround/
├── tech-layoffs/
│   ├── finalround-tech-layoffs-overview.md  ← 本文（架构与维护总览）
│   ├── finalround-layoff-data.md            （裁员数据明细）
│   └── finalround-resources.md              （外部资源与竞品参考）
├── technical/
│   └── finalround-production-routing.md     （主域 Rewrite 通用方案）
├── finalround-site-structure.md             （全站 URL 树与 sitemap）
└── finalround-project-tasks.md              （资源内容任务 §4）
```

### 5.2 与其他文档的交叉引用

| 主题 | 权威文档 |
|------|----------|
| 裁员数据明细 | [finalround-layoff-data.md](./finalround-layoff-data.md) |
| 竞品与外部资源 | [finalround-resources.md](./finalround-resources.md) |
| 主域 Rewrite 通用规则 | [finalround-production-routing.md](../technical/finalround-production-routing.md) |
| Tech Layoffs URL 与 sitemap | [finalround-site-structure.md](../finalround-site-structure.md) §1.4、§6.4 |
| 资源内容任务状态 | [finalround-project-tasks.md](../finalround-project-tasks.md) §4 |

---

## 六、SEO 与运维注意事项

1. **canonical**：子站页面 `metadataBase` 设为 `https://www.finalroundai.com`，避免搜索引擎收录 `finalround-nextjs.vercel.app` 域名。
2. **sitemap**：Tech Layoffs 页面已纳入主站 sitemap（`tech_layoffs` 子 sitemap，26 条），确保爬虫发现路径为主域 URL。
3. **子域名直访**：`finalround-nextjs.vercel.app` 不应被用户或搜索引擎直接访问；可在子站侧配置 canonical 指向主域，或在 `robots.txt` 中限制。
4. **`/_next` 冲突**：若主站同为 Next.js，注意 `/_next/static/*` 资源加载路径，参考 [finalround-production-routing.md](../technical/finalround-production-routing.md) §7。
5. **发版节奏**：子站内容更新可独立部署，不依赖主站发版；仅当修改主站 Rewrite 规则时才需主站/基建配合。
6. **监控**：主域 `/tech-layoffs` 返回 200、页面内容与子站 origin 一致、无混合内容警告。

---

## 七、历史与迁移记录

| 日期 | 事件 |
|------|------|
| 2026-05 之前 | Tech Layoffs 部署于 `finalround.lovable.app/tech-layoffs`（Lovable 平台） |
| 2026-06-03 | 迁移至独立 Vercel 子域名 `finalround-nextjs.vercel.app/tech-layoffs`；主站通过 Rewrite 反向代理；Kostja 本地维护 |

---

*架构变更或新增公司页后请更新本文 §二～§三 及「Last updated」日期。*
