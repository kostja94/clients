## §XA — 跨文章审计（Phase 5.5）

> Phase 5.5 加载 · 同批 ≥2 篇时必执行
>
> **定位**: 单篇 SelfCheck 有一个结构性盲区——它只检查一篇文章内部是否自洽，不检查多篇文章之间是否自洽。以下问题只能在跨篇审计中发现：事实矛盾、段落级重复、叙事模式雷同、hub-spoke 链接断裂、关键词 cannibalization。
>
> 单篇 SelfCheck 保证「每篇都是好文章」。跨篇审计保证「好文章放在一起不会互相伤害」。

---

### 1. 审计流程

```
同批所有文章单篇 SelfCheck 通过
  │
  ├── CA1 叙事模式雷同检测
  ├── CA2 互链双向完整性
  ├── CA3 产品描述跨篇重复率
  ├── CA4 Intro 模板化检测
  ├── CA5 Conclusion 模板化检测
  ├── CA6 核心概念跨篇重复
  ├── CA7 事实矛盾检测
  ├── CA8 关键词 Cannibalization
  ├── CA9 跨篇表现形式雷同
  └── CA10 署名一致性
        │
        └── 任一项 ❌ → 修复后重跑 CA1–CA10 → 全部 ✅ 方可批量交付
```

---

### 2. CA1 — 叙事模式雷同检测

**问题**: 如果 3+ 篇文章共享相同的叙事弧（教育→中立→"but X changes everything"→Dubbing AI 答案），读者形成模式识别，整个 blog 可信度降低。

**检测方法**:
1. 提取每篇文章的叙事弧：开头（教育/问题陈述）→ 中部（中立概述/问题展开）→ 转折点（"but"/"however"/"this is where"）→ 产品作为答案
2. 标记每篇的转折点位置（前 30% / 30–60% / 60%+）
3. 如果 3+ 篇共享同一叙事弧 + 转折点位置相同 → ❌

**修复**: 每篇文章使用不同的叙事入口——一篇用场景问题、一篇用数据/趋势、一篇用反直觉观点、一篇用具体案例。

| 检查 | 标准 | 阈值 |
|------|------|:---:|
| 叙事弧结构 | 各篇叙事弧类型不同 | ≥3 篇相同 → ❌ |
| 转折点位置 | 各篇转折点分布在文章不同位置 | ≥3 篇同一区间 → ⚠️ |

---

### 3. CA2 — 互链双向完整性

**检测方法**:
1. 提取每篇文章中的所有 blog 正文内链和 Related 列表
2. 交叉检查：Article 1 → Article 2 的内链，Article 2 是否回链 Article 1？
3. Dubbing AI Hub-Spoke 硬性要求：`best-ai-voice-changer` ↔ `how-to-change-google-assistant-voice` ↔ `how-to-change-your-voice` ↔ `dubbing-ai-vs-voicemod` 必须两两双向互链（见 `content-graph.md` §4.6）

| 检查 | 标准 |
|------|------|
| 正文 blog 互链 | 双向（A→B 且 B→A） |
| Related 互指（正文） | 2026-08-11 起 frontmatter 不再含 `related`；Related 以正文互链为准 |
| Hub-Spoke 网络 | #01↔#02↔#03↔#04 四向互链 |

---

### 4. CA3 — 产品描述跨篇重复率

**问题**: 相同产品描述在不同文章中重复出现→连续阅读场景下退化为营销轰炸感。

**检测方法**:
1. 提取每篇文章的所有产品描述段落（提及 Dubbing AI 功能/数字/优势的段落）
2. 逐段对比措辞相似度
3. 计算重复率：有 ≥30% 的内容在另一篇中出现了几乎相同的措辞 → ❌

**修复**: 每篇文章的产品段落使用不同的切入角度和措辞：
- 第一篇用架构描述（"real-time audio processing pipeline"）
- 第二篇用工作流示例（"how to set up Dubbing AI for Discord"）
- 第三篇只提一行（"Dubbing AI handles the voice change at the driver level"）

---

### 5. CA4 — Intro 模板化检测

**检测方法**:
1. 提取每篇 intro（第一个 `##` 之前的所有段落）的句子功能序列：
   - 标记每句的功能类型：**定义句** / **比喻句** / **路标句**（"this article explains…"）/ **场景句** / **数据句** / **问题句**
2. 对比同批文章的功能序列
3. 三级分类：
   - **模板化确认** ❌：3+ 篇共享同一功能序列 + 功能句措辞高度相似
   - **疑似模板化** ⚠️：2 篇共享或 3+ 篇共享序列但措辞不同
   - **健康** ✅：每篇功能序列各不相同

**「删定义和路标句」测试**: 删掉 intro 中所有术语定义句和路标句（"This article explains/defines/covers…"），剩下的内容是否仍能唯一标识这篇文章？如果不能 → intro 模板化。

**修复**: 每篇用不同的入口类型——场景 / 数据 / 反讽 / 困境 / 新闻 / 问题——而非统一的三段式。

---

### 6. CA5 — Conclusion 模板化检测

**检测方法**:
1. 提取每篇 Conclusion 的收束模式：**概念定论** / **局限性** / **产品位置** / **预测** / **未解问题** / **反直觉洞察** / **具体警告**
2. 如果 3+ 篇 Conclusion 可互换首段而不产生语义冲突 → ❌

**健康标准**: 每篇 Conclusion 留给读者一个**不同的**认知动作——一篇做预测、一篇提未解决问题、一篇给反直觉洞察、一篇给具体警告。

**修复**: 每篇用不同的认知收束类型。

---

### 7. CA6 — 核心概念跨篇重复

