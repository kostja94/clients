# Gate 失败回溯表

> Step 10 SelfCheck 或 audit-article 任一 Fail 时，按本表回退。**随 create-article 分发。**

---

## Gate C / SelfCheck Fail

| Fail 维度 / 项 | 回退至 | 典型原因 |
|----------------|--------|----------|
| H0 Research | Step 02 | 无 SERP Fit、Synthesis 空、IG 未答 |
| H1 G1–G7 / P0 | Step 05–06 + Step 02 | 事实错误、死链、无来源数字 |
| H2 Brief | Step 02 | Moat 未声明或未在大纲体现 |
| H3 双语 parity | Step 09 或 Step 05 | EN 缺节、锚点 id 不一致 |
| H4 深度 / BLUF | Step 05–06 | TL;DR 弱、FAQ 复制正文、伪列表 |
| 维度 8 内链 | Step 07 | distinct <5、FAQ 含链、硬插锚文本 |
| 维度 9 SEO/Meta | Step 08 | title 无 Best/最佳、H1 含年份 |
| 维度 11 结构 | Step 05 大纲 | 结论在 FAQ 后、缺主体节 |
| 脚本 audit 红 | 对应 Step | meta-titles、en-content、internal-links |

---

## Gate A / 0R Fail

| 结果 | 动作 |
|------|------|
| Gate A → STOP | 终止；改关键词或合并至已有 slug |
| Gate A → MERGE | 并入 target slug，不新建页 |
| Gate 0R → 无 Synthesis | 回 Step 02 补 R3 Fetch |
| Gate 0R → IG-2 Fail | 改角度或 STOP（删本篇不会少实质信息 → 无增量） |
| Outline 3.5 Fail | 改 Planned H2 或 MERGE 同批冲突篇 |

---

## Final Audit Fail

| 结果 | 动作 |
|------|------|
| P0 BLOCKED | 不得发布；按 G# 回 Step 05–07 |
| 总分 <80 | 按十维低分项回 Step 05–09 |
| P1 未清零 | 修复或记录 waive 理由（仅非 flagship 场景；Alignify 默认 **须清零**） |

---

*gate-rollback · v1.0 · 2026-08-26*
