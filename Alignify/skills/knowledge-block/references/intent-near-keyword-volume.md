# 同意图关键词 · 搜索量快判（Intent-Near Volume Compare）

> **Skill**：[`../SKILL.md`](../SKILL.md) · **用途**：知识块选题 / `keywordEn` / 文件夹与 slug 分流  
> **非 SSOT 数字**：结果数为 **方向性代理**，禁止写进 KB 或正文当精确 MSV；定稿仍应用 GSC / Ahrefs / Semrush 交叉。

---

## 第一性原理

1. **slug 跟 SERP 头词 / 搜索量**，不是跟内部「买家轴验收」强行拆词。
2. **文件夹跟品类**：物理路径 `knowledge/tools/{cluster}/{slug}.md`（slug 与路由不变）。**建站器** → [`website-builder/`](../../../knowledge/tools/website-builder/README.md)；**CMS 架构/API** → [`cms/`](../../../knowledge/tools/cms/README.md)；**图像** → [`image/`](../../../knowledge/tools/image/image.md) 等——全表见 [`README §主题簇物理路径`](../../../knowledge/tools/README.md#主题簇物理路径2026-08-28)。两建站相关簇 **并列**，勿混在 `website-building/`。
3. 仅当 **SERP 模板明显分裂** 才拆 slug；同一 listicle 混排 → 同一 spoke。
4. **新建 spoke 三关**（[`cms/KEYWORD-RESEARCH.md`](../../../knowledge/tools/cms/KEYWORD-RESEARCH.md)）：SERP 头词 · **≥2 款 born-for 垂直产品** · 非品牌/许可证/学术 taxonomy轴。

---

## 何时用

- 两个词描述 **同一买家问题**，但说法不同（builder vs platform vs CMS）。
- 需决定 **Primary keyword**、**slug**、或 **进哪个文件夹**。
- **不要**用于完全不同意图（blog builder vs headless browser）——用分流表 + SERP 模板。

---

## 方法 A · 现搜 Google/Bing 结果数

| 候选词 | 约结果数（Bing · 2026-08-28） | 备注 |
|--------|-------------------------------|------|
| `blog website builder` | ~898,000 | **博客 spoke 头词** |
| `blog CMS` | ~898,000 | 同 SERP；不单独 slug |
| `blogging platform` | ~45,500 | Secondary，非主 slug |
| `CMS for publishing blog` | ~238,000 | **非自然 query** |

---

## 方法 B · SERP 标题展开

搜较低量词时，若 ≥50% 标题用 **另一候选词**（*platform* / *builder* / *create a blog*），则 **标题反复出现的词** 更接近头词。

---

## 标答 · `blog website builder` vs `CMS for publishing blog`

**结论**：**`blog website builder` > `CMS for publishing blog`**（后者非自然英文）。

**Alignify 分流（2026-08-28）**：

| 检索词 | slug | 文件夹 |
|--------|------|--------|
| `blog website builder` · *best website builder for blogs* | **`blog-website-builder`** | `website-builder/` |
| `website builder` · AI website builder | **`website-builder`** | `website-builder/` |
| `headless CMS` · API-first CMS | **`headless-cms`** | `cms/` |
| 不用 CMS / Git+AI 建博客 | 跨频道 [`how-to-build-a-blog-without-a-cms-using-ai`](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai) | — |

**禁止**：因「CMS 轴」把 `blog website builder` 赶去 Hub 或拆 `blog-cms` / `blogging-platform` 第二 slug。

---

## 检查清单

- [ ] 现搜两候选词 + SERP 标题展开
- [ ] 结论写入 KB `keywordEn` 或簇 `KEYWORD-RESEARCH.md`
- [ ] Brief Primary 与 KB 一致
- [ ] 文件夹：`website-builder/` vs `cms/` 不混放

---

## 相关 SSOT

- [`website-builder/KEYWORD-RESEARCH.md`](../../../knowledge/tools/website-builder/KEYWORD-RESEARCH.md)
- [`cms/KEYWORD-RESEARCH.md`](../../../knowledge/tools/cms/KEYWORD-RESEARCH.md)
- [`keyword-research.md`](../../../knowledge/marketing/keyword-research.md)
