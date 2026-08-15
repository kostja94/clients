# Step 1 — 知识块就绪检查 + 关键词注册

> **前置条件**：`knowledge/tools/{slug}.md` 已创建
> **产出**：关键词锚点 + README 条目
> **参照**：`knowledge/tools/_TEMPLATE.md`、`product/alignify-keywords-tools.md`、`knowledge/tools/README.md`

---

## 1.1 验证知识块合规

对照 [`knowledge/tools/_TEMPLATE.md`](../../knowledge/tools/_TEMPLATE.md) 逐项核对：

- [ ] 材料范围（含整理日期）：已填写且格式正确
- [ ] 站内对照：已标注（含"待上线"状态）
- [ ] 关键词与 slug 映射：已声明 keywordEn / keywordZh
- [ ] 词汇锚点：≥5 条加粗术语定义
- [ ] 问题域：≥5 条"为何出现这类产品"
- [ ] 能力栈：≥5 层概念拆分
- [ ] 形态谱系：≥5 种类型
- [ ] 风险合规治理：≥5 条
- [ ] 落地碎片：≥5 条实操建议
- [ ] 工具与产品类型表：有
- [ ] 外链索引：≥10 条 + 对比与测评
- [ ] 延伸阅读：≥5 条

如有未通过项 → 先补齐知识块，**不进入 Step 2**。

---

## 1.2 注册关键词到 alignify-keywords-tools.md

在 [`product/alignify-keywords-tools.md`](../../product/alignify-keywords-tools.md) 中新增：

### 步骤

1. 在「主关键词表」中添加一行：
```markdown
| **{slug}** | {keywordEn}, {keywordZh} | /blog/{slug} | ✅ |
```

2. 在支柱关键词表中添加一行（按工具类型归类）：
```markdown
| {类型} | {keywordEn} | /blog/{slug}、/zh/blog/{slug}（[关键词与意图](#{slug}-tools)） |
```

3. 创建 `#{slug}-tools` 锚点段：
```markdown
<span id="{slug}-tools"></span>

## {slug}（{中文名}）

**配置**：`blog-pages-config` → `{ slug, shortTitleEn, shortTitleZh }`（关键词字段仅保留在 `alignify-keywords-tools.md`）

**目标 URL**

| 语言 | 路径 |
|------|------|
| 英文 | [/blog/{slug}](https://alignify.co/blog/{slug}) |
| 中文 | [/zh/blog/{slug}](https://alignify.co/zh/blog/{slug}) |

**意图与关键词**

| 角色 | 英文关键词 / 短语 | 中文关键词 / 短语 |
|------|-------------------|-------------------|
| 核心品类 | {key phrases} | {key phrases} |
| 子功能 | {sub-features} | {sub-features} |
| 代表产品 | {product names} | {product names} |
| 辨析 | {differentiation from adjacent slugs} | {区分说明} |
| 相邻 Tools | [{adjacent-slug}](/tools/{adjacent-slug}) | 说明 |

**内容数据源**：`content/blog/en/{slug}.json`、`content/blog/zh/{slug}.json`

**知识块** → [{slug}.md](../knowledge/tools/{slug}.md)

> **注意**：新文章走 `/blog/` 路由，注册到 `blog-meta.ts` + `blog-pages-config.ts`（字段为 `{ slug, shortTitleEn, shortTitleZh }`）。关键词文件中的 anchor 仍放在 `alignify-keywords-tools.md`（与知识块的 tools 目录一致），但 URL 指向 `/blog/{slug}`。
```

---

## 1.3 注册到 knowledge/tools/README.md

在 [`knowledge/tools/README.md`](../../knowledge/tools/README.md) 中按字母序插入条目：

```markdown
- **{中文名} / {英文名}（`{slug}`）**：[{slug}.md](./{slug}.md) 归纳 **{一句话描述}**；与 [{adjacent}.md](./{adjacent}.md)（{adjacent 描述}）分流——{slug} 是"{核心问题}"，{adjacent} 是"{相邻问题}"；正式页{状态说明}。
```

**位置**：按 slug 字母序插入，位于前后相邻条目之间。

---

## 1.4 检查

- [ ] 关键词文件中的锚点链接有效（`#{slug}-tools`）
- [ ] README 中的相邻 slug 链接有效
- [ ] slug / keywordEn / keywordZh 三处一致
- [ ] 知识块路径指向正确文件

---

*01-knowledge-to-keywords · v2.0 · 2026-06-23*
