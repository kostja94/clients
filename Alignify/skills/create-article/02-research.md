# Step 2 — Research & Article Brief（Gate 0R）

> **适用**：**所有 articleType**（含 best-ranking / legacy）— Alignify **无 Research 跳过**  
> **产出**：Research Log + SERP Fit + **Article Brief 定稿**  
> **SSOT**：[`article-brief.md`](article-brief.md)
>
> Research 三角规范已并入本文件（2026-09-09）

---

## Flagship 深度（固定）

| 步骤 | 要求 |
|------|------|
| R1 | **优先** Brief 的 `SSOT: {绝对路径}`（如 `E:\个人知识库\增长策略-Growth`）；**禁止**增长策略类再读/建 `knowledge/marketing/{slug}.md` 副本 + README + cannibalization |
| R2 | primary keyword **中英**各搜 → SERP Top **5** + PAA |
| R3 | Fetch **≥5** URL（SERP Top 3–5 + **≥2** 产品官方页） |
| Synthesis | 三问 + **同句测试** Pass |
| IG | 三问全答，**IG-2 必 Pass** |
| Examples | **≥2** |
| Moat | **≥1** 写入 Brief |

---

## Gate 0R Checklist

- [ ] Research Log 完整（R1/R2/R3 表）
- [ ] SERP Fit 模板已填（见本文件 §SERP Fit 模板）
- [ ] Synthesis Statement（80–150 字 ZH）
- [ ] IG-1/2/3 已答
- [ ] Candidate Examples ≥2
- [ ] **Article Brief** 按 [`article-brief.md`](article-brief.md) 定稿（Moat + Answer Blocks 3–5）
- [ ] **best-ranking**：Brief **`Product roster`** + **`Product dedup check`** 全 clear（[`product-coverage.md`](product-coverage.md)）
- [ ] Brief **Copy quality** 字段已填（`Copy mode`；M2 时 `cluster hub` / `swap neighbors`；见 [`copy-quality.md`](copy-quality.md) 附录 A）
- [ ] Brief 中 Planned H2 与 Step 01 大纲一致或说明变更

**Fail** → 补 R2/R3 或 STOP（见 [`quality-gates.md`](quality-gates.md)）

**Degraded**（WebSearch/Fetch 不可用）：标注 `Research mode: Degraded`；P0 数字不得写未验证 claim；Gate 0R **不得 Pass** 直至人工补 R3。

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

**IG 判据**（Research Log 内必答三问，IG-2 必 Pass）：

| # | 问题 | Fail 动作 |
|---|------|----------|
| **IG-1** | 核心 claim 能否贴进另外 10 篇同类 Alignify 文？ | 改角度 |
| **IG-2** | 删掉本篇，网上会少**实质性**信息吗？ | STOP |
| **IG-3** | 前 30% 能否用 40–60 词（ZH）/ 40–60 words（EN）独立成段？ | 加强 TL;DR / Answer Blocks |

**Candidate Examples 判据**：

- 禁止「某 AI 公司…」式模糊案例
- Tools 文：优先真实产品场景、定价区间、工作流片段

---

## SERP Fit 模板（Step 02 产出 · Step 10 复核）

> Step 02 产出物；Step 10 SelfCheck 复核时按下方「Flagship 硬性检查」逐项核对。
> Step 10 复核判据见 `quality-gates.md`。
> （模板 2026-09-09 由原独立文档并入）

### 模板

```markdown
## SERP Fit — {slug}

**Primary keyword**（ZH）:
**Primary keyword**（EN）:
**Search intent**: [ ] Definition  [ ] Comparison  [ ] Tutorial  [ ] Alternative  [ ] Commercial  [ ] Best-of

**Top 5 ranking pages**:
1. URL — covers:
2. URL — covers:
3. URL — covers:
4. URL — covers:
5. URL — covers:

**PAA / related searches**（FAQ 应对齐）:

**Common coverage across top pages**:

**What they miss**:

**Our unique contribution**（= Brief Moat）:

**Snippet-ready definition**（ZH 40–80 字 / EN 40–60 words）:
```

### Flagship 硬性检查（Step 10 复核）

- [ ] 回答 primary keyword 背后的真实问题
- [ ] 比 SERP 前 5 多至少 **一个** Alignify 独有角度（Moat）
- [ ] Meta title 匹配 search intent（Tools：含最佳/Best）
- [ ] TL;DR intro 让读者 10 秒内确认「来对地方了」
- [ ] SERP Fit：**若**采用 FAQ，7 问覆盖 PAA / 正文未展开的决策点
- [ ] Snippet-ready 定义与 TL;DR intro 信息一致、非重复堆砌

---

## Article Brief

Gate 0R Pass 后，将 Brief 写入 `knowledge/{dir}/_briefs/{slug}.md`（或对话留存）；**外部 SSOT** 时在 Brief 顶部写 `**SSOT**: {绝对路径}`。Step 05（[`content-locale.md`](content-locale.md) Part 2）动笔前 **不得偏离** One-line thesis 与 Moat。

---

## 输出

- [ ] Gate 0R：**PASS**
- [ ] Brief 路径或完整粘贴
- [ ] Moat Asset 一行摘要

下一步：[03-keywords.md](03-keywords.md)
