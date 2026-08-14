# 归档系统文档

> 适用于 `D:\项目文档\clients\others\` 下所有暂停合作客户的归档管理。
> 包含：规范文档 + JSON 配置 + Python 生成器。
> 最后更新: 2026-05-31

---

## 一、归档规范

# 归档文档规范

> 适用于 `D:\项目文档\clients\others\` 下所有暂停合作客户的归档文档。
> 最后更新: 2026-05-31

---

## 1. 目录结构

**每个项目必须有一个独立文件夹**，不允许单文件放在根目录。

| 规则 | 说明 |
|------|------|
| **一个项目 = 一个文件夹** | 文件夹名用小写连字符，内含 `{name}.md` 主索引 |
| 补充材料放同一文件夹 | 加 `-draft`、`-supplement`、`-copy` 等后缀 |
| 根目录仅保留系统文件 | README.md、ARCHIVE-SYSTEM.md 等

---

## 2. 文件命名

**规则：** 仅用小写字母、数字、连字符。不含空格、中文、下划线。

```
正确:  crepal-ai-vlog.md
       aisheet.md
       use-cases-copy-draft.md

错误:  CrePal文案.md
       ai_sheet_archive.md
       Medeo Use Cases.md
```

**特殊情况：**
- 同公司多产品：`{主产品}-{副产品}.md`，如 `crepal-ai-vlog.md`
- 补充文件（不覆盖已有文档）：加 `-draft` 后缀，如 `use-cases-copy-draft.md`
- 从混合来源提取的片段：加 `-copy` 后缀

---

## 3. 文档头部元数据

每个归档文档必须在顶部包含以下元数据块：

```markdown
# {客户名} — 归档文档

> 归档日期: YYYY-MM-DD
> 来源: {原始文件名，逗号分隔}
> 产品: {官网 URL，如有}
> 状态: 暂停合作
```

**必填字段：**
- `归档日期` — 文件创建日期
- `来源` — 原始材料文件名（便于追溯）
- `状态` — 固定为「暂停合作」

**可选字段：**
- `产品` — 官网链接
- `备注` — 补充说明，如品牌名变更、材料状态等

---

## 4. 内容编排

### 4.1 来源文件按节排列

每个来源文件对应一个一级标题（`##`），按重要程度排序：

```markdown
## 1. 页面优化
## 2. 竞品调研
## 3. 关键词调研
## 4. SEO 文案
```

标题取源文件名去掉扩展名后的部分，中英文均可，保持可读。

### 4.2 xlsx 内容

每个 sheet 转为 markdown 表格。规则：
- 过滤全空行
- 第一非空行作表头；空表头自动填 `Col1, Col2, ...`
- 空 sheet 标记 `*(空表)*`
- 表格不宜过宽：超过 5 列考虑拆分为多个小表或仅保留关键列

### 4.3 markdown 内容

直接嵌入，保持原格式。注意：
- 原文中的 `\&\#39;` 等 HTML 实体替换为正常字符（`'`）
- 原文中的 `\&\#34;` 替换为 `"`
- 原文中的 `\#` 替换为 `#`（markdown 标题）

---

## 5. 品牌名归属

### 5.1 原则

**一个归档文档只属于一个客户/公司。** 不同公司的材料绝不合并到同一文档。

### 5.2 混合来源处理

源文件中出现多个品牌名混用时，按以下优先级判定归属：

1. **Meta Title 中的品牌名** — 最高优先级。如 `<meta title="CrePal Features">` 归属 CrePal
2. **Permalink 路径** — 如 `/features`、`/use-cases` 有助于判断目标站
3. **正文高频品牌名** — 辅助判定
4. **文件名** — 最低优先级，仅作参考

判定后，对正文中不匹配的品牌名做规范化替换（`brand_normalize`）。

### 5.3 规范化替换

在 `archive-config.json` 中配置：

```json
"brand_normalize": {
  "Medeo accepts": "CrePal accepts",
  "Medeo integrates": "CrePal integrates"
}
```

