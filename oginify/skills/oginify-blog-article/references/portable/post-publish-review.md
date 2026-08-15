# Post-Publish Review — 发布后复盘

> 便携参考 · Phase 6（Brief 参考）· T+7/30/90/180

---

## 1. 时间线

| 检查点 | 关注 |
|--------|------|
| T+7 | 收录状态、CTR、生成量（GA/搜索控制台） |
| T+30 | 排名位置、进 Hub 互链是否生效 |
| T+90 | 排名趋势、FAQ 命中 PAA 与否 |
| T+180 | 内容是否过时（竞品/定价变化）、Refresh 决策 |

---

## 2. 复盘指标（对照 Brief SuccessMetric）

| 指标 | 目标 | 实际 | 判定 |
|------|------|------|------|
| 主关键词排名 | {Top N} | ... | PASS/FAIL |
| CTR | {基准} | ... | PASS/FAIL |
| 生成量（注册/工具点击） | {N} | ... | PASS/FAIL |

---

## 3. 复盘问题

- [ ] 读者是否在正文找到答案？（跳出率）
- [ ] 竞品/定价是否变化？（as-of 过期？）
- [ ] 内链是否全部有效？
- [ ] 是否需 RefreshInPlace / Promote / Archive？（见 retro-audit.md）

---

## 4. 动作

- 实质性更新 → 改 `updated` 字段 + bump SKILL version patch
- 收录异常 → 检查 frontmatter/robots/sitemap
- 排名差 → retro-audit 定位