**问题**: 同一概念在多篇文章中完整展开→非 canonical 篇越界。

**检测方法**: 对照 content-graph Hub-Spoke 结构，检查非 Hub 文章是否在 Hub 已覆盖的概念上做了 >2 段的完整展开。

**Dubbing AI Canonical Map**（以 `content-graph.md` §4.4 为准——此为唯一 Canonical Registry）:

| Concept | Canonical Article | 其他文章处理 |
|------|------|------|
| How to choose a voice changer | #01 `best-ai-voice-changer` | 1–2 句 + 内链 |
| Assistant vs Mic routing | #02 `how-to-change-google-assistant-voice` | 1 句 disambiguate + 内链 |
| Live vs File boundary | #03 `how-to-change-your-voice` | 1 句分流 + 内链 |
| Dubbing AI vs Voicemod | #04 `dubbing-ai-vs-voicemod` | 1 句 "For a head-to-head comparison, see…" + 内链 |
| Dubbing Box hardware | HardwareGuide (tracking #05) | 1 句 "Dubbing Box adds a hardware layer" + 内链 shop |

> **规则**: Agent 引用 Canonical 映射时，只允许引用 `content-graph.md` §4.4——禁止在 project-config、platform-routing、CA6 等文件各自维护。任一文件需引用 Hub-Spoke 时只写 `→ content-graph.md §4.4`。

---

### 8. CA7 — 事实矛盾检测

**检测方法**:
1. 提取同批所有文章中的可验证 claim（数字、门槛、政策、流程、产品状态）
2. 按主题分组（voice count、latency、pricing、platform support、sound count）
3. 逐 claim 对比措辞，判定矛盾等级

**矛盾等级**:

| 等级 | 定义 | 示例 | 处理 |
|:---:|------|------|------|
| **硬矛盾 P0** | 两个声明互斥，无法同时为真 | 文章 A: "500+ voices" vs 文章 B: "300+ voices"（同年同月） | 必修——统一为 canonical 口径 |
| **软不一致 P1** | 措辞不同导致读者理解偏差 | 文章 A: "sub-30ms latency" vs 文章 B: "under 30ms response time"——措辞不同但数字一致，问题在于 B 用了 "response time" 不是 "audio latency" | 统一术语 |
| **精度差异 P2** | 同一数字用不同精度表达 | 文章 A: "100,000+ sounds" vs 文章 B: "over 100k sound effects" | 统一精度 |

**Dubbing Canonical 口径**（所有文章必须对齐）:
- Voice count: **500+ character-style voices** (as of dubbingai.io, {month} {year})
- Sound count: **100,000+ meme/soundboard sounds** (同上)
- Latency: **marketed sub-30ms class**; verify on your rig
- CPU: **often cited low single-digit %**; verify on your rig
- Dubbing Box: **hardware bridge for console/mobile paths**; sold at shop.dubbingai.io
- Free tier: **free tier exists**; limits on /download-desktop

---

### 9. CA8 — 关键词 Cannibalization 审计

**检测方法**:
1. 提取同批所有文章的 primary keyword
2. 检查搜索意图重叠度：两个 primary keyword 搜 Google，top 5 结果重叠 >50% → cannibalization 风险
3. 如果两篇文章 targeting 高度重叠的搜索意图 → 一篇应合并到另一篇或重新分配关键词

| 重叠度 | 判定 | 动作 |
|:---:|------|------|
| >70% | 🔴 Cannibalization | MERGE 或重新分配 primary keyword |
| 40–70% | ⚠️ 关注 | 确保两篇的 H1/angle 有明显差异 |
| <40% | ✅ 安全 | — |

---

### 10. CA9 — 跨篇表现形式雷同

**检测方法**:
1. 检查 3+ 篇是否共享相同的段落节奏模式（如每篇都是 "短-列表-短-列表-短"）
2. 检查各篇的列表占比是否都接近类型上限

**修复**: 调整至少 1 篇的表现形式——加 2–3 个长论证段落、减少列表、增加表格+分析。

---

### 11. CA10 — 署名/分类一致性

| 检查 | 标准 |
|------|------|
| 署名一致 | 同系列使用相同署名策略（均为 Kostja） |
| category 准确 | Track C frontmatter `category` 匹配 manifest 五类 |
| Research 标签 | 不将 opinion piece 标为 Research |

---

### 12. 审计输出格式

```markdown
## Cross-Article Audit — {batch name}

| # | Check | Status | Detail |
|---|-------|:---:|------|
| CA1 | Narrative pattern | {✅/⚠️/❌} | {shared arcs / all unique} |
| CA2 | Bidirectional links | {✅/❌} | {missing backlinks} |
| CA3 | Product description repeat | {✅/❌} | {repeat rate %} |
| CA4 | Intro templating | {✅/⚠️/❌} | {shared function sequences} |
| CA5 | Conclusion templating | {✅/⚠️/❌} | {shared closure patterns} |
| CA6 | Core concept duplication | {✅/❌} | {non-canonical expansions} |
| CA7 | Fact contradictions | {✅/❌} | {hard/soft/precision issues} |
| CA8 | Keyword cannibalization | {✅/⚠️/❌} | {overlap pairs} |
| CA9 | Presentation pattern sameness | {✅/⚠️/❌} | {shared rhythm patterns} |
| CA10 | Author/category consistency | {✅/❌} | {inconsistencies} |

**Verdict**: {ALL CLEAR / NEEDS FIX — {list failed checks}}
```

---

### 13. 修复后重审

任一项 ❌ → 修复 → 重跑 CA1–CA10 → 全部 ✅ 方可交付。Cross-Article Audit 在 Phase 6 Delivery 之前完成。
