# Retro — 已发稿回溯

> 季度内容健康检查或重大产品/定价变更后使用。入口：[`SKILL.md`](./SKILL.md)

---

## 快速 P0 扫描

- [ ] G1–G4：定价、能力、竞品状态仍正确？
- [ ] G2：内链/外链仍有效？
- [ ] Meta title/description 仍符合当前规则？
- [ ] FAQ 7 问仍覆盖真实 PAA？

完整 P0 / 十维见 [`rules/page-audit.md`](./rules/page-audit.md)。仅出建议时可不跑十维全表。

---

## 12 维回溯摘要

对每维打 **Retain / Refresh / Deprecate**：

| 维 | 判定 | 动作 |
|----|------|------|
| Differentiation | Retain/Refresh | Moat 是否仍独有？ |
| Fact & EEAT | … | 数字/政策是否过期？ |
| SERP | … | 是否被新 SERP 模式超越？ |

---

## 处置建议

| 建议 | 条件 | 下一步 |
|------|------|--------|
| **Retain** | P0 Pass；分数仍 ≥80 | 结束；可选记入季度日志 |
| **Refresh** | 事实过期或 SERP 落后 | → [`03-refresh.md`](./03-refresh.md) 改正文 + `modifiedDate` |
| **Merge** | 与另一 slug cannibalization | 人类决策 301 / Hub 合并 |
| **Deprecate** | 品类失效 | 人类决策 301 或 Hub 合并 |

若处置为 Refresh 并落地修改 → 过 [`rules/page-audit.md`](./rules/page-audit.md)。

---

*01-retro · v1.0 · 2026-09-03 · 自 audit-article/rules/retro-audit.md 迁入*
