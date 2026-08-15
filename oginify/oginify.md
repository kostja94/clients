# Oginify

> 遵循 [客户文档规范](../client-template.md)
> **产品入口**：[oginify.com](https://oginify.com)
> **开源产品**：[social-cards-skills](https://github.com/kostja94/social-cards-skills)（MIT）
> **关联文档**：[site-structure](./oginify-site-structure.md) | [features](./oginify-features.md) | [technical](./oginify-technical.md) | [use-cases](./use-cases/index.md) | [platforms-og](./platforms-og-and-social-preview.md) | [keywords](./oginify-keywords.md) | [competitors](./oginify-competitors.md) | [growth-strategy](./oginify-growth-strategy.md) | [social-posts](./social-posts/index.md) | [others](./oginify-others.md) | [changelog](./oginify-CHANGELOG.md) | [Build in Public](./oginify-build-in-public.md)

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [oginify.md](./oginify.md) | **本文档**：概览、ICP、文档索引 | — |
| [oginify-site-structure.md](./oginify-site-structure.md) | URL、IA、技术栈 | [keywords](./oginify-keywords.md) · [features](./oginify-features.md) |
| [oginify-features.md](./oginify-features.md) | 产品能力、漏斗 | [keywords](./oginify-keywords.md) · [competitors](./oginify-competitors.md) |
| [oginify-technical.md](./oginify-technical.md) | 技术实现：四条管线、模型选择、前端裁切 | [features](./oginify-features.md) · [others](./oginify-others.md) |
| [use-cases/index.md](./use-cases/index.md) | 场景四维度 | [features](./oginify-features.md) · [keywords](./oginify-keywords.md) |
| [oginify-keywords.md](./oginify-keywords.md) | 关键词 × 页面 | [growth-strategy](./oginify-growth-strategy.md) · [site-structure](./oginify-site-structure.md) |
| [oginify-competitors.md](./oginify-competitors.md) | 竞品与差异化 | [features](./oginify-features.md) |
| [oginify-growth-strategy.md](./oginify-growth-strategy.md) | 渠道与内容战役 | [keywords](./oginify-keywords.md) · [site-structure](./oginify-site-structure.md) |
| [platforms-og-and-social-preview.md](./platforms-og-and-social-preview.md) | **OG / Social Preview 平台参考**（内置能力、尺寸、决策树） | [competitors](./oginify-competitors.md) · [use-cases/by-image-size](./use-cases/by-image-size.md) |
| [oginify-others.md](./oginify-others.md) | 成本、定价依据、待办、Backlog | [features](./oginify-features.md) |
| [oginify-CHANGELOG.md](./oginify-CHANGELOG.md) | 版本变更记录 | — |
| [oginify-build-in-public.md](./oginify-build-in-public.md) | Build in Public 每日日志 | 以上所有 |
| [social-posts/index.md](./social-posts/index.md) | 社媒发帖归档、Playbook、Milestone 系列 | [growth-strategy](./oginify-growth-strategy.md) · [build-in-public](./oginify-build-in-public.md) |

---

## 项目概览

| 项目 | 内容 |
|------|------|
| **行业** | AI / SaaS / SEO 工具 |
| **产品形态** | Web 应用 + 开源 Agent Skills |
| **网站** | https://oginify.com |
| **当前阶段** | 早期（Lovable 托管，自有域名 oginify.com 已绑定，支付接入中） |
| **核心产品** | Open Graph 配图生成器：粘贴 URL → 2 张 1200×630 社交分享图（截图 + 模板渲染），AI 按需 Regenerate |
| **核心价值** | 为**每个页面**生成定制化可视化元素，支撑 **社媒传播**与 **programmatic SEO（pSEO）**——不是上线后补的「最后一步」，而是页面分发链路的一环 |
| **需求规模** | 全球网站 × 每站多 URL × 换图次数 × 1200×630 多用途；Vibe Coding 加速建站——**TAM 足够大** |
| **用量模型** | 单个用户用量**两极分化**：小量级（月 1–20 张）vs 大量级（月 500+ 张、pSEO / Agency）→ 定价分层 |
| **关键差异化** | 主流程零 AI 成本（截图 + 模板）+ AI 按需 Regenerate + 完整产品矩阵（生成 → 校验 → 灵感 → 开发者套件）+ 透明定价 + Build in Public |
| **目标用户** | 所有有网站的站长：SEOer、独立开发者、内容站、电商站、pSEO 规模化站点；Agent 环境（Cursor / Claude Code）的开发者 |
| **商业模式** | v1：Free（6 张/天）+ PAYG $0.99 / Bundle $7.90–$29.00 + Skills MIT。**v2 目标**：Free → PAYG $2.90 → Pro $19 → Studio $29 → Enterprise/API |
| **域名** | oginify.com（$11.10，已绑定 Lovable 项目；**仍托管于 Lovable**，未迁出） |
| **名字由来** | **OG**（Open Graph）+ **-inify**（动词化后缀）= 把 OG 图这件事做了 |
| **更新日期** | 2026-06-03 |

---

## 产品价值主张

### OG 图在增长栈中的位置

OG 图**不是**上线 checklist 里「有空再补」的最后一项。它是页面离开网站之后的第一张脸：

| 场景 | OG 图的角色 |
|------|-------------|
| **社媒传播** | 链接被分享到 LinkedIn、X、Slack、Discord 时，预览图就是广告素材——决定有没有人点 |
| **Programmatic SEO** | pSEO 站往往有数百至数千 URL；每页需要**独立、内容相关**的预览图，而非全站共用一张 logo |
| **内容分发** | 博客、产品页、活动页天然为分享而存在——视觉应与页面主题一致，才能提高 CTR |
| **Discover / 外链场景** | Google Discover、Newsletter 转发、社群分享等渠道，OG 图是页面在站外的可视化入口 |

### 常见误区 vs Oginify 解法

| 误区 | Oginify 解法 |
|------|--------------|
| 「先上线，图后面补」 | 把 OG 图纳入**发布流程**，与 SEO meta、内容一并规划 |
| 「全站一张通用 OG 图就够了」 | AI 读页面内容 → **每 URL 一张**定制化图（4 风格可选） |
| 「pSEO 页面太多，手工做不过来」 | 粘贴 URL 批量出图；Enterprise / API 接入规模化站点 |
| 「模板工具够用」 | 模板填空不理解页面——Oginify 是 **content-aware** 生成 |

### 起源故事（对外叙事口径）

Kostja 以 SEO 顾问身份服务客户时，为一个 **AI Notes Generator** 产品做 SEO：为各页面配置定制化 OG 图，配合社媒分发与搜索可见性——分享预览立刻变专业，点击表现明显改善。这验证了需求：**OG 图是 SEO + 传播基础设施，不是装饰。**

完整 Build in Public 日志见 [oginify-build-in-public.md](./oginify-build-in-public.md)。

---

## 1. 产品矩阵

| 产品 | 类型 | URL | 状态 |
|------|------|-----|------|
| **OG Generator** | 核心 SaaS | `/` | 已上线 |
| **Above the Fold** | 轻量工具 | `/above-the-fold` | 已上线 |
| **OG Validator** | 辅助工具 | `/open-graph-validator` | 已上线 |
| **Twitter Card Generator** | 产品 | `/twitter-card-generator` | 已上线 |
| **Templates** | 内容/工具 | `/templates` | 已上线 |
| **Gallery** | 内容资产 | `/gallery` | 已上线 |
| **Websites Without OG** | 内容资产 | `/websites-without-og-image` | 已上线（21 站） |
| **Use Cases Hub** | 内容 | `/use-cases` | 已上线 |
| **Pricing** | 商业 | `/pricing` | 已上线 |
| **Changelog** | 内容 | `/changelog` | 已上线 |
| **Platforms Built-in OG** | 内容 | `/platforms-with-built-in-og` | 规划中（文档源：[platforms-og-and-social-preview.md](./platforms-og-and-social-preview.md)） |
| **social-cards-skills** | 开源 | GitHub | 已开源 |

产品漏斗：Generator + Above the Fold（出图）→ Validator（校验）→ Gallery / Websites Without（灵感/警示）→ 付费转化（待上线）。开源 Skills 是独立触达开发者的并行渠道。

完整产品拆解见 [oginify-features.md](./oginify-features.md)。URL 详情见 [oginify-site-structure.md](./oginify-site-structure.md)。

---

## 2. 商业模式（摘要）

### 定价主轴

市场足够大（互联网尺度上的 1200×630 资产需求）；单个用户用量两极分化——小量级与大量级并存。定价须分层：**Free / PAYG 接长尾试用，Pro / Studio 订阅接中量级，Enterprise / API 接 pSEO 与平台集成**。

### 线上方案（v1 · 当前）

| 方案 | 价格 | 内容 |
|------|------|------|
| **Free** | $0 | 匿名 **6 张/天**；Validator、Templates、Above the Fold 等工具免费；无需注册 |
| **PAYG** | $0.99 | 2 张 + 6 次 regenerate 上限 |
| **Bundle 10** | $7.90 | 10 张 |
| **Bundle 50** | $29.00 | 50 张 |
| **social-cards-skills** | $0 / MIT | 永久免费自部署 |

### 目标方案（v2 · 规划）

| 方案 | 价格 | 内容 |
|------|------|------|
| **PAYG** | $2.90 | 2 张 + 6 Regenerate（冲动入口） |
| **Pro** | $19/月 · $149/年 | 100 张/月（主推） |
| **Studio** | $29/月 · $229/年 | 300 张/月（升级） |
| **Enterprise / API** | Contact | sitemap 批量、Webhook、按量/SLA |

完整依据、用量模型与实施路线图见 [oginify-others.md §定价依据](./oginify-others.md#定价依据)。

支付为 MoR 托管结账（手续费约 4.5% + $0.30/笔）。

---

## 3. 增长策略（摘要）

- **Build in Public**：即刻每日更新，公开产品决策、成本、踩坑
- **内容三件套**：Gallery（正面）+ Websites Without（反面）+ Platforms Built-in（决策参考，待建）
- **开源分发（GEO）**：social-cards-skills 通过 npm / GitHub / Agent 生态触达开发者
- **产品漏斗**：校验 → 灵感 → 生成 → 付费（待上线）

完整策略见 [oginify-growth-strategy.md](./oginify-growth-strategy.md)。

---

## 4. 关键决策记录

| 日期 | 决策 | 原因 |
|------|------|------|
| 2026-05-29 | MVP 用 Lovable 上线 | 最快验证需求 |
| 2026-05-30 | 自有域名 oginify.com 绑定 Lovable | 对外品牌 URL；**托管仍在 Lovable** |
| 2026-05-30 | 建 Validator + Gallery + Websites Without | 产品矩阵 > 单点工具 |
| 2026-05-30 | 开源 social-cards-skills（MIT） | 开发者与站长两个人群互相背书 |
| 2026-06-03 | 管线重构：主流程非 AI（截图 + 模板） | 主流程零 AI 成本（~$0.005/次），AI 仅用于 Regenerate（$0.030/Fast, $0.024/Precise） |
| 2026-06-03 | 接入支付，定价锁定 | PAYG $0.99 / Bundle 10 $7.90 / Bundle 50 $29.00；MoR 手续费约 4.5% + $0.30/笔 |
| 2026-06-03 | 定价叙事修正：TAM 大 + 用量两极 | 市场不小；小量级用 Free/PAYG，中量级用订阅，大量级用 Enterprise/API；非「低频工具」 |
| 2026-06-03 | 定价 v2 路线图 | Pro $19 / Studio $29 / PAYG $2.90；Bundle 过渡后下线；见 others §定价依据 |
| 2026-06-03 | 配额从 5 次/天 → 6 张/天 | 由代码 `src/lib/quota.server.ts` 驱动，单桶模型无关 |
| 2026-05-31 | Above the Fold 上线，后整合入 Generator 主流程 | Generator 输出第 1 张即为截图；独立 `/above-the-fold` 页面保留为免费工具入口 |
| 2026-05-31 | 对外叙事修正：OG 图 ≠ 最后一步 | 定位为社媒传播 + pSEO 的**每页定制化可视化**；取代「先上线后补图」口径 |
| 2026-05-31 | 文档校正：托管口径 | **仍于 Lovable**；oginify.com 为绑定域名，非独立站迁出 |

---

*Last updated: 2026-06-03*
