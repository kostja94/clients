#!/usr/bin/env python3
"""Dissolve media-image-cluster.md into knowledge blocks; quality fixes."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / "knowledge" / "tools"
DATE = "2026-06-23"

IMAGE_SLUGS = [
    "image",
    "image-generator",
    "image-editor",
    "image-enhancer",
    "image-relighting",
    "background-changer",
    "headshot-generator",
    "logo-generator",
    "poster-generator",
    "tattoo-generator",
    "avatar",
    "image-to-video",
]

FOOTER_TEMPLATE = """**延伸阅读 · 站内知识块**
- 品类 Hub：[image.md](./image.md)
- 生成层 SSOT：[image-generator.md](./image-generator.md)（§行业注记 / §外链索引 / §共享事实速查）
{extra}"""


def strip_cluster_refs(text: str) -> str:
    text = re.sub(r"\*\*簇治理\*\*[^\n]*\n+", "", text)
    text = re.sub(r"\*\*簇治理（视频簇）\*\*[^\n]*\n+", "", text)
    text = re.sub(r"- 簇治理：\[media-image-cluster\.md\]\(\./media-image-cluster\.md\)\n", "", text)
    text = re.sub(r" · \*\*图片簇\*\*：\[media-image-cluster\.md\]\(\./media-image-cluster\.md\)", "", text)
    text = re.sub(r"cluster 共享事实表 \+ generator 行业注记", "image-generator §共享事实速查 / §行业注记", text)
    text = re.sub(r"cluster 内容所有权表", "下文「内容分工」", text)
    text = re.sub(r"见 cluster 共享事实表", "见 [image-generator.md](./image-generator.md) §共享事实速查", text)
    return text


def write_image_hub() -> None:
    content = f"""# AI Image · 知识块（非线性笔记 · Hub）

**材料范围**：公开网络检索（Research and Markets 市场报告摘要、EU AI Act 合规分析、Alignify 静态图像 slug 互链结构）；**未**引用 Alignify 站内 JSON 正文为论据。网摘整理日期 **{DATE}**。

