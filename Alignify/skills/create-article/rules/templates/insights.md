# Insights 页面模板

> 原 `content/templates/template-*` 中 Insights 结构摘要。完整类型说明见 [article-types.md](../article-types.md)。

---

## 页面结构

```
核心要点(md) → 背景/趋势 section → 分析 sections×N → 案例/数据 → 结论 → FAQ(7, md) → References(md，仅事件相关，见 [references.md §3.2](../sections/references.md))
```

## 路径

- 正文：`content/insights/{locale}/{slug}.md`
- Meta：`insights-meta.ts` / `insights-pages-config.ts`

## Meta 规则组

分析型：title 突出洞察角度；description 含 2–3 个核心论点或数据点。

---

*templates/insights · v1.0 · 2026-08-26*
