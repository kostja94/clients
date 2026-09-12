# Sparki Blog 文章结构与内链

> **用途**：全站 Blog 唯一的**结构与内链参考**（人类 + 站点维护）。回答两件事——**① 74 篇文章如何组织；② 文章之间应如何互链**（含实测快照与补链待办）。
>
> **Skill 对齐**：创作 Gate / Canonical / Hub-Spoke 以 [`skills/sparki-blog-article/references/content-graph.md`](../skills/sparki-blog-article/references/content-graph.md) 为 SSOT，写作规则见 [`references/internal-links.md`](../skills/sparki-blog-article/references/internal-links.md)（R1–R6）。本文档是同一信息的**项目级视图**，随实际成稿维护。
>
> **本地工作区范围**：本文档内链矩阵**只覆盖本地成稿 14 篇**（`blog/vlog/` 2 篇 + `blog/food-beverage/` 12 篇）。既有 62 篇成稿在部署仓 `E:\客户部署项目\sparki-blog\content\blog\`，本文仅把它们作为**库内已有链接目标**（canonical/锚点）登记，不逐篇展开。
>
> **快照**：2026-09-11 · 14 篇本地成稿全量实测（**内链优化已执行，全库 R1–R5 通过、零入链清零**）。统计口径：frontmatter 之后正文中站内 `/blog/{slug}` 链接（Markdown `](/blog/…)` 写法）；一篇对同一 slug 计 1；主站 `https://sparki.io/...` 绝对 URL 与竞品外链不计入。

---

## 一、Blog 文章结构

```
Blog (/blog) — 74 篇（62 既有 + 12 food-beverage 新；本地工作区可见 14 篇）

├── 既有 62 篇（部署仓，本文仅登记为「库内链接目标」）
│   ├── Clone Edit Viral Videos（红人风格）24 篇
│   ├── ai-video-editor（AI 编辑器选型/流程）17 篇  ← 含 ai-video-editor（概念 canonical）
│   ├── Video Editing Features（功能/工作流）12 篇   ← 含 long-video-to-short-video / ai-caption 等 canonical
│   ├── Editor-in-browser 4 篇 · AI Video Editing 4 篇 · AI Tools 1 篇
│   └── Vlog 簇 2 篇（what-is-a-vlog 品类 canonical · edit-vlog-15-minutes-smart-cut 手动对照）
│
├── vlog/（本地成稿 · 簇 hub 主站 https://sparki.io/vlog）
│   ├── how-to-edit-a-vlog-with-ai        ★ 流程 canonical（C1）
│   └── how-to-edit-a-travel-vlog         （travel spoke）
│
└── food-beverage/（本地成稿 · 簇 hub 主站 https://sparki.io/industries + 7 详情页）
    ├── how-to-edit-restaurant-videos-with-ai   ★ 流程 canonical（C1）
    ├── restaurant-video-marketing              ★ 品类 POV（C2，flagship）
    ├── how-to-edit-food-videos-with-ai         ★ format canonical（C3）
    ├── how-to-edit-coffee-shop-videos          （vertical V1 · cafe）
    ├── how-to-edit-cocktail-videos             （vertical V2 · bar）
    ├── how-to-edit-bakery-videos               （vertical V3 · bakery）
    ├── how-to-edit-pizza-videos                （vertical V4 · pizza）
    ├── how-to-edit-bubble-tea-videos           （vertical V5 · bubble-tea）
    ├── how-to-edit-food-truck-videos           （vertical V6 · food-truck）
    ├── how-to-edit-food-asmr-videos            （format F1）
    ├── how-to-edit-kitchen-behind-the-scenes-videos （format F2）
    └── ai-food-video-editor                    （选型 S1，FeatureGuide）
```

