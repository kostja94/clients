#!/usr/bin/env python3
"""One-off: merge sections/*.md into rules/sections.md

NOTE: `sections/` 子目录已删除；本脚本仅作历史重建参考。增量合并 Part 4/5 用 merge-sections-conclusion-cta.py。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "skills" / "create-article" / "rules"
OUT = ROOT / "sections.md"
SECTIONS_DIR = ROOT / "sections"

PART0 = """# Alignify 章节规范（唯一真相源）

> **位置**：`skills/create-article/rules/sections.md`  
> **格式**：`content/{channel}/{locale}/{slug}.md` + JSON 侧车（TL;DR / FAQ / References）  
> **Last updated**：2026-08-27  
> **说明**：所有章节写法、选节决策、JSON 侧车、结论、Final CTA **仅在本文件维护**。结构映射见 [`anatomy.md`](./anatomy.md)；内链见 [`internal-links.md`](./internal-links.md)。  
> **增量合并**：`scripts/ops/merge-sections-conclusion-cta.py`（Part 4–5）；初版九文件合并见 `merge-sections-doc.py`。

---

## 目录

1. [Part 0 · 内容优先：如何选节](#part-0-内容优先如何选节)
2. [Part 1 · 全局写法（Markdown / H1–H6）](#part-1-全局写法markdown--h1h6)
3. [Part 2 · JSON 侧车三件套](#part-2-json-侧车三件套)
   - [2.1 TL;DR / 核心要点](#part-21-tldr--核心要点)
   - [2.2 FAQ / 常见问题](#part-22-faq--常见问题)
   - [2.3 References / 参考文献](#part-23-references--参考文献)
4. [Part 3 · 正文节型库（按需选用）](#part-3-正文节型库按需选用)
   - [3.1 什么是 XXX](#part-31-什么是-xxx)
   - [3.2 通用主体节（分析 / 场景 / 技术）](#part-32-通用主体节分析--场景--技术)
   - [3.3 Best 产品 H3（best-ranking）](#part-33-best-产品-h3best-ranking)
   - [3.4 对比表格](#part-34-对比表格)
   - [3.5 How To / 如何选择（可选）](#part-35-how-to--如何选择可选)
5. [Part 4 · 结论](#part-4-结论)
6. [附录 A · 节型 × articleType 速查](#附录-a-节型--articletype-速查)
7. [附录 B · A/B/C 底线汇总](#附录-b-abc-底线汇总)

---

<a id="part-0-内容优先如何选节"></a>

# Part 0 · 内容优先：如何选节

> **原则**：文章架构由**内容**决定；下文与 `templates/` 均为**参考菜单**，不是必填清单。详见 [`anatomy.md`](./anatomy.md) §〇。

## 选节三问（Step 01 / Brief）

1. 读者离开页面前**必须带走什么**？（定义 / 对比 / 决策路径 / 判断）
2. 哪一节能**单独删掉**而不伤主旨？→ 删
3. 两节是否在**说同一件事**？→ 合并

## 节型菜单（C 层建议）

| 读者需求 | 考虑采用的节 | 常见 articleType | 可省略条件 |
|----------|-------------|------------------|------------|
| 快速判断值不值 | TL;DR | 全部 | Brief 写理由 |
| 建立共同语言 | 什么是 | 几乎全部 | 极短快讯可并入首段 |
| 看产品差异 | Best H3 + 对比表 | best-ranking | 非榜单文 |
| 主体论证 / 场景 | 分析节 / 应用场景 H3 | marketing / insights | 由大纲决定 |
| 知道怎么选 | How To | tools / seo 操作文 | marketing / insights **默认不用** |
| 收束行动 | 结论 | 几乎全部 | — |
| 扫尾疑问 | FAQ | 常用 | Brief 省略 |
| 权威背书 | References | 有外部引用时 | 策略文仅 A/B 类源 |

## Brief Section Plan（推荐）

```markdown
| 节 | 采用 | 理由 |
|----|------|------|
| TL;DR | ✅ / ❌ | … |
| 什么是 | ✅ | … |
| How To | ❌ | 策略判断文，用分析节表达落地 |
| FAQ | ✅ | … |
```

## A 层硬底线（与采用哪些节无关）

- md 正文以 **`## 结论 {#conclusion}`** 收束；FAQ 由页底 `FAQ.tsx` 全局渲染（**不在 md 流内**）
- Brief **采用** FAQ → `faq-data.json` 中英文各 **7 问**；内链若存在须 R4 全文 1 次
- Brief **省略** TL;DR/FAQ/Refs → 三 JSON **不得**留对应 pathname 键
- **禁止** frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44）
- **禁止** md 写 `#article-intro` / `#faq` / `#references` 指望渲染
- ZH/EN **对齐实际采用的节**与 anchor id，不对齐「是否凑满 10 节」

---

"""

PART1 = """<a id="part-1-全局写法markdown--h1h6"></a>

# Part 1 · 全局写法（Markdown / H1–H6）

> 新文（2026-08+）：`content/blog/` 或 `content/tools/` 的 md + `<!-- block:section -->` + Markdown `##` / `###` + `{#anchor}`。详见 [`anatomy.md`](./anatomy.md) §四·一。

## 1.1 基本结构

```markdown
<!-- block:section -->
## 章节标题 {#kebab-case-id}

首段 BLUF ≥3 句（策略/marketing 文）。

第二段展开…

### 子节标题 {#sub-id}

…
```

- 列表 / 表格 → `childrenHtml`（`content-html` + 语义 class，E35）
- 段落 → 裸 Markdown，**禁止** inline Tailwind（E35）

## 1.2 H1 / H2 / excerpt

| 元素 | 来源 | 规范 |
|------|------|------|
| H1 | frontmatter `title` | [`meta.md`](./meta.md) §三 |
| excerpt | frontmatter `description` | [`meta.md`](./meta.md) §四 |
| H2/H3 | 正文 `##` / `###` | kebab-case `{#id}`；ZH/EN 同 slug 用相同 id |

## 1.3 H1–H6 层级

- **H1**：`[主题]：[价值]`；不写年份
- **H2 间距**：容器 `space-y-12`；正文 H2 之间**不加** divider（E36）
- 完整可访问性与字数见 [`meta.md`](./meta.md)、[`copy-quality.md`](./copy-quality.md)

---

<a id="part-2-json-侧车三件套"></a>

# Part 2 · JSON 侧车三件套

> **共性**：Brief 决定采用/省略 → **Step 08 注册 JSON**（键 = `pageUrl` 路径）。线上组件读 JSON；md 内对应 block 被 parser 跳过。

---

"""

PART4 = """
---

<a id="part-4-结论"></a>

# Part 4 · 结论

> **已合并**：完整正文见 [`sections.md`](./sections.md#part-4-结论) Part 4.1–4.9（由 `merge-sections-conclusion-cta.py` 维护）。

**A 层**：md 以 `## 结论 {#conclusion}` 收束；结论在 FAQ **之前**（页底 FAQ 为全局组件）。

---

<a id="附录-a-节型--articletype-速查"></a>

# 附录 A · 节型 × articleType 速查

| articleType | 几乎总是 | 常用 | 视题材 | 默认省略 |
|-------------|---------|------|--------|---------|
| best-ranking | 什么是 · 主体(Best H3) · 结论 | TL;DR · 对比表 · 应用场景 · How To · FAQ | References | — |
| seo-guide | 什么是 · 主体 · 结论 | TL;DR · How To · FAQ | References | How To（纯概念文） |
| marketing-strategy | 什么是 · 主体分析节 · 结论 | TL;DR · FAQ | References（A/B 源） | **How To**（观点/事件文） |
| insights-analysis | 主体 · 结论 | 什么是 · TL;DR · FAQ | References | How To · Best H3 |

**中英 parity**：对齐**实际采用的节**与 anchor id，不机械复制节数。

---

<a id="附录-b-abc-底线汇总"></a>

# 附录 B · A/B/C 底线汇总

| 层级 | 含义 | 章节相关示例 |
|------|------|-------------|
| **A** | 违反即 Fail | 结论收束 md；FAQ 7 问（若采用）；无 frontmatter `howTo:`；产品 H3 ≥2 款（best-ranking）；对比表 bestFor/pricing 非空 |
| **B** | 强建议 | TL;DR intro 30–100 字；什么是 180–380 字；How To 3–5 步（若采用） |
| **C** | 软建议 | 节型菜单顺序；GEO items 模板；References 条数区间 |

质检：A 层必 Pass；B/C 偏离须在 Brief 或 SelfCheck 说明理由。

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 初版：合并 `sections/` 九文件为单 SSOT；新增 Part 0 内容优先选节；`sections/*.md` 改 stub |

*sections.md · v1.0 · 2026-08-27*
"""


def strip_header(text: str) -> str:
    lines = text.splitlines()
    i = 0
    if i < len(lines) and lines[i].startswith("# "):
        i += 1
    while i < len(lines) and lines[i].strip() != "---":
        i += 1
    if i < len(lines):
        i += 1
    return "\n".join(lines[i:]).strip()


def main():
    chunks = [PART0, PART1]

    for fname, aid, title in [
        ("tldr.md", "part-21-tldr--核心要点", "2.1 TL;DR / 核心要点"),
        ("faq.md", "part-22-faq--常见问题", "2.2 FAQ / 常见问题"),
        ("references.md", "part-23-references--参考文献", "2.3 References / 参考文献"),
    ]:
        body = strip_header((SECTIONS_DIR / fname).read_text(encoding="utf-8"))
        chunks.append(f'<a id="{aid}"></a>\n\n## {title}\n\n{body}\n\n---\n\n')

    chunks.append(
        '<a id="part-3-正文节型库按需选用"></a>\n\n'
        "# Part 3 · 正文节型库（按需选用）\n\n"
        "> 按 Brief Section Plan **只写需要的节**；勿为凑模板加空章。\n\n---\n\n"
    )

    for fname, aid, title in [
        ("what-is.md", "part-31-什么是-xxx", "3.1 什么是 XXX"),
        ("generic.md", "part-32-通用主体节分析--场景--技术", "3.2 通用主体节（分析 / 场景 / 技术）"),
        ("best-tools.md", "part-33-best-产品-h3best-ranking", "3.3 Best 产品 H3（best-ranking）"),
        ("comparison-table.md", "part-34-对比表格", "3.4 对比表格"),
        ("how-to.md", "part-35-how-to--如何选择可选", "3.5 How To / 如何选择（可选）"),
    ]:
        body = strip_header((SECTIONS_DIR / fname).read_text(encoding="utf-8"))
        if fname == "generic.md":
            body = body.split("## 四、与专用章节的关系")[0].strip()
        chunks.append(f'<a id="{aid}"></a>\n\n## {title}\n\n{body}\n\n---\n\n')

    chunks.append(PART4)
    OUT.write_text("\n".join(chunks), encoding="utf-8")
    n = len(OUT.read_text(encoding="utf-8").splitlines())
    print(f"Wrote {OUT} ({n} lines)")


if __name__ == "__main__":
    main()