**站内对照**：[alignify.co/tools/image](https://alignify.co/tools/image) · [alignify.co/zh/tools/image](https://alignify.co/zh/tools/image) · `content/tools/en/image.json` · `content/tools/zh/image.json` · slug **`image`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 `#image-tools`

**站内相邻**：[image-generator.md](./image-generator.md) · [image-editor.md](./image-editor.md) · [image-enhancer.md](./image-enhancer.md) · [image-relighting.md](./image-relighting.md) · [background-changer.md](./background-changer.md)

**勿与…混买**：本页是 **静态图像品类地图**——不含旗舰模型 URL 表；T2I/I2I 模型横评、共享事实与时间线见 [image-generator.md](./image-generator.md)。

以下条目可任意顺序阅读；**不是**文章体例。

---

## Buyer 决策树

| 你的问题 | 去哪个 slug | 知识块 |
|----------|-------------|--------|
| 从零生成图片 / 哪个模型最好？ | `image-generator` | [image-generator.md](./image-generator.md) |
| 改已有图的内容（填充、移除、扩图）？ | `image-editor` | [image-editor.md](./image-editor.md) |
| 把图变清晰 / 放大不改变内容？ | `image-enhancer` | [image-enhancer.md](./image-enhancer.md) |
| 只改光照 / 重打光？ | `image-relighting` | [image-relighting.md](./image-relighting.md) |
| 抠图换背景 / 电商白底？ | `background-changer` | [background-changer.md](./background-changer.md) |
| 职业照 / LinkedIn 头像要像本人？ | `headshot-generator` | [headshot-generator.md](./headshot-generator.md) |
| Logo + 品牌 Kit / 矢量？ | `logo-generator` | [logo-generator.md](./logo-generator.md) |
| 活动海报（图+字+版式）？ | `poster-generator` | [poster-generator.md](./poster-generator.md) |
| 纹身图案 + 试戴？ | `tattoo-generator` | [tattoo-generator.md](./tattoo-generator.md) |
| 会说话的数字人**视频**？ | `avatar` | [avatar.md](./avatar.md) |
| 静态图怎么动起来？ | `image-to-video` | [image-to-video.md](./image-to-video.md) |

---

## 内容分工（编辑前必读）

各 slug **唯一主归属**；其它块只保留与本页相关的一行对比 + 链出，避免重复维护模型榜。

| 内容类型 | 主归属 slug | 其它块 |
|----------|-------------|--------|
| 品类地图 / 子 slug 分流 | **`image`（本页）** | spoke 只保留一行边界 |
| T2I/I2I/LoRA/行业时间线/旗舰 URL 表 | **`image-generator`** | hub 不定义；spoke ≤2 代表产品 |
| Generative Fill / Inpainting | **`image-editor`** | generator 1 句 + 链 |
| 超分 / 降噪（不改语义） | **`image-enhancer`** | generator Upscaling 1 句 + 链 |
| 物理光照 / relight | **`image-relighting`** | editor sky replace 链出 |
| Matting / 换底 / 批量 API | **`background-changer`** | editor 不重复 Photoroom 长文 |
| Likeness / 职业照 | **`headshot-generator`** | 与 avatar、generator 分流表互链 |
| Logo 矢量 / Brand Kit | **`logo-generator`** | 不重复 Ideogram 横评 |
| 海报版式 / 多尺寸 | **`poster-generator`** | 不重复 Canva 功能清单 |
| 纹身 / 试戴 / Stencil | **`tattoo-generator`** | 不重复通用 T2I 榜 |
| 数字人视频 | **`avatar`** | 非静态 headshot |
| I2V / Motion Brush | **`image-to-video`** | generator 不写 I2V 长段 |
| 版权 / C2PA / deepfake 全文 | **`image-generator` §风险** | hub ≤3 条摘要 |

**产品表规则**：完整 Midjourney / FLUX / Ideogram / gpt-image-2 URL 表**仅** `image-generator`；hub **无** URL 表。

---

## 与相邻 slug 分流（12 成员摘要）

| slug | 一句话边界 |
|------|------------|
| `image-generator` | T2I/I2I、模型 SSOT；不含抠图专页 |
| `image-editor` | 已有图像的内容编辑；Generative Fill SSOT |
| `image-enhancer` | 超分/降噪；不改语义 |
| `image-relighting` | 只改光照；sky replace 见 editor |
| `background-changer` | Matting + 换底 + 批量 API |
| `headshot-generator` | Likeness 约束；非通用文生图 |
| `logo-generator` | 矢量 Logo + Brand Kit |
| `poster-generator` | 海报 = 生图 + 排版 + 文字 |
| `tattoo-generator` | 纹身风格 + 试戴 |
| `avatar` | 数字人**视频**；非静态头像 |
| `image-to-video` | 输入=静态图→视频；T2V 见 video-generator |

---

## 词汇锚点（Hub 级）

- **AI 图像（本 Hub）**：涵盖 **生成**、**编辑**、**增强**、**重打光** 与 **垂直任务**。2026 年市场约 **$2–3B+**（Research and Markets 等第三方口径），CAGR 双位数。
- **2026 旗舰摘要**（版本号 SSOT 见 [image-generator.md](./image-generator.md) §共享事实速查）：**gpt-image-2**、**Midjourney V8.1**、**Ideogram 4.0**、**FLUX.2**、**Nano Banana 2**、**Adobe Firefly**；DALL·E 2/3 已于 **2026-05-12** 退役。

---

## 问题域

- **多模型实用主义**：按任务切换工具——先定 slug，再进 generator 或 spoke 选产品。
- **设计平台 AI 化**：Canva AI 2.0 等完成「设计任务」而非单张出图——poster/logo 与 generator 分工见上表。
- **合规窗口**：EU AI Act 第 50 条 **2026-08-02** 生效——详见 generator §风险。
- **版权分叉**：Firefly（授权+赔偿）vs 开源 FLUX.2——企业采购哲学不同。

---

## 落地碎片

- 用上表决策树 + 内容分工，避免在 Hub 层做模型横评。
- 静态 JPEG 职业照 → headshot；口型同步视频 → avatar。
- 已有照片只要白底 → background-changer 可能足够。
- I2V：生成质量见 generator，动画见 image-to-video。

---

## 形态谱系（Hub 级，无 URL 表）

| 形态 | 典型买家 | 深入阅读 |
|------|----------|----------|
| 从零生成 | 营销、概念艺术、API | `image-generator` |
| 改已有图 | 设计师、电商 | `image-editor` |
| 提质放大 | 摄影师、档案 | `image-enhancer` |
| 改光照 | 产品/人像后期 | `image-relighting` |
| 换底抠图 | 电商、证件白底 | `background-changer` |
| 垂直交付 | Logo/海报/职业照/纹身 | 对应 spoke |

---

## 与 video 簇交叉

- **image-to-video**：静态图 → I2V；通用 T2V 见 [video-generator.md](./video-generator.md)。
- **canvas-video**：节点编排图像+视频模型。

---

## 风险 · 合规 · 摘要（≤3 条）

- **深度伪造 / NCII**：见 headshot、image-editor 场景化讨论。
- **AI 屏显文字不可作唯一事实源**：gpt-image-2 等亦需人工核验。
- **完整框架**：见 [image-generator.md](./image-generator.md) §风险 · 合规。

---

*说明：旗舰 URL 表与 2026 时间线 SSOT 见 image-generator。*

---

{FOOTER_TEMPLATE.format(extra="")}
"""
    (KB / "image.md").write_text(content, encoding="utf-8")
    print("Wrote image.md")


def patch_image_generator(text: str) -> str:
    text = strip_cluster_refs(text)
    text = re.sub(
        r"\*\*簇治理\*\*[^\n]*\n+",
        "",
        text,
    )
    text = text.replace(
        "**站内相邻**",
        "**角色**：本 slug 为静态图像 **生成层 SSOT**（T2I/I2I、行业时间线、旗舰 URL 表）。品类地图见 [image.md](./image.md) §内容分工。\n\n**站内相邻**",
        1,
    )
    text = text.replace(
        "| **文字能力** | 2026 年大幅提升 | 仍弱（~10% 成功率） | 中等 |",
        "| **文字能力** | 2026 年大幅提升（~95% 社区测） | V8.1 较 V7 改善；复杂排版仍弱于 Ideogram/gpt-image-2 | 中等 |",
    )
    text = text.replace(
        "V7 引入 `--oref` 角色一致性和 Model Personalization",
        "V8.1 延续 `--oref`（暂 V7 训练版）与 Model Personalization",
    )
    # Fix timeline order: move June block after April-May
    june_block = re.search(
        r"### 2026 年 6 月\n\n.*?\n\n### 2026 年 4–5 月",
        text,
        re.DOTALL,
    )
    if june_block:
        full = june_block.group(0)
        june_only = full.split("### 2026 年 4–5 月")[0].strip()
        rest_start = full.index("### 2026 年 4–5 月")
        before = text[: june_block.start()]
        after = text[june_block.end() :]
        middle = full[rest_start:]
        text = before + middle + "\n\n" + june_only.replace("### 2026 年 6 月", "### 2026 年 6 月") + after

    if "## 共享事实速查" not in text:
        facts = """
## 共享事实速查（全静态图像 slug 统一口径）

**版本号与关停日期仅在本节 + §行业注记维护**；spoke 写「见 image-generator §共享事实速查」，避免多处硬编码。

| 事实 | 统一表述（截至 2026-06-23） |
|------|---------------------------|
| Midjourney 默认 | **V8.1**（2026-06-10）；SD ~4s / HD ~12s；原生 2K |
| Midjourney Omni Reference | 暂 **V7 训练版** `--oref` |
| OpenAI 图像 API | **`gpt-image-2`**；DALL·E 2/3 **2026-05-12** 退役 |
| Ideogram 旗舰 | **4.0**（2026-06-03 开放权重）；Layerize = 可编辑文字层 |
| FLUX | **FLUX.2**（klein Apache 2.0；pro/flex/max API）；多参考 ≤10 张 |
| Google 图像 | **Nano Banana 2**（Gemini 3.1 Flash Image） |
| 文字渲染（2026-06 社区口径） | Ideogram 4.0 / gpt-image-2 / Nano Banana 2·Pro |
| 中英双语排版 | **Qwen-Image-2.0**（DashScope $0.035–0.075/图） |
| 企业商用安全 | **Adobe Firefly**（授权数据 + 赔偿）；Foundry 私有 IP |
| EU AI Act Art.50 | **2026-08-02** 生效；C2PA 为常见溯源标准 |

---
"""
        text = text.replace("---\n\n## 词汇锚点", facts + "\n## 词汇锚点", 1)

    # Add poster/logo table if missing
    if "poster-generator" not in text.split("## 问题域")[0][-1200:]:
        insert = """
| 维度 | **image generator** | **poster-generator / logo-generator** |
|------|---------------------|----------------------------------------|
| **重心** | 通用 T2I/I2I | 海报版式 / Logo 矢量 |
| **文字** | 引用 Ideogram/gpt-image-2 | 验收可读+可导出；细节见本页 |
| **知识块** | 本页 | [poster-generator.md](./poster-generator.md) · [logo-generator.md](./logo-generator.md) |
"""
        text = text.replace(
            "| **适用场景** | 全球通用 | 中文电商、中式品牌物料、中英双语信息图 |\n---",
            "| **适用场景** | 全球通用 | 中文电商、中式品牌物料、中英双语信息图 |\n" + insert + "\n---",
            1,
        )

    text = re.sub(
        r"\*\*延伸阅读 · 站内知识块\*\*\n- 品类 Hub.*",
        FOOTER_TEMPLATE.format(extra=""),
        text,
        flags=re.DOTALL,
    )
    return text


def patch_spoke(slug: str, text: str) -> str:
    text = strip_cluster_refs(text)
    text = re.sub(r"网摘整理日期[^\n]*", f"网摘整理日期 **{DATE}**", text, count=1)

    if slug == "image-to-video":
        if "**站内相邻**" in text and "video.md" in text:
            text = re.sub(
                r"\*\*站内相邻\*\*：[^\n]+",
                "**站内相邻**：[image.md](./image.md) · [image-generator.md](./image-generator.md) · [video.md](./video.md) · [video-generator.md](./video-generator.md) · [text-to-video.md](./text-to-video.md) · [video-to-video.md](./video-to-video.md)",
                text,
                count=1,
            )
        extra = "- I2V 专页；T2V 旗舰表见 [video-generator.md](./video-generator.md)"
    elif slug == "logo-generator":
        text = text.replace(
            "通用模型文字渲染弱（Midjourney ~10% 成功率）",
            "通用 T2I 复杂排版弱于 Ideogram 4.0 / gpt-image-2（见 image-generator §共享事实速查）",
        )
        text = re.sub(
            r"> \*\*簇规则\*\*：[^\n]+\n\n",
            "> **分工**：Ideogram/Canva 平台叙事见 [image-generator.md](./image-generator.md)；本页只列 Logo 垂直验收。\n\n",
            text,
        )
        extra = "- Logo 垂直：[logo-generator.md](./logo-generator.md)"
    elif slug == "poster-generator":
        text = re.sub(
            r"> \*\*簇规则\*\*：[^\n]+\n\n",
            "> **分工**：Canva/Ideogram 横评见 [image-generator.md](./image-generator.md)；本页只列海报验收。\n\n",
            text,
        )
        extra = "- 海报垂直：[poster-generator.md](./poster-generator.md)"
    else:
        extra = ""

    if "**延伸阅读 · 站内知识块**" in text:
        text = re.sub(
            r"\*\*延伸阅读 · 站内知识块\*\*.*",
            FOOTER_TEMPLATE.format(extra=extra),
            text,
            flags=re.DOTALL,
        )
    elif slug != "image-generator":
        text = text.rstrip() + "\n\n---\n\n" + FOOTER_TEMPLATE.format(extra=extra) + "\n"

    return text


def update_readme(text: str) -> str:
    text = text.replace(
        "- **媒体生产链 · 图片簇（12 slug）**：SSOT 见 [media-image-cluster.md](./media-image-cluster.md)；Hub 为 [image.md](./image.md)（Buyer 决策树，**无**旗舰 URL 表）；生成层主归属 [image-generator.md](./image-generator.md)（A 档 pillar）。管线 spoke（editor/enhancer/relighting）与任务 spoke（background/headshot/logo/poster/tattoo/avatar）按 cluster **内容所有权表** 互链去重；[image-to-video.md](./image-to-video.md) 为静态图→视频相邻块。",
        "- **媒体生产链 · 静态图像（12 slug）**：Hub 为 [image.md](./image.md)（Buyer 决策树 + **§内容分工**；无旗舰 URL 表）；生成层 SSOT 为 [image-generator.md](./image-generator.md)（§共享事实速查 / §行业注记 / §外链索引）。管线 spoke（editor/enhancer/relighting）与任务 spoke（background/headshot/logo/poster/tattoo/avatar）互链去重；[image-to-video.md](./image-to-video.md) 为静态图→视频相邻块。",
    )
    text = text.replace(
        "与 [media-image-cluster.md](./media-image-cluster.md)；正式页",
        "；正式页",
    )
    text = text.replace(
        "深度见 [image-generator.md](./image-generator.md) 与 [media-image-cluster.md](./media-image-cluster.md)",
        "深度见 [image-generator.md](./image-generator.md) 与 [image.md](./image.md) §内容分工",
    )
    return text


def main() -> None:
    cluster = KB / "media-image-cluster.md"
    if cluster.exists():
        cluster.unlink()
        print("Deleted media-image-cluster.md")

    write_image_hub()

    gen_path = KB / "image-generator.md"
    gen_path.write_text(patch_image_generator(gen_path.read_text(encoding="utf-8")), encoding="utf-8")
    print("Patched image-generator.md")

    for slug in IMAGE_SLUGS:
        if slug in ("image", "image-generator"):
            continue
        path = KB / f"{slug}.md"
        if path.exists():
            path.write_text(patch_spoke(slug, path.read_text(encoding="utf-8")), encoding="utf-8")
            print(f"Patched {slug}.md")

    readme = ROOT / "knowledge" / "tools" / "README.md"
    readme.write_text(update_readme(readme.read_text(encoding="utf-8")), encoding="utf-8")

    territory = KB / "territory-map.md"
    t = territory.read_text(encoding="utf-8")
    t = t.replace("| `media-image-cluster.md` | 媒体生产链 · **图片簇**（12 slug）SSOT、共享事实、互链规范 |\n", "")
    territory.write_text(t, encoding="utf-8")

    print("Done.")


if __name__ == "__main__":
    main()
