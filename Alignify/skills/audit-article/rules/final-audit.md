# Final Audit — 发布前终审 Rubric

> SelfCheck Pass = **audit-ready**，**不保证** publish-ready。

---

## 审核前填写

| 配置项 | 值 |
|--------|-----|
| 站点 | alignify.co |
| 待审 ZH | `content/{channel}/zh/{slug}.md` |
| 待审 EN | `content/{channel}/en/{slug}.md` |
| articleType | |
| Primary keyword | |
| Brief Moat（1 行） | |

---

## P0 Gate（任一项 → BLOCKED，不得发布）

| Gate | 阻断条件 |
|------|----------|
| **G1** | 产品/竞品事实与官方 docs 矛盾 |
| **G2** | 站内死链；站外大面积失效 |
| **G3** | 量化 claim 无 attribution |
| **G4** | 竞品状态错误 |
| **G5** | 能力夸大 |
| **G6** | 内链指向未上线页 |
| **G7** | 合规/贬低风险 |

**Alignify 结构 P0**（与 create-article P0-1–P0-11 一致）：结论在 FAQ 前、FAQ 7 问无内链、Meta Best/最佳、无 `howTo:` frontmatter 等。

输出：`P0 Gate: PASS / BLOCKED by G?`

---

## 十维加权评分（P0 Pass 后）

每维 0–10，加权合计 100：

| 维 | 权重 | 10 分摘要 |
|----|:---:|----------|
| A Strategy & Intent | 10% | 意图正确；Brief thesis 兑现；Hub-Spoke 清晰 |
| B SEO & SERP | 10% | Meta/H1 合规；SERP Fit；snippet 定义 |
| C Structure | 9% | 内容驱动架构合理；TL;DR + 主体 + 结论 + FAQ |
| D Writing & Voice | 11% | 中英地道；无 AI 腔；具体例子 |
| E Fact & EEAT | 20% | Source Map；E1–E6 |
| F Links & Graph | 6% | 点击意图；同 URL 1 次；Hub/Spoke；无硬插/机械指路 |
| G Differentiation | 14% | Moat 兑现；非 SERP paraphrase |
| H Bilingual parity | 6% | ZH/EN 信息对等、结构对齐 |
| I Depth & FAQ | 12% | 主体完整；FAQ 独立；Best 段达标 |
| J Presentation | 12% | BLUF 三处；段落节奏；无伪列表 |

**等级**：

| 分数 | 等级 | 动作 |
|------|------|------|
| **≥90** | **S** | 标杆；Moat + Excellence + 零 P1 |
| 80–89 | A | **publish-ready**（Alignify 最低发布线） |
| 70–79 | B | 须修 P1 后再审 |
| <70 | C/D | 回 create-article Step 05–09 |

**Alignify 默认**：≥**80** 且 P0 Pass = **publish-ready**；追求 S 级为每篇 flagship 目标。

---

## 审核步骤

1. 读 Brief + Source Map + SERP Fit  
2. P0 逐项（G1–G7 + Alignify 结构 P0）  
3. 十维打分 + Moat 兑现 + Excellence  
4. P1/P2 修复清单  
5. 输出等级与是否 publish-ready  

---

## 输出模板

```markdown
## Final Audit — {slug}

**P0 Gate**: PASS | BLOCKED by G?
**Weighted score**: {X}/100 — Grade {S|A|B|C|D}
**Publish-ready**: Yes | No
**Moat delivered**: Yes | No — {evidence}
**Excellence**: Yes | No — {type}

### P1 fixes（须清零方可 publish-ready）
1. …

### P2 optional
1. …
```

---

*final-audit · v1.0 · 2026-08-26*
