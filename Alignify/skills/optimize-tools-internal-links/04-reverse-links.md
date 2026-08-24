# 反向互链 SOP

Phase 4 专批；不在单页 Wave 内同步做，避免改动面过大。

## 输入

`audit-cross-page-links.py` 的 `missing_backlinks` 或 baseline 报告中的 `missing_backlinks`。

## 步骤

1. 筛选 P0/P1 页 ↔ 执行链 / Web 数据链双向对
2. 在**目标源页**增加 1 条指向已优化页的链
3. 遵守全文 href 唯一（R4）
4. 优先 howItWorks、useCases 或 FAQ（不与现有 slug 重复）

## 批量执行

```bash
python scripts/permanent/apply-reverse-backlinks.py --locale both --dry-run
python scripts/permanent/apply-reverse-backlinks.py --locale both --max 50
```

## 验收

复跑 `audit-cross-page-links.py --locale both`，P0/P1 缺回链数应下降。