替换规则：
- 原文中每处不属于本品牌的名称必须替换
- 替换字符串尽量长且唯一，避免误伤（如 `CrePal` 可能出现在 URL 中）
- FAQ 中的品牌名问题也需替换（`What video formats does Medeo support?` → `What video formats does CrePal support?`）

---

## 6. README.md 维护

`others/README.md` 是归档索引。新增归档后同步更新：

```markdown
| 文件夹 | 主文档 |
|--------|--------|
| [aisheet](./aisheet.md) | AI Sheet |
| [crepal-ai-vlog](./crepal-ai-vlog.md) | CrePal / AI Vlog |
```

### 护规则：
- 仅列出「当前不合作」的客户
- 已恢复合作的移出此表
- `另见` 行保留单文件归档的引用

---

## 7. archive-config.json 规范

### 7.1 条目格式

```json
{
  "name": "客户名（用于文档标题）",
  "output": "输出文件名（遵循第2节命名规则）",
  "description": "一行说明（产品/URL/备注）",
  "links": [],
  "source_files": ["源文件1.xlsx", "源文件2.md"],
  "brand_normalize": {
    "旧品牌文本": "新品牌文本"
  }
}
```

### 7.2 配置原则

- `source_files` 按文件在归档中的出现顺序排列
- 同一源文件可以被多个 client 引用（如 `CrePal文案.md` 同时用于 CrePal 和 Medeo）
- `brand_normalize` 仅在源文件内容混用品牌名时配置，单品牌源文件不需要
- `output` 路径可以包含子目录（如 `medeo/use-cases-copy-draft.md`）

---

## 8. 归档流程

```
1. 收集材料 → 放入 materials/ 文件夹
2. 判定归属 → 按 Meta Title / Permalink 确定品牌
3. 配置映射 → 编辑 archive-config.json
4. 运行生成 → python3 archive-generator.py
5. 人工复核 → 检查品牌名是否规范、表格是否完整
6. 更新索引 → 同步 README.md
7. 清理材料 → 删除 materials/ 中的原始文件（已归档）
```

---

## 9. 反例

以下做法**不允许**：

- 多个客户的材料合并到同一个归档文档
- 文件名含中文、空格或大小写混用
- 归档文档无日期、无来源追溯
- 正文中残留其他品牌名称未做规范化替换
- xlsx 内容仅写"见附件"而不转为可读表格
- 覆盖已有归档文件夹中的现有文档（应新建补充文件）
- README.md 未同步更新

---

*此规范自身遵循其定义的规则。*


---

## 二、归档配置 (archive-config.json)

