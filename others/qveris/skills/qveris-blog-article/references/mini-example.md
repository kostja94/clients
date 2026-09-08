# §10 Mini Example（Brief + Outline 范例）

> 以已发稿 `01-stock-api-free-comparison.md`（Comparison 类）为基准样本，展示 Brief → Outline → 成稿的对应关系。

## Article Brief 范例（01 实际）

```markdown
## Article Brief
**Working title**: Best Free Stock APIs for Real-Time, Historical & Python Use (2026)
**Primary keyword**: free stock api
**Search intent**: [x] Commercial
**Article type**: Comparison（ToolsList 子类）
**Reader stage**: Evaluation
**Publish goal**: SEO
**Target audience**: developers / quant engineers evaluating free data APIs
**Word count target**: 2800–3500
**Cluster role**: Standalone（系列第一篇）
**Canonical concept links**: (none yet — first in series)
**Differentiation angle**: corrects the "free = permanent tier" misconception; Polygon→Massive rebrand; Databento as evaluation credit
**Information Gain Statement**:
1. 明确区分 permanent free tier / free feed / signup credit / sandbox 四类免费模型
2. 全部 8 家免费档 2026-07-24 复核 + 商业使用权逐项核对
3. 含可复现 Python 测试脚本（Alpha Vantage demo key）
**Primary product link(s)**: （本文为纯第三方对比，QVeris 未直接出现）
**KEEP/MERGE**: KEEP
**Compliance notes**: API 价格为估算 → 注明以官方为准；无投资建议（不涉及行情建议）
```

## Outline 范例（01 实际）

```
正文：`# H1` title → `*excerpt*` → `## TL;DR`（3–5 条：Fast answer / Important correction / Decision rule）→ 正文 H2…
## Which Free Stock API Offers Real-Time Data Without a Credit Card?
## What "Free Stock API" Means in 2026        ← 四类免费模型（差异化）
## The 8 Best Free Stock APIs Compared (Updated July 2026)   ← 主对比表
## Best Free Stock API by Use Case           ← 决策表
## Provider Deep Dive: Strengths, Limits and Hidden Trade-Offs  ← 8 家逐个
## Free Stock API Limits That Actually Matter  ← 五个关键限制
## Free Stock API Python Example: Test Before You Integrate   ← 代码
## When a Free Stock API Stops Being the Right Choice
## Conclusion
## Frequently asked questions
```

## Brief → 成稿 关键映射

| Brief 要素 | 成稿落点 |
|-----------|---------|
| Information Gain（四类免费模型） | H2 `## What "Free Stock API" Means in 2026` |
| 决策表意图 | H2 `## Best Free Stock API by Use Case` |
| 可复现脚本 | H2 `## Free Stock API Python Example…` |
| API 价格估算 + 以官方为准 | 表注 + 数据来源标注 |
| FAQ | 从 PAA / 决策表推导 ≥3 题 |

## 第二篇 Brief 模板（空白，直接复用）

```markdown
## Article Brief
**Working title**: {title}
**Primary keyword**: {keyword}
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional
**Article type**: {from §2 route}
**Reader stage**: {stage}
**Publish goal**: SEO / Brand / Conversion
**Target audience**: {描述}
**Word count target**: {按类型区间}
**Cluster role**: Pillar / Spoke / Standalone
**Canonical concept links**: {link only, do not redefine}
**Differentiation angle**: {vs SERP top 3}
**Information Gain Statement**: {≥2 项}
**Primary product link(s)**: {白名单内}
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Compliance notes**: {F1–F4 checklist / comparison fair-treatment / field-test provenance}
```
