# Alignify「How To / 如何选择」章节规范（唯一真相源）

> **站点**：[alignify.co](https://alignify.co)
> **部署仓正文**：`alignify-by-kostja/content/**/*.md`（Markdown + frontmatter + block 标记）
> **Last updated**: 2026-08-08
> **说明**：Alignify 所有「How To / 如何选择」章节的**定位、结构、写作规则、正文渲染、验收与常见错误仅在本文件维护**。HowTo JSON-LD Schema 已于 2026-08-08 移除；`template-tools.md §5.1`、`template-marketing.md §4.4`、`SKILL.md`、`common-errors.md` 中与本文件重叠的条目均已改为指向本文件或仅保留精简引用。

---

## 目录

1. [Part 1 · 定位与分工（与 TLDR 的关系）](#part-1--定位与分工与-tldr-的关系)
2. [Part 2 · 结构规范（位置 / 标题 / 步骤数量）](#part-2--结构规范位置--标题--步骤数量)
3. [Part 3 · 写作规则（去模板 / 决策分叉 / 内容优先）](#part-3--写作规则去模板--决策分叉--内容优先)
4. [Part 4 · 正文渲染结构（H2 + intro + H3 步骤，无 Schema）](#part-4--正文渲染结构h2--intro--h3-步骤无-schema)
5. [Part 5 · 页面类型差异](#part-5--页面类型差异)
6. [Part 6 · 验收与审计](#part-6--验收与审计)
7. [Part 7 · 常见错误速查](#part-7--常见错误速查)

---

<a id="part-1--定位与分工与-tldr-的关系"></a>

# Part 1 · 定位与分工（与 TLDR 的关系）

> **Last updated**: 2026-08-08
> **实践来源**：2026-08 tools 全站 TLDR 去模板化 + howTo 试点（`chatbot`、`directory`、`video-clipping`）

## 一、定位

**How To（如何选择）是页面结尾的「决策路由」章节**：把「从哪几个分叉点开始选、每一步要核验什么」拆成可执行步骤。它位于正文末尾（Conclusion 之前），给读者一条从「产品认知」到「做出选择」的路径。

## 二、与 TLDR 的分工（不重复）

| | TLDR（开篇） | How To（结尾） |
|---|-------------|---------------|
| **回答** | 「这个工具是做什么、该选谁」的**结论摘要** | 「具体怎么选」的**步骤路径** |
| **形式** | intro 直答 + 4–5 条要点（可独立抽取） | intro 给分叉 + 3–5 步递进动作 |
| **决策锚点** | 与 HowTo **共享同一分叉**（真相源 / 技术路线 / 交付物…） | 与 TLDR **共享同一分叉** |
| **表述** | 结论式短句（`Intercom fits product inboxes…`） | 判断式步骤（`Locate the truth source` → 核验条件） |
| **重复** | 不复制 HowTo 的步骤文字 | 不复制 TLDR 的要点文字 |

**一句话分工**：TLDR 给答案，How To 给路径；两者锚定同一个分叉，但一个讲「该选谁」，一个讲「怎么确认」。

## 三、与正文的关系

- 不与「什么是 / What are」（主题介绍）重复——How To 是决策，不是概念。
- 不与 BestTools 产品卡重复——How To 的步骤里可点名工具，但不重述产品卡描述。
- 不与结论重复——How To 是「怎么选」，结论是「选型后的落地要点」。

---

<a id="part-2--结构规范位置--标题--步骤数量"></a>

# Part 2 · 结构规范（位置 / 标题 / 步骤数量）

> **Last updated**: 2026-08-08

## 一、位置

正文末尾，**结论之前**（Tools 页面顺序见 [template-tools](../templates/template-tools.md) 一、页面结构）：

```
… 应用场景 → 如何选择 → 结论 → FAQ
```

## 二、H2 标题与 id

| 项目 | 中文 | 英文 |
|------|------|------|
| **H2 标题** | `如何选择 [AI] [工具类型]` | `How to Choose [AI] [Tool Type]` |
| **示例** | 如何选择 AI 变声器 | How to Choose AI Voice Changer |
| **block id** | `how-to-choose-{slug}` | `how-to-choose-{slug}` |

**id 规则**：必须 `how-to-choose-{slug}`（如 `how-to-choose-chatbot`），**禁止**全站统一 `"id": "how-to-choose"`（防锚点冲突）。

## 三、步骤数量：3–5 步，不硬性 5

步骤数量**按主题复杂度决定**，不强制 5 步：

| 主题复杂度 | 步数 | 说明 |
|-----------|------|------|
| 单一品类、单一分叉 | 3–4 步 | 分叉 → 核验 → 落地即可 |
| 多子域、多分叉（代理+API+合规+管线等） | 5 步 | 覆盖完整决策链 |

**硬底线**：≥3 步；「步骤少于 5 个」不再视为错误，但少于 3 个视为 stub。

## 四、introduction（引导段）

- **第一句给决策分叉**：点明读者要做的第一个关键取舍（`The fork is where truth lives — a product inbox, a ticket queue, or a marketing landing page`）。
- **第二句说明步骤职责**：`These steps route that decision first, then check…`。
- 禁止模板开头（见 Part 3 黑名单）。
- 篇幅：**内容优先**，参考 40–90 字 / 40–90 词，说清分叉即可，不硬凑。

---

<a id="part-3--写作规则去模板--决策分叉--内容优先"></a>

# Part 3 · 写作规则（去模板 / 决策分叉 / 内容优先）

> **Last updated**: 2026-08-08
> **实践来源**：tools 全站 TLDR 去模板化标准迁移 + howTo 试点反馈（用户明确「内容优先，不要为字数牺牲信息」）

## 一、步骤标题：动词开头 + 分叉短语，禁止泛化祈使

标题 = **动词开头的决策分叉短语**，让读者一眼看到这一步在判断什么：

| 优秀（动词 + 分叉） | 劣质（泛化祈使，禁止） |
|--------------------|----------------------|
| `Locate the truth source` / `定位真相源` | `Evaluate Technical Requirements` / `评估技术要求` |
| `Route by source type` / `按素材类型路由` | `Consider Budget and Pricing` / `考虑预算和定价` |
| `Pick the curation model` / `选策展模型` | `Determine Your Purpose` / `确定使用目的` |
| `Lock the handoff` / `锁死移交` | `Assess Usability` / `评估易用性` |

**禁用的泛化祈使**（无分叉信息，跨页复用 = 模板）：`Evaluate` / `Consider` / `Assess` / `Determine` / `Check`（单独成步且无具体对象时）。

## 二、步骤描述：四条要素，内容优先

每步描述为**单一段落**，至少包含以下要素（不要求每步全有，但整节覆盖）：

1. **决策分叉**：这一步在 A 与 B 之间怎么取舍（`Product inbox → Intercom; SLA queue → Zendesk AI`）。
2. **判断信号**：读者怎么知道自己属于哪一档（`if your renewals bill in Stripe…`）。
3. **约束条件**：选了之后要满足什么才成立（`verify 9:16 export presets, batch limits…`）。
4. **可测指标 / 成本 / 误区**：一个能验收的数字或常见坑（`containment rate and time-to-first-response`；`orphaned chats burn trust faster than a slow queue`）。

**要点**：
- 可点名 ≥2 个真实产品/机制锚点（Intercom、Zendesk AI、OpusClip、Toolify…），但不重述产品卡。
- 段落式，**禁止 `<ul>` 列表**（见原规范 3.1 保留）。
- **内容优先**：篇幅以讲透为准，不为凑字数增删信息（EN 参考 35–90 词 / ZH 参考 60–140 字，作为质检参考而非硬底线）。
- 与 TLDR 同一分叉、不同表述：TLDR 写结论，How To 写判断过程。

## 三、去模板黑名单（must be 0）

| 信号 | 示例 | 替代 |
|------|------|------|
| description 泛模板 | `Select the right X based on A, B, C` / `选择合适的 X 需要综合考虑 A、B、C` | 第一句给分叉 |
| description 数步数 | `Follow these 5 steps…` / `以下五步…` | 第二句给步骤职责 |
| 标题泛祈使 | `Evaluate…` / `Consider…` / `Assess…` / `确定使用目的` | 动词 + 分叉短语 |
| 步骤标题跨页复用 | `Consider budget and pricing`（同标题多页） | 每页分叉不同 |
| 步骤描述一句箭头 | `A→B` / `A → B；C → D` 无展开 | 补判断信号与约束 |
| 与 TLDR 复制 | 步骤文字 = TLDR 要点文字 | 换判断式表述 |

## 四、与 TLDR 的分叉一致性

每篇 howTo 的**首个分叉应与 TLDR 的选型槽锚点一致**（真相源 / 技术路线 / 交付物 / 交互模式…），但表述为「步骤判断」而非「要点结论」。审计时核对两者锚点是否同一分叉。

---

<a id="part-4--正文渲染结构h2--intro--h3-步骤无-schema"></a>

# Part 4 · 正文渲染结构（H2 + intro + H3 步骤，无 Schema）

> **Last updated**: 2026-08-08
> **变更**：2026-08-08 移除 HowTo JSON-LD Schema（Google 已停用 HowTo rich results）。`howto-schema.ts`、`markdown-doc.ts` 的 schema 注入逻辑、`HowToChoose` 组件引用均已删除；`HowToChoose.tsx` 组件在部署仓不存在。How To 章节由 Markdown 正文直接渲染。

## 一、Markdown 结构（唯一真相源）

```md
<!-- block:section -->
## How to Choose [AI] [Tool Type] {#how-to-choose-{slug}}

[intro 段：分叉句 + 步骤职责]

### [Step1 标题] {#step-1-id}

[步骤 1 段落：分叉 / 判断信号 / 约束 / 可测指标]

### [Step2 标题] {#step-2-id}

[步骤 2 段落]
…
```

- **H2**：`如何选择 [AI] [工具类型]` / `How to Choose [AI] [Tool Type]`，id 用 `how-to-choose-{slug}`（禁止全站统一 `how-to-choose`）
- **intro 段**：H2 下第一个段落，按 Part 3（分叉 + 步骤职责）
- **步骤**：每步一个 `###` + 单一段落；`markdown-doc.ts` 会把 `###` 解析为 subSection 渲染
- **无 script / childrenHtml**：不再插入 `application/ld+json` HowTo 脚本

## 二、frontmatter 不再需要 howTo 字段

- **Markdown 版**：如何选择内容全部在正文（H2 + intro + H3 步骤），**frontmatter 不需要 `howTo:` 块**。历史遗留的 `howTo:` frontmatter 字段不再被读取（schema 生成已删），可在改版时顺带清理。
- **JSON 版（已废弃）**：`howToChoose` block 与 `HowToChoose.tsx` 组件仅存在于旧 JSON 体系；Markdown 内容不使用。

## 三、步骤标题格式

见 Part 3（动词开头 + 分叉短语），`###` 标题与 TLDR 分叉一致。

---

<a id="part-5--页面类型差异"></a>

# Part 5 · 页面类型差异

> **Last updated**: 2026-08-08

| 页面类型 | 特有规则 |
|----------|---------|
| **Tools** | 可点名具体工具与选择建议（Intercom、OpusClip、Toolify…）；步骤覆盖选型分叉、核验与落地 |
| **SEO** | 偏实施步骤（怎么配置、怎么验证），可含 HowTo 但不重述技术正文；纯文字 |
| **Marketing** | 偏方法论步骤（策略选型、执行顺序）；**禁止**链接、具体产品名、工具名、平台名，用通用表述（「趋势类工具」「关键词挖掘工具」）——见 [template-marketing §4.4](../templates/template-marketing.md#44-how-to如何实施) |

页面类型的 section 顺序与内链分布细则见 [template-tools](../templates/template-tools.md) 与 [alignify-internal-links.md §3.1.5](../alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)。

---

<a id="part-6--验收与审计"></a>

# Part 6 · 验收与审计

> **Last updated**: 2026-08-08

## 一、必跑命令（部署仓）

```bash
npm run verify:content-json    # 校验 frontmatter 与 block 标记
npm run build
```

> **HowTo Schema 已移除（2026-08-08）**：Google 已停用 HowTo rich results 展示，且 Markdown 版内容由正文 H2 + H3 步骤直接渲染。不再生成 `application/ld+json` HowTo 脚本，`howto-schema.ts` 已删除，`audit:howto-choose`（JSON 版）不再适用 Markdown 内容。

## 二、howTo 专用审计（部署仓）

`scripts/permanent/audit-howto-tools.mjs` 检查：

| 维度 | 标准 |
|------|------|
| description 模板信号 | `select-right` / `based-on-list` / `follow-n-steps` / `choosing-right` / 副词模板 = 0 |
| 步骤标题泛化 | `evaluate` / `consider` / `assess` / `identify` / `determine` 等泛化祈使出现率尽量低 |
| 步骤标题跨页复用 | 同标题 ≥4 页 = 模板信号，须整改 |
| 步骤数量 | ≥3 步 |
| 步骤 stub | 每步 description 有实质内容（非 `A→B` 箭头式） |
| 与 TLDR 分叉一致 | howTo 首个分叉与 TLDR 选型槽锚点一致 |

**批次流程**（对齐 TLDR 实践）：读正文提取分叉 → 写 EN+ZH（分叉一致、表述不同）→ 审计 → 合入 → `verify:content-json`。

---

<a id="part-7--常见错误速查"></a>

# Part 7 · 常见错误速查

> **Last updated**: 2026-08-08

| 编号 | 症状 | 修复 |
|------|------|------|
| H1 | frontmatter 仍保留 `howTo:` 块 | schema 已删，正文（H2+intro+H3 步骤）是唯一真相源；`howTo:` frontmatter 可清理 |
| H2 | 步骤过短（stub） | 每步段落有实质判断信号；勿写 `A→B` 一句箭头式 |
| H3 | H2 id 泛化 | 用 `how-to-choose-{slug}`，勿全站 `how-to-choose` |
| H4 | intro 泛模板 | `Select the right X based on…` / `Follow these N steps` → 首句给分叉 |
| H5 | 标题泛化祈使 | `Evaluate…` / `Consider…` / `Assess…` / `确定使用目的` → 动词 + 分叉短语 |
| H6 | 与 TLDR 复制 | 步骤文字 ≠ TLDR 要点文字；同一分叉、判断式表述 |
| H7 | 步骤少于 3 个 | ≥3 步；按主题复杂度 3–5 步 |
| H8 | body 残留 HowTo JSON-LD script | 已废弃；删除 `<!-- childrenHtml -->` 中 `"@type": "HowTo"` 的 script 块 |

---

## 与其他文档的关系

- **[template-tools §5.1](../templates/template-tools.md#51-how-to如何选择)**：Tools 特有规则仅保留「可含工具名 + 标题示例」，其余指向本文件。
- **[template-marketing §4.4](../templates/template-marketing.md#44-how-to如何实施)**：Marketing 特有规则（禁产品名/链接）指向本文件 Part 5。
- **[sections/README.md](./README.md)**：组件索引表指向本文件。
- **common-errors.md**：howTo 相关条目指向本文件，长期以本文为准。
