## §RA — 已发布稿回溯审计（Retro Audit）

> **通用流程**：`references/portable/retro-audit.md`（R1–R14）。本文档仅补充 Dubbing AI 项目特有检查项与 #01–#04 预览。

---

### 0. 通用流程

```
请按 references/portable/retro-audit.md 对 slug {slug} 做合规扫描，只输出 diff 清单，不改文。
项目配置：dubbingai.io · Pillar: best-ai-voice-changer
```

加载 `content-graph.md` §4.6、`proof-gate.md`、`cross-article-audit.md` 作 R1/R8/R3 补充。

---

### 1. Dubbing 特有 Retro 项（叠加 R1–R14）

| # | 检查项 | 对比标准 |
|---|------|------|
| **D-R1** | Track S Hub 4-Spoke 四向互链 | `content-graph.md` §4.6 |
| **D-R2** | 产品数字 as-of | `proof-gate.md` P1 |
| **D-R3** | Live vs File / Assistant vs Mic | `proof-gate.md` P2–P3 |
| **D-R4** | CMS category 与 Track C 8 维 | `selfcheck-track-c.md` |

---

### 2. 已知 Retro 缺口（#01–#04 预览）

| 稿 | 可能 Fail | 修复优先级 |
|----|-----------|:---:|
| #01 hub | R1 未链 #04 | P1 |
| #02 IntentSplit | R1 未回链 #04（可选） | P2 |
| #03 HowTo | R4 Fragmentation 未实测 | P1 |
| #04 Alternative | R1 正文未链 #02 · R8 单向（2026-08-11 起 related 不入 frontmatter，以正文互链为准） | P1 |

---

*retro-audit · v1.4 · 2026-06-19 · base: references/portable/retro-audit.md*
