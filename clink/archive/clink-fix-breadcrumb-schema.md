# Clink 站内任务单 — 修复 BreadcrumbList Schema「Invalid URL in field 'id'」

> **任务类型**：结构化数据修复（Technical SEO）
> **目标域名**：clinkbill.com
> **状态**：待处理
> **优先级**：P1（全站所有博客页触发；非阻断富结果，但影响 GSC 数据质量与富结果稳定性）
> **提交**：2026-08-11

---

## 1. 任务目标

消除 clinkbill.com 全站博客页面在 Google Search Console（GSC）中持续出现的以下问题：

```
Invalid URL in field "id" (in 'itemListElement.item')
```

修复后所有博客页面的 `BreadcrumbList` 结构化数据必须通过 [Rich Results Test](https://search.google.com/test/rich-results) 校验，GSC「增强功能 / 面包屑」报告不再产生无效 URL 错误。

---

## 2. 问题证据（2026-08-11 实测）

对 `/blog/runway`（GlossaryTerm 文章）抓取的当前页面源码，页面输出的 `application/ld+json` 如下：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "/blog" },
    { "@type": "ListItem", "position": 3, "name": "What Is Runway? — How Startup Cash Runway Works" }
  ]
}
```

`/blog` 列表页输出：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "/" },
    { "@type": "ListItem", "position": 2, "name": "Blog" }
  ]
}
```

首页 `/` 无 JSON-LD（正常，无需处理）。

---

## 3. 根因分析

`ListItem.item` 字段输出的是**相对路径**，而非完整绝对 URL：

- `"item": "/"` → 不是有效 URL
- `"item": "/blog"` → 不是有效 URL
- position 3（当前文章页）→ **完全缺失 `item`**

Google 的 [Breadcrumb 富结果规范](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) 要求每个 `ListItem.item` 必须是**完整、绝对、可抓取**的 URL（即 `https://clinkbill.com/...` 形式）。相对路径无法解析为有效 URL，因此校验器将该 `item` 字段判定为 `Invalid URL in field "id"`（错误中的 `id` 指的就是 `ListItem.item` 实体标识）。

GSC 将其归类为 non-critical 的原因是：Google 会对无效 `item` 做容错，面包屑富结果**可能**仍被展示。但这是不可靠的：

1. 无法通过 Rich Results Test，富结果展示不稳定；
2. 错误会在 GSC 中持续累积，掩盖真正的关键问题；
3. 缺少完整 URL 时 Google 无法确认该层级指向的页面，点击/导航追踪失真。

---

## 4. 影响范围（全站）

同一面包屑组件被所有博客页面共用，**全部博客页受影响**：

| 页面 | 受影响字段 |
|------|-----------|
| `/blog`（列表页） | position 1 的 `item: "/"` |
| `/blog/{slug}`（全部文章页） | position 1、2 的 `item` 相对路径；position 3 缺失 `item` |

已抽验页面：`/blog/runway`、`/blog`。

---

## 5. 修复要求

### 5.1 修复位置

定位生成 `<script type="application/ld+json">` 面包屑数据的组件（Next.js 项目中通常为 `BreadcrumbJsonLd` 或自定义 `<script>` 注入逻辑）。

### 5.2 规则（必须满足）

1. **绝对 URL**：所有 `item` 值必须为 `${SITE_URL} + 路径` 形式（`SITE_URL = "https://clinkbill.com"`），禁止直接输出 `/xxx` 相对路径。
2. **末级也必须带 `item`**：position 3（当前文章页）必须输出当前页的完整绝对 URL。
3. **全局生效**：修复一处组件即可覆盖 `/blog` 与全部文章页。
4. **不引入新问题**：仅修复面包屑 JSON-LD；不要改动页面其他 schema、不要改动面包屑 UI 展示。

### 5.3 修复后的期望输出

`/blog/runway` 修复后应为：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://clinkbill.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://clinkbill.com/blog" },
    { "@type": "ListItem", "position": 3, "name": "What Is Runway? — How Startup Cash Runway Works", "item": "https://clinkbill.com/blog/runway" }
  ]
}
```

`/blog` 列表页修复后应为：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://clinkbill.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://clinkbill.com/blog" }
  ]
}
```

### 5.4 代码级参考（示意，按项目实际实现调整）

```tsx
const SITE_URL = "https://clinkbill.com";

const breadcrumbSchema = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: [
    { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
    { "@type": "ListItem", position: 2, name: "Blog", item: `${SITE_URL}/blog` },
    // 文章页末级：必须带当前页完整 URL
    ...(currentSlug
      ? [{ "@type": "ListItem", position: 3, name: title, item: `${SITE_URL}${currentSlug}` }]
      : []),
  ],
};
```

---

## 6. 验收标准

- [ ] `/blog` 与 `/blog/runway` 页面源码中，所有 `ListItem.item` 均为 `https://clinkbill.com/...` 绝对 URL
- [ ] 文章页末级 ListItem 已补充完整 `item`
- [ ] 通过 [Rich Results Test](https://search.google.com/test/rich-results) 验证无错误（仅提示无关的容错信息视为通过）
- [ ] 抽查 3 篇不同类型文章（BrandIntroduction / Product / Glossary）均无 `Invalid URL in field "id"`
- [ ] 生产部署后观察 GSC 面包屑报告，待 Google 重新抓取后错误清零

---

*本任务单由外部 SEO 审计提交，供 Clink 方 agent 直接执行。*
