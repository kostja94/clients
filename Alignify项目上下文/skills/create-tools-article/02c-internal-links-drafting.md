# Step 2c — 内链初稿（创建阶段必做）

> **编辑层规范**：[alignify-internal-links.md §1](../../content/alignify-internal-links.md#part-1-编辑层单篇怎么改best-practice)  
> **审计规则**：[alignify-internal-links.md §3.1.5](../../content/alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)  
> **存量优化**：Skill `optimize-tools-internal-links`  
> **验收脚本**：部署仓 `verify-content-md.py`；JSON 页另跑 `audit:internal-links`

创建 JSON 时**同步规划内链**，不要写完正文再补链——Hub 页与 Spoke 页写法不同，事后 patch 成本高。

---

## 一、创建阶段 vs 优化阶段

| 阶段 | Skill | 动作 |
|------|-------|------|
| **新文创建** | `create-tools-article`（本节） | 写 JSON 时按区块配额分配；Step 5 跑 audit |
| **存量修复** | `optimize-tools-internal-links` | 审计 → patch → 附录 C → 复验 |

---

## 二、硬性规则速查（R1–R7 + R-TLDR）

| 规则 | 要求 | 严重度 | 创建时怎么做 |
|------|------|--------|-------------|
| **R-TLDR-1** | TLDR 块（intro + items）≤ **2** 个不同 slug | high | **默认 0–1 条**；Hub 页 TLDR **禁止**枚举 3+ 子品类链 |
| **R-TLDR-2** | 相邻两链间距 ≥ **40** 字符（中英文均计） | high | 只放 1 条链，或链与链之间写完整从句 |
| **R-TLDR-3** | TLDR 中的 slug **不得**再出现在「什么是」/ `section` / `html` | high | TLDR 链下沉到「什么是」第二段起 |
| **R1** | 全文 distinct 站内链 ≥ **5** | high | Hub 在「什么是」+ useCases 凑够；Spoke 用邻居表 |
| **R2** | 单屏（400 词 / 250 字）≤ **3** 链 | medium | 长枚举改纯文本，链分散到 useCases / howToChoose |
| **R4** | 同一目标 slug **全文仅 1 次** `<a>` | high | 首次出现保留链，后续改纯文本 |
| **R7** | FAQ ≤ **3** distinct slug，与正文去重；单答 ≤2 链 | high | FAQ 只放正文未链过的邻居 |
| **R-LINK-ONLY** | 存量修复 **只改 `<a>`** | 阻断 | 创建阶段不适用；优化见 `optimize-tools-internal-links` |

---

## 二b、R-LINK-ONLY（存量修复必读）

优化内链时 **禁止改非链接正文**。去 HTML 后字数应与 baseline 一致（R1 新增链除外最多 +1 句）。

| 场景 | 做法 |
|------|------|
| R4 重复 slug | 保留首次 `<a>`，其余 **unwrap**（锚文本留纯文本） |
| 「Related tools include…」 | **保留句子**；重复 slug 改纯文本，不删段 |
| R1 补邻居 | 在现有句外包链，或段末 **加 1 句**，不替换 useCases |
| FAQ/结论 | 不得从 700 字缩到 150 字 |

验收：`npm run audit:text-regression` + `npm run audit:internal-links`。

---

## 三、Hub 页 vs Spoke 页（Territory map）

### Hub 页（如 `voice`、`image`、`llm`）

**读者需求**：知道版图，再点进专页。

| 区块 | 内链策略 |
|------|---------|
| **TLDR intro** | **0 链**（纯文本列子品类）或 **1 链**（指向最核心 spoke） |
| **TLDR items** | 无链 |
| **什么是 · 第 2 段** | 首次链向各 spoke（1 条/ slug，可 2–4 链，注意 R2 密度） |
| **什么是 · 边界段** | 相邻品类（accent-conversion、video-translator 等） |
| **howItWorks / BestTools 分类卡** | 避免重复已链 slug；卡内描述用纯文本指专页 |
| **结论** | 不重复 TTS/STT 等已在正文链过的 slug；可保留 `/tools` 目录链 |

**反模式（禁止）**：

```
TLDR: TTS + STT + music-generator 三链相邻  ❌
什么是: 再链一遍 TTS/STT/music           ❌（若 TLDR 已链则 R-TLDR-3；若未链则 architecture 又链 → R4）
结论: 再链 TTS/STT/audio-translator      ❌ R4
```

**正例**：`content/tools/en/memory.json` — TLDR 仅 1 链到 `agent-memory`；consumer vs agent 边界在「什么是」展开。

### Spoke 页（如 `text-to-speech`、`speech-to-text`）

| 区块 | 内链策略 |
|------|---------|
| **TLDR intro** | **0–1 链**，指向最易混淆的邻居（如 TTS 页链 `voice-cloning` **或**纯文本写「见声音克隆专页」） |
| **什么是** | 工作流上下游 1–2 链，与 TLDR **去重** |
| **useCases** | 每场景 0–1 链 |
| **howToChoose** | 选型相关 1–2 链 |
| **FAQ** | 正文未覆盖的邻居，≤3 slug |

**反模式**：TLDR 写 `Related: note-taker, audio-translator` 两链相邻（间距 <40）❌

---

## 四、按区块写入顺序（推荐）

写 JSON 时按此顺序决策，避免 R4/R-TLDR-3 冲突：

```
1. 读附录 B / keywords「相邻 Tools」→ 列候选 5–8 slug
2. TLDR：0–1 链（或 0 链 + 纯文本）
3. 什么是 §2：放 Hub 辐条或 Spoke 主邻居（首次 <a>）
4. useCases / howToChoose：放剩余邻居
5. FAQ：仅放正文未出现的 slug（≤3）
6. 全文搜索 href=：同一 slug 出现 >1 次 → 保留最早区块，其余改纯文本
7. npm run audit:internal-links
```

---

## 五、锚文本（创建时即遵守）

### 5.1 硬底线

- 覆盖目标页核心语义（禁孤立「TTS」链向 `text-to-speech` — 用 `text-to-speech tools` 或中文「文字转语音工具」）
- 同页不同目标锚文本不雷同
- 禁「点击这里 / Learn more」

### 5.2 融入语境（硬底线——非"建议"）

**链接出现的唯一理由是被链目标出现在解释性内容中**，而非为了塞一条内链而额外插入一个"如果你需要X"的指路句。核心原则：

> **删掉这个带链接的句子，文章的解释链会被打断吗？**  
> 会 → 正确融入。不会 → 这条链接是硬插入的，删除重写。

**禁止的插入句式**（下面任何一种都是硬插入）：

| 禁止模式 | 示例 |
|----------|------|
| "相邻品类：X。" | `相邻品类：<a>AI 图片生成</a>。` |
| "若需要X，参见Y。" | `若需要从零生成场景，参见 <a>图片生成工具</a>。` |
| "参考 / 详见 Y。" | `详见 <a>Image Editor</a> 专页。` |
| "Related to X." | `Related to <a>image generators</a>.` |
| "See also X." | `See also <a>Image Editor</a>.` |
| "与 X 一并评估。" | `选型时常与 <a>Search Api</a> 一并评估。` |

**正确做法**：链接工具名必须出现在对工作流/原理的**解释**中，而不是一个**导航指令**里。正确的例子是将被链工具嵌入到对当前工具的流程解释中：

| 禁止（插入的指路句） | 正确（自然融入的解释句） |
|---|---|
| `相邻品类：AI 图片生成。` | `生成式铺底方案通常先在 AI 图片生成工具里按 prompt 出创意底图，再进换底工具做抠图合成。` |
| `需要精修可搭配 Image Editor。` | `换底后边缘溢色与锯齿需要在 AI 图像编辑里做局部精修才算交付级成片。` |
| `选型时常与 Search Api 一并评估。` | （如果确实不相关，就不应该放这条内链） |

### 5.3 自检步骤（提交前对每条 `<a>` 逐句执行）

1. 把整句（含 `<a>`）从段落中**完全删掉**
2. 重读段落——是否依然完整？如果依然完整，则链接是硬插入的
3. 如果链接通不过测试，改写为含链解释句，而非加一句导航

---

## 六、Blog Tools 文（`/blog/{slug}`）

- href 可为 `/tools/` 或 `/blog/`（如 `agent-memory` ↔ `memory`）
- 规则相同；审计加 `--source blog`
- 标杆：`content/blog/en/web-fetch.json`、`content/blog/en/agent-sandbox.json`

---

## 七、Step 2c 完成检查

- [ ] TLDR distinct slug ≤2（建议 ≤1）
- [ ] TLDR 与「什么是」无 slug 交集
- [ ] 全文每个 slug 仅 1 个 `<a>`
- [ ] distinct ≥5（稀疏页在 useCases 补邻居）
- [ ] FAQ slug 与正文无交集且 ≤3
- [ ] `npm run audit:internal-links` 对该 slug 零 high
- [ ] （存量）`npm run audit:text-regression` 无字段/文件缩水

---

## 八、常见错误 → 修复

| 症状 | 修复 |
|------|------|
| Hub TLDR 枚举 3+ 子品类 | TLDR 改纯文本；链移到「什么是」 |
| R-TLDR-2 相邻 | 删 TLDR 一条，或移到 section |
| R-TLDR-3 TLDR∩section | 删 TLDR 或 section 中重复 slug 的 `<a>` |
| R4 重复 | 保留首次出现区块的链，其余改纯文本 |
| R7 FAQ 与正文重叠 | FAQ 改纯文本或换未链过的邻居 |
| R1 <5 | useCases / howToChoose 补附录 B 邻居 |

详见 [`references/common-errors.md`](./references/common-errors.md) E9 及 `optimize-tools-internal-links/03-per-page-workflow.md`。

---

*02c-internal-links-drafting · v1.0 · 2026-06-24*
