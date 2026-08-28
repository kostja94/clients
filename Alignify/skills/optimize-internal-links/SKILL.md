# optimize-internal-links

存量文章内链：**审计 → 选链 → 写入 → 验收 → 刷新快照**（Markdown / `faq-data.json` 正文侧车）。

> **当前范围**：本 skill 维护流程与参考数据；**存量正文修复**另开任务执行（见 [`workflow.md`](./workflow.md)）。

## 读什么

| 文档 | 用途 |
|------|------|
| [`workflow.md`](./workflow.md) | 全站 baseline + 单页 loop |
| [`references/rules-quickref.md`](references/rules-quickref.md) | R 规则 1 页速查 |
| [`references/site-structure-internal-links.md`](references/site-structure-internal-links.md) | 全站快照（~400 篇 · 脚本生成 · **§七 Marketing/GTM**） |
| [`references/marketing-internal-links-backlog.md`](references/marketing-internal-links-backlog.md) | Marketing cluster 矩阵与执行批次（嵌入 §7.4） |
| [`reverse-links.md`](reverse-links.md) | Phase 4 反向互链（批量，与单页分开） |

**规则 SSOT**（不在此重复）：[`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md)（Part 1–2 · 4.5 M1–M11 · Part 8 外链）  
**新文创建**：[`../create-article/07-internal-links.md`](../create-article/07-internal-links.md)

## 脚本（部署仓根目录）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py   # 刷新快照
npm run verify:content-json && npm run build
```

## 分布原则（摘要）

点击意图优先 · 每段 ≤1 链 · **全文同 URL 1 次**（含 FAQ 答案）· 结论 0–2 链 · 无 distinct 条数下限

FAQ 答案中的内链**计入正文**，遵守与同页 section 相同的 R4 / 密度规则（User confirmed 2026-08-27）。

## 标杆页

`content/blog/en/agent-sandbox.md` · `content/blog/en/web-fetch.md`

*optimize-internal-links · v2.0 · 2026-08-27*
