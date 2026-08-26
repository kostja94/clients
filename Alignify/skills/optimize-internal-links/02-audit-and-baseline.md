# 审计与 Baseline

> 入口：[`SKILL.md`](SKILL.md) · 规则速查：[`references/rules-quickref.md`](references/rules-quickref.md) · 下一步：[`03-per-page-workflow.md`](03-per-page-workflow.md)

从**部署仓根目录**执行：

```bash
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
npm run verify:content-json
```

## 阻断标准

| 检查 | 标准 |
|------|------|
| R0 无效 href | 0 high |
| R4 重复 slug | 0 |
| R7 FAQ 内链 | FAQ 答案无 `<a>` |
| 机械指路 / 同段堆链 | 按 Part 1 清理 |

**无 distinct 条数下限** — 快照中的 distinct 计数仅作观察。

## 报告

`E:/clients/Alignify/scripts/reports/`

## 刷新全站快照

```bash
python ../../clients/Alignify/scripts/audit/build-site-internal-links-doc.py
```

输出：[`references/site-structure-internal-links.md`](references/site-structure-internal-links.md)
