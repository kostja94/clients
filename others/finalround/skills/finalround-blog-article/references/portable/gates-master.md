# FinalRound Gates Master（Skill reference · portable）

> **Gate 总表速查。** Phase 0 / 5 加载。

---

## Gate 总表

| Gate | 位置 | 内容 | 阻断条件 |
|------|------|------|---------|
| **A** | Phase 0 | Investment Score + KEEP/MERGE/STOP + 信息增量 | MERGE / STOP / Investment <3.0 / 必问缺失 |
| **0R** | Phase 0R | Research 三角完整 + Synthesis | R2 未搜 / R3 未 Fetch / 无 Synthesis / P0 claim 不可验证 |
| **B** | Phase 2 | Slug 6 问全 Pass | 任一问 Fail |
| **C** | Phase 5 | H0–H4 + 12 维全 Pass | 任一 Fail → 回溯 |

## Hard Gates（Phase 5）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填 |
| **H1** | P0 Gate G1–G7 | 零触发 |
| **H1B** | FinalRound Gate F1–F6 | 零触发 |
| **H2** | Slug Gate B | 6 问全 Pass |
| **H3** | 字数硬门槛 | 达类型词数下限 |
| **H4** | FinalRound-Specific | 桌面应用叙事、无免费试用、旧词规避、Stealth 措辞准确 |

## G1–G7 速查

| # | 阻断条件 |
|---|---------|
| G1 | 事实错误 |
| G2 | 死链 |
| G3 | 无来源数字 |
| G4 | 竞品状态错误 |
| G5 | 产品能力夸大 |
| G6 | 内链指向未上线页面 |
| G7 | 品牌风险 / 贬低竞品 |

## F1–F6 速查（FinalRound 特有）

| # | 阻断条件 |
|---|---------|
| F1 | 定价违规（无免费试用；禁 free trial 类文案） |
| F2 | 旧产品形态词汇（Mock/Career Coach/Coding/Phone 独立产品；Scan Code/Listen Check 等旧词） |
| F3 | 桌面应用叙事（实时功能在桌面端，非网站） |
| F4 | 内部决策泄漏（SEO implication 等内部语言） |
| F5 | Stealth 措辞（不把 undetectable 当首要卖点） |
| F6 | 转化内链（/download /subscription /getting-started /try /special-discount 不入正文；按钮承载） |

## 回溯表（§3.G）

| Gate / 结果 | 回退至 |
|-------------|--------|
| Gate A → STOP/MERGE | 流程结束或改选题 |
| Gate 0R ❌ | Phase 0R |
| Gate 3.5 ❌ | Phase 3 |
| Gate B ❌ | Phase 2 |
| Gate C 写作/事实 | Phase 4 |
| Gate C 结构 | Phase 3 |
| Gate C Slug/Meta | Phase 2 |

---

*gates-master · portable · 可跨项目复用（F 系为 FinalRound 定制）*
