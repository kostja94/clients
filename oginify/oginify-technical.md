# Oginify 技术实现

> **本文档职责**：记录 Oginify 各功能的实现方式——AI 生成管线、截图管线、校验器、前端裁切、模型选择。面向开发者与产品迭代参考。  
> **引用**：[主文档](./oginify.md) 概览 | [features](./oginify-features.md) 产品 | [site-structure](./oginify-site-structure.md) 技术栈 | [others](./oginify-others.md) 成本

---

## 总览：四条管线

| 管线 | 入 | 出 | 关键步骤 | 成本/次 |
|------|----|----|----------|---------|
| **OG Generator** | URL | 2 张 1200×630 PNG | Firecrawl 截图首屏 + Next.js 模板渲染 | ~$0.005 |
| **AI Regenerate** | 单张补生成 | 1 张 1200×630 PNG | Firecrawl 爬取 → LLM 理解 → Gemini/GPT 出图 | ~$0.035 |
| **Validator** | URL | 0–100 评分 + 标签清单 | 抓取 HTML → 解析 meta 标签 → 评分 | ~0 |
| **Twitter Card** | URL / prompt | 1200×675 PNG | 同 OG Generator，尺寸不同 | ~$0.005 |

---

## 1. OG Generator — 核心生成管线

### 1.1 流程

```
用户输入 URL
  │
  ├─→ 1. Firecrawl 抓取
  │      轻度 scrape（~3 次），抓取页面元数据与首屏截图
  │      成本: ~$0.003–0.005
  │      输出: 页面 meta 数据 + 首屏截图
  │
  ├─→ 2. 输出 2 张 1200×630 PNG
  │      第 1 张: Firecrawl 首屏截图 → 裁切 1200×630（非 AI）
  │      第 2 张: Next.js 模板渲染（Satori/resvg，非 AI）
  │      成本: ~$0
  │
  └─→ 3. 返回 2 张 1200×630 PNG → 前端展示 + 下载

（可选）Regenerate:
  用户对某张不满意 → 单独 AI 重新生成 1 张
    管线: Firecrawl 爬取 → aiBrief（LLM 理解）→ Gemini/GPT 出图
    成本: ~$0.032–0.035/张
```

**主流程总成本**: ~$0.005/次（仅 Firecrawl，无 AI 图像成本）
**AI Regenerate 成本**: ~$0.035/张（Firecrawl + LLM + 1 张 AI 图）

### 1.2 模型选择（AI Regenerate 管线）

主流程不调用 AI 图像模型。以下单价仅用于 Regenerate 路径：

| 模型 | API ID | 输出分辨率 | 单张成本 | 优势 | 劣势 |
|------|--------|-----------|---------|------|------|
| Nano Banana 2 (Fast) | `google/gemini-3.1-flash-image-preview` | 1200×630（通过 Lovable AI Gateway） | **$0.030** | 设计感强、速度快 | 经 Gateway，成本可能浮动 ±20% |
| GPT Image 2 (Precise) | `openai/gpt-image-2` | 1536×1024（3:2）| **$0.024** (low quality) | 文字渲染最好、最便宜 | 慢；需前端裁切（~17% 损失） |

