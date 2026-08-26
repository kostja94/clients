# optimize-internal-links

存量文章的内链审计、选链、写入与验收（Markdown 正文）。

## 文档

| 步骤 | 文件 |
|------|------|
| 入口（本文件） | 流程 + 脚本 |
| 规则速查 | [`references/rules-quickref.md`](references/rules-quickref.md) |
| 全站快照 | [`references/site-structure-internal-links.md`](references/site-structure-internal-links.md) |
| 审计 baseline | [`02-audit-and-baseline.md`](02-audit-and-baseline.md) |
| 单页 checklist | [`03-per-page-workflow.md`](03-per-page-workflow.md) |
| 反向互链 | [`04-reverse-links.md`](04-reverse-links.md) |

**规则 SSOT**：[`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md) · Marketing [`../create-article/rules/marketing-internal-links.md`](../create-article/rules/marketing-internal-links.md)  
**创建阶段**：[`../create-article/07-internal-links.md`](../create-article/07-internal-links.md)

## 脚本（从部署仓根目录）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
npm run verify:content-json
npm run build
```

## 标准流程

```
读快照/附录 B → git show HEAD baseline（R-LINK-ONLY）
→ audit-tools-internal-links.py
→ StrReplace 只改 md 内 <a>
→ verify:content-json + build
→ python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py  # 刷新快照
```

## 分布原则

点击意图优先 · 每段 ≤1 链 · 同 URL 1 次 · FAQ 无链 · 结论 0–2 链 · **无硬性 distinct 下限**

详见 [`references/rules-quickref.md`](references/rules-quickref.md)。

## 标杆页

`content/blog/en/agent-sandbox.md` · `content/blog/en/web-fetch.md`
