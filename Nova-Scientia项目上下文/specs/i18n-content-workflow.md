# Nova Scientia — 多语言内容翻译流程

> 基于 es-MX 示例翻译（`content/locales/es-mx/topics/image-generator.json`）总结的可复用操作流程。
> **Last updated**: 2026-08-08

---

## 一、架构速览

| 项 | 说明 |
|----|------|
| 默认语言 | `pt-br`（巴西葡语），URL 无前缀，内容在 `content/{type}/` |
| 其他语言 | URL 带 `/{locale}/` 前缀，翻译内容在 `content/locales/{locale}/{type}/` |
| 路由生成 | 按**目录里实际存在的 JSON 文件**自动 SSG——放文件即生效，缺文件即 404 |
| 支持 locales | `pt-pt`、`es-mx`、`es-es`、`en`（见 `src/lib/i18n.ts`） |
| 数据层 | `src/lib/content/content-dir.ts` 负责解析：pt-br 读 `content/`，其他读 `content/locales/{locale}/` |

**核心原则**：未翻译的页面在对应语言下直接 404，**绝不回落显示 pt-BR 原文**（避免 hreflang 冲突与低质量混语言页）。

---

## 二、翻译一个页面的完整流程

### 第 1 步：查变体基准

翻译任何 JSON 前，先读 [knowledge/locale-vocabulary.md](../knowledge/locale-vocabulary.md) 确认目标变体：
- **人称系统**（es-AR 用 `vos`、es-ES 用 `vosotros`、pt-PT 用 `estar a` 句式）
- **核心词汇**（`ordenador`/`móvil`、`suscripción`、`gratis` 等）
- **元数据关键词**

### 第 2 步：确定目录与文件名

```
content/locales/{locale}/{type}/{slug}.json
```

| 参数 | 取值 |
|------|------|
| `{locale}` | 小写 locale：`pt-pt`、`es-mx`、`es-es`、`en` |
| `{type}` | `products`、`topics`、`companies` |
| `{slug}.json` | **与 pt-br 源文件同名**（slug 不本地化） |

> 示例：`content/locales/es-mx/topics/image-generator.json` 对应 `content/topics/image-generator.json`。

### 第 3 步：复制源文件并改写

复制 `content/{type}/{slug}.json` 到目标目录，然后**逐字段改写**：

| 字段 | 处理 |
|------|------|
| `slug` / `name` | `slug` 保持不变；`name` 翻译（导航显示名） |
| `seo_title` | 翻译为本地化关键词标题（≤60 字符） |
| `seo_description` | 翻译（≤160 字符） |
| `content.h1` | 翻译，含目标语言主关键词 |
| `content.description` | 翻译 |
| `content.intro` / `content.sections[].paragraphs` | 按变体**改写**（词汇 + 句式 + 人称），非逐词翻译 |
| `content.faqs[].q/a` | 翻译（注意疑问句式：西语 `¿...?`） |
| `content.tldr.*` | 翻译 |
| `content.comparisonTable` | 表头/单元格翻译（产品名、专有名词保留） |
| `content.featuredProducts[].name/description` | 翻译；`slug`、`image` 保持不变 |
| `content.recommendedTopics[].name` | 翻译；`slug` 保持不变 |
| `content.breadcrumbs` | 翻译 label；url 保持不变 |
| `canonical_url` / `og_image` | 保持 `null`（由路由自动生成 locale 版） |

**保持不变的字段**：`slug`、`image` 路径、`cta_url`、`content.sections[].id`、`stats[].value`、价格数值、产品品牌名（Midjourney、DALL-E 等）。

### 第 4 步：可选——section id 本地化

`content.sections[].id`（锚点 id）默认可保持不变；若想本地化（如 `como-escolher` → `como-elegir`），需同步修改 `TopicPage` 的 TOC 逻辑（`buildTocItems` 使用 `section.id`），**且该语言的所有页面保持一致**。建议默认保持与 pt-br 相同，降低维护成本。

### 第 5 步：更新 manifest.json（可选但推荐）

```
content/locales/{locale}/manifest.json
```

