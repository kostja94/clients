# optimize-tools-internal-links

存量 Tools / Blog 文章的内链审计、选链、写入与验收（**Markdown 正文**）。

## 脚本（从部署仓根目录）

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
npm run verify:content-json
npm run build
```

> **无 npm 命令**：`audit:internal-links`、`audit:text-regression` 未在部署仓 `package.json` 注册。

## 标准流程

```
附录 B 选邻居 → git show HEAD 建立 baseline（R-LINK-ONLY）
→ audit-tools-internal-links.py
→ StrReplace 只改 md 内 <a>（unwrap 重复 / 补 R1）
→ verify:content-json + build
```

## 区块配额

| 区块 | 配额 |
|------|------|
| TL;DR（JSON intro） | 0–1 链 |
| 什么是 · 第二段 | 1–4 链 |
| 应用场景 / 如何选择 section | 0–1 链/段 |
| FAQ（JSON） | 无内链（plain text） |
| 全文 | ≥5 distinct；R4 每 slug 一次 |

创建阶段见 `create-tools-article/02c-internal-links-drafting.md`。

## 标杆页

`content/blog/en/agent-sandbox.md`、`content/blog/en/web-fetch.md`
