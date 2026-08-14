# FinalRound Final Audit（Skill reference · portable）

> **发布前终审。** Phase 6 使用。独立于创作自检的**加权评分**。

---

## 1. 使用方式

创作 Agent 在 Delivery 输出审核指令，由**另一视角**（人工或独立 Agent）执行终审：

```
请按 finalround-blog-article skill 内 references/portable/final-audit.md 审核 finalround/blog/NN-{slug}.md

项目配置：
- 品牌：FinalRound
- 主域名：finalroundai.com
- 博客前缀：/blog/
- 核心产品：Interview CoPilot™（桌面应用）；无免费试用
- 作者：Kostja

要求：
1. 先过 P0 Gate G1–G7 + F1–F5
2. 逐维评分（A–J 十维加权 → 100 分）
3. 输出十维评分 + 总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
4. 标记 P1/P2
```

## 2. P0 Gate（先过，任一 Fail → 不评分）

- **G1–G7**（见 gates-master）
- **F1–F5**（见 gates-master）

## 3. 十维加权评分（A–J）

| 维度 | 权重 | 要点 |
|------|:---:|------|
| A. Publishability | 10% | G/F Gate 通过后清零重计 |
| B. Fact / E-E-A-T | 15% | 可验证 claim 有来源；Source Map |
| C. Differentiation | 15% | 正文兑现 Synthesis；IG 成立 |
| D. Depth | 10% | 词数、FAQ 独立、例子密度 |
| E. Presentation | 10% | 段落节奏、列表、衔接 |
| F. Writing / Voice | 10% | Voice 5 项、禁词、空泛句 |
| G. Objectivity | 10% | 产品占比、竞品公平、漏斗 |
| H. Structure / Links | 5% | 模块完整、内链、锚文本 |
| I. SEO / SERP | 10% | title/description、BLUF、slug |
| J. Conversion | 5% | CTA 匹配、无免费试用文案 |

## 4. 等级

| 总分 | 等级 |
|------|------|
| ≥90 | **S** |
| 80–89 | **A** |
| 70–79 | **B** |
| 60–69 | **C** |
| <60 | **D** |

**Excellence**：`Yes — {类型}` / `No`
**Moat Asset 兑现**：`Yes/Partial/No`
**Perfect gap**：对照 perfect-article-checklist 的缺失项

## 5. P1/P2 标记

- **P1**：发布前必须修复
- **P2**：发布后可优化

---

*final-audit · portable · 可跨项目复用（FinalRound 配置定制）*
