# optimize-internal-links

存量文章的内链审计、选链、写入与验收（Markdown 正文）。

## 脚本（从部署仓根目录）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
npm run verify:content-json
npm run build
```

## 标准流程

```
附录 B 选邻居 → git show HEAD 建立 baseline（R-LINK-ONLY）
→ audit-tools-internal-links.py
→ StrReplace 只改 md 内 <a>
→ verify:content-json + build
```

## 区块配额

| 区块 | 配额 |
|------|------|
| 核心要点 intro（md） | 0–1 链 |
| 什么是 · 第二段 | 1–4 链 |
| 应用场景 / 如何选择 | 0–1 链/段 |
| FAQ（md） | 无内链 |
| 全文 | ≥5 distinct；R4 每 slug 一次 |

**SSOT**：[`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md)  
**创建阶段**：[`../create-article/07-internal-links.md`](../create-article/07-internal-links.md)

## 标杆页

`content/blog/en/agent-sandbox.md` · `content/blog/en/web-fetch.md`
