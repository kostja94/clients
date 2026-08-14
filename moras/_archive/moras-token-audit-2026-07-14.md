# Moras Token 审计报告

> **类型**: 设计 Token 一致性审计 | **日期**: 2026-07-14 | **对标规范**: `demo/docs/style.md`
>
> **审计范围**: 全站 56 个已上线页面, 8 样本 (首页 ×1 / 静态页 ×1 / Product ×1 / Tools ×1 / Use Cases ×1 / TikTok Video Generator ×1 / Blog ×1)
>
> **数据来源**: `site-sitemap.xml` + `seo-sitemap.xml`，CSS 静态文件双向校验，实际 HTML class 提取

---

## 执行摘要

全站存在 **两套完全独立的设计 token 系统**，无共享 CSS 自定义属性。两套管线在颜色、字体族、字号、行高、圆角、间距等多个维度均不一致。本报告聚焦 **排版 (Typography) 统一**，颜色 token 统一建议作为后续优化项。

---

## 管线定义

| 管线 | CSS 路径 | 覆盖页面 | 页面数 |
|------|----------|----------|:------:|
| **Pipeline A — 首页 SPA** | `/_next/static/css/*.css` (3 文件) | `/` | 1 |
| **Pipeline B — SEO 页面** | `/seo-static/_next/static/css/1938677c2da06320.css` | `/about` `/pricing` `/product-research` `/tools/*` `/use-cases/*` `/tiktok-video-generator/*` `/blog/*` `/terms` `/privacy` `/precheck-guidance` `/subscription` `/landing` `/managedLanding` | 55 |

---

## 当前排版参数完整快照

### Pipeline A — 首页 (基准 / 规范)

```yaml
typography:
  naming: "--moras-font-size-*"  # 语义命名空间
  font_family:
    display: '-apple-system, "Noto Sans SC", "PingFang SC", "Helvetica Neue", "Microsoft YaHei", system-ui, sans-serif'
    body: '-apple-system, "Noto Sans SC", "PingFang SC", "Helvetica Neue", "Microsoft YaHei", system-ui, sans-serif'
    mono: 'ui-monospace, "SF Mono", Menlo, "Cascadia Mono", monospace'
  font_size:
    display_xl: 72px    # token: --moras-font-size-display-xl
    display:    56px    # token: --moras-font-size-display
    h1:         40px    # token: --moras-font-size-h1
    h2:         32px    # token: --moras-font-size-h2
    h3:         24px    # token: --moras-font-size-h3
    h4:         20px    # token: --moras-font-size-h4
    body_lg:    18px    # token: --moras-font-size-body-lg
    body:       16px    # token: --moras-font-size-body
    body_sm:    14px    # token: --moras-font-size-body-sm
    caption:    13px    # token: --moras-font-size-caption
    mono:       14px    # token: --moras-font-size-mono
  line_height:
    display_xl: 1.05
    display:    1.08
    h1:         1.15
    h2:         1.20
    h3:         1.30
    h4:         1.35
    body_lg:    1.55
    body:       1.55
    body_sm:    1.50
    caption:    1.45
    mono:       1.55
  font_weight:
    bold:     700
    semibold: 600
    medium:   500
    regular:  400
  letter_spacing:
    body:     0
    heading:  0
    caption:  0.02em
    eyebrow:  0.12em
```

### Pipeline B — SEO 页面 (现状 / 需修复)

