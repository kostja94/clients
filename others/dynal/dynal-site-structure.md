# Dynal 网站结构（dynal.ai）

> **站点根**：https://dynal.ai/  
> **Sitemap（主索引）**：[https://dynal.ai/sitemap.xml](https://dynal.ai/sitemap.xml)  
> **关联**：[dynal.md](./dynal.md) | [dynal-features.md](./dynal-features.md) | [dynal-keywords.md](./dynal-keywords.md) | [dynal-use-cases.md](./dynal-use-cases.md) | [dynal-competitors.md](./dynal-competitors.md) | [dynal-production-routing.md](./dynal-production-routing.md)（**主域 Rewrite → dynal-nextjs.vercel.app、`/linkedin-post-generator/*` 与多语言前缀**） | [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)（**`/solutions/linkedin-post-generator`** 与规划 **`/tools/linkedin-post-generator`**）| [dynal-tools.md](./dynal-tools.md)（**规划中的**其余 `/tools/`、`/product/` 营销路径）  
> **Skills 对齐**：**website-structure**、**sitemap**、**internal-links（Blog 独立内链规范**：[blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md](./blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md)**）**。

**用途**：描述 **线上 URL 模式、多语言规则、sitemap 与 robots 暴露的路径**，供 SEO、内链与营销文档对齐。规划中的 **`/tools/*`（其中 `linkedin-post-generator` 见 [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)）**、carousel 产品页等路径清单与映射以 [dynal-tools.md](./dynal-tools.md) **§2** 为准，**上线后再写入本文**。产品一句定位与叙事以 [dynal.md](./dynal.md) §1 为准。**站点改版后请更新本文**（并复核 sitemap / robots）。

**信息来源**：主 sitemap 全文（`lastmod` 均为 **2026-05-09T11:05:30.173Z**）、[robots.txt](https://dynal.ai/robots.txt)（抓取于 **2026-04-07**）、以及对若干路径的 HTTP 抽样校验。

**Last updated**: 2026-05-11 — 标注  将被废弃，由  替代。

---

## 〇、站点层级与 URL 规则（总则）

### 〇.1 树状层级（概览）

```
dynal.ai/
├── /（默认语言首页，无前缀）
├── /{locale}/（es | fr | de | pt | it — 与 sitemap 一致；**无** /en/）
├── /pricing、/about-us、/blog、/agent（各语言同构）
├── /legal/privacy-policy、/legal/terms-of-service
├── /use-cases/{slug}（Persona 落地，10 个 slug，见 §二）
├── /product/{slug}（原 Solutions：linkedin-ai-writer、linkedin-content-system）
├── /linkedin-post-generator（Post Generator hub；**已上线**）
├── /linkedin-post-generator/{topic}（10 个 topic 子页，见 §五）
├── /linkedin-{tool}（免费工具：headline-generator、banner-generator、profile-picture-generator、profile-score、about-section-generator、engagement-calculator）
├── /playbook、/vs-chatgpt（**不在**主 sitemap；**200**，见 §五）
└── 应用区（多被 robots **Disallow**，见 §四）— /plan、/brand-dna、/analytics、/calendar、/projects 等
```

### 〇.2 多语言 URL 规则

| 规则 | 说明 |
|------|------|
| **默认语言** | 英文：**无前缀**，根路径即为英文页（如 `/pricing`）。 |
| **其它 UI 语言** | 路径前缀 **`/{locale}/`**，`locale ∈ { es, fr, de, pt, it }`（与 [dynal.md](./dynal.md) 首页多语言列表一致）。 |
| **同构路径** | 除首页外，sitemap 中每个「模板路径」均存在 **6 个版本**（1 个默认 + 5 个前缀），例如 `/blog` 与 `/es/blog`。 |
| **法律页** | 统一在 **`/legal/`** 下：`privacy-policy`、`terms-of-service`。 |
| **Use Case** | 固定段 **`/use-cases/`**（复数 *use-cases*），下接 **kebab-case** slug（见 §二）。 |

### 〇.3 与营销文档路径对照（易错）

以下在 [dynal.md](./dynal.md) §5 **主导航文案**中常见，但 **路径并非** 直觉 slug；内链与 SEO 文案 **以本文与线上为准**。

| 文档/导航常见说法 | 线上路径（校验 2026-04-07） |
|-------------------|-----------------------------|
| **Compare → VS ChatGPT** | **`/vs-chatgpt`**（**200**）；**非** `/compare/vs-chatgpt`（404）。 |
| **Use Cases（导航）** | 公开收录为 **`/use-cases/...`** 各页；**非** `/use-case/...`（404）。 |
| **Features** | **`/features`** → **404**（可能为应用内或前端路由，非此静态路径）。 |
| **Contact us** | **`/contact-us`** → **404**（需从页内链接或新版路径复核）。 |
| **Roadmap** | **`/roadmap`** → **404**（同上）。 |
| **Solutions** | 已迁移至 **`/product/`**：**`/product/linkedin-content-system`**、**`/product/linkedin-ai-writer`**；**`/linkedin-post-generator`** 替代原 `/solutions/linkedin-post-generator`。 |

---

## 一、主 sitemap 收录的「模板路径」（英文默认 URL）

以下每条在 sitemap 中均另有 **`/es`…`/it` 共 5 个语言副本**（结构相同）。完整枚举见 [sitemap.xml](https://dynal.ai/sitemap.xml)。

| 路径 | `changefreq` | `priority` | 角色 |
|------|--------------|------------|------|
| `/` | weekly | 1.0 | 首页 |
| `/pricing` | weekly | 0.8 | 定价 |
| `/about-us` | monthly | 0.7 | 关于 |
| `/blog` | weekly | 0.9 | 博客索引 |
| `/agent` | monthly | 0.8 | Agent 聚合页 |
| `/linkedin-post-generator` | weekly | 0.85 | Post Generator hub |
| `/linkedin-headline-generator` | weekly | 0.8 | 免费工具 |
| `/linkedin-profile-score` | weekly | 0.82 | 免费工具 |
| `/linkedin-banner-generator` | monthly | 0.8 | 免费工具 |
| `/linkedin-profile-picture-generator` | monthly | 0.8 | 免费工具 |
| `/linkedin-about-section-generator` | monthly | 0.78 | 免费工具 |
| `/linkedin-engagement-calculator` | monthly | 0.78 | 免费工具 |
| `/legal/privacy-policy` | yearly | 0.4 | 隐私政策 |
| `/legal/terms-of-service` | yearly | 0.4 | 服务条款 |

---

## 二、Use Case 落地（sitemap 收录）

**模式**：`/use-cases/{slug}`（及 `/es/use-cases/{slug}` 等）。**注意**：sitemap 中路径为复数 **`/use-cases/`**，slug 无 `for-` 前缀。

| Slug | 默认 URL |
|------|----------|
| `founders` | https://dynal.ai/use-cases/founders |
| `executives` | https://dynal.ai/use-cases/executives |
| `marketers` | https://dynal.ai/use-cases/marketers |
| `coaches` | https://dynal.ai/use-cases/coaches |
| `agencies` | https://dynal.ai/use-cases/agencies |
| `sales-professionals` | https://dynal.ai/use-cases/sales-professionals |
| `recruiters` | https://dynal.ai/use-cases/recruiters |
| `job-seekers` | https://dynal.ai/use-cases/job-seekers |
| `personal-branding` | https://dynal.ai/use-cases/personal-branding |
| `ghostwriter` | https://dynal.ai/use-cases/ghostwriter |

与 [dynal-use-cases.md](./dynal-use-cases.md) 人群叙事对照时，**以 slug 与线上标题为准**；Use Case 文档的 slug 列表需同步更新。

---

## 三、子 Sitemap 与博客 / Playbook

`robots.txt` 声明 **3 个** sitemap：

| Sitemap | URL |
|---------|-----|
| 主站 | https://dynal.ai/sitemap.xml |
| 博客 | https://dynal.ai/blog/sitemap.xml |
| Playbook | https://dynal.ai/playbook/sitemap.xml |

**说明**：主 `sitemap.xml` 仅列出 **首页型模板 + Use Case + 法律** 等（§1–§2）；**单篇文章**与 **Playbook 单页** 的 URL  discovery 应同时参考上述子 sitemap（具体条目随内容变更，**不**在本文逐条固化）。

---

## 四、robots.txt 与「应用区」路径

摘自线上 [robots.txt](https://dynal.ai/robots.txt)（抓取 2026-04-07；**以后台为准**）。

### 4.1 Allow（摘录）

- `Allow: /`
- `Allow: /about-us`
- `Allow: /pricing`
- `Allow: /blog/*`
- `Allow: /agent`
- `Allow: /product/*`

### 4.2 Disallow（产品内页 / 敏感区）

| 模式 | 说明 |
|------|------|
| `/cases/*` | 案例相关（全站 disallow） |
| `/auth/invitation`、`/auth/forget-password` | 认证相关 |
| `/plan`、`/plan/*` | 套餐 / 计划 |
| `/brand-dna`、`/brand-dna/*` | Brand DNA |
| `/analytics`、`/analytics/*` | 分析 |
| `/calendar`、`/calendar/*` | 日历 |
| `/projects`、`/projects/*` | 项目 |

**SEO 含义**：上述路径**不应**作为自然搜索主要着陆页依赖；是否与 **noindex**、登录门栏配合，以页面 HTML 与 GSC 为准（执行项见 [dynal.md](./dynal.md) §10）。

---

## 五、主 sitemap 未列出但可访问的营销路径（抽样）

以下 **200**（HEAD/GET 抽样 **2026-04-07**），用于内链与关键词落地时对齐；**是否应并入主 sitemap** 属技术 SEO 决策。

| URL | 备注 |
|-----|------|
| https://dynal.ai/agent | Agent 聚合页（sitemap 收录） |
| https://dynal.ai/linkedin-post-generator | Post Generator hub（sitemap 收录；weekly/0.85） |
| https://dynal.ai/linkedin-post-generator/{topic} | 10 个 topic 子页（sitemap 收录；monthly/0.7）：announcement-post、case-study、engagement-post、farewell-post、hiring-post、hook-generator、how-to-post、recommendation、storytelling-post、thought-leadership |
| https://dynal.ai/product/linkedin-ai-writer | 原 Solutions（sitemap 收录；monthly/0.75） |
| https://dynal.ai/product/linkedin-content-system | 原 Solutions（sitemap 收录；monthly/0.75） |
| https://dynal.ai/linkedin-headline-generator | 免费工具（sitemap 收录；weekly/0.8） |
| https://dynal.ai/linkedin-profile-score | 免费工具（sitemap 收录；weekly/0.82） |
| https://dynal.ai/linkedin-banner-generator | 免费工具（sitemap 收录；monthly/0.8） |
| https://dynal.ai/linkedin-profile-picture-generator | 免费工具（sitemap 收录；monthly/0.8） |
| https://dynal.ai/linkedin-about-section-generator | 免费工具（sitemap 收录；monthly/0.78） |
| https://dynal.ai/linkedin-engagement-calculator | 免费工具（sitemap 收录；monthly/0.78） |
| https://dynal.ai/playbook | Playbook 入口（**不在**主 sitemap）；另有 `playbook/sitemap.xml` |
| https://dynal.ai/vs-chatgpt | 对比 ChatGPT（**不在**主 sitemap） |

---

## 六、URL 校验记录（抽样 · 2026-04-07）

| URL | HTTP | 备注 |
|-----|------|------|
| `https://dynal.ai/` | 200 | 首页 |
| `https://dynal.ai/vs-chatgpt` | 200 | 对比页 |
| `https://dynal.ai/solutions/linkedin-content-system` | 200 | Solutions |
| `https://dynal.ai/playbook` | 200 | Playbook |
| `https://dynal.ai/features` | 404 | 勿假设存在 |
| `https://dynal.ai/use-cases` | 404 | Use Case 用 **`/use-case/...`** |
| `https://dynal.ai/compare/vs-chatgpt` | 404 | 对比页用 **`/vs-chatgpt`** |
| `https://dynal.ai/contact-us` | 404 | 联系路径待随站点更新复核 |
| `https://dynal.ai/roadmap` | 404 | 同上 |

*全量与重定向链以浏览器、Screaming Frog 或 GSC 为准。*

---

## 七、维护清单

- [ ] 站点导航或路由变更后，对照 [sitemap.xml](https://dynal.ai/sitemap.xml) 与 [robots.txt](https://dynal.ai/robots.txt) 更新 §1–§6。  
- [ ] 新增 **locale** 时，在 §〇.2 与 sitemap 枚举中同步。  
- [ ] [dynal-keywords.md](./dynal-keywords.md) §5 中 Solutions / product 页、免费工具 URL 待办，**以本文 §5 与 sitemap 为准**复核。  
- [ ] [dynal.md](./dynal.md) §5 仅保留摘要，**详细路径以本文为权威**。  
- [ ] 新增免费工具或 `/product/` 页上线后，同步更新本文 §一、§五 与 sitemap 记录。
