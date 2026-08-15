# SenseNova — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./sensenova.md) | [keywords](./sensenova-keywords.md) | [features](./sensenova-features.md) | [competitors](./sensenova-competitors.md) | [use-cases](./sensenova-use-cases.md) | [growth-strategy](./sensenova-growth-strategy.md) | [README](./README.md)

**Last updated**: 2026-07-27 | Phase 0 识别：robots + sitemap + 首页/模型/定价/EN/U1 Pro（[sensenova.cn](https://www.sensenova.cn/)）

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 | 状态 |
|------|---------|-----------|--------|------|
| `/` | 品牌首页（模型 / 原生应用 / 开源生态） | SenseNova, 日日新, SenseNova U1 | P0 | 已上线 |
| `/models` | 模型与办公 Agent 能力页（Flash-Lite / U1 Fast / Cowork-Skills） | multimodal agent, AI PPT, office AI agent | P0 | 已上线 |
| `/token-plan` | Token Plan 订阅 / 公测免费 | SenseNova pricing, Token Plan, API 定价 | P0 | 已上线 |
| `/u1-pro` | U1 Pro 旗舰创意图册 / 作品墙 | SenseNova U1 Pro, AI image generation 8K | P0 | 已上线（未入 sitemap） |
| `/en` | 英文首页 | SenseNova English, native multimodal | P0 | 已上线 |
| `/en/models` | 英文模型页 | SenseNova models, multimodal agent | P0 | 已上线 |
| `/en/token-plan` | 英文定价页 | SenseNova token plan, pricing | P1 | 已上线 |
| `platform.sensenova.cn/docs` | 开发者文档（外链子域） | SenseNova API docs | P0 | 已上线 |
| `platform.sensenova.cn/console` | 控制台 / API Key | SenseNova console, API key | P0 | 已上线 |

访问日期：2026-07-27。来源：[sensenova.cn](https://www.sensenova.cn/) · sitemap lastmod `2026-07-24`

---

## 2. URL 层级与信息架构

```
www.sensenova.cn                    # 营销站（中文默认）
├── /                               # Hero：U1 Pro / U1 / 6.7 Flash-Lite
│   ├── #hero                       # 模型卖点
│   ├── #products                   # 原生应用（小浣熊 / Seko / 如影 / Skills）
│   └── #opensource                 # 开源生态入口
├── /models                         # 原生多模态智能体 + 场景 + Cowork-Skills
├── /token-plan                     # Free 公测 + Lite/Pro 即将上线
├── /u1-pro                         # U1 Pro 作品展示（sitemap 未收录）
├── /en                             # 英文镜像首页
├── /en/models
└── /en/token-plan

platform.sensenova.cn               # 产品平台子域
├── /docs                           # API / 接入文档
└── /console                        # 控制台

github.com/OpenSenseNova            # 开源组织
├── SenseNova-U1
├── SenseNova-Vision
├── SenseNova-SI / MARS / Skills …
└── piccolo-embedding
```

### 首页锚点 IA

| 区域 | 内容 | CTA |
|------|------|-----|
| Nav | 模型 / 产品 / 开源；Token Plan / 文档 / 控制台 | 控制台、English |
| Hero | 「原生多模态，突破技术边界」— U1 Pro / U1 / Flash-Lite | 模型详情 |
| 原生应用 | 办公小浣熊、Seko、如影数字人、SenseNova Skills | 应用入口 |
| 开源生态 | U1、Vision、SI、MARS、Embedding、NEO、Kairos、Skills | GitHub |
| Footer | ICP / 商汤科技 / 问题反馈（飞书表单） | — |

---

## 3. 技术架构

| 维度 | 观测 | 依据 |
|------|------|------|
| 前端 | **Next.js**（`/_next/static/...`） | 首页 HTML 资源路径，2026-07-27 |
| 统计 | 百度统计 `hm.baidu.com` | 首页 script |
| 文档/控制台 | 独立子域 `platform.sensenova.cn` | 主导航外链 |
| 开源 | GitHub `OpenSenseNova` 组织 | 首页 + 新闻披露 |
| robots.txt | `Allow: /`；声明 Sitemap | 2026-07-27 |
| sitemap.xml | 单层 urlset，**6 条 URL**（无 `/u1-pro`） | 2026-07-27；WebFetch 曾 500，curl 可读 |
| 多语言 | 路径前缀 `/en/*`（非子域） | sitemap + 导航 |

---

## 4. 多语言

| 项 | 状态 |
|----|------|
| 主语言 | 简体中文（默认根路径） |
| 英文 | `/en`、`/en/models`、`/en/token-plan` — 内容深度与中文接近 |
| hreflang | ⚠️ 待验证（HTML 未系统核查） |
| 海外独立域名 | **规划中**（用户确认将发布海外独立域名；当前英文挂在 `sensenova.cn/en`） |

> 海外站建议：独立域名承接 EN SEO；保留 `/en` 301 或 hreflang 双向；Token Plan / Console 登录态与区域合规需单独设计。

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| sitemap.xml | `/` `/models` `/token-plan` `/en` `/en/models` `/en/token-plan` | **6** | 2026-07-24 |
| 站内可达但未入 sitemap | `/u1-pro` | 1+ | ⚠️ 待验证 |
| 子域 | `platform.sensenova.cn/{docs,console}` | 文档树 ⚠️ 待爬 | — |
| 开源外链 | `github.com/OpenSenseNova/*` | 多仓库 | — |

**URL 模式归纳**：营销站极简（模型 / 定价 / 语言镜像）；能力叙事集中在 `/models` 长页；旗舰作品在 `/u1-pro`；开发者体验在 `platform.*`。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` | 锚点 + 模型卡 + 开源 GitHub + 导航 | 品牌认知 → 模型/应用/开源 |
| `/models` | Token Plan、场景案例、Cowork-Skills | 办公 Agent 转化 |
| `/token-plan` | Free 开始、Hermes Agent / OpenClaw、控制台 | API / 订阅转化 |
| `/en` | 镜像中文 IA | 海外访客入口（过渡） |
| Nav 常驻 | Docs / Console / Token Plan / English | 开发者与付费路径 |

---

## 7. URL 分阶段规划

| 阶段 | 建议页面 | 对口关键词优先级 | 备注 |
|------|---------|-----------------|------|
| 短期（0–3 月） | 将 `/u1-pro` 纳入 sitemap；补 `/u1` 或 `/models/u1` 独立产品页；About / 技术博客入口 | P0 品牌+U1 | 服务海外独立域名筹备 |
| 中期（3–6 月） | 海外独立域名 EN 全站；`/pricing` 付费档位页；对比页（vs GPT-4o / Gemini / Seedream） | P0/P1 商业词 | Lite/Pro 上线联动 |
| 长期（6–12 月） | 行业解决方案页、案例库、Blog/Docs SEO、Skills 市场页 | P1/P2 长尾 | 与小浣熊/Seko 交叉导流 |

---

## 站点发现摘要（Phase 0）

- 访问日期：2026-07-27
- 官网：https://www.sensenova.cn/
- Sitemap：有；单文件 6 URL；估算营销站极小
- robots.txt：`Allow: /`；声明 Sitemap；未见 AI crawler 特殊 Disallow
- 核心路径：见 §1（≥5）
- URL 模式：`/{models|token-plan|u1-pro}` + `/en/*` + `platform.sensenova.cn/*`
- 内链枢纽：首页锚点、`/models`、Token Plan、Docs/Console
- 技术栈初判：Next.js + 百度统计 + 平台子域
- 待验证项：hreflang；`/u1-pro` 未入 sitemap 原因；platform docs URL 全量；海外域名上线时间
- 建议模式：**多文件**（产品线清晰、有定价/竞品/开源、有展示需求）

---

*阶段*：Demo 冷启动 · *品牌*：SenseNova / 日日新 · *官网*：[sensenova.cn](https://www.sensenova.cn/)
