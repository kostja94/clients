# Clink SelfCheck — H4 + C1–C4（叠加 L0）

> **L0 通用 12 维 + H0–H3** → `E:\Agent执行\blog-create\references\selfcheck.md`
> **本文件** → Clink **H4**（C1–C4 + 结构 + 产品占比）
> 加载时机：**Phase 5**（Gate C）。先跑 `tools/` → L0 H0–H3 → 本文件 H4 → L0 十二维。

---

## Gate C — 全部 Pass 方可 audit-ready

> Gate C：L0 **H0–H4** + **12 维** 全 Pass → **audit-ready**。终审 → `E:\Agent执行\blog-audit\SKILL.md`（publish-ready ≥70）。

**执行顺序**：`tools/` 脚本 → L0 H0–H3 → **本文件 H4 + C1–C4** → L0 十二维。

---

## H4 — Clink-Specific（含 C1–C4）

| ID | Pass 标准 |
|----|----------|
| **C1** | 无具体 Clink 费率数字（Contact Sales） |
| **C2** | MoR/tax 有限定语或 as-of |
| **C3** | 证言 as-of；无夸大 GMV |
| **C4** | Agentic Payments → Early Access（若提及） |
| — | 产品占比 ≤ 类型上限（见 `article-types.md`） |
| — | 品牌名统一 **Clink**；域名 clinkbill.com |
| — | frontmatter **无** keywords / related / disclosure |
| — | **倒数第二节 `## Conclusion`，最后一节 `## FAQ`**（6 题） |
| — | 集群文 `category` 与 folder 一致（Agentic Payments / Stripe Risk / Industry News） |

---

## 维度 12 扩展（Clink）

L0 维度 12 默认为 Project-Specific。Clink 替换为：

| 检查项 | Pass 标准 |
|--------|----------|
| Cross-Article | 同 cluster 无矛盾；Glossary 簇互链闭环 |
| Series 05–09 | 符合 `references/series-canonical-ownership.md` |
| Financial compliance | C1–C4 零触发 |

---

## `--intent` 与 H3 硬门槛

| 类型 | `--intent` | 推荐 `--min` |
|------|------------|-------------|
| BrandIntroduction | `brand` | 2500 |
| Comparison | `comparison` | 1600 |
| Product / StripeRisk | `product` | 1800 |
| Opinion / IndustryNews | `opinion` | 1800 |
| EvaluationComparison | `evaluation` | 2500 |
| GlossaryTerm | `glossary` | 1800 |

脚本硬门槛为最低线；**优先用 `--min` 传入上表推荐值**。

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}
### Tools
| Script | Result |
### Hard Gates H0–H4
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

*selfcheck · v2.0.0 · 2026-08-23 · L1 overlay on blog-create*
