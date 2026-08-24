# 猎豹AI实战派 — 站点结构

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` 或 `/homepage-one-to-one.html` | 首页 / 转化枢纽 | 猎豹AI实战派、企业AI Native转型 | P0 |
| `/blog.html` | 博客索引 | AI Native 转型、企业 AI 落地 | P0 |
| `/blog/*.html`（单篇，模式待统一） | 观点 / 笔记 | AI 能力边界、Agent 验收 | P0 |
| `/research.html` | 研究索引 | 企业 AI 采用率、AI 编程效能 | P1 |
| `/research/*.html`（单篇） | 研究报告 / Case Study | CAMA 五阶段、FDE 制度 | P1 |
| `/solution-*.html`（7 行业） | 行业解决方案 | 教育/制造/电商 AI 解决方案 | P0 |
| `/event-*.html` | 活动落地页 | 傅盛 AI 课、深圳 AI 实战派 | P0 |
| `/ai-native-zone.html` | 特区 / 方法论展示 | AI Native 特区、西安 AI 团队 | P1 |
| 飞书表单（外链） | 报名 / 诊断申请 | 企业 AI 诊断、实战派报名 | P0 |
| `https://easyaisuite.com` | 产品生态（外链） | Easy AI Suite、企业 Agent 工具 | P1 |
| `https://www.cmai.club/` | 社群 / 延伸触点 | 猎豹 AI 社群 | P2 |

## 2. URL 层级

```
cmainative.cmcm.com/
├── /（首页，同 homepage-one-to-one.html）
├── blog.html                    # 博客索引（AI Native 转型研究院）
│   └── [单篇 URL 模式 ⚠️ 待验证：当前索引无独立 slug 页可见]
├── research.html                # 研究索引
│   └── [单篇 URL 模式 ⚠️ 待验证]
├── ai-native-zone.html          # AI Native 特区
├── solution-{industry}.html     # 7 个行业解决方案
│   ├── solution-industrial-automation.html
│   ├── solution-traditional-manufacturing.html
│   ├── solution-general-marketing.html
│   ├── solution-general-finance.html
│   ├── solution-general-legal.html
│   ├── solution-ecommerce.html
│   └── solution-education.html
├── event-{city}-{date}.html     # 往期 / 当期活动页
│   ├── event-beijing-20260724.html
│   ├── event-shenzhen-20260710.html
│   └── event-shenzhen-20260711.html
└── css/、images/                # 静态资源
```

**主导航逻辑**（首页区块）：品牌 Hero → 傅盛 / 猎豹转型故事 → 三步变革（思维 / 组织 / 产品，弹窗）→ 行业入口 → 活动日程 → 双 CTA（企业 AI 诊断 + 报名下一场）。

## 3. 技术架构

| 维度 | 识别结果 | 识别方式 |
|------|---------|---------|
| 站点类型 | 静态 HTML + CSS | 首页 HTML 引用 `css/site.css`、`css/contact-dialog.css`（2026-08-21） |
| 托管 | ⚠️ 待验证（猎豹移动子域 `cmcm.com`） | 域名归属 |
| CMS | 无独立 CMS 迹象；内容可能由模板 / 脚本生成 | 页面结构高度一致 |
| 转化 | 飞书多维表格表单 + 二维码图片 | 内链 `cheetah-mobile.feishu.cn/share/base/form/...` |
| SEO 基础设施 | robots.txt **404**；sitemap.xml **500** | 直接请求（2026-08-21） |
| 关联产品 | Easy AI Suite（easyaisuite.com）、CMAI Club | 首页外链 |

## 4. 多语言

| 项 | 内容 |
|----|------|
| 主语言 | 简体中文 |
| URL 结构 | 无 `/zh/` 前缀，单语站点 |
| 目标市场 | 中国大陆企业决策者、一把手、业务负责人 |

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| 首页 + 变体 | `/`、`/homepage-one-to-one.html` | 2 | ⚠️ 待验证 |
| 博客 | `/blog.html` + 单篇 | 4+（索引显示 4 篇，增长中） | 2026-08-05 起 |
| 研究 | `/research.html` + 单篇 | 5+ | 2026-08-20 起 |
| 行业方案 | `/solution-{slug}.html` | 7 | ⚠️ 待验证 |
| 活动 | `/event-{city}-{YYYYMMDD}.html` | 5+（含往期） | 下一场 2026-09-04 深圳 |
| 特区 | `/ai-native-zone.html` | 1 | ⚠️ 待验证 |

> sitemap.xml 当前不可用（500）；以上由首页内链 + 页面索引归纳（2026-08-21）。

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 Hero | CTA | 立即报名、下一场活动 |
| 三步变革弹窗 | 深度说明 + CTA | 实战派活动 / 入企陪跑 / Easy Suite |
| 行业卡片 | 解决方案页 | 7 个 `solution-*.html` |
| 活动日程 | 活动页 / 报名 | `event-*.html`、飞书表单 |
| 页脚双 CTA | 转化 | 企业 AI 诊断、报名深圳场 |
| blog / research | 内容 → 转化 | 特区页、近期活动、诊断申请 |

## 7. URL 分阶段规划

### 短期（0–3 个月）— 获客内容基建

| 新增/优化 | 类型 | 关联关键词优先级 |
|-----------|------|-----------------|
| 修复 robots.txt + sitemap.xml | 技术 SEO | 全站 |
| 博客单篇独立 URL + 结构化数据 | 内容页 | P0 信息型词 |
| 活动页模板化 `/event/shenzhen-20260904` | 落地页 | P0 交易型词 |
| 「傅盛亲授 / 一把手 AI 转型」专题页 | 信任 / 转化 | P0 品牌 + 商业型 |
| 行业方案页内链至对应 blog 文章 | 内链 | P1 行业长尾 |

### 中期（3–6 个月）

| 新增/优化 | 类型 | 关联关键词 |
|-----------|------|-----------|
| `/compare/` 对比页（vs 混沌AI院等） | 商业型 | P1 |
| `/cases/` 学员案例集 | 社会证明 | P1 |
| `/glossary/` AI Native 术语表 | 信息型 / GEO | P1 |
| 研究栏目 PDF / 可引用摘要 | 权威内容 | P1 |

### 长期（6–12 个月）

| 新增/优化 | 类型 | 关联关键词 |
|-----------|------|-----------|
| 按城市 programmatic 活动页 | 本地 SEO | P2 |
| 行业 × 场景矩阵页（如「制造业 + 质检 Agent」） | 长尾 | P2 |
| 与 easyaisuite.com 跨域内链体系 | 产品联动 | P2 |

---

*关联：[主文档](./cmainative.md) | [keywords](./cmainative-keywords.md) | [features](./cmainative-features.md) | [competitors](./cmainative-competitors.md) | [use-cases](./cmainative-use-cases.md) | [growth-strategy](./cmainative-growth-strategy.md)*

*Last updated: 2026-08-21*
