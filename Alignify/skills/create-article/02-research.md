# Step 2 — Research & Article Brief（Gate 0R）

> **适用**：**所有 articleType**（含 best-ranking / legacy）— Alignify **无 Research 跳过**  
> **产出**：Research Log + SERP Fit + **Article Brief 定稿**  
> **SSOT**：[`rules/research-triangle.md`](./rules/research-triangle.md) · [`rules/article-brief.md`](./rules/article-brief.md)

---

## Flagship 深度（固定）

| 步骤 | 要求 |
|------|------|
| R1 | **优先** Brief 的 `SSOT: {绝对路径}`（如 `E:\个人知识库\营销campaign\`）；**禁止** campaign 类再读/建 `knowledge/marketing/{slug}.md` 副本 + README + cannibalization |
| R2 | primary keyword **中英**各搜 → SERP Top **5** + PAA |
| R3 | Fetch **≥5** URL（SERP Top 3–5 + **≥2** 产品官方页） |
| Synthesis | 三问 + **同句测试** Pass |
| IG | 三问全答，**IG-2 必 Pass** |
| Examples | **≥2** |
| Moat | **≥1** 写入 Brief |

---

## Gate 0R Checklist

- [ ] Research Log 完整（R1/R2/R3 表）
- [ ] [`serp-fit-template.md`](./rules/serp-fit-template.md) 已填
- [ ] Synthesis Statement（80–150 字 ZH）
- [ ] IG-1/2/3 已答
- [ ] Candidate Examples ≥2
- [ ] **Article Brief** 按 [`article-brief.md`](./rules/article-brief.md) 定稿（Moat + Answer Blocks 3–5）
- [ ] Brief 中 Planned H2 与 Step 01 大纲一致或说明变更

**Fail** → 补 R2/R3 或 STOP（见 [`gate-rollback.md`](./rules/gate-rollback.md)）

---

## Research Log 模板

```markdown
## Research Log — {slug}

### R1 — SSOT
| # | 来源 | 关键发现 | Confidence |

### R2 — SERP
| Query | Rank | URL | 覆盖点 | 缺口 |

### R3 — Fetch
| URL | 关键数据 | 用于 section / Source Map | Confidence |

### Synthesis Statement
1. SERP 未说的：…
2. 一句话论点（Top5 找不到同句）：…
3. 读者改变：…

### IG-1 / IG-2 / IG-3
…

### Candidate Examples
| 例子 | 来源 | section |
```

---

## Article Brief

Gate 0R Pass 后，将 Brief 写入 `knowledge/{dir}/_briefs/{slug}.md`（或对话留存）；**外部 SSOT** 时在 Brief 顶部写 `**SSOT**: {绝对路径}`。Step 05（[`content-locale.md`](./rules/content-locale.md) Part 2）动笔前 **不得偏离** One-line thesis 与 Moat。

---

## 输出

- [ ] Gate 0R：**PASS**
- [ ] Brief 路径或完整粘贴
- [ ] Moat Asset 一行摘要

下一步：[03-keywords.md](./03-keywords.md)