当前默认：Fast (Gemini via Lovable Gateway)。**以上价格为 Lovable AI Gateway 转售价**，非 Google/OpenAI 原厂价。降本方案见 [others.md](./oginify-others.md#降本路径)。

### 1.3 尺寸保证

#### 当前（Lovable 托管）

Lovable 内置 Gemini 经 AI Gateway 出图时，**无法稳定依赖原生 1200×630 输出**。实测两类失败：

1. 不约束尺寸 → 输出大于或偏离 1200×630，平台预览裁切不可控  
2. 强制 1200×630 硬裁 → 尺寸达标但主体被切掉（模型常按 1:1 或 3:2 满幅生成）

**当前方案**：预制 prompt 要求所有可读内容落在画面中央 **1200×630 安全区**，安全区外 **留白（纯白）** → 再裁切至 1200×630，裁掉的是留白而非 headline。详见 Build in Public 帖 [social-posts/published/bip-lovable-og-size/jike.md](./social-posts/published/bip-lovable-og-size/jike.md)。

Trade-off：构图偏保守；交付给用户的不保留可见白边。

#### 目标（迁出 Lovable 或 API 层可控时）

Gemini Nano Banana 2 支持 `aspect_ratio` **原生出 1200×630**。如引入 gpt-image-2（1536×1024）等非 1.91:1 模型，客户端 normalization：

```
AI 返回原始尺寸
  │
  ├── 尺寸 == 1200×630 → 直接使用
  ├── 比例 ≈ 1.91:1    → 等比缩放到 1200×630
  └── 比例 ≠ 1.91:1    → cover-center crop
                            (以主导轴为准缩放 → 裁切对面的多余像素)
```

**交付原则**：不 stretch；生成阶段安全区留白 ≠ 最终交付 letterbox（Slack/X 预览会二次裁切，最终图不应带可见白边）。

### 1.4 内容抓取

**当前路径（主流程）**: Firecrawl 轻度抓取（~3 次 scrape），抓取页面元数据 + 首屏截图 → 裁切。无 JSON extract，无 LLM 调用。

**Regenerate 路径**: Firecrawl `v2/scrape` + JSON extract（5 credits）→ aiBrief（Gemini 3 Flash Preview，~$0.002）→ AI 出图。

**优化方向**: 
- 主流程 Firecrawl 调用已极轻量（~$0.003–0.005）
- Regenerate 路径：页面 `og:title`、`og:description`、`og:image` 已完整 → 跳过 JSON extract（省 $0.02）
- `fetch-meta` fallback 已存在，但 `analyze-content` 路径未接短路逻辑

### 1.5 输出策略

每次生成 2 张：
- **第 1 张（截图）**: Firecrawl 抓取首屏 → top-crop 裁切 1200×630，100% 忠实还原页面
- **第 2 张（模板）**: Next.js 模板渲染（Satori/resvg），风格库 6 种可选

AI 图像生成仅用于 Regenerate（用户手动触发补生成），消耗 1 张 AI 配额。

风格库与 `/templates` 页和 social-cards-skills 三方对齐。

---

## 2. Above the Fold — 首屏截图（已整合入 Generator）

首屏截图功能已整合入 Generator 主流程，作为输出的第 1 张图。独立 `/above-the-fold` 页面保留作为免费工具入口。

### 2.1 流程（Generator 内）

```
Generator 输入 URL
  │
  ├─→ Firecrawl 抓取首屏 (viewport: 1200×800)
  │
  ├─→ 裁切为 1200×630
  │     从顶部取 630px（top-crop，非 cover-center）
  │     意图: 保留首屏可见内容（导航 + hero + CTA）
  │
  └─→ 作为 Generator 输出的第 1 张图
```

### 2.2 与模板渲染的裁切差异

| | 截图（第 1 张） | 模板渲染（第 2 张） |
|---|---|---|
| 裁切方式 | top-crop（从顶部取） | N/A（原生 1200×630） |
| 原因 | 保留首屏导航和 hero 信息 | Satori/resvg 精确输出 |
| 成本 | ~$0（Firecrawl 截图费） | ~$0（本地渲染） |

### 2.3 成本

两张图的主流程成本几乎为零——Firecrawl 轻度抓取（~$0.003–0.005）+ 本地模板渲染（$0）。

---

## 3. Validator — OG 标签校验

### 3.1 流程

```
用户输入 URL
  │
  ├─→ 1. 抓取页面 HTML（fetch / Firecrawl 轻量请求）
  │
  ├─→ 2. 解析 <meta> 标签
  │      og:title, og:description, og:image, og:url, og:type
  │      twitter:card, twitter:title, twitter:description, twitter:image
  │
  ├─→ 3. 加权评分（0–100）
  │      高分项: og:image 存在 + 尺寸 ≥1200×630 + 可访问
  │      中分项: og:title/description 长度合适
  │      扣分项: 缺关键标签、尺寸不符、相对 URL
  │
  └─→ 4. 返回评分 + pass/warn/fail 清单 + 5 平台 Preview
```

### 3.2 评分规则

| 标签 | 权重 | Pass 条件 |
|------|------|----------|
| `og:image` | **最高** | 存在、尺寸 ≥1200×630、公开可访问、绝对 URL |
| `og:title` | 高 | 存在、55–65 字符 |
| `og:description` | 高 | 存在、150–200 字符 |
| `twitter:card` | 中 | 存在、值为 `summary_large_image` |
| `twitter:image` | 中 | 存在或与 `og:image` 一致 |
| `og:url` | 低 | 存在、为规范 URL |
| `og:type` | 低 | 存在、为有效类型 |

### 3.3 平台 Preview

对每个被校验的 URL，实时渲染 5 个平台的模拟预览：

| 平台 | 卡片规格 |
|------|---------|
| X / Twitter | `summary_large_image` 卡 |
| Facebook | 标准 link share 卡 |
| LinkedIn | Post link preview |
| Slack | unfurl 卡 |
| Discord | embed 卡 |

---

## 4. Twitter Card Generator — X 专用卡片

### 4.1 与 OG Generator 的差异

| | OG Generator | Twitter Card Generator |
|---|---|---|
| 输出尺寸 | 1200×630 | **1200×675**（2:1） |
| 风格库 | 6 风格 | 同 6 风格 |
| 管线 | 同 AI Generator | 同 AI Generator |
| `twitter:card` 类型 | — | `summary_large_image` |

### 4.2 尺寸差异原因

Twitter/X 的 `summary_large_image` 卡原生比例是 2:1（1200×600），但 X 官方推荐 1200×675（16:9 兼容）以获得最大显示面积。1200×630 的 OG 图在 X 上也兼容，但上下会被裁切。

---

## 5. Templates — 风格模板库

在线展示 6 种风格的视觉效果，供用户在生成前预览每种风格的视觉语言。模板数据与 Generator 的 6 风格库和 social-cards-skills 的 6 种 Satori 模板对齐。

### 5.1 三方对齐

| Oginify Generator | Templates 页 | social-cards-skills |
|-------------------|-------------|---------------------|
| Swiss | Swiss Minimal 模板 | `og-image-generator` Swiss variant |
| Magazine | Magazine Editorial 模板 | `og-image-generator` Magazine variant |
| Terminal | Terminal / CLI 模板 | `og-image-generator` Terminal variant |
| Brutalist | Brutalist 模板 | `og-image-generator` Brutalist variant |
| Newspaper | Newspaper 模板 | `og-image-generator` Newspaper variant |
| Pixel | Pixel Retro 模板 | `og-image-generator` Pixel variant |

---

## 6. 模型选择架构（仅用于 Regenerate）

主流程不调用 AI 图像模型。Regenerate 支持双模型：

### 6.1 模型能力矩阵

| 模型 | 原生横版输出 | 比例 | 相对速度 | 文字渲染 | 单张成本 |
|------|------------|------|---------|---------|---------|
| Gemini NB2 (Fast) | 通过 Lovable AI Gateway | — | 快 | 中 | **$0.030** |
| gpt-image-2 (Precise) | 1536×1024 | 1.5:1 ❌ | 慢 | 最好 | **$0.024** |

> **价格来源**: Lovable AI Gateway 转售价（`src/lib/og-model.server.ts`），非 Google/OpenAI 原厂价。Gateway 价格可能浮动 ±20%。

### 6.2 Prompt 安全区语言

如果引入非 1.91:1 模型，需在 prompt 中注入安全区提示。以下为参考语言：

**Gemini（1.91:1 接近原生）**:
> "Keep logo, headline, and primary subject inside the central 1.91:1 safe-zone — about 4% off the top and bottom edges may be cropped on export."

**GPT Image 2（3:2 → 需大幅裁切）**:
> "Landscape 3:2 frame. Keep logo, headline, and primary subject inside the central 1.91:1 safe-zone — about 17% off the top and bottom edges will be cropped on export. Place the subject and type vertically centered with generous padding."

### 6.3 API 抽象

所有模型调用应通过统一的 `buildImageRequest()` 函数路由：

```ts
type ImageModel = "fast" | "precise";

function buildImageRequest(opts: {
  model: ImageModel;
  prompt: string;          // 已含安全区语言
  refImages?: string[];    // data URLs，可选
}): { endpoint: string; body: unknown };
```

- `"fast"` → Gemini 3.1 Flash Image Preview
- `"precise"` → gpt-image-2

三个生成入口（URL 表单、Text-to-OG、Image-to-OG）接受可选的 `model` 参数，默认 `"fast"`。永远不硬编码模型名称。

---

## 7. 前端裁切合约

如果引入非 1200×630 原生输出的模型，所有 AI 图像在前端必须经过 normalization：

```ts
// 输入: 任意尺寸的 data URL
// 输出: 严格的 1200×630 PNG data URL
async function normalizeToOg(srcDataUrl: string): Promise<string>;
```

决策树：
```
srcDataUrl
  ├── dims == 1200×630        → 重新编码为 PNG，返回
  ├── ratio ≈ 1.91:1 (±0.01)  → 等比缩放至 1200×630
  └── ratio ≠ 1.91:1          → cover-center crop 至 1200×630
```

**决不** letterbox，**决不** stretch。调用点在每个 AI 图像进入 UI state 之前。

---

## 8. 已知技术债

| 项 | 状态 | 影响 |
|----|------|------|
| Regenerate 硬上限 | 待实施（计划 6 次/订单） | PAYG 用户可无限 regenerate，AI 成本爆破风险 |
| 免费用户滥用防护 | 待接入 Turnstile | Cookie 6 张/天 + IP fallback ×3 = $0.54/天/IP |
| AI 使用量埋点 (`ai_usage_log`) | 未实施 | 依赖 Lovable balance 对账会被工作区其他项目污染 |
| Firecrawl 短路逻辑 | 未实现 | Regenerate 路径浪费 ~$0.02/次 |
| Lovable AI Gateway 直连 | 未迁出 | Gemini 经 Lovable AI Gateway；迁独立栈待定 |
| Gallery 条目数 | 未核实 | 文档写"约 100"，后台实际条目数待确认 |
| Above the Fold 截图质量 | 未在 Generator 内验证 | Firecrawl 截图在不同页面结构上的裁切效果待测试 |

---

*Last updated: 2026-06-03. 定价以 Lovable AI Gateway 转售价为准；管线变更（主流程非 AI、2 张输出、Regenerate AI 路径）同步至代码 `src/lib/og-model.server.ts` 和 `src/routes/index.tsx`。*
