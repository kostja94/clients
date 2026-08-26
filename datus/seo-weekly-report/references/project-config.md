# Datus Project Config — seo-weekly-report

> **自包含约束**：Agent 与脚本执行时只读本文件夹内文件；站点事实已全部内嵌于下文，**禁止**读取上级 `datus-*.md`、`datus/blog/` 原文（blog 数据通过 `blog-catalog.yaml` 同步）。

## Site Facts

| 字段 | 值 |
|------|-----|
| **Brand** | Datus |
| **Primary domain** | datus.ai |
| **GSC property** | `https://datus.ai/` |
| **Product** | Open-source data engineering agent — evolvable context for data systems |
| **Stage** | 早期 SEO（~56+ blog，GitHub ~1.2K stars，自然搜索基数低） |
| **Locale** | EN 主站；`/zh` 仅营销页镜像（**不含** `/blog/**`） |

## 独立域（不在本 skill GSC 范围）

| 域名 | 说明 |
|------|------|
| docs.datus.ai | 产品文档（56 EN + 56 ZH） |
| studio.datus.ai | 云端产品 / 登录注册 |
| dosi.datus.ai | OSI 执行引擎文档 |
| github.com/Datus-ai/Datus-agent | 开源仓库 |

## URL 模型

| 类型 | 路径 | 说明 |
|------|------|------|
| 首页 | `/` | 品牌 + 品类 |
| 产品 | `/products/cli/` 等 | CLI / VS Code / Studio / Enterprise |
| Blog | `/blog/{slug}/` | **所有长文 canonical**（Glossary + DE Agent + OSI） |
| Glossary 索引 | `/glossary/` | 聚合页，非术语正文 URL |
| OSI 工具 | `/osi-field-mapping/`、`/tools/osi-playground/` | 非 blog，战略 SEO 页 |
| 定价 | `/pricing/` | 转化 |

## Blog Category → 内容簇

| frontmatter `category` | 内容簇 |
|------------------------|--------|
| Glossary | glossary |
| Data Engineering Agent | de-agent |
| Semantic Layer | semantic-layer |
| Comparison | comparison |
| Case Study | case-study |

## Landing Page Types（脚本与 AI 共用）

| pageType | 路径模式 | 商业意图 |
|----------|----------|----------|
| `homepage` | `/` | 品牌 |
| `blog` | `/blog/*` | 内容 SEO |
| `glossary-index` | `/glossary` | 术语索引 |
| `product` | `/products/*` | 产品探索 |
| `pricing` | `/pricing` | 购买意向 |
| `osi-tool` | `/osi-field-mapping/`, `/tools/osi-playground/` | OSI 漏斗 |
| `integrations` | `/integrations/` | 集成 |
| `faq` | `/faq/` | 支持 |
| `zh` | `/zh/*` | 中文营销页 |
| `other` | 其余 | — |

## SEO 生命周期（Datus 早期）

| 阶段 | 特征 |
|------|------|
| 冷启动 | 全站周 GSC 点击 < 20 |
| 内容扩张期 | 曝光涨、点击滞后，Glossary 批量收录 |
| 品类词起量 | `data engineering agent`、`semantic layer` 进 Top query |
| OSI 红利期 | OSI 工具页 + OSI vs 文获独立流量 |
| 稳定增长 | 非品牌占比 > 60% |

## Report Thresholds（早期站点）

| 指标 | 健康 🟢 | 关注 🟡 | 干预 🔴 |
|------|---------|---------|---------|
| 周 GSC 点击环比 | +10% ~ +100% | -20% ~ +10% | 连续 2 周 < -30% |
| 品牌词点击占比 | 20–60% | < 15% 或 > 80% | 需解释 |
| Blog 新文首周曝光 | ≥ 10 | 1–9 | 0 且已发布 ≥7 天 |
| 高曝光低 CTR | CTR ≥ 1% | 0.3–1% | 曝光 >500 且 CTR < 0.1% |
| GSC 点击 vs GA4 organic | 0.8–1.5× | 0.5–0.8 或 1.5–2.0 | > 2.0 或 < 0.5 |

## 转化事件（默认，以 GA4 实测为准）

| 事件名 | 含义 |
|--------|------|
| `github_click` | GitHub CTA |
| `file_download` | 文件下载 |
| `sign_up` | 注册 |
| `login` | 登录 |
| `generate_lead` | 线索 |

## Blog 联动规则

1. 每周一运行 `npm run sync-blog` 更新 `blog-catalog.yaml`
2. `merge` 脚本自动识别 `period.current` 内 `date` 的新文章
3. §11 / §13 必须交叉：新发布 slug × GSC 首周表现 × GA4 落地页
4. 手工块 `===CONTENT===` 补充 CMS 发布日与实际 slug（frontmatter date 可能≠上线日）

*Last updated: 2026-08-24 · v1.0.0 self-contained*
