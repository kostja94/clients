# Step 4 — Meta 注册 + Config 注册

> **定位**：中文 JSON 创建完成后，在部署仓的三层注册——Meta（blog-meta.ts）、Config（blog-pages-config.ts）。
> **产出**：`blog-meta.ts` 更新 + `blog-pages-config.ts` 更新
> **引用**：`skills/create-tools-article/03-meta-and-config.md`（可复用工具型注册流程）、`references/meta-requirements.md`

---

## 前置条件

- [ ] 中文 JSON 创建完毕且经 Step 3b 中文本地化润色通过
- [ ] 文章类型已判定（Step 1）
- [ ] routeCategory 和 hubCategory 已确定

---

## 第一层：blog-meta.ts 注册

在部署仓 `src/data/blog-meta.ts` 的 `BLOG_META` 对象中新增条目：

```typescript
export const BLOG_META: Record<string, PageMeta> = {
  // ... 现有条目 ...

  "your-slug": {
    en: {
      title: "根据 Meta 规则组填写 | Alignify",
      description: "英文 description"
    },
    zh: {
      title: "根据 Meta 规则组填写 | Alignify",
      description: "中文 description"
    },
    publishDate: "2026-07-16",
    modifiedDate: "2026-07-16",
  }
};
```

### Meta title/description 填写规则

参照 `references/meta-requirements.md`，根据文章类型的 Meta 规则组填写。

**注意**：
- **先填中文**（中文版先完成），英文版在 Step 5 创建英文 JSON 时同步填写
- 可暂时填英文占位符 `"TODO"`，并在 Step 5 时更新

---

## 第二层：blog-pages-config.ts 注册

在部署仓 `src/data/blog-pages-config.ts` 的 `BLOG_PAGES_CONFIG` 数组中新增条目：

```typescript
{
  slug: "your-slug",
  shortTitleEn: "Short Title",     // 简短英文标题（用于 Hub 页面列表展示）
  shortTitleZh: "短中文标题",       // 简短中文标题
  routeCategory: "tools",          // "tools" | "marketing"
  toolsHubCategory: "image",       // routeCategory="tools" 时必填
  // 或
  // marketingHubCategory: "affiliate",  // routeCategory="marketing" 时必填
  hubKeywordEn: "keyword",
  hubKeywordZh: "关键词",
}
```

### hubCategory 取值

**从部署仓对应的 pages-config 文件中读取可用值**：

- `routeCategory: "tools"` → 取 `src/data/tools-pages-config.ts` 中已有的分组名
- `routeCategory: "marketing"` → 取 `src/data/marketing-pages-config.ts` 中已有的分组名

**核心原则**：**绝不凭空编造分组名**，必须确认该分组已在使用中。

---

## 注册后验证

- [ ] `blog-meta.ts` 新增条目格式与现有条目一致（缩进、引号、逗号）
- [ ] `blog-pages-config.ts` 新增条目格式与现有条目一致
- [ ] routeCategory 与知识块目录一致
- [ ] hubCategory 值存在于对应的 pages-config 分组中
- [ ] shortTitleEn 和 shortTitleZh 不重复（不与已有条目冲突）
- [ ] slug 在 blog-meta.ts 和 blog-pages-config.ts 中都已添加
- [ ] `npm run build` 无 TypeScript 错误（确认类型安全）

---

## 输出清单

- [ ] `blog-meta.ts` 新增 slug 条目
- [ ] `blog-pages-config.ts` 新增 slug 条目（含正确的 routeCategory + hubCategory）
- [ ] `npm run build` 通过

---

*04-meta-and-config.md · v1.0 · 2026-07-16*
