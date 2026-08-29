# Nova Scientia — 内容编辑流程

本文档描述本地内容编辑和构建部署的完整工作流。

**内容路径**：`E:\自有部署项目\nova-scientia-main\content\`（部署仓）。本文档在上下文仓，路径均相对于部署仓根目录。

---

## 一、内容架构

页面内容存储在部署仓 `content/` 目录下，直接受 git 版本控制：

```
content/
├── products/         # 产品详情页（435 个 JSON）
│   └── {slug}.json
├── topics/           # 主题指南（35 个 Markdown）
│   └── {slug}.md
├── companies/        # 公司/VC 页面（35 个 JSON）
│   └── {slug}.json
├── glossary.json     # AI 词汇表（147 术语，15 分类）
└── locales/          # 多语言覆盖层（按 locale 子目录）
    └── {locale}/
        ├── manifest.json
        └── topics/{slug}.md   # 已翻译的主题（示例：es-mx/image-generator.md）
```

构建时通过 `src/lib/content/*.ts` 读取；主题由 `topic-md.ts` 解析 MD，产品/公司读 JSON。

**路由**：所有页面在 `app/[locale]/` 下；pt-BR 默认语言 URL 无前缀（middleware 内部重写为 `/pt-br/*`）。

---

## 二、编辑产品页

### 2.1 添加新产品

1. 创建 `content/products/{slug}.json`，使用 kebab-case slug
2. 确保 slug 不在保留/冲突列表中（参考 [slug-breadcrumb.md](slug-breadcrumb.md)）
3. 按照 `ApiProduct` 类型完整填写所有必填字段
4. 运行 `npm run validate:products` 检查 slug/breadcrumb 一致性

### 2.2 修改产品信息

直接编辑 `content/products/{slug}.json`。常用编辑场景：

| 场景 | 字段路径 |
|------|----------|
| 更新 Hero CTA URL | `content.hero.cta_url` |
| 更新描述 | `content.hero.description` |
| 更新定价 | `content.pricing.plans[]` |
| 添加新闻 | `content.news[]` |
| 修改 FAQ | `content.faqs[]` |

### 2.3 产品 JSON 结构

参考 `specs/content-model.md` 的 `ApiProduct` 完整字段表。

最小必填字段：
- `slug`：唯一标识
- `name`：产品名称
- `content.hero`：`h1`、`description`、`cta_url`、`cta_text`
- `content.about`：`title` + 至少 1 个 `paragraph`
- `content.faqs`：至少 1 个 `{ q, a }`

---

## 三、编辑主题页

### 3.1 添加新主题

1. 创建 `content/topics/{slug}.md`（YAML frontmatter + 正文块，见 [content-model.md](content-model.md) §二）
2. 复制已有主题（如 `llm.md`）作为模板
3. 路由由 `getAllTopicSlugs()` 自动发现；动态路由在 `app/[locale]/[slug]/page.tsx`，需避开 `RESERVED_SLUGS`（见 [page-types.md](page-types.md) §B）

### 3.2 修改主题

直接编辑 `content/topics/{slug}.md`：
- 元数据（SEO、h1、faqs 等）→ frontmatter
- 正文段落 → `<!-- block:section -->` 块内

### 3.3 验证主题 MD

```bash
# 在部署仓根目录
npx tsx scripts/permanent/verify-topic-md-roundtrip.ts
```

---

## 四、编辑公司/VC 页

### 4.1 公司类型

公司页有 `company` 和 `investor` 两种变体，由 `content.type` 字段决定。

- `"company"`：标准公司档案（logo、产品、新闻、FAQ）
- `"investor"`：VC 档案（额外：投资聚焦、条款、投资组合批次、顾问、福利）

### 4.2 公司 JSON 结构

参考 `specs/content-model.md` 的 `ApiCompany` 完整字段表。

---

## 五、编辑词汇表

词汇表通过分片文件管理，使用合并脚本生成：

```bash
# 编辑分片（上下文仓）
# Nova-Scientia/scripts/ref/glossary/parts/

# 合并为部署仓 content/glossary.json（在部署仓根目录执行）
node ../../clients/Nova-Scientia/scripts/ref/glossary/merge-glossary.mjs
```

---

## 六、验证

每次内容修改后运行验证：

```bash
# 在部署仓根目录
npm run validate:products      # 产品 slug/breadcrumb 一致性（build 门禁）
npx tsx scripts/permanent/verify-topic-md-roundtrip.ts   # 主题 MD 解析（修改 topics 后）
```

`npm run build` 会自动运行 `validate:products` 作为门禁。

---

## 七、完整发布流程

```bash
# 1. 编辑内容
# products/companies → JSON；topics → MD

# 2. 验证
npm run validate:products
npx tsx scripts/permanent/verify-topic-md-roundtrip.ts   # 若改了 topics

# 3. 本地预览
npm run dev

# 4. 构建检查
npm run build

# 5. 提交 & 部署
git add content/
git commit -m "update: {描述修改内容}"
git push origin main
# Vercel 自动部署

# 6. 通知搜索引擎
npm run indexnow:all
```

---

## 八、关键约束

- 产品/公司 JSON、主题 MD 全部提交到 git，受版本控制
- 所有修改通过 git commit 追踪变更历史
- `content/glossary.json` 由 `merge-glossary.mjs` 脚本生成，不直接编辑
- Slug 规则见 [slug-breadcrumb.md](slug-breadcrumb.md)
- 多语言翻译流程见 [i18n-content-workflow.md](i18n-content-workflow.md)
