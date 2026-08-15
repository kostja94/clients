# Create Tools Article — Alignify 文章创建 Skill

> **用途**：从知识块（`knowledge/tools/{slug}.md`）到发布就绪的正式文章（中文 JSON + 英文 JSON + Meta 注册 + 配置注册）的完整流程。
> **版本**：v2.0 · 2026-06-23
> **适用范围**：Alignify 新文章创建（**新文章统一走 `/blog/{slug}` 路由**；旧 `/tools/{slug}` 保持不变）。
> **文章类型**：本 Skill 面向**从知识块创建的 Tools 型榜单/对比文章**（含「最佳」/ `Best` Meta 规则）。纯营销攻略或非对比型长文的 Meta 规则可能不同——以现有 Blog 文章（`github-for-marketing`、`how-to-write-github-readme`）为参考。

---

## 路由决策（先读此节）

| 场景 | 路由 | 内容目录 | Meta 注册 | Config 注册 |
|------|------|---------|-----------|-------------|
| **新文章（默认）** | `/blog/{slug}` | `content/blog/{en,zh}/{slug}.json` | `src/data/blog-meta.ts` | `src/data/blog-pages-config.ts` |
| 旧文章（保持不变） | `/tools/{slug}` | `content/tools/{en,zh}/{slug}.json` | `src/data/tools-meta.ts` | `src/data/tools-pages-config.ts` |

**架构说明**（2026-05-20 迁移后）：
- **不存在**每 slug 一个 `page.tsx`。路由使用单个动态路由文件。
- Meta 由 `generateMetadata()` 从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取。
- 正文由 `getPageData("blog"|"tools", slug, locale)` 加载 JSON。
- 若同时保留 `BLOG_META` + `TOOLS_META`（模式 B 迁移），动态路由自动将 `/tools/{slug}` redirect 到 `/blog/{slug}`。

---

## 何时使用本 Skill

当以下条件**全部满足**时加载本 Skill：

- [ ] `knowledge/tools/{slug}.md` 知识块已创建并通过模板逐项核对（见 `_TEMPLATE.md`）
- [ ] 需要创建对应的正式页面
- [ ] 该 slug 尚未在 `blog-pages-config.ts` 中注册

**不适用场景**：
- 知识块尚未完成 → 先完成知识块
- 仅为已有文章做局部优化 → 参考 `content/templates/template-tools.md` §九 + `content/sections/section-optimization-playbook.md`
- 非本频道的文章（SEO/Marketing/Insights）→ 使用对应 template

---

## 流程总览

```
Step 1 — 知识块就绪检查 + 关键词注册
   ├── 验证知识块是否通过 _TEMPLATE.md 逐项核对
   ├── 在 alignify-keywords-tools.md 新增 slug 锚点
   └── 在 knowledge/tools/README.md 新增条目
        ↓
Step 2 — 创建中文文章 JSON
   ├── 按 10 节结构组装 section（TL;DR → ... → FAQ）
   ├── 创建 content/blog/zh/{slug}.json
   └── 从知识块提取产品数据填入 BestTools/Table/FAQ
        ↓
Step 2b — 中文本地化润色（必做）
   ├── 加载 `skills/localize-content-zh/SKILL.md`
   ├── 术语、References title、blogLayout 日期、小节标题
   └── 运行 deploy 仓 `polish-zh-page.py` + audit 脚本
        ↓
Step 3 — Meta 注册 + 配置注册 + 图片注册
   ├── 在 blog-meta.ts 新增 slug 条目（publishDate 为 slug 级字段）
   ├── 在 blog-pages-config.ts 新增 { slug, shortTitleEn, shortTitleZh }
   ├── 在 blog-article-images.ts 新增图片映射
   └── 确认使用模式 A（全新）还是模式 B（迁移）
        ↓
Step 4 — 创建英文文章 JSON
   ├── 中文完成后再创建 content/blog/en/{slug}.json
   └── 意译非逐句，本地化差异
        ↓
Step 5 — 质量检查
   ├── 运行 audit 脚本（跨仓路径）
   ├── 手动核对图片/FAQ/Conclusion 位置
   └── npm run build 验证
        ↓
Step 6 — 发布日期错开（Blog 新文，成批上线前）
   ├── 仅 /blog/{slug} 未上线 slug
   ├── 从今天往前一天一篇（避让已占用日）
   └── stagger-unpublished-publish-dates.py
        ↓
Step 7 — Tools modifiedDate（/tools/{slug} 已上线页）
   ├── 三处同步：tools-meta.ts + en/zh toolsLayout
   ├── 保守错开 origin 大簇（≤2 篇/日，不拉跨数月）
   └── report-tools-dates.py + rebalance-tools-dates-conservative.py
```

**关键原则**：
- **新文章走 `/blog/`**：JSON 放 `content/blog/`，Meta 注册到 `blog-meta.ts`
- **先中文，后英文**：新增页面时仅创建中文版，中文创建完毕后一次性创建英文
- **知识块 ≠ 文章**：知识块是非线性笔记，文章需要改写为叙事体例
- **无需创建 page.tsx**：路由和页面渲染由动态路由 + `getPageData()` 统一处理

---

