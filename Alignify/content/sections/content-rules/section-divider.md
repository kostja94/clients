# No-Divider Policy · 分割线策略

全局规范：**文章内容页不使用任何分割线**（border-t / border-b / `<hr>` / `<Separator>`）。

## 原则

分割线（分割线）在文章排版中无信息增量——用空白间距（`space-y-12`、`pt-8`、`pb-6` 等）分隔内容块已足够清晰。所有文章内容块之间和块内条目之间均不得出现横向分割线。

## 适用范围

- 所有通过 `ArticleFromJson` 渲染的内容页（tools / seo / marketing / insights）
- 所有文章块类型：Section、References、FAQ、Table、Tldr（Markdown `section` / 集中 JSON）

## 不适用范围（保留的边框）

以下边框不受此策略约束，因为它们是页面框架/UI 元素而非文章内容分隔：

- **页面框架**：Header 底边、Footer 顶边及内部 Separator、BreadcrumbNav 底边、BlogLayout 粘性头底边、CookieConsent 顶边、TopBanner 底边
- **卡片/表格边框**：`border border-border` 包围的卡片（Tldr、BestTools、FAQ `<details>`、Partner 卡片）和表格边框（Table 组件）
- **标题下划线**：h2 等标题的 `border-b` 装饰线
- **首页区域边框**：HomeSections 和 TrustedBySection 的 `border-y`
- **独立页面底部附注**：PartnershipPageContent、CustomerStoriesIndex、GrowthCaseStudiesIndex、GlossaryViewer 的底部 border-t

## 实施状态（2026-05-20）

### 已清理

| 类型 | 数量 | 方式 |
|------|------|------|
| JSON `section.showDivider: true` | 565 | 迁移期已清除（现 Markdown section） |
| JSON `References.showDivider: true` | 16 | 字段删除或改为 `false` |
| JSON `howToChoose.wrapperClassName` 含 `border-t` | 230 | 清空为 `""` |
| `HowToChoose.tsx` 硬编码 `border-t` | 1 | 移除 |
| `UseCases.tsx` 硬编码 `border-t` | 1 | 移除 |
| `References.tsx` 默认值 | 1 | `true` → `false` |
| `HowToChoose.tsx` 条目间 `border-b` | 1 | 移除 |
| `UseCases.tsx` 条目间 `border-b` | 1 | 移除 |
| `FAQ` CSS `.faq-details` `border-b` | 1 | 移除 |
| `HomeSections.tsx` FAQ 条目 `border-b` | 1 | 移除 |
| `GlossaryViewer.tsx` 词条间 `border-b` | 1 | 移除 |

### 保留的惰性代码

- `Section.tsx:102-103`：`showDivider ? "border-t ..." : ""` — 保留条件逻辑，但因所有 JSON 触发已清除且组件默认值为 `false`，不会渲染分割线
- `References.tsx:98-100`：同上，默认值已改为 `false`

### 新增内容时的注意事项

- **Section 块**：`showDivider` 字段可选，省略或设为 `false`；**不得设为 `true`**
- **References 块**：同上
- **howToChoose 块** → **已废弃**；如何选择 = 正文 section
- **Section**：间距由 `space-y-12` 与 `pb-6 mb-6` 提供
- **FAQ `<details>` 条目**：CSS 中 `.faq-details` 不设边框
- **Glossary 词条**：词条间使用 `pb-2` 间距，**不带 `border-b`**

## 设计替代

块间自然间距由 `ArticleFromJson` 中父级 `div` 的 `space-y-12`（48px）提供。块内条目间距由各组件自身的 `pb-6 mb-6`（24px）或 `pb-2`（8px）提供。
