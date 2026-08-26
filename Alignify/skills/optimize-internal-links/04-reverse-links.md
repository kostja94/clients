# 反向互链 SOP

> 入口：[`SKILL.md`](SKILL.md) · 单页流程：[`03-per-page-workflow.md`](03-per-page-workflow.md) · 规则：[`references/rules-quickref.md`](references/rules-quickref.md)

Phase 4 专批；不在单页 Wave 内同步做，避免改动面过大。

## 输入

[`audit-cross-page-links.py`](../../scripts/audit/audit-cross-page-links.py) 的 `missing_backlinks`，或 [`audit-tools-internal-links.py`](../../scripts/audit/audit-tools-internal-links.py) baseline 报告中的 `missing_backlinks`。

## 步骤

1. 筛选 P0/P1 页 ↔ 执行链 / Web 数据链双向对
2. 在**目标源页**增加 1 条指向已优化页的链
3. 遵守全文 href 唯一（R4）
4. 优先 howItWorks、useCases 或 FAQ（不与现有 slug 重复）

## 批量执行

按步骤 1–3 逐对手动写入（遵守 R-LINK-ONLY）。无自动化脚本时，每批 10–20 对后复跑验收。

## 验收

```bash
python ../../clients/Alignify/scripts/audit/audit-cross-page-links.py --locale both
```

P0/P1 缺回链数应下降。
