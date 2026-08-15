# Step 5 — 质量检查

> **前置条件**：Step 2–4 完成（中英文 JSON + blog-meta.ts + blog-pages-config.ts 全部就绪）
> **产出**：全量审计通过 + `npm run build` 成功
> **参照**：[`references/quality-checklist.md`](./references/quality-checklist.md)、[`references/common-errors.md`](./references/common-errors.md)

---

## 5.1 运行自动化脚本

**部署仓（Blog + Tools 通用）**：

```bash
npm run verify:content-json
npm run audit:howto-choose
npm run audit:internal-links
```

**上下文仓（Tools Meta / 字段，若适用）**：

```bash
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-meta-titles.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-page-fields.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/check-tools-en-content.mjs
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

**如有 error → 先修复再继续。** howToChoose 的 warn（描述过短、缺 step id）在发布前应清零或列入同批修复。

**Tools 日期（更新 `/tools/` 文章或成批错开后）**：

```bash
python scripts/permanent/report-tools-dates.py
npm run verify:content-json
```

见 Step 7 [`07-tools-modified-date.md`](./07-tools-modified-date.md)。

---

## 5.2 P0 手动检查（阻断发布）

逐项核对，**任一 Fail 不得发布**：

| # | 检查项 | 怎么查 |
|---|--------|--------|
| 1 | Conclusion 在 FAQ 之前 | 读 JSON，确认 conclusion section 的数组位置在 faq 之前 |
| 2 | FAQ ≥8 问 | 数 FAQ items 数组长度 |
| 3 | FAQ 内链合规 | Tools/Blog JSON：检查 FAQ 内链是否违反唯一性/条数上限；MDX 仍搜 FAQ answer 中的 `<a` 和 `](` |
| 4 | 图片文件存在 | `ls public/blog/{slug}/` 确认所有引用图片存在 |
| 5 | BestTools description 硬底线 | ZH ≥100 字 / EN ≥280 字符 |
| 6 | BestTools shortDescription 硬底线 | ZH ≥4 字 / EN ≥10 字符 |
| 7 | Meta title 含「最佳」/ `Best` | 读 `blog-meta.ts` → `BLOG_META["{slug}"].en.title` 和 `.zh.title` |
| 8 | Meta description 列举 ≥2 产品名 | 读 `blog-meta.ts` → `BLOG_META["{slug}"].en.description` 和 `.zh.description` |
| 9 | Meta 规则一致性 | en/zh 双向 title 含 Best/「最佳」+ 年份 + 冒号副线；description 列举 ≥2 产品名 |
| 10 | howToChoose 渲染与 schema | `npm run verify:content-json` 通过；页面「如何选择」小标题非空；每步有引导 intro |

---

## 5.3 P1 手动检查（应修复）

| # | 检查项 | 怎么查 |
|---|--------|--------|
| 1 | 10 节完整 | 检查 blocks 数组长度 ≥9，包含全部必需 type |
| 2 | 内链相关性 | 检查内链工具与当前品类的功能关联 |
| 3 | 同页 BestTools max/min < 3× | 对比最长和最短 description |
| 4 | bestFor/pricing 无空值 | 检查 comparisonSection items |
| 5 | FAQ 答案不复制正文 | 对比 FAQ answer 与正文段落 |
| 6 | Excerpt 不出现通用结尾 | 搜索 "这将帮助" 或通用结尾句 |

---

## 5.4 Build 验证

```bash
npm run build
```

确认：
- [ ] 无 TypeScript 错误
- [ ] 无 JSON 解析错误
- [ ] `/blog/{slug}` 可访问
- [ ] `/zh/blog/{slug}` 可访问
- [ ] 面包屑正确渲染
- [ ] OG 图片正常显示
- [ ] 页面在 sitemap 中出现

---

## 5.5 最终发布检查

| # | 最终确认 |
|---|---------|
| 1 | `blog-meta.ts` 中 publishDate 已设置为当前日期（ISO 格式） |
| 2 | `blog-meta.ts` 中 modifiedDate 已设置为当前日期（ISO 格式） |
| 3 | JSON `blogLayout` 中展示日期与 meta.ts 同步 |
| 4 | `knowledge/tools/{slug}.md` 站内对照已更新为正式页链接 |
| 5 | `knowledge/tools/README.md` 条目中"正式页状态"已更新 |
| 6 | P0 手动检查全部通过；Blog Tools 内链由 `audit-tools-internal-links.py --source blog` 覆盖 |
| 7 | `npm run build` 通过 |
| 8 | **Tools 更新**：`modifiedDate` 三处同步；`report-tools-dates.py` 无未来日、无 modified < publish |

---

## 5.6 如果检查失败

1. 定位失败项属于哪个 Step 的产物
2. 对照 [`references/common-errors.md`](./references/common-errors.md) 找到错误编号
3. 按修复方案修正
4. 重跑该 Step 和 Step 5
5. 不要跳过检查直接发布

---

*05-quality-gates · v2.1 · 2026-06-25*
