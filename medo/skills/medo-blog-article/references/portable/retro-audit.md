# 已发布稿回溯审计（Retro Audit）

> 对已发布 `.md` 做合规扫描，**只输出 diff 清单，不改文**。随 skill 分发。

---

## 使用方式

```
请按 references/portable/retro-audit.md 对 {path} 做合规扫描，只输出 diff 清单，不改文。
项目配置：{brand · domain · pillar · 禁链}
```

加载 skill 内 `content-graph.md`、`project-config.md` 作互链与 Gate 补充。

---

## 回溯检查项（14 项）

| # | 检查项 | 查什么 |
|---|--------|--------|
| R1 | Hub-Spoke 互链 | content-graph；Spoke↔Pillar |
| R2 | 产品数字 as-of | 定价/能力/政策是否过时 |
| R3 | 竞品公平性 | 对比文是否有竞品优势段 |
| R4 | 碎片化 | 长段不足、列表堆砌 |
| R5 | 空泛句 / AI 腔 | hype、模板化开头 |
| R6 | 列表占比 | 是否超限 |
| R7 | Frontmatter | title/desc/slug 完整；2026-08-14 起不含 image/keywords/related |
| R8 | 上下文内链 | 不设文末 Related 区块；内链全部为上下文内链（正文自然嵌入）；Spoke 链回 Pillar |
| R9 | Information Gain | vs SERP 是否仍有增量 |
| R10 | Slug 合规 | 反模式、年份 in slug 等 |
| R11 | Meta title/desc | 长度、主词 |
| R12 | Canonical 引用 | 非 canon 文是否越界展开 |
| R13 | 证据链 | 裸数字、缺 Source Map |
| R14 | 跨篇矛盾 | 与同 cluster 其他稿冲突 |

Status：✅ Pass · ⚠️ Partial · ❌ Fail

---

## 输出格式

```markdown
## Retro Audit — {slug}

**Date**: YYYY-MM-DD

| # | 检查项 | Status | Detail |
|---|--------|:------:|--------|

**P1**: …
**P2**: …
```

Retro **不替代** P0 + 十维终审；修复 P1 后建议跑 `final-audit.md`。

---

*retro-audit · portable v1.0*
