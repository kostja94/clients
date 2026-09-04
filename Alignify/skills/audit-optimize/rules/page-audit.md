# Page Audit — 已发稿质检（自包含）

> **用途**：audit-optimize 改文后（或 retro 深审）的 P0 + 十维验收。  
> **阈值同步**：分数线若调整，须与 [`../../create-article/rules/final-audit.md`](../../create-article/rules/final-audit.md) 保持一致。本文件完整自包含，**不必**打开 create-article SKILL。

---

## 审核前填写

| 配置项 | 值 |
|--------|-----|
| 站点 | alignify.co |
| 待审 ZH | `content/{channel}/zh/{slug}.md` |
| 待审 EN | `content/{channel}/en/{slug}.md` |
| Primary keyword | |
| 模式 | retro / links / refresh |
| 处置建议（可选） | Retain / Refresh / Merge / Deprecate |

---

## P0 Gate（任一项 → BLOCKED）

| Gate | 阻断条件 |
|------|----------|
| **G1** | 产品/竞品事实与官方 docs 矛盾 |
| **G2** | 站内死链；站外大面积失效 |
| **G3** | 量化 claim 无 attribution |
| **G4** | 竞品状态错误 |
| **G5** | 能力夸大 |
| **G6** | 内链指向未上线页 |
| **G7** | 合规/贬低风险 |

**Alignify 结构 P0**：md 以 `#conclusion` 收束、FAQ JSON 7 问（内链若存在须 R4 全文 1 次）、Meta Best/最佳、无 `howTo:`/`heroHtml:` frontmatter（E44）、Brief/侧车 JSON 一致（E10，若页仍注册）等。

**存量专用**：Refresh / links **不得**改写 `publishDate`；仅允许更新 `modifiedDate`。

输出：`P0 Gate: PASS / BLOCKED by G?`

---

## 十维加权评分（P0 Pass 后）

每维 0–10，加权合计 100：

| 维 | 权重 | 10 分摘要 |
|----|:---:|----------|
| A Strategy & Intent | 10% | 意图正确；thesis 仍兑现；Hub-Spoke 清晰 |
| B SEO & SERP | 10% | Meta/H1 合规；SERP Fit；snippet 定义 |
| C Structure | 9% | 内容驱动架构合理；TL;DR + 主体 + 结论 + FAQ |
| D Writing & Voice | 11% | 中英地道；无 AI 腔；具体例子 |
| E Fact & EEAT | 20% | 事实未过期；attribution；E1–E6 |
| F Links & Graph | 6% | 点击意图；同 URL 1 次；Hub/Spoke；无硬插/机械指路 |
| G Differentiation | 14% | Moat 仍成立；非 SERP paraphrase |
| H Bilingual parity | 6% | ZH/EN 信息对等、结构对齐 |
| I Depth & FAQ | 12% | 主体完整；FAQ 独立；Best 段达标 |
| J Presentation | 12% | BLUF 三处；段落节奏；无伪列表 |

**等级**：

| 分数 | 等级 | 动作 |
|------|------|------|
| **≥90** | **S** | 标杆；Moat + Excellence + 零 P1 |
| 80–89 | A | **可上线 / 可保留**（最低线） |
| 70–79 | B | 须修 P1 后再审 |
| <70 | C/D | 扩大 Refresh 范围或建议整篇重写（→ create-article） |

**Alignify 默认**：≥**80** 且 P0 Pass = 通过 page-audit。

---

## 审核步骤

0. **自动化预检（必跑，Fail 则修复后重跑）**  
   - `python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py --slug {slug}` — 全部 `content/blog/*`；blog E37≥3 Fail  
   - `python ../../clients/Alignify/scripts/audit/audit-frontmatter.py`  
   - `python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only`  
   - `npm run verify:content-json` · `npm run build`（部署仓根目录）  
   - 任一 Fail → **不得进入十维打分**
1. P0 逐项（G1–G7 + 结构 P0 + publishDate 未改）  
2. 十维打分  
3. 处置建议：Retain / Refresh / Merge / Deprecate  
4. P1/P2 修复清单  
5. 输出是否通过 page-audit  

仅 **links** 小改且未动主体叙述时：可只跑预检 + P0 + 维 F；文中注明 `Scope: links-only`。

---

## 输出模板

```markdown
## Page Audit — {slug}

**Mode**: retro | links | refresh
**P0 Gate**: PASS | BLOCKED by G?
**Weighted score**: {X}/100 — Grade {S|A|B|C|D}
**Pass**: Yes | No
**Disposition**: Retain | Refresh | Merge | Deprecate
**modifiedDate OK**: Yes | N/A — publishDate untouched

### P1 fixes
1. …

### P2 optional
1. …
```

---

*page-audit · v1.0 · 2026-09-03*
