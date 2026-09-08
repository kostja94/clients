# Clink SelfCheck — H4 + C1–C4（Gate C）

> 加载时机：**Phase 5**（Gate C）。先跑 `tools/` → Hard Gates H0–H4（H4 定义见下）→ 通用 12 维（`references/portable/gates-master.md` 语义 + `final-audit.md` 十维供对照）。
> 词数硬门槛 H3：阈值见 `references/article-types.md` §1（每类型 `--min`）。
> C1–C4 详表 → `references/project-config.md` §4（此处不复制，仅检查项引用）。

---

## Gate C — 全部 Pass 方可 audit-ready

> H0–H4 + C1–C4 + 12 维全 Pass → **audit-ready**。终审 → `references/portable/final-audit.md`（publish-ready ≥70 且 P0 Pass）。SelfCheck ≠ 终审，不可互相替代。

**执行顺序**：`tools/` 三脚本 → H0–H3 → 下方 H4 → 12 维。

---

## Hard Gates H0–H4

| # | Pass 标准 |
|----|----------|
| H0 | Gate 0R 完整（Research Log + Synthesis + SERP Fit 已填） |
| H1 | G1–G7 零触发（详表 → project-config §3） |
| H2 | Gate B 全 Pass（slug-gate.md） |
| H3 | 词数达 article-types §1 类型下限 |
| H4 | Clink-Specific（下表） |

## H4 — Clink-Specific（含 C1–C4 引用）

| ID | Pass 标准 | 判定依据 |
|----|----------|---------|
| **C1** | 无具体 Clink 费率数字 | project-config §4 |
| **C2** | MoR/tax 有限定语或 as-of | project-config §4 |
| **C3** | 证言 as-of；无夸大 GMV | project-config §4 |
| **C4** | Agentic Payments → Early Access（若提及） | project-config §4 |
| — | 产品占比 ≤ article-types §1 类型上限 | article-types |
| — | 品牌名统一 **Clink**；域名 clinkbill.com | project-config §1 |
| — | frontmatter 无 keywords / related / disclosure / image | article-types §4 |
| — | 倒数第二节 `## Conclusion`，最后一节 `## FAQ`（**6 题**） | article-types §2 |
| — | 集群文 `category`/`secondaryCategory` 与 folder 一致 | content-graph §1B |

## 12 维扩展（Clink 替换维度 12）

| 检查项 | Pass 标准 |
|--------|----------|
| Cross-Article | 同 cluster 无矛盾；Glossary 簇互链闭环 |
| Series 05–09 | 符合 `references/series-canonical-ownership.md` |
| Financial compliance | C1–C4 零触发 |

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}
### Tools
| Script | Result |
### Hard Gates H0–H4
| Gate | Pass/Fail | Notes |
### C1–C4
| Gate | Pass/Fail | Notes |
### 12-Dim
| # | Dimension | Pass/Fail | Notes |
### Source Map
| Claim | § | Source | Confidence |
**Status**: audit-ready | needs-fix
```

---

## Perfect-Ready（flagship）

- [ ] Moat Asset 正文兑现
- [ ] Answer Blocks 3–5 可独立成 40–60 词段
- [ ] Excellence 已标注
- [ ] Post-publish Metric Spec 已写入 Brief

---

*selfcheck · v3.0.0 · 2026-09-08 · 去重：--intent 表迁 article-types；C1–C4 详表收敛 project-config*
