# Oginify 增长策略

> **本文档职责**：覆盖 Oginify 的全部增长杠杆——Build in Public 传播、内容三件套 SEO、开源分发（GEO）、产品漏斗、渠道优先级。合并原 content-strategy.md。  
> **引用**：[主文档](./oginify.md) 概览 | [features](./oginify-features.md) 产品 | [keywords](./oginify-keywords.md) 关键词 | [competitors](./oginify-competitors.md) 竞品

---

## 增长总览

| 杠杆 | 类型 | 时间线 | 目标 |
|------|------|--------|------|
| Build in Public | 信任 + 传播 | 进行中（Daily） | 即刻粉丝 → 自然流量 → 早期用户 |
| 内容三件套 | SEO 资产 | Gallery / Websites Without 已上线，Platforms 规划中 | 搜索表面积 ×3，吃三类搜索意图 |
| 开源分发 | GEO + npm | 已上线 | Agent 生态可发现性 → 安装量 → 开发者群体 |
| 产品漏斗 | 留存 + 变现 | 进行中 | 校验 → 灵感 → 生成 → 付费（待上线） |
| 竞品定位 | 差异化 | 进行中 | 「6 张/天免费 + 混合管线 + 产品矩阵」vs 模板化工具 |

---

## 1. Build in Public 传播

### 为什么 Build in Public

- Oginify 是 SEOer 为自己做的产品：OG 图服务于**社媒传播 + pSEO 每页可视化**，有天然的「真实需求」叙事
- 成本透明、定价透明、决策过程公开——这些在即刻上本身就是内容
- 早期没有投放预算，信任和传播靠人，不靠钱

### 对外传播渠道

| 平台 | 内容 | 频率 |
|------|------|------|
| **即刻** | 每日更新：做了什么、为什么、成本账、踩坑 | Daily |
| **LinkedIn**（Kostja 个人号） | 每个 milestone 一篇；Build in Public 旅程 + 专业洞察 | 按里程碑 |
| **X**（@kostjazhang） | 每个 milestone 一篇 Article（中文）+ Feed Post | 按里程碑 |
| **GitHub** | social-cards-skills 开源仓库，README 即内容 | 随迭代 |
| **项目文档** | [oginify-build-in-public.md](./oginify-build-in-public.md) 每日日志 | Daily |

**社媒发帖 SOP、已发归档、叙事口径** → [social-posts/playbook.md](./social-posts/playbook.md) · [social-posts/index.md](./social-posts/index.md)（各平台规格与全文不在此重复）

### 传播逻辑

```
即刻帖子 → 点赞/转发 → 新用户访问 oginify.com
  → 免费试用（6 张/天）→ 满意 → PAYG/Bundle 付费
    → 在即刻分享结果 → 二次传播
```

关键指标：即刻帖子互动率 > 网站日访问量 > 付费转化率（待上线）。

---

## 2. 内容三件套（SEO 资产）

Oginify 不只是一个生成器，也是 OG 图的知识库。三个内容页面各自吃不同的搜索意图，最终都导向产品。

### 2.1 三页对照

| 页面 | URL | 定位 | 核心搜索词 | 产品漏斗角色 |
|------|-----|------|-----------|-------------|
| **Gallery** | `/gallery` | 正面灵感 | "og image examples""best og images""social share card inspiration" | 启发 → 试试生成器 |
| **Websites Without** | `/websites-without-og-image` | 反面警示 | "sites without og image""missing meta tags""websites missing open graph" | 焦虑 → 检查自己的站 |
| **Platforms Built-in**（规划中） | `/platforms-with-built-in-og` | 决策参考 | "vercel og image""wordpress social image generator""ghost og image" | 教育 → 没内置？用 Oginify |

### 2.2 为什么这三个页面有价值

**搜索表面积**：单个 Generator 页只能吃 "og image generator" 类词。三个内容页面打开了完全不同的搜索入口——设计灵感、问题排查、工具对比。

**每个条目自带搜索量**：Gallery 的品牌名 + "og image"、Websites Without 的知名网站名 + "missing og"、Platforms Built-in 的平台名 + "og image generation"——都是长尾但精准的词。100 个条目 × 关键词 = 可观的搜索表面积。

**正反对照的叙事力量**：单独一个 Gallery 说服力有限。加上 Websites Without——「连 Hacker News、Berkshire Hathaway、W3.org 都没配 OG 图」——这个事实本身就有传播力。再加上 Platforms Built-in——「如果你的平台已经内置了，直接用；如果没有，用 Oginify」——把决策路径讲清楚。

**真实数据 > AI 生成**：手工验证的站点清单比 AI 批量生成的文章在搜索引擎里更有竞争力。

### 2.3 Websites Without OG Image — 详细策略

**已覆盖的站点类别**：

| 类别 | 代表站点 | 故事性 |
|------|---------|--------|
| Hacker 文化 | HN、xkcd、motherfuckingwebsite.com | 极简主义宣言——故意不加 |
| 金融/权威 | Berkshire Hathaway、W3.org | 1996 风格，OG 不是优先级 |
| 老牌技术 | GNU、Linux kernel、LWN | 开源基础设施，功能 > 社交 |
| 极简新闻 | text.npr.org、lite.cnn.com、old.reddit.com | 轻量版刻意剥离富媒体 |
| 学术/博客 | arXiv、Paul Graham、Dan Luu | 内容为王 |

