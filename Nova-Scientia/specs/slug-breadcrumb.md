# Nova Scientia — 命名规则与面包屑规范

本文档定义 Nova Scientia 项目全量的**命名规则、slug 约束、面包屑一致性规则**。

适用范围：上下文仓内目录命名、部署仓 `content/` 文件命名、产品/主题 slug、以及产品页面包屑 URL 一致性检查。

---

## 〇、命名总则

### 0.1 文件命名

| 规则 | 说明 |
|------|------|
| 大小写 | 除 `README.md` 外，文件名默认 **全小写** |
| 分段 | **kebab-case**（`-` 连接） |
| 目录名 | 子目录使用小写 kebab-case |

### 0.2 部署仓 `content/` 路径

| 类型 | 路径 | 规则 |
|------|------|------|
| 产品 | `content/products/{slug}.json` | slug = 文件名（kebab-case），见 §一 |
| 主题 | `content/topics/{slug}.md` | 与 URL `/{slug}` 一致；frontmatter `slug` 须匹配 |
| 公司 | `content/companies/{slug}.json` | 与 URL `/company/{slug}` 一致 |
| 词汇表 | `content/glossary.json` | 由 `scripts/ref/glossary/merge-glossary.mjs` 合并生成 |

### 0.3 版本追踪笔记

`knowledge/topics/{slug}.md` 的 basename 必须与 `content/topics/{slug}.md` 的 slug 对齐。

---

## 一、Slug 基本规则

### 1.1 文件名一致性

JSON 文件名必须与内部的 `slug` 字段一致：

```
content/products/chatgpt.json → data.slug === "chatgpt" ✅
content/products/leonardo-ai.json → data.slug === "leonardo-ai" ✅
content/products/leonardo-ai.json → data.slug === "leonardo-ia" ❌
```

验证脚本会检查每个 JSON 文件：
```js
const expectedSlug = f.replace(/\.json$/, '');
if (data.slug !== expectedSlug) { /* 报错 */ }
```

### 1.2 命名格式

- 所有 slug 必须使用 **kebab-case**（小写字母 + 连字符）
- 使用品牌名的标准写法：`janitor-ai`（非 `janitor-ia`）、`chatgpt`（非 `chat-gpt`）
- 限制使用 ASCII 字母、数字、连字符

---

## 二、禁止的 Slug

### 2.1 ISO 639-1 两字母语言代码

共 183 个两字母代码（定义在 `scripts/lib/iso639-1-alpha2.json` 中），禁止作为产品 slug。

**示例**：`en`、`pt`、`de`、`ja`、`zh` 等

**原因**：这些 slug 会与多语言 URL 路径混淆（如 `/en`、`/pt`），Google 可能将其解读为语言变体页。

**已知修正案例**（`scripts/sync-products-from-api.js` 中 `API_SLUG_OVERRIDES`）：
- `en` → `make`（`make.com/en` 被 API 误解析）
- `ai` → `linear-ai`（`linear.app/ai` 被误解析）

### 2.2 保留路径冲突

以下 slug 与站点路由、CMS 路径或系统保留项冲突，**禁止作为产品 slug**：

| Slug | 冲突原因 |
|------|----------|
| `home` | 首页路径 |
| `ai` | ISO 639-1 + 常见路径片段 |
| `categoria` | `/products/categoria/*` 分类路径 |
| `index` | 目录索引文件 |
| `page` | 通用路由片段 |
| `app` | 应用路由片段 |
| `new` | `/new` 常见新建路径 |
| `admin` | 后台管理路径 |
| `api` | API 路由 |
| `login` | 登录页 |
| `signup` | 注册页 |
| `search` | 搜索页 |
| `settings` | 设置页 |
| `dashboard` | 后台面板 |

### 2.3 误用的路径片段

API 同步时可能将完整 URL 的路径片段误解析为 slug。`scripts/sync-products-from-api.js` 通过 `API_SLUG_OVERRIDES` 修正：

- `home`（来自 `you.com/home`）→ `you-com`
- `en`（来自 `make.com/en`）→ `make`
- `ai`（来自 `linear.app/ai`）→ `linear-ai`

新增产品时如遇到类似问题，请在此映射中添加。

---

## 三、面包屑规则

### 3.1 最后一项 URL 一致性

产品 JSON 中 `content.breadcrumbs` 的最后一项 `url` 必须指向正确的产品页路径：

```json
{
  "content": {
    "breadcrumbs": [
      { "name": "Início", "url": "/" },
      { "name": "Produtos", "url": "/products" },
      { "name": "ChatGPT", "url": "/products/chatgpt" }
    ]
  }
}
```

**规则**：`breadcrumbs[last].url` 必须等于 `/products/{slug}`。字段名为 `name`（非 `label`）；`BreadcrumbNav` 组件内部映射为显示 label。

`scripts/sync-products-from-api.js` 中的 `normalizeBreadcrumbUrl()` 函数会在同步时自动修正不匹配的面包屑 URL。

### 3.2 验证命令

```bash
npm run validate:products   # 检查 slug 与 breadcrumb 一致性
npm run build               # 自动运行 validate:products 作为门禁
```

---

## 四、News 字段规则

产品 JSON 中 `content.news` 数组的每一项必须满足：

| 字段 | 规则 |
|------|------|
| `title` | `string`，非空 |
| `summary` | `string`，非空 |
| `date` | `string`，非空 |
| `url` | `string`（可选） |
| `source` | `string`（可选） |

验证脚本会对每个 news item 检查 `title`、`summary`、`date` 三个必填字段。

---

## 五、添加新产品的检查清单

1. JSON 文件名 = `{slug}.json`（kebab-case）
2. 内部 `slug` 字段与文件名一致
3. Slug 不在 ISO 639-1 列表中
4. Slug 不在保留/冲突列表中
5. `content.breadcrumbs` 最后一项 url 为 `/products/{slug}`
6. 如有 `content.news`，每项 title/summary/date 非空
7. 运行 `npm run validate:products` 通过
