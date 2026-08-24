# Meta 四要素完整规则

> **来源**：`content/templates/template-tools.md` §二、`content/sections/section-meta-copy.md`
> **版本**：v2.0 · 2026-06-23

---

## 一、四要素速查

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| **Meta title** | 必须含「最佳」；`（2026）` + `：` + 副线；禁止「`（2026）\| Alignify`」无副线直连 | 必须含 `Best`；`(2026)` + `:` + subtitle |
| **Meta description** | 列举 2–3 个代表产品名；由 TL;DR 与 bestTools 支撑；60–80 字 | 列举 2–3 个代表产品名；120–160 字符 |
| **H1** | 不写年份；推荐「类型：核心价值」格式；不强制含「最佳」 | 不写年份；40–60 字符 |
| **Excerpt** | 三段式、80–150 字；避免通用结尾（如「这将帮助你更好地理解和应用」） | 三段式、200–250 字符 |

---

## 二、Meta Title 格式模板

### 中文
```
最佳{工具类型}（2026）：{2-4个差异化标签，顿号分隔} | Alignify
```

**示例**：
- ✅ `最佳AI图片生成器（2026）：文生图、图生图、AI写真 | Alignify`
- ❌ `AI图片生成器（2026）| Alignify`（缺少「最佳」、无副线）
- ❌ `最佳AI图片生成器（2026）| Alignify`（无冒号副线）

### 英文
```
Best {Tool Type} (2026): {2-4 differentiating tags} | Alignify
```

**示例**：
- ✅ `Best AI Image Generators (2026): Text-to-Image, AI Avatars, Photo Editing | Alignify`
- ❌ `AI Image Generators (2026) | Alignify`（缺少 `Best`、无冒号副线）

---

## 三、Meta Description 格式模板

### 中文（60–80 字）
```
探索2026年最佳{工具类型}：{产品A}、{产品B}等。比较{核心功能}，{用户收益}。立即探索站内完整指南，免费阅读。
```

### 英文（120–160 字符）
```
Explore the best {tool type} in 2026: {Product A}, {Product B}, and more. Compare {key features} and find the right tool for {use case}. Free guide — read now.
```

---

## 四、H1 格式

### 中文
```
{工具类型}：{核心价值描述}
```

**示例**：`AI图片生成器：从文字到视觉的智能创作工具`

### 英文
```
{Tool Type}: {Core Value Proposition}
```

**示例**：`AI Image Generators: Intelligent Visual Creation from Text`

---

## 五、Excerpt 格式

### 中文（三段式，80–150 字）
```
段落1：品类定义 + 核心价值
段落2：2026年关键趋势或用户痛点
段落3：本文帮助读者做什么
```

**禁止结尾**：「这将帮助你更好地理解和应用这些先进的技术工具，提升工作效率和创造力。」

### 英文（三段式，200–250 字符）
```
Para 1: Category definition + core value
Para 2: 2026 trend or user pain point
Para 3: What this guide helps the reader do
```

---

## 六、publishDate 双源同步

| 位置 | 格式 | 用途 |
|------|------|------|
| `blog-meta.ts` → slug 级 `publishDate` / `modifiedDate` | ISO `2026-06-23T00:00:00+08:00` | SEO、OG、sitemap |
| md frontmatter `date` / `updated` | 中文 `"2026年6月23日"` / 英文 `"June 23, 2026"` | Hero 展示 |

**同一日历日，两处须一致。** `publishDate` 创建后永不更改；`modifiedDate` 每次内容更新时同步 meta + frontmatter `updated`。

## 七、Tools 文章日期（双源同步）

适用于 `/tools/{slug}`（`tools-meta.ts` + `content/tools/{en,zh}/*.md` frontmatter）。

| 字段 | 规则 |
|------|------|
| `publishDate` | **创建后永不修改** |
| `modifiedDate` | 实质内容更新时修改；**≤ 今天**、**≥ publishDate** |

| 位置 | 格式 |
|------|------|
| `tools-meta.ts` | ISO `2026-06-22T00:00:00+08:00` |
| md frontmatter | 中文 `2026年6月22日` / 英文 `June 22, 2026` |

成批维护见 Step 7 [`07-tools-modified-date.md`](../07-tools-modified-date.md)。

## 八、验证

Meta 注册到 `blog-meta.ts`（或 `tools-meta.ts`），由 `generateMetadata()` 统一输出。

Audit 脚本（从部署仓根目录）：

```bash
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/audit-tools-page-fields.mjs
```

---

*meta-requirements · v3.0 · 2026-08-23*