| slug | date | category | 簇 | 角色 |
|------|------|----------|----|------|
| `how-to-edit-a-vlog-with-ai` | 2026-08-02 | ai-video-editor | vlog | **流程 canonical** |
| `how-to-edit-a-travel-vlog` | 2026-08-03 | ai-video-editor | vlog | Spoke（travel） |
| `how-to-edit-restaurant-videos-with-ai` | 2026-08-04 | ai-video-editor | food-beverage | **流程 canonical** |
| `restaurant-video-marketing` | 2026-08-05 | ai-video-editor | food-beverage | **品类 POV** |
| `how-to-edit-food-videos-with-ai` | 2026-08-06 | Video Editing Features | food-beverage | **format canonical** |
| `how-to-edit-coffee-shop-videos` | 2026-08-07 | ai-video-editor | food-beverage | Spoke（V1） |
| `how-to-edit-cocktail-videos` | 2026-08-08 | Video Editing Features | food-beverage | Spoke（V2） |
| `how-to-edit-bakery-videos` | 2026-08-09 | Video Editing Features | food-beverage | Spoke（V3） |
| `how-to-edit-pizza-videos` | 2026-08-10 | Video Editing Features | food-beverage | Spoke（V4） |
| `how-to-edit-bubble-tea-videos` | 2026-08-11 | Video Editing Features | food-beverage | Spoke（V5） |
| `how-to-edit-food-truck-videos` | 2026-08-12 | ai-video-editor | food-beverage | Spoke（V6） |
| `how-to-edit-food-asmr-videos` | 2026-08-13 | Video Editing Features | food-beverage | Spoke（F1） |
| `how-to-edit-kitchen-behind-the-scenes-videos` | 2026-08-14 | Video Editing Features | food-beverage | Spoke（F2） |
| `ai-food-video-editor` | 2026-08-15 | ai-video-editor | food-beverage | Spoke（S1 选型） |

**结构规则**：公开 URL 扁平 `/blog/{slug}`（sparki 无 NN 序号前缀）；文件名 = slug；`category` 取枚举且与簇一致；不设文末 Related articles，内链只在正文自然语境出现。

---

## 二、内链硬性规则（R1–R6 · 引用 internal-links.md）

| 规则 | 要求 |
|------|------|
| **R1** | 每篇正文 ≥2 条不同 `/blog/` slug 内链（全文分布，非集中末尾）；主站页面 1–3（绝对 URL）；外链 2–6 |
| **R2** | 主站页面（features/solutions/creators/industries/video-editor/pricing/use-cases/api）**一律绝对 URL** `https://sparki.io/...`；blog 文章相对 `/blog/{slug}`；竞品外链 HTML `rel="nofollow noopener"` |
| **R3** | 锚文本描述性，禁 "click here" / "learn more" / 裸 URL |
| **R4** | Canonical 概念 1–2 句 + link，不重定义 |
| **R5** | **Hub-Spoke 双向互链**：hub 链向主要 spoke；spoke 回链 hub；spoke↔spoke 语义相关时互链 |
| **R6** | 禁未上线页面 / forthcoming 正文核心流程 / 死链 / 相对路径主站路由 |

**Canonical 概念注册表（本簇相关）**：

| 概念 | Canonical slug | 他文处理 |
|------|----------------|----------|
| AI video editor 概念 | `/blog/ai-video-editor`（既有） | 1–2 句 + link |
| 长改短总流程 | `/blog/long-video-to-short-video`（既有） | 1–2 句 + link |
| 字幕工作流选型 | `/blog/ai-caption-generator-how-to-pick-the-right-workflow`（既有） | 1–2 句 + link |
| 餐厅视频编辑流程（本地餐饮商家） | `/blog/how-to-edit-restaurant-videos-with-ai`（C1） | 全簇 vertical 文引用 |
| 美食过程/工艺视频剪辑 | `/blog/how-to-edit-food-videos-with-ai`（C3） | 全簇 format 文引用 |

---

## 三、簇内链矩阵（应链向 / 应被链自）

> 标记：**✓** = 实测正文已有该出链。主站页面（绝对 URL）与既有 canonical 出链不在此矩阵（它们天然合规，见 §五）。

### 3.1 Food & Beverage 簇（C1/C3 双 canonical · 12 篇）

