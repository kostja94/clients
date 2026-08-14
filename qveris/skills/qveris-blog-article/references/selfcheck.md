# §10 维健康分完整判据（Phase 5）

> 创作自检用（1–5 健康分）。独立发布终审用 `portable/final-audit.md`（S/A/B/C/D 加权评分），两者不可互相替代。

## 评分标准

| 分 | 含义 |
|----|------|
| 5 | 满足该维度全部标准，无明显瑕疵 |
| 4 | 基本满足，1–2 处可改进（交付后人工修） |
| 3 | 部分满足，明显缺口但非阻断（标注 P1） |
| 2 | 不满足核心标准（标注 P1，建议修复后交付） |
| 1 | 严重不满足（等同 Hard Gate Fail，不得交付） |

## 10 维

| # | 维度 | 快速判据 |
|---|------|---------|
| 1 | **Fact / E-E-A-T** | P0 数字全有来源？数据有时效（as of）？竞品 ≥1 优势？Who/How/Why 齐备？ |
| 2 | **Differentiation** | 独有框架/表格 ≥1？句级重复 <30%？信息增量 2 项已验证？ |
| 3 | **Presentation** | 长段落 ≥3？列表占比 ≤上限？0 碎片化集群？表格前后有分析？ |
| 4 | **Writing / Voice** | 五正向全满足？禁词 0？空泛句 ≤2？≥1 具体 scenario？ |
| 5 | **Objectivity** | 漏斗符合类型标准？产品 ≤上限？无贬低措辞？无投资建议暗示？ |
| 6 | **Structure / Links** | 正文 `## TL;DR` 区块 ≥3 条？Conclusion+FAQ 收尾？blog 互链 ≥2？锚文本语义化？ |
| 7 | **SEO** | title 含 P1？description 120–160？metaTitle 含 `\| QVeris`？slug 常青？ |
| 8 | **Depth** | 词数在区间？每 ~500 词 ≥1 例子？FAQ ≥3 且 ≥1 题独立？ |
| 9 | **QVeris + Compliance** | 品牌正确？协议叙事准确？F1–F4 全过？ |
| 10 | **Conversion** | CTA ≤2？匹配读者阶段？CTA 前有独立价值？ |

## 整体判定

- **整体** = 10 维平均；🟢 ≥4.0 / 🟡 3.0–3.9 / 🔴 <3.0
- **交付标准**：Hard Gates 全部 Pass + 无 🔴 维度。🟡 维度标注 P1 修复项。

## 输出格式

```markdown
## SelfCheck — {slug}
### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| G1–G7 | Pass | |
| F1–F4 | Pass | (or: F skipped — non-financial topic) |
| Slug  | Pass | |
### Health Check
| # | Dimension | Score | Notes |
|---|-----------|:---:|-------|
| 1 | Fact/E-E-A-T | 4/5 | … |
**Overall**: 4.2/5.0 🟢
### Information Gain Statement
{3 sentences vs SERP Top3}
### Source Map (internal)
| Claim | § | Source | Checked | Confidence |
### Cannibalization Check
| vs | Boundary | Clear? |
**🟡 P1 fixes**: …
**Human decisions** (⚠️ items): …
```