```json
{
  "_说明": "每个 client 条目定义: name(归档名), output(输出文件名), source_files(材料列表), brand_normalize(可选,品牌名规范替换)",
  "_用法": "python3 archive-generator.py --config archive-config.json --source ./materials --output ./",
  "clients": [
    {
      "name": "AI Sheet",
      "output": "aisheet/aisheet.md",
      "description": "产品: https://aisheet.ai",
      "links": [],
      "source_files": [
        "AIsheet.ai.xlsx",
        "文案.md"
      ]
    },
    {
      "name": "CrePal / AI Vlog",
      "output": "crepal-ai-vlog/crepal-ai-vlog.md",
      "description": "产品: CrePal (Chat-to-Edit AI Video) + AI Vlog (同公司)",
      "links": [],
      "source_files": [
        "CrePal文案.md"
      ],
      "brand_normalize": {
        "Medeo accepts": "CrePal accepts",
        "Medeo adapts": "CrePal adapts",
        "Medeo integrates": "CrePal integrates",
        "What video formats does Medeo support?": "What video formats does CrePal support?"
      }
    },
    {
      "name": "SynthMind",
      "output": "synthmind/synthmind.md",
      "description": "产品: https://synthmind.app/ (AI Social Marketer: Auto-Create Viral Content, Auto-Engagement, Auto-Lead Generation)",
      "links": [],
      "source_files": [
        "SynthMind文案.md",
        "Synthmind.xlsx"
      ]
    },
    {
      "name": "Medeo",
      "output": "medeo/use-cases-copy-draft.md",
      "description": "产品: https://medeo.app (已有完整归档在 medeo/ 文件夹,此为补充文案稿)",
      "links": [],
      "source_files": [
        "CrePal文案.md"
      ],
      "brand_normalize": {
        "CrePal Features": "Medeo Features",
        "CrePal's innovative": "Medeo's innovative",
        "CrePal goes beyond": "Medeo goes beyond",
        "CrePal Use Cases": "Medeo Use Cases",
        "CrePal's comprehensive": "Medeo's comprehensive",
        "CrePal allows": "Medeo allows",
        "CrePal's AI understands": "Medeo's AI understands",
        "CrePal supports": "Medeo supports",
        "CrePal can handle": "Medeo can handle"
      }
    },
    {
      "name": "Simular",
      "output": "simular/simular.md",
      "description": "产品: https://simular.ai (Open-source AI Agent for Computer Use)",
      "links": [],
      "source_files": [
        "simular-optimization.xlsx",
        "Simular文案.md"
      ]
    },
    {
      "name": "Soku",
      "output": "soku/soku.md",
      "description": "产品: https://soku.ai/ — AI Advertising Agent for Meta Ads",
      "links": [],
      "source_files": [
        "文案.md",
        "Soku SEO SOP.xlsx"
      ]
    },
    {
      "name": "Cofidein",
      "output": "cofidein/cofidein.md",
      "description": "Cofidein (AI Bible Chat / Prayer / Sermon Generator)",
      "links": [],
      "source_files": [
        "Cofidein SEO.xlsx"
      ]
    },
    {
      "name": "Collov AI - 补充文案",
      "output": "collov/collov-copy-draft.md",
      "description": "https://collov.ai (已有完整归档在 collov/ 文件夹，此为补充文案+结构图)",
      "links": [],
      "source_files": [
        "Collov AI文案.md",
        "Collov AI网站结构可视化（修改完之后）.mm"
      ]
    },
    {
      "name": "Dubbing AI",
      "output": "dubbing/dubbing.md",
      "description": "https://dubbing.ai (AI Voice Changer, Real-time AI Voice)",
      "links": [],
      "source_files": [
        "Dubbing AI.xlsx",
        "Dubbing AI affiliate文案.md",
        "Dubbing AI网站结构可视化.mm"
      ]
    },
    {
      "name": "Kusa.Pics",
      "output": "kusa-pics/kusa-pics.md",
      "description": "https://kusa.pics (AI Anime/Manga/Character Generator)",
      "links": [],
      "source_files": [
        "Kusa.Pics.xlsx"
      ]
    },
    {
      "name": "Make Film",
      "output": "make-film/make-film.md",
      "description": "https://makefilm.ai (AI Film Tool)",
      "links": [],
      "source_files": [
        "Make Film.xlsx"
      ]
    },
    {
      "name": "PaperGen",
      "output": "papergen/papergen.md",
      "description": "PaperGen (AI Paper Generator)",
      "links": [],
      "source_files": [
        "PaperGen.xlsx"
      ]
    },
    {
      "name": "Pattern Look",
      "output": "pattern-look/pattern-look.md",
      "description": "https://patternlook.ai (AI Pattern Generator for Textiles)",
      "links": [],
      "source_files": [
        "Pattern Look项目.xlsx",
        "Pattern Look SEO文案.md",
        "Pattern Look网站结构可视化.mm"
      ]
    },
    {
      "name": "Pine AI",
      "output": "pine-ai/pine-ai.md",
      "description": "Pine AI",
      "links": [],
      "source_files": [
        "Pine AI.xlsx",
        "Pine AI结构可视化模板.mm"
      ]
    },
    {
      "name": "RockFlow",
      "output": "rockflow/rockflow.md",
      "description": "RockFlow",
      "links": [],
      "source_files": [
        "RockFlow.xlsx",
        "RockFlow网站结构可视化.mm"
      ]
    },
    {
      "name": "Streaml",
      "output": "streaml/streaml.md",
      "description": "Streaml (AI Agent for SDR/BDR)",
      "links": [],
      "source_files": [
        "Streaml.md"
      ]
    },
    {
      "name": "Tripo Shop",
      "output": "tripo-shop/tripo-shop.md",
      "description": "Tripo Shop",
      "links": [],
      "source_files": [
        "Tripo Shop网站结构可视化.mm"
      ]
    },
    {
      "name": "Lessie",
      "output": "lessie/lessie-supplement.md",
      "description": "https://lessie.ai (   )",
      "links": [],
      "source_files": [
        "Lessie.xlsx"
      ]
    },
    {
      "name": "Medeo",
      "output": "medeo/medeo-optimization-draft.md",
      "description": "https://medeo.app (   )",
      "links": [],
      "source_files": [
        "Medeo优化方案.xlsx",
        "Medeo文案.md",
        "Medeo网站结构可视化.mm"
      ]
    },
    {
      "name": "DolphinRadar",
      "output": "dolphinradar/dolphinradar.md",
      "description": "DolphinRadar (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar / Erasa",
      "output": "dolphinradar/dolphinradar-erasa.md",
      "description": "Erasa (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar / Moms GPTs",
      "output": "dolphinradar/dolphinradar-moms-gpts.md",
      "description": "Moms GPTs (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar / Hairpaca",
      "output": "dolphinradar/dolphinradar-hairpaca.md",
      "description": "Hairpaca (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar / Planbowl",
      "output": "dolphinradar/dolphinradar-planbowl.md",
      "description": "Planbowl (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar / InstantKnow",
      "output": "dolphinradar/dolphinradar-instantknow.md",
      "description": "InstantKnow (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "DolphinRadar 网站结构",
      "output": "dolphinradar/dolphinradar-site-structure.md",
      "description": "刀豆-网站结构 (刀豆.xlsx)",
      "links": [],
      "source_files": [
        "刀豆.xlsx"
      ]
    },
    {
      "name": "Abaka AI",
      "output": "abaka-ai/abaka-ai.md",
      "description": "Abaka AI (Mooredata Platform)",
      "links": [],
      "source_files": [
        "Abaka AI.xlsx",
        "Abaka AI文章.md",
        "Abaka网站结构可视化.mm"
      ]
    },
    {
      "name": "Beyz",
      "output": "beyz/beyz.md",
      "description": "Beyz (Interview Assistant)",
      "links": [],
      "source_files": [
        "Beyz网站结构可视化.mm"
      ]
    },
    {
      "name": "Coura.AI",
      "output": "coura-ai/coura-ai.md",
      "description": "https://coura.ai (AI Fashion/Style)",
      "links": [],
      "source_files": [
        "Coura.AI.xlsx",
        "Coura网站结构可视化.mm"
      ]
    },
    {
      "name": "CraveU",
      "output": "craveu/craveu.md",
      "description": "https://craveu.ai (AI Chat/Character Platform)",
      "links": [],
      "source_files": [
        "CraveU 网站结构可视化.mm"
      ]
    },
    {
      "name": "DICA",
      "output": "dica/dica.md",
      "description": "DICA (UX Testing/Prototype Platform)",
      "links": [],
      "source_files": [
        "DICA.xlsx",
        "DICA网站结构可视化.mm"
      ]
    },
    {
      "name": "Edensign",
      "output": "edensign/edensign.md",
      "description": "Edensign (E-signature Platform)",
      "links": [],
      "source_files": [
        "Edensign SEO优化.xlsx"
      ]
    },
    {
      "name": "FalcoCut",
      "output": "falcocut/falcocut.md",
      "description": "FalcoCut (AI Face Swap)",
      "links": [],
      "source_files": [
        "FalcoCut.xlsx",
        "FalcoCut结构可视化模板.mm"
      ]
    },
    {
      "name": "Talkie",
      "output": "talkie/talkie.md",
      "description": "Talkie (AI Character Chat)",
      "links": [],
      "source_files": [
        "Talkie结构可视化.mm",
        "增长计划.xlsx"
      ]
    },
    {
      "name": "Coura.AI - Blog 竞品文章",
      "output": "coura-ai/coura-blog-competitors.md",
      "description": "https://coura.ai (竞品 Blog 文章参考)",
      "links": [],
      "source_files": [
        "Blog文章.md"
      ]
    },
    {
      "name": "FalcoCut Blog",
      "output": "falcocut/falcocut-blog-draft.md",
      "description": "FalcoCut Blog 文章合集",
      "links": [],
      "source_files": [
        "Blog文章 (1).md"
      ]
    },
    {
      "name": "Fancy Tech",
      "output": "fancy-tech/fancy-tech.md",
      "description": "Fancy Tech (3D AI短视频)",
      "links": [],
      "source_files": [
        "Fancy Tech.xlsx",
        "Fancy结构可视化.mm"
      ]
    },
    {
      "name": "Fellou",
      "output": "fellou/fellou.md",
      "description": "Fellou",
      "links": [],
      "source_files": [
        "Fellou.xlsx",
        "Fellou资料.md",
        "Fellou网站结构可视化.mm",
        "落地页文案.md"
      ]
    },
    {
      "name": "GMI",
      "output": "gmi/gmi.md",
      "description": "GMI",
      "links": [],
      "source_files": [
        "GMI.xlsx"
      ]
    },
    {
      "name": "Goenhance",
      "output": "goenhance/goenhance.md",
      "description": "Goenhance",
      "links": [],
      "source_files": [
        "Goenhance.xlsx",
        "Goenhance结构可视化.mm"
      ]
    },
    {
      "name": "Joyland",
      "output": "joyland/joyland.md",
      "description": "Joyland",
      "links": [],
      "source_files": [
        "Joyland优化方案.xlsx"
      ]
    },
    {
      "name": "Kaze AI",
      "output": "kaze-ai/kaze-ai.md",
      "description": "Kaze AI",
      "links": [],
      "source_files": [
        "Kaze AI.xlsx",
        "Kaze AI网站结构可视化.mm"
      ]
    },
    {
      "name": "MolyPix",
      "output": "molypix/molypix.md",
      "description": "MolyPix",
      "links": [],
      "source_files": [
        "MolyPix.xlsx"
      ]
    },
    {
      "name": "Powerdrill",
      "output": "powerdrill/powerdrill.md",
      "description": "Powerdrill",
      "links": [],
      "source_files": [
        "Powerdrill.xlsx"
      ]
    },
    {
      "name": "SellerPic",
      "output": "sellerpic/sellerpic.md",
      "description": "SellerPic",
      "links": [],
      "source_files": [
        "SellerPic.xlsx",
        "SellerPic网站结构可视化.mm"
      ]
    },
    {
      "name": "VoiSpark - 声音落地页",
      "output": "voispark/voispark-voice-landing.md",
      "description": "https://voispark.com (Voice Actor Library — 455 voice entries)",
      "links": [],
      "source_files": [
        "Voispark声音落地页.xlsx"
      ]
    },
    {
      "name": "Tunee / Tempolor",
      "output": "tunee/tunee-tempolor.md",
      "description": "Tunee (Tempolor 已停止运营)",
      "links": [],
      "source_files": [
        "tempolor.md"
      ]
    }
  ]
}
```