| slug | 角色 | 实测链向 | 实测入链 |
|------|------|----------|----------|
| `how-to-edit-restaurant-videos-with-ai` (C1) | **流程 canonical** | ✓ 6 vertical + C2 + S1 + 3 既有 canonical（共 11 出链） | ✓ 11 |
| `how-to-edit-food-videos-with-ai` (C3) | **format canonical** | ✓ F1 + F2 + V3 + V4 + C1 + 2 既有 canonical（共 7 出链） | ✓ 9 |
| `restaurant-video-marketing` (C2) | 品类 POV | ✓ C1 + F1 + F2 + ai-video-editor（共 4 出链） | ✓ 1（C1） |
| `how-to-edit-coffee-shop-videos` (V1) | vertical spoke | ✓ C1 + C3 + caption（共 3 出链） | ✓ 1（C1） |
| `how-to-edit-cocktail-videos` (V2) | vertical spoke | ✓ C1 + C3（共 2 出链） | ✓ 1（C1） |
| `how-to-edit-bakery-videos` (V3) | vertical spoke | ✓ C1 + C3 + long-to-short（共 3 出链） | ✓ 2（C1 + C3） |
| `how-to-edit-pizza-videos` (V4) | vertical spoke | ✓ C1 + C3 + F1（共 3 出链） | ✓ 2（C1 + C3） |
| `how-to-edit-bubble-tea-videos` (V5) | vertical spoke | ✓ C1 + C3（共 2 出链） | ✓ 1（C1） |
| `how-to-edit-food-truck-videos` (V6) | vertical spoke | ✓ C1 + C3 + long-to-short（共 3 出链） | ✓ 1（C1） |
| `how-to-edit-food-asmr-videos` (F1) | format spoke | ✓ C1 + C3 + caption（共 3 出链） | ✓ 3（C2 + V4 + C3） |
| `how-to-edit-kitchen-behind-the-scenes-videos` (F2) | format spoke | ✓ C1 + C3（共 2 出链） | ✓ 2（C2 + C3） |
| `ai-food-video-editor` (S1) | 选型 spoke | ✓ C1 + C3 + ai-video-editor + long-to-short（共 4 出链） | ✓ 1（C1） |

> **R5 双向互链已闭合**：C1 反向链向全部 6 vertical + C2 + S1；C3 反向链向 F1 + F2 + V3 + V4。全簇零入链清零。

### 3.2 Vlog 簇（how-to-edit-a-vlog-with-ai Hub · 2 篇）

| slug | 角色 | 实测链向 | 实测入链 |
|------|------|----------|----------|
| `how-to-edit-a-vlog-with-ai` | **流程 canonical** | ✓ travel + 4 既有锚点（共 5 出链） | ✓ 1（travel） |
| `how-to-edit-a-travel-vlog` | travel spoke | ✓ hub + 4 既有锚点（共 5 出链） | ✓ 1（hub） |

> Vlog 簇双向互链已闭合（hub↔spoke），无缺口。

---

## 四、实测快照（2026-09-11 · 内链优化后）

### 4.1 出链（每篇 → 不同 /blog/ slug）

| 篇 | 出链数 |
|----|:---:|
| vlog · `how-to-edit-a-vlog-with-ai` | 5 |
| vlog · `how-to-edit-a-travel-vlog` | 5 |
| `how-to-edit-restaurant-videos-with-ai` (C1) | 11 |
| `restaurant-video-marketing` (C2) | 4 |
| `how-to-edit-food-videos-with-ai` (C3) | 7 |
| `how-to-edit-coffee-shop-videos` (V1) | 3 |
| `how-to-edit-cocktail-videos` (V2) | 2 |
| `how-to-edit-bakery-videos` (V3) | 3 |
| `how-to-edit-pizza-videos` (V4) | 3 |
| `how-to-edit-bubble-tea-videos` (V5) | 2 |
| `how-to-edit-food-truck-videos` (V6) | 3 |
| `how-to-edit-food-asmr-videos` (F1) | 3 |
| `how-to-edit-kitchen-behind-the-scenes-videos` (F2) | 2 |
| `ai-food-video-editor` (S1) | 4 |

**R1 结论**：14 篇全部 ≥2 出链 → **PASS**。

### 4.2 入链（每篇 ← 被谁链入，本工作区 14 篇口径）

