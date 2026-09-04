# Step 11 — Final Audit（→ publish-ready）

> **Rubric SSOT**：[`rules/final-audit.md`](./rules/final-audit.md)  
> **硬性**：须在**新会话 / 另一 Agent 或人类**执行；**禁止**写稿同一会话自审终审。  
> **前置**：Step 10 SelfCheck **全 Pass** → audit-ready；送审包齐全（见 [`rules/selfcheck.md`](./rules/selfcheck.md)）。

---

## 何时使用

- [ ] ZH + EN md 已完成  
- [ ] Step 10 SelfCheck **全 Pass**（H0–H4 + 12 维）  
- [ ] Source Map + SERP Fit + Brief 可查阅  

**不适用**：

| 场景 | 改用 |
|------|------|
| 从选题到成稿 | 本 skill Step 01–10 |
| 已发稿健康检查 / 内链 / 局部刷新 | [`../audit-optimize/SKILL.md`](../audit-optimize/SKILL.md) |
| 成稿未过 Gate C | 回 Step 10 / [`rules/gate-rollback.md`](./rules/gate-rollback.md) |

---

## 触发语（复制到新会话）

```
按 Alignify create-article Step 11 终审：
- ZH：content/{channel}/zh/{slug}.md
- EN：content/{channel}/en/{slug}.md
- Primary keyword：{kw}
- SelfCheck：12/12 + H0–H4 Pass
- Brief Moat：{一行}
- 预检：audit-marketing-md-render.py --slug {slug} 全量 blog Pass 后才开始打分
```

---

## 终审流程

1. **只读**本文件 + [`rules/final-audit.md`](./rules/final-audit.md) — **不要**加载 Step 01–09  
2. 读 Brief（Moat、Answer Blocks）— [`rules/article-brief.md`](./rules/article-brief.md) 产出物  
3. 读 Source Map — [`rules/source-map-template.md`](./rules/source-map-template.md) 产出物  
4. 按 `final-audit.md`：自动化预检 → P0 → 十维 → 输出  

**判定**：

- P0 BLOCKED → **不得发布**  
- 总分 **≥80** + P0 Pass → **publish-ready** → 人类发布（复核 Step 08 日期）  
- 总分 **≥90** + Moat + Excellence + 零 P1 → **S 级标杆**  

Fail → [`rules/gate-rollback.md`](./rules/gate-rollback.md) 回退修复后重跑本 Step。

---

## 渐进加载

终审会话默认：**本文件 + `rules/final-audit.md`**。需要时最多再读 Brief / Source Map / SERP Fit 产出物。禁止一次性加载全部 `rules/`。

---

*11-final-audit · v1.0 · 2026-09-03*