```yaml
typography:
  naming: "Tailwind --text-* (无级命名) + 裸 CSS h1-h6 覆盖"
  font_family:
    display: '"SF Pro", "SF Pro SC", "PingFang SC", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    body:    '"SF Pro", "SF Pro SC", "PingFang SC", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    mono:    '"SF Pro", "SF Pro SC", "PingFang SC", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'   # ⚠️ mono 未独立
  font_size:
    # Tailwind vars:
    text_xs:   12px     # --text-xs: 0.75rem
    text_sm:   14px     # --text-sm: 0.875rem
    text_base: 16px     # --text-base: 1rem
    text_lg:   18px     # --text-lg: 1.125rem
    text_xl:   20px     # --text-xl: 1.25rem
    text_2xl:  24px     # --text-2xl: 1.5rem
    text_3xl:  30px     # --text-3xl: 1.875rem
    text_4xl:  36px     # --text-4xl: 2.25rem
    text_5xl:  48px     # --text-5xl: 3rem
    text_6xl:  60px     # --text-6xl: 3.75rem
    text_7xl:  72px     # --text-7xl: 4.5rem
    text_8xl:  96px     # --text-8xl: 6rem
    # 实际 HTML h1-h6 覆盖:
    h1_override: clamp(32px, 2vw, 40px)     # ⚠️ 多组规则互相覆盖
    h2_override: clamp(26px, 1.18vw, 34px)  # ⚠️ 含 !important + 硬编码颜色 #3a2a22
    h3_override: clamp(20px, 0.5vw, 24px)   # ⚠️ 含 !important
    h4_override: 24px                        # ⚠️ 比首页大 4px
  line_height:
    normal:  1.50     # --leading-normal
    relaxed: 1.625    # --leading-relaxed
    snug:    1.375    # --leading-snug
    tight:   1.25     # --leading-tight
    # 实际 h 元素:
    h1: 1.12
    h2: 1.15 ~ 1.18   # ⚠️ 多组值
    h3: 1.20 ~ 1.25   # ⚠️ 多组值
    h4: 1.17
  font_weight:
    bold:     700
    semibold: 600
    medium:   500
    normal:   400
    light:    300
  letter_spacing:
    normal:  0em
    tight:   -0.025em
    wide:    0.025em
    wider:   0.05em
    widest:  0.1em
    h1_specific: -0.02em   # ⚠️ h1 单独覆写
```

---

## 差异矩阵 (Pipeline A vs Pipeline B)

| 维度 | 具体项 | Pipeline A | Pipeline B | 严重度 |
|------|--------|:-:|:-:|:--:|
| **字号** | Display/XL | 有 (72/56px) | 无对应语义 | 🟡 |
| **字号** | H1 | 40px 固定 | clamp(32, 2vw, 40) 流式 | 🟡 |
| **字号** | H2 | 32px 固定 | clamp(26, 1vw, 34) + 28px 两版混用 | 🔴 |
| **字号** | H3 | 24px 固定 | clamp(20, 0.5vw, 24) + clamp(22, 1vw, 28) 两版混用 | 🔴 |
| **字号** | H4 | 20px 固定 | 24px 固定 | 🟡 |
| **行高** | H1 | 1.15 | 1.12 | 🟢 |
| **行高** | H2 | 1.20 | 1.15~1.18 | 🟡 |
| **行高** | H3 | 1.30 | 1.20~1.25 | 🟡 |
| **行高** | H4 | 1.35 | 1.17 | 🔴 |
| **字体** | display | 系统栈 + Noto Sans SC | SF Pro + PingFang + MS YaHei | 🔴 |
| **字体** | body | 系统栈 + Noto Sans SC | SF Pro + PingFang + MS YaHei | 🔴 |
| **字体** | mono | 独立 mono 栈 | 回退到 sans (未独立) | 🟡 |
| **CSS 规则** | 级联稳定性 | 单一来源，无覆盖 | h1-h6 至少 5 组规则，含 !important | 🔴 |
| **硬编码颜色** | 在排版规则中 | 0 处 | h2 含 `color:#3a2a22!important` + 装饰线 `#22c5d1` | 🔴 |

---

## 违规明细

### 1. 级联覆盖混乱

SEO 管线中 `h2` 至少被 **5 组 CSS 规则**先后覆写，其中第 4 组含 `!important`:

