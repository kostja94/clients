# What-is Section 优化方案与实施记录

## 概述

本文档记录了对 Alignify 全站 198 个 Tools 页面「什么是 XXX」section（What-is，即 TL;DR 之后第一个 `section` 类型 block）的系统优化过程，包括方法论、脚本、规则修订和结果，便于将相同流程复用到站内其他 H2 section（如「如何工作」「结论」「FAQ」等）。

---

## 一、方法论：规则先行，审计后改

### 核心原则

**不要直接改内容。** 正确顺序是：

1. **找到规则文档**（本目录 `section-*.md`、`../templates/template-*.md`）
2. **审计规则本身**——规则是否自洽？是否有硬底线与软建议分层？是否覆盖所有边界情况？
3. **优化规则，使之成为最佳实践**
4. **用脚本审计全站内容**，输出违规清单
5. **分批修复内容**，每批验证后继续
6. **终审确认零硬违规**

### 为什么这个顺序重要

- 直接改内容会导致「改完一个回头看规则不对，又要返工」
- 规则定义了「什么算合格」——规则没定好就动手，等于没有验收标准
- 先定规则再执行，可以写脚本批量审计和修复，而不是手工翻页

---

## 二、规则体系：三级分层

从 section-what-is.md 和 section-consistency.md 中提炼的三级体系：

| 层级 | 含义 | 违规后果 | 示例 |
|------|------|----------|------|
| **A 硬底线** | 不可逾越的最低标准 | 必须修复 | 段落数 ≥ 2、总字数/词数不超上限、必须有内链 |
| **B 强建议** | SERP/首屏相关，像素/字数导向 | 应修复 | meta title、H1、excerpt 长度 |
| **C 软建议** | 正文各 H2 与 JSON 块的篇幅区间 | 尽量贴近 | 「什么是」180–380c (ZH) / 150–280w (EN) |

**一致性重新定义**：跨页优先对齐 H2 语气、信息顺序、组件用法；正文字数允许在建议区间内随主题难度浮动。章内并列块避免约 3 倍以上长短悬殊即可，不要求逐项字数几乎相等。

### What-is Section 的硬底线

| 约束 | 中文 | 英文 | 说明 |
|------|------|------|------|
| 段落数 | ≥ 2 段 | ≥ 2 段 | 单段落为错误 |
| 绝对上限 | ≤ 450 字 | ≤ 350 词 | 防止篇幅失衡 |
| 绝对下限 | ≥ 150 字 | ≥ 100 词 | 防止信息空洞 |
| 内链 | ≥ 1 个强相关内链 | ≥ 1 个强相关内链 | 链接到相关工具页 |
| 段间比例 | < 3x | < 3x | 避免极长段 + 极短段并排 |

### 段落结构模板

| 类型 | 适用 | P0 | P1 | P2-P3 |
|------|------|-----|-----|--------|
| 标准型 | 80% 页面 | 定义 + 价值 + 适用人群 | 生态位置 + 相邻品类边界 | — |
| 扩展型 | 复杂概念 | 定义 + 价值 | 工作流与上下游 | 技术区分点 + 边界说明 |
| 小众/新兴型 | 新兴概念 | 概念解释 + 为什么值得关注 | 与成熟品类的对比定位 | — |

---

## 三、操作流程

### Step 1：审计脚本

```python
# 核心逻辑：遍历所有 JSON，找到 TL;DR 后的第一个 section block
def get_whatis_section(data):
    found_tldr = False
    for block in data.get("blocks", []):
        if block.get("type") == "tldr":
            found_tldr = True
            continue
        if found_tldr and block.get("type") == "section":
            return block
    return None

# 统计：strip HTML 后数字数/词数
def strip_html(text):
    return re.sub(r'<[^>]+>', '', text)

# ZH: len(strip_html(text))
# EN: len(strip_html(text).split())
```

### Step 2：分批修复

使用 Python 脚本批量操作 JSON 文件，**严禁用 Edit 工具编辑 JSON**（会引入格式问题）：

