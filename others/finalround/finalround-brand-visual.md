# Final Round AI - Brand Visual Guidelines

> 本文档专注**品牌视觉**（色彩、字体、设计、CTA）。  
> 产品功能 → [finalround-features.md](./finalround-features.md) | Blog CTA 规范 → 本文档 §5  
> 来源：[finalroundai.com](https://www.finalroundai.com/)

**Last updated**: 2026-03-12

---

## 1. 色彩系统

### 1.1 核心色板（Core Palette）

| 用途 | 色值 | 说明 |
|------|------|------|
| **Primary Orange** | `#FF4800` | 按钮、CTA、高亮（官网出现 29 次） |
| **Dark Charcoal** | `#1C1D20` | 深色区块背景、深色文字（14 次） |
| **White** | `#FFFFFF` | 所有浅色背景（30 次） |
| **Text Black** | `#0A0A0A` | 正文主色 |
| **Secondary Gray** | `#6B7280` | 辅助文字、元数据 |
| **Link Blue** | `#9FC4FF` | 链接、次要强调 |

### 1.2 橙色渐变谱（Orange Spectrum）

| 用途 | 色值 | 说明 |
|------|------|------|
| 最浅 | `#FFF8EE` | 蜜桃色 / 暖色区块背景 |
| 浅橙 | `#FFCFBC` / `#FFCABF` | 腮红 / 浅橙填充 |
| 亮橙 | `#FF9C3F` | 亮橙变体 |
| 暖橙 | `#FF7640` | 暖橙 / hover 状态 |
| **主色** | `#FF4800` | ⭐ 所有 IG 图文主色 |
| 深橙 | `#F54E00` / `#EF5C01` | 深橙变体 / 按下状态 |
| 焦橙 | `#802400` | 焦橙 / 深阴影（5 次） |

### 1.3 IG 视频图文公式

```
主色：#FF4800
高光：#FF7640
阴影：#802400
背景：仅 white 或 #1C1D20 charcoal
```

---

## 2. 字体（Typography）

| 层级 | 字体 | 字号 | 用途 |
|------|------|------|------|
| **H1** | Instrument Serif（衬线） | 48px | 主标题 |
| **H2** | Instrument Serif | 30px | 副标题 |
| **正文 / UI** | Roboto → system sans-serif | 12–16px | 正文、界面 |

---

## 3. 设计规范

| 项目 | 规范 |
|------|------|
| **框架** | Tailwind CSS |
| **圆角** | 6–10px |
| **按钮** | `#FF4800` 填充、白色文字、8px 圆角、无阴影 |

---

## 4. CSS 变量（供前端使用）

```css
:root {
  /* Core */
  --fr-primary: #FF4800;
  --fr-charcoal: #1C1D20;
  --fr-white: #FFFFFF;
  --fr-text: #0A0A0A;
  --fr-gray: #6B7280;
  --fr-link: #9FC4FF;

  /* Orange spectrum */
  --fr-peach: #FFF8EE;
  --fr-blush: #FFCFBC;
  --fr-light-orange: #FF9C3F;
  --fr-warm-orange: #FF7640;
  --fr-dark-orange: #F54E00;
  --fr-burnt: #802400;

  /* Typography */
  --fr-font-heading: 'Instrument Serif', serif;
  --fr-font-body: 'Roboto', system-ui, sans-serif;
  --fr-h1: 48px;
  --fr-h2: 30px;
  --fr-body: 12px; /* 12–16px range */

  /* UI */
  --fr-radius: 8px;
  --fr-radius-lg: 10px;
}
```

---

## 5. 使用规则

- **CTA / 按钮**：一律使用 `#FF4800`，白字，8px 圆角
- **IG 图文**：主色 `#FF4800`，高光 `#FF7640`，阴影 `#802400`
- **背景**：仅 `#FFFFFF` 或 `#1C1D20`，避免杂色
- **链接**：`#9FC4FF`，hover 可加深或加下划线
- **正文**：`#0A0A0A`；辅助文字 `#6B7280`

---

## 6. 文档导航

| 文档 | 用途 | 何时查阅 |
|------|------|----------|
| [finalround.md](./finalround.md) | 主文档、产品概览 | 了解产品全貌 |
| [finalround-brand-visual.md](./finalround-brand-visual.md) | 品牌色彩、设计规范、CTA | 本文档 |
| [finalround-features.md](./finalround-features.md) | 功能、定价 | 产品详情 |
| [finalround-blog.md](./blog/finalround-blog.md) | Blog 内容策略 | 文章 CTA |
| [finalround-keywords.md](./finalround-keywords.md) | 关键词映射 | 写文案、SEO |
| [finalround-use-cases.md](./finalround-use-cases.md) | Use Cases、场景 | 场景页 |
| [finalround-site-structure.md](./finalround-site-structure.md) | 落地页 URL 与结构 | 建站 |
| [finalround-competitors.md](./finalround-competitors.md) | 竞品分析 | 对比页 |
| [finalround-project-tasks.md](./finalround-project-tasks.md) | 项目任务 | 执行任务 |
