# Alignify 站内内链规范（唯一真相源）

> **位置（2026-08-26）**：`skills/create-article/rules/internal-links.md`  
> **站点**：[alignify.co](https://alignify.co)  
> **部署仓正文**：`alignify-by-kostja/content/**/*.md`（Markdown + frontmatter + block 标记）  
> **Last updated**: 2026-08-27  
> **说明**：Alignify 所有**站内内链**与**站外外链**规则（含 Marketing M1–M11、FAQ、R1–R7、UTM、Nofollow）、编辑方法论、Tools/SEO 拓扑、邻居表与验收标准**仅在本文件维护**。存量优化**执行流程**见 [`optimize-internal-links/workflow.md`](../../optimize-internal-links/workflow.md)。

---

## 目录

1. [编辑层：单篇怎么改（Best Practice）](#part-1-编辑层单篇怎么改best-practice)
2. [全站内链规则（唯一性 / 相关性 / 密度 / FAQ）](#part-2-全站内链规则)
3. [Tools 类目：拓扑 / R1–R7 / 组件 / 维护](#part-3-tools-类目)
4. [SEO 频道内链](#part-4-seo-频道内链)
5. [Marketing 频道内链（M1–M11）](#part-45-marketing-频道内链)
6. [Insights / 其他频道](#part-5-insights--其他频道)
7. [创建与存量优化工作流](#part-6-创建与存量优化工作流)
8. [Markdown 正文格式与计数范围](#part-7-markdown-正文格式与计数范围)
9. [外链：UTM 与 Nofollow](#part-8-外链utm-与-nofollow)

### Step 07 阅读路径（create-article）

| articleType | 必读（除 Part 1–2 · Part 8 外） |
|-------------|----------------------------------|
| `best-ranking` · `best-ranking-legacy` | [Part 3](#part-3-tools-类目) |
| `marketing-strategy` | [Part 4.5](#part-45-marketing-频道内链) |
| `seo-guide` | [Part 4](#part-4-seo-频道内链) |
| `insights-analysis` | [Part 5](#part-5-insights--其他频道) |

Part 6–7 归属 [`optimize-internal-links`](../../optimize-internal-links/SKILL.md)，**非** create-article Step 07。

---

<a id="part-1-编辑层单篇怎么改best-practice"></a>

# Part 1 · 编辑层：单篇怎么改（Best Practice）

> **Last updated**: 2026-08-07  
> **实践来源**：Alignify tools/zh 批次优化（`video-generator`、`headless-browser`、`image-generator`、`headshot-generator`、`ide`、`productivity`、`text-generator` 等）

---


## 一、核心原则

**内链是正文的一部分，不是导航栏。**

好的内链应满足：

- **可点击意图（最高优先级）**：读者在该句是否自然想「继续搞清 X」——X 必须是目标页主题
- **相关**：读者在当前段落确实可能需要跳转
- **自然**：删掉链接后句子仍通顺，链接是语义的自然延伸
- **稀疏**：宁可少链、晚链，不在一段里堆清单

坏的信号（应优先清理）：

- 「相邻品类：…」
- 「如果你在探索 X，可能也会对 A、B、C 感兴趣」
- 「可参考 / 可对照 / 搭配 / 一并评估」+ 链接列表
- 结论段末尾的 Explore / 相关工具领域包括…
- 同目标 URL 在文中重复出现

**一句话口诀**：一段一两链，全文有节奏；链要进句子，不要进清单；边界写清楚，结论不摆摊。

---

## 二、数量与密度

| 维度 | 建议 |
|------|------|
| **单段 / 单逻辑块** | 1–2 个内链；超过 2 个通常应拆段或改纯文字 |
| **整篇 tools 长文** | 通常 **4–9** 个内链（视篇幅与任务需要）；**无硬性下限**；产品表、对比表、References 不计 |
| **TLDR** | **0–1** 个；优先无链，用 bullet 说明边界 |
| **结论** | **0–2** 个；承接上文未覆盖的相邻环节，不做「延伸阅读清单」 |
| **HowTo / 选型步骤** | 步骤正文尽量无链；链放在对应场景段 |
| **FAQ** | **允许**站内链；**计入正文**；同 URL **全文仅 1 次**（与 section、结论共享 R4） |

**密度自检**：若连续 3 段都有内链，或开篇 500 字内已有 4+ 链，通常过密。


---

## 三、分布：全文均匀，而非局部堆砌

内链应像「章节间的桥」，而非集中在：

- 开篇定义段
- TLDR
- 结论「感兴趣」段

**推荐节奏**（典型 tools 长文）：

```
核心要点     → 0–1（仅划界类，如「人类向浏览器 vs 无头浏览器」）
定义/边界    → 1（说明本文不做什么、与谁互补）
技术/原理    → 0–1（与架构强相关时）
产品/对比    → 0（工具表已足够）
应用场景     → 1–2（按场景自然引出下游工具）
选型/HowTo   → 0–1
结论         → 0–1（落地动作，如「导出到建站 / 监测 GEO」）
```

**反例**：在「什么是 X」一段里同时链到抓取、Web Fetch、LLM、工作流、IDE、API。

**正例**：定义段只链「抓取（渲染引擎）」；Agent 场景段再链「大语言模型」；结论再链「GEO」。

---

## 四、写法：链进句子，不链进清单

### 4.1 推荐模式

1. **边界说明**  
   > 虚构角色合成属于 [AI 图片生成] 范畴；成片后的精修则在图像编辑环节处理。

2. **流程下游**  
   > 电商白底图批量场景，生成后可交给 [AI 背景替换工具] 统一换底。

3. **能力分层**  
   > 若只需行级建议而不换 IDE，[AI 代码补全] 是更轻量的入口。

4. **纯文字指代（不链）**  
   > 节点编排与多类分流分别在「节点式 AI 视频画布」与「AI 视频工具」聚合页展开。  
   读者需要时可通过导航找到，不必每处都链。

### 4.2 避免模式

| 避免 | 改为 |
|------|------|
| 相邻品类：[A]、[B] | 删标签；在正文一句说明边界，最多 1 链 |
| 可搭配 A、B、C | 只保留与当前段落最强相关的 1 个 |
| 选型时常与 X 一并评估 | 删除；或改为单句流程描述 |
| 结论：可能也会对…感兴趣 | 改为 1 个具体下游场景 + 1 链 |
| 同一 URL 开篇 + 结论各链一次 | 保留一处，另一处改纯文字 |

### 4.3 自检（每条链接）

删掉带链接的整句话，段落解释链是否仍完整？

- **会** → 正确融入  
- **不会** → 硬插入，删链或重写句子

（与 Alignify 专册 §1.5.3 一致。）

---

## 五、何时链、何时不链

**应该链**：

- 读者读完本段后，**很可能**需要进入相邻专页继续决策
- 目标页与当前段落的 **输入/输出** 有明确上下游（生成 → 编辑 → 增强）
- 划界清晰（本文 scope vs 专页 scope）

**不应链**：

- 仅「品类相邻」但段落主题无关（如无头浏览器文里链工作流、IDE、API）
- 聚合页 / 目录页（除非在对比表前言一句带过）
- 已在同文链过 1 次的目标（去重，R4）
- SEO 指南、论文工具等 **跨频道** 链接堆在结论（最多 1 个且与结论强相关）


---

## 六、中文页锚文本

**ZH 页锚文本用中文**，专有名词 / 缩写保留英文并规范大小写：

| 保留英文 | 示例 |
|----------|------|
| API、GEO、LLM、CLI、IDE、OCR、MCP | `[GEO]`、`[大语言模型](/zh/tools/llm)` |
| 已建立品牌 / 产品名 | GitHub、ChatGPT（按站点惯例） |

**避免**：`[Headless Browser]`、`[Workflow]`、`[Cli]` 等英文 / 拼音锚文本。

批量规范化可用部署仓 `localize-anchors.py`；**手工改写时**仍要检查语义是否自然，不要只改锚文本不改上下文。

---

## 七、单篇 / 批量工作流

> **执行 SSOT**（审计命令、单页 loop、快照刷新）：[`optimize-internal-links/workflow.md`](../../optimize-internal-links/workflow.md)  
> 本节 Part 1 §一–§六 为**编辑原则**；不在此重复维护操作清单与脚本命令。

---

## 八、Before / After（抽象模板）

**Before（机械 + 过密）**

> 相邻品类：[A]、[B]。在内容创作场景中，可搭配 [C]；若需 D，可搭配 [E]。选型时常与 F 一并评估。如果你在探索 X，可能也会对 G、H、I 感兴趣。

**After（自然 + 稀疏）**

> 本文聚焦 X 的核心行为；[C] 负责 Y 环节，与生成互补而非替代。（中段用例）成稿若需 Z，可在 [G] 环节处理。（结论）落地时把产出接到 [H] 等对外渠道。

---

## 九、与 SEO / 站点边界

- **FAQ 答案**：`faq-data.json` 及正文 inline FAQ **允许**站内链；**计入正文**；同 URL 全文 **1 次**（见 [Part 2 §1.5](#15-faq-内链规则)）
- **References**：外链，不算内链优化范围
- **`childrenHtml` 表格 / 列表**：其中 `<a href>` **计入**密度；列表项里的链也要遵守 1–2 规则
- 内链目标优先 **同频道 tools 专页**；跨到 blog/seo 应极少且与段落主题一致

---

## 十、Definition of Done

一篇优化完成当且仅当：

- [ ] 无机械引导词残留
- [ ] 同 URL 不重复；无连续多段堆链
- [ ] 每处链接删除后句子仍可读
- [ ] ZH 页锚文本中文化 + 缩写规范
- [ ] `verify-content-md.py` 通过（Markdown 页）
- [ ] 渲染后页面内容与优化前一致（只改链与 surrounding copy，不改事实与产品结构）

---

## 十一、批量推进

见 [`optimize-internal-links/workflow.md`](../../optimize-internal-links/workflow.md) §1 baseline 与 [`reverse-links.md`](../../optimize-internal-links/reverse-links.md)。邻居表：本文附录 B。

---

---

<a id="part-2-全站内链规则"></a>

# Part 2 · 全站内链规则

## 一、内链规则

### 1.1 唯一性与分布

- **同一内链只出现一次**：同一个内链 URL 在整个页面中只能出现一次
- **不在同一 H2 中重复**：同一个内链不能在同一 H2 章节中出现多次
- **分布在不同章节**：内链应分布在不同的 H2 或 H3 章节中
- **「提高内链频率」的含义**：指增加**不同目标 URL**（不同 `/tools/{slug}` 或频道页）的出现次数，并让它们落在 TLDR、什么是、如何工作、场景、如何选择、结论等不同区块；**不是**在同一页内对同一 slug 重复加链。试点类目（如 Avatar、Background Changer）可在不违反本条的前提下，比「仅在什么是放 2 条」再多链向若干互补 spoke；细则见 [§3 Tools 内链均衡分布](#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)
- **优先位置**：放在最相关、最自然的章节中
- **场景匹配**：放在最能体现相关性的场景

### 1.2 内链放置

- **中文优先**：「什么是 XXX」章节
- **英文优先**：「What Are XXX」章节
- 参见 [`sections.md`](./sections.md) Part 3.1、Part 2.1

### 1.3 内链相关性原则

**内链目标必须与当前主题有强功能关联或工作流关联**，避免为凑数而强行链接。

| 关联类型 | 说明 | 示例 |
|----------|------|------|
| **功能互补** | 同一工作流中上下游工具 | 音乐生成 → 视频编辑（为视频配乐）、MV 生成 |
| **同质替代** | 解决同类问题的不同工具 | 变声器 ↔ 文字转语音 ↔ 声音克隆（均为人声处理） |
| **场景延伸** | 同一使用场景下的不同需求 | 视频制作：视频编辑 + 音乐生成 |

**避免**：仅因同属某大类而链接。例如音乐生成与文字转语音、声音克隆虽同属「音频」，但音乐是旋律创作、后两者是人声处理，功能边界不同，不宜作为内链目标。详见 [`sections.md`](./sections.md) Part 3.1 §内链相关性。

### 1.4 内链样式

- **正文内链**：`.link-internal` 或 `.blog-post-content a`（非外链）
- **样式**：`text-inherit font-medium underline underline-offset-2 decoration-foreground/30`，hover 加深下划线 `decoration-foreground/50`（由 `src/index.css` 全局控制）
- 参见 [`sections.md`](./sections.md) Part 3.2

### 1.5 FAQ 内链规则

**统一政策（2026-08-27）**：`faq-data.json` 答案及正文 inline FAQ **允许**站内 `<a href>` / Markdown 链。

| 规则 | 说明 |
|------|------|
| **计入正文** | FAQ 答案中的链与 TLDR、section、结论等**一并**计入密度（§1.6）与 R2 窗口 |
| **R4 全文 1 次** | 同一 URL 在全页（**含 FAQ**）仅出现 **1** 次；FAQ 与正文**共享**配额 |
| **点击意图** | 每条 FAQ 链仍须过 [Part 1 §四](#四写法链进句子不链进清单) 自检；禁止清单式堆链 |
| **写法** | 见 [`sections.md` Part 2.2](./sections.md#part-22-faq--常见问题) |

**TL;DR / HowTo 步骤**：仍建议无链或极少链（见 Part 1 §二）；Marketing [M4](#m4) 对 TL;DR / HowTo 无链，**FAQ 除外**。

### 1.6 正文内链密度（目标频次）

用于**新写与大改版**时控制可读性与主题相关内链的疏密；**不强制**短期内对存量全文批量回刷。本文 §3 / §4 中的**区块上限**（如 Tools TLDR ≤2 条不同 slug 等）**仍须同时满足**。

| 项目 | 规则 |
|------|------|
| **默认目标** | **正文**（**含 FAQ 答案**）中约 **每 1000 个英文单词** 配置 **约 3 条**指向 **不同路径** 的站内链（与 §1.1「同一 URL 全页仅一次」一致；每条链计 1 个 distinct 目标）。 |
| **合理区间** | **约 2～4 条/千词** 即视为合格；极短正文不必硬凑，超长正文避免明显高于 4 条/千词（资源索引类专题若另有专册说明可从其规定）。 |
| **「正文」范围** | **计入密度语境**：TLDR 引言与要点、「什么是 / What are」、How it works、应用场景、如何选择、结论、**FAQ 答案**、对比表前的 `introHtml` 等**连贯说明性**段落。 |
| **不计入** | BestTools 产品卡描述、References、纯表体文案、AlsoInterestedIn / Header / Footer 等全局组件。 |
| **中文稿** | 以汉字为主的正文，可近似 **每 350～450 汉字** 配 **约 1 条**站内链作等量参照（稀疏度与上表英文目标同档）；或以导出正文用工具统计后再换算。 |
| **专册** | SEO / Tools / Insights 等频道细节见本文 §3–§5；密度为正文层总控，与区块规则不冲突时一并执行。 |

---

<a id="part-3-tools-类目"></a>

# Part 3 · Tools 类目

> **站点**：[alignify.co](https://alignify.co) · **关联**：[§2 全站内链规则](#part-2-全站内链规则)（全站规则）· `alignify-keywords-tools.md`（关键词与邻居权威表）· `src/data/tools-pages-config.ts` · [§4 SEO 频道内链](#part-4-seo-频道内链)（SEO JSON）· 本文 Part 5（其余页面）

**用途**：**`content/tools/en|zh/*.{md,json}`**（Markdown 优先） 之间的推荐链接拓扑，及固定组件（AlsoInterestedIn 等）与正文内链；**产品外链质检**见 §五。

---

## 一、框架：SEO × 用户意图 × 链接拓扑

| 维度 | 目标 | Alignify Tools 落地 |
|------|------|---------------------|
| **SEO** | 减少孤儿页、主题相关锚文本、层级清晰 | `/tools` 聚合 + 导航；重要 spoke 有正文语义内链 + 相关推荐组件 |
| **用户** | 当前页搞清「是什么」后，自然进入「下一步工具」 | 以**整篇阅读顺序**分布内链（见 §1.5）；「什么是」可保留 1～2 个强相关链，**不必**与 TLDR 重复同一 slug；Tools JSON 的 FAQ 在遵守 §1.5 上限时可放**站内**链（见 §四） |

### 1.1 纵向：聚合 ↔ 详情（Hub / Spoke）

| 方向 | 典型意图 | 做法 |
|------|----------|------|
| **聚合 → 详情** | 从工具大全进入某一类目 | `/tools`（及 locale 的 `/zh/tools`）列出或随机推荐链向 `/tools/[slug]` |
| **详情 → 聚合** | 回到总览换类目 | 面包屑、站点导航；必要时文内「更多工具」指回 `/tools` |

### 1.2 横向：同类目互补（Peer / 工作流）

| 场景 | 做法 |
|------|------|
| **同一工作流上下游** | 如视频生成 → 视频编辑；换背景 → 图像编辑（邻居速查见 **附录 B**） |
| **易混类目分流** | 详见 **附录 B** 末「与 note-taker / notes-generator 的交叉说明」及 `alignify-keywords-tools.md` |

### 1.3 固定区块 vs 上下文内链

| 类型 | Alignify 中的体现 |
|------|-------------------|
| **固定区块** | `Header` / `Footer` / `BreadcrumbNav`、**AlsoInterestedIn**（四卡片，数据来自 `TOOLS_PAGES`） |
| **上下文内链** | `content/tools/*/*.md` 与 `content/blog/*/*.md` 中 TLDR intro、「什么是」、应用场景 / 如何选择 section、`section`/`html` 内的 `<a href="/tools/...">` 或 `<a href="/blog/...">` |

### 1.4 基础原则（与全站 section-links 对齐）

| 原则 | Tools 页执行要点 |
|------|------------------|
| **避免孤立页** | 新 slug 上线后应进入 `tools-pages-config`、被聚合或随机推荐命中，并在至少一处正文或邻居表中体现 |
| **锚文本** | 描述目标功能；忌「点击这里」；可与 keywords 表中的英文/中文短语对齐 |
| **同一 URL 单页仅出现一次** | 见 [section-links §1.1](./internal-links.md#11-唯一性与分布) |

### 1.5 Tools 内链均衡分布（阅读体验优先 · 锚文本规范 · 跨板块预留）

> **编辑层规范**（单篇 DoD、参考 4–9 条·**无硬性下限**、去机械句、批次 SOP）：通用知识库 本文 Part 1。本节为 **R1–R7 审计层**，与 15 号文档互补。

在遵守 **同一站内路径全文仅出现一次**（含 FAQ 答案 HTML）的前提下，以 **整篇阅读体验** 为唯一判断标准分配内链。不以百分比或条数硬指标约束——换用密度肉检 + 功能意图 + 锚文本质量三项判断。

#### 1.5.1 分布原则（替代百分比约束）

**密度原则**：读者连续滚动 2–3 屏（约 400–600 英文词 / 250–400 中文字）内，不应遇到超过 **3 条**站内 `<a>`。通过肉检判断，不依赖自动化计数。

**功能意图原则**：每个区块的链接服务于该区块的读者需求，不为凑分布而塞链：

| 区块 | 读者此时的需求 | 链接应做什么 |
|------|-------------|------------|
| **TL;DR** | 我要不要继续读 | 指一条「读完摘要后直接能用的下一步」（≤2 条不同 slug） |
| **什么是** | 这跟我已知的概念什么关系 | 区分/承接相关概念，1–2 条，与 TL;DR 去重 |
| **How It Works** | 技术上怎么办到的 | 链向依赖的基础技术工具或架构组件 |
| **Use Cases** | 我在什么场景用 | 每个场景 0–1 条，链向该场景会用到的其他工具 |
| **How to Choose** | 我该怎么选 | 链向辅助决策的工具（评估、对比、检索等），1–3 条 |
| **结论 / HTML** | 还有什么 | 收束类链接，1–2 条，不与中段重复 |
| **FAQ** | 追问 | **允许**站内链；**计入正文**；同 URL 全文 1 次（R4）；须有点击意图 |
| **BestTools** | — | 产品卡以外链为主，避免在描述里堆站内 Tools 链 |

执行判断标准：**「这个链接放在这里，读者真的需要此时点它吗？」如果不是，换位置；如果整个页面都找不到合适位置，就不放。**

#### 1.5.2 跨板块链接配额（预留）

当前阶段只做 tools↔tools 互链。未来 SEO、Marketing、Insights 等板块优化完毕后，会出现跨板块互链（如 `/tools/geo` ↔ `/seo/search-engine-optimization`）。为避免届时需要大规模返工，当前 tools↔tools 链接**不占满每页总量**：

| 页面当前实际内链数 | tools↔tools 使用 | 预留给跨板块 |
|-----------------|-----------------|-----------|
| 5–9 条（稀疏页） | 全部用于 tools | 0（等跨板块启动时再扩总量） |
| 10–15 条（正常页） | 7–11 条 | 3–4 个位置 |
| 16–20 条（丰富页） | 11–14 条 | 5–6 个位置 |

附录 C 各 slug 台账中标注当前已使用的 tools 内链数和预留位置数。

#### 1.5.3 锚文本规范

**三层要求**：

**① 一致性（底线）**：锚文本必须覆盖目标页面的核心主题语义。目标页是 image-generator，锚文本不能只写「图片工具」——需要体现「生成」语义。目标页是 geo，锚文本需要有「搜索引擎可见度/优化」的意味，不能只写一个缩写。

**② 变体自然度**：同一目标页在不同源页中应使用不同的锚文本变体。image-generator 在不同上下文中的变体示例：
- 「从文字生成图像」（在 text-to-image 页）
- 「用 AI 产出产品主图」（在 background-changer 页）
- 「图像生成引擎」（在 image-editor 页）
- 「AI 生图能力」（在 API 页）

这样对 SEO（Google 将不同锚文本视为独立语义信号）和 LLM 引用（语义丰富的锚文本帮助模型建立概念关系图）都有益。研究显示 11+ 种不同锚文本变体指向同一页面与 **13 倍** 的 SEO 访问量相关。

**③ 描述性（融入语境）**：锚文本应是自然语句的一部分，而非孤立标签。

核心原则：**链接出现的唯一理由是被链目标出现在解释性内容中**，而非为了塞一条内链而额外插入一个导航指令句。

**自检（对每条 `<a>` 逐句执行）**：删掉这个带链接的整句话，文章的解释链是否被打断？会 → 正确融入。不会 → 这条链接是硬插入的。

**禁止的插入句式**：

| 禁止模式 | 示例 |
|----------|------|
| "相邻品类：X。" | `相邻品类：<a>AI 图片生成</a>。` |
| "若需要X，参见Y。" | `若需要从零生成场景，参见 <a>图片生成工具</a>。` |
| "参考 / 详见 Y。" | `详见 <a>Image Editor</a> 专页。` |
| "Related to X." | `Related to <a>image generators</a>.` |
| "See also X." | `See also <a>Image Editor</a>.` |
| "与 X 一并评估。" | `选型时常与 <a>Search Api</a> 一并评估。` |

**正确 vs 错误对比**：

| 禁止（插入的指路句） | 正确（自然融入的解释句） |
|---|---|
| `AI 图片生成工具` / `相邻品类：X。` | `生成式铺底方案通常先在 AI 图片生成工具里按 prompt 出创意底图，再进换底工具做抠图合成。` |
| `AI 搜索引擎` | `测试时对比不同搜索引擎的检索覆盖` |
| `API 平台` | `选型前检查 API 平台的集成门槛` |
| `需要精修可搭配 Image Editor。` | `换底后边缘溢色与锯齿需要在 AI 图像编辑里做局部精修才算交付级成片。` |

**锚文本底线**：
- 每条锚文本 ≥1 个英文词（且 ≥2 字符）或 ≥2 个汉字；中文页面中锚文本可为英文产品名（如 `Avatar`、`GEO`、`API`），不强制要求中文字符数
- 同一页面内，指向不同目标页的链接，锚文本不应雷同
- 禁止通用锚文本：`点击这里`、`了解更多`、`Click here`、`Learn more` 等
- 同一目标页在同一页面内只出现一次（全文唯一，无例外）

**锚文本类型分布参考**（非硬性约束，用于自查）：

| 锚文本类型 | 大致占比 | 说明 |
|----------|---------|------|
| 精确描述（如 `AI 图像生成工具`） | 15–25% | 目标页的核心主题词 |
| 部分变体（如 `从文字生成图像`） | 30–40% | 包含部分关键词的自然变体 |
| 语义描述（如 `先用 AI 生成底图再换背景`） | 25–35% | 融入上下文的完整语义片段 |
| 品牌/其他 | 5–10% | 频道页链接等 |

#### 1.5.4 综合底线规则

1. **每页 distinct 站内链接**：通常 **4–9**（tools 长文）为参考区间；**无审计底线条数**——以点击意图、R4 唯一性、无机械指路为准（见 Part 1）
2. **单屏密度 ≤3 条**（连续 400 英文词 / 250 中文词内不堆链）
3. **每页 tools↔tools 当前实际使用 ≤ 总配额的 70%**（预留跨板块）
4. **同一目标页全文只出现一次**
5. **锚文本覆盖率**：覆盖目标页核心语义 + 自然融入上下文句子 + 与其他锚文本不雷同
6. **最小锚文本长度**：≥1 个英文词（且 ≥2 字符）或 ≥2 个汉字；中文页面中锚文本可为英文产品名，不强制中文字符数要求
7. **FAQ 内链**：Tools/Blog JSON 允许 FAQ 内放站内链（≤3 个不同 slug，与正文去重）；FAQ 内链与正文内链同等对待
8. **R-LINK-ONLY（内容保全）**：存量内链修复 **只允许改 `<a>` 标签**（增/删 `href`、保留锚文本为纯文本）。**禁止**整段替换 FAQ/结论、删非链接字段、用短句覆盖长段以满足 R1/R4。验收：改链前后去 HTML 后字段长度不得异常缩水（人工 spot-check）。

**R-LINK-ONLY 按违规类型的唯一合法操作**：

| 违规 | 合法操作 | 禁止 |
|------|----------|------|
| R4 同 slug 第 2+ 次 | 去掉后续 `<a>`，锚文本保留为纯文本 | 删整段「Related tools…」 |
| R-TLDR-3 TLDR∩section | 删重复 slug 的 `<a>`（TLDR 或 section 二选一） | 重写 TLDR intro |
| R1 机械指路链 / 同段堆链 | 改为任务句内链；每段 ≤1；无 distinct 下限 | 为凑条数在 useCases 硬插邻居 |
| R7 FAQ 与正文重复 | FAQ 里重复 slug 改纯文本 | 把 FAQ 答案缩成 2 句 |
| 结论内链枚举 | 保留叙述句；已链 slug 在结论改纯文本；可保留 1 条 `/tools` 目录链 | 换成一句「Next steps: …」 |

#### 1.5.5 已知局限与后续改进方向

以下项目当前未纳入规则体系，但行业最佳实践建议未来逐步引入（按优先级排列）：

| 改进项 | 说明 | 优先级 |
|-------|------|--------|
| **锚文本多样性追踪** | 当前只追踪 distinct slug，未追踪同一目标页在不同源页中的锚文本变体数量。研究显示 11+ 变体与 13x SEO 访问相关 | 高 |
| **双向链接检测** | 当页面 A 链向页面 B 时，自动检查 B 是否应回链 A（当前附录 B 只做单向邻居） | 高 |
| **孤页自动发现** | 每月自动扫描全站，标记零入链的页面（当前依赖人工发现） | 中 |
| **爬取深度度量** | 确保核心页面从首页起 ≤3 次点击可达（当前依赖站点结构 + Header 导航，未量化） | 中 |
| **旧内容反向链接** | 新页面发布时，自动识别 2–5 个旧高权页面应添加回链（当前无此机制） | 中 |
| **链接权益流向** | 分析 PageRank 在内链图中的分布，确保高价值页面获得足够链接权重 | 低 |
| **移动端可点性** | 连续 `<a>` 标签间距 ≥8px 防止误触（当前不做 CSS 级约束） | 低 |
| **AI 爬虫可达性** | 显式允许 `ClaudeBot`、`PerplexityBot`、`OAI-SearchBot` 在 robots.txt 与 AI 引用率直接相关（当前需确认） | 低 |

---

试点落地顺序与 **附录 B** 中已列 slug 一致：P0 → P1 → P2 → P3（长尾页以 R4 / 机械链清理为主，不凑条数）。

维护：**href → 首次出现区块 → 锚文本** 见 **附录 C**。

#### 1.5.7 全库优化排期（P0→P3）

Hub 合计 **106** slug（`tools-pages-config` 100 + Blog 中 `category` 映射到 tools hub 的 6 篇，无重叠）。

| 波次 | 范围 | slug 列表 |
|------|------|-----------|
| **Wave 0** | Blog Tools | `agent-memory`、`agent-sandbox`（模板）、`ai-training-data`、`data-engineering-agent`、`inference-infrastructure`、`medical-scribe`、`web-fetch` |
| **P0** | Agent 执行链 | `headless-browser`、`agent-for-desktop`、`agent-skills`、`browser`、`cli`、`workflow`、`openclaw-alternatives`、`coding` |
| **P1** | 高流量 ~15 | `search-engine`、`web-search-api`、`web-scraping`、`llm`、`authentication`、`documentation`、`code-review`、`character-chat`、`linkedin`、`avatar`、`world-model`、`evaluation`、`api`、`vibe-coding`、`knowledge-base` |
| **P2** | 中流量 ~30 | 附录 B 已列其余 slug + territory-map B 档（如 `note-taker`、`web-scraping` 邻居簇、`image-generator` 媒体链等） |
| **P3** | 长尾 | 未列入 P0–P2 的剩余 `/tools` slug；清理 R4 / 机械指路链 |

执行 Skill：[`optimize-internal-links`](../../optimize-internal-links/SKILL.md)；批次脚本：`batch-internal-links-wave.py`（`wave0_blog` / `p0` / `p1` / `p2` / `p3`）。

#### 1.5.6 审计脚本与执行

`scripts/` 目录下提供三个审计脚本，对应上述规则的自动化检查：

| 脚本 | 检查范围 | 对应规则 |
|------|---------|---------|
| `audit-tools-internal-links.py` | 单页内链分布、密度、重复、锚文本长度、FAQ 合规 | R1–R7（§1.5.4 全部） |
| `audit-anchor-text-diversity.py` | 跨页面锚文本变体数量、通用锚文本检测 | R5、R6 + §1.5.3 |
| `audit-cross-page-links.py` | 孤页检测、双向链接缺失、PageRank、点击深度 | 跨页面关系 |

**用法示例**：

```bash
# 全量审计 + 仅显示违规（日常使用）
python3 scripts/audit/audit-tools-internal-links.py --locale both --source both --violations-only

# 单页详细审计
python3 scripts/audit-tools-internal-links.py --slug headless-browser --locale en

# 锚文本多样性分析
python3 scripts/audit-anchor-text-diversity.py --locale both

# 孤页 + 双向链接检查
python3 scripts/audit-cross-page-links.py --locale both

# JSON 输出（供 CI 集成）
python3 scripts/audit-tools-internal-links.py --locale both --json > audit-result.json
```

**CI 集成建议**：在每次 `content/tools/` 或 `content/blog/` 正文变更时，CI 运行 `audit-tools-internal-links.py --violations-only --json`；**R4/R6/R7**（severity=high）违规应阻断合并；distinct 计数与 R1 仅作观察，**不**作发布阻断。
---

## 二、URL 模式（Tools 与 Tools 型 Blog）

| 语言 | Tools 页 | Blog 页（tools hub 归属） |
|------|----------|-----------------------------------|
| 英文 | `/tools/[slug]` | `/blog/[slug]` |
| 中文 | `/zh/tools/[slug]` | `/zh/blog/[slug]` |

**hreflang** 与全站规则见 `alignify-keywords.md`。Blog 型 Tools 文（如 `agent-sandbox`、`inference-infrastructure`）内链可混用 `/tools/` 与 `/blog/`，仍遵守全文 href 唯一。

---

## 三、全站组件与 Tools 相关的内链位

汇总自 [section-links §三](./internal-links.md#三全站链接使用场景汇总)；Tools 编辑需重点核对：

| 组件 | 说明 |
|------|------|
| **AlsoInterestedIn** | 四卡片内链；slug 来自 `TOOLS_PAGES`，锚文本为 `keywordZh` / `keywordEn` |
| **BestTools** | 产品 `linkUrl` 多为外链，按规范加 UTM/rel；**内链**产品较少见 |
| **BreadcrumbNav** | 回上级频道 |
| **JSON 内 `<a>`** | 站内相对路径；**FAQ 答案**允许站内链，见 [§1.5](#15-faq-内链规则) |

---

## 四、正文与 JSON：内链放哪里

| 位置 | 规则 |
|------|------|
| **什么是 · 第二段** | **建议**含 **1～2 个**强相关内链，且与 TLDR 去重；全页仍以唯一性为先；见 [`sections.md`](./sections.md) Part 3.1 |
| **邻居选题** | 优先 **附录 B** 与 keywords 表；不足时自拟并后续补 keywords |
| **结论** | 可含内链（见 [`sections.md`](./sections.md) Part 4.4）；仍遵守唯一性 |
| **FAQ** | **允许**站内链；**计入正文**；同 URL 全文 1 次（见 [§1.5](#15-faq-内链规则)） |

**嵌入示例（音乐生成工作流）** 见本文 **附录 A**（与 [`templates.md`](./templates.md) Part 2 内链示例一致）。

---

## 五、产品链接验证与优化（Tools 页面）

以下内容自 [section-links.md §四](./internal-links.md) **迁入**，今后 **Tools 产品链接质检**以本节为准；`section-links` 仅保留指向本目录的索引。

### 5.1 验证流程

- **必须验证**：创建或更新页面时，验证所有产品外部链接的真实性和有效性
- **验证方法**：直接访问链接、检查指向正确产品页面、确认格式（含 `https://`）
- **验证时机**：创建/更新页面时；建议每 3 个月定期检查

### 5.2 无效链接处理

- **移除无效链接**：无法访问或指向错误时，移除该产品介绍
- **移除范围**：产品章节、对比表格、FAQ 引用；更新产品数量
- **重新编号**：确保序号连续（1, 2, 3...）
- **同步更新**：中英文页面同步

### 5.3 产品文案检查

- 产品名称、版本号、公司名称正确
- 功能描述、特点说明准确
- 产品定位和适用场景准确

---

## 六、维护与抽检

| 项 | 说明 |
|----|------|
| **新 Tools slug** | 更新 `tools-pages-config`、keywords 文档、（可选）附录 B 速查；检查 `/tools` 可达性；面包屑 `/tools/{slug}` 标签由 `TOOLS_PAGES` 自动生成（见 [technical-breadcrumb-nav](../../ops/seo-fundamentals.md)），**无需**改 `BreadcrumbNav` 手写映射 |
| **改邻居** | 同步 `alignify-keywords-tools.md` 与 **附录 B** |
| **单页** | 核对 section-links 检查清单 + 本节 5.1–5.3 |

---

## 附录 A：什么是 · 第二段内链示例（音乐生成）

```tsx
<p>
  在视频与音乐创作流程中，AI 音乐生成可为<Link href="/zh/tools/video-editor"><strong>AI 视频编辑工具</strong></Link>提供背景音乐，也可与<Link href="/zh/tools/music-video-generator"><strong>AI MV 生成工具</strong></Link>配合，从音乐到视觉一体化制作。
</p>
```

---

## 附录 B：相邻 Tools 速查（邻居矩阵）

> **权威数据源**：各 slug 的完整意图表与「相邻 Tools」原文见 `alignify-keywords-tools.md` 对应 `#*-tools` 锚点。  
> **用途**：写「什么是」第二段、结论、或 `content/tools/*/*.md` 中 `<a href="/zh/tools/...">` 时快速对齐已约定邻居；**未列出的 slug** 由编辑按 [section-links §1.3](./internal-links.md#13-内链相关性原则) 自拟，并可在 keywords 文档中补行。

---

## 已配置「相邻 Tools」的 slug

| slug | 英文路径示例 | 相邻内链（摘要） |
|------|----------------|------------------|
| `family-assistant` | `/tools/family-assistant` | note taker、chatbot（儿童边界见知识块） |
| `interview-assistant` | `/tools/interview-assistant` | recruiting、text generator、note taker |
| `note-taker` | `/tools/note-taker` | speech-to-text、text generator |
| `notes-generator` | `/tools/notes-generator` | note-taker、speech-to-text、text-generator |
| `vibe-coding` | `/tools/vibe-coding` | app builder、code completion |
| `code-review` | `/tools/code-review` | vibe-coding、code-completion、coding、workflow、llm（正文与 FAQ 分布见附录 C §9） |
| `agent-skills` | `/tools/agent-skills` | cli、ide、vibe-coding、coding、workflow、directory、**agent-memory**（记忆层，Blog `/blog/agent-memory`）、**agent-sandbox**（执行隔离层，Blog `/blog/agent-sandbox`）、**multi-agent**（多 Agent 编排，Blog `/blog/multi-agent`）（附录 C §10） |
| `agent-for-desktop` | `/tools/agent-for-desktop` | browser、agent-skills、**agent-sandbox**、headless-browser、cli、coding、llm、workflow、**multi-agent**（团队多 Agent 见 Blog）、geo 等；FAQ：note-taker、code-review、website-builder（附录 C §16；正文与 FAQ href 全文唯一） |
| `agent-sandbox` | `/blog/agent-sandbox` | agent-skills、inference-infrastructure、agent-for-desktop、authentication、headless-browser；FAQ：cli、openclaw-alternatives、workflow（与正文去重）；Blog 路由见附录 C §blog-agent-sandbox |
| `openclaw-alternatives` | `/tools/openclaw-alternatives` | agent-skills、agent-for-desktop、**multi-agent**（Clawith 团队向，Blog `/blog/multi-agent`）、llm、coding、workflow、cli、productivity、chatbot、documentation、knowledge-base、api、directory；FAQ：note-taker、evaluation、browser（附录 C §17；TLDR ≤2、`agent-for-desktop` 仅 TLDR；正文与 FAQ 去重） |
| `browser` | `/tools/browser` | search engine、text generator |
| `avatar` | `/tools/avatar` | video-generator、video-editor、voice-cloning、image-generator（静态头像见 headshot） |
| `background-changer` | `/tools/background-changer` | image-editor、image-generator、headshot-generator、virtual-staging |
| `headshot-generator` | `/tools/headshot-generator` | image-editor、image-generator、background-changer |
| `legal` | `/tools/legal` | text-generator、productivity、notes-generator（材料笔记≠执业检索） |
| `linkedin` | `/tools/linkedin` | geo、headshot-generator、text-generator、lead-generation、b2b、recruiting；FAQ：interview-assistant、presentation-maker、productivity（附录 C §15；正文与 FAQ href 全文唯一） |
| `search-engine` | `/tools/search-engine` | knowledge-base、text-generator（工作流）；与专页 <code>web-search-api</code> 易混时，终端产品链 <code>search-engine</code>、程序化检索链 <code>web-search-api</code>，全文各 URL 仅出现一次 |
| `web-search-api` | `/tools/web-search-api` | search-engine（对话式产品）、llm、knowledge-base、api、geo、search-indexing；与 <code>search-engine</code> 成对互指；下游 fetch 链路见 <code>web-fetch</code>，见附录 C §7 |
| `web-fetch` | `/blog/web-fetch` | web-search-api（上游「找 URL」）、web-scraping（批量采集管道——别买错）、headless-browser（需交互时上浏览器）；与 search→fetch→browser 三层分工对齐；Blog 路由 `/blog/web-fetch`、`/zh/blog/web-fetch`，见附录 C §blog-web-fetch |
| `medical-scribe` | `/blog/medical-scribe` | healthcare（医疗 AI 全景——影像/CDS）、note-taker（会议记录≠环境文书）；Blog 路由 `/blog/medical-scribe`、`/zh/blog/medical-scribe`，见附录 C §blog-medical-scribe |
| `healthcare` | `/tools/healthcare` | knowledge-base、productivity；环境文书分流见 `medical-scribe` Blog；本页主线为放射影像 AI 与循证 CDS |
| `ai-training-data` | `/blog/ai-training-data` | evaluation（训后评测）、web-scraping（raw 抓取≠训练交付）、world-model（多模态/视频数据）、inference-infrastructure（推理部署）、llm（模型基准）；Blog 路由 `/blog/`，见附录 C §blog-ai-training-data |
| `multi-agent` | `/blog/multi-agent` | workflow（固定流程≠Agent 编排）、agent-for-desktop（单人本机）、openclaw-alternatives（OpenClaw 生态）、agent-skills（MCP/Skill）、agent-sandbox（执行隔离）、hr-assistant（HR 垂直≠编排层）；Blog 见附录 C §blog-multi-agent |
| `web-scraping` | `/tools/web-scraping` | web-search-api、web-fetch（AI 开发者向、轻量 URL→Markdown）、ai-training-data（curated 训练交付——别与 scrape 混买）、search-engine、`/seo/crawler`（入站治理）；llm、workflow、geo（附录 C §11；正文「什么是 / 典型场景」与 TLDR 去重 `web-search-api`） |
| `headless-browser` | `/tools/headless-browser` | web-scraping、web-fetch（无交互取内容时先看 fetch）、browser、web-search-api、llm、workflow、agent-skills、coding、ide、api、vibe-coding、knowledge-base、directory、cli、productivity、geo；FAQ：evaluation、code-review、website-builder（附录 C §13；TLDR ≤2 条 Tools 链，FAQ 与正文全文唯一） |
| `authentication` | `/tools/authentication` | workflow、evaluation、app-builder、knowledge-base、agent-skills、llm、browser、web-search-api、notes-generator、productivity、api、user-research、spreadsheet、chatbot、directory；hero：`documentation`；FAQ：note-taker、recruiting、speech-to-text（附录 C §14；正文与 FAQ href 全文唯一） |
| `documentation` | `/tools/documentation` | agent-skills、knowledge-base、vibe-coding、coding、api、workflow、web-search-api、geo、llm、ide、cli、code-completion、directory、app-builder、chatbot、website-builder、text-generator、productivity、user-research、browser、code-review；FAQ：note-taker、notes-generator、recruiting（附录 C §12） |
| `world-model` | `/tools/world-model` | text-to-video、image-to-video、video-generator（创作向）；正文落地另含 video-editor、3d、llm、search-engine、directory、image-generator、legal（见 JSON，遵守全文唯一） |
| `video` | `/tools/video` | video-generator、text-to-video、image-to-video、video-to-video、video-editor、video-clipping、video-effects、canvas-video、filmmaking、animation-generator、short-drama、music-video-generator（Hub 分流 + 内容分工见 [video.md](../../../knowledge/tools/video/video.md)） |
| `video-generator` | `/tools/video-generator` | video、text-to-video、image-to-video、video-to-video、canvas-video、filmmaking、animation-generator（生成层 SSOT；完整旗舰模型表仅此 slug） |
| `text-to-video` | `/tools/text-to-video` | video、video-generator、image-to-video、video-editor（输入=文本/文档；讲解视频专表在本 slug） |
| `image-to-video` | `/tools/image-to-video` | video、video-generator、text-to-video、video-to-video、filmmaking（输入=静态图；Motion Brush 深度在本 slug） |
| `video-to-video` | `/tools/video-to-video` | video-generator、video-effects、animation-generator、filmmaking（全片风格迁移；抠像见 video-effects） |
| `video-editor` | `/tools/video-editor` | video-generator、video-clipping、video-effects、filmmaking（时间线编辑；上游生成见 generator） |
| `video-clipping` | `/tools/video-clipping` | video-editor、video-generator（长→多片段 repurposing；非完整时间线） |
| `video-effects` | `/tools/video-effects` | video-editor、video-to-video、animation-generator（VFX/抠像；全片 anime 化见 V2V） |
| `filmmaking` | `/tools/filmmaking` | video-generator、text-to-video、image-to-video、video-editor、short-drama、animation-generator（电影全管线；短剧见 short-drama） |
| `animation-generator` | `/tools/animation-generator` | video-generator、short-drama、video-to-video、music-video-generator（动漫平台；通用 T2V 横评见 generator） |
| `short-drama` | `/tools/short-drama` | video-generator、animation-generator、filmmaking（竖屏多集+投流；底层模型见 generator） |
| `music-video-generator` | `/tools/music-video-generator` | music-generator、video-generator（排除通用 T2V；music-first MV） |
| `canvas-video` | `/tools/canvas-video` | video-generator、text-to-video、image-to-video、video-editor、workflow、filmmaking（节点画布编排） |
| `character-chat` | `/tools/character-chat` | chatbot、text、text-to-speech、llm、workflow、avatar、text-generator、headshot-generator、api、directory、notes-generator、productivity、evaluation、web-search-api、website-builder、geo；FAQ：`speech-to-text`、`recruiting`、`spreadsheet`（附录 C §18；正文与 FAQ href 全文唯一） |

**中文站**：路径前缀 `/zh/tools/{slug}`；锚文本以中文关键词为主，见 keywords 表右列。

---

## 与 note-taker / notes-generator 的交叉说明

- 会议 **note taker** 与 **notes-generator**（学习材料→笔记）勿混；keywords 中 note-taker 节下有专门提示链至 `notes-generator-tools`。

---

*修订时请同步更新 `alignify-keywords-tools.md`，并回写本表以保持速查一致。*

---


## 附录 C：试点 JSON 正文内链对照

> **用途**：记录已按 section-links §1.1、本文 §1.5 落地的 **JSON 正文内链**（`<a href="/tools/...">` / `<a href="/zh/tools/...">`），便于改稿时做 **href → 锚文本 → 区块** 核对。
> **锚文本列**：与 JSON 中 `<a>` 标签内对用户可见的文案一致（已去掉包裹用的 `<strong>` 等标签，仅保留可读字符串）。
> **数据源**：`content/tools/zh|en/*.md` 共 23 个试点 slug。
> **更新日期**：2026-05-20 — 由脚本从实际 JSON 文件自动扫描生成，替换此前手动维护的过时版本。
> **阅读阶段**：按 `blocks` 自上而下粗分；**非**精确字数占比，仅用于肉检篇首是否过密。

**不含**：页面 `pageUrl`、`AlsoInterestedIn` 四卡片、`BestTools` 产品外链。

**含**：Tools JSON **FAQ** 答案中的站内 `<a>`（须与正文 href 全文唯一）。

## 1. avatar

### 1.1 中文版 `content/tools/zh/avatar.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/lip-sync` | AI 对口型工具 | 什么是 | 开篇 |
| `/zh/tools/image-generator` | AI图片生成工具 | Avatar的两个含义 | 开篇 |
| `/zh/tools/headshot-generator` | AI头像生成工具 | Avatar的两个含义 | 开篇 |
| `/zh/tools/image` | AI图片工具 | Avatar的两个含义 | 开篇 |
| `/zh/tools/text-to-speech` | AI 文字转语音 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/voice-cloning` | AI 声音克隆 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/video-translator` | AI 视频翻译 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/workflow` | AI 工作流 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/video-editor` | AI 视频编辑工具 | 应用场景 | 中部 |
| `/zh/tools/video-generator` | AI 视频生成工具 | 应用场景 | 中部 |
| `/zh/tools/music-generator` | AI 音乐生成 | 应用场景 | 中部 |
| `/zh/tools/presentation-maker` | AI 演示文稿 | 应用场景 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 应用场景 | 中部 |
| `/zh/tools/character-chat` | 角色对话 | 应用场景 | 中部 |
| `/zh/tools/image-enhancer` | AI 图像增强 | 应用场景 | 中部 |
| `/zh/tools/api` | API 平台 | 如何选择 | 中部 |
| `/zh/tools/web-search-api` | AI 搜索 API | 如何选择 | 中部 |
| `/zh/tools/background-changer` | AI 换背景 | 结论 | 后部 |
| `/zh/tools/image-editor` | AI 图像编辑 | 结论 | 后部 |
| `/zh/tools/speech-to-text` | 语音识别转写 | FAQ | FAQ |
| `/zh/tools/note-taker` | 会议记录工具 | FAQ | FAQ |

**统计**：正文 **19** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **21** 条。

### 1.2 英文版 `content/tools/en/avatar.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/lip-sync` | AI lip sync tools | What Are | 开篇 |
| `/tools/image-generator` | AI image generators | What Are | 开篇 |
| `/tools/headshot-generator` | AI headshot generators | What Are | 开篇 |
| `/tools/image` | AI image tools | What Are | 开篇 |
| `/tools/video-translator` | AI video translators | How It Works · technologyBase | 中部 |
| `/tools/video-editor` | AI video editors | Use Cases | 中部 |
| `/tools/video-generator` | AI video generators | Use Cases | 中部 |
| `/tools/music-generator` | AI music generators | Use Cases | 中部 |
| `/tools/presentation-maker` | AI presentation makers | Use Cases | 中部 |
| `/tools/chatbot` | AI chatbots | Use Cases | 中部 |
| `/tools/character-chat` | character chat | Use Cases | 中部 |
| `/tools/image-enhancer` | AI image enhancers | Use Cases | 中部 |
| `/tools/api` | API platform | How to Choose | 中部 |
| `/tools/web-search-api` | AI search APIs | How to Choose | 中部 |
| `/tools/background-changer` | AI background changers | Conclusion | 后部 |
| `/tools/image-editor` | AI image editors | Conclusion | 后部 |
| `/tools/speech-to-text` | speech-to-text | FAQ | FAQ |
| `/tools/note-taker` | note taker | FAQ | FAQ |

**统计**：正文 **16** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **18** 条。

---

## 2. world-model

### 2.1 中文版 `content/tools/zh/world-model.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm` | 大语言模型 | 什么是 | 开篇 |
| `/zh/tools/text-to-video` | AI文生视频工具 | 什么是 | 开篇 |
| `/zh/tools/image-to-video` | AI图生视频工具 | 什么是 | 开篇 |
| `/zh/tools/video-to-video` | AI 视频转视频工具 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/video-generator` | AI视频创作工具 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/video-editor` | AI 视频编辑工具 | 应用场景 | 中部 |
| `/zh/tools/3d` | AI 3D 工具 | 应用场景 | 中部 |
| `/zh/tools/web-search-api` | AI 搜索 API | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 后部 |
| `/zh/tools/image-generator` | AI 图片生成工具 | 结论 | 后部 |
| `/zh/tools/video` | AI视频制作 | 结论 | 后部 |
| `/zh/tools/legal` | AI 法律工具 | FAQ | FAQ |

**统计**：正文 **11** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **12** 条。

### 2.2 英文版 `content/tools/en/world-model.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm` | large language models | What Are | 开篇 |
| `/tools/text-to-video` | text to video AI | What Are | 开篇 |
| `/tools/video` | AI video tools | How It Works · technologyBase | 前部 |
| `/tools/video-generator` | AI video generators | How It Works · technologyBase | 前部 |
| `/tools/video-editor` | AI video editors | Use Cases | 中部 |
| `/tools/3d` | AI 3D tools | Use Cases | 中部 |
| `/tools/web-search-api` | AI search APIs | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/image-generator` | AI image generators | Conclusion | 后部 |
| `/tools/legal` | AI legal tools | FAQ | FAQ |

**统计**：正文 **9** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **10** 条。

---

## 3. background-changer

### 3.1 中文版 `content/tools/zh/background-changer.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/image-editor` | AI图像编辑 | 什么是 | 开篇 |
| `/zh/tools/api` | API 平台 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/avatar` | AI 数字人 | 对比表 | 中部 |
| `/zh/tools/image-enhancer` | AI 图像增强 | 应用场景 | 中部 |
| `/zh/tools/poster-generator` | AI 海报生成 | 应用场景 | 中部 |
| `/zh/tools/text-generator` | AI 文本生成 | 应用场景 | 中部 |
| `/zh/tools/logo-generator` | AI Logo 生成 | 应用场景 | 中部 |
| `/zh/tools/web-search-api` | AI 搜索 API | 如何选择 | 中部 |

**统计**：正文 **8** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **8** 条。

### 3.2 英文版 `content/tools/en/background-changer.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/headshot-generator` | AI headshot generators | Key Takeaways | 开篇 |
| `/tools/workflow` | AI workflow | Key Takeaways | 开篇 |
| `/tools/image-editor` | AI image editing tools | What Are | 开篇 |
| `/tools/image-generator` | AI-powered image generation | What Are | 开篇 |
| `/tools/virtual-staging` | virtual staging | What Are | 开篇 |
| `/tools/image-relighting` | image relighting | What Are | 开篇 |
| `/tools/avatar` | AI talking avatar | Comparison | 中部 |
| `/tools/image-enhancer` | AI image enhancer | Use Cases | 中部 |
| `/tools/poster-generator` | AI poster generators | Use Cases | 中部 |
| `/tools/text-generator` | AI text generators | Use Cases | 中部 |
| `/tools/logo-generator` | AI logo generators | Use Cases | 中部 |
| `/tools/web-search-api` | AI search APIs | How to Choose | 中部 |

**统计**：正文 **12** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **12** 条。

---

## 4. headshot-generator

### 4.1 中文版 `content/tools/zh/headshot-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/image-generator` | AI 图片生成工具 | 什么是 | 开篇 |
| `/zh/tools/image-editor` | AI 图像编辑工具 | 什么是 | 开篇 |
| `/zh/tools/background-changer` | AI 换背景 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/image-relighting` | AI 重打光 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/api` | API 平台 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/image` | AI 图片 | 对比表 | 中部 |
| `/zh/tools/image-enhancer` | AI 图像增强 | 应用场景 | 中部 |
| `/zh/tools/poster-generator` | AI 海报生成 | 应用场景 | 中部 |
| `/zh/tools/logo-generator` | AI Logo 生成 | 应用场景 | 中部 |
| `/zh/tools/spreadsheet` | AI 表格 | 应用场景 | 中部 |
| `/zh/tools/presentation-maker` | AI 演示文稿 | 应用场景 | 中部 |
| `/zh/tools/workflow` | AI 工作流 | 如何选择 | 中部 |
| `/zh/tools/web-search-api` | AI 搜索 API | 如何选择 | 中部 |
| `/zh/tools/website-builder` | AI 建站 | 结论 | 中部 |
| `/zh/tools/avatar` | AI 数字人生成 | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **15** 条。

### 4.2 英文版 `content/tools/en/headshot-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/image-generator` | AI image creation tools | What Are | 开篇 |
| `/tools/image` | AI image tools | What Are | 开篇 |
| `/tools/image-editor` | AI image editors | What Are | 开篇 |
| `/tools/image-enhancer` | AI image enhancer | Use Cases | 中部 |
| `/tools/presentation-maker` | AI presentation makers | Use Cases | 中部 |
| `/tools/poster-generator` | AI poster creation | Use Cases | 中部 |
| `/tools/logo-generator` | AI logo creation | Use Cases | 中部 |
| `/tools/spreadsheet` | AI spreadsheets | Use Cases | 中部 |
| `/tools/text-generator` | AI text generators | Use Cases | 中部 |
| `/tools/web-search-api` | AI search APIs | How to Choose | 中部 |
| `/tools/website-builder` | website creation tools | Conclusion | 中部 |
| `/tools/avatar` | AI talking avatars | FAQ | FAQ |

**统计**：正文 **11** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **12** 条。

---

## 5. legal

### 5.1 中文版 `content/tools/zh/legal.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/text-generator` | AI 文本生成 | 什么是 | 开篇 |
| `/zh/tools/productivity` | AI 生产力工具 | 什么是 | 开篇 |
| `/zh/tools/notes-generator` | AI 笔记生成 | 应用场景 | 中部 |
| `/zh/tools/education` | AI学生工具 | 结论 | 后部 |
| `/zh/tools/religion` | AI宗教工具 | 结论 | 后部 |
| `/zh/tools/presentation-maker` | AI演示文稿工具 | 结论 | 后部 |
| `/zh/tools/note-taker` | 会议记录工具 | FAQ | FAQ |
| `/zh/tools/speech-to-text` | 语音转文字 | FAQ | FAQ |

**统计**：正文 **6** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **8** 条。

### 5.2 英文版 `content/tools/en/legal.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/notes-generator` | smart notes apps | Use Cases | 中部 |
| `/tools/note-taker` | note takers | FAQ | FAQ |
| `/tools/speech-to-text` | speech-to-text | FAQ | FAQ |

**统计**：正文 **2** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **4** 条。

---

## 6. geo

### 6.1 中文版 `content/tools/zh/geo.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/search-engine` | AI搜索引擎 | 什么是 | 开篇 |
| `/zh/tools/browser` | AI 浏览器 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/search-indexing` | AI 搜索索引 | 对比表 | 中部 |
| `/zh/tools/notes-generator` | AI 笔记生成 | 应用场景 | 中部 |
| `/zh/tools/productivity` | AI 效率 | 如何选择 | 中部 |
| `/zh/tools/api` | AI API | 如何选择 | 中部 |
| `/zh/tools/user-research` | AI 用户研究 | 如何选择 | 中部 |
| `/zh/tools/spreadsheet` | 智能表格工具 | 如何选择 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 产品目录 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 会议记录 | FAQ | FAQ |
| `/zh/tools/recruiting` | AI 招聘 | FAQ | FAQ |
| `/zh/tools/speech-to-text` | 语音转文字 | FAQ | FAQ |

**统计**：正文 **10** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **13** 条。

### 6.2 英文版 `content/tools/en/geo.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/web-search-api` | AI search APIs | What Are | 开篇 |
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/ocr` | AI OCR tools | How It Works · technologyBase | 前部 |
| `/tools/search-indexing` | AI search indexing | Comparison | 中部 |
| `/tools/notes-generator` | AI meeting notes tools | Use Cases | 中部 |
| `/tools/productivity` | AI productivity | How to Choose | 中部 |
| `/tools/api` | AI API | How to Choose | 中部 |
| `/tools/user-research` | AI user research | How to Choose | 中部 |
| `/tools/spreadsheet` | AI spreadsheet | How to Choose | 中部 |
| `/tools/chatbot` | AI chatbot | How to Choose | 中部 |
| `/tools/directory` | AI directory | Conclusion | 后部 |
| `/tools/search-engine` | AI Search Engines | Conclusion | 后部 |
| `/tools/note-taker` | AI note taker | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting | FAQ | FAQ |
| `/tools/speech-to-text` | speech-to-text | FAQ | FAQ |

**统计**：正文 **12** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **15** 条。

---

## 7. web-search-api

### 7.1 中文版 `content/tools/zh/web-search-api.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/search-engine` | AI 搜索引擎 | 核心要点 | 开篇 |
| `/zh/tools/llm` | 大模型平台 | 什么是 | 开篇 |
| `/zh/tools/geo` | GEO（生成式引擎优化） | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/search-indexing` | 搜索索引 | 最佳工具 | 中部 |
| `/zh/tools/text-generator` | AI 文本生成 | 应用场景 | 中部 |
| `/zh/tools/workflow` | 工作流自动化 | 应用场景 | 中部 |
| `/zh/tools/api` | 云端 API | 如何选择 | 中部 |
| `/zh/tools/web-scraping` | 网页抓取 | 结论 | 后部 |
| `/zh/tools/evaluation` | AI 评估 | FAQ | FAQ |
| `/zh/tools/browser` | AI 浏览器 | FAQ | FAQ |

**统计**：正文 **8** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **10** 条。

### 7.2 英文版 `content/tools/en/web-search-api.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm` | LLM platforms | What Are | 开篇 |
| `/tools/knowledge-base` | knowledge base | What Are | 开篇 |
| `/tools/geo` | GEO tools | How It Works · technologyBase | 前部 |
| `/tools/search-indexing` | search indexing | BestTools | 中部 |
| `/tools/text-generator` | AI text generators | Use Cases | 中部 |
| `/tools/workflow` | workflow automation | Use Cases | 中部 |
| `/tools/api` | cloud API | How to Choose | 中部 |
| `/tools/search-engine` | AI Search Engines | Conclusion | 后部 |
| `/tools/web-scraping` | Best Web Scraping Tools | Conclusion | 后部 |
| `/tools/evaluation` | AI evaluation | FAQ | FAQ |
| `/tools/browser` | AI browser | FAQ | FAQ |

**统计**：正文 **9** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **11** 条。

---

## 8. search-engine

### 8.1 中文版 `content/tools/zh/search-engine.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/browser` | AI 浏览器 | 什么是 | 开篇 |
| `/zh/tools/knowledge-base` | AI 知识库工具 | 什么是 | 开篇 |
| `/zh/tools/text-generator` | AI 文本生成工具 | 什么是 | 开篇 |
| `/zh/tools/web-search-api` | Web Search API 指南 | 什么是 | 开篇 |
| `/zh/tools/evaluation` | AI 评估 | 如何选择 | 中部 |
| `/zh/tools/geo` | GEO（生成式引擎优化） | 结论 | 后部 |
| `/zh/tools/search-indexing` | 搜索索引优化 | 结论 | 后部 |
| `/zh/tools/web-scraping` | AI数据采集 | 结论 | 后部 |

**统计**：正文 **8** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **8** 条。

### 8.2 英文版 `content/tools/en/search-engine.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/browser` | AI browser tools | What Are | 开篇 |
| `/tools/knowledge-base` | AI knowledge bases | What Are | 开篇 |
| `/tools/search-indexing` | AI search indexing tools | How It Works · technologyBase | 前部 |
| `/tools/evaluation` | AI evaluation | How to Choose | 中部 |
| `/tools/geo` | GEO | Conclusion | 后部 |

**统计**：正文 **5** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **5** 条。

---

## 9. code-review

### 9.1 中文版 `content/tools/zh/code-review.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/code-completion` | AI 代码补全 | 什么是 | 开篇 |
| `/zh/tools/coding` | AI 编程工具 | 什么是 | 开篇 |
| `/zh/tools/llm` | 大语言模型 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/workflow` | 工作流自动化 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/text-generator` | AI 文本生成 | 对比表 | 中部 |
| `/zh/tools/productivity` | 团队效率 | 应用场景 | 中部 |
| `/zh/tools/api` | API | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 中部 |
| `/zh/tools/ide` | AI代码编辑器 | 结论 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | FAQ | FAQ |
| `/zh/tools/notes-generator` | AI 笔记生成 | FAQ | FAQ |
| `/zh/tools/evaluation` | AI 评估 | FAQ | FAQ |

**统计**：正文 **9** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **12** 条。

### 9.2 英文版 `content/tools/en/code-review.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/code-completion` | AI code completion | What Are | 开篇 |
| `/tools/coding` | AI code assistants | How It Works · technologyBase | 中部 |
| `/tools/text-generator` | AI text generators | Comparison | 中部 |
| `/tools/productivity` | productivity | Use Cases | 中部 |
| `/tools/api` | API | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 中部 |
| `/tools/notes-generator` | AI meeting notes | FAQ | FAQ |
| `/tools/browser` | AI browser | FAQ | FAQ |
| `/tools/evaluation` | AI evaluation | FAQ | FAQ |

**统计**：正文 **6** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **9** 条。

---

## 10. agent-skills

### 10.1 中文版 `content/tools/zh/agent-skills.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/workflow` | AI 工作流 | 核心要点 | 开篇 |
| `/zh/tools/evaluation` | AI 评估 | 核心要点 | 开篇 |
| `/zh/tools/vibe-coding` | AI Vibe Coding | 什么是 | 开篇 |
| `/zh/tools/directory` | AI 产品目录 | 应用场景 | 中部 |
| `/zh/tools/app-builder` | 低代码应用搭建 | 应用场景 | 中部 |
| `/zh/tools/knowledge-base` | AI 知识库 | 应用场景 | 中部 |
| `/zh/tools/productivity` | AI 效率 | 应用场景 | 中部 |
| `/zh/tools/web-search-api` | Web 搜索 API | 如何选择 | 中部 |
| `/zh/tools/api` | API 平台 | 如何选择 | 中部 |
| `/zh/tools/user-research` | AI 用户研究 | 如何选择 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/spreadsheet` | AI 表格 | 如何选择 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 结论 | 中部 |
| `/zh/tools/code-review` | AI 代码审查 | 结论 | 中部 |
| `/zh/tools/note-taker` | 会议记录工具 | FAQ | FAQ |
| `/zh/tools/notes-generator` | AI 笔记生成器 | FAQ | FAQ |
| `/zh/tools/text-generator` | AI 文本生成 | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **17** 条。

### 10.2 英文版 `content/tools/en/agent-skills.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/cli` | AI CLI tools | Key Takeaways | 开篇 |
| `/tools/ide` | AI IDE | Key Takeaways | 开篇 |
| `/tools/vibe-coding` | AI vibe coding | What Are | 开篇 |
| `/tools/code-completion` | AI code completion | What Are | 开篇 |
| `/tools/coding` | AI coding tools | What Are | 开篇 |
| `/tools/llm` | large language model | How It Works · technologyBase | 中部 |
| `/tools/agent-for-desktop` | AI desktop agent tools | How It Works · technologyBase | 中部 |
| `/tools/evaluation` | AI evaluation | Comparison | 中部 |
| `/tools/directory` | AI tool directories | Use Cases | 中部 |
| `/tools/app-builder` | AI app builders | Use Cases | 中部 |
| `/tools/knowledge-base` | AI knowledge base | Use Cases | 中部 |
| `/tools/productivity` | AI productivity | Use Cases | 中部 |
| `/tools/web-search-api` | Web Search API | How to Choose | 中部 |
| `/tools/api` | API platform | How to Choose | 中部 |
| `/tools/user-research` | AI user research | How to Choose | 中部 |
| `/tools/chatbot` | AI chatbots | How to Choose | 中部 |
| `/tools/spreadsheet` | AI spreadsheet | How to Choose | 中部 |
| `/tools/browser` | AI browser | Conclusion | 中部 |
| `/tools/code-review` | AI code review | Conclusion | 中部 |
| `/tools/note-taker` | AI note taker | FAQ | FAQ |
| `/tools/notes-generator` | AI notes generators | FAQ | FAQ |
| `/tools/text-generator` | AI text generators | FAQ | FAQ |

**统计**：正文 **19** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **22** 条。

---

## 11. web-scraping

### 11.1 中文版 `content/tools/zh/web-scraping.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/web-search-api` | Web Search API | 什么是 | 开篇 |
| `/zh/tools/llm` | 大语言模型工具 | 如何选择 | 中部 |
| `/zh/tools/workflow` | AI 工作流工具 | 如何选择 | 中部 |
| `/zh/tools/geo` | GEO | 结论 | 后部 |

**统计**：正文 **4** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **4** 条。

### 11.2 英文版 `content/tools/en/web-scraping.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/web-search-api` | Web Search API | What Are | 开篇 |
| `/tools/llm` | LLM tools | How to Choose | 中部 |
| `/tools/workflow` | workflow automation | How to Choose | 中部 |
| `/tools/geo` | Generative Engine Optimization | Conclusion | 后部 |
| `/tools/search-engine` | AI Search Engines | Conclusion | 后部 |
| `/tools/search-indexing` | Search Indexing Tools | Conclusion | 后部 |
| `/tools/browser` | AI Browsers | Conclusion | 后部 |

**统计**：正文 **7** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **7** 条。

---

## 12. documentation

### 12.1 中文版 `content/tools/zh/documentation.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/vibe-coding` | AI Vibe Coding | 什么是 | 开篇 |
| `/zh/tools/coding` | AI 编程 | 什么是 | 开篇 |
| `/zh/tools/api` | API 平台 | 什么是 | 开篇 |
| `/zh/tools/ide` | AI IDE | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/cli` | AI CLI 工具 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/web-search-api` | Web 搜索 API | 对比表 | 中部 |
| `/zh/tools/geo` | GEO | 对比表 | 中部 |
| `/zh/tools/directory` | AI 产品目录 | 应用场景 | 中部 |
| `/zh/tools/app-builder` | 低代码应用搭建 | 应用场景 | 中部 |
| `/zh/tools/code-completion` | AI 代码补全 | 应用场景 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 应用场景 | 中部 |
| `/zh/tools/website-builder` | AI 建站 | 如何选择 | 中部 |
| `/zh/tools/text-generator` | AI 文本生成 | 如何选择 | 中部 |
| `/zh/tools/productivity` | AI 效率 | 如何选择 | 中部 |
| `/zh/tools/user-research` | AI 用户研究 | 如何选择 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 结论 | 中部 |
| `/zh/tools/code-review` | AI 代码审查 | 结论 | 中部 |
| `/zh/tools/note-taker` | 会议记录工具 | FAQ | FAQ |
| `/zh/tools/notes-generator` | AI 笔记生成 | FAQ | FAQ |
| `/zh/tools/recruiting` | AI 招聘 | FAQ | FAQ |

**统计**：正文 **17** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **20** 条。

### 12.2 英文版 `content/tools/en/documentation.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/knowledge-base` | AI knowledge base | Key Takeaways | 开篇 |
| `/tools/vibe-coding` | AI vibe coding | What Are | 开篇 |
| `/tools/coding` | AI coding tools | What Are | 开篇 |
| `/tools/api` | API platform | What Are | 开篇 |
| `/tools/llm` | large language models | How It Works · technologyBase | 中部 |
| `/tools/workflow` | AI workflow | How It Works · technologyBase | 中部 |
| `/tools/ide` | AI IDE | How It Works · technologyBase | 中部 |
| `/tools/cli` | AI CLI tools | How It Works · technologyBase | 中部 |
| `/tools/web-search-api` | Web Search API | Comparison | 中部 |
| `/tools/geo` | GEO | Comparison | 中部 |
| `/tools/directory` | AI directory | Use Cases | 中部 |
| `/tools/app-builder` | AI app builders | Use Cases | 中部 |
| `/tools/code-completion` | AI code completion | Use Cases | 中部 |
| `/tools/chatbot` | AI chatbots | Use Cases | 中部 |
| `/tools/website-builder` | AI website builders | How to Choose | 中部 |
| `/tools/text-generator` | AI text generators | How to Choose | 中部 |
| `/tools/productivity` | AI productivity | How to Choose | 中部 |
| `/tools/user-research` | user research platforms | How to Choose | 中部 |
| `/tools/browser` | AI browser | Conclusion | 中部 |
| `/tools/code-review` | AI code review | Conclusion | 中部 |
| `/tools/note-taker` | AI note taker | FAQ | FAQ |
| `/tools/notes-generator` | AI notes generators | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting | FAQ | FAQ |

**统计**：正文 **20** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **23** 条。

---

## 13. headless-browser

### 13.1 中文版 `content/tools/zh/headless-browser.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm` | 大语言模型工具 | 什么是 | 开篇 |
| `/zh/tools/web-search-api` | Web 搜索 API | 什么是 | 开篇 |
| `/zh/tools/workflow` | AI 工作流 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/agent-skills` | Agent Skills 目录 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/coding` | AI 编程 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/ide` | AI IDE | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/api` | API 平台 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/vibe-coding` | Vibe coding | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/knowledge-base` | AI 知识库 | 应用场景 | 中部 |
| `/zh/tools/directory` | AI 产品目录 | 应用场景 | 中部 |
| `/zh/tools/cli` | AI CLI 工具 | 如何选择 | 中部 |
| `/zh/tools/productivity` | 效率 | 如何选择 | 中部 |
| `/zh/tools/geo` | GEO | 结论 | 中部 |
| `/zh/tools/evaluation` | AI 评估工具 | FAQ | FAQ |
| `/zh/tools/code-review` | AI 代码审查 | FAQ | FAQ |
| `/zh/tools/website-builder` | AI 建站 | FAQ | FAQ |

**统计**：正文 **13** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **16** 条。

### 13.2 英文版 `content/tools/en/headless-browser.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/web-scraping` | web scraping tools | Key Takeaways | 开篇 |
| `/tools/browser` | AI browsers | Key Takeaways | 开篇 |
| `/tools/llm` | LLM tools | What Are | 开篇 |
| `/tools/web-search-api` | Web Search API | What Are | 开篇 |
| `/tools/workflow` | workflow automation | How It Works · technologyBase | 中部 |
| `/tools/agent-skills` | Agent Skills directories | How It Works · technologyBase | 中部 |
| `/tools/coding` | AI coding | How It Works · technologyBase | 中部 |
| `/tools/ide` | IDE | How It Works · technologyBase | 中部 |
| `/tools/api` | API platform | How It Works · technologyBase | 中部 |
| `/tools/vibe-coding` | vibe coding | How It Works · technologyBase | 中部 |
| `/tools/knowledge-base` | AI knowledge base | Use Cases | 中部 |
| `/tools/directory` | AI tool directories | Use Cases | 中部 |
| `/tools/cli` | AI CLI tools | How to Choose | 中部 |
| `/tools/productivity` | productivity | How to Choose | 中部 |
| `/tools/geo` | GEO | Conclusion | 中部 |
| `/tools/evaluation` | AI evaluation tools | FAQ | FAQ |
| `/tools/code-review` | AI code review | FAQ | FAQ |
| `/tools/website-builder` | AI site builders | FAQ | FAQ |

**统计**：正文 **15** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **18** 条。

---

## 14. authentication

### 14.1 中文版 `content/tools/zh/authentication.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/knowledge-base` | AI知识库 | 什么是 | 开篇 |
| `/zh/tools/llm` | 大语言模型 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/browser` | AI 浏览器 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/web-search-api` | Web 搜索 API | 对比表 | 中部 |
| `/zh/tools/notes-generator` | AI 笔记生成 | 应用场景 | 中部 |
| `/zh/tools/productivity` | AI 效率 | 如何选择 | 中部 |
| `/zh/tools/api` | API 平台 | 如何选择 | 中部 |
| `/zh/tools/user-research` | AI 用户研究 | 如何选择 | 中部 |
| `/zh/tools/spreadsheet` | AI电子表格 | 如何选择 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 产品目录 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 会议记录 | FAQ | FAQ |
| `/zh/tools/recruiting` | AI 招聘 | FAQ | FAQ |
| `/zh/tools/speech-to-text` | 语音转文字 | FAQ | FAQ |

**统计**：正文 **11** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **14** 条。

### 14.2 英文版 `content/tools/en/authentication.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/workflow` | AI workflow | Key Takeaways | 开篇 |
| `/tools/evaluation` | AI evaluation | Key Takeaways | 开篇 |
| `/tools/app-builder` | AI app builders | What Are | 开篇 |
| `/tools/knowledge-base` | AI knowledge base | What Are | 开篇 |
| `/tools/agent-skills` | Agent Skills | What Are | 开篇 |
| `/tools/llm` | large language model | How It Works · technologyBase | 前部 |
| `/tools/browser` | AI browser | How It Works · technologyBase | 前部 |
| `/tools/web-search-api` | Web Search API | Comparison | 中部 |
| `/tools/notes-generator` | AI meeting notes tools | Use Cases | 中部 |
| `/tools/productivity` | AI productivity | How to Choose | 中部 |
| `/tools/api` | API platform | How to Choose | 中部 |
| `/tools/user-research` | AI UX research tools | How to Choose | 中部 |
| `/tools/spreadsheet` | AI spreadsheet | How to Choose | 中部 |
| `/tools/chatbot` | AI chatbots | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/note-taker` | AI note taker | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting | FAQ | FAQ |
| `/tools/speech-to-text` | speech-to-text | FAQ | FAQ |

**统计**：正文 **15** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **18** 条。

---

## 15. linkedin

### 15.1 中文版 `content/tools/zh/linkedin.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/text-generator` | AI文本生成 | 什么是 | 开篇 |
| `/zh/tools/lead-generation` | AI销售线索工具 | 什么是 | 开篇 |
| `/zh/tools/b2b` | B2B 营销 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/recruiting` | AI 招聘工具 | 应用场景 | 中部 |
| `/zh/tools/interview-assistant` | AI 面试助手 | FAQ | FAQ |
| `/zh/tools/presentation-maker` | AI 演示文稿工具 | FAQ | FAQ |
| `/zh/tools/productivity` | AI 效率/生产力工具 | FAQ | FAQ |

**统计**：正文 **4** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **7** 条。

### 15.2 英文版 `content/tools/en/linkedin.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/lead-generation` | lead generation | What Are | 开篇 |
| `/tools/b2b` | B2B marketing | How It Works · technologyBase | 前部 |
| `/tools/recruiting` | AI recruiting | Use Cases | 中部 |
| `/tools/legal` | AI Legal Assistants & Tools | Conclusion | 后部 |
| `/tools/education` | AI Education Tools | Conclusion | 后部 |
| `/tools/religion` | AI Religion Tools | Conclusion | 后部 |
| `/tools/interview-assistant` | AI interview assistants | FAQ | FAQ |
| `/tools/presentation-maker` | AI presentation makers | FAQ | FAQ |
| `/tools/productivity` | AI productivity | FAQ | FAQ |

**统计**：正文 **7** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **10** 条。

---

## 16. agent-for-desktop

### 16.1 中文版 `content/tools/zh/agent-for-desktop.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/browser` | AI浏览器 | 什么是 | 开篇 |
| `/zh/tools/cli` | AI CLI | 什么是 | 开篇 |
| `/zh/tools/llm` | 大语言模型 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/workflow` | 工作流自动化 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/ide` | AI IDE | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/productivity` | AI 效率工具 | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/authentication` | 身份认证与 IAM | 如何工作 · 核心技术 | 中部 |
| `/zh/tools/knowledge-base` | AI 知识库 | 对比表 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 对比表 | 中部 |
| `/zh/tools/api` | API 平台 | 应用场景 | 中部 |
| `/zh/tools/evaluation` | AI 评估工具 | 应用场景 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/web-search-api` | Web Search API | 如何选择 | 中部 |
| `/zh/tools/geo` | GEO（生成式引擎优化） | 结论 | 中部 |
| `/zh/tools/note-taker` | AI 会议记录 | FAQ | FAQ |
| `/zh/tools/code-review` | AI 代码审查 | FAQ | FAQ |
| `/zh/tools/website-builder` | AI 建站 | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **17** 条。

### 16.2 英文版 `content/tools/en/agent-for-desktop.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/browser` | AI browsers | Key Takeaways | 开篇 |
| `/tools/agent-skills` | Agent Skills directories | Key Takeaways | 开篇 |
| `/tools/headless-browser` | headless and cloud browser | What Are | 开篇 |
| `/tools/cli` | AI CLI tools | What Are | 开篇 |
| `/tools/coding` | AI coding | What Are | 开篇 |
| `/tools/llm` | large language model | How It Works · technologyBase | 中部 |
| `/tools/workflow` | workflow automation | How It Works · technologyBase | 中部 |
| `/tools/ide` | AI IDE | How It Works · technologyBase | 中部 |
| `/tools/productivity` | AI productivity | How It Works · technologyBase | 中部 |
| `/tools/authentication` | authentication and IAM | How It Works · technologyBase | 中部 |
| `/tools/knowledge-base` | AI knowledge base | Comparison | 中部 |
| `/tools/directory` | AI tool directories | Comparison | 中部 |
| `/tools/api` | API platform | Use Cases | 中部 |
| `/tools/evaluation` | AI evaluation tools | Use Cases | 中部 |
| `/tools/chatbot` | chatbot | How to Choose | 中部 |
| `/tools/web-search-api` | Web Search API | How to Choose | 中部 |
| `/tools/geo` | GEO | Conclusion | 中部 |
| `/tools/note-taker` | AI note takers | FAQ | FAQ |
| `/tools/code-review` | AI code review | FAQ | FAQ |
| `/tools/website-builder` | AI website builders | FAQ | FAQ |

**统计**：正文 **17** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **20** 条。

---

## 17. openclaw-alternatives

### 17.1 中文版 `content/tools/zh/openclaw-alternatives.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/agent-for-desktop` | 桌面Agent方案 | 「AI龙虾类产品」与 OpenClaw 替代路线到底指什么 | 开篇 |
| `/zh/tools/documentation` | 开发者文档工具 | 对比表 | 中部 |
| `/zh/tools/knowledge-base` | AI 知识库 | 如何选择 | 中部 |
| `/zh/tools/api` | 云上 API | 如何选择 | 中部 |
| `/zh/tools/directory` | Alignify AI 工具目录 | 结语 | 中部 |
| `/zh/tools/note-taker` | AI 会议记录 | FAQ | FAQ |
| `/zh/tools/evaluation` | AI 评测与基准工具 | FAQ | FAQ |
| `/zh/tools/browser` | AI 浏览器 | FAQ | FAQ |

**统计**：正文 **5** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **8** 条。

### 17.2 英文版 `content/tools/en/openclaw-alternatives.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/agent-for-desktop` | desktop agent approach | What Are | 开篇 |
| `/tools/productivity` | AI productivity | How It Works · technologyBase | 中部 |
| `/tools/chatbot` | chatbots | How It Works · technologyBase | 中部 |
| `/tools/documentation` | Documentation tools | Comparison | 中部 |
| `/tools/knowledge-base` | AI knowledge bases | How to Choose | 中部 |
| `/tools/api` | managed API programs | How to Choose | 中部 |
| `/tools/directory` | AI tool directories | Conclusion | 中部 |
| `/tools/llm` | Large Language Models | Conclusion | 中部 |
| `/tools/character-chat` | AI character chatbots | Conclusion | 中部 |
| `/tools/note-taker` | an AI note taker | FAQ | FAQ |
| `/tools/evaluation` | AI evaluation tooling | FAQ | FAQ |
| `/tools/browser` | browser AI programs | FAQ | FAQ |

**统计**：正文 **9** 条不同 Tools 内链；FAQ **3** 条与正文不重复。合计 **12** 条。

---

## 18. character-chat

### 18.1 中文版 `content/tools/zh/character-chat.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/chatbot` | AI对话助手 | 什么是 | 开篇 |
| `/zh/tools/text-to-speech` | 文字转语音工具 | 什么是 | 开篇 |
| `/zh/tools/avatar` | AI 数字人生成 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/text-generator` | 文本生成工具 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/api` | API 平台 | 合规边界、BYOK 与「替代品」检索 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 合规边界、BYOK 与「替代品」检索 | 中部 |
| `/zh/tools/notes-generator` | 笔记生成工具 | 应用场景 | 中部 |
| `/zh/tools/productivity` | 效率工具 | 如何选择 | 中部 |
| `/zh/tools/evaluation` | 评估与基准工具 | 如何选择 | 中部 |
| `/zh/tools/web-search-api` | Web Search API | 如何选择 | 中部 |
| `/zh/tools/website-builder` | AI 建站工具 | 结论 | 后部 |
| `/zh/tools/geo` | GEO（生成式引擎优化） | 结论 | 后部 |
| `/zh/tools/speech-to-text` | 语音转文字工具 | FAQ | FAQ |
| `/zh/tools/recruiting` | AI 招聘工具 | FAQ | FAQ |

**统计**：正文 **12** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **14** 条。

### 18.2 英文版 `content/tools/en/character-chat.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm` | LLM tools | Key Takeaways | 开篇 |
| `/tools/workflow` | workflow automation | Key Takeaways | 开篇 |
| `/tools/chatbot` | AI chatbot tools | What Are | 开篇 |
| `/tools/text` | AI text tools | What Are | 开篇 |
| `/tools/text-to-speech` | text-to-speech tools | What Are | 开篇 |
| `/tools/avatar` | AI avatar / talking avatar tools | How It Works · technologyBase | 前部 |
| `/tools/text-generator` | AI text generators | How It Works · technologyBase | 前部 |
| `/tools/headshot-generator` | AI headshot generators | How It Works · technologyBase | 前部 |
| `/tools/api` | API platforms | Filters, BYOK, and “alternative” se | 中部 |
| `/tools/directory` | AI tool directories | Filters, BYOK, and “alternative” se | 中部 |
| `/tools/notes-generator` | smart notes apps | Use Cases | 中部 |
| `/tools/productivity` | AI productivity tools | How to Choose | 中部 |
| `/tools/evaluation` | AI evaluation tools | How to Choose | 中部 |
| `/tools/web-search-api` | Web Search API tools | How to Choose | 中部 |
| `/tools/website-builder` | AI website builders | Conclusion | 后部 |
| `/tools/geo` | GEO tools | Conclusion | 后部 |
| `/tools/speech-to-text` | speech-to-text tools | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting tools | FAQ | FAQ |

**统计**：正文 **16** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **18** 条。

---

## 19. llm

### 19.1 中文版 `content/tools/zh/llm.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm-for-math` | 数学大模型指南 | 核心要点 | 开篇 |
| `/zh/tools/multimodal-llm` | 多模态大模型指南 | 核心要点 | 开篇 |
| `/zh/tools/text-generator` | AI文本生成 | 什么是 | 开篇 |
| `/zh/tools/knowledge-base` | AI 知识库 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/workflow` | AI 工作流 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/evaluation` | AI 评估工具 | 公开榜单与基准：如何读分而不被排行绑架 | 中部 |
| `/zh/tools/search-engine` | AI 搜索引擎 | 公开榜单与基准：如何读分而不被排行绑架 | 中部 |
| `/zh/tools/geo` | GEO | 公开榜单与基准：如何读分而不被排行绑架 | 中部 |
| `/zh/tools/documentation` | 开发者文档 | 检索增强、接口形态与人工把关 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 检索增强、接口形态与人工把关 | 中部 |
| `/zh/tools/llm-for-reasoning` | AI 推理大模型 | 对比表 | 中部 |
| `/zh/tools/chatbot` | AI 聊天机器人 | 应用场景 | 中部 |
| `/zh/tools/llm-for-coding` | AI 编程大模型 | 应用场景 | 中部 |
| `/zh/tools/api` | API 平台 | 如何选择 | 中部 |
| `/zh/tools/character-chat` | 智能角色对话 | 结论 | 后部 |

**统计**：正文 **15** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **15** 条。

### 19.2 英文版 `content/tools/en/llm.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm-for-math` | AI math LLM guide | Key Takeaways | 开篇 |
| `/tools/llm-for-coding` | LLMs for coding | What Are | 开篇 |
| `/tools/llm-for-reasoning` | LLMs for reasoning | What Are | 开篇 |
| `/tools/evaluation` | AI model evaluation platforms | What Are | 开篇 |
| `/tools/knowledge-base` | knowledge base | How It Works · technologyBase | 前部 |
| `/tools/workflow` | AI workflow | How It Works · technologyBase | 前部 |
| `/tools/geo` | GEO practice | How LLM Leaderboards Work (and Why  | 中部 |
| `/tools/documentation` | developer documentation | Grounding, API Deployments, and Whe | 中部 |
| `/tools/text-generator` | AI text generators | Comparison | 中部 |
| `/tools/api` | cloud API partner | How to Choose | 中部 |
| `/tools/chatbot` | AI chatbot | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/character-chat` | AI Character Chat | Conclusion | 后部 |

**统计**：正文 **13** 条不同 Tools 内链；FAQ **0** 条与正文不重复。合计 **13** 条。

---

## 20. llm-for-coding

### 20.1 中文版 `content/tools/zh/llm-for-coding.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm` | 大语言模型 | 什么是 | 开篇 |
| `/zh/tools/code-completion` | AI 代码补全工具 | 什么是 | 开篇 |
| `/zh/tools/knowledge-base` | 知识库与 RAG | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/workflow` | 工作流自动化工具 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/evaluation` | AI 模型评测指南 | 编程榜单怎么读（为什么 SWE 分数会大起大落） | 中部 |
| `/zh/tools/search-engine` | AI 搜索引擎 | 编程榜单怎么读（为什么 SWE 分数会大起大落） | 中部 |
| `/zh/tools/code-review` | 代码审查 | 仓库落地：检索、合规与榜单测不到的事 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 仓库落地：检索、合规与榜单测不到的事 | 中部 |
| `/zh/tools/documentation` | 开发者文档工具 | 仓库落地：检索、合规与榜单测不到的事 | 中部 |
| `/zh/tools/llm-for-math` | 数学大模型指南 | 对比表 | 中部 |
| `/zh/tools/vibe-coding` | vibe coding（氛围编程） | 应用场景 | 中部 |
| `/zh/tools/api` | Web API | 如何选择 | 中部 |
| `/zh/tools/chatbot` | 聊天机器人搭建工具 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 会议纪要 / 笔记工具 | FAQ | FAQ |
| `/zh/tools/recruiting` | AI 招聘工具 | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **16** 条。

### 20.2 英文版 `content/tools/en/llm-for-coding.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm-for-reasoning` | reasoning models | Key Takeaways | 开篇 |
| `/tools/multimodal-llm` | multimodal LLMs | Key Takeaways | 开篇 |
| `/tools/llm` | general LLM tools | What Are | 开篇 |
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/code-completion` | AI code completion tools | What Are | 开篇 |
| `/tools/knowledge-base` | knowledge base | How It Works · technologyBase | 前部 |
| `/tools/workflow` | workflow automation tools | How It Works · technologyBase | 前部 |
| `/tools/evaluation` | AI evaluation guide | How Coding Leaderboards Work (and W | 中部 |
| `/tools/search-engine` | search engine | How Coding Leaderboards Work (and W | 中部 |
| `/tools/code-review` | code review | What Are | 中部 |
| `/tools/browser` | AI browser | What Are | 中部 |
| `/tools/documentation` | developer documentation | What Are | 中部 |
| `/tools/llm-for-math` | math LLM guide | Comparison | 中部 |
| `/tools/vibe-coding` | vibe coding | Use Cases | 中部 |
| `/tools/api` | Web API | How to Choose | 中部 |
| `/tools/chatbot` | chatbot builders | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/note-taker` | AI note takers | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting tools | FAQ | FAQ |

**统计**：正文 **17** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **19** 条。

---

## 21. llm-for-math

### 21.1 中文版 `content/tools/zh/llm-for-math.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm` | 大语言模型 | 什么是 | 开篇 |
| `/zh/tools/search-engine` | AI 搜索引擎 | 什么是 | 开篇 |
| `/zh/tools/workflow` | 工作流自动化 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/evaluation` | AI 模型评测 | 竞赛榜、证明题与 FrontierMath 分层 | 中部 |
| `/zh/tools/documentation` | 开发者文档/教案出口 | 从教培到 FP&A：奥数分数哪里会骗人 | 中部 |
| `/zh/tools/browser` | 浏览器 | 从教培到 FP&A：奥数分数哪里会骗人 | 中部 |
| `/zh/tools/web-search-api` | 联网搜索 API | 从教培到 FP&A：奥数分数哪里会骗人 | 中部 |
| `/zh/tools/llm-for-coding` | AI 编程大模型指南 | 对比表 | 中部 |
| `/zh/tools/text-generator` | 长文本生成工具 | 应用场景 | 中部 |
| `/zh/tools/api` | Web API | 如何选择 | 中部 |
| `/zh/tools/chatbot` | 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 后部 |
| `/zh/tools/character-chat` | AI角色聊天 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 笔记/会议纪要工具 | FAQ | FAQ |

**统计**：正文 **13** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **14** 条。

### 21.2 英文版 `content/tools/en/llm-for-math.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm-for-reasoning` | reasoning-first LLMs | Key Takeaways | 开篇 |
| `/tools/multimodal-llm` | multimodal LLM | Key Takeaways | 开篇 |
| `/tools/llm` | general LLM tools | What Are | 开篇 |
| `/tools/memory` | AI memory tools | What Are | 开篇 |
| `/tools/search-engine` | AI search engine guide | What Are | 开篇 |
| `/tools/evaluation` | AI evaluation guide | Competition Leaderboards, Proof Tas | 中部 |
| `/tools/documentation` | documentation | From Tutoring UX to FP&A: Where Oly | 中部 |
| `/tools/browser` | browser | From Tutoring UX to FP&A: Where Oly | 中部 |
| `/tools/web-search-api` | Web Search API | From Tutoring UX to FP&A: Where Oly | 中部 |
| `/tools/llm-for-coding` | AI coding LLM guide | Comparison | 中部 |
| `/tools/text-generator` | long-form text generators | Use Cases | 中部 |
| `/tools/api` | Web API | How to Choose | 中部 |
| `/tools/chatbot` | chatbot builders | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/note-taker` | AI note takers | FAQ | FAQ |
| `/tools/recruiting` | AI recruiting tools | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **2** 条与正文不重复。合计 **16** 条。

---

## 22. multimodal-llm

### 22.1 中文版 `content/tools/zh/multimodal-llm.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm-for-coding` | 多模态软件工程 | 核心要点 | 开篇 |
| `/zh/tools/llm-for-math` | 数学向大模型 | 核心要点 | 开篇 |
| `/zh/tools/llm` | 大语言模型 | 什么是 | 开篇 |
| `/zh/tools/image-generator` | AI 图像生成 | 什么是 | 开篇 |
| `/zh/tools/workflow` | 工作流自动化 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/evaluation` | AI 模型评测 | MMMU / Pro、MM-Vet 与裁判效应 | 中部 |
| `/zh/tools/search-engine` | AI 搜索 | MMMU / Pro、MM-Vet 与裁判效应 | 中部 |
| `/zh/tools/world-model` | 世界模型工具 | 世界模型话术、OCR SLA 与工单场景 | 中部 |
| `/zh/tools/documentation` | 开发者文档 | 世界模型话术、OCR SLA 与工单场景 | 中部 |
| `/zh/tools/web-search-api` | 联网搜索 API | 世界模型话术、OCR SLA 与工单场景 | 中部 |
| `/zh/tools/llm-for-reasoning` | AI 推理大模型 | 对比表 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 应用场景 | 中部 |
| `/zh/tools/api` | Web API | 如何选择 | 中部 |
| `/zh/tools/chatbot` | 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 笔记工具 | FAQ | FAQ |

**统计**：正文 **15** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **16** 条。

### 22.2 英文版 `content/tools/en/multimodal-llm.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm-for-coding` | multimodal software engineering | Key Takeaways | 开篇 |
| `/tools/llm` | general LLM tools | What Are | 开篇 |
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/image-generator` | image generators | What Are | 开篇 |
| `/tools/llm-for-reasoning` | AI reasoning tools | How It Works · technologyBase | 前部 |
| `/tools/evaluation` | AI evaluation guide | MMMU vs MMMU-Pro, MM-Vet, and Judge | 中部 |
| `/tools/search-engine` | AI search products | MMMU vs MMMU-Pro, MM-Vet, and Judge | 中部 |
| `/tools/world-model` | world model tooling guide | World Models, OCR SLAs, and Support | 中部 |
| `/tools/documentation` | documentation | World Models, OCR SLAs, and Support | 中部 |
| `/tools/web-search-api` | Web Search API | World Models, OCR SLAs, and Support | 中部 |
| `/tools/browser` | AI browser | Use Cases | 中部 |
| `/tools/api` | Web API | How to Choose | 中部 |
| `/tools/chatbot` | chatbot builders | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/note-taker` | AI note takers | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **15** 条。

---

## 23. llm-for-reasoning

### 23.1 中文版 `content/tools/zh/llm-for-reasoning.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/llm-for-math` | 数学大模型 | 核心要点 | 开篇 |
| `/zh/tools/llm-for-coding` | 编程大模型 | 核心要点 | 开篇 |
| `/zh/tools/llm` | 大语言模型 | 什么是 | 开篇 |
| `/zh/tools/search-engine` | AI 搜索 | 什么是 | 开篇 |
| `/zh/tools/workflow` | 工作流自动化 | 如何工作 · 核心技术 | 前部 |
| `/zh/tools/evaluation` | AI 模型评测 | GPQA、HLE、ARC-AGI-2 与精炼循环 | 中部 |
| `/zh/tools/geo` | GEO（生成式引擎优化） | GPQA、HLE、ARC-AGI-2 与精炼循环 | 中部 |
| `/zh/tools/web-search-api` | 联网搜索 API | 时延路由、工具模式与人审门禁 | 中部 |
| `/zh/tools/documentation` | 开发者文档 | 时延路由、工具模式与人审门禁 | 中部 |
| `/zh/tools/browser` | AI 浏览器 | 时延路由、工具模式与人审门禁 | 中部 |
| `/zh/tools/multimodal-llm` | 多模态大模型指南 | 对比表 | 中部 |
| `/zh/tools/text-generator` | 长文本生成工具 | 应用场景 | 中部 |
| `/zh/tools/api` | Web API | 如何选择 | 中部 |
| `/zh/tools/chatbot` | 聊天机器人 | 如何选择 | 中部 |
| `/zh/tools/directory` | AI 工具目录 | 结论 | 后部 |
| `/zh/tools/note-taker` | AI 笔记工具 | FAQ | FAQ |

**统计**：正文 **15** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **16** 条。

### 23.2 英文版 `content/tools/en/llm-for-reasoning.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/llm-for-math` | math LLM | Key Takeaways | 开篇 |
| `/tools/llm-for-coding` | coding LLM | Key Takeaways | 开篇 |
| `/tools/llm` | general LLM tools | What Are | 开篇 |
| `/tools/text-generator` | AI text generators | What Are | 开篇 |
| `/tools/search-engine` | AI search engine guide | What Are | 开篇 |
| `/tools/chatbot` | AI chatbot tools | How It Works · technologyBase | 前部 |
| `/tools/evaluation` | AI evaluation guide | GPQA, Humanity's Last Exam, ARC-AGI | 中部 |
| `/tools/geo` | GEO programs | GPQA, Humanity's Last Exam, ARC-AGI | 中部 |
| `/tools/web-search-api` | Web Search API | Latency-Sensitive Routing, Tools, a | 中部 |
| `/tools/documentation` | documentation | Latency-Sensitive Routing, Tools, a | 中部 |
| `/tools/browser` | AI browser | Latency-Sensitive Routing, Tools, a | 中部 |
| `/tools/multimodal-llm` | multimodal LLM guide | Comparison | 中部 |
| `/tools/api` | Web API | How to Choose | 中部 |
| `/tools/directory` | AI tools directory | Conclusion | 后部 |
| `/tools/note-taker` | AI note takers | FAQ | FAQ |

**统计**：正文 **14** 条不同 Tools 内链；FAQ **1** 条与正文不重复。合计 **15** 条。

---

## blog-ai-training-data · `ai-training-data`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/ai-training-data.md` · **2026-06-23** 初版。

### 中文版 `content/blog/zh/ai-training-data.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/evaluation` | AI 评测工具 | 什么是 | 开篇 |
| `/zh/tools/web-scraping` | 网页抓取工具 | 什么是 | 开篇 |
| `/zh/tools/world-model` | 世界模型 | 应用场景 | 中部 |
| `/zh/blog/inference-infrastructure` | 推理基础设施 | 如何选择 | 中部 |
| `/zh/tools/llm` | 大模型评测 | 结论 | 后部 |

**统计**：正文 **5** 条不同内链（含 1 条 Blog→Blog）；FAQ **0** 条站内链。

### 英文版 `content/blog/en/ai-training-data.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/evaluation` | AI evaluation tools | What Are | 开篇 |
| `/tools/web-scraping` | web scraping tools | What Are | 开篇 |
| `/tools/world-model` | world models | Use Cases | 中部 |
| `/blog/inference-infrastructure` | inference infrastructure | How to Choose | 中部 |
| `/tools/llm` | LLM benchmarks | Conclusion | 后部 |

**统计**：正文 **5** 条不同内链（含 1 条 Blog→Blog）；FAQ **0** 条站内链。

**跨页互链建议（keywords `#ai-training-data-tools` 对齐）**：`evaluation`、`web-scraping`、`world-model`、`inference-infrastructure`、`llm` 源页可在「什么是 / 应用场景 / 如何选择」中链向 `/blog/ai-training-data`（锚文本变体示例：「大模型训练数据平台」「AI training data platform」「RLHF 数据采购」），全文 URL 唯一。

---

## blog-multi-agent · `multi-agent`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/multi-agent.md` · **2026-06-23** 初版。

### 中文版 `content/blog/zh/multi-agent.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/workflow` | 工作流自动化 | 什么是 | 开篇 |
| `/zh/tools/agent-for-desktop` | 桌面智能体 | 什么是 | 开篇 |
| `/zh/tools/openclaw-alternatives` | OpenClaw 生态 | 各类型工具详细介绍 | 中部 |
| `/zh/tools/agent-skills` | Agent Skills | 如何工作 | 中部 |
| `/zh/tools/hr-assistant` | AI HR 助手 | 应用场景 | 中部 |
| `/zh/blog/agent-sandbox` | Agent 沙箱 | 如何选择 | 中部 |
| `/zh/tools/hr-assistant` | AI HR 助手 | 应用场景 | 中部 |
| `/zh/tools/llm` | 大模型选型 | 结论 | 后部 |

**统计**：正文 **7** 条不同内链（含 1 条 Blog→Blog）；FAQ **4** 条站内链（workflow、agent-for-desktop、openclaw-alternatives、agent-skills）。

### 英文版 `content/blog/en/multi-agent.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/workflow` | workflow automation | What Are | 开篇 |
| `/tools/agent-for-desktop` | desktop agents | What Are | 开篇 |
| `/tools/openclaw-alternatives` | OpenClaw ecosystem | Best Tools | 中部 |
| `/tools/agent-skills` | Agent Skills | How It Works | 中部 |
| `/tools/hr-assistant` | AI HR assistants | Use Cases | 中部 |
| `/blog/agent-sandbox` | agent sandbox | How to Choose | 中部 |
| `/tools/llm` | LLM selection | Conclusion | 后部 |

**统计**：正文 **7** 条不同内链（含 1 条 Blog→Blog）；FAQ **4** 条站内链（workflow、agent-for-desktop、openclaw-alternatives、agent-skills）。

**跨页互链建议（keywords `#multi-agent-tools` 对齐）**：`workflow`、`agent-for-desktop`、`openclaw-alternatives`、`agent-skills` 源页可在「什么是 / 场景 / FAQ」中链向 `/blog/multi-agent`（锚文本变体：「多智能体系统」「multi-agent orchestration」「Agent 工作空间」），全文 URL 唯一。

---

## blog-medical-scribe · `medical-scribe`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/medical-scribe.md` · **2026-06-23** 初版。

### 中文版 `content/blog/zh/medical-scribe.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/note-taker` | AI 会议记录 | 什么是 | 开篇 |
| `/zh/tools/healthcare` | AI 医疗工具 | 什么是 | 开篇 |

**统计**：正文 **2** 条不同内链；FAQ **0** 条站内链（healthcare 关系见 FAQ 纯文本）。

### 英文版 `content/blog/en/medical-scribe.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/note-taker` | AI note takers | What Are | 开篇 |
| `/tools/healthcare` | AI healthcare tools | What Are | 开篇 |

**统计**：正文 **2** 条不同内链；FAQ **0** 条站内链。

**跨页互链建议（keywords `#medical-scribe-tools` 对齐）**：`healthcare` 页在 useCases / 结论 / FAQ 中链向 `/blog/medical-scribe`（锚文本变体：「最佳 AI 医疗文书」「AI medical scribe guide」），全文 URL 唯一；`note-taker` 源页可在 FAQ 中区分会议记录与环境文书。

---

## blog-web-fetch · `web-fetch`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/web-fetch.md` · **2026-06-23** 初版。

### 中文版 `content/blog/zh/web-fetch.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/web-search-api` | Web Search API | 什么是 | 开篇 |
| `/zh/tools/web-scraping` | Web Scraping | 什么是 | 开篇 |
| `/zh/tools/headless-browser` | 无头浏览器 | 什么是 | 开篇 |

**统计**：正文 **3** 条不同内链；FAQ **0** 条站内链（headless-browser / scraping 关系见 FAQ 纯文本）。

### 英文版 `content/blog/en/web-fetch.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/web-search-api` | Web Search API | What Are | 开篇 |
| `/tools/web-scraping` | Web Scraping | What Are | 开篇 |
| `/tools/headless-browser` | headless browsers | What Are | 开篇 |

**统计**：正文 **3** 条不同内链；FAQ **0** 条站内链。

**跨页互链建议（keywords `#web-fetch-tools` 对齐）**：`web-search-api`、`web-scraping`、`headless-browser` 源页可在「什么是 / 典型场景 / FAQ」中链向 `/blog/web-fetch`（锚文本变体：「Web Fetch 工具」「URL→Markdown」），全文 URL 唯一；与 search→fetch→browser 三层分工对齐。

---

## blog-agent-sandbox · `agent-sandbox`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/agent-sandbox.md` · **2026-06-23** 初版（正文 5 + FAQ 3，全文 href 唯一）。

### 中文版 `content/blog/zh/agent-sandbox.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/agent-skills` | Agent Skills | TL;DR · introduction | 开篇 |
| `/zh/blog/inference-infrastructure` | AI 推理基础设施 | TL;DR · introduction | 开篇 |
| `/zh/tools/agent-for-desktop` | 桌面端 Agent | 什么是 · 第 2 段 | 早期 |
| `/zh/tools/authentication` | 身份认证与 IAM | 应用场景 · 企业部署 | 中部 |
| `/zh/tools/headless-browser` | 无头浏览器 | 应用场景 · Computer Use | 中部 |
| `/zh/tools/cli` | AI CLI | FAQ · 与 agent-skills 关系 | 末尾 |
| `/zh/tools/openclaw-alternatives` | OpenClaw 系谱 | FAQ · NanoClaw 与 OpenClaw | 末尾 |
| `/zh/tools/workflow` | Agent 工作流 | FAQ · 自托管 | 末尾 |

**统计**：正文 **5** 条不同内链；FAQ **3** 条与正文不重复。合计 **8** 条。

### 英文版 `content/blog/en/agent-sandbox.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/agent-skills` | Agent Skills | TL;DR · introduction | 开篇 |
| `/blog/inference-infrastructure` | AI inference infrastructure | TL;DR · introduction | 开篇 |
| `/tools/agent-for-desktop` | desktop agents | What Is · ¶2 | 早期 |
| `/tools/authentication` | authentication and IAM | Use cases · enterprise | 中部 |
| `/tools/headless-browser` | headless browsers | Use cases · computer use | 中部 |
| `/tools/cli` | AI CLI tools | FAQ · agent-skills | 末尾 |
| `/tools/openclaw-alternatives` | OpenClaw alternatives | FAQ · NanoClaw vs OpenClaw | 末尾 |
| `/tools/workflow` | agent workflow tools | FAQ · self-hosted | 末尾 |

**统计**：正文 **5** 条不同内链；FAQ **3** 条与正文不重复。合计 **8** 条。

**跨页互链建议（keywords `#agent-sandbox-tools` 对齐）**：`agent-skills`、`inference-infrastructure`、`headless-browser`、`authentication` 源页可在「什么是 / 场景 / FAQ」中链向 `/blog/agent-sandbox`（锚文本变体：「AI Agent 沙箱」「agent sandbox guide」），全文 URL 唯一；与 Agent 执行链 skills → sandbox → browser 分工对齐。

---



## tools-memory · `memory`（`/tools/memory`）

> **数据源**：`content/tools/zh|en/memory.md` · **2026-06-23** 第二大脑/PKM 重写（移除 Mem0/Zep 等 Agent 中间件主榜）。

### 中文版 `content/tools/zh/memory.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/blog/agent-memory` | AI Agent 记忆层指南 | TL;DR · introduction | 开篇 |
| `/zh/tools/knowledge-base` | 企业知识库 | TL;DR · introduction | 开篇 |
| `/zh/tools/note-taker` | AI 会议纪要 | TL;DR · introduction | 开篇 |
| `/zh/tools/productivity` | 生产力工具 | TL;DR · introduction | 开篇 |
| `/zh/blog/agent-memory` | Agent 记忆中间件 | 什么是 · ¶2 | 早期 |
| `/zh/blog/agent-memory` | Agent 记忆层 | 如何选择 · 步骤1 | 中部 |
| `/zh/blog/agent-memory` | AI Agent 记忆层指南 | 结论 | 后部 |
| `/zh/tools/knowledge-base` | knowledge-base | 应用场景 | 中部 |
| `/zh/tools/note-taker` | note-taker | 什么是 · ¶3 | 早期 |
| `/zh/blog/agent-memory` | Agent 记忆层 | FAQ | 末尾 |

**统计**：正文 **6** 条不同内链（含 blog）；FAQ **1** 条与正文不重复。合计 **7** 条。

### 英文版 `content/tools/en/memory.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/blog/agent-memory` | AI agent memory layer guide | TL;DR · introduction | 开篇 |
| `/tools/knowledge-base` | knowledge base | TL;DR · introduction | 开篇 |
| `/tools/note-taker` | AI note takers | TL;DR · introduction | 开篇 |
| `/tools/productivity` | productivity tools | TL;DR · introduction | 开篇 |
| `/blog/agent-memory` | agent memory middleware | What Are · ¶2 | 早期 |
| `/blog/agent-memory` | agent memory guide | How to Choose · step 1 | 中部 |
| `/blog/agent-memory` | AI agent memory layer guide | Conclusion | 后部 |
| `/tools/knowledge-base` | knowledge-base | Use Cases | 中部 |
| `/tools/note-taker` | note-taker | What Are · ¶3 | 早期 |
| `/blog/agent-memory` | agent memory guide | FAQ | 末尾 |

**统计**：正文 **6** 条不同内链（含 blog）；FAQ **1** 条与正文不重复。合计 **7** 条。

**互链**：与 `blog-agent-memory` 双向分流——memory 页链 Agent 层；agent-memory 页链 `/tools/memory` 第二大脑（已存在于 agent-memory JSON）。

---

## blog-agent-memory · `agent-memory`（`/blog/` 路由）

> **数据源**：`content/blog/zh|en/agent-memory.md` · **2026-06-23** 初版。

### 中文版 `content/blog/zh/agent-memory.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/agent-skills` | Agent Skills | TL;DR · introduction | 开篇 |
| `/zh/tools/memory` | AI 记忆工具 | TL;DR · introduction | 开篇 |
| `/zh/tools/knowledge-base` | 企业知识库 | 什么是 · ¶2 | 早期 |
| `/zh/blog/agent-sandbox` | AI Agent 沙箱 | 如何工作 · architecture | 中部 |
| `/zh/tools/openclaw-alternatives` | OpenClaw MEMORY.md | Coding agents · introduction | 中部 |
| `/zh/tools/agent-skills` | Agent Skills MCP | 如何选择 | 中部 |
| `/zh/tools/memory` | 第二大脑 | FAQ | 末尾 |
| `/zh/tools/knowledge-base` | 企业 RAG | FAQ | 末尾 |

**统计**：正文 **5** 条不同内链；FAQ **2** 条与正文不重复。合计 **7** 条。

### 英文版 `content/blog/en/agent-memory.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/agent-skills` | Agent Skills | TL;DR · introduction | 开篇 |
| `/tools/memory` | AI memory tools | TL;DR · introduction | 开篇 |
| `/tools/knowledge-base` | enterprise knowledge base | What Is · ¶2 | 早期 |
| `/blog/agent-sandbox` | AI agent sandbox | How It Works · architecture | 中部 |
| `/tools/openclaw-alternatives` | OpenClaw MEMORY.md | Coding agents · introduction | 中部 |
| `/tools/agent-skills` | Agent Skills MCP | How to Choose | 中部 |
| `/tools/memory` | second brain | FAQ | 末尾 |
| `/tools/knowledge-base` | enterprise RAG | FAQ | 末尾 |

**统计**：正文 **5** 条不同内链；FAQ **2** 条与正文不重复。合计 **7** 条。

**跨页互链建议（keywords `#agent-memory-tools` 对齐）**：`agent-skills`、`memory`、`knowledge-base`、`openclaw-alternatives` 源页可在「什么是 / FAQ」中链向 `/blog/agent-memory`（锚文本变体：「AI Agent 记忆层」「agent memory guide」），全文 URL 唯一；与 Agent 执行链 skills → memory → sandbox 分工对齐。

---

---

## tools-music-video-generator · `music-video-generator`（`/tools/music-video-generator`）

> **数据源**：`content/tools/zh|en/music-video-generator.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/music-video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/design` | Design | tldr · article-intro | — |
| `/zh/tools/music-generator` | Music Generator | section · what-are-ai-music-video-generator-tools | — |
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-music-video-generator-tools | — |
| `/zh/tools/voice` | Voice | section · music-video-generation-types | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/zh/tools/avatar` | Avatar | section · conclusion | — |
| `/zh/tools/world-model` | World Model | section · conclusion | — |
| `/zh/tools/text-to-speech` | Text To Speech | section · conclusion | — |
| `/zh/tools/animation-generator` | Animation Generator | section · conclusion | — |

**统计**：distinct href **9** 条。

### 英文版 `content/tools/en/music-video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/animation-generator` | Animation Generator | tldr · article-intro | — |
| `/tools/music-generator` | Music Generator | section · what-are-ai-music-video-generators | — |
| `/tools/video-generator` | Video Generator | section · what-are-ai-music-video-generators | — |
| `/tools/text-to-speech` | Text To Speech | useCases · use-cases | — |
| `/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/tools/design` | Design | section · conclusion | — |
| `/tools/voice` | Voice | faq | — |
| `/tools/world-model` | World Model | faq | — |

**统计**：distinct href **8** 条。

---

---

## tools-video · `video`（`/tools/video`）

> **数据源**：`content/tools/zh|en/video.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/zh/tools/video-editor` | Video Editor | tldr · article-intro | — |
| `/zh/tools/text-to-video` | Text-to-Video | section · what-are-ai-video-tools | — |
| `/zh/tools/image-to-video` | Image-to-Video | section · what-are-ai-video-tools | — |
| `/zh/tools/video-to-video` | Video-to-Video | section · what-are-ai-video-tools | — |
| `/zh/tools/video-clipping` | Video Clipping | section · what-are-ai-video-tools | — |
| `/zh/tools/video-effects` | Video Effects | section · what-are-ai-video-tools | — |
| `/zh/tools/filmmaking` | Filmmaking | section · what-are-ai-video-tools | — |
| `/zh/tools/animation-generator` | Animation Generator | section · what-are-ai-video-tools | — |
| `/zh/tools/short-drama` | Short Drama | section · what-are-ai-video-tools | — |
| `/zh/tools/music-video-generator` | Music Video Generator | section · what-are-ai-video-tools | — |
| `/zh/tools/canvas-video` | Canvas Video | section · what-are-ai-video-tools | — |
| `/zh/tools/video-translator` | Video Translator | section · conclusion | — |
| `/zh/tools/lip-sync` | Lip Sync | section · conclusion | — |

**统计**：distinct href **14** 条。

### 英文版 `content/tools/en/video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/tools/video-editor` | Video Editor | tldr · article-intro | — |
| `/tools/text-to-video` | Text To Video | section · what-are-ai-video-tools | — |
| `/tools/image-to-video` | Image To Video | section · what-are-ai-video-tools | — |
| `/tools/video-to-video` | Video To Video | section · what-are-ai-video-tools | — |
| `/tools/video-clipping` | Video Clipping | section · what-are-ai-video-tools | — |
| `/tools/video-effects` | Video Effects | section · what-are-ai-video-tools | — |
| `/tools/filmmaking` | Filmmaking | section · what-are-ai-video-tools | — |
| `/tools/animation-generator` | Animation Generator | section · what-are-ai-video-tools | — |
| `/tools/short-drama` | Short Drama | section · what-are-ai-video-tools | — |
| `/tools/music-video-generator` | Music Video Generator | section · what-are-ai-video-tools | — |
| `/tools/canvas-video` | Canvas Video | section · what-are-ai-video-tools | — |
| `/tools/video-translator` | Video Translator | section · conclusion | — |
| `/tools/lip-sync` | Lip Sync | section · conclusion | — |

**统计**：distinct href **14** 条。

## tools-video-generator · `video-generator`（`/tools/video-generator`）

> **数据源**：`content/tools/zh|en/video-generator.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-clipping` | Video Clipping | tldr · article-intro | — |
| `/zh/tools/video-editor` | Video Editor | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/music-generator` | Music Generator | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/video-translator` | Video Translator | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/short-drama` | Short Drama | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/canvas-video` | Canvas Video | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/filmmaking` | Filmmaking | section · what-are-ai-video-generator-tools | — |
| `/zh/tools/text-to-video` | Text To Video | section · conclusion | — |
| `/zh/tools/image-to-video` | Image To Video | section · conclusion | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |

**统计**：distinct href **10** 条。

### 英文版 `content/tools/en/video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/music-generator` | Music Generator | tldr · article-intro | — |
| `/tools/text-to-video` | Text To Video | section · what-are-ai-video-generators | — |
| `/tools/image-to-video` | Image To Video | section · what-are-ai-video-generators | — |
| `/tools/video-editor` | Video Editor | section · what-are-ai-video-generators | — |
| `/tools/canvas-video` | Canvas Video | section · what-are-ai-video-generators | — |
| `/tools/video-to-video` | Video To Video | section · conclusion | — |

**统计**：distinct href **6** 条。

## tools-text-to-video · `text-to-video`（`/tools/text-to-video`）

> **数据源**：`content/tools/zh|en/text-to-video.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/text-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/zh/tools/video-editor` | Video Editor | tldr · article-intro | — |
| `/zh/tools/image-to-video` | Image To Video | section · what-are-ai-text-to-video-tools | — |
| `/zh/tools/world-model` | World Model | section · conclusion | — |
| `/zh/tools/video-translator` | Video Translator | section · conclusion | — |
| `/zh/tools/video-clipping` | Video Clipping | section · conclusion | — |
| `/zh/tools/story-generator` | Story Generator | section · conclusion | — |

**统计**：distinct href **7** 条。

### 英文版 `content/tools/en/text-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/tools/video-editor` | Video Editor | tldr · article-intro | — |
| `/tools/image-to-video` | Image To Video | section · what-are-ai-text-to-video-tools | — |
| `/tools/world-model` | World Model | section · conclusion | — |
| `/tools/video-clipping` | Video Clipping | section · conclusion | — |

**统计**：distinct href **5** 条。

## tools-image-to-video · `image-to-video`（`/tools/image-to-video`）

> **数据源**：`content/tools/zh|en/image-to-video.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/image-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/zh/tools/filmmaking` | Filmmaking | tldr · article-intro | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/zh/tools/video-translator` | Video Translator | faq | — |
| `/zh/tools/world-model` | World Model | faq | — |

**统计**：distinct href **5** 条。

### 英文版 `content/tools/en/image-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/tools/filmmaking` | Filmmaking | tldr · article-intro | — |
| `/tools/image-generator` | Image Generator | useCases · use-cases | — |
| `/tools/avatar` | Avatar | section · conclusion | — |
| `/tools/world-model` | World Model | section · conclusion | — |
| `/tools/video-translator` | Video Translator | section · conclusion | — |
| `/tools/video-to-video` | Video To Video | section · conclusion | — |

**统计**：distinct href **7** 条。

## tools-video-to-video · `video-to-video`（`/tools/video-to-video`）

> **数据源**：`content/tools/zh|en/video-to-video.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-clipping` | Video Clipping | tldr · article-intro | — |
| `/zh/tools/video-effects` | Video Effects | section · what-are-ai-video-to-video-tools | — |
| `/zh/tools/animation-generator` | Animation Generator | section · what-are-ai-video-to-video-tools | — |
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-video-to-video-tools | — |
| `/zh/tools/world-model` | World Model | section · conclusion | — |
| `/zh/tools/lip-sync` | Lip Sync | section · conclusion | — |
| `/zh/tools/music-video-generator` | Music Video Generator | section · conclusion | — |

**统计**：distinct href **7** 条。

### 英文版 `content/tools/en/video-to-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/music-video-generator` | Music Video Generator | tldr · article-intro | — |
| `/tools/video-effects` | Video Effects | section · what-are-ai-video-to-video-tools | — |
| `/tools/animation-generator` | Animation Generator | section · what-are-ai-video-to-video-tools | — |
| `/tools/video-generator` | Video Generator | section · what-are-ai-video-to-video-tools | — |
| `/tools/world-model` | World Model | section · conclusion | — |

**统计**：distinct href **5** 条。

## tools-video-editor · `video-editor`（`/tools/video-editor`）

> **数据源**：`content/tools/zh|en/video-editor.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video-editor.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-video-editor-tools | — |
| `/zh/tools/text-to-video` | Text To Video | section · what-are-ai-video-editor-tools | — |
| `/zh/tools/image-to-video` | Image To Video | section · what-are-ai-video-editor-tools | — |
| `/zh/tools/video-clipping` | Video Clipping | section · what-are-ai-video-editor-tools | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/zh/tools/video` | Video | section · conclusion | — |
| `/zh/tools/animation-library` | Animation Library | section · conclusion | — |
| `/zh/tools/canvas-video` | Canvas Video | section · conclusion | — |
| `/zh/tools/filmmaking` | Filmmaking | section · conclusion | — |

**统计**：distinct href **9** 条。

### 英文版 `content/tools/en/video-editor.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | section · what-are-ai-video-editors | — |
| `/tools/text-to-video` | Text To Video | section · what-are-ai-video-editors | — |
| `/tools/image-to-video` | Image To Video | section · what-are-ai-video-editors | — |
| `/tools/video-clipping` | Video Clipping | section · what-are-ai-video-editors | — |
| `/tools/canvas-video` | Canvas Video | section · conclusion | — |
| `/tools/animation-library` | Animation Library | section · conclusion | — |
| `/tools/filmmaking` | Filmmaking | section · conclusion | — |
| `/tools/music-video-generator` | Music Video Generator | section · conclusion | — |
| `/tools/animation-generator` | Animation Generator | section · conclusion | — |
| `/tools/video` | Video | section · conclusion | — |

**统计**：distinct href **10** 条。

## tools-video-clipping · `video-clipping`（`/tools/video-clipping`）

> **数据源**：`content/tools/zh|en/video-clipping.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video-clipping.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/lip-sync` | Lip Sync | tldr · article-intro | — |
| `/zh/tools/video-editor` | Video Editor | section · what-are-ai-video-clipping-tools | — |
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-video-clipping-tools | — |

**统计**：distinct href **3** 条。

### 英文版 `content/tools/en/video-clipping.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/music-generator` | Music Generator | tldr · article-intro | — |
| `/tools/video-editor` | Video Editor | section · what-are-video-clipping-tools | — |
| `/tools/video-generator` | Video Generator | section · what-are-video-clipping-tools | — |

**统计**：distinct href **3** 条。

## tools-video-effects · `video-effects`（`/tools/video-effects`）

> **数据源**：`content/tools/zh|en/video-effects.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/video-effects.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/animation-library` | Animation Library | tldr · article-intro | — |
| `/zh/tools/video-to-video` | Video To Video | section · what-are-ai-video-effects-tools | — |
| `/zh/tools/animation-generator` | Animation Generator | section · what-are-ai-video-effects-tools | — |
| `/zh/tools/video` | Video | section · conclusion | — |

**统计**：distinct href **4** 条。

### 英文版 `content/tools/en/video-effects.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video` | Video | tldr · article-intro | — |
| `/tools/video-to-video` | Video To Video | section · what-are-ai-video-effects-tools | — |
| `/tools/animation-generator` | Animation Generator | section · what-are-ai-video-effects-tools | — |
| `/tools/animation-library` | Animation Library | section · conclusion | — |

**统计**：distinct href **4** 条。

## tools-canvas-video · `canvas-video`（`/tools/canvas-video`）

> **数据源**：`content/tools/zh|en/canvas-video.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/canvas-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/documentation` | Documentation | tldr · article-intro | — |
| `/zh/tools/workflow` | Workflow | section · what-is-canvas-video | — |
| `/zh/tools/video-generator` | Video Generator | section · what-is-canvas-video | — |
| `/zh/tools/avatar` | Avatar | section · conclusion | — |
| `/zh/tools/agent-skills` | Agent Skills | section · conclusion | — |
| `/zh/tools/agent-for-desktop` | Agent For Desktop | section · conclusion | — |
| `/zh/tools/llm-for-coding` | Llm For Coding | section · conclusion | — |

**统计**：distinct href **7** 条。

### 英文版 `content/tools/en/canvas-video.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/agent-skills` | Agent Skills | tldr · article-intro | — |
| `/tools/workflow` | Workflow | section · what-is-canvas-video | — |
| `/tools/video-generator` | Video Generator | section · what-is-canvas-video | — |
| `/tools/documentation` | Documentation | section · conclusion | — |
| `/tools/avatar` | Avatar | section · conclusion | — |
| `/tools/agent-for-desktop` | Agent For Desktop | section · conclusion | — |
| `/tools/llm-for-coding` | Llm For Coding | section · conclusion | — |

**统计**：distinct href **7** 条。

## tools-filmmaking · `filmmaking`（`/tools/filmmaking`）

> **数据源**：`content/tools/zh|en/filmmaking.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/filmmaking.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/lip-sync` | Lip Sync | tldr · article-intro | — |
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-filmmaking-tools | — |
| `/zh/tools/short-drama` | Short Drama | section · what-are-ai-filmmaking-tools | — |
| `/zh/tools/video-editor` | Video Editor | section · what-are-ai-filmmaking-tools | — |
| `/zh/tools/avatar` | Avatar | section · conclusion | — |
| `/zh/tools/world-model` | World Model | section · conclusion | — |
| `/zh/tools/animation-generator` | Animation Generator | section · conclusion | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |

**统计**：distinct href **8** 条。

### 英文版 `content/tools/en/filmmaking.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/text-to-video` | Text To Video | tldr · article-intro | — |
| `/tools/video-generator` | Video Generator | section · what-are-ai-filmmaking-tools | — |
| `/tools/short-drama` | Short Drama | section · what-are-ai-filmmaking-tools | — |
| `/tools/video-editor` | Video Editor | section · what-are-ai-filmmaking-tools | — |
| `/tools/avatar` | Avatar | section · conclusion | — |
| `/tools/world-model` | World Model | section · conclusion | — |
| `/tools/animation-generator` | Animation Generator | section · conclusion | — |
| `/tools/video-to-video` | Video To Video | section · conclusion | — |

**统计**：distinct href **8** 条。

## tools-animation-generator · `animation-generator`（`/tools/animation-generator`）

> **数据源**：`content/tools/zh|en/animation-generator.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/animation-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/3d` | 3D | tldr | — |
| `/zh/tools/video-generator` | Video Generator | section · what-is-animation-generator | — |
| `/zh/tools/short-drama` | Short Drama | section · what-is-animation-generator | — |
| `/zh/tools/video-to-video` | Video To Video | section · what-is-animation-generator | — |
| `/zh/tools/video-effects` | Video Effects | section · conclusion | — |
| `/zh/tools/lip-sync` | Lip Sync | section · conclusion | — |
| `/zh/tools/image-to-video` | Image To Video | section · conclusion | — |

**统计**：distinct href **7** 条。

### 英文版 `content/tools/en/animation-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | section · what-is-animation-generator | — |
| `/tools/short-drama` | Short Drama | section · what-is-animation-generator | — |
| `/tools/video-to-video` | Video To Video | section · what-is-animation-generator | — |
| `/tools/3d` | 3D | section · conclusion | — |
| `/tools/lip-sync` | Lip Sync | section · conclusion | — |
| `/tools/video-effects` | Video Effects | section · conclusion | — |
| `/tools/image-to-video` | Image To Video | section · conclusion | — |

**统计**：distinct href **7** 条。

## tools-short-drama · `short-drama`（`/tools/short-drama`）

> **数据源**：`content/tools/zh|en/short-drama.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/short-drama.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/zh/tools/animation-generator` | Animation Generator | tldr · article-intro | — |
| `/zh/tools/llm` | Llm | section · what-are-ai-short-drama-tools | — |
| `/zh/tools/workflow` | Workflow | useCases · use-cases | — |
| `/zh/tools/api` | Api | section · conclusion-section | — |
| `/zh/tools/productivity` | Productivity | faq · faq-section | — |
| `/zh/tools/coding` | Coding | faq · faq-section | — |

**统计**：distinct href **7** 条。

### 英文版 `content/tools/en/short-drama.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/video-generator` | Video Generator | tldr · article-intro | — |
| `/tools/animation-generator` | Animation Generator | tldr · article-intro | — |
| `/tools/llm` | Llm | section · what-are-ai-short-drama-tools | — |
| `/tools/workflow` | Workflow | useCases · use-cases | — |
| `/tools/api` | Api | section · conclusion-section | — |
| `/tools/productivity` | Productivity | faq · faq-section | — |
| `/tools/coding` | Coding | faq · faq-section | — |

**统计**：distinct href **7** 条。

## tools-music-video-generator · `music-video-generator`（`/tools/music-video-generator`）

> **数据源**：`content/tools/zh|en/music-video-generator.md` · **2026-06-24** 视频簇优化。

### 中文版 `content/tools/zh/music-video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/zh/tools/design` | Design | tldr · article-intro | — |
| `/zh/tools/music-generator` | Music Generator | section · what-are-ai-music-video-generator-tools | — |
| `/zh/tools/video-generator` | Video Generator | section · what-are-ai-music-video-generator-tools | — |
| `/zh/tools/voice` | Voice | section · music-video-generation-types | — |
| `/zh/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/zh/tools/avatar` | Avatar | section · conclusion | — |
| `/zh/tools/world-model` | World Model | section · conclusion | — |
| `/zh/tools/text-to-speech` | Text To Speech | section · conclusion | — |
| `/zh/tools/animation-generator` | Animation Generator | section · conclusion | — |

**统计**：distinct href **9** 条。

### 英文版 `content/tools/en/music-video-generator.md`

| 目标路径（slug） | 锚文本 | 首次出现区块 | 阅读阶段 |
|------------------|--------|----------------|----------|
| `/tools/animation-generator` | Animation Generator | tldr · article-intro | — |
| `/tools/music-generator` | Music Generator | section · what-are-ai-music-video-generators | — |
| `/tools/video-generator` | Video Generator | section · what-are-ai-music-video-generators | — |
| `/tools/text-to-speech` | Text To Speech | useCases · use-cases | — |
| `/tools/video-to-video` | Video To Video | section · conclusion | — |
| `/tools/design` | Design | section · conclusion | — |
| `/tools/voice` | Voice | faq | — |
| `/tools/world-model` | World Model | faq | — |

**统计**：distinct href **8** 条。

---

## 文档修订

| 2026-06-23 | 附录：**`tools-memory`** 重写内链表（PKM/第二大脑；Agent 中间件改链 `/blog/agent-memory`）。

| 日期 | 说明 |
|------|------|
| 2026-08-27 | **SSOT 合并**：Marketing M1–M11 迁入 Part 4.5；FAQ **允许**内链、**计入正文**、R4 全文 1 次；`marketing-internal-links.md` / `rules-quickref.md` 改为跳转 stub；Part 1 §七–§十一 执行流程指向 `optimize-internal-links/workflow.md` |
| 2026-06-23 | 附录 B：新增 **`multi-agent`**（`/blog/`）；`agent-skills`、`agent-for-desktop`、`openclaw-alternatives` 邻居增 multi-agent。附录 C：新增 **§blog-multi-agent**（正文各 6 + FAQ 各 2）。知识块 `knowledge/tools/agent/multi-agent.md` + 部署仓 `content/blog/{en|zh}/multi-agent.md`。 |
| 2026-06-23 | 附录 B/C：新增 **`agent-memory`**（`/blog/`）；`agent-skills`、`memory` 邻居增 agent-memory。
| 2026-06-23 | 附录 B：新增 **`agent-sandbox`**（`/blog/`）；`agent-skills`、`agent-for-desktop` 邻居增 agent-sandbox。附录 C：新增 **§blog-agent-sandbox**（正文各 5 + FAQ 各 3，共 8 distinct href）。规范：`create-tools-article` / `section-faq` 统一允许 Tools/Blog JSON FAQ 内链。 |
| 2026-06-23 | 附录 B：新增 **`medical-scribe`**、**`healthcare`**（`/blog/` / `/tools/`）；`web-fetch` 行指向 §blog-web-fetch。附录 C：新增 **§blog-medical-scribe**（正文各 2 条）、**§blog-web-fetch**（正文各 3 条），FAQ 均无站内链。 |
| 2026-06-23 | 附录 B：新增 **`ai-training-data`**（`/blog/`）；`web-scraping` 邻居增 ai-training-data。附录 C：新增 **§blog-ai-training-data** 中英内链台账（正文各 5 条，FAQ 无站内链）。 |
| 2026-05-20 | 附录 C：**全量刷新** — 由脚本从 23 个试点 slug 的实际 JSON 文件自动扫描生成，替换此前手动维护的过时版本（EN/ZH 计数与锚文本均来自当前 `content/tools/` 文件）。 |
| 2026-04-29 | 附录 C：新增 **§20–§23** 垂类 LLM（`llm-for-coding`、`llm-for-math`、`multimodal-llm`、`llm-for-reasoning`）中英内链台账；`content/tools/zh|en` 四页 JSON 扩写（英文叙事 2000+ words、`bestTools` 与对比表未改序）；附录数据源与 §19 试点说明同步。 |
| 2026-04-29 | 附录 C：新增 §19 **`llm`** 中英内链台账（正文 16–17 + FAQ 3）；`content/tools/zh|en/llm.md` 扩写榜单/检索方法论、英文 2000+ words、内链与 §1.5 对齐。 |
| 2026-04-28 | 附录 B：`character-chat`；附录 C：新增 §18 `character-chat` 中英台账（正文 16 + FAQ 3，`TL;DR` ≤2）；`content/tools/zh|en/character-chat.md` 扩写与 knowledgehub 对齐。 |
| 2026-04-28 | **`openclaw-alternatives` 产品线修订**：移除 Tencent QClaw；五个产品外链统一 `utm_source=kostja&utm_medium=blog`（与 linkedin/authentication 等 Tools 一致）；`public/tools/openclaw-alternatives/` 替换为实拍产品图；`knowledge/tools/agent/openclaw-alternatives.md` 与之对齐。 |
| 2026-04-28 | 附录 B：`openclaw-alternatives`；附录 C：新增 §17 `openclaw-alternatives` 中英台账（TL;DR 2、`agent-for-desktop` 不重复于「什么是」、正文 12 + FAQ 3）；`content/tools` 数据源与 `alignify-keywords-tools` 更新。 |
| 2026-04-28 | 附录 B：`agent-for-desktop`；附录 C：新增 §16 `agent-for-desktop` 中英台账（正文 18 + FAQ 3，`TL;DR` ≤2 条 Tools 链）；`alignify-keywords-tools` 增支柱行与 `#agent-for-desktop-tools`。 |
| 2026-04-24 | 附录 C 未改 slug 台账：`web-scraping`、`headless-browser`、`linkedin`、`geo`、`code-review`、`agent-skills`、`documentation`、`authentication` 等文将原 TLDR 后「弱化 html 岛」并入 `tldr`/`section`；内链首次出现位置与表一致者维持不变；`documentation` 中文版 TL;DR 不再重复放 `geo`/`web-search-api` 的 `<a>`（保留对比表 `introHtml` 唯一定位）。 |
| 2026-04-24 | 清理英文 Tools JSON 中误合并的 `Additional detail` 碎片段落；补全 `en/documentation` TL;DR 截断句；不改动附录 slug 行。 |
| 2026-04-21 | 附录 C：新增 §15 `linkedin` 中英内链台账（正文 6 + FAQ 3，1 条 FAQ 双链 presentation-maker / productivity） |
| 2026-04-19 | 初版：Tools 拓扑专册；迁入原 section-links「四、产品链接验证与优化（Tools 页面）」；§1.5 内链均衡分布与「提高频率」释义 |
| 2026-04-19 | §1.5 改为「整篇阅读顺序」分布；TLDR/什么是/FAQ（Tools JSON 例外）规则；§三、§四与表格同步 |
| 2026-04-19 | 将原 `tools-neighbor-links`、`tools-articles-internal-link-inventory` 并入为附录 B、附录 C |
| 2026-04-19 | 附录 C：初版 inventory（锚文本三列）；§3 `headshot-generator` 中英内链表 |
| 2026-04-19 | 附录 C：对齐 Avatar / Background / Headshot 改稿；增「阅读阶段」列；FAQ 纳入表 |
| 2026-04-20 | 附录 C：§1.5 锚点与 section-consistency 文档修订同步（无 href 变更） |
| 2026-04-19 | 附录 C：§4 `legal` 相邻 tools 内链 |
| 2026-04-19 | 附录 C：§5 `geo` 中英扩写 + 内链 17 个不同 slug |
| 2026-04-21 | 附录 B：`search-engine`、`web-search-api` 邻居；附录 C：新增 §7 `web-search-api` 中英台账与互链建议 |
| 2026-04-22 | 附录 C §7：`web-search-api` 改版（TLDR 链 `search-engine`、增 `useCases`、FAQ 链 `evaluation`/`browser`、移除 Related） |
| 2026-04-21 | 附录 B：`agent-skills` 邻居摘要；附录 C：新增 §10 `agent-skills` 中英内链台账（18+3） |
| 2026-04-20 | 附录 C：新增 §8 `search-engine` 中英内链台账（browser / web-search-api / evaluation / geo / llm） |
| 2026-04-22 | 附录 B：`code-review` 邻居摘要；附录 C：新增 §9 `code-review` 中英内链台账（9+3） |
| 2026-04-22 | 附录 B：`web-scraping` 邻居；附录 C：新增 §11 `web-scraping` 中英台账（6 含 SEO 跨链）；正文去重 `web-search-api`、增 `llm`/`workflow` |
| 2026-04-21 | 附录 B：`documentation` 邻居；附录 C：新增 §12 `documentation` 中英台账（20+3）；references 仅 a16z 播客外链 |
| 2026-04-22 | 附录 B：`headless-browser` 邻居；附录 C：新增 §13 `headless-browser` 中英台账（15+3）；TLDR 仅 2 条 Tools 链，FAQ 与正文去重 |
| 2026-04-21 | 附录 B：`authentication` 邻居；附录 C：新增 §14 `authentication` 中英台账（15+3）；hero 链 `documentation` 不计入 blocks 内链 |

---

<a id="part-4-seo-频道内链"></a>

# Part 4 · SEO 频道内链

> **站点**：[alignify.co](https://alignify.co) · **关联**：[section-links.md](./internal-links.md)（全站规则）· [templates.md](./templates.md) · `alignify-keywords.md` · `src/data/site-pages-config.ts` · `alignify-keywords-seo.md`  
> **同目录**：本文 Part 3（Tools JSON）· 本文 Part 5（其余页面索引）

**用途**：**`content/seo/en|zh/*.{md,json}`**（BlogLayout）之间的推荐链接拓扑，及与 Marketing / Tools 的**节制**跨链。全站唯一性、锚文本、样式仍以 `section-links` 为准。

---

## 一、框架：SEO × 用户意图 × 链接拓扑

| 维度 | 目标 | Alignify SEO 指南落地 |
|------|------|------------------------|
| **SEO（站内）** | 减少主题孤岛、锚文本描述目标页、层级清晰 | 支柱页与长尾指南互链；`BreadcrumbNav` 回 SEO 频道 |
| **用户** | 读完「是什么」后能进入「怎么做 / 下一步检查」 | 以**整篇阅读顺序**分布内链（见 §1.5）；「什么是」段可含 **1～2** 个强相关 `/seo/...` 链，与 TLDR **去重** |
| **与 Tools 的差异** | Tools 以 `/tools/[slug]` 为主 | 本类以 **`/seo/[slug]`** 为主；链向 `/tools/...` 或 `/marketing/...` 仅当**同一工作流**需要（见 §五），细则与 FAQ 例外见 本文 §3.1.5 / §3.4 |

### 1.1 纵向：聚合 ↔ 详情（Hub / Spoke）

| 方向 | 典型意图 | 做法 |
|------|----------|------|
| **聚合 → 详情** | 从 SEO 学习入口进入专题 | `/seo/learn-seo`（及中文对应页）在正文中链向具体指南（如 `/seo/sitemap`、`/seo/robots-txt`）；站点导航「SEO」下拉已列主要 spoke |
| **详情 → 聚合** | 回到总览换主题 | 面包屑、页脚频道；结论段可收束 **0–2** 条「下一步必读」链（须全文唯一；见 [`sections.md`](./sections.md) Part 4.4） |

### 1.2 横向：同一工作流互补（Peer）

| 场景 | 做法 |
|------|------|
| **技术流水线** | 爬取与可访问性 → 索引与规范化 → 站点地图与内链（例：`/seo/crawler` ↔ `/seo/website-indexing` ↔ `/seo/sitemap` ↔ `/seo/internal-links`） |
| **how ↔ crawler** | `/seo/how-search-engine-works` 讲三阶段与索引/呈现；`/seo/crawler` 讲访问者谱系与治理；全文 `href` 各页仅出现一次，避免两文重复长教程 |
| **On-page 集群** | Title/Meta、HTML 语义、Schema 互链（见 `alignify-keywords.md` 技术行表） |
| **易混分流** | 经典 **Web SEO** 与 **GEO/AEO** 分册：长文 GEO 以 `/marketing/geo`、`/tools/geo` 为主入口；`/seo/...` 侧重搜索引擎与站点技术 |

### 1.3 固定区块 vs 上下文内链

| 类型 | Alignify 中的体现 |
|------|-------------------|
| **固定区块** | `Header` / `Footer` / `BreadcrumbNav`；SEO JSON 文章**无** Tools 页的 **AlsoInterestedIn** 四卡组件 |
| **上下文内链** | `content/seo/*/*.md` 内 **`section` 的 `paragraphs`（支持 HTML 字符串）**、`comparisonSection` 的 **`introHtml`**、`html` 块、结论 HTML 等中的 `<a href="/seo/...">` 或 `<a href="/zh/seo/...">`（须遵守 [section-links](./internal-links.md) 唯一性与 §1.5） |

### 1.4 基础原则（与全站 section-links 对齐）

| 原则 | SEO 指南执行要点 |
|------|------------------|
| **避免孤立页** | 新 `/seo/[slug]` 上线后应写入 `site-pages-config`、进入 sitemap 管线；并在至少 **1～2** 篇相关指南正文中被语义化链入 |
| **锚文本** | 用目标页主题短语（中/英与目标页 H1 或 keywords 表对齐）；忌「点击这里」「本页」 |
| **同一 URL 单页仅出现一次** | 含 FAQ 在内全文去重（见 §四） |
| **跨语言** | 英文用 `/seo/...`，中文用 `/zh/seo/...`；勿混用 |

### 1.5 SEO 文章内链均衡分布（整篇阅读顺序 + 不同 URL）

在遵守 **同一站内路径全文仅出现一次** 的前提下，以 **`blocks` 自上而下** 与**约前 25% 篇幅**为主轴分配内链；**不以「每个 H2 凑满 N 条」为硬指标**。在「distinct URL + 阅读顺序」上与 本文 §3.1.5 对齐；**本类 FAQ 答案仍为纯文本**（与 Tools JSON FAQ 可链不同）。

| 维度 | 建议 |
|------|------|
| **主轴** | TLDR 的 `items` 一般为**纯文本**（无 `<a>`）；若必须在 TLDR `introduction` 内链，**≤1** 条且与后文去重 |
| **什么是 · 末段或第二段** | **1～2** 条强相关 `/seo/...` 链；与 [`sections.md`](./sections.md) Part 3.1 及 [`templates.md`](./templates.md) Part 4 一致 |
| **正文中部** | `comparisonSection.introHtml`、`html`、`section` 长段落承担 **多数** distinct `/seo/...` URL；**同一 H2 内**建议 **≤3** 条不同站内链，避免单屏链接堆叠 |
| **结论** | **0–2** 条 distinct（见 [`sections.md`](./sections.md) Part 4.4）；常与「网站结构 / 站点地图 / 内链」等收束组合；**不得**与上文重复同一 `href` |
| **FAQ** | **允许**答案内链；**计入正文**；同 URL 全文 1 次（见 [§1.5](#15-faq-内链规则)） |
| **试点 href 台账** | 见本文 **附录 B**；新增试点时在附录 B 追加章节 |

### 1.6 学习 / 资源类页面的内链节制（主题紧约束）

适用于「学 SEO」「资源列表」「导读」等**非执行清单**正文：站内链以**少而准**为原则，与 §1.5「分布均衡」不矛盾——**distinct URL 总数可以很少**，只要每条都直接服务本页主任务。

| 原则 | 说明 |
|------|------|
| **先修叙事优先** | 例如 `learn-seo`：用 **1** 条先修文（如「搜索引擎如何工作」）建立爬取—索引—呈现心智模型即可，不必再链 Checklist 或整站技术 spoke 堆满屏。 |
| **承接段内例子** | 仅当句子**明确写到**某类问题时再链对应指南（如「不收录」检索示例下链「网站索引与收录排查」），避免「能链就链」。 |
| **执行向 spoke 外置** | 爬虫、sitemap、schema 等深度实操更适合在 Checklist、`how-search-engine-works` 收束段或各专题指南中互链；**不要**在导读页为 Hub 完整性凑数。 |
| **跨频道** | 与 §五 一致；学习导读若无同一用户任务，**可不**链 Marketing / Tools。 |

---

## 二、URL 模式（SEO 指南）

| 语言 | 模式 | 示例 |
|------|------|------|
| 英文 | `/seo/[slug]` | `/seo/internal-links` |
| 中文 | `/zh/seo/[slug]` | `/zh/seo/internal-links` |

**Marketing / Tools**（跨频道）：

| 频道 | 模式 | 示例 |
|------|------|------|
| Marketing | `/marketing/[slug]` | `/marketing/geo` |
| Tools | `/tools/[slug]` | `/tools/geo` |

**hreflang** 与规范 URL 见 `alignify-keywords.md` 及页面 `page.tsx` 内 metadata。

---

## 三、全站组件与 SEO 页相关的内链位

汇总自 [section-links §三](./internal-links.md#三全站链接使用场景汇总)；SEO JSON 编辑需重点核对：

| 组件 | 说明 |
|------|------|
| **BreadcrumbNav** | 回「SEO」频道上级 |
| **Header / Footer** | 频道入口；非正文计数范围 |
| **JSON 内 `<a>`** | 站内相对路径 + `class="text-primary hover:underline"` |
| **faq-data.json** | 仅纯文本答案；不放站内链 |

---

## 四、正文与 JSON：内链放哪里

| 位置 | 规则 |
|------|------|
| **什么是 · 段落** | 可在字符串中内嵌 HTML `<a>`；**1～2** 条强相关链，与 TLDR 去重 |
| **comparisonSection · introHtml** | 适合承担清单型章节的主体说明 + 分散内链（参见附录 B checklist） |
| **html 块** | 长教程、多 H3、列表；注意唯一性 |
| **结论** | 可含 **0–2** 条收束链；遵守 [`sections.md`](./sections.md) Part 4.4 |
| **FAQ** | **允许**答案内链；**计入正文**；同 URL 全文 1 次 |
| **References** | 若有，以外链权威源为主；站内链不重复计数为「正文内链」 |

---

## 五、与 Marketing / Tools 的跨频道链（节制）

| 场景 | 建议 |
|------|------|
| **同一用户任务** | 如 checklist 中「实施模块」同时需要 GEO 策略与工具聚合：链 `/marketing/geo`、`/tools/geo` **各最多一次** |
| **避免引流堆砌** | 单篇 SEO 指南全文 distinct 的 **非 `/seo` 路径**建议 **≤3～4**，且须有上文语义支撑 |
| **关键词权威** | 主题与 slug 映射仍以 `alignify-keywords.md` 为准 |

---

## 六、维护与抽检

| 项 | 说明 |
|----|------|
| **新 SEO slug** | 更新 `src/data/site-pages-config.ts`、sitemap 相关管线（见 [technical-sitemap.md](../../ops/sitemap.md)）、`content/seo/en|zh` 成对文件（若站点多语言） |
| **改内链** | 先跑全文 **href 唯一**检查；同步更新 **附录 B**（试点页） |
| **单页抽检** | [section-links 检查清单](./internal-links.md) + 本节 §1.5 + [`templates.md`](./templates.md) Part 4 字数与 FAQ 条数 |

---

## 附录 A：`introHtml` 内链片段示例（英文路径）

便于复制到 `content/seo/en/*.md`（注意 JSON 内引号转义）：

```html
<p class="text-base md:text-lg leading-relaxed">Pair Search Console with <a href="/seo/website-traffic" class="text-primary hover:underline">traffic and channel reporting</a> so technical fixes and content launches share one dashboard story.</p>
```

中文路径将 `href` 改为 `/zh/seo/...` 即可。

---

## 附录 B：试点页正文内链对照（`checklist`）

> **用途**：记录 `content/seo/en|zh/checklist.md` 中 **全文唯一**的站内 `href`（分布原则见上文 §1.5；全站唯一性见 [section-links §1.1](./internal-links.md#11-唯一性与分布)），便于改版时核对 **href → 锚文本 → 区块**。  
> **不含**：`pageUrl`、`BlogLayout` 元信息；FAQ 答案内链见 [§1.5](#15-faq-内链规则)。  
> **维护**：修改 checklist JSON 内链后，**请同步更新本附录**；新增其他 SEO JSON 试点页可追加章节。

### B.1 SEO Checklist（英文 `content/seo/en/checklist.md`）

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/seo/learn-seo` | how SEO learning paths map to execution | What is · 第 3 段 |
| `/seo/how-search-engine-works` | search engine mechanics | What is · 第 3 段 |
| `/seo/google-tag-manager` | Google Tag Manager | 1. Tracking Setup · introHtml |
| `/seo/website-traffic` | traffic and channel reporting | 1. Tracking Setup · introHtml |
| `/seo/robots-txt` | robots.txt | 2. Technical SEO · introHtml |
| `/seo/url-optimization` | URL optimization | 2. Technical SEO · introHtml |
| `/seo/redirect-chain` | redirect chains | 2. Technical SEO · introHtml |
| `/seo/website-rendering` | rendering | 2. Technical SEO · introHtml |
| `/seo/website-indexing` | Indexing | 2. Technical SEO · introHtml |
| `/seo/crawler` | crawler fundamentals | 2. Technical SEO · introHtml |
| `/seo/schema` | structured data | 3. On-Page & Content · introHtml |
| `/seo/meta-tag` | meta tags | 3. On-Page & Content · introHtml |
| `/seo/html-tag` | semantic HTML | 3. On-Page & Content · introHtml |
| `/seo/link-building` | link-building | 4. Link Building & CTR · introHtml |
| `/seo/external-links` | outbound links | 4. Link Building & CTR · introHtml |
| `/seo/serp` | SERP | 4. Link Building & CTR · introHtml |
| `/seo/create-blog` | blog content | 5. Content Updates · introHtml |
| `/seo/programmatic-seo` | programmatic SEO | 5. Content Updates · introHtml |
| `/seo/landing-page` | landing page SEO | 6. SEO Content Modules · introHtml |
| `/seo/category-pages` | category page | 6. SEO Content Modules · introHtml |
| `/seo/submit-website` | submit the site | 7. Implementation Modules · introHtml |
| `/marketing/geo` | GEO playbook | 7. Implementation Modules · introHtml |
| `/tools/geo` | GEO tools hub | 7. Implementation Modules · introHtml |
| `/seo/subdomain-vs-subfolder` | subdomain vs subfolder | 7. Implementation Modules · introHtml |
| `/seo/website-structure` | website structure | Conclusion · html |
| `/seo/sitemap` | sitemap | Conclusion · html |
| `/seo/internal-links` | internal links | Conclusion · html |

**统计**：上表共 **27** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次。

### B.2 SEO Checklist（中文 `content/seo/zh/checklist.md`）

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/seo/learn-seo` | SEO 学习路径 | 什么是 · 第 3 段 |
| `/zh/seo/how-search-engine-works` | 搜索引擎如何工作 | 什么是 · 第 3 段 |
| `/zh/seo/google-tag-manager` | Google Tag Manager | 一、Tracking · introHtml |
| `/zh/seo/website-traffic` | 流量与渠道报表 | 一、Tracking · introHtml |
| `/zh/seo/robots-txt` | robots.txt | 二、技术 SEO · introHtml |
| `/zh/seo/url-optimization` | URL 优化 | 二、技术 SEO · introHtml |
| `/zh/seo/redirect-chain` | 重定向链 | 二、技术 SEO · introHtml |
| `/zh/seo/website-rendering` | 渲染与抓取 | 二、技术 SEO · introHtml |
| `/zh/seo/website-indexing` | 网站索引 | 二、技术 SEO · introHtml |
| `/zh/seo/crawler` | 爬虫基础 | 二、技术 SEO · introHtml |
| `/zh/seo/schema` | 结构化数据 | 三、On-Page · introHtml |
| `/zh/seo/meta-tag` | meta 标签 | 三、On-Page · introHtml |
| `/zh/seo/html-tag` | 语义化 HTML | 三、On-Page · introHtml |
| `/zh/seo/link-building` | 外链建设 | 四、链接与 CTR · introHtml |
| `/zh/seo/external-links` | 出站链接 | 四、链接与 CTR · introHtml |
| `/zh/seo/serp` | SERP | 四、链接与 CTR · introHtml |
| `/zh/seo/create-blog` | 博客内容 | 五、内容更新 · introHtml |
| `/zh/seo/programmatic-seo` | 程序化 SEO | 五、内容更新 · introHtml |
| `/zh/seo/landing-page` | 着陆页 SEO | 六、内容模块 · introHtml |
| `/zh/seo/category-pages` | 分类页 | 六、内容模块 · introHtml |
| `/zh/seo/submit-website` | 提交网站 | 七、实施待办 · introHtml |
| `/zh/marketing/geo` | GEO 策略长文 | 七、实施待办 · introHtml |
| `/zh/tools/geo` | GEO 工具聚合 | 七、实施待办 · introHtml |
| `/zh/seo/subdomain-vs-subfolder` | 子域与子目录 | 七、实施待办 · introHtml |
| `/zh/marketing/keyword-research` | 关键词研究 | 七、实施待办 · introHtml |
| `/zh/seo/website-structure` | 网站结构 | 结论 · html |
| `/zh/seo/sitemap` | 站点地图 | 结论 · html |
| `/zh/seo/internal-links` | 内部链接 | 结论 · html |

**统计**：上表共 **28** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次（已移除失效的 `competitive-analysis` 类路径，结论段不再与第六节重复 `website-structure`）。

### B.3 How search engines work（英文 `content/seo/en/how-search-engine-works.md`）

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/seo/website-indexing` | website indexing diagnostics | Official stages · §3 |
| `/seo/serp` | SERP overview | Official stages · §3 |
| `/seo/learn-seo` | SEO learning resources | Search Engine Basics · 第 1 段 |
| `/seo/sitemap` | XML sitemap | Build index · URLs |
| `/seo/robots-txt` | robots.txt guide | Build index · Crawling |
| `/seo/crawler` | crawler guide | Build index · Crawling |
| `/seo/website-rendering` | rendering and crawl notes | Build index · Processing |
| `/seo/url-optimization` | URL optimization | Build index · Indexing |
| `/tools/search-indexing` | Search Indexing Tools | Build index · Push vs Pull |
| `/seo/link-building` | link building | Rank · Backlinks |
| `/seo/meta-tag` | meta tags and SERP presentation | Rank · Relevance |
| `/seo/subdomain-vs-subfolder` | subdomain vs subfolder | Personalize · Language |
| `/seo/schema` | structured data | Technical · §1 |
| `/seo/html-tag` | semantic HTML | Technical · §1 |
| `/tools/web-search-api` | AI search surfaces | Technical · GEO |
| `/seo/website-structure` | site structure | Technical · GEO |
| `/seo/internal-links` | internal links | Technical · GEO |
| `/seo/submit-website` | submit your site to search engines | Technical · GEO |
| `/seo/checklist` | SEO checklist | Technical · 收束 |
| `/glossary` | SEO glossary | Technical · 收束 |

**统计**：上表共 **20** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。结论段不再重复正文已出现的 `/seo/website-indexing` 与 `/seo/checklist`。

### B.4 How search engines work（中文 `content/seo/zh/how-search-engine-works.md`）

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/seo/website-indexing` | 网站索引与收录排查 | Google 阶段与边界 · §3 |
| `/zh/seo/serp` | SERP 与搜索结果形态 | Google 阶段与边界 · §3 |
| `/zh/seo/learn-seo` | SEO 学习资源 | 什么是搜索引擎 · 第 2 段 |
| `/zh/seo/sitemap` | XML 站点地图（sitemap） | 构建索引 · URLs |
| `/zh/seo/robots-txt` | robots.txt 指南 | 构建索引 · Crawling |
| `/zh/seo/crawler` | 网络爬虫指南 | 构建索引 · Crawling |
| `/zh/seo/website-rendering` | 网站渲染与抓取 | 构建索引 · Processing |
| `/zh/seo/url-optimization` | URL 优化 | 构建索引 · Indexing |
| `/zh/tools/search-indexing` | 搜索引擎索引工具 | 构建索引 · Push vs Pull |
| `/zh/seo/link-building` | 外链建设 | 排名 · 外链 |
| `/zh/seo/meta-tag` | meta 标签与搜索展示 | 排名 · 相关性 |
| `/zh/seo/subdomain-vs-subfolder` | 子域还是子目录 | 个性化 · 语言 |
| `/zh/seo/schema` | 结构化数据 | 技术 SEO · §1 |
| `/zh/seo/html-tag` | 语义化 HTML 与核心标签 | 技术 SEO · §1 |
| `/zh/tools/web-search-api` | AI 搜索入口 | 技术 SEO · GEO |
| `/zh/seo/website-structure` | 网站结构 | 技术 SEO · GEO |
| `/zh/seo/internal-links` | 内部链接 | 技术 SEO · GEO |
| `/zh/seo/submit-website` | 提交网站与 URL 到搜索引擎 | 技术 SEO · GEO |
| `/zh/seo/checklist` | SEO Checklist | 技术 SEO · 收束 |
| `/zh/glossary` | SEO 词汇表 | 技术 SEO · 收束 |

**统计**：上表共 **20** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。结论段不再重复正文已出现的 `/zh/seo/website-indexing` 与 `/zh/seo/checklist`。

### B.5 Web crawler（英文 `content/seo/en/crawler.md`）

> **定位**：爬虫谱系与治理；**流水线教程**仅通过 Introduction 链向 `how-search-engine-works`，全文 `href` 仅出现一次；**Tools 数据采集**链 `web-scraping`；结论段收束 **indexing / sitemap / robots / internal-links** 四 spoke。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/seo/how-search-engine-works` | complete guide on how search engines work | Introduction · 第 4 段 |
| `/tools/geo` | GEO / AEO | Introduction · 第 4 段 |
| `/tools/web-scraping` | Web Scraping Tools | Introduction · 第 5 段 |
| `/seo/website-traffic` | complete guide on website traffic management | Bot Traffic Management · html |
| `/seo/website-indexing` | website indexing | Conclusion · 第 3 段 |
| `/seo/sitemap` | XML sitemaps | Conclusion · 第 3 段 |
| `/seo/robots-txt` | robots.txt | Conclusion · 第 3 段 |
| `/seo/internal-links` | internal links | Conclusion · 第 3 段 |

**统计**：上表共 **8** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。TLDR `introduction` 无 `<a>`（导读内链见 Introduction 段与过渡 html）。

### B.6 Web crawler（中文 `content/seo/zh/crawler.md`）

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/seo/how-search-engine-works` | 搜索引擎如何工作完整指南 | 爬取与抓取后过渡段 · html |
| `/zh/tools/geo` | GEO / AEO | 同上 |
| `/zh/tools/web-scraping` | 网页抓取工具 | 同上 |
| `/zh/seo/website-traffic` | 网站流量管理完整指南 | Bot 流量管理 · html |
| `/zh/seo/website-indexing` | 网站收录 | Conclusion · 第 3 段 |
| `/zh/seo/sitemap` | 站点地图 | Conclusion · 第 3 段 |
| `/zh/seo/robots-txt` | robots.txt | Conclusion · 第 3 段 |
| `/zh/seo/internal-links` | 内链策略 | Conclusion · 第 3 段 |

**统计**：上表共 **8** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。TLDR `introduction` 无 `<a>`。

### B.7 Learn SEO（中文 `content/seo/zh/learn-seo.md`）

> **主题紧约束**：本页为学习导读；正文站内链仅保留「先修概念」「术语检索」「段内示例直链」。详见 **§1.6**。**阅读顺序**：`blocks` 自上而下为「介绍 → 官方锚点与课程 → 用谷歌自学 → 资源列表（**中文 JSON** 将中文资源置于英文资源之前）→ 纸质书 → 专家 → 干中学 → FAQ」；英文 JSON 将英文资源置于中文资源之前。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/seo/how-search-engine-works` | 搜索引擎如何工作 | 介绍:为什么学习SEO · 第 3 段 |
| `/zh/glossary` | SEO概念或问题的英文术语 | 用好谷歌搜索学习SEO · 第 2 段 |
| `/zh/seo/website-indexing` | 网站索引与收录排查 | 用好谷歌搜索学习SEO · 第 2 段 |
| `/` | Alignify | 学习SEO的中文网站 · childrenHtml |

**统计**：上表共 **4** 条站内路径（含首页 `/`）；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

### B.8 Learn SEO（英文 `content/seo/en/learn-seo.md`）

> **主题紧约束**：同上；详见 **§1.6**。`blocks` 顺序与 B.7 对称（中英互逆：B.7 中文资源先于英文资源，B.8 英文资源先于中文资源）。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/seo/how-search-engine-works` | how search engines work | Introduction: Why Learn SEO · 第 3 段 |
| `/glossary` | SEO concepts or English terminology | Using Google Search Effectively · 第 2 段 |
| `/seo/website-indexing` | website indexing guide | Using Google Search Effectively · 第 2 段 |
| `/` | Alignify | Chinese SEO Learning Resources · childrenHtml |

**统计**：上表共 **4** 条站内路径（含首页 `/`）；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

### B.9 Search engines landscape（英文 `content/seo/en/search-engine.md`）

> **定位**：全球/区域搜索引擎盘点 + AI 与 Web Search API；**正文**以 `/seo/...` 收束学习/执行，**跨频道**保留浏览器、AI 搜索产品、GEO 策略、Web Search API 各 **1** 次；**移除**弱相关 Insights 链；**FAQ 无 `<a>`**。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/tools/browser` | browsers | What Are Search Engines · 第 1 段 |
| `/tools/search-engine` | AI search engines | What Are Search Engines · 第 2 段 |
| `/seo/how-search-engine-works` | search engine technical guide | What Are Search Engines · 第 2 段 |
| `/glossary` | SEO glossary | Search Engine Comparison Table · 表前说明 |
| `/seo/serp` | SERP | Search Engine Comparison Table · 表后解读 · 第 1 段 |
| `/seo/website-indexing` | indexing diagnostics | Search Engine Comparison Table · 表后解读 · 第 1 段 |
| `/marketing/geo` | GEO (generative engine optimization) | AI Search Engines · html |
| `/tools/web-search-api` | Web Search API — providers, selection, and RAG integration | Web Search APIs · html |
| `/seo/schema` | Schema.org structured data | Future Trends · 第 2 段 |
| `/seo/checklist` | SEO checklist | Conclusion · 第 2 段 |
| `/seo/learn-seo` | SEO learning resources | Conclusion · 第 2 段 |
| `/seo/website-traffic` | traffic and channel reporting | Conclusion · 第 2 段 |

**统计**：上表共 **12** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

### B.10 Search engines landscape（中文 `content/seo/zh/search-engine.md`）

> **定位**：与 B.7 对称；GEO 链 **Marketing** `/zh/marketing/geo`；**FAQ** 中关于 Web Search API 的答案为**纯文本**（正文「Web Search API」节已链 Tools 专页）。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/tools/browser` | 浏览器 | 什么是搜索引擎 · 第 1 段 |
| `/zh/tools/search-engine` | AI搜索引擎 | 什么是搜索引擎 · 第 2 段 |
| `/zh/seo/how-search-engine-works` | 搜索引擎技术详解指南 | 什么是搜索引擎 · 第 3 段 |
| `/zh/glossary` | 词汇表 | 搜索引擎对比表 · 表前说明 |
| `/zh/seo/serp` | SERP 与搜索结果形态 | 搜索引擎对比表 · 表后解读 · 第 1 段 |
| `/zh/seo/website-indexing` | 网站索引与收录排查 | 搜索引擎对比表 · 表后解读 · 第 1 段 |
| `/zh/marketing/geo` | GEO（生成式引擎优化） | AI搜索引擎 · html |
| `/zh/tools/web-search-api` | Web Search API · 选型与接入指南 | Web Search API · html |
| `/zh/seo/schema` | Schema.org 结构化数据 | 搜索引擎未来趋势 · 第 2 段 |
| `/zh/seo/checklist` | SEO Checklist | 结论 · 第 2 段 |
| `/zh/seo/learn-seo` | SEO 学习资源 | 结论 · 第 2 段 |
| `/zh/seo/website-traffic` | 流量与渠道报表 | 结论 · 第 2 段 |

**统计**：上表共 **12** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

### B.11 Best SEO tools 指南（英文 `content/seo/en/best-tools.md`）

> **定位**：工具栈盘点（免费官方层 → 叠栈顺序 → 套件 → 排名与内容 → 单点工具 → 插件 → 桌面爬虫 → 企业日志 → 本地商户 → AI/GEO → 社媒）；**跨频道** `/marketing/geo`、`/tools/geo`、`/tools/text` 各 **1** 次；企业级与本地商户节**无**正文站内链（英文与「索引」指南的链已在免费清单出现，避免重复）。**FAQ 无 `<a>`**。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/seo/how-search-engine-works` | how search engines crawl, index, and rank | What are SEO tools · 第 1 段 |
| `/seo/learn-seo` | SEO learning resources | What are SEO tools · 第 1 段 |
| `/seo/website-indexing` | indexing and coverage | Free essentials · 列表 · GSC |
| `/seo/website-traffic` | traffic and channel reporting | Free essentials · 列表 · GA4 |
| `/seo/schema` | structured data (Schema.org) | Free essentials · 列表 · Rich Results |
| `/seo/website-structure` | site structure | Stack order · 第 2 段 |
| `/seo/checklist` | SEO checklist | Stack order · 第 3 段 |
| `/seo/link-building` | link building | All-in-one platforms · 引言 |
| `/seo/serp` | SERP | Rank tracking · 第 2 段 |
| `/seo/create-blog` | blog and content hubs | Content optimization · 第 1 段 |
| `/seo/meta-tag` | title tags and meta descriptions | Content optimization · 第 2 段 |
| `/seo/crawler` | crawler behavior | Single-function free tools · 引言 |
| `/seo/internal-links` | internal links | Browser extensions · 引言 |
| `/seo/url-optimization` | URL and canonical strategy | Desktop crawlers · 引言 |
| `/tools/text` | AI writing tools hub | AI / GEO · AirOps |
| `/marketing/geo` | GEO playbook | AI / GEO · GEO 小节 |
| `/tools/geo` | GEO tools hub | AI / GEO · GEO 小节 |
| `/glossary` | SEO glossary | Conclusion · 第 2 段 |

**统计**：上表共 **18** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

### B.12 Best SEO tools 指南（中文 `content/seo/zh/best-tools.md`）

> **定位**：与 B.11 对称；**企业级云爬**段仅用纯文字提 Search Console 覆盖报告，**不**重复链 `/zh/seo/website-indexing`（已在「免费必选项」链过）。**FAQ 无 `<a>`**。

| 目标路径 | 锚文本（可见文案） | 首次出现区块 |
|----------|-------------------|--------------|
| `/zh/seo/how-search-engine-works` | 搜索引擎如何抓取、索引与排序 | 什么是 SEO 工具 · 第 1 段 |
| `/zh/seo/learn-seo` | SEO 学习资源 | 什么是 SEO 工具 · 第 1 段 |
| `/zh/seo/website-indexing` | 索引与收录排查 | 免费必选项 · 列表 · GSC |
| `/zh/seo/website-traffic` | 流量与渠道分析 | 免费必选项 · 列表 · GA4 |
| `/zh/seo/schema` | 结构化数据（Schema.org） | 免费必选项 · 列表 · 富结果 |
| `/zh/seo/website-structure` | 网站结构 | 叠栈 · 第 2 段 |
| `/zh/seo/checklist` | SEO Checklist | 叠栈 · 第 3 段 |
| `/zh/seo/link-building` | 外链建设 | 一站式平台 · 引言 |
| `/zh/seo/serp` | SERP 与搜索结果形态 | 排名与内容 · 排名小节 |
| `/zh/seo/create-blog` | 博客与内容枢纽 | 排名与内容 · 内容优化 |
| `/zh/seo/meta-tag` | Title 与 meta 描述 | 排名与内容 · 内容优化 |
| `/zh/seo/crawler` | 爬虫与抓取 | 单功能工具 · 引言 |
| `/zh/seo/internal-links` | 内部链接 | 浏览器插件 · 引言 |
| `/zh/seo/url-optimization` | URL 与 canonical 策略 | 桌面爬虫 · 引言 |
| `/zh/tools/text` | AI 文本工具聚合 | AI / GEO · 第 1 段 |
| `/zh/marketing/geo` | GEO 策略长文 | AI / GEO · 第 2 段 |
| `/zh/tools/geo` | GEO 工具聚合 | AI / GEO · 第 2 段 |
| `/zh/glossary` | SEO 词汇表 | 结论 · 第 2 段 |

**统计**：上表共 **18** 条不同站内路径；同一 `href` 在 JSON 内仅出现一次；FAQ 无 `<a>`。

---

*试点页：[alignify.co/seo/checklist](https://alignify.co/seo/checklist) · [alignify.co/zh/seo/checklist](https://alignify.co/zh/seo/checklist) · [alignify.co/seo/how-search-engine-works](https://alignify.co/seo/how-search-engine-works) · [alignify.co/zh/seo/how-search-engine-works](https://alignify.co/zh/seo/how-search-engine-works) · [alignify.co/seo/crawler](https://alignify.co/seo/crawler) · [alignify.co/zh/seo/crawler](https://alignify.co/zh/seo/crawler) · [alignify.co/seo/learn-seo](https://alignify.co/seo/learn-seo) · [alignify.co/zh/seo/learn-seo](https://alignify.co/zh/seo/learn-seo) · [alignify.co/seo/search-engine](https://alignify.co/seo/search-engine) · [alignify.co/zh/seo/search-engine](https://alignify.co/zh/seo/search-engine) · [alignify.co/seo/best-tools](https://alignify.co/seo/best-tools) · [alignify.co/zh/seo/best-tools](https://alignify.co/zh/seo/best-tools)。*

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-19 | 初版：SEO 指南内链专册；FAQ 无链、§1.5 分布、跨频道节制；附录 introHtml 示例 |
| 2026-04-19 | 将原 `seo-pages-internal-link-inventory` 并入为附录 B |
| 2026-04-19 | checklist 英文章节调整为 7（新增 §6 Content Modules）；附录 B 英表「实施/内容模块」首次出现区块同步 |
| 2026-04-20 | 新增附录 B.3 / B.4：`how-search-engine-works` 英/中文 JSON 全文唯一 `href` 台账；试点页脚注补链 |
| 2026-04-20 | 新增附录 B.5 / B.6 与 §1.6、`learn-seo` 内链台账与主题紧约束；试点页脚注补链；`learn-seo` 正文链收紧；中英 JSON **重排 `blocks`**（先官方与检索法，再资源；**中文页**中文资源先于英文资源）；微调 `childrenHtml` 顶部分隔 |
| 2026-04-22 | 新增附录 B.7 / B.8：`search-engine` 中英 landscape 全文唯一 `href` 台账；正文分散 `/seo` 集群（SERP、索引、Schema、Checklist、学习、流量）；GEO 改链 Marketing；去 Insights 弱链；中文 FAQ 去掉 Web Search API 的 `<a>` |
| 2026-04-21 | 新增附录 B.9 / B.10：`best-tools` 中英全文唯一 `href` 台账（18 条/语言）；英文 GEO 段避免重复 `/seo/serp`；中文企业级段不重复 `/zh/seo/website-indexing` |
| 2026-04-21 | 新增附录 B.5 / B.6：`crawler` 中英台账；附录 Learn SEO / search-engine / best-tools 顺延为 B.7–B.12；§1.2 增 **how ↔ crawler**；`crawler` JSON 去除重复的 `how-search-engine-works` 链并缩短与 how 重叠的「蜘蛛工作流程」；试点脚注补 crawler |
| 2026-04-22 | 附录 B.5 / B.6：`crawler` 英/中文结论段增 `website-indexing`、`sitemap`、`robots-txt`、`internal-links`；TLDR 与 `web-scraping` 链去重；全文 **8** 条 distinct `/seo|/tools` 路径 |
| 2026-05-20 | 附录 B.8（Learn SEO EN）注释修正：「与 B.5 对称」→「与 B.7 对称（中英互逆）」；旧引用因 crawler 插入 B.5 后过期，现恢复为指 B.7 Learn SEO ZH |
| 2026-05-20 | 附录 B.2 / B.3 / B.4 台账统计修正：B.2 27→28（含 `/zh/marketing/keyword-research`）、B.3 18→20、B.4 18→20；三表行数与实际 JSON 内 `href` 去重校验一致 |

---

<a id="part-45-marketing-频道内链"></a>

# Part 4.5 · Marketing 频道内链（M1–M11）

> **逐页执行表**：[`skills/optimize-internal-links/references/site-structure-internal-links.md`](../../../skills/optimize-internal-links/references/site-structure-internal-links.md) **§七** · [`marketing-internal-links-backlog.md`](../../../skills/optimize-internal-links/references/marketing-internal-links-backlog.md)  
> **全站快照**：[`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md)  
> **Last updated**：2026-08-27

> **代号消歧**：本节 **M1–M11** = Marketing **内链**规则；[`copy-quality.md`](./copy-quality.md) Part 0.2 的 **Copy mode M1/M2/M3** = 成稿五维模式。**二者无关**。

新文 `content/blog/` + `/blog/{slug}`；存量 `/marketing/` 不重迁。全站共性规则见 [Part 1–2](#part-2-全站内链规则)。

---

## 一、第一原则：读者想点（Click Intent）

内链优化的**最高优先级**不是 SEO 权重传递，而是：

> **读者读到此处，是否自然产生「我想继续搞清 X」的冲动——而 X 恰好是目标页主题？**

| 通过 | 不通过 |
|------|--------|
| 「触顶后开启 Extra Usage，把 panic 收成按量收入」→ 链 **生成式 AI 定价与包装** | 「详见 [定价策略](/zh/blog/pricing-strategy)」单独成句 |
| 「矩阵 UGC 的 performance 层往往就是联盟计划」→ 链 **联盟营销** | 段末「延伸阅读：A、B、C」清单 |
| 「Claude weekly cap 窗口里，stable Plan 可接迁移」→ 链 **Coding Plan** | 锚文本写「点击这里」「本文」「这篇文章」 |

**自检三问（每条链必过）：**

1. 删掉链接后，句子是否仍通顺？（自然性）
2. 读者点过去，能否在 10 秒内感到「来对了」？（相关性）
3. 若本段已有 1 条链，再加这条是否抢注意力？（分布）

---

## 二、Marketing 规则 M1–M11

| # | 规则 | 说明 |
|---|------|------|
| **M1** | **无硬性条数** | 以点击意图为准；长文通常 3–6 条 distinct 为参考，Hub 页可更少。**不**为凑数加链 |
| **M2** | **每段 ≤1 链** | 同段 2 链仅当不同 H3 子块且不同目标；**禁止 ≥3 链/段** |
| **M3** | 同 URL **全页仅 1 次** | 含正文首段 BLUF；hero 已废弃（E44）；**含 FAQ 答案** |
| **M4** | **TL;DR / HowTo 步骤** 无链 | FAQ **允许**内链（见 [§1.5](#15-faq-内链规则)） |
| **M5** | **描述性锚文本** | 用策略名、任务名、平台名；禁 click here / 本文 / learn more |
| **M6** | **高度相关** | 同一 GTM 工作流、互补策略、或经批准的跨频道任务链（见 §四） |
| **M7** | **均匀分布** | 什么是 0–1 · 主体方法论 2–4 · 案例/框架 0–1 · 结论 0–1；**禁止**集中在「组合拳/延伸阅读」单段 |
| **M8** | **链进句子** | 禁止「**Coding Plan + 定价溢出**：[链接]…**+ 邀请裂变**：[链接]…」式标签堆链 |
| **M9** | **结论可含内链** | **0–2** 条；须承接上文未覆盖的**单一**下游任务；禁止清单式堆链（见 [`sections.md`](./sections.md) Part 4.4） |
| **M10** | **表格/列表默认无链** | 表格内链例外须逐条过 M6；优先改正文叙述 |
| **M11** | **只链已上线页** | Brief / Link Plan 禁止含未发布 slug；G6 阻断。姊妹篇、OSS 线等未上线 → 纯文字，不发 `href`；上线后再补反向链 |

---

## 三、推荐分布节奏（A/B/C 三类）

| 类型 | 代表 slug | 内链落点 |
|------|-----------|----------|
| **A 策略框架型** | pricing-strategy, competitive-analysis, keyword-research | 什么是：边界 1 · 框架节：互补方法论 1–2 · 实施/趋势：SEO 或 blog 1 · 结论：0–1 |
| **B 平台战术型** | geo, reddit, x-formerly-twitter, email-marketing | 什么是：平台机制 0 · 战术节：相邻渠道 1 · 测量/合规：SEO/blog 1 · 案例：0–1 |
| **C 项目运营型** | creator-program, referral-program, ugc-marketing, lifetime-deal | 什么是：与邻近策略区分 1 · 激励/招募：相关运营文 1–2 · 合规/定价：1 · 结论：0 |

**Blog GTM / campaign 长文**（`coding-plan`, `rate-limit-reset`, `git-commit-attribution` 等）：内链按 M1–M10；**组合拳节零内链**为常见做法（非强制），链分布在架构/案例/风险节。**结构不套用固定骨架**，见 [`templates.md`](./templates.md#part-3-marketing) §3.1。

---

## 四、Marketing Cluster 与跨频道节制

### 4.1 站内 Cluster（优先互链）

```
                    marketing-types (Hub)
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
 Research 基础          Creator 生态           GTM 定价
 keyword-research      creator-program        pricing-strategy
 competitive-analysis  creator-challenge      lifetime-deal
                       influencer             │
                       ugc-marketing          ├── blog/coding-plan
 affiliate ─────────── referral-program       └── blog/rate-limit-reset
     │
 Channel 战术
 geo · x-formerly-twitter · reddit · email-marketing
 localization-strategy · growth-case-studies
```

### 4.2 批准跨频道链（每页每目标 ≤1）

| 从 Marketing | 可链至 | 触发语境 |
|--------------|--------|----------|
| geo, keyword-research | `/seo/*` | 同一调研/实施任务（如 landing-page, search-engine） |
| geo, competitive-analysis | `/blog/ai-visibility`, `/blog/ai-traffic-*` | 测量 AI 可见度/引用 |
| affiliate, referral-program | `/tools/affiliate-marketing`, `/tools/referral-program` | 「工具选型」非策略定义 |
| pricing-strategy, lifetime-deal | `/blog/coding-plan`, `/blog/rate-limit-reset` | GTM 增长模式对照 |
| localization-strategy | `/seo/navigation-menu`, `/seo/submit-website` | 实施层站点结构 |

**禁止**：为凑数链 `/tools/llm`、无关 SEO 学习页、insights 泛览。

---

## 五、锚文本规范（ZH / EN）

| 场景 | 推荐锚文本 | 避免 |
|------|-----------|------|
| 策略对照 | 生成式 AI 定价与包装 / generative AI pricing and packaging | pricing-strategy 页、点这里 |
| 事件促销 | 用量限额重置 / usage limits reset | reset 文章、这篇 |
| 创作者 | 创作者计划、联盟营销、推荐奖励计划 | creator-program slug |
| 研究 | 关键词调研、竞品分析 | 详见竞品分析 |
| GEO | AI 可见度监测、AI 流量与引用来源 | GEO 工具（除非在工具选型段） |

---

## 六、反模式（立即改）

1. **组合拳段堆链** — `#gtm-combo`、结论「延伸阅读」段 ≥2 链  
2. **同段重复 cluster** — geo 开篇段同时链 affiliate + influencer + creator-program  
3. **表格当导航** — ugc-marketing 对比表 4 链；lifetime-deal 渠道表内嵌 affiliate  
4. **零出链孤岛** — affiliate、creator-program、influencer、reddit（EN）等 0 正文链  
5. **结论重复开篇** — lifetime-deal 结论再链 pricing-strategy（正文已链）  
6. **首节 BLUF + 正文双链同目标** — 如 rate-limit-reset 首节链 pricing，正文再链 pricing（M3 违规，须合并为 1 次）  
7. **机械指路链（M8 变体）** — 「对照 / 详见 / 见 XXX 指南 / 见 XXX 文章 / 系统方法见 / 可配合 XXX」单独成句；结论段为凑数堆「选题对接 A、并借 B」；Hub 自指或「访问 / 查看 XXX 页」。**改法**：链必须嵌在读者正在执行的任务句里——删掉链接后句子仍通顺，且读者点过去 10 秒内感到「来对了」。

**机械 ❌ → 自然 ✅ 示例**

| 机械（禁） | 自然（可） |
|-----------|-----------|
| 改价邮件前可先对照 [竞品分析] 里竞品的邮件节奏 | 改 tier 邮件前先看竞品 pricing 页有没有动过 seat/credits——和监测定价页变更是一轮 desk research（无链或链在「监测定价页」工作流句） |
| tier 与包装见 [定价策略] | reward 若是 credits 升级，得和 [定价策略] 里的 hybrid credits 结构对齐，否则用户算不清值不值 |
| 矩阵 UGC 见 [UGC 营销] 的 flat fee 披露 | 不少团队把 [UGC 营销] 的 flat fee 和 30% 佣金叠在同一合同里——两层须分别披露 |
| 结论：将邮件纳入整合体系，对接 [关键词调研]，并借 [竞品分析] | （删除整句；若需链，放在 Newsletter 选题那句：「选题应与 [关键词调研] 及 Topical Map 对齐」） |

## 七、新建 / 改版工作流

1. 查 [`site-structure-internal-links.md` §7.3–7.4](../../../skills/optimize-internal-links/references/site-structure-internal-links.md) 或 [`marketing-internal-links-backlog.md`](../../../skills/optimize-internal-links/references/marketing-internal-links-backlog.md) 该 slug 的「应链向 / 应被链自」  
2. 写 **Internal Link Plan** 表（见 [`07-internal-links.md`](../07-internal-links.md)）— 锚文本 / 目标 / 段落 / 点击意图  
3. 落稿：先写无链正文，再按 M7 节奏插入  
4. 自检：M1–M11 + 三问  
5. 刷新 [`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md)

---

## 八、与模板对齐

[`templates.md`](./templates.md) Part 3 · 内链 M1–M11 见本文 Part 4.5 — 创建 checklist 须含 M1–M11。

---

<a id="part-5-insights--其他频道"></a>

# Part 5 · Insights / 其他频道

### Insights 长文

> **全站共性规则**：[Part 2 §1.5 FAQ 内链](#15-faq-内链规则)（唯一性、相关性、样式等）。  
> **同目录索引**：本文 Part 5  
> **Indie 专册 stub**（避免旧链接失效）：本文 Part 5

**用途**：维护 **`content/insights/zh/*.md`** 与 **`content/insights/en/*.md`**（`ArticleDocV1`，由 `ArticleFromJson` 渲染）时的推荐内链、FAQ 约束与本地化差异；与 `content/tools`、`content/seo` 专册分离（本页不写 Tools 邻居矩阵）。

**编辑部知识块（非站点路由）**：可与 [knowledgehub/marketing/indie-hackers.md](../../../knowledge/marketing/indie-hackers.md) 对照；勿要求读者从 Insights 点击进 `docs/`。

---

## 一、七篇长文：路由与 JSON 路径

| Slug | 中文路由 | 英文路由 | 中文 JSON | 英文 JSON |
|------|-----------|-----------|------------|------------|
| `indie-hackers` | `/zh/insights/indie-hackers` | `/insights/indie-hackers` | `@content/insights/zh/indie-hackers.md` | `@content/insights/en/indie-hackers.md` |
| `directory-submission-sites` | `/zh/insights/directory-submission-sites` | `/insights/directory-submission-sites` | `@content/insights/zh/directory-submission-sites.md` | `@content/insights/en/directory-submission-sites.md` |
| `reasons-you-need-seo` | `/zh/insights/reasons-you-need-seo` | `/insights/reasons-you-need-seo` | `@content/insights/zh/reasons-you-need-seo.md` | `@content/insights/en/reasons-you-need-seo.md` |
| `generative-ai-landscape` | `/zh/insights/generative-ai-landscape` | `/insights/generative-ai-landscape` | `@content/insights/zh/generative-ai-landscape.md` | `@content/insights/en/generative-ai-landscape.md` |
| `ai-logo-design` | `/zh/insights/ai-logo-design` | `/insights/ai-logo-design` | `@content/insights/zh/ai-logo-design.md` | `@content/insights/en/ai-logo-design.md` |
| `google` | `/zh/insights/google` | `/insights/google` | `@content/insights/zh/google.md` | `@content/insights/en/google.md` |
| `openai` | `/zh/insights/openai` | `/insights/openai` | `@content/insights/zh/openai.md` | `@content/insights/en/openai.md` |

**组件内 `href` 规则**：中文正文使用 **`/zh/...` 前缀**；英文正文使用 **`/marketing/...`、`/tools/...`、`/insights/...`** 等无前缀英文路径。

---

## 二、FAQ 与内链（七篇通用）

| 规则 | 说明 |
|------|------|
| **FAQ 答案允许内链** | 与 [Part 2 §1.5](#15-faq-内链规则)、[`sections.md`](./sections.md) Part 2.2 一致；**计入正文**；同 URL 全文 1 次 |
| **首屏 TL;DR** | 可概括内链主题，不要在 `items` 里塞 URL；具体链放在正文 `section` / `html` 字符串中 |

---

## 三、Indie Hackers：推荐内链矩阵与地域适配

**目标**：在「核心概念」「冷启动与分发」「增长策略」「实践指南/地域」「结论」中分散出现；同一 URL 全篇最多 2 次（结论中仅复述高优先级页时仍建议 ≤2）。

### 3.1 中文（`/zh/...`）高优先级 href

| 主题 | 推荐 `href` | 建议出现节 |
|------|-------------|------------|
| 冷启动 / 上架渠道 | `/zh/insights/directory-submission-sites` | 冷启动与分发、实践指南 |
| SEO 心智 | `/zh/insights/reasons-you-need-seo` | 增长策略、冷启动表 |
| 关键词与内容 | `/zh/marketing/keyword-research` | 增长策略、（与哥飞段落呼应） |
| GEO / AI 答案可见度 | `/zh/marketing/geo` | TrustMRR 旁、增长策略 |
| 定价与套餐叙事 | `/zh/marketing/pricing-strategy` | 业务模式、实践指南定价 |
| LTD 与促销 | `/zh/marketing/lifetime-deal` | 业务模式、收入模式 |
| 联盟与流量变现 | `/zh/marketing/affiliate` | 业务模式 |
| X / Twitter 运营 | `/zh/marketing/x-formerly-twitter` | 增长策略、冷启动表 |
| Reddit | `/zh/marketing/reddit` | 增长策略 |
| 邮件与留存 | `/zh/marketing/email-marketing` | 增长策略、冷启动 |
| 国际化 / 出海文案 | `/zh/marketing/localization-strategy` | 实践指南（出海、良渚） |
| 增长案例心智 | `/zh/marketing/growth-case-studies` | 实践指南 |
| 竞品与定位 | `/zh/marketing/competitive-analysis` | 实践指南 |
| Tools 总入口 | `/zh/tools` | 产品类型、工具选型 |
| App builder / no-code | `/zh/tools/app-builder` | 什么是独立开发者 |
| Marketing 总览 | `/zh/marketing` | 结论或冷启动节延伸阅读 |

### 3.2 英文（无前缀）对照 href

| 主题 | 推荐 `href` |
|------|-------------|
| Directory / launch surfaces | `/insights/directory-submission-sites` |
| SEO narrative | `/insights/reasons-you-need-seo` |
| Keyword research | `/marketing/keyword-research` |
| GEO | `/marketing/geo` |
| Pricing | `/marketing/pricing-strategy` |
| Lifetime deals | `/marketing/lifetime-deal` |
| Affiliate | `/marketing/affiliate` |
| X / Twitter | `/marketing/x-formerly-twitter` |
| Reddit | `/marketing/reddit` |
| Email | `/marketing/email-marketing` |
| Localization | `/marketing/localization-strategy` |
| Growth case studies | `/marketing/growth-case-studies` |
| Competitive analysis | `/marketing/competitive-analysis` |
| Tools hub | `/tools` |
| App builder | `/tools/app-builder` |
| Marketing hub | `/marketing` |

**路由校验**：改 href 前在 `app/` 与 `app/zh/` 下确认 `page.tsx` 存在。

### 3.3 中英文内容适配（与内链挂钩）

| 维度 | 中文长文 | 英文长文 |
|------|-----------|-----------|
| **线下/地域聚落** | **良渚**（杭州近郊）+ 出海、版号等本土段落 | **曼谷 / 清迈**等东南亚数字游民枢纽 + **里斯本**等欧洲枢纽一句带过；链 **`/marketing/localization-strategy`**、**`/marketing/geo`** |
| **社群资源** | 哥飞、Web.Cafe、出海去等（外链 + 精简） | **Indie Hackers、Product Hunt、TrustMRR** 为主；不写中文付费社群名 |
| **冷启动七周表** | 全站中文 Marketing 内链 | 同结构；表内「LinkedIn」等可保留英文 |

**原则**：执行表（周次、渠道）两语可对齐；地域叙事不对齐。

---

## 四、其余六篇 Insights（简述）

- 正文大块多为 `blocks` 中的 **`type: "html"`** 或 **`type: "section"`**；站内链用带 `class` 的 `<a href="...">`；外链加 UTM、`rel` 与 `section-links` 一致。
- 含 **`type: "references"`** 的页面：`generative-ai-landscape`（中英）、`ai-logo-design`（中英）、`directory-submission-sites`（仅英文 JSON）。改参考文献时同步检查 URL 与 `locale`。
- 改版后同步：`blogLayout.modifiedDate`、`app/**/insights/*/page.tsx` 的 `openGraph.modifiedTime`（若采用）、`src/data/site-pages-config.ts`、RSS `app/feed/route.ts` 中对应条目。

---

## 五、维护清单（改版时打勾）

- [ ] 正文新增/替换链接后，全篇搜索同一 `href` 是否大于 2 次（Indie 等长文）。
- [ ] FAQ 内链（若有）遵守 R4：同一 `href` 全页仅 1 次。
- [ ] `blogLayout.modifiedDate` 与页面 `metadata.openGraph.modifiedTime` / RSS / `PAGE_MODIFIED_DATES` 一致（按站点策略选子集同步）。
- [ ] 英文 JSON 中 `/insights/`、`/marketing/` 链接是否存在对应路由。
- [ ] 与 knowledgehub / skill 执行表冲突时，以 skill + knowledgehub 为 SSOT，长文只保留读者向缩写。

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-20 | 创刊：七篇 JSON 路径、通用 FAQ、Indie 矩阵与地域适配迁入总册 |
| 2026-04-20 | 从 `insights-indie-hackers-internal-links` 合并 Indie 专册正文 |
### Marketing / 聚合等

> **单一真相源（全站）**：[section-links.md](./internal-links.md)（唯一性、相关性、样式、组件级规则）。  
> **同目录专册**：本文 Part 4（`content/seo` JSON）· 本文 Part 3（`content/tools` JSON）· 本文 Part 5（`content/insights` 七篇长文 JSON）· 本文 Part 5（stub → 总册）

**用途**：**非** SEO JSON、**非** Tools JSON 的页面（Marketing、聚合页、法律页等）在 **`docs/`** 中**分散**存放的内链相关规范索引；本页**不重复**专册正文，仅便于按场景跳转。

---

## 一、页面类型与专册对应

| 内容载体 | 内链拓扑与试点台账 | 全站共性规则 |
|----------|-------------------|--------------|
| `content/seo/*/*.md` | 本文 Part 4 | `section-links` |
| `content/tools/*/*.md` | 本文 Part 3 | `section-links` |
| `content/insights/*/*.md`（Insights 长文） | 本文 Part 5 | `section-links` |
| Marketing、聚合、其他 | **下表「文档导航」与「排查表」** → 各 template / section | `section-links` |

**一句话**：FAQ **允许**内链；**计入正文**；同 URL 全文 1 次（[§1.5](#15-faq-内链规则)）。

---

## 二、文档导航（模板与章节规范）

| 文档 | 用途 |
|------|------|
| [sections.md](./sections.md) | 章节 SSOT（Part 0–5：TL;DR / FAQ / 节型 / 结论 / Final CTA） |
| [templates.md](./templates.md) | 四类页面结构参考（Part 2–5）；**建议非施工图** |
| [internal-links.md](./internal-links.md) | 全站内链、外链、组件级规则 |
| [copy-quality.md](./copy-quality.md) | 五维 · Swap Test · L0 阻断（Part 2）；篇幅 C 层（Part 3–4） |
| [README.md](./README.md) | 规范索引 |
| [meta.md](./meta.md) | SEO 章约束 |
| `alignify-keywords-tools.md` | Tools 意图与「相邻 Tools」**权威表** |
| `src/data/tools-pages-config.ts` | AlsoInterestedIn 等组件 slug 列表 |

---

## 三、`docs/` 内含内链规则或约束的文档（排查表）

下表用于完整排查，**非**要求迁入 `internal-links/`。

| 文档 | 与内链相关的内容（保留原因） |
|------|------------------------------|
| [internal-links.md](./internal-links.md) | **全站**内链唯一性、相关性、样式、FAQ 可链、组件表；主文档 |
| [sections.md](./sections.md) | 各节写法与内链位点（Part 2–5） |
| [templates.md](./templates.md) | 四类页面结构参考（Part 2–5） |
| [copy-quality.md](./copy-quality.md) | 五维 · Swap Test · L0 阻断（Part 2）；篇幅 C 层（Part 3–4） |
| [README.md](./README.md) | 规范索引 |
| [meta.md](./meta.md) | Meta / H1 约束 |
| [technical/technical-crawlability.md](../../ops/seo-fundamentals.md) | 孤儿页与内链 |
| [technical/technical-indexing.md](../../ops/seo-fundamentals.md) | 索引检查项含内链 |
| [alignify-project-context/brand-visual.md](../../../knowledge/design/aesthetic-references.md) | 内链视觉/token |
| [alignify-project-context/seo-article-optimization-tracker.md](../../ops/gsc-optimization-plan.md) | 站内 SEO 文章 Internal Links 页进度 |
| `alignify-keywords.md` | 支柱表「internal links」→ `/seo/internal-links` |
| [knowledgehub/tools/*.md](../../../knowledge/tools/README.md) | 少数「相邻 Tools」句或外链索引（知识块，非站点内链规范） |

---

## 四、与 `section-links` 迁出内容的关系

已从 [section-links §四](./internal-links.md) **迁入 Tools 专册**的正文：**「产品链接验证与优化（Tools 页面）」** 全文 → 本文 §3 第五节。`section-links` 保留标题索引。

**未迁入、且不应迁入本目录的权威数据**：`alignify-keywords-tools.md` 各 slug 下完整「相邻 Tools」表（Tools 专册 [附录 B](#附录-b相邻-tools-速查邻居矩阵) 仅为速查，修订以 keywords 为准）。

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-19 | 从原 `internal-links/README` 拆出「其他页面」索引与排查表；与三专册交叉引用、避免正文重复 |


---

<a id="part-6-创建与存量优化工作流"></a>

# Part 6 · 创建与存量优化工作流

> **执行 SSOT**：[`../../optimize-internal-links/workflow.md`](../../optimize-internal-links/workflow.md) · [`../../optimize-internal-links/SKILL.md`](../../optimize-internal-links/SKILL.md)  
> **全站快照**：[`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md)  
> **新文 Step 7**：[`../07-internal-links.md`](../07-internal-links.md)

验收（部署仓）：`audit-tools-internal-links.py` · `verify:content-json` · `build`。存量修复编辑模式见任务 Brief（本 skill 不预设 R-LINK-ONLY）。

---
<a id="part-7-markdown-正文格式与计数范围"></a>

# Part 7 · Markdown 正文格式与计数范围

- **源文件**：`alignify-by-kostja/content/{tools|seo|blog|marketing|insights|events}/en|zh/{slug}.md`
- **内链语法**：Markdown `[锚文本](/zh/tools/slug)` 或 `childrenHtml` 内 `<a href="/zh/tools/slug">`
- **计数范围**：TLDR intro（`tldr-data.json` · 不计 md）、`section` 段落、应用场景/如何选择 section、结论、`html`/`childrenHtml` 列表/表格中的 `<a>`；**不计** References、外链产品 URL、Header/Footer/Breadcrumb
- **FAQ**：`faq-data.json` 全局渲染；**7 问**；答案**允许**站内链（计入正文；同 URL 全文 1 次，见 [§1.5](#15-faq-内链规则)）
- **验收**：`npm run verify:content-json`（即 `verify-content-md.py`）；内链审计 `audit-tools-internal-links.py --format md`（上下文仓 `scripts/audit/`）
- **编辑方式**：少量改动 StrReplace；批量 UTF-8 脚本写入；存量优化默认 **R-QUALITY-REWRITE**（可改 surrounding copy，禁止机械句凑数）；JSON 批量 patch 仍 **R-LINK-ONLY**

---

<a id="part-8-外链utm-与-nofollow"></a>

# Part 8 · 外链：UTM 与 Nofollow

> **实现（部署仓）**：`src/lib/utils.ts` — `addUtmToExternalLink()` · `getExternalLinkRel()`  
> **与内链关系**：Part 1–7 规范 **alignify.co 站内路径**；本节规范 **出站 URL** 的 UTM 追踪与 `rel` 属性。正文引用、References、产品外链、Footer 等均由渲染层或组件调用上述函数，**作者无需手写 UTM 参数**。

## 8.1 UTM 注入（`addUtmToExternalLink`）

### 默认行为

所有站外（非 `alignify.co`）出站链自动追加 `?utm_source=kostja&utm_medium=blog`。

### 例外 — 不追加 UTM

| 条件 | 规则 | 示例 |
|------|------|------|
| URL 已有 query 参数 | 跳过通用 UTM（不干扰既有追踪） | `?vsource=cutout_share-1370384` |
| 合作伙伴邀请链 | 原样返回（不加 Alignify UTM） | `lovable.dev/invite/*`、`manus.im/invitation/*` |

### 站内链

链向 `alignify.co`、`www.alignify.co` 或 `*.alignify.co` 子域 **永不** 追加 UTM。

## 8.2 Nofollow 规则（`getExternalLinkRel`）

### 默认行为

所有站外链使用 `rel="noopener noreferrer nofollow"`。

### 例外 — dofollow（不含 `nofollow`）

| 域名 | 原因 |
|------|------|
| `voispark.com` / `*.voispark.com` | VoiSpark（合作伙伴） |
| `novascientia.com.br` / `*.novascientia.com.br` | Nova Scientia（Kostja 本地化测试站） |
| `google.com` / `google.cn` / `g.cn` / `blog.google.com` / `developers.google.com` / `search.google.com` / `support.google.com` / `*.google.com` / `*.blog.google.com` / `*.developers.google.com` / `*.search.google.com` / `*.support.google.com` | Google（搜索引擎，dofollow） |

### 无效 URL

无法解析时，**默认 `nofollow`**（安全兜底）。

## 8.3 正文与 References 写法（与 Part 7 配合）

| 场景 | href | rel |
|------|------|-----|
| md `#references` 底部列表 | 经 `addUtmToExternalLink()` | 经 `getExternalLinkRel()` |
| 正文 inline 引用（React/`childrenHtml`） | 经 `addUtmToExternalLink()` | `noopener noreferrer`（**正文引用不设 nofollow**，便于读者溯源） |
| Tools 产品 H3 外链按钮 | 组件自动 | 经 `getExternalLinkRel()` |

详见 [`sections.md`](./sections.md) Part 2.3 References · Part 3.3 Best Tools。

## 8.4 相关代码与组件

| 路径 | 用途 |
|------|------|
| `src/lib/utils.ts` | 函数定义 |
| Markdown 正文产品 H3 块 | 工具卡片外链 |
| `src/components/CustomerCaseCard.tsx` | 客户案例网站链 |
| `src/components/Footer.tsx` | 社交图标 + Nova Scientia |
| `src/components/GlossaryViewer.tsx` | Glossary 参考外链 |
| `src/components/PartnershipPageContent.tsx` | IRIS 项目链 |
| `src/components/References.tsx` | 引用列表链 |
| `src/components/YouTubeThumbnail.tsx` / `YouTubeThumbnailImage.tsx` | 视频链 |
| `src/marketing/GrowthCaseStudiesIndex.tsx` | 增长案例卡片 |

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 合并 `utm-nofollow.md` → Part 8（外链 UTM · Nofollow） |

