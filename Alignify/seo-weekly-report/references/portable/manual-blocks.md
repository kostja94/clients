# 手动块规范

API **无法**替代的部分，每周由人填写后交给 Agent。

| 块名 | 模板文件 | 用途 |
|------|----------|------|
| `===CONTENT===` | content-weekly-block.txt | 新发布/更新内容与索引状态 |
| `===BACKLINKS===` | backlinks-weekly-block.txt | 购买/获得外链 |
| `===PROJECT_STATUS===` | project-status-block.txt | 技术 SEO / 执行项 |
| `===OBSERVATIONS===` | observations-block.txt | 异常与假设 |

**硬性规则**：`week_start` / `week_end` 必须与 bundle `period.current` 一致。

---

## Agent 处理要求

1. 解析 YAML 风格字段（冒号后内容）  
2. `===CONTENT===.published` × bundle `gsc.pages` / `ga4.topPages` → 每篇新文：首周点击、sessions、是否已有展示  
3. `===BACKLINKS===` → 报告外链章；若有 GA4 Referral 可交叉提及（不强制）  
4. 若某块为空，对应章节写「本周未提供」  

---

## UTM 提醒（外链投放）

外链若带 campaign，建议：

- `utm_source` / `utm_medium` / `utm_campaign`  
- 便于 GA4 Source/Medium 报告核对（**Paid/Social 完整归因见 extensions.md**）