```css
/* 规则 1 */  h2 { font-size:1.75rem;line-height:1.15 }
/* 规则 2 */  h2 { font-size:2rem }
/* 规则 3 */  h2 { letter-spacing:0;color:#3a2a22!important }
/* 规则 4 */  h2 { ... font-size:clamp(...) !important;line-height:1.18 !important }
/* 规则 5 */  h2 { color:#3a2a22 }  /* 硬编码 */
```

**影响**: 任何后续维护都会与 `!important` 对抗, 极难调试。

### 2. 排版规则耦合装饰性样式

h2 规则内嵌入了 `content:""` 装饰下划线和 `box-shadow` glow:

```css
h2 {
  content: "";
  background: #22c5d1;
  border-radius: 999px;
  width: 3rem;
  height: .1875rem;
  margin-bottom: 1rem;
  display: block;
  box-shadow: 0 10px 28px -14px #22c5d1e6;
}
```

`style.md` §6 禁止装饰性元素; 此规范在此被违反且耦合到了排版规则中。

### 3. 字体栈不统一

- Pipeline B 首选项 `SF Pro` → 非 Apple 设备直接跳过 → 视觉回落不一致
- Pipeline A 直接用系统原生字体栈 → 跨平台一致

---

## 优化建议

### 策略: 分阶段统一, 优先排版

| 阶段 | 内容 | 预估影响 | 建议时间 |
|:--:|------|:--:|:--:|
| **Phase 1** | 统一排版 token (字号/行高/字重/字间距) + 字体栈 | 全站 56 页 | 1-2 sprint |
| **Phase 2** | 统一颜色 token + 圆角 + 阴影 | 全站 | 后续 |
| **Phase 3** | SEO 底部 CTA 硬编码颜色替换 | 48 页 | 后续 |

---

### Phase 1 — 排版统一方案

#### 1.1 创建共享 Typography Token 文件

将以下 token 定义为全站唯一的排版事实来源 (Single Source of Truth):

```css
/* === typography-tokens.css — 全站唯一排版 SSoT === */

:root {
  /* 字体族 */
  --font-display: -apple-system, "Noto Sans SC", "PingFang SC",
                  "Helvetica Neue", "Microsoft YaHei", system-ui, sans-serif;
  --font-body:    -apple-system, "Noto Sans SC", "PingFang SC",
                  "Helvetica Neue", "Microsoft YaHei", system-ui, sans-serif;
  --font-mono:    ui-monospace, "SF Mono", Menlo, "Cascadia Mono", monospace;

  /* 字号 (9 级, 固定 px, 禁止即兴增减) */
  --fs-display-xl: 72px;
  --fs-display:    56px;
  --fs-h1:         40px;
  --fs-h2:         32px;
  --fs-h3:         24px;
  --fs-h4:         20px;
  --fs-lead:       18px;   /* 大正文 */
  --fs-body:       16px;
  --fs-sm:         14px;
  --fs-caption:    13px;

  /* 行高 */
  --lh-display-xl: 1.05;
  --lh-display:    1.08;
  --lh-h1:         1.15;
  --lh-h2:         1.20;
  --lh-h3:         1.30;
  --lh-h4:         1.35;
  --lh-lead:       1.55;
  --lh-body:       1.55;
  --lh-sm:         1.50;
  --lh-caption:    1.45;

  /* 字重 (禁止在组件中使用裸 300/400/500/600/700) */
  --fw-light:    300;
  --fw-regular:  400;
  --fw-medium:   500;
  --fw-semibold: 600;
  --fw-bold:     700;

  /* 字间距 */
  --ls-heading: 0;
  --ls-body:    0;
  --ls-caption: 0.02em;
  --ls-eyebrow: 0.12em;
}
```

#### 1.2 首页适配 (Pipeline A)

**操作**: 替换现有 `--moras-font-size-*` → 新的 `--fs-*` / `--lh-*` (值不变, 只改命名).

需要替换的 token 映射:

