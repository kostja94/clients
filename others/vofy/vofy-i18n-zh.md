# Vofy 多语种（i18n）方案

> 关联：[vofy-site-structure.md](./vofy-site-structure.md) · [vofy-sitemap-optimization-zh.md](./vofy-sitemap-optimization-zh.md) · [vofy-keywords.md](./vofy-keywords.md) · [apps/03-vofy-apps-howto-implementation-zh.md](./apps/03-vofy-apps-howto-implementation-zh.md) · [blog/README.md](./blog/README.md)

**官网**：[vofy.art](https://www.vofy.art/)  
**最后更新**：2026-06-15  
**首增语言**：简体中文（`zh`）

---

## 一、设计原则

| 原则 | 说明 |
|------|------|
| **英文为默认语，无前缀** | 现有 `/apps/...`、`/models/...`、`/blog/...` 全部保持不变，避免 SEO 震荡 |
| **新语言用路径前缀** | 中文：`/zh/...` |
| **Slug 跨语言共用** | `/apps/ai-kissing-video` 与 `/zh/apps/ai-kissing-video` 共用同一 slug，只换文案 |
| **Blog 不迁移** | 59 篇英文文章、`/blog` 索引页保持纯英文，不参与 hreflang 配对 |
| **渐进上线** | 按路由模块分批，未翻译页面不进入 sitemap |
| **Studio 产品层解耦** | `/studio/*` 工作台 UI 与营销 SEO 分阶段处理 |

---

## 二、URL 策略

### 2.1 路径对照

| 英文（默认） | 中文 | 备注 |
|-------------|------|------|
| `/` | `/zh/` | 首页 |
| `/apps` | `/zh/apps` | 工具目录 |
| `/apps/{slug}` | `/zh/apps/{slug}` | slug 不变 |
| `/models` | `/zh/models` | 模型聚合 |
| `/models/{vendor}/{version}` | `/zh/models/{vendor}/{version}` | 路径段不变 |
| `/pricing` | `/zh/pricing` | 定价 |
| `/canvas` | `/zh/canvas` | 新产品页 |
| `/privacy` | `/zh/privacy` | 需独立法务稿 |
| `/terms` | `/zh/terms` | 需独立法务稿 |
| `/blog` | `/blog` | **始终英文，无 `/zh/blog`** |
| `/blog/{slug}` | `/blog/{slug}` | **同上** |
| `/studio/*` | `/studio/*` | 暂不加 locale 前缀 |

### 2.2 hreflang 规则

**有中文版本的页面**（Apps、Models、核心营销页）：

```html
<link rel="alternate" hreflang="en" href="https://www.vofy.art/apps/ai-kissing-video" />
<link rel="alternate" hreflang="zh-Hans" href="https://www.vofy.art/zh/apps/ai-kissing-video" />
<link rel="alternate" hreflang="x-default" href="https://www.vofy.art/apps/ai-kissing-video" />
```

**Blog 页**（仅英文）：

```html
<link rel="alternate" hreflang="en" href="https://www.vofy.art/blog/nano-banana-2-guide" />
<link rel="alternate" hreflang="x-default" href="https://www.vofy.art/blog/nano-banana-2-guide" />
```

中文 App 页内链到 Blog 时，直接链 `/blog/...`，UI 标注「English」。

---

## 三、迁移范围

### 3.1 渐进迁移

| 模块 | 优先级 | 说明 |
|------|--------|------|
| **`/apps` + 单工具页** | P0 | 程序化 SEO 主战场；已有 Style/Filter/Effect/Edit 中文模板 |
| **`/models` + 14 模型页** | P1 | 模型名本身国际化；中文补「怎么用 / 定价 / 对比」 |
| **首页 `/`** | P0 | Hero、What's New、导航，与 Apps 同步 |
| **`/pricing`** | P2 | 转化关键；Credits 说明需对齐 |
| **`/canvas`** | P2 | 新产品页，可与中文同步 |
| **`/privacy` `/terms`** | P2 | 独立法务版本，非简单机翻 |

### 3.2 不迁移

| 模块 | 理由 |
|------|------|
| **`/blog/*`（59 篇）** | 已索引、hub-spoke 内链完整；Blog Skill 规定 `locale: en` |
| **`/studio/*`** | 需登录、不索引；产品 UI 复杂度高 |
| **`/explore`** | 可能需登录 |
| **`/assets`** | 视是否公开 SEO 页再定 |

---

## 四、技术架构

> 线上推断为 Next.js App Router；具体实现以工程仓库为准。

### 4.1 目录结构（目标态）

```
app/
├── [locale]/                    # locale = en | zh
│   ├── layout.tsx               # 语言切换器、nav、footer
│   ├── page.tsx                 # 首页
│   ├── apps/
│   │   ├── page.tsx
│   │   └── [slug]/page.tsx
│   ├── models/
│   │   ├── page.tsx
│   │   └── [vendor]/[version]/page.tsx
│   ├── pricing/page.tsx
│   ├── canvas/page.tsx
│   └── (legal)/privacy|terms/page.tsx
├── blog/                        # 无 [locale]，始终英文
│   ├── page.tsx
│   └── [slug]/page.tsx
└── studio/                      # 无 [locale]
    └── ...
```

### 4.2 Middleware 行为

| 请求路径 | 行为 |
|---------|------|
| `/` | `locale=en`，无前缀（canonical） |
| `/zh/...` | `locale=zh` |
| `/blog/...` | 强制 `en`，忽略 `Accept-Language` |
| `/studio/...` | 产品默认 `en`；UI 语言可后期用 cookie 切换 |
| `Accept-Language: zh-CN` | 可选跳转 `/zh/`（仅 marketing 页，不作用于 `/blog`） |

**部署注意**：
- 若有反向代理，须原样转发 `/zh/:path*`，不能剥前缀
- `/_next/static/*` 与 locale 无关，共用一套规则
- `metadataBase` 固定 `https://www.vofy.art`

### 4.3 CMS 内容模型

```yaml
# App 工具页示例
slug: ai-kissing-video          # 全局唯一，跨语言共用
translations:
  en:
    title: "AI Kissing Video Generator"
    h1: "..."
    howto_steps: [...]
    faq: [...]
    meta_description: "..."
  zh:
    title: "AI 亲吻视频生成器"
    h1: "..."
    howto_steps: [...]
    faq: [...]
    meta_description: "..."
    status: published | draft | missing
```

Blog 文章**不加** `translations.zh`。

### 4.4 未翻译页面策略

| 策略 | 说明 |
|------|------|
| **404**（推荐） | `/zh/apps/{slug}` 无中文稿 → 404，sitemap 不收录 |
| **英文 fallback + noindex** | 仅过渡；不能配 hreflang |
| **301 到英文版** | 不推荐 |

---

## 五、分阶段路线图

### Phase 0 — 基础设施（1–2 周）

| 任务 | 产出 |
|------|------|
| i18n 路由骨架 | `[locale]` + middleware |
| 全局 Shell 翻译 | Nav、Footer、语言切换器 |
| 文案资源 | `messages/en.json`、`messages/zh.json` |
| PostHog 约定 | `locale`、`first_landing_path` 含 `/zh/` 前缀 |
| Sitemap 预备 | 见 §七 |

**验收**：`/zh/` 可访问；`/blog` 仍纯英文；现有英文 URL 全部 200 不变。

---

### Phase 1 — `/apps` 聚合 + 类目 Hub（2–3 周）

| 批次 | 范围 |
|------|------|
| 1a | `/apps` 索引页 + Tab 文案 |
| 1b | 类目 Hub（Effects、Anime、Headshots 等 10 子类） |
| 1c | Featured 8 条 + Video 类 8 条 |

URL 示例：
- `https://www.vofy.art/zh/apps`
- 类目可用 query（`?category=effects`）或独立 pillar 路径（`/zh/apps/effects`），以实现为准

---

### Phase 2 — `/apps/{slug}` 单工具页（滚动，4–8 周）

| Sprint | 数量 | 品类 |
|--------|------|------|
| 2-A | 15–20 | Video 特效（Kiss/Hug/Pet 等） |
| 2-B | 20–25 | Filter / Style 高频 |
| 2-C | 20–25 | Edit / Headshots / Cleanup |
| 2-D | 剩余 | 长尾补齐 |

**每页必译字段**（对齐 [HowTo 方案](./apps/03-vofy-apps-howto-implementation-zh.md)）：
- Title / H1 / Meta description
- HowTo 3–4 步
- FAQ 3–5 条
- CTA 文案（→ `/studio/...` 链接不变）

---

### Phase 3 — `/models`（2–3 周）

| 页面 | 翻译重点 |
|------|----------|
| `/models` Hub | 模型对比表、选型指南 |
| 14 个单模型页 | 能力描述、Credits 区间、Quick Start HowTo |

Blog 中的模型教程仍链英文 `/blog/...`；中文模型页可加「Read full guide (EN)」。

---

### Phase 4 — 核心转化页（1–2 周）

| 页面 | 说明 |
|------|------|
| `/zh/pricing` | 套餐名可保留英文（Credits / Pro），说明中文化 |
| `/zh/canvas` | 与 AI Canvas 产品页同步 |
| `/zh/privacy` `/zh/terms` | 法务审校版 |

---

### Phase 5 — 产品 UI（后期）

| 模块 | 策略 |
|------|------|
| `/studio/*` | Cookie / 用户设置切换 UI 语言；URL 不加 `/zh/` |
| `/explore` | 视产品优先级 |
| 邮件 / 通知 | 独立 i18n 资源 |

---

## 六、Blog：英文-only 处理

**产品侧**
- 语言切换器在 `/blog` 下隐藏或置灰；切换中文后跳转 `/zh/` 首页
- 中文 App 页「Related guides」→ 英文 Blog，标注语言

**SEO 侧**
- `blog-sitemap.xml` 仅含 `/blog/*`
- Blog 页不输出 `hreflang="zh-Hans"`

**内容策略**
- 中文获客靠 Apps 长尾页 + 模型页，不翻译 59 篇 Blog
- 若需中文内容营销，走独立渠道，不进主站 Blog

---

## 七、Sitemap

在 [sitemap 优化计划](./vofy-sitemap-optimization-zh.md) 拆分基础上扩展：

```
/sitemap.xml                    → index
/pages-sitemap.xml              → 英文核心页 + models
/pages-zh-sitemap.xml           → /zh/ 已发布核心页（新增）
/apps-sitemap.xml               → 英文 apps
/apps-zh-sitemap.xml            → 已译中文 apps（随批次增长）
/blog-sitemap.xml               → 仅英文
```

**规则**：
- 中文 sitemap 只收录 `status: published` 的翻译
- 每对 en/zh URL 互指 hreflang
- `x-default` 始终指向英文无前缀 URL

---

## 八、本地化文档来源

| CMS 字段 | 本地文档 |
|---------|---------|
| App 页 H1 / 区块结构 | `apps/vofy-*-apps-guide-zh.md` |
| HowTo 步骤 | `apps/03-vofy-apps-howto-implementation-zh.md` |
| 品类定义 | `apps/01-vofy-style-effect-filter-framework-zh.md` |
| 关键词意图 | `vofy-keywords.md` §二 |
| Blog 内链白名单 | `blog/skills/vofy-blog-article/SKILL.md` §1.1（仍指向英文路径） |

---

## 九、语言切换器

- 在 `/apps/ai-kissing-video` 选中文 → `/zh/apps/ai-kissing-video`（若已译）或 `/zh/apps`（若未译）
- 在 `/blog/...` 选中文 → `/zh/`
- 选择写入 `NEXT_LOCALE` cookie

---

## 十、归因（PostHog）

| 属性 | 约定 |
|------|------|
| `locale` | `en` \| `zh` |
| `first_landing_path` | 保留完整前缀，如 `/zh/apps/ai-kissing-video` |
| `content_language` | 页面正文语言 |
| Blog 阅读 | 始终 `locale=en` |

---

## 十一、风险与规避

| 风险 | 规避 |
|------|------|
| 重复内容 | hreflang 配对 + 中文改写 meta/H1 |
| 中文页链英文 Blog 跳出 | 明确标注语言；App FAQ 吸收 Blog 核心信息 |
| Apps 计数不一致（85 vs 108+） | Phase 2 前导出 CMS 全量 slug |
| 未译页 404 | Hub 只展示已译工具 |
| Studio 链接跨语言 | Studio URL 全球统一，仅 CTA 文案本地化 |

---

## 十二、MVP（4 周可验证）

1. Phase 0 基础设施 + 中文 Shell
2. `/zh/` 首页（Hero + What's New 中文）
3. `/zh/apps` 聚合页
4. **20 个** P0 App 单页（Video 8 + Style/Filter 高频 12）
5. `apps-zh-sitemap.xml`（仅这 20 条）
6. 语言切换器 + hreflang

**明确不做**：Blog 翻译、Studio UI、全量 Apps、法务页。

---

## 十三、进度跟踪

| Phase | 范围 | 状态 | 目标完成 |
|-------|------|------|----------|
| 0 | 基础设施 | Pending | — |
| 1 | `/apps` Hub | Pending | — |
| 2-A | Apps Video 15–20 | Pending | — |
| 2-B | Apps Filter/Style 20–25 | Pending | — |
| 2-C | Apps Edit/Headshots 20–25 | Pending | — |
| 2-D | Apps 长尾补齐 | Pending | — |
| 3 | `/models` | Pending | — |
| 4 | pricing / canvas / legal | Pending | — |
| 5 | Studio UI | Pending | — |

**已译 App slug 登记表**：（随实施填写）

---

*Demo 方案文档 · 实施前需与 Vofy 工程团队确认 CMS 与路由实现方式。*