```json
{
  "locale": "es-mx",
  "lang": "es-MX",
  "region": "México",
  "lastUpdated": "2026-08-08",
  "translated": {
    "topics": ["image-generator"],
    "products": [],
    "companies": []
  }
}
```

作用：记录该 locale 已翻译的 slug 索引，便于审计覆盖率。**路由不依赖它**（由文件存在驱动）。

### 第 6 步：本地验证

```bash
npm run validate:products   # 结构门禁（slug/breadcrumb/news）
npm run build               # 完整构建，确认新 locale 页面生成
npm start                   # 或 next start -p 3100，然后：
```

| 验证项 | 期望 |
|--------|------|
| `/{locale}/{slug}` | 200，`<html lang>` 正确（如 `es-MX`） |
| `/{locale}/{slug}` 的 `<title>`/canonical/`og:locale` | 本地化值 |
| `/{locale}/` 列表页 | 有内容时 200，无内容时 404 |
| `/{locale}/未翻译slug` | 404（不回落 pt-BR） |
| 页内站内链接 | 全部带 `/{locale}/` 前缀 |
| 无前缀 URL | 仍 200（pt-BR 零影响） |

### 第 7 步：提交

```bash
git add content/locales/
git commit -m "i18n: add {locale} translations for {slug}"
git push origin main    # Vercel 自动部署
npm run indexnow:all    # 提交新 URL（IndexNow 目前只含 pt-BR，全语言扩展见待办）
```

---

## 三、翻译分级策略

| 级别 | 适用 | 必做 | 成本 |
|------|------|------|------|
| **L1 深度** | 高流量主题（llm、image-generator、chatbot、video-generator 等） | 全量改写：人称 + 句式 + 词汇 + 元数据 + 本地补充 | 高 |
| **L2 中度** | 热门产品评测 | 词汇替换 + 句式调整 + 元数据；正文细节可保留 | 中 |
| **L3 轻量** | 长尾产品 | 元数据本地化 + 首段改写；结构化部分复用 | 低 |

**本地化补充**（L1 差异化武器，提升本地相关性）：
- es-AR：提及本地生态（MercadoLibre、Pago Fácil）
- es-MX：用墨西哥定价语境（MXN）
- pt-PT：用欧葡句式（`estar a`），避免巴西口语

---

## 四、示例参考

已完成示例：`content/locales/es-mx/topics/image-generator.json`

改写演示：

| 字段 | pt-BR 源 | es-MX 翻译 | 处理类型 |
|------|----------|------------|----------|
| `seo_title` | `Melhores Geradores de Imagem com IA: Guia e Análise` | `Mejores Generadores de Imágenes con IA: Guía 2026` | 元数据本地化 |
| `h1` | `Geradores de Imagem com IA: Crie Visuais...` | `Generadores de Imágenes con IA: Crea Visuales...` | 翻译 + 动词改写 |
| FAQ 句式 | `Qual o melhor...` | `¿Cuál es el mejor...?` | 疑问句式 |
| 词汇 | `assinatura`（订阅） | `suscripción` | 核心词替换 |
| 词汇 | `gratuito` | `gratis` | 口语偏好 |
| section id | `como-escolher` | `como-elegir` | 锚点本地化（可选） |

---

## 五、关键约束与提醒

- **slug 永不本地化**——`image-generator` 在所有语言下都是 `image-generator`，URL 靠前缀区分
- **未翻译 → 404**，不要回落
- **校验脚本只查结构**（`validate:products`），语言正确性靠 `locale-vocabulary.md` 人工把关
- **section id 本地化需全局一致**，否则 TOC 锚点断裂
- 翻译后新增的 URL 不会自动进 IndexNow（当前 `urls.ts` 只列 pt-BR），全语言 IndexNow/sitemap/hreflang 是待办

---

## 六、相关文档

| 文档 | 用途 |
|------|------|
| [i18n-route-plan.md](i18n-route-plan.md) | 路由与架构规划 |
| [locale-vocabulary.md](../knowledge/locale-vocabulary.md) | 语言变体差异对照表（翻译基准） |
| [content-model.md](content-model.md) | JSON 字段定义 |
| [content-workflow.md](content-workflow.md) | 单语言内容编辑流程 |
| [keyword-map.md](keyword-map.md) | 主题关键词规划（西语版待建） |
