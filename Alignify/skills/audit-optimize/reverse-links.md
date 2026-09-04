# 反向互链（Phase 4）

> 与单页 Wave **分开批**；入口：[`SKILL.md`](SKILL.md) · 单页：[`workflow.md`](./workflow.md)

## 输入

[`audit-cross-page-links.py`](../../scripts/audit/audit-cross-page-links.py) 的 `missing_backlinks`，或 audit 报告中的 `missing_backlinks`。

## 步骤

1. 筛 P0/P1 页 ↔ 执行链 / Web 数据链等**双向对**
2. 在**源页**加 1 条链指向已优化页（section 或 FAQ 答案均可；遵守 R4）
3. 每批 10–20 对后复跑验收

## 验收

```bash
python ../../clients/Alignify/scripts/audit/audit-cross-page-links.py --locale both
```

*reverse-links · v1.1 · 2026-09-03 · 自 optimize-internal-links 迁入*
