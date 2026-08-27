# 双语正文管线（唯一真相源）

> **位置**：`skills/create-article/rules/content-locale.md`  
> **适用**：Step 05–06（中文）· Step 09–09c（英文 + 对等验收）  
> **版本**：v1.1 · 2026-08-27  
> **原则**：ZH/EN **各自 native 成稿**；**信息对等、表达独立**；**禁止**「先写一语种再翻译另一语种」。  
> **关联**：[`presentation.md`](./presentation.md) · [`extractability-checklist.md`](./extractability-checklist.md) · [`sections.md`](./sections.md) · [`word-counts.md`](./word-counts.md) · [`copy-quality.md`](./copy-quality.md)

---

## 目录

1. [Part 0 · 核心原则与「地道」定义](#part-0-核心原则与地道定义)
2. [Part 1 · 双轨成稿（Subagent）与流程总览](#part-1-双轨成稿subagent与流程总览)
3. [Part 2 · Step 05 · 中文起草](#part-2-step-05-中文起草)
4. [Part 3 · Step 06 · 中文地道化](#part-3-step-06-中文地道化)
5. [Part 4 · Step 09 · 英文独立成稿](#part-4-step-09-英文独立成稿)
6. [Part 5 · Step 09c · 双语对等对比](#part-5-step-09c-双语对等对比)
7. [Part 6 · 验收脚本与回退](#part-6-验收脚本与回退)
8. [附录 A · 禁腔对照速查](#附录-a-禁腔对照速查)

---

<a id="part-0-核心原则与地道定义"></a>

# Part 0 · 核心原则与「地道」定义

## 0.1 核心原则

| 原则 | 中文 | 英文 |
|------|------|------|
| **Native-first** | 读起来像**中文作者写的长文**，不是英译稿 | 读起来像 **native editorial**，不是 MT / 翻译腔 |
| **双语 flagship** | ZH/EN **同等深度与 Moat**；无「先简后补」「EN 从简」 | 与 ZH 同为 flagship，非附属翻译版 |
| **信息对等，表达独立** | 事实、判断、结构对齐；**禁止**逐句翻译 | 从 Brief **Answer Blocks 重写**；可换例子与句序 |
| **双轨成稿** | ZH 轨与 EN 轨 **各自成稿**；共享 Brief，**不**互译 | 同上 |
| **内容饱满优先** | 先写足论证与场景，再对照字数区间 | 字数是 **饱满度信号**，不是 padding 目标 |
| **作者声音** | Marketing/Blog 默认 **Kostja 第一人称**（见 `presentation.md`） | *I* / *my read* 融入分析节；默认无 `#author-take` H2 |

## 0.2 什么叫「地道」（Pass 判据）

**不是**「像翻译软件」或「像英文 PPT 直译成中文」。朗读一遍，用下面 **正向信号 + 负向红线** 自检。

### 中文地道

| 正向（应达到） | 负向（须改） |
|----------------|--------------|
| 首段 **BLUF**：先答「这篇解决什么」，再背景 | 连续 3 段「该 X 用于…」英译句式 |
| 因果用完整汉语句（因为…所以…） | 正文里 **A → B → C** 箭头链当句子 |
| 术语用 **中文主称**（提交署名、用量限额重置）；英文产品名保留 | 把 `git commit attribution` 译成「Git 提交归因」 |
| 有 **场景**（谁、在什么窗口、做什么决策） | H2 以英文短语开头、括号里才是中文 |
| 有 **可证伪判断**（Brief Author POV） | 英文 slogan 直译（如「抄机制，别抄烟花」） |
| 表前有 ≥3 句 BLUF，表后有 prose 收束 | 孤立 `**标签：**` + 单句段 |

### 英文地道

| 正向（应达到） | 负向（须改） |
|----------------|--------------|
| 完整句 + 连接词（*That's why*, *In practice*, *The catch is*） | Telegraphic 名词串、`→` 当句子 |
| Editorial 节奏：平均句长合理，非连续 5 句 ≤8 词 | 按 ZH **1:1 句数**机械对齐 |
| 同一 Moat / 论据在 EN **同等深度**兑现 | EN 只有 ZH 的摘要版 |
| Kostja *I* 判断与 ZH「我」**信息对等** | 一处有具体价格/日期，另一处只有模糊概括 |

**验收手感**：中文像「行业媒体长文」；英文像「Substack / Lenny 式 editorial」——**都不是**对方语言的直译版。

## 0.3 共享输入（双轨相同）

两轨 Subagent **只共享**以下锁定物，**不**共享对方语种的 prose 草稿：

| 输入 | 来源 |
|------|------|
| Article Brief | Step 02 定稿：One-line thesis · Moat · Answer Blocks · Planned H2 · Author POV |
| **锚点 id 表** | Brief Section Plan：`{#kebab-case-id}` ZH/EN **必须相同** |
| SSOT / Research | `knowledge/` 或 Brief `SSOT:` 路径 |
| 节型规范 | [`sections.md`](./sections.md) Part 0 + 实际采用的 Part |
| 术语 | [`locale-glossary.md`](./locale-glossary.md) · [`locale-glossary.json`](./locale-glossary.json) |
| GTM/PLG 禁腔 | [`gtm-prose-voice.md`](./gtm-prose-voice.md)（Marketing/Blog 必过） |

---

<a id="part-1-双轨成稿subagent与流程总览"></a>

# Part 1 · 双轨成稿（Subagent）与流程总览

## 1.1 推荐执行模型

```
Brief 锁定（Step 02）
        │
        ├──────────────────────────┬──────────────────────────┐
        ▼                          ▼                          │
  Subagent · ZH 轨              Subagent · EN 轨              │ 可并行
  Part 2 → Part 3               Part 4                        │
  content/.../zh/{slug}.md      content/.../en/{slug}.md      │
        │                          │                          │
        └────────────┬─────────────┘                          │
                     ▼                                          │
              Step 07 内链（全篇口径一致）                       │
                     ▼                                          │
              Step 08 Meta + JSON + Final CTA                   │
                     ▼                                          │
              Part 5 · 09c 双语对等对比 ← 协调者 / 主 Agent     │
                     ▼                                          │
              Step 10 SelfCheck + audit                         │
```

**Hard rule**

- EN Subagent **不得**以 ZH md 为「源稿」逐段翻译；仅可读 Brief + 同一 SSOT + **锚点 id 表**。
- ZH Subagent **不得**按 EN 已有稿回译对齐。
- 对等验收在 **09c** 一次性做，不在成稿过程中「边写边译」。

## 1.2 Step 编号（与 SKILL 对齐）

| Step | 本文 Part | 产出 |
|------|-----------|------|
| 05 | Part 2 | ZH md 初稿 + 05b 扩写 |
| 06 | Part 3 | ZH 地道化 + Extractability |
| 07 | — | 内链（[`07-internal-links.md`](../07-internal-links.md)） |
| 08 | — | Meta + JSON + CTA（[`08-meta-config.md`](../08-meta-config.md)） |
| 09 | Part 4 | EN **独立**成稿 + 09b Pass |
| 09c | Part 5 | ZH/EN 信息对等对比 |
| 10 | — | Gate C（[`10-quality-gates.md`](../10-quality-gates.md)） |

---

<a id="part-2-step-05-中文起草"></a>

# Part 2 · Step 05 · 中文起草

> **前置**：Brief 定稿 + Gate 0R Pass  
> **产出**：`content/{channel}/zh/{slug}.md`  
> **规范**：[`presentation.md`](./presentation.md) · [`extractability-checklist.md`](./extractability-checklist.md)

## 2.1 Gate B（动笔前）

- [ ] Article Brief 已锁定（Moat + Answer Blocks 3–5）
- [ ] Planned H2 与 Brief 一致；**锚点 id 表**已写入 Brief（EN 轨复用）
- [ ] **Outline 3.5**（Brief `BatchCount ≥2`）：[`outline-cross-check.md`](./outline-cross-check.md) Pass；**单篇** → 输出 `Outline cross-check: N/A — single article`
- [ ] Brief **Copy quality** 已填（Mode · Hero fault；M2 含 cluster + swap neighbors）— 见 [`copy-quality.md`](./copy-quality.md) 附录 A

## 2.2 路径

| articleType | 路径 |
|-------------|------|
| best-ranking | `content/blog/zh/{slug}.md` |
| best-ranking-legacy | `content/tools/zh/{slug}.md` |
| seo-guide | `content/blog/zh/{slug}.md`（新文）；存量 `content/seo/zh/{slug}.md` |
| marketing-strategy | `content/blog/zh/{slug}.md`（新文）；存量 `content/marketing/zh/{slug}.md` |
| insights-analysis | `content/blog/zh/{slug}.md`（新文）；存量 `content/insights/zh/{slug}.md` |

## 2.3 起草协议（Flagship）

1. 按 Brief **Answer Blocks** 顺序写 major H2；每节首段 **BLUF**（先答后背景）
2. Moat Asset **至少 1 项**须在正文显式兑现（非 footnote）
3. **Author POV**（Brief）至少 1 处 **第一人称**判断——**写入**相关分析/案例/坑/分工节；**默认不设**独立 `#author-take` H2（User/Brief 明示除外；见 `presentation.md` §Author voice）
4. **若 Brief 采用 TL;DR**：Step 08 注册 `tldr-data.json`（intro 40–80 字直接回答 primary keyword）
5. **若 Brief 采用 FAQ**：Step 08 注册 `faq-data.json` **7 问** — 首句即答，与正文相似度 <30%
6. 段落优先 — 禁伪列表（见 `presentation.md`）
7. **含表 H2**：先 ≥3 句 BLUF → `childrenHtml` → 表后 ≥2 句（E40–E41）
8. 节规范按**实际采用的节**查阅 [`sections.md`](./sections.md) Part 0 + Part 3.x
9. **禁止**正文 meta 句：「落地细节进 skills / runbook…」（E49）
10. **go/no-go 矩阵**仅当 Brief 勾选且 `marketing-strategy` + GTM 适用性题材（[`templates.md`](./templates.md#part-3-marketing) §3.2 — **参考菜单**，非施工图）

> **templates 用法**：只读 Part 0 + **当前 articleType 对应 Part**（Tools→2 · Marketing→3 · SEO→4 · Insights→5）的节级建议；**禁止**按模板增删 H2。

## 2.4 05b 深度扩写（动笔后、Step 06 前）

- 每 major H2 含 **事实 + 场景 + 判断** 中至少两类（见 Part 0.2）
- 对照 [`word-counts.md`](./word-counts.md) 与 [`templates.md`](./templates.md) 节级建议区间；**不足则补论证**，不堆同义句
- 从 SSOT 抽**事件时间线**与**可核实数字**，勿只留表格摘要
- **删列表 / 改 prose 时**：同步删除孤立 `**标签：**` 行（E41）

## 2.5 05c 呈现债预检（Step 06 前）

对照 [`presentation.md`](./presentation.md) §Step 06 / 10；含 `childrenHtml` 的每个 H2 人工过 E40–E42。

**Best-ranking Meta**（Step 08）：title 含「最佳」+ `（2026）`；H1 不含最佳/年份

## 2.6 禁止

- 偏离 Brief One-line thesis / Moat
- 从知识块整段复制
- frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44）
- md 写 `#article-intro` / `#faq` / `#references` 指望渲染（JSON SSOT）
- Brief 省略 TL;DR/FAQ/Refs 但 JSON 仍留键（E10）

## 2.7 A 层检查

- [ ] 主体节覆盖 Brief Answer Blocks
- [ ] TL;DR / FAQ 与 Brief 一致
- [ ] Moat 已兑现
- [ ] **best-ranking**：产品 H3 定稿前过 [`sections.md`](./sections.md) Part 3.3 §3.3.0（客户 Tier）

---

<a id="part-3-step-06-中文地道化"></a>

# Part 3 · Step 06 · 中文地道化

## 3.1 流程

```
1. 术语统一（[`locale-glossary.md`](./locale-glossary.md) Part 1–2 · [`locale-glossary.json`](./locale-glossary.json)）
2. **GTM 禁腔**（Marketing/Blog：[`gtm-prose-voice.md`](./gtm-prose-voice.md) §2 — 禁分轨/同族分流/组合拳/姊妹篇等）
3. 去英译腔 — 箭头链改 prose；英文术语降频，中文主称
4. BLUF 三处复核（B1 TL;DR · B2 每 major H2 首段 · B3 FAQ 首句）
5. Author POV — 第一人称判断可读、可证伪
6. Extractability — Answer Blocks 可独立成 40–60 字段（见 extractability-checklist.md）
7. 段落节奏 — 长段≥3；伪列表清零；E40–E42
8. FAQ vs 正文 spot-check（相似度 <30%）
9. **Swap Test** 抽样 ≥3 处 + 独特性自评 ≥ L2（L0 不得 Pass）— 见 [`copy-quality.md`](./copy-quality.md) Part 2·4
10. audit-locale-voice.py --slug {slug}（Fail 则回改）
11. audit-marketing-md-render.py（Marketing/Blog 策略文；E40–E42）
```

## 3.2 术语要点

- 正文叙述用 **中文主称**（用量限额重置、**AI 提交署名** 等）
- 英文术语 **首次** 括号标注即可
- `keep_english` 内词（Codex、Credits、CLI、Agent）保留
- **attribution 分流**：Git/Co-Author → **提交署名 / AI 提交署名**；Paid Ads/UTM → **广告归因**

## 3.3 Pass 勾选

- [ ] 朗读一遍：无英译腔、无箭头链正文（Part 0.2）
- [ ] 每 H2 首段 BLUF
- [ ] Author POV（Brief）≥1 处第一人称——**在相关节内**
- [ ] 无 skills/runbook meta（E49）
- [ ] 无伪列表
- [ ] Extractability Pass
- [ ] Swap Test 抽样 Pass + 独特性 ≥ L2
- [ ] E40–E42 Pass

---

<a id="part-4-step-09-英文独立成稿"></a>

# Part 4 · Step 09 · 英文独立成稿

> **输入**：Brief + SSOT + **锚点 id 表** — **不是** ZH md 全文。  
> **产出**：`content/{channel}/en/{slug}.md`（路径与 Part 2.2 对称，locale 为 `en`）

## 4.1 独立成稿原则

- **结构 parity**：与 Brief 相同的 section 类型、顺序、**anchor id**（对齐**实际采用的**架构）
- **禁止逐句翻译 ZH**：从 Answer Blocks + Author POV **用英文重写**
- **同等论证深度**：Moat、数据、价格、日期、权衡逻辑须与 ZH **信息对等**（见 Part 5）
- **Kostja 第一人称**：*I* / *my read* 与 ZH「我」判断对齐
- **BLUF 三处**：各 major H2 首段 **≥3 句**；TL;DR intro 40–60 words；FAQ 首句即答
- **呈现不镜像坏债**：ZH 若有表前短桥接/孤立标签，EN **写正确 prose**，不复制缺陷
- TL;DR / FAQ / References：**Brief 采用则 EN 须有**；Step 08 注册 JSON（E10）

## 4.2 Step 09b · 英文地道化 Pass

- 对照 Part 0.2 英文正向/负向表；朗读一遍
- 改 telegraphic 句与 `→`
- **Swap Test**（英文独立轴，非翻译腔检查）— 同 [`copy-quality.md`](./copy-quality.md) Part 2
- 跑 `audit-locale-voice.py --slug {slug}`
- Marketing/Blog 策略文：跑 `audit-marketing-md-render.py`

## 4.3 字数

Marketing 叙事须**饱满**（见 [`word-counts.md`](./word-counts.md)）；Best 产品段 EN ≥280 字符。

## 4.4 A 层检查（09b 后）

- [ ] section 顺序与锚点 id 与 Brief 一致（非与 ZH 逐段对齐）
- [ ] md 以 `#conclusion` 收束
- [ ] FAQ：若采用则 7 问；内链若存在须 R4
- [ ] Moat + Author POV **同等深度**（非摘要版）
- [ ] EN native Pass（Part 0.2）
- [ ] E40–E42 Pass

## 4.5 B 层

- [ ] Meta 已在 `*-meta.ts` 注册 en 键
- [ ] **Final CTA**：`cta-config.json` → `slugs.{slug}.en`（见 [`sections.md`](./sections.md) Part 5）

---

<a id="part-5-step-09c-双语对等对比"></a>

# Part 5 · Step 09c · 双语对等对比

> **执行者**：协调者 / 主 Agent（**不是**翻译校对）。  
> **时机**：ZH 轨（06 Pass）与 EN 轨（09b Pass）**均完成**，Step 08 JSON 注册后、Step 10 前。

## 5.1 对比维度

| 维度 | Pass 标准 |
|------|-----------|
| **锚点 id** | 每个 `##` / `###` 的 `{#id}` ZH/EN **完全一致** |
| **节型对称** | 采用的 TL;DR / FAQ / How To / 对比表 等 **两边相同**（Brief 省略则两边都省略） |
| **Answer Blocks** | 每个 Block 在 ZH/EN 均有对应 H2；**缺块 = Fail** |
| **Moat** | Brief 登记的 Moat Asset 在 **两种语言** 均显式兑现 |
| **Author POV** | Brief 判断条目在 **两种语言** 均有可证伪表述（可不同句式） |
| **关键事实** | 日期、价格、产品名、限额数字、事件名 **一一对应**；禁止一侧具体一侧模糊 |
| **段落功能** | 同 id 下两段承担相同功能（定义/案例/判断/收束）；**不要求**句数相等 |
| **FAQ** | 若采用：7 问 **题意对等**（非逐句翻译）；内链 R4 各自遵守 |
| **内链** | 同 slug 链 **同一 URL**；全文各语种内 R4 各算各的 |

## 5.2 明确不做的事

- ❌ 把 EN 改成 ZH 的英译版
- ❌ 把 ZH 改成 EN 的汉译版
- ❌ 为对齐句数删论据或加 padding
- ✅ 仅当 **信息丢失 / 事实不对等 / 锚点漂移** 时，**分别**回改 ZH 或 EN 轨（注明回 Step 06 或 09b）

## 5.3 09c 勾选表

```markdown
## Parity Check — {slug}

| 检查项 | ZH | EN | 备注 |
|--------|----|----|------|
| 锚点 id 一致 | ☐ | ☐ | |
| Answer Blocks 全覆盖 | ☐ | ☐ | |
| Moat 兑现 | ☐ | ☐ | |
| Author POV 对等 | ☐ | ☐ | |
| 关键数字/日期对等 | ☐ | ☐ | 列差异：… |
| FAQ 7 问题意对等 | ☐/N/A | ☐/N/A | |
| 结论收束 md | ☐ | ☐ | |

**回改**：ZH → Step 06 · EN → Step 09b · 无 → Step 10
```

---

<a id="part-6-验收脚本与回退"></a>

# Part 6 · 验收脚本与回退

```bash
# 中文 / 英文地道化（locale-glossary.json → forbidden + localize_required）
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog

# Marketing/Blog 呈现债 E40–E42
python E:/clients/Alignify/scripts/audit/audit-marketing-md-render.py ...
```

| Fail | 回退 |
|------|------|
| audit-locale-voice（ZH forbidden / localize_required） | Step 06 · 对照 `locale-glossary.md` |
| audit-locale-voice（EN forbidden） | Step 09b · 对照 `locale-glossary.md` 附录 |
| audit-marketing-md-render | Step 06 或 09b（视语种） |
| 09c 信息不对等 | **分别**回改对应语种轨，**禁止**用翻译补齐 |

Fail → **不得**用同义词替换凑字数。

---

<a id="附录-a-禁腔对照速查"></a>

# 附录 A · 禁腔对照速查

> **SSOT**：[`locale-glossary.md`](./locale-glossary.md) 附录 · [`gtm-prose-voice.md`](./gtm-prose-voice.md)（GTM 相邻文）· `locale-glossary.json` → `forbidden_in_*` / `forbidden_regex_*`  
> 地道 workflow 判据见 Part 0.2；Step 06/09b 须对照附录 Pass。

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 合并 localization-quality · 05/06/09；新增双 Subagent 独立成稿 + 09c 对等对比 |
| 2026-08-27 | 术语 SSOT 迁至 locale-glossary；附录 A 改指针 |

*content-locale.md · v1.0 · 2026-08-27*