| 篇 | 入链数 | 来源 |
|----|:---:|------|
| `how-to-edit-restaurant-videos-with-ai` (C1) | **11** | 除自身外全部 food-beverage 篇 |
| `how-to-edit-food-videos-with-ai` (C3) | **9** | F1、F2、V1–V6、S1 |
| `how-to-edit-food-asmr-videos` (F1) | 3 | C2、V4、C3 |
| `how-to-edit-kitchen-behind-the-scenes-videos` (F2) | 2 | C2、C3 |
| `how-to-edit-bakery-videos` (V3) | 2 | C1、C3 |
| `how-to-edit-pizza-videos` (V4) | 2 | C1、C3 |
| `restaurant-video-marketing` (C2) | 1 | C1 |
| `how-to-edit-coffee-shop-videos` (V1) | 1 | C1 |
| `how-to-edit-cocktail-videos` (V2) | 1 | C1 |
| `how-to-edit-bubble-tea-videos` (V5) | 1 | C1 |
| `how-to-edit-food-truck-videos` (V6) | 1 | C1 |
| `ai-food-video-editor` (S1) | 1 | C1 |
| `how-to-edit-a-vlog-with-ai` | 1 | travel |
| `how-to-edit-a-travel-vlog` | 1 | vlog-hub |

**R2 入链结论**：14 篇全部入链 ≥1 → **PASS，零入链清零**。

### 4.3 死链 / 链接目标可达性

所有 `/blog/` 链接目标（14 本地成稿 + 8 既有 canonical）经核对全部存在：

- 既有 canonical：`ai-video-editor` · `long-video-to-short-video` · `ai-caption-generator-how-to-pick-the-right-workflow` · `edit-vlog-15-minutes-smart-cut` · `what-ai-video-editors-can-automate` · `what-is-a-vlog` · `how-to-master-adventure-content-creation-like-karaandnate` · `how-to-master-travel-highlight-reels-like-nicolelaeno` — **均在 content-graph 62 篇登记表中**
- 本批 12 篇 + vlog 2 篇 — 均落盘于 `blog/food-beverage/` / `blog/vlog/`

**结论：无死链，无 G6 违规，无相对路径主站路由（所有主站链接均绝对 URL）。**

---

## 五、优化记录

### 5.1 已执行（2026-09-11）

- **C1 补 8 条反向链**：C2（§1 品类论证）· V1–V6（§2 格式库「各业态 hero format」段）· S1（§5 工具选型段）。
- **C3 补 4 条反向链**：F2（§2 plating 段）· F1（§2 ASMR 段）· V4（§2 cheese pull 段）· V3（§2 cross-section 段）。
- **验证**：`link_checker.py` 对两篇复跑全 PASS（无重复 slug / TL;DR 0 链接 / 无死链 / 无 G6 前缀）；`word_count_narrative.py` C1=2437、C3=3700（均 ≥2000 下限）。
- **效果**：零入链 8 → 0；R5 双向互链闭合；全库 R1–R5 通过。

### 5.2 遗留观察（非阻断）

| 项 | 说明 |
|----|------|
| C3 词数 3700 | 超 WorkflowHowTo 软上限 2800（硬 Gate 只有下限 2000）；作为 format canonical 偏长，可选精简 |
| 既有 62 篇的入链关系 | 本文档只覆盖本地 14 篇；既有 62 篇与本批 12 篇之间仅有「本批 → 既有 canonical」单向，需部署后回填时一并复核 |

---

## 六、维护节奏

| 时机 | 动作 |
|------|------|
| 每篇新稿发布前 | 对照 §三 对应簇「应链向」落实内链；跑 `tools/link_checker.py {file}` |
| 每篇新稿发布后 | 回填本文档 §一表、§三矩阵（✓）与 §四快照；同步 `content-graph.md`、`blog/README.md` |
| 每批 ≥3 篇后 | 扫零入链表，补 1 条/篇（有自然语境时） |
| 快照刷新 | 重跑 `rg '\]\(/blog/' blog/` 统计，更新本文档 §四与「快照」日期 |

---

*Sparki blog · blog-structure-internal-links · v1.1 · 2026-09-11（14 篇本地成稿实测 · 内链优化后）*