**SEO 关键词机会**：
- 头部长尾："websites without og image""sites missing open graph tags"
- 品牌长尾：每个被列出站点名 + "og image""open graph"
- 问题驱动："why is my link not showing preview image"

**风险与应对**：

| 风险 | 应对 |
|------|------|
| 公关：被点名网站不满 | 中性 "OG coverage audit" 定位；takedown 链接 |
| 数据过期：网站后来补了图 | 每个条目标注 snapshot 时间；定期重抓 |
| 法律 | 只展示 meta 标签缺失状态，不展示网站内容 |

### 2.4 Platforms with Built-in OG — 规划

**已整理的四类平台**：

| 类别 | 平台 |
|------|------|
| 框架/Hosting | Vercel (@vercel/og)、Next.js、Nuxt、Astro、SvelteKit、Cloudflare Workers |
| CMS/Blogging | WordPress (Jetpack)、Ghost、Substack、Medium、Dev.to、Hashnode |
| 代码托管/文档 | GitHub、GitLab、Mintlify、Docusaurus |
| No-code | Framer、Webflow、Notion、Super.so、Read.cv、Linear |

**页面价值**：
- SEO：每个平台名 + "og image generation" 是独立搜索词
- 叙事：如果用户的平台已内置 → 直接用；没内置 → Oginify 填补空白
- 定位：Oginify 不只是工具，是关心 OG 生态的人

### 2.5 后续扩展方向

- OG 图 A/B 测试工具：同页面多套 OG 图 → 对比 CTR → 数据驱动选图
- 行业 OG 基准报告：爬取某行业 Top 100 站点的 OG 标签覆盖率 → 免费报告引流
- OG 设计指南：尺寸、格式、文字安全区、平台差异——教育型内容

---

## 3. 开源分发（GEO）

### 策略

social-cards-skills 不是 Oginify 的竞品，是增长引擎。

Oginify = 托管 SaaS → 零门槛，面向站长和营销人
Skills = 开源 Agent 工具 → 需 Node.js，面向开发者

两个人群不重叠，但互相背书：
- 开源项目给商业产品带来技术可信度
- 商业产品给开源项目带来曝光

### GEO 逻辑

Agent 生态（GPT、Claude、Cursor、Copilot）的搜索结果不完全依赖传统搜索引擎。Agent Skills 的可发现性来自：
- npm 关键词排名（"og-image""open-graph""social-card"）
- GitHub 仓库的 README 质量和星星数
- Agent 工具的 skill registry / marketplace

一个 npm 关键词排名带来的安装量 ≈ 十篇 SEO 文章——之前其他 skills 已验证过这个模型。

### 执行

- 仓库文案优化（中英文 README）
- npm 关键词精准覆盖
- 在 Agent 社区（Cursor directory、Claude Code skills）提交 listing
- 开源项目本身的内容更新 = 持续的增长信号

---

## 4. 产品漏斗

### 漏斗设计

```
Layer 1 — 发现
  ├── 搜索引擎（"og image checker""og image generator"）
  ├── 即刻 Build in Public 帖子
  ├── GitHub / npm（开发者）
  └── 社区（Reddit, HN, V2EX）

Layer 2 — 首次使用
  ├── Validator（免费校验 → 发现问题）
  ├── Gallery（看案例 → 被启发）
  └── Websites Without（看到大牌也缺 → 查自己的）

Layer 3 — 核心转化
  ├── Generator（6 张/天免费 → 下载）
  └── Above the Fold（无配额截图）

Layer 4 — 变现
  └── 付费版（接入中，价格待定）
```

### 转化指标（待追踪）

| 环节 | 指标 |
|------|------|
| 发现 → 访问 | 日 UV（按来源） |
| 访问 → 生成 | 生成按钮点击率 |
| 生成 → 下载 | 下载率 |
| 额度用尽 → 付费 | 付费转化率（待上线） |

---

## 5. 渠道优先级

| 优先级 | 渠道 | 原因 | 当前状态 |
|--------|------|------|----------|
| **P0** | 即刻 Build in Public | 零成本，高频，信任积累快 | 每日执行中 |
| **P0** | 开源 GEO | 已验证的增长杠杆，安装量 > 文章阅读量 | Skills 已上线 |
| **P1** | SEO（内容三件套） | 长期慢增长，但复利效应强 | Gallery + Websites Without 已上线 |
| **P1** | 产品矩阵互导流 | 内部流量循环，降低流失 | Validator → Generator 已打通 |
| **P2** | 社区（HN, V2EX, Reddit） | 一次性流量脉冲，时机重要 | 待合适里程碑 |
| **P3** | 付费投放 | 当前阶段过早，ROI 不划算 | 暂不启动 |

---

## 6. 竞品差异化定位

详见 [oginify-competitors.md](./oginify-competitors.md)。核心差异点：

| 维度 | 竞品（Bannerbear 等） | Oginify |
|------|----------------------|---------|
| 定价 | $19–49/月订阅 | 6 张/天免费 + PAYG $0.99 / Bundle $7.90–$29.00 |
| 生成方式 | 模板 + 手动编辑 | AI 读页面自动感知 |
| 产品矩阵 | 单点 API/SaaS | Generator + Validator + Gallery + 开源 Skills |
| 透明度 | 不公开 | Build in Public，成本/决策全公开 |

---

*Last updated: 2026-05-31. 每新增渠道或内容页面时同步更新。*