| 旧 token | 新 token | 值不变? |
|----------|----------|:--:|
| `--moras-font-size-display-xl` | `--fs-display-xl` | ✅ |
| `--moras-font-size-display`    | `--fs-display`    | ✅ |
| `--moras-font-size-h1`         | `--fs-h1`         | ✅ |
| `--moras-font-size-h2`         | `--fs-h2`         | ✅ |
| `--moras-font-size-h3`         | `--fs-h3`         | ✅ |
| `--moras-font-size-h4`         | `--fs-h4`         | ✅ |
| `--moras-font-size-body-lg`    | `--fs-lead`       | ✅ |
| `--moras-font-size-body`       | `--fs-body`       | ✅ |
| `--moras-font-size-body-sm`    | `--fs-sm`         | ✅ |
| `--moras-font-size-caption`    | `--fs-caption`    | ✅ |
| `--moras-font-size-mono`       | `--fs-sm`         | ✅ |
| `--moras-line-height-*`        | `--lh-*`          | ✅ |
| `--moras-font-weight-*`        | `--fw-*`          | ✅ |
| `--moras-tracking-*`           | `--ls-*`          | ✅ |
| `--moras-font-display`         | `--font-display`  | ✅ |
| `--moras-font-body`            | `--font-body`     | ✅ |
| `--moras-font-mono`            | `--font-mono`     | ✅ |

**影响文件**: `/_next/static/css/b510c294d85136f0.css`, `a50bdf7e082c4f45.css`, `d1b5976f598f3010.css`

#### 1.3 SEO 页面适配 (Pipeline B)

这是最大的改动面。SEO 管线当前使用 Tailwind 原生字号体系, 需重新映射。

**目标**: 将 `h1-h4` 从当前的 clamp 流式 + !important 覆盖, 统一为固定 px + 新 token。

**当前 h1-h4 样式**→ **目标样式**:

| 元素 | 当前 CSS | 替换为 |
|------|----------|--------|
| h1 | `clamp(32px, 2vw, 40px); lh:1.12` | `font-size: var(--fs-h1); line-height: var(--lh-h1)` |
| h2 | `clamp(26px, 1vw, 34px) !important; lh:1.18 !important` | `font-size: var(--fs-h2); line-height: var(--lh-h2)` |
| h3 | `clamp(20px, 0.5vw, 24px) !important; lh:1.25 !important` | `font-size: var(--fs-h3); line-height: var(--lh-h3)` |
| h4 | `24px; lh:1.17` | `font-size: var(--fs-h4); line-height: var(--lh-h4)` |

**需要同时执行的清理**:

- [ ] 删除 h2 内嵌的 `content:""` 装饰下划线规则 (迁移到独立 utility class 或移除)
- [ ] 删除 h2 的 `color:#3a2a22!important` 硬编码
- [ ] 删除全部 `!important` 修饰
- [ ] 删除 h2 的 5 组重复规则, 合并为 1 组
- [ ] 删除 h3 的 3 组重复规则, 合并为 1 组

**字体栈对齐**: SEO 管线 `--font-sans` / `--font-display` / `--font-mono` 全部替换为新的统一值。

#### 1.4 SEO 页面向 Body 字号的额外对齐

当前 SEO 页面使用 Tailwind `text-sm` / `text-base` / `text-lg` 作为 body 级字号:

| Tailwind class | 当前值 | 目标值 | 操作 |
|----------------|--------|--------|------|
| `text-sm`       | 14px (0.875rem) | 不变 | ✅ 无需改动 |
| `text-base`     | 16px (1rem)     | 不变 | ✅ 无需改动 |
| `text-lg`       | 18px (1.125rem)| 不变 | ✅ 无需改动 |

行高对齐:

| Tailwind class | 当前 leading | 目标 line-height | 操作 |
|----------------|:-----------:|:----------------:|------|
| `text-base leading-relaxed` | 1.625 | `var(--lh-body)` → 1.55 | 微调 |
| `text-sm text-muted-foreground` | 默认 | `var(--lh-sm)` → 1.50 | 显式声明 |

---

### Phase 2 — 颜色 Token 统一 (后续)

