# optimize-internal-links · 参考文档

| 文档 | 用途 |
|------|------|
| [../SKILL.md](../SKILL.md) | Skill 入口与标准流程 |
| [../02-audit-and-baseline.md](../02-audit-and-baseline.md) | 全站审计与 baseline |
| [../03-per-page-workflow.md](../03-per-page-workflow.md) | 单页 checklist |
| [../04-reverse-links.md](../04-reverse-links.md) | Phase 4 反向互链 |
| [site-structure-internal-links.md](./site-structure-internal-links.md) | **全站快照**（~400 篇出链/入链；脚本自动生成） |
| [rules-quickref.md](./rules-quickref.md) | R 规则速查 + 违规修复矩阵 |

**规则 SSOT**（不在此重复）：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md)

**刷新快照**：

```bash
python scripts/audit/build-site-internal-links-doc.py
```
