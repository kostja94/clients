# Vofy — Brand Visual Guidelines

> 遵循 [brand-visual](../../.cursor/skills/components/branding/brand-visual/SKILL.md)（若本地路径不同，以对应用 Cursor skills 中的 brand-visual 为准）  
> 关联：[vofy.md](./vofy.md) · [vofy-site-structure.md](./vofy-site-structure.md) · [vofy-use-cases.md](./vofy-use-cases.md)  
> **来源**：官网 [vofy.art](https://www.vofy.art/) 公开文案与站面结构（见 demo 归纳文档）；**色值、字体栈、圆角、阴影等实现层代币须以线上构建为准**，请在浏览器 DevTools → Computed / Sources 中核对后回填本文「线上令牌」表。  
> 用于：官网延展、模型/活动着陆页、Apps hub、社群物料、Brief 给设计与前端。

**Last updated**：2026-04-30

---

## Brand Identity

| 项 | 内容 |
|----|------|
| **Brand Name** | Vofy（站面亦可见 **VOFY** 大写形式） |
| **One-line（公开）** | Your All-in-One AI Creative Studio |
| **Hero 问句（首页）** | What do you want to create? |
| **Website** | https://www.vofy.art/ |
| **次级入口** | [Apps](https://www.vofy.art/apps)、[Discord](https://www.vofy.art/)（导航常见外链心智） |
| **品类气质** | **消费级 / 创作者向**多模型创意工作室：图像 + 视频 + 海量场景化微工具；**上新节奏快**（What’s New 轮播）、**积分（Credits）**透明、**社区作品墙**作社交证明 |
| **促销** | 站面可出现条幅类折扣（如 **-30%**，**以实时为准**，勿写死在品牌色里） |

---

## Logo

- **主标识**：导航与页眉中的 **Vofy / VOFY** 字标（具体 SVG/PNG、favicon、`apple-touch-icon` 以线上 `_next` 或静态资源为准）。
- **Minimum Clear Space**：建议 **≥ 字标高度 0.5×** 四周留白；勿横向拉伸、勿与强噪点社区缩略图拼贴争夺辨识度。
- **深色 / 浅色场景**：工作室与营销区可能同时存在深浅背景 — 维护 **反白稿 / 单色稿** 两套（若产品侧有 Logo Kit，在此补充下载路径）。
- **禁止**：与「What’s New」第三方模型 Logo 混排时冒充官方联名；投放素材需符合各模型品牌指南。

---

## Color Palette

### A. 线上令牌（待 DevTools 回填）

> 下列表需在 **vofy.art** 对 **header / 主 CTA / 主背景 / 卡片** 抽样后填写 HEX 或 CSS 变量名；当前为 **占位**，避免与真实构建不一致。

| Name | Hex / Token（待填） | 用途 |
|------|---------------------|------|
| Background primary | 待提取 | 页身主背景 |
| Surface / Card | 待提取 | 卡片、画布侧栏 |
| Text primary | 待提取 | 标题、主正文 |
| Text secondary | 待提取 | 描述、元数据 |
| Border / Divider | 待提取 | 分割线、描边 |
| CTA primary | 待提取 | Create now、主按钮 |
| CTA primary text | 待提取 | 主按钮字色 |
| Accent / Link | 待提取 | 文字链、高亮 |
| Discount / Promo banner | 待提取（或时令） | 顶部促销条 |

### B. Demo 扩展页参考（非官方令牌）

仓库内 [models/seedance-2/index.html](./models/seedance-2/index.html) 为 **深色电影感**营销 demo，仅供内部对齐「Seedance / 视频向」活动页情绪板，**不作为** vofy.art 主站唯一真实来源：

| 角色 | 参考 Hex | 说明 |
|------|----------|------|
| 深底 | `#07080f` | Hero 背景倾向 |
| 表面 | `#0f111a` / `#161a26` | 卡片层级 |
| 强调（青绿） | `#3ee0c4` | CTA / 标点（与「生成感、工作室」偏科技一致） |
| 正文 | `#e8eaf0` | 主字 |
| 次要 | `#9aa3b5` | 辅文 |

上线活动页若需与主站一致，**必须改用最接近线上的变量**。

### 无障碍

- 正文与背景对比建议 **≥ 4.5 : 1**；大号标题 **≥ 3 : 1**。
- **勿单独用颜色**表状态（成功/失败/可点）；配合文案或图标。
- 动画尊重 `prefers-reduced-motion`；社媒导出避免强闪烁。

---

## Typography

### 线上字体（待 DevTools 回填）

| 角色 | Font（待填） | 用途 |
|------|--------------|------|
| Headings | 待提取 | H1 Hero、区块标题 |
| Body / UI | 待提取 | 正文、按钮、导航 |
| Monospace（若有） | 待提取 | Credits、技术参数 |

### Type Scale（待对齐线上）

| Element | 用途 |
|---------|------|
| H1（Hero） | 「What do you want to create?」级主标题 |
| H2 | **WHAT'S NEW**、**COMMUNITY** 等分区标题（站面常用全大写强调） |
| H3 | 卡片标题（如 **Create Video**、模型名 **SEEDANCE 2.0**） |
| Body | 模型一句描述、工具说明 |
| Caption | Credits 价签、小字法律链 |

### Demo 扩展页字体（仅 seedance-landing）

| 角色 | 字体 | 说明 |
|------|------|------|
| Display | Syne | Hero 标题个性 |
| Body | DM Sans | 正文与按钮 |

---

## Spacing & Layout

- **Base unit**：建议 **8px**，与常见设计系统对齐。
- **Container max-width**：待从首页与 `/apps` 列表提取。
- **Section padding**：待提取；社区瀑布流区与 Hero 密度不同，宜分档（紧凑 / 舒适）。
- **Radius**：主按钮、卡片、输入框圆角 — **以线上统一为准**，避免用 demo 的 14px 硬套主站。
- **栅格**：What’s New 为横滑卡片；Community 为瀑布流 — 营销页复刻时优先 **保持与首页信息架构一致**，而非自创多栏。

---

## UI Components

### Buttons & CTAs

| 变体 | 站面语义（归纳） | 示例文案 |
|------|------------------|----------|
| Primary | 进入创作 / 试用新模型 | Create now、**Try Now**（条幅）、打开带 `model=` 的 Studio |
| Secondary | 并列创作入口 | Create Video、Create Image、Motion Control、Inpaint Image |
| Tertiary / Nav | 全站导航 | Explore、Image、Video、Apps、Assets |
| Credits 提示 | 计价心智 | 如首页 **2.5 Credits**（随模型变化） |

### Cards

- **快捷入口卡**：Create Video / Image / Motion Control / Inpaint / Apps — 图标 + 短标题。
- **What’s New 卡**：模型名（常全大写）+ 一句话利益 + 链至 `/studio/create/...`。
- **Community 卡**：创作者 handle、prompt 节选、互动计数 — **UGC 真实感**优先于精修 stock。

### Navigation

- 顶栏：**Logo**、**Explore / Image / Video / Apps / Assets**、**Discord**、账户区（以线上为准）。
- 促销条：可与 nav 叠放 — 注意 **首屏高度**与 **主 CTA 可见性**（尤其移动端）。

### 图标

- 使用 **一致图标集**（如 Lucide / Heroicons）；**禁止用 emoji 充当 UI 功能图标**（与 brand-visual skill 一致）。

---

## Imagery & Motion

- **题材**：真实 UI 截图、生成结果对比、**社区作品**截帧；突出「多模型、一站式」而非单点工具。
- **调性**：偏 **活力、创作者向**；可适度电影感用于 **视频模型**专场，但与主站浅色/中性主氛围冲突时需单独定义「活动子主题」。
- **视频**：Hero 或 What’s New 可截短循环预览；控制体积以保障 LCP。
- **权利**：含人像、换脸、亲密动效类工具时，营销素材需预留 **合规提示位**（参见 [vofy-features.md](./vofy-features.md) §七）。

---

## Content Voice & Tone

> 综合 [vofy.md](./vofy.md)、[vofy-use-cases.md](./vofy-use-cases.md) 与首页可见英文。

- **Voice**：直接、行动导向、**偏低摩擦** — 强调「想做什么」而非「我们是谁的长篇」。
- **Tone**：兴奋度适中偏**务实**：新模型用 **强利益词**（cinematic、native audio、1080p、Flash speed）；计价处 **诚实展示 Credits**。
- **Avoid**：空泛「Transform your creativity」、过度承诺 **未官宣的分辨率/时长**、与 **Grok 等第三方品牌**混排导致品牌混淆（见 [vofy-site-structure.md](./vofy-site-structure.md)「快速修复观察项」）。
- **Preferred patterns**：
  - 问句开头：「What do you want to create?」
  - 动宾短语：Create Video、**Motion Control**、**Inpaint Image**
  - 模型行：「**[MODEL NAME]** + 一句具体能力」（与英文站一致时保持全大写惯例）
- **CTA 语言**：Create now、Try Now、跳转 **Studio** 预设 URL；避免同一屏 **多个等价主 CTA** 抢转化。

---

## SEO & Meta

- **Title pattern**（建议）：`[Model or Tool] — [Benefit] | Vofy` 或 `Vofy — [All-in-One AI Creative Studio]`（首页）。
- **Description**：含 **Credits**、**multi-model**、**video/image** 等品类词；模型页对齐 **品牌模型名**（Seedance、Veo、Kling 等）。
- **Canonical**：以各页的官方 **首选 URL** 为准；带 `model=` 的 Studio 链接可能变更 — 内容外链需定期 **reconcile**。
- **OG Image**：待品牌/产品导出模板；需支持 **暗色社区截图**与 **亮色营销**两套 Safe zone。

---

## Product Marketing Context（Section 12）

可复制到 `.cursor/product-marketing-context.md` 或项目级营销上下文的 **Section 12**：

```markdown
## 12. Visual Identity

**Brand**: Vofy | Tagline: All-in-One AI Creative Studio
**Hero prompt**: What do you want to create?
**Colors**: 待从 vofy.art DevTools 提取；demo 深色活动页参考见 clients/vofy/vofy-brand-visual.md §「Demo 扩展页」
**Typography**: 待从线上提取
**CTA**: Create now, Try Now, Create Video/Image/Motion Control/Inpaint, Apps
**Voice**: 行动导向、低摩擦、Credits 透明；模型一句利益 + What’s New 节奏
**SEO**: 模型着陆与 /apps 长尾区分 Title；避免 Grok 等与 Vofy 品牌混淆
```

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Logo, Colors, Typography | 官网、着陆页、App 内嵌 Web、邮件头图 |
| Spacing, UI Components | Studio 外包营销页、程序化 /apps 模板 |
| Voice & Tone | 英文文案、Discord、广告文案 |
| Imagery & Motion | 视频模型发布、社区运营、短贴片 |
| SEO & Meta | 模型页、sitemap、分享卡片 |

---

## 验证要点（对照 brand-visual skill）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Logo 使用规则 | ⚠ | clear space、favicon 待产品导出 |
| 色彩体系 | ⚠ | **须从 vofy.art 提取**真实 HEX/CSS 变量 |
| 字体层级 | ⚠ | **须从线上**核对 |
| 间距与圆角 | ⚠ | 与 Next 构建同步 |
| 组件规范 | ✓ | CTA / 卡片 / 导航结构已按站面归纳 |
| CTA 一致性 | ✓ | 单一主目标/屏；Try Now 与 Create now 分层 |
| Voice & Tone | ✓ | 与 ICP、首页话术对齐 |
| 无障碍 | ⚠ | 提取后需跑对比度与 focus 状态 |

---

## 文档导航

| 文档 | 用途 |
|------|------|
| [vofy.md](./vofy.md) | 主文档、ICP、索引 |
| [vofy-brand-visual.md](./vofy-brand-visual.md) | **本文档**：视觉与语气规范 |
| [vofy-features.md](./vofy-features.md) | 模型矩阵、Credits、Studio URL 形态 |
| [vofy-site-structure.md](./vofy-site-structure.md) | 首页模块、/apps IA、内容机会 |
| [vofy-use-cases.md](./vofy-use-cases.md) | 人物画像与场景 |
| [vofy-keywords.md](./vofy-keywords.md) | 关键词与 URL 推断 |
| [vofy-competitors.md](./vofy-competitors.md) | 竞品与差异化 |
| [models/seedance-2/](./models/seedance-2/) | Demo 深色着陆 HTML（非官方设计系统） |

---

*Demo 品牌视觉规范包 · 实现数值以便与 [vofy.art](https://www.vofy.art/) 线上一致为准*