---

## 三、归档生成器 (archive-generator.py)

```python
#!/usr/bin/env python3
"""
Archive document generator.

Usage: put source materials in a folder, configure archive-config.json, run this script.
  python3 archive-generator.py --config archive-config.json --source ./materials --output ./

Requires: pip install openpyxl --break-system-packages
"""

import json
import os
import sys
import argparse
from datetime import date
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("Install openpyxl: pip install openpyxl --break-system-packages")
    sys.exit(1)


def read_xlsx_sheets(filepath):
    """Read all sheets from xlsx, return {sheet_name: [[cell, ...], ...]}"""
    wb = openpyxl.load_workbook(filepath, data_only=True)
    result = {}
    for name in wb.sheetnames:
        ws = wb[name]
        rows = []
        for row in ws.iter_rows(values_only=True):
            rows.append([str(c) if c is not None else "" for c in row])
        result[name] = rows
    return result


def xlsx_to_markdown(sheets):
    """Convert xlsx sheets dict to markdown tables"""
    md = ""
    for sheet_name, rows in sheets.items():
        md += "## {}\n\n".format(sheet_name)
        non_empty = [r for r in rows if any(c.strip() for c in r)]
        if not non_empty:
            md += "*(empty sheet)*\n\n"
            continue

        header = non_empty[0]
        col_count = max(len(row) for row in non_empty)
        header = list(header) + [""] * (col_count - len(header))
        header = [h if h.strip() else "Col{}".format(i+1) for i, h in enumerate(header)]

        md += "| " + " | ".join(header) + " |\n"
        md += "|" + "|".join(["---"] * col_count) + "|\n"

        for row in non_empty[1:]:
            padded = list(row) + [""] * (col_count - len(row))
            md += "| " + " | ".join(padded) + " |\n"
        md += "\n"
    return md


def read_md(filepath):
    """Read markdown file"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def apply_normalize(content, rules):
    """Apply brand name normalization: {old_text: new_text}"""
    for old, new in rules.items():
        content = content.replace(old, new)
    return content


def generate_archive(client_name, source_files, source_dir, output_dir,
                     brand_normalize=None, description="", links=None):
    """Generate archive markdown for one client"""
    lines = []
    lines.append("# {} -- Archive".format(client_name))
    lines.append("")
    lines.append("> Date: {}".format(date.today().isoformat()))
    fnames = ", ".join(Path(f).name for f in source_files)
    lines.append("> Source: {}".format(fnames))
    if description:
        lines.append("> {}".format(description))
    if links:
        for link in links:
            lines.append("> {}".format(link))
    lines.append("> Status: paused")
    lines.append("")
    lines.append("---")
    lines.append("")

    section_num = 0
    for fname in source_files:
        fpath = os.path.join(source_dir, fname)
        if not os.path.exists(fpath):
            lines.append("> WARNING: file not found: {}".format(fname))
            lines.append("")
            continue

        section_num += 1
        ext = Path(fname).suffix.lower()

        if ext == ".xlsx":
            sheets = read_xlsx_sheets(fpath)
            lines.append("## {}. {}".format(section_num, Path(fname).stem))
            lines.append("")
            lines.append(xlsx_to_markdown(sheets))

        elif ext == ".md":
            content = read_md(fpath)
            if brand_normalize:
                content = apply_normalize(content, brand_normalize)
            lines.append("## {}. {}".format(section_num, Path(fname).stem))
            lines.append("")
            lines.append(content)
            lines.append("")

        else:
            lines.append("## {}. {}".format(section_num, Path(fname).name))
            lines.append("")
            lines.append("> *(binary file, review manually: {})*".format(fpath))
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Archive complete.*")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Archive document generator")
    parser.add_argument("--config", default="archive-config.json")
    parser.add_argument("--source", default=".")
    parser.add_argument("--output", default=".")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print("Config not found: {}".format(args.config))
        print("Create archive-config.json (see archive-config.json for example)")
        sys.exit(1)

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    source_dir = args.source
    output_dir = args.output
    os.makedirs(output_dir, exist_ok=True)

    generated = []
    for entry in config.get("clients", []):
        client_name = entry["name"]
        out_name = entry.get("output", "{}.md".format(client_name.lower().replace(" ", "-")))
        source_files = entry["source_files"]
        brand_normalize = entry.get("brand_normalize")
        description = entry.get("description", "")
        links = entry.get("links", [])

        content = generate_archive(
            client_name=client_name,
            source_files=source_files,
            source_dir=source_dir,
            output_dir=output_dir,
            brand_normalize=brand_normalize,
            description=description,
            links=links,
        )

        output_path = os.path.join(output_dir, out_name)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        size_kb = len(content.encode("utf-8")) / 1024
        generated.append("  [{}] {} ({:.1f} KB)".format(out_name, client_name, size_kb))

    print("Generated {} archive(s):".format(len(generated)))
    for g in generated:
        print(g)
    print("Output: {}".format(os.path.abspath(output_dir)))


if __name__ == "__main__":
    main()
                                                                                                                                                                                                                  
```

---

*此文档包含完整的归档系统：规范 + 配置 + 工具。*
