# Nova Scientia — 内容编辑流程

本文档描述本地内容编辑和构建部署的完整工作流。

**内容路径**：`D:\部署项目\nova-scientia\content\`（部署仓）。本文档在上下文仓，路径均相对于部署仓根目录。

---

## 一、内容架构

所有页面内容以 JSON 文件形式存储在部署仓 `content/` 目录下，直接受 git 版本控制：

```
content/
├── products/         # 产品详情页（435 个 JSON 文件）
│   └── {slug}.json
├── topics/           # 主题编辑页（35 个 JSON 文件）
│   └── {slug}.json
├── companies/        # 公司/VC 页面
│   └── {slug}.json
└── glossary.json     # AI 词汇表（147 术语）
```

构建时通过 `src/lib/content/*.ts` 中的 `readFileSync` 同步读取。

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

1. 创建 `content/topics/{slug}.json`
2. 填写 `ApiTopic` 类型的完整内容
3. 在 `app/[slug]/page.tsx` 中确保 `generateStaticParams` 覆盖（通过 `RESERVED_SLUGS` 排除保留 slug）

### 3.2 主题 JSON 结构

参考 `specs/content-model.md` 的 `ApiTopic` 完整字段表。

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
# Nova-Scientia项目上下文/scripts/ref/glossary/parts/

# 合并为部署仓 content/glossary.json（在部署仓根目录执行）
node ../../项目文档/Nova-Scientia项目上下文/scripts/ref/glossary/merge-glossary.mjs
```

---

## 六、验证

每次内容修改后运行验证：

```bash
# 在部署仓根目录
npm run validate:products      # slug/breadcrumb 一致性（build 门禁）
```

`npm run build` 会自动运行 `validate:products` 作为门禁。

---

## 七、完整发布流程

```bash
# 1. 编辑内容
# 直接修改 content/ 下的 JSON 文件

# 2. 验证
npm run validate:products

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

- 内容 JSON 文件全部提交到 git，受版本控制
- 所有修改通过 git commit 追踪变更历史
- `content/glossary.json` 由 `merge-glossary.mjs` 脚本生成，不直接编辑
- Slug 规则见 [slug-breadcrumb.md](slug-breadcrumb.md)
