# Nova Scientia — 多语言内容翻译流程

> 基于 es-MX 示例翻译（`content/locales/es-mx/topics/image-generator.md`）总结的可复用操作流程。
> **Last updated**: 2026-08-29

---

## 一、架构速览

| 项 | 说明 |
|----|------|
| 默认语言 | `pt-br`（巴西葡语），URL 无前缀，内容在 `content/{type}/` |
| 其他语言 | URL 带 `/{locale}/` 前缀，翻译内容在 `content/locales/{locale}/{type}/` |
| 路由生成 | 按**目录里实际存在的文件**自动 SSG——放文件即生效，缺文件即 404 |
| 支持 locales | `pt-pt`、`es-mx`、`es-es`、`en`（见 `src/lib/i18n.ts`） |
| 数据层 | `src/lib/content/content-dir.ts` 负责解析：pt-br 读 `content/`，其他读 `content/locales/{locale}/` |

**核心原则**：未翻译的页面在对应语言下直接 404，**绝不回落显示 pt-BR 原文**（避免 hreflang 冲突与低质量混语言页）。

**格式说明**：pt-BR 主题为 `content/topics/{slug}.md`；翻译版同样为 MD，frontmatter 与正文结构一致。

---

## 二、翻译一个页面的完整流程

### 第 1 步：查变体基准

翻译任何内容前，先读 [knowledge/locale-vocabulary.md](../knowledge/locale-vocabulary.md) 确认目标变体：
- **人称系统**（es-AR 用 `vos`、es-ES 用 `vosotros`、pt-PT 用 `estar a` 句式）
- **核心词汇**（`ordenador`/`móvil`、`suscripción`、`gratis` 等）
- **元数据关键词**

### 第 2 步：确定目录与文件名

```
content/locales/{locale}/{type}/{slug}.md    # 主题
content/locales/{locale}/{type}/{slug}.json  # 产品/公司（未来）
```

| 参数 | 取值 |
|------|------|
| `{locale}` | 小写 locale：`pt-pt`、`es-mx`、`es-es`、`en` |
| `{type}` | `products`、`topics`、`companies` |
| `{slug}` | **与 pt-br 源文件同名**（slug 不本地化） |

> 示例：`content/locales/es-mx/topics/image-generator.md` 对应 `content/topics/image-generator.md`。

### 第 3 步：复制源文件并改写

复制 `content/{type}/{slug}.md`（或 `.json`）到目标目录，然后**逐字段改写**：

**主题 MD（frontmatter + 正文）**：

| 字段 / 区块 | 处理 |
|-------------|------|
| `slug` / `name` | `slug` 保持不变；`name` 翻译 |
| `seo_title` / `seo_description` | 翻译为本地化关键词（≤60 / ≤160 字符） |
| `h1` / `description` | 翻译 |
| 正文 `<!-- block:section -->` 段落 | 按变体**改写**（词汇 + 句式 + 人称） |
| `faqs` | 翻译（注意疑问句式：西语 `¿...?`） |
| `tldr` / `comparisonTable` / `featuredProducts` | 翻译文案；`slug`、`image` 路径不变 |
| `recommendedTopics[].name` | 翻译；`slug` 不变 |
| section 锚点 `{#id}` | 默认可保持与 pt-br 相同（降低 TOC 维护成本） |
| `canonical_url` / `og_image` | 保持 `null` |

**产品/公司 JSON**（流程同前，字段见 [content-model.md](content-model.md)）：

| 字段 | 处理 |
|------|------|
| `content.breadcrumbs[].name` | 翻译；`url` 保持不变 |
| 其余 | 同单语言编辑流程 |

**保持不变的字段**：`slug`、图片路径、`cta_url`、价格数值、产品品牌名（Midjourney、DALL-E 等）。

### 第 4 步：更新 manifest.json（可选但推荐）

```
content/locales/{locale}/manifest.json
```

```json
{
  "locale": "es-mx",
  "lang": "es-MX",
  "region": "México",
  "lastUpdated": "2026-08-29",
  "translated": {
    "topics": ["image-generator"],
    "products": [],
    "companies": []
  }
}
```

作用：记录该 locale 已翻译的 slug 索引，便于审计覆盖率。**路由不依赖它**（由文件存在驱动）。

### 第 5 步：本地验证

```bash
npm run validate:products   # 产品结构门禁（产品翻译时）
npx tsx scripts/permanent/verify-topic-md-roundtrip.ts   # 主题 MD 解析
npm run build               # 完整构建，确认新 locale 页面生成
```

| 验证项 | 期望 |
|--------|------|
| `/{locale}/{slug}` | 200，`<html lang>` 正确（如 `es-MX`） |
| `/{locale}/{slug}` 的 `<title>`/canonical/`og:locale` | 本地化值 |
| `/{locale}/未翻译slug` | 404（不回落 pt-BR） |
| 页内站内链接 | 全部带 `/{locale}/` 前缀 |
| 无前缀 URL | 仍 200（pt-BR 零影响） |

### 第 6 步：提交

```bash
git add content/locales/
git commit -m "i18n: add {locale} translations for {slug}"
git push origin main    # Vercel 自动部署
npm run indexnow:all
```

---

## 三、翻译分级策略

| 级别 | 适用 | 必做 | 成本 |
|------|------|------|------|
| **L1 深度** | 高流量主题（llm、image-generator、chatbot 等） | 全量改写：人称 + 句式 + 词汇 + 元数据 | 高 |
| **L2 中度** | 热门产品评测 | 词汇替换 + 句式调整 + 元数据 | 中 |
| **L3 轻量** | 长尾产品 | 元数据本地化 + 首段改写 | 低 |

---

## 四、示例参考

已完成示例：`content/locales/es-mx/topics/image-generator.md`

| 字段 | pt-BR 源 | es-MX 翻译 | 处理类型 |
|------|----------|------------|----------|
| `seo_title` | `Melhores Geradores de Imagem...` | `Mejores Generadores de Imágenes...` | 元数据本地化 |
| FAQ 句式 | `Qual o melhor...` | `¿Cuál es el mejor...?` | 疑问句式 |
| 词汇 | `gratuito` | `gratis` | 口语偏好 |

---

## 五、关键约束与提醒

- **slug 永不本地化**
- **未翻译 → 404**，不要回落
- **主题用 MD**，与 pt-BR 源结构一致
- section 锚点 id 本地化需全局一致，否则 TOC 断裂

---

## 六、相关文档

| 文档 | 用途 |
|------|------|
| [i18n-route-plan.md](i18n-route-plan.md) | 路由与架构规划 |
| [locale-vocabulary.md](../knowledge/locale-vocabulary.md) | 语言变体差异对照表 |
| [content-model.md](content-model.md) | 字段定义 |
| [content-workflow.md](content-workflow.md) | pt-BR 内容编辑流程 |
| [keyword-map.md](keyword-map.md) | 主题关键词规划 |
