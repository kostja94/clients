#!/usr/bin/env python3
"""Merge conclusion.md + final-cta.md into sections.md Part 4/5."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "skills" / "create-article" / "rules"
SECTIONS = ROOT / "sections.md"
CONCLUSION = ROOT / "conclusion.md"
FINAL_CTA = ROOT / "final-cta.md"

HEADER = """# Alignify 章节规范（唯一真相源）

> **位置**：`skills/create-article/rules/sections.md`  
> **格式**：`content/{channel}/{locale}/{slug}.md` + JSON 侧车（TL;DR / FAQ / References）  
> **Last updated**：2026-08-27  
> **说明**：所有章节写法、选节决策、JSON 侧车、**结论**、**Final CTA** 规则**仅在本文件维护**。`sections/`、`conclusion.md`、`final-cta.md` 均为跳转 stub。结构映射见 [`anatomy.md`](./anatomy.md)；内链见 [`internal-links.md`](./internal-links.md)。

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
6. [Part 5 · Final CTA（页底 SecondaryCta）](#part-5-final-cta页底-secondarycta)
7. [附录 A · 节型 × articleType 速查](#附录-a-节型--articletype-速查)
8. [附录 B · A/B/C 底线汇总](#附录-b-abc-底线汇总)
9. [附录 C · 相关文档索引](#附录-c-相关文档索引)

---

"""

PART4_INTRO = """<a id="part-4-结论"></a>

# Part 4 · 结论

> **渲染**：md 正文 `## 结论 {#conclusion}`；FAQ 在其后由页底 `FAQ.tsx` 全局渲染。  
> **内链专规**：本节 §4.4；全站规则见 [`internal-links.md`](./internal-links.md)。  
> **篇幅数字索引**：[`word-counts.md`](./word-counts.md) · [`consistency.md`](./consistency.md)

"""

PART5 = """<a id="part-5-final-cta页底-secondarycta"></a>

# Part 5 · Final CTA（页底 SecondaryCta）

> **渲染**：部署仓 `src/components/SecondaryCta.tsx`  
> **数据源 SSOT**：`src/data/cta-config.json` → `slugs.{slug}.{zh|en}`  
> **缺条目时**：回退 `fallback` 通用文案（「你的产品，值得被发现。」）——**禁止**新文上线时落入 fallback。  
> **与 Part 4 关系**：CTA title/description 从结论 / Author POV 提炼，**不复读** Meta description。

## 5.1 何时写入

| 时机 | 动作 |
|------|------|
| **Step 08** Meta + Config | 与 `*-meta.ts` 注册**同批**写入 `cta-config.json` |
| **Step 09 后** | EN 版 title/description 定稿后，**补齐** `slugs.{slug}.en` |
| **改版 slug** | 若结论/主叙事大变，同步更新 CTA；小改可不动 |

## 5.2 JSON 结构

```json
"{slug}": {
  "zh": {
    "title": "一句 punchline，≤28 字为宜",
    "description": "1–2 句，承接结论或 Author POV，≤60 字为宜",
    "cta": "开始合作"
  },
  "en": {
    "title": "One punchline sentence.",
    "description": "1–2 sentences tied to conclusion or thesis.",
    "cta": "Work with us"
  }
}
```

- **href 不写**：组件固定链 `/services`（中文自动加 `/zh` 前缀）
- **cta 按钮文案**：中文常用 `开始合作` · `获取帮助` · `看看我们怎么做`；英文常用 `Work with us` · `Get started` · `Get help`
- **slug 键**：与 md 文件名一致（如 `git-commit-attribution`），**非** URL path

## 5.3 写法原则

1. **承接正文，不复读 Meta description** — 用结论句、Author POV 或「我会把这篇文章收成…」的提炼  
2. **title = 可独立传播的 punchline** — 读者没读全文也能 get 核心判断  
3. **description = 下一步行动的理由** — 为什么找 Alignify / 为什么现在动  
4. **双语独立撰写** — EN 不是 ZH 直译；语气对齐 [`presentation.md`](./presentation.md)  
5. **Hub 页走 `exact`** — 仅 `/tools`、`/marketing` 等频道首页；**文章详情页一律 `slugs`**

## 5.4 Brief 必填字段（Step 02 定稿）

```markdown
**Final CTA**（Step 08 写入 cta-config.json）:
- ZH title: …
- ZH description: …
- EN title: …
- EN description: …
- cta 按钮: zh「开始合作」/ en「Work with us」（或见 §5.2）
```

Step 05 动笔前 Brief 里 ZH title/description **至少要有草案**；Step 09 EN 完稿后 EN 字段定稿。

## 5.5 验收

```powershell
node E:\\clients\\Alignify\\scripts\\ops\\merge-cta-slugs.mjs --check
```

- 输出 `Missing: 0` → Pass  
- 任一 slug 缺失 → Gate C **BLOCK**

## 5.6 常见错误

| 错误 | 正确 |
|------|------|
| 新文上线无 `slugs.{slug}` | Step 08 与 meta 同批注册 |
| 用 fallback 通用「好产品输的从来不是质量」 | 每篇定制 punchline |
| title 复制 Meta title | 从结论/POV 提炼 |
| EN 逐句翻译 ZH CTA | 独立重写 |
| slug 键写错（如 `git-commit`） | 与 `{slug}.md` 文件名一致 |

见 [`common-errors.md`](./common-errors.md) **E43**。

---

"""

APPENDIX_C = """<a id="附录-c-相关文档索引"></a>

# 附录 C · 相关文档索引

| 主题 | 文档 | 说明 |
|------|------|------|
| 各节字数表 | [`word-counts.md`](./word-counts.md) | TL;DR / 什么是 / 结论 / FAQ 数字索引 |
| Best H3 客户露出 | [`partner-products.md`](./partner-products.md) | Tier 1/2 商业规则；写法见 Part 3.3 |
| Best 产品截图 | [`product-screenshots.md`](./product-screenshots.md) | Step 04 操作；非节写法 |
| 跨页一致性 | [`consistency.md`](./consistency.md) | C 层软建议定位 |
| BLUF / Author voice | [`presentation.md`](./presentation.md) | 全节通用 |

---

"""

REVISION = """## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 初版：合并 `sections/` 九文件为单 SSOT；新增 Part 0 内容优先选节；`sections/*.md` 改 stub |
| 2026-08-27 | 合并 `conclusion.md` → Part 4 · `final-cta.md` → Part 5；附录 C 索引 |

*sections.md · v1.1 · 2026-08-27*
"""

PART_MAP = {
    "part-1-定位与作用": ("4.1", "定位与作用", "part-41-定位与作用"),
    "part-2-通用规范": ("4.2", "通用规范", "part-42-通用规范"),
    "part-3-页面类型差异": ("4.3", "页面类型差异", "part-43-页面类型差异"),
    "part-4-内链规则": ("4.4", "内链规则", "part-44-内链规则"),
    "part-5-实现方式": ("4.5", "实现方式", "part-45-实现方式"),
    "part-6-质量检查": ("4.6", "质量检查", "part-46-质量检查"),
    "part-7-相关文档与迁移说明": ("4.7", "相关文档与迁移说明", "part-47-相关文档与迁移说明"),
    "part-8-常见错误": ("4.8", "常见错误", "part-48-常见错误"),
    "part-9-修订记录": ("4.9", "修订记录", "part-49-修订记录"),
}


def strip_conclusion_preamble(text: str) -> str:
    lines = text.splitlines()
    i = 0
    if lines and lines[0].startswith("# "):
        i = 1
    while i < len(lines) and lines[i].strip() != "---":
        i += 1
    if i < len(lines):
        i += 1
    # skip TOC block until next ---
    while i < len(lines):
        if lines[i].strip() == "---":
            i += 1
            break
        i += 1
    return "\n".join(lines[i:]).strip()


def transform_conclusion(body: str) -> str:
    out = []
    for line in body.splitlines():
        m = re.match(r'<a id="(part-\d+-[^"]+)"></a>', line)
        if m:
            old_id = m.group(1)
            if old_id in PART_MAP:
                num, title, new_id = PART_MAP[old_id]
                out.append(f'<a id="{new_id}"></a>')
                out.append("")
                out.append(f"## {num} {title}")
                out.append("")
            continue
        if line.startswith("# Part "):
            continue
        # renumber ## 2.x under 4.2 → ### 4.2.x
        m2 = re.match(r"^(#{2,6})\s+(\d+\.\d+(?:\.\d+)?)\s", line)
        if m2:
            hashes, sec = m2.group(1), m2.group(2)
            if sec.startswith(("2.", "3.", "4.", "5.", "6.", "8.")):
                major = sec.split(".")[0]
                mapping = {"2": "4.2", "3": "4.3", "4": "4.4", "5": "4.5", "6": "4.6", "8": "4.8"}
                if major in mapping:
                    rest = sec[len(major) :]
                    new_sec = mapping[major] + rest
                    line = re.sub(r"^#{2,6}\s+\d+\.\d+(?:\.\d+)?", f"{'#' * len(hashes)} {new_sec}", line)
        out.append(line)
    # drop migration table pointing to old conclusion.md as SSOT
    text = "\n".join(out)
    text = text.replace(
        "`skills/create-article/rules/templates.md` | 结论位置/篇幅/内链见本文件 §2/§3/§4 与各 Part",
        "`sections.md` Part 4 | 结论 SSOT",
    )
    text = re.sub(
        r"# Part 7 · 相关文档与迁移说明[\s\S]*?(?=<a id=\"part-49-修订记录\">)",
        "",
        text,
    )
    return text.strip()


def main():
    raw = SECTIONS.read_text(encoding="utf-8")
    # body: from part-0 through end of part 3 (before part-4)
    start = raw.find("<a id=\"part-0-内容优先如何选节\">")
    part4 = raw.find("<a id=\"part-4-结论\">")
    appendix_a = raw.find("<a id=\"附录-a-节型--articletype-速查\">")
    if start < 0 or part4 < 0 or appendix_a < 0:
        raise SystemExit("Could not find section boundaries in sections.md")

    body_before = raw[start:part4]
    appendix_tail = raw[appendix_a:]

    conclusion_body = transform_conclusion(strip_conclusion_preamble(CONCLUSION.read_text(encoding="utf-8")))

    merged = (
        HEADER
        + body_before
        + PART4_INTRO
        + conclusion_body
        + "\n\n---\n\n"
        + PART5
        + appendix_tail.replace(
            "*sections.md · v1.0 · 2026-08-27*",
            REVISION.split("*sections.md")[1].strip(),
        )
    )
    # inject appendix C before revision block
    rev_marker = "## 文档修订"
    if rev_marker in merged and APPENDIX_C.strip() not in merged:
        merged = merged.replace(rev_marker, APPENDIX_C + rev_marker, 1)

    # fix revision footer
    merged = re.sub(r"\*sections\.md · v[\d.]+\ · [\d-]+\*", REVISION.split("\n")[-1], merged)

    SECTIONS.write_text(merged, encoding="utf-8")
    n = len(merged.splitlines())
    print(f"Wrote {SECTIONS} ({n} lines)")


if __name__ == "__main__":
    main()
