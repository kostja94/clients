# 面包屑导航（BreadcrumbNav）与 Tools 标签

## 单一数据源

`/tools/{slug}` 路径的面包屑文案由 **`src/data/tools-pages-config.ts`** 中的 **`TOOLS_PAGES`** 按当前语言生成（`keywordZh` / `keywordEn`），与 **`AlsoInterestedIn`**、**`/tools` 聚合页** 使用同一套关键词，避免手写映射与配置漂移。

聚合入口 **`/tools`** 本身的标签仍为组件内文案（「AI 工具」/「AI Tools」），与子路径无关。

## 维护约定

- 新增或重命名 Tools 类目：只改 **`tools-pages-config`**（及 `content/tools`、`app/*/tools/[slug]` 等既有流程），**不必**再改 `BreadcrumbNav` 中的逐条 `/tools/...` 映射。
- 若某条工具路径需要**与关键词表不同的**面包屑专用文案，再在 `BreadcrumbNav` 的 `pathNameMap` 中**后序覆盖**同一路径键（当前未使用）。

## 相关代码

- `src/components/BreadcrumbNav.tsx`：`toolsPathLabels`（`useMemo`，依赖 `locale`）
