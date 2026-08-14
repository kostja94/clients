# Golden Brief — stock-api-free-comparison（已发稿回归基准）

> 基于 `qveris/blog/01-stock-api-free-comparison.md`（2026-07-24）提取的 golden 样本。回归测试用：按 qveris-blog-article skill 复现该 Brief → Outline → 成稿流程，输出应达到同等质量与信息增量。

## Golden Brief

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
1. 明确区分 permanent free tier / free feed / signup credit / sandbox 四类免费模型（SERP 常见混淆）
2. 全部 8 家免费档 2026-07-24 复核 + 商业使用权逐项核对（数据时效）
3. 含可复现 Python 测试脚本（Alpha Vantage demo key，含延迟/时间戳/限流记录）
**Primary product link(s)**: （本文为纯第三方对比，QVeris 未直接出现）
**KEEP/MERGE**: KEEP
**Compliance notes**: API 价格为估算 → 注明以官方为准；不涉及投资建议；数据 as of 2026-07-24
```

## Golden Outline（8 个编号 H2 + 无 Conclusion/FAQ 尾）

> 01 已发稿用**编号 H2**（`## 1.`…`## 8.`）且**无 Conclusion/FAQ 尾**（FAQ 由 CMS 经 tocExtra 渲染）——这是 QVeris 已发格式的合法变体。描述性 H2 与 Conclusion/FAQ 尾为推荐样式（多数官网文），非强制。

```
正文：`# H1` title → `*excerpt*` → `## TL;DR`（3–5 条：Fast answer / Important correction / Decision rule）→ 正文 H2…
## 1. Which Free Stock API Offers Real-Time Data Without a Credit Card?
## 2. What "Free Stock API" Means in 2026
## 3. The 8 Best Free Stock APIs Compared (Updated July 2026)
## 4. Best Free Stock API by Use Case
## 5. Provider Deep Dive: Strengths, Limits and Hidden Trade-Offs
## 6. Free Stock API Limits That Actually Matter
## 7. Free Stock API Python Example: Test Before You Integrate
## 8. When a Free Stock API Stops Being the Right Choice
```

## Golden 断言（回归通过标准）

| 维度 | 断言 |
|------|------|
| Frontmatter | slug 无年份；metaTitle 含 `\| QVeris`；frontmatter 无 tldr/title/excerpt；publishedAt 唯一 |
| 正文头 | `# H1` title 45–90 字符含主关键词；`*excerpt*` ≥40 字符；`## TL;DR` ≥3 条且首条 BLUF ≥40 字符 |
| 信息增量 | ≥2 项独有（四类免费模型 / 逐项复核 / 可复现脚本） |
| 结构 | H2 描述性或编号均可（本 golden 为编号）；Conclusion/FAQ 建议非强制 |
| 数据 | 8 家逐行对比表；价格估算注"以官方为准"；无投资建议 |
| 决策 | Use Case 表给"Job Shape → What Decides It → Start With" |
| 可执行 | Python 示例可复现（demo key） |

## 复现脚本（回归）

```bash
# 1) 校验成稿 frontmatter（应 PASS）
python tools/frontmatter_validator.py ../../blog/01-stock-api-free-comparison.md --keyword "free stock api"

# 2) 叙事词数（comparison 下限 2500，应 PASS）
python tools/word_count_narrative.py ../../blog/01-stock-api-free-comparison.md --intent comparison

# 3) 链接检查（应 PASS：本文外部链接多，内部 blog 链按语境）
python tools/link_checker.py ../../blog/01-stock-api-free-comparison.md
```

> 注意：01 是纯第三方对比文（QVeris 未出现），link_checker 的"internal blog links ≥2"预期在本例可能告警——回归时以 golden 断言为准，不强求非品牌对比文强塞内链。
