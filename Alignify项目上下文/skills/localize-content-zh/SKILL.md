---
name: localize-content-zh
description: >-
  Alignify 中文内容本地化：seo/marketing/insights/blog/tools JSON 的地道化、术语统一、
  References 中文化、与英文结构 parity。在优化 zh JSON、审查翻译质量、修复中英不一致时使用。
---

# Localize Content ZH — Alignify 中文本地化 Skill

> **版本**：v1.0 · 2026-06-23  
> **适用范围**：`content/{seo,marketing,insights,tools,blog}/zh/*.json`  
> **标杆页**：`content/insights/zh/reasons-you-need-seo.json`

---

## 何时使用

- 中英文 **结构已对齐**，但中文仍像英译稿
- 新建/扩写中文页后做 **地道化润色**
- References title 英文残留、术语 CTR/CTA/ROI 混用
- 运行 `audit-zh-en-parity.py` / `audit-localization-quality.py` 后逐页修复

**不适用**：知识块撰写（用 `knowledge/tools/_TEMPLATE.md`）；英文意译（用 `create-tools-article/04-english-localization.md`）

---

## 流程（逐页）

```
1. 读 en + zh JSON，确认 block 类型与顺序一致
2. 按 01-terminology-and-style.md 润色正文
3. 按 02-references-and-metadata.md 修 blogLayout + references
4. 对照 en FAQ：信息等价，允许中文更简练
5. 运行 deploy 仓 audit 脚本验收
```

部署仓验收命令（在 `alignify-by-kostja`）：

```bash
python scripts/permanent/audit-zh-en-parity.py
python scripts/permanent/audit-localization-quality.py
```

---

## 核心规则（摘要）

| 维度 | 中文页要求 |
|------|-----------|
| **文风** | 行业长文口吻；避免「该标签用于…」连续说明书腔 |
| **术语** | 正文用中文指标名（点击率、行动号召、投入产出比）；缩写首次可「点击率（CTR）」 |
| **小节标题** | 中文为主：`页面描述（meta description）`；禁止 `Description：页面描述` |
| **专有名词** | 保留 Google、Open Graph、robots、viewport；协议/标签名可保留英文 |
| **内链** | 中文页 `href="/zh/..."` |
| **References** | **title + description 均中文**（见 section-references.md §2.5） |
| **blogLayout** | 日期 `2026年6月8日`；readTime `14 分钟阅读`；title 中英文间加空格 |
| **与 EN** | 语义等价；FAQ 条数一致；不要求字数机械对齐 |

---

## 详细文档

| 文档 | 内容 |
|------|------|
| [`01-terminology-and-style.md`](./01-terminology-and-style.md) | 术语表、小节标题、直译腔改写 |
| [`02-references-and-metadata.md`](./02-references-and-metadata.md) | References、blogLayout、FAQ 对等 |
| [`03-per-page-workflow.md`](./03-per-page-workflow.md) | 检查清单 + 频道优先级 |

---

## 与 create-tools-article 的关系

- **Step 2** 产出中文初稿 → 本 Skill **润色定稿**
- **Step 4** 英文意译 → 见 `04-english-localization.md`（勿与本 Skill 混淆）

在 `create-tools-article/SKILL.md` 中，中文 JSON 完成后应加载本 Skill 做本地化 pass。

---

## 脚本（部署仓）

| 脚本 | 用途 |
|------|------|
| `scripts/permanent/audit-zh-en-parity.py` | 结构 parity |
| `scripts/permanent/audit-localization-quality.py` | 本地化启发式扫描 |
| `scripts/permanent/polish-zh-page.py` | 单页术语替换 + references 模板（见脚本 `--help`） |

JSON 修改遵守部署仓 Windows 规则：**仅用 Python 脚本写 `.json`**。
