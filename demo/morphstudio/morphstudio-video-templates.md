# Morph Studio — Video Templates 批量页面

> **定位**：**程序化 + 可复用模板** 的 **video templates** 聚合页（hub）与 **单模板详情页**（detail），支撑批量建站与 SEO；与 [morphstudio-site-structure.md](./morphstudio-site-structure.md) 内链、 [morphstudio-features.md](./morphstudio-features.md) 视频能力对齐。  
> **产品**：[morphstudio.com](https://www.morphstudio.com/) · **Last updated**: 2026-03-27

---

## 1. 页面类型与 URL 约定

| 类型 | 角色 | 建议 URL 模式（slug 以工程为准） |
|------|------|----------------------------------|
| **聚合页（Hub）** | 浏览、筛选、内链枢纽 | `/video-templates` 或 `/templates/video` |
| **详情页（Detail）** | 单模板：预览、说明、**使用** CTA | `/video-templates/{template-slug}` |

**原则**：全站 **唯一 slug 规范**（小写、连字符）；详情页 **自引用 canonical**；聚合页与首页、**/text-to-video**、**/image-to-video**（若存在）互链。

---

## 2. 批量构建：数据字段（每条模板一行）

用于 CSV / CMS / 程序化生成；**缺字段则不出页或降级为 draft**。

| 字段 | 必填 | 说明 |
|------|------|------|
| `template_slug` | ✅ | URL 段，唯一，英文，如 `cinematic-product-launch` |
| `name` | ✅ | 列表页标题 + 详情 H1 主名 |
| `short_description` | ✅ | 1–2 行，卡片与 meta description 共用基础 |
| `long_description` | 建议 | 详情首屏下正文；避免与 hub 重复 |
| `thumbnail_url` | ✅ | 封面图；**width/height** 固定比例，避免 CLS |
| `preview_video_url` | 建议 | 预览片段（静音/循环）；无则静态图 |
| `category` | 建议 | 分类筛选用，如 `social` / `ads` / `cinematic` / `ugc` |
| `visual_style` | 可选 | **画面风格/题材**，见 **§2.1**；可与 `category` 组合筛选（例：`cinematic` + `kissing`） |
| `tags` | 可选 | 数组或逗号分隔，用于站内搜索与相关推荐 |
| `aspect_ratio` | 建议 | 如 `16:9`、`9:16`，便于文案与筛选器 |
| `duration_hint` | 可选 | 如「约 5–10s」，与产品能力一致 |
| `recommended_models` | 可选 | 与 [morphstudio-features.md](./morphstudio-features.md) §3 一致；**须与真实接入一致** |
| `prompt_template` 或 `starter_prompt` | 可选 | 「一键使用」可复制进编辑器；**需合规审核** |
| `locale` | 可选 | 默认 `en`；多语言 hreflang 另表 |
| `published_at` / `updated_at` | 建议 | sitemap `lastmod`、文章类 Schema |

### 2.1 可选风格 / 题材（示例）

以下为 **非必填** 枚举示例，用于 Hub **风格筛选**、详情页 **相关推荐**；实际上线以产品与合规为准。

| `visual_style`（key） | 说明 | 典型用途 |
|------------------------|------|----------|
| **`kissing`** | **接吻 / 亲密镜头** 向画面（运镜、光影、节奏、情绪）；与「剧情/MV/广告」类 brief 对齐 | 剧情短片、MV、情感向广告、社媒竖屏等 |
| `cinematic` | 电影感、景深、调色偏胶片/大片 | 品牌片、预告感片段 |
| `ugc` | 手持、自然光、原生感 | 带货、真实感短视频 |

- **slug 示例**（含 kissing）：`kissing-scene-soft-light`、`romantic-close-up-16x9`（仅作命名参考）。  
- **合规**：含 **`kissing`** 的模板须在 **内容审核**、**年龄分级/地区政策**、**prompt 与预览素材** 上与 Morph 产品规则一致；Hub 可提供「风格」筛选项，**默认不勾选**或单独分组，避免与全年龄向模板混排引起误判。

---

## 3. 聚合页（Hub）结构

| 区块 | 目的 |
|------|------|
| **H1 + 简介** | 如 *Browse AI video templates*；1 段差异化（Morph：多模型、画布工作流） |
| **筛选** | 分类、**风格（含可选 `kissing` 等）**、比例、时长、用途（轻量，避免 crawl trap） |
| **模板卡片网格** | 缩略图、名称、短描述、**Use template** / **Preview** |
| **内链** | → `/text-to-video`、Open Canvas / Video 相关工具页、Pricing |
| **FAQ（可选）** | 2–4 条；**FAQPage** Schema 若上 |

**Schema**：`ItemList`（列表项指向各详情 URL）+ 站点级 `WebSite`/`Organization` 见全站策略。

---

## 4. 详情页（Detail）结构

| 区块 | 目的 |
|------|------|
| **Hero** | 模板名 + 一句话价值；**主 CTA**：*Use this template* / *Open in Morph* → App 深链或注册 |
| **预览** | 视频或 GIF；多比例若产品支持 |
| **适用场景** | 谁、什么 brief、什么产出 |
| **推荐模型 / 设置** | 与 `recommended_models` 一致；**不写未接入模型** |
| **How to use** | 3–5 步：选模板 → 调提示/参数 → 生成 → 导出（与产品真实流程一致） |
| **相关模板** | 同 category / tag；**内链** |
| **FAQ（可选）** | 授权、商业使用、与 Canvas 衔接等 |

**Schema**：`VideoObject`（若预览视频）、`CreativeWork` 或 `HowTo`（步骤块）；**BreadcrumbList**。

---

## 5. SEO 与索引（批量必查）

| 项 | 要求 |
|----|------|
| **Title** | 唯一；`{Template Name} Video Template | Morph Studio` |
| **Meta description** | 唯一；含用途词 + 品牌词 |
| **H1** | 每页唯一；详情 H1 = 模板名 |
| **Canonical** | 详情自引用；**带参 URL** 用 canonical 或 `noindex` |
| **Index** | 薄内容（无描述、无预览）→ **noindex** 或合并 |
| **内链** | Hub ↔ Detail ↔ 视频工具根页；避免孤儿页 |

---

## 6. 内链与站点结构（与现有 IA 对齐）

- **Hub** → 首页 Video 区块、**Pricing**、**Models** 子页（若模板与某模型强绑定）  
- **Detail** → Hub、**同系列** 2–4 个详情、**`/resources`** 或博客（若有「教程」）  
- **电影向长尾**（可选）：部分模板可挂到 [morphstudio-use-cases.md](./morphstudio-use-cases.md) 叙事下的解决方案页，**单向**链入 Hub，避免 cannibalization

---

## 7. 批量上线流程（建议）

1. **定稿** URL 模式、slug 规则、字段表（§2）。  
2. **内容**：首批 N 条（建议 **20–50** 验证索引与内链）→ 再扩量。  
3. **工程**：列表/详情模板组件、SSR/SSG、**sitemap** 分片（`/video-templates/sitemap.xml` 或主 sitemap）。  
4. **QA**：每模板随机抽检：预览、CTA、canonical、移动端、LCP。  
5. **GSC**：提交 sitemap；监控 **Coverage**、**Core Web Vitals**。

---

## 8. 优先级（建议）

| 阶段 | 内容 |
|------|------|
| **P0** | Hub + 详情模板 + 字段表 + canonical/sitemap + 首批 10–20 条真实可预览模板 |
| **P1** | 筛选器、相关推荐、FAQ、VideoObject；扩至全量数据 |
| **P2** | 多语言 hreflang、与 `/for-filmmakers` 等专题交叉内链 |

---

## 9. 文档导航

| 文档 | 职责 |
|------|------|
| [morphstudio.md](./morphstudio.md) | 产品总览 |
| [morphstudio-features.md](./morphstudio-features.md) | 视频能力、模型名 |
| [morphstudio-site-structure.md](./morphstudio-site-structure.md) | 全站 IA |
| [morphstudio-video-templates.md](./morphstudio-video-templates.md)（本文） | Video templates 批量页与数据规范 |

**说明**：仓库中曾附的 **kissing 风格静态 HTML 原型**（`*-kissing-hub.html` / `*-kissing-detail.html`）**已删除**，本文不再引用文件路径。**聚合页 / 详情页** 的区块划分、字段与合规要求仍以 **§2–§4** 为准；若需重新做可点击原型，可按 **template-page**、**card**、**hero** 技能在工程或设计稿中另建。

---

*Demo · Morph Studio · Video templates 程序化建站说明*
