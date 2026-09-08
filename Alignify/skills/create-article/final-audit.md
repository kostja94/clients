# Final Audit — 发布前终审 Rubric（Step 11 入口）

> SelfCheck Pass = **audit-ready**，**不保证** publish-ready。  
> **流程入口**：本文件即 **Step 11 终审入口与 Rubric**（原 `11-final-audit` 入口壳已并入）——须在**新会话 / 另一 Agent / 人类**执行，**禁止写稿同一会话自审**，**不得跳过终审直接发布**。  
> **前置**：Step 10 SelfCheck **全 Pass** → audit-ready；送审包齐全（见 [`quality-gates.md`](quality-gates.md) §Step 10 交付物）。  
> **阈值同步**：若调整分数线，须与 [`../audit-optimize/rules/page-audit.md`](../audit-optimize/rules/page-audit.md) 保持一致。

---

## 入口与触发语（Step 11）

**何时使用**

- [ ] ZH + EN md 已完成  
- [ ] Step 10 SelfCheck **全 Pass**（H0–H4 + 12 维）  
- [ ] Source Map + SERP Fit + Brief 可查阅  

**不适用**

| 场景 | 改用 |
|------|------|
| 从选题到成稿 | 本 skill Step 01–10 |
| 已发稿健康检查 / 内链 / 局部刷新 | audit-optimize 技能（`../audit-optimize/SKILL.md`） |
| 成稿未过 Gate C | 回 Step 10（[`quality-gates.md`](quality-gates.md)） |

**触发语（复制到新会话）**

```text
按 Alignify create-article Step 11 终审：
- ZH：content/{channel}/zh/{slug}.md
- EN：content/{channel}/en/{slug}.md
- Primary keyword：{kw}
- SelfCheck：12/12 + H0–H4 Pass
- Brief Moat：{一行}
- 预检：audit-marketing-md-render.py --slug {slug} 全量 blog Pass 后才开始打分
```

---

## 审核前填写

| 配置项 | 值 |
|--------|-----|
| 站点 | alignify.co |
| 待审 ZH | `content/{channel}/zh/{slug}.md` |
| 待审 EN | `content/{channel}/en/{slug}.md` |
| Primary keyword | |
| Brief Moat（1 行） | |

---

## P0 Gate（任一项 → BLOCKED，不得发布）

P0 事实 Gate G1–G7 定义见 [quality-gates.md](quality-gates.md) §P0 Gate G1–G7；Alignify 结构 / Meta P0（P0-1–P0-13）见同文件 §综合质量检查表。

**Alignify 结构 P0**（与 create-article P0-1–P0-13 一致）：md 以 `#conclusion` 收束、FAQ JSON 7 问（内链若存在须 R4 全文 1 次）、Meta Best/最佳、无 `howTo:`/`heroHtml:` frontmatter（E44）、Brief 与 TL;DR/FAQ/Refs JSON 一致（E10）等。

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

> 本会话**只读本文件**（入口与触发语 + Rubric 合一），**不加载 Step 01–09 规范**；需要 Brief / Source Map / SERP Fit 产出物时按需读取（加载纪律见文末 §渐进加载）。

0. **自动化全量预检（必跑，Fail 则修复后重跑直至 Pass）**  
   - `python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py --slug {slug}` — **全部** `content/blog/*`（**不按 category 过滤**）；blog 通道 E37 伪列表 ≥3 为 **Fail**  
   - `python ../../clients/Alignify/scripts/audit/audit-frontmatter.py`  
   - `npm run verify:content-json` · `npm run build`（部署仓根目录）  
   - 任一脚本 Fail → **不得进入十维打分**；修复后**从头重跑**预检清单  
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

## 渐进加载

终审会话默认**只读本文件**；需要时最多再读 **Brief / Source Map / SERP Fit** 产出物。**禁止一次性加载全部规范文档**（Step 01–09）。Fail → 按 [`quality-gates.md`](quality-gates.md) §Gate 失败回溯表 回退修复后重跑本 Step。

---

*final-audit · v2.0 · 2026-09-09 · 自 audit-article 迁入 create-article；并入 Step 11 入口壳（原 11-final-audit）*