本阶段不涉及排版变更, 仅在此列出差异供后续参考:

| Pipeline A color | Pipeline B color | 差异 |
|-----------------|-----------------|------|
| `--moras-color-primary: #22c5d1` | `--primary: #086eff` | 🔴 青绿 vs 蓝色 |
| `--moras-color-bg-default: #fbf5ee` | `--background: #050917` | 🔴 暖奶油 vs 深海军蓝 |
| `--moras-color-text-primary: #3d2a1f` | `--foreground: #fff` | 🔴 深棕 vs 白色 |

---

## 迁移检查清单

### Pipeline A (首页)

- [ ] 提取 `typography-tokens.css` 到共享层
- [ ] 替换 `--moras-font-size-*` → `--fs-*`
- [ ] 替换 `--moras-line-height-*` → `--lh-*`
- [ ] 替换 `--moras-font-weight-*` → `--fw-*`
- [ ] 替换 `--moras-tracking-*` → `--ls-*`
- [ ] 替换 `--moras-font-display` / `--moras-font-body` / `--moras-font-mono` → `--font-*`
- [ ] 视觉回归测试 (Hero / Features / Showcase / Pricing / CTA 各区块)
- [ ] 移动端 (375px) 验证

### Pipeline B (SEO, 55 页)

- [ ] 引入共享 `typography-tokens.css`
- [ ] 替换 `--font-sans` / `--font-display` → 统一值
- [ ] 替换 `--font-mono` → 独立 mono 栈 (当前错误地指向 sans)
- [ ] 重写 h1 → `font-size: var(--fs-h1)`
- [ ] 重写 h2 → `font-size: var(--fs-h2); line-height: var(--lh-h2)` (清理 5 组规则 + !important)
- [ ] 重写 h3 → `font-size: var(--fs-h3); line-height: var(--lh-h3)` (清理 3 组规则)
- [ ] 重写 h4 → `font-size: var(--fs-h4); line-height: var(--lh-h4)` (24px→20px)
- [ ] 删除 h2 装饰下划线规则 (或迁移到独立 utility)
- [ ] 删除所有 h 元素 `!important` 修饰
- [ ] `leading-relaxed` → 显式 `var(--lh-body)`
- [ ] 7 类页面各抽 1 样本做视觉回归: about / pricing / product-research / tool / use-case / tvg-vertical / blog-post
- [ ] 移动端 (375px) + 平板 (768px) 验证 (clamp → 固定 px 需确认不会破坏响应式布局)

---

## 附录 A: 页面分类与受影响程度

| 页面类型 | 数量 | 管线 | 受排版影响 | 备注 |
|----------|:--:|------|:--:|------|
| 首页 `/` | 1 | Pipeline A | 仅改名 | 值不变, 无视觉变化 |
| 静态页 (非首页) | 8 | Pipeline B | h1-h4 重写 | 含 /about /pricing /terms 等 |
| Product | 1 | Pipeline B | h1-h4 重写 | /product-research |
| Tools | 3 | Pipeline B | h1-h4 重写 | |
| Use Cases | 7 | Pipeline B | h1-h4 重写 | |
| TikTok Video Generator | 16 | Pipeline B | h1-h4 重写 | |
| Blog | 20 | Pipeline B | h1-h4 重写 + prose 行高 | |

---

## 附录 B: 审计方法

- **CSS 提取**: 下载 2 套管线 CSS 静态文件全文 (`1938677c2da06320.css` + 3 首页 CSS), 正则提取 `font-size` / `line-height` / `font-weight` / `letter-spacing` / `font-family` / CSS 自定义属性
- **HTML class 提取**: 下载 about / blog / tiktok-video-generator 3 个代表性页面, 提取实际使用的 Tailwind 字号 class
- **交叉比对**: Pipeline A ⇔ Pipeline B ⇔ `demo/docs/style.md` 规范逐项对照

---

*报告生成: 2026-07-14 · 下次审计建议: Phase 1 完成后*