```python
# 标准修复模式
import json

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定位 what-is section
found_tldr = False
for block in data.get("blocks", []):
    if block.get("type") == "tldr":
        found_tldr = True
        continue
    if found_tldr and block.get("type") == "section":
        block["paragraphs"] = new_paragraphs  # 替换
        break

# 用 json.dump 写回（保证格式）
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### Step 3：每批验证

每批修复后立即运行审计脚本，确认硬违规数下降。不要在全部改完后再验证——出错时无法定位是哪一批引入的。

### Step 4：终审

全量审计，确认硬违规数为 0，记录软建议偏离数及其理由。

---

## 四、本轮的批量操作明细

### 4.1 EN 扩展（30 文件，<100w → 100+w）

| 批次 | 文件数 | 类别 | 脚本 |
|------|--------|------|------|
| B4 | 10 | browser, chatbot, productivity, workflow, spreadsheet, ocr, animation-library, design, website-builder, presentation-maker | expand_whatis_en_b4.py |
| B5 | 20 | api, avatar, community, directory, education, evaluation, family-assistant, filmmaking, healthcare, image-to-video, interview-assistant, knowledge-base, legal, lip-sync, memory, recruiting, religion, text-to-video, user-research, video | expand_whatis_en_b5.py |

**扩展模式**：
- P0：定义 + 核心价值 + 适用人群（目标 60-90w）
- P1：与相邻品类的边界 + 内链 + 工作流位置（目标 35-60w）
- 内链格式：`<a href='/tools/{slug}'>AI 工具名</a>`

### 4.2 ZH 修剪（10 文件，>450c → ≤450c）

| 批次 | 文件 | 原字数 → 新字数 |
|------|------|-----------------|
| B1 | openclaw-alternatives | 866 → 435c |
| B1 | character-chat | 667 → 378c |
| B1+B2 | authentication | 643 → 439c |
| B1 | agent-for-desktop | 544 → 434c |
| B1 | linkedin | 542 → 417c |
| B2 | web-scraping | 512 → 376c |
| B2 | background-changer | 508 → 390c |
| B2 | geo | 508 → 423c |
| B2 | web-search-api | 496 → 444c |
| B2 | agent-skills | 455 → 420c |

**修剪策略**：保留核心论点，合并冗余段落，删除修饰性语言。每个文件仍保留 ≥ 2 段。

### 4.3 段间比例修复（23 文件）

- **EN 10 文件**（background-changer, referral-program, notes-generator, lead-generation, b2b, text-generator, influencer-marketing, search-indexing, poster-generator, search-engine）
- **ZH 13 文件**（community, image-generator, b2b, presentation-maker, spreadsheet, browser, poster-generator, voice, design, text, llm, video-to-video, video-effects）

**策略**：不删 P0 内容，而是扩展 P1 使其成为有实质深度的生态位置说明（而非简单罗列交叉引用）。所有文件段间比例降至 < 3x。

### 4.4 EN 软目标推送（28 文件，100-149w → 150+w）

在 P1 中加入更详细的品类边界和协同说明，同时丰富内链。大部分文件增加 5-30 词即可达到软目标。

### 4.5 openclaw-alternatives EN 修剪（376w → 325w）

合并冗余段落，收紧表达，添加 agent-for-desktop 内链。

---

## 五、对后续 H2 section 优化的复用指南

### 适用的 H2 section 类型

| Section | 对应 block type | 规则文档 | 复用本方案需调整的点 |
|---------|-----------------|----------|---------------------|
| 如何工作 | `section`（第二个之后） | section-consistency.md | 硬底线字数区间不同，需先审计再定 |
| 结论 | `section`（FAQ 之前） | [alignify-conclusion.md](../../alignify-conclusion.md) | 篇幅软建议 + 高密度例外见真相源 §2.3 |
| FAQ | `faq` | section-faq.md | 不同 block type，审计脚本需适配 |
| HowToChoose | `howToChoose` | [section-how-to.md](../section-how-to.md) | 不同组件结构；定位分工、3–5 步、去模板见 SSOT |
| UseCases | `useCases` | section-consistency.md | 场景块的字数建议 |

### 复用步骤

1. **找到对应规则文档**在本目录和 `../templates/` 下
2. **审计规则**——是否有硬底线？字数区间是否合理？是否与 consistency 文档一致？
3. **写审计脚本**——参考本文 Step 1，适配目标 block type
4. **跑审计，分类违规**——硬违规（必须修）/ 软偏离（尽量修）
5. **先修规则文档，再改内容**
6. **分批修复**——每批 10-20 个文件，每批后验证
7. **终审确认**

### 关键注意点

- **不同 block type 的审计逻辑不同**：FAQ 是 `type: "faq"` 下的 `items[]`，HowToChoose 是 `type: "howToChoose"` 下的 `steps[]`
- **字数统计**：务必 `strip_html()` 后再数——ZH 数字数，EN 数词数
- **段间比例**：仅检查同一 section 内的并列段落，不跨 section 比较
- **内链唯一性**：FAQ 中不能有内链（独立规则），结论必须排在 FAQ 之前

---

## 六、修改过的文件清单

### 规则文档（4 个）

- `content/sections/section-what-is.md` — 全面重写，引入硬/软分层、三模板、反模式表
- `content/sections/section-consistency.md` — 第 43 行 EN 区间更新为 150-280 词
- `content/templates/template-tools.md` — 第 54 行同步
- `content/templates/template-marketing.md` — 第 51 行同步

### 内容文件（约 100 个 JSON）

- 30 个 EN tools JSON 扩展（<100w → 100+w）
- 10 个 ZH tools JSON 修剪（>450c → ≤450c）
- 23 个 JSON 段间比例修复
- 28 个 EN JSON 软目标推送
- 1 个 openclaw-alternatives EN 修剪

所有 JSON 操作使用 Python `json.dump()`，未使用 Edit 工具。

---

## 七、最终审计结果

| | ZH (99页) | EN (99页) |
|---|---|---|
| **硬违规 (A)** | **0** | **0** |
| 段落数 ≥ 2 | ✅ | ✅ |
| 绝对上限不超 | ✅ | ✅ |
| 绝对下限不低 | ✅ | ✅ |
| 至少 1 个内链 | ✅ | ✅ |
| 段间比例 < 3x | ✅ | ✅ |
| **软偏离 (C)** | 11 页略超 380c | 34 页略低 150w / 3 页略超 280w |

软偏离均有合理原因——复杂话题需要更多解释，已说清的话题加塞会冗余。

---

## 八、日期

- 规则优化与方案制定：2026-05-09
- 内容批量修复：2026-05-09 至 2026-05-10
- 终审通过：2026-05-10