## 各步骤详细文档

| 步骤 | 文档 | 产出 |
|------|------|------|
| 1 | [`01-knowledge-to-keywords.md`](./01-knowledge-to-keywords.md) | 关键词注册 + README 条目 |
| 2 | [`02-article-structure.md`](./02-article-structure.md) | `content/blog/zh/{slug}.json` |
| 2c | [`02c-internal-links-drafting.md`](./02c-internal-links-drafting.md) | 内链初稿（R-TLDR + Hub/Spoke） |
| 2b | [`../localize-content-zh/SKILL.md`](../localize-content-zh/SKILL.md) | 中文地道化 + References 中文化 |
| 3 | [`03-meta-and-config.md`](./03-meta-and-config.md) | `blog-meta.ts` + `blog-pages-config.ts` + `blog-article-images.ts` 更新 |
| 4 | [`04-english-localization.md`](./04-english-localization.md) | `content/blog/en/{slug}.json` |
| 5 | [`05-quality-gates.md`](./05-quality-gates.md) | 全量审计通过 + build 成功 |
| 6 | [`06-publish-date-stagger.md`](./06-publish-date-stagger.md) | Blog 未上线 slug `publishDate` 错开 |
| 7 | [`07-tools-modified-date.md`](./07-tools-modified-date.md) | Tools `/tools/` 页 `modifiedDate` 保守维护 |

---

## 核心引用

本 Skill 引用以下 Alignify 项目文件（不复制其内容，按需 Read）：

| 引用 | 用途 | 路径 |
|------|------|------|
| 知识块模板 | 验证知识块合规 | `knowledge/tools/_TEMPLATE.md` |
| 部署仓 blog-meta.ts | 确认 Meta 格式 | `src/data/blog-meta.ts`（部署仓） |
| 部署仓 blog-pages-config.ts | 确认 config 字段（`{ slug, shortTitleEn, shortTitleZh }`） | `src/data/blog-pages-config.ts`（部署仓） |
| Section 规范 | 各章节组件格式 | `content/sections/` 对应文件 |
| 内链专册 | 内链拓扑 | `content/alignify-internal-links.md` |
| **内链初稿（创建）** | TLDR 0–1 链、Hub/Spoke、R4 全文唯一 | [`02c-internal-links-drafting.md`](./02c-internal-links-drafting.md) |
| **存量内链优化** | 审计、批次优化、附录 C | Skill **`optimize-tools-internal-links`** |

> **注意**：`content/templates/template-tools.md` §2（旧 page.tsx 模式）和 §十二（旧 page.tsx 示例）已过时，**不引用**。其他章节（§一页面结构、§五各章节规范、§十四翻译）仍可参考。

---

## 快速参考

### 文章结构顺序（不可变）

```
TL;DR → 什么是XXX → 如何工作 → 各类型工具详细介绍 → 工具对比表格 → 应用场景 → 如何选择 → 结论 → FAQ
```

### Meta 四要素硬约束

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| Meta title | 必须含「最佳」、年份 `（2026）`、冒号副线 | 必须含 `Best`、年份 `(2026)`、冒号副线 |
| Meta description | 列举 2–3 个代表产品 | 列举 2–3 个代表产品 |
| H1 | 不写年份；推荐「类型：核心价值」 | 不写年份 |
| Excerpt | 三段式、80–150 字；避免通用结尾 | 三段式、200–250 字符 |

### 质量检查脚本（部署仓 + 上下文仓）

**部署仓** `alignify-by-kostja`（Blog/Tools JSON 通用）：

```bash
npm run verify:content-json    # 含 howToChoose error 级（name/title/id）
npm run audit:howto-choose     # 全量 howToChoose 报告
npm run audit:internal-links
npm run build
```

**上下文仓**（主要覆盖旧 `/tools/` Meta）：

```bash
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-meta-titles.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-page-fields.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/check-tools-en-content.mjs
```

> **根因备忘**：`howToChoose` 完整规范见 [`section-how-to.md`](../../content/sections/section-how-to.md)（唯一真相源）。字段硬约束：必用 `steps[].title`，**禁止** `name`；步骤 3–5 步、标题动词+分叉短语、去模板（见 Part 3 黑名单）。

---

## 参考速查表

| 文档 | 内容 |
|------|------|
| [`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md) | 10 节结构 × 组件 × JSON 字段映射 |
| [`references/meta-requirements.md`](./references/meta-requirements.md) | Meta 四要素完整规则 + publishDate 双位置说明 |
| [`references/section-word-counts.md`](./references/section-word-counts.md) | 各章节中英文字数硬底线与建议区间 |
| [`references/quality-checklist.md`](./references/quality-checklist.md) | 综合质量检查表（脚本 + 手动） |
| [`references/common-errors.md`](./references/common-errors.md) | 已归档的常见错误与修复方案 |
| [`06-publish-date-stagger.md`](./06-publish-date-stagger.md) | Blog 新文 `publishDate` 错开 |
| [`07-tools-modified-date.md`](./07-tools-modified-date.md) | Tools 旧路由 `modifiedDate` 三处同步与保守错开 |

---

*create-tools-article · v2.3 · 2026-06-25*
