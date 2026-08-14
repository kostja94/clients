# Lessie AI — Brand Visual Guidelines

> 遵循 [brand-visual](../../.cursor/skills/components/branding/brand-visual/SKILL.md) | 关联 [lessie.md](./lessie.md)  
> 基于官网 [lessie.ai](https://lessie.ai/) 提取  
> 用于：网站、落地页、场景页、Profile/List Directory、设计稿、前端实现

**Last updated**: 2026-03-16

---

## Brand Identity

- **Brand Name**: Lessie AI
- **Tagline**: "Agentic Search Engine to Find Anyone Instantly"
- **Sub-tagline**: "Find Influencers, B2B Leads, Investors, Talent, and Partners"
- **Website**: https://lessie.ai
- **App**: https://app.lessie.ai
- **Profile Directory**: https://profile.lessie.ai
- **List Directory**: https://lists.lessie.ai

---

## Logo

- **Wordmark**: "Lessie AI" — 官网主标识
- **Logo Format**: 主站、场景页、定价页统一使用 Lessie AI 品牌名
- **Favicon**: 需从官网确认
- **Minimum Clear Space**: 建议等于 logo 高度
- **多语言**: 中文「开始体验」、英文「Start for free」；日/韩/西/葡等见 hreflang

---

## Color Palette

> **说明**：以下色值需从 lessie.ai 官网 DevTools 提取验证。B2B SaaS / People Search 品类常见蓝/青/中性系。

### Primary Colors（待官网提取）

| Name | Hex（建议） | Usage |
|------|-------------|-------|
| Primary / CTA | 待提取 | 主按钮、链接、强调 |
| Background | 待提取 | 页面背景 |
| Card Background | 待提取 | 卡片、区块 |

### Secondary / Neutral（待官网提取）

| Name | Hex（建议） | Usage |
|------|-------------|-------|
| Text Primary | 待提取 | 标题、正文 |
| Text Secondary | 待提取 | 辅助文字、描述 |
| Border | 待提取 | 分割线、边框 |

### CTA 按钮

- **主 CTA**：官网统一为 "Start for free" / "开始体验" / "Search More" / "Find" / "Upgrade to Basic|Pro|Max"
- **样式**：待从官网提取（填充色、圆角、hover 状态）

---

## Typography

> **说明**：字体需从 lessie.ai 官网提取（Computed Styles / font-family）。

### Font Families（待官网提取）

| Role | Font（建议） | Fallback | 说明 |
|------|--------------|----------|------|
| Headings | 待提取 | sans-serif | H1–H3 |
| Body | 待提取 | sans-serif | 正文、描述 |
| UI / Button | 待提取 | sans-serif | 按钮、导航 |

### Type Scale（待官网提取）

| Element | Size（建议） | Weight | 用途 |
|---------|-------------|--------|------|
| H1 (Hero) | 待提取 | 待提取 | 首页、场景页主标题 |
| H2 (Section) | 待提取 | 待提取 | 区块标题 |
| H3 (Card Title) | 待提取 | 待提取 | 卡片、功能标题 |
| Body | 待提取 | 待提取 | 正文 |
| Caption | 待提取 | 待提取 | 辅助说明、元数据 |

---

## Spacing & Layout

- **Container Max Width**: 待从官网提取
- **Section Padding**: 待从官网提取
- **Card Padding**: 待从官网提取
- **Card Border Radius**: 待从官网提取
- **Grid Gap**: 待从官网提取
- **Base Spacing Unit**: 建议 8px（0.5rem）

---

## UI Components

### Buttons

| Variant | 说明 | 官网示例 |
|---------|------|----------|
| Primary (CTA) | 主行动按钮 | "Start for free", "Find", "Search More", "Upgrade to Basic" |
| Secondary | 次要操作 | "Check", "Check it", "Related list" |
| Link | 文字链接 | 场景页卡片、内链 |

### Cards

- **场景页卡片**：Influencer / Client / Talent / Partner 等，含数据（50M+、95%、300K+ 等）
- **Showcase 卡片**：示例查询 + 数字（如 115、157）
- **定价卡片**：Basic / Pro / Max，含 Credits、功能列表

### Navigation

- **主导航**：Solutions、Tools、Directory、Resources、Pricing
- **语言切换**：English 及多语言（de、es、fr、it、ja、ko、pt、ru、zh、zh-tw）
- **CTA 位置**：右上角 "Start for free"

---

## Content Voice & Tone

> 自 [lessie.md](./lessie.md) §8 Brand & Voice 迁移

- **Voice**: 高效、专业、自信、面向营销/销售/招聘人
- **Tone**: 强调「Find Anyone Instantly」「world's first」「replace manual search」「3x reply rates」
- **Avoid**: 过度技术化、冷冰冰的 AI 术语
- **Preferred terms**: "People Search AI Agent"、"agentic"、"find"、"instantly"
- **CTA Language**: Action-oriented（"Start for free"、"Find"、"Search More"、"Upgrade to Basic"）
- **Feature Descriptions**: Benefit-first，强调 50M+、95%、3x、100+ 数据源等 proof points

---

## SEO & Meta

- **Title Pattern**: `[Page] | Lessie AI` 或 `[Page] - Lessie AI`
- **Meta Description Style**: Action-oriented，含 "People Search AI"、"influencer finder" 等核心词
- **OG Image**: 待从官网确认
- **Canonical URL**: `https://lessie.ai/`（根域）；多语言 `https://lessie.ai/{lang}/`
- **hreflang**: en（根域）、de、es、fr、it、ja、ko、pt、ru、zh、zh-tw；x-default → lessie.ai

---

## 多语言

| 语言 | URL | CTA 示例 |
|------|-----|----------|
| en | lessie.ai | Start for free, Find, Search More |
| zh | lessie.ai/zh/ | 开始体验、寻找 |
| 其他 | lessie.ai/{lang}/ | 见各语言版 |

---

## Product Marketing Context (Section 12)

复制到 `.cursor/product-marketing-context.md` Section 12：

```markdown
## 12. Visual Identity

**Brand**: Lessie AI | Tagline: Agentic Search Engine to Find Anyone Instantly
**Colors**: 待从 lessie.ai 提取；B2B SaaS 常见蓝/青/中性
**Typography**: 待从官网提取
**CTA**: Start for free, Find, Search More, Upgrade to Basic|Pro|Max
**Voice**: 高效、专业、自信；Preferred: People Search AI Agent, agentic, find, instantly
**SEO**: Title [Page] | Lessie AI；hreflang 覆盖 11 种语言
```

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Logo, Colors, Typography | Hero, CTA, footer, 场景页、Profile/List |
| Spacing, UI Components | Layout, cards, navigation, 定价页 |
| Voice & Tone | Copywriting, CTA, metadata, Blog |
| SEO & Meta | Title, description, OG image, hreflang |

---

## 验证要点（对照 brand-visual skill）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Logo 使用规则 | ⚠ | 待补充 clear space、favicon |
| 色彩体系 | ⚠ | 待从官网 DevTools 提取 HEX |
| 字体层级 | ⚠ | 待从官网提取 font-family |
| 间距规范 | ⚠ | 待从官网提取 |
| 组件规范 | ✓ | 按钮、卡片、导航有描述 |
| CTA 一致性 | ✓ | Start for free, Find, Search More |
| Voice & Tone | ✓ | 自 lessie.md 迁移完整 |
| 多语言 | ✓ | hreflang、CTA 已列 |

---

## 文档导航

| 文档 | 用途 |
|------|------|
| [lessie.md](./lessie.md) | 主文档、产品概览、定位（Brand & Voice 已迁移至本文档） |
| [lessie-features.md](./lessie-features.md) | 功能、产品线、四步流程 |
| [lessie-profile.md](./lessie-profile.md) | Profile Directory |
| [lessie-lists.md](./lessie-lists.md) | List Directory |
| [lessie-tools.md](./lessie-tools.md) | 资源工具 |
| [lessie-use-cases.md](./lessie-use-cases.md) | Use Cases |
| [lessie-competitors.md](./lessie-competitors.md) | 竞品分析 |
| [lessie-keywords.md](./lessie-keywords.md) | 关键词映射 |
