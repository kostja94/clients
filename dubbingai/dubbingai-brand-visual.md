# Dubbing AI — Brand Guidelines

> **数据来源**：dubbingai.io 线上实测（2026-05-19，1440×900 桌面视口）  
> **方法**：视觉实测 + DevTools Console CSS 抓取 + 跨页对比  
> **替代**：本文档基于线上真实数据，覆盖此前基于内部文档的推测版本  
> **关联**：[dubbingai.md](./dubbingai.md)（产品上下文）· [现状审计报告（归档）](./_archive/dubbingai-style-audit-findings.md)（2026-05-19 线上 CSS 实测）

---

## 0. 技术栈现实

| 实际 | 说明 |
|------|------|
| **框架** | VitePress（`--vt-c-*` Token）+ Element Plus（`--el-*` Token） |
| **CSS** | 单文件 `/assets/app-C13Kl8Fv.css`，无品牌级 CSS 自定义属性 |
| **品牌色 Token** | **不存在**——`--primary` 返回空值，全站无统一品牌色变量 |
| **字体体系** | **3–4 套字体并存**，无统一 `font-family` 声明体系 |

---

## 1. 字体（Font Families）— 当前现状

线上实测确认 **至少 4 套字体并存**，这是品牌不一致的根本原因：

| 用途 | 实测字体 | 问题 |
|------|---------|------|
| **Logo "Dubbing AI"** | 深蓝 italic 粗体自定义字体 | 不复用于任何其他位置 |
| **H1**（/voice-changer、/soundboard、/sdk、/blog、/community-sounds） | 圆润几何 sans，黑实心 + cyan 1px `-webkit-text-stroke` | 与正文非同一字体族 |
| **首页 H1** | 同上家族但**无描边**、字重略轻 | 与产品页 H1 不同视觉处理 |
| **正文/按钮/Nav** | `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, …` | ✅ 正文层一致 |
| **Element Plus 组件** | `"Helvetica Neue", Helvetica, "PingFang SC", …`（**无 Inter**） | Element Plus 组件与正文字体不同 |

### 1.1 推荐统一方案

```
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

- **全局** `body` 设置上述 font-family。
- **Element Plus** 覆盖 `--el-font-family` 为同一字体栈。
- **Logo** 保留自定义字体（仅用于 Logo 组件）。
- **H1 display 字体**：如保留当前几何 sans 风格，需显式声明 `font-family`，不作为"浏览器默认 sans-serif"依赖系统回退。

---

## 2. H1 — 当前现状与规范

### 2.1 实测数据

| 页面 | H1 文案 | 视觉字号 | 字重 | 颜色处理 | 大小写 |
|------|---------|---------|------|---------|--------|
| `/` | Best Free Real-Time AI Voice Changer | ~72px | 700 | 纯黑实心 | Title Case |
| `/voice-changer` | Free Real-Time AI Voice Changer | ~60px | 800 | 黑 + cyan 1px 外描边 | Title Case |
| `/soundboard` | Level Up Your Content with the Ultimate AI Soundboard | ~64px | 800 | 黑 + cyan 描边 | Title Case（"with" 小写） |
| `/sdk` | The Best Real-Time AI Voice Transformation SDK | ~56px | 700 | 黑 + cyan 描边 | Title Case |
| `/blog` | Blog | ~80px | 800 | 黑 + cyan 描边 | 单单词 |
| `/community-sounds` | Meow Soundboard by Dubbing AI | ~64px | 800 | 黑 + cyan 描边 | Title Case（"by" 小写） |

### 2.2 问题

1. **字号范围 56–80px**（差异 24px，无规律）。
2. **首页是唯一无 cyan 描边的 H1**——「实心黑」vs「黑底+cyan 描边」两套视觉并存。
3. **Title Case 小词处理不统一**：`with` / `by` / `for` / `and` 在各页的大小写不一致。
4. **首页可能存在双重 H1**：Console 抓取到的 `<h1>` 文案为 "Voice Transformation Made Easy"（48px CSS），但视觉上最突出的 H1 是 "Best Free Real-Time AI Voice Changer"（~72px）。这说明**视觉 H1 可能不是 `<h1>` 标签**——需确认是否为 `<div>` / `<span>` 伪装。
5. **`/blog` H1 仅一个单词 "Blog"**，字号却最大（~80px），与产品页不成比例。

### 2.3 规范

| 规则 | 值 |
|------|-----|
| **字号** | **统一 64px**（桌面），`text-5xl md:text-6xl` |
| **字重** | **统一 800**（`font-extrabold`） |
| **颜色** | **统一 黑 + cyan 1px 外描边**（与产品页一致；首页废弃实心黑） |
| **大小写** | Title Case，小词（a / an / the / and / or / for / nor / but / yet / so / at / by / in / of / on / to / up / with / via）**全小写** |
| **每页限制** | **1 个 `<h1>` 标签**，不允许 div/span 伪装，不允许多个 H1 |

```
/* CSS 参考 */
h1 {
  font-size: 4rem;          /* 64px */
  font-weight: 800;
  line-height: 1.1;
  -webkit-text-stroke: 1px #22D3EE;
  color: #18181B;
}
```

---

## 3. H2 — 当前现状与规范

### 3.1 实测数据

| 页面 | 视觉字号 | 字重 | 问题 |
|------|---------|------|------|
| `/voice-changer` | ~36px | 800 | "Realtime" 与 H1 "Real-Time" 拼写不同 |
| `/soundboard` | ~56px | 800 | 含 `FREE` 单词 ALL-CAPS（全站唯一） |
| `/sdk` | ~40px | 700 | — |
| `/community-sounds` | ~40px | 800 | 与 H1 一样带 cyan 描边（H2 不应描边） |

### 3.2 问题

1. **字号范围 36–56px**（差异 20px）。
2. **"Real-Time" vs "Realtime"** 同站两种拼写。
3. **`FREE` ALL-CAPS** 作为单词级强调出现 1 次，无规则。
4. **部分 H2 带 cyan 描边**（/community-sounds）——描边应仅限 H1。

### 3.3 规范

| 规则 | 值 |
|------|-----|
| **字号** | **统一 40px**（桌面），`text-3xl md:text-4xl` |
| **字重** | **统一 800**（`font-extrabold`） |
| **颜色** | 纯黑（`#18181B`），**无描边** |
| **大小写** | Title Case（小词规则同 H1） |
| **禁止** | 单词级 ALL-CAPS 嵌在 Title Case 中 |

```
/* CSS 参考 */
h2 {
  font-size: 2.5rem;        /* 40px */
  font-weight: 800;
  color: #18181B;
}
```

---

## 4. 正文体系 — 当前现状与规范

### 4.1 实测数据

| 元素 | 字号 | 颜色 | 字重 | 跨页一致性 |
|------|------|------|------|-----------|
| Lead 段 | 18px | `#52525B` | 400 | ✅ 一致 |
| Body | 16px | `#52525B` | 400 | ✅ 一致 |
| 行内链接 | 16px | `#5B5BFF` **或** cyan | 500 | ❌ **两种链接色并存** |

### 4.2 问题

行内链接色混用：部分页面用蓝紫 `#5B5BFF`，部分用主色 cyan `#22D3EE`。

### 4.3 规范

| 元素 | 字号 | 颜色 | 字重 |
|------|------|------|------|
| Lead | 18px（`text-lg`） | `#52525B` | 400 |
| Body | 16px（`text-base`） | `#52525B` | 400 |
| 行内链接 | 继承 body 字号 | **统一 `#5B5BFF`** | 500 |
| Small / Caption | 14px（`text-sm`） | `#52525B` | 400 |

---

## 5. 缩略词与专有名词写法

### 5.1 实测不一致

| 词 | 出现的写法 | 推荐 |
|----|----------|------|
| SDK | ✅ 一致 `SDK` | `SDK` |
| SFX | `Sfx` / `SFX` | `SFX` |
| TikTok | `Tiktok` / `TikTok` | `TikTok` |
| Real-Time | `Real-Time`（H1）/ `Realtime`（H2） | `Real-Time` |

### 5.2 规范

| 规则 | 示例 |
|------|------|
| 全大写缩写保持全大写 | `SDK`、`SFX`、`API`、`AI`、`CPU` |
| 品牌/产品名遵循官方写法 | `TikTok`（非 `Tiktok`）、`Discord`（非 `discord`）、`VRchat`（非 `VRChat`） |
| "Real-Time" 全站统一带连字符 | `Real-Time`（非 `Realtime`、`Real Time`、`real-time`（正文中除外）） |

---

## 6. 按钮 — 当前现状与规范

### 6.1 实测数据

| 类型 | 出现位置 | 形状 | 字号 | 颜色 |
|------|---------|------|------|------|
| 主 CTA pill | 各营销页 | `rounded-full` | 18px / 600 | cyan→indigo 渐变，白字 |
| Sticky CTA pill | 全站底部栏 | `rounded-full` | 16px / 700 | **橙→粉渐变**，白字 + ✨ |
| 次级实心 indigo | `/`（Home） | `rounded-md` | 16px / 500 | 纯靛蓝实心 |
| 次级实心 purple | `/community-sounds` | `rounded-md` | 16px / 500 | 纯紫实心 |
| 链接/边框 | Nav | 边框 | 14px / 500 | 边框 + 文字色 |

**问题**：
- 5 种视觉变体。
- **2 套互不相关的渐变**（cyan→indigo 主品牌 vs orange→pink sticky）。
- 次级实心按钮两种颜色（indigo vs purple），选择无规律。
- CTA 文案 "Download for Free" / "Download Dubbing for Free" **同义双写**。

### 6.2 规范

| 级别 | 样式 | 使用场景 |
|------|------|----------|
| **Primary CTA** | `rounded-full`、cyan→indigo 渐变、白字 18px/600 | Hero、各页底部主 CTA |
| **Secondary** | `rounded-md`、纯 `#6366F1` 实心、白字 16px/500 | 次级操作 |
| **Outline** | `rounded-md`、边框 `#E4E4E7`、文字 `#18181B` 14px/500 | 第三级操作（Log in、Learn more） |
| **Sticky CTA** | `rounded-full`、**统一用 cyan→indigo 渐变**（废弃橙→粉） | 全站底部固定栏 |

**规则**：
- 每 fold 最多 1 Primary + 1 Secondary。
- CTA 文案统一为 `Download for Free`（废弃 `Download Dubbing for Free`）。
- 按钮内文案 **Title Case**（与当前一致）。
- 废弃紫色实心按钮——统一用 indigo（`#6366F1`）。

```
/* CSS 参考 */
.btn-primary {
  border-radius: 9999px;
  background: linear-gradient(135deg, #22D3EE, #6366F1);
  color: #FFFFFF;
  font-size: 18px;
  font-weight: 600;
}
.btn-secondary {
  border-radius: 0.375rem;
  background: #6366F1;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 500;
}
```

---

## 7. 颜色系统 — 当前现状与规范

### 7.1 实测现状

线上**无 CSS 自定义属性体系**（`--primary` 返回空值）。实际使用的颜色散落在各处：

| 角色 | 当前实际颜色 | 出现位置 | 问题 |
|------|------------|---------|------|
| 主 cyan | `#22D3EE` | 渐变左、H1 描边 | ✅ |
| 主 indigo | `#5B5BFF` ~ `#6366F1` | 渐变右、实心按钮、部分链接 | 两种近似值并存 |
| 链接蓝紫 | `#5B5BFF` | 部分行内链接 | 与 cyan 链接色矛盾 |
| 紫 | `#7C3AED` | /community-sounds 按钮、404 插画 | **额外色**，无体系 |
| 浅蓝白底 | `#F0F5FF` ~ `#E7F4FF` | 营销页大区背景 | ✅ |
| 正文灰 | `#52525B` | body 文本 | ✅ |
| 橙→粉渐变 | `#F97316` → `#EC4899` | sticky bar | **第二套渐变**，与品牌渐变矛盾 |
| 黑 | `#18181B` | H1 填充色 | ✅ |

### 7.2 推荐 CSS Token 体系

```css
:root {
  /* Core */
  --color-background: #FFFFFF;
  --color-foreground: #18181B;
  --color-muted: #F4F4F5;
  --color-muted-foreground: #52525B;
  --color-border: #E4E4E7;

  /* Brand */
  --color-primary: #6366F1;         /* indigo - 统一主色 */
  --color-primary-foreground: #FFFFFF;
  --color-accent: #22D3EE;          /* cyan - 点缀色 */
  --color-accent-foreground: #18181B;

  /* Gradient */
  --gradient-brand: linear-gradient(135deg, #22D3EE, #6366F1);

  /* Hero surface */
  --color-hero-bg: #F0F5FF;

  /* Destructive */
  --color-destructive: #EF4444;
}
```

### 7.3 规则

- **主色统一为 indigo `#6366F1`**（替代 `#5B5BFF` / `#7C3AED` 混用）。
- **紫色 `#7C3AED` 废弃**（/community-sounds 按钮改用 indigo）。
- **橙→粉渐变废弃**（sticky bar 改用品牌 cyan→indigo 渐变）。
- **链接色统一为 indigo `#6366F1`**（废弃 cyan 链接色）。
- H1 外描边保留 cyan `#22D3EE`（仅 H1 使用此色）。
- 所有颜色通过 CSS 变量引用，**禁止**裸 hex 值出现在模板中。

---

## 8. Nav — 当前现状与规范

### 8.1 实测问题

| 区域 | 现状 | 问题 |
|------|------|------|
| 主营销页 Nav | Voice Changer / Soundboard ▾ / SDK / Useful Tools ▾ / Resources ▾ + EN ▾ | ✅ 五页一致 |
| /community-sounds Nav | Sounds · Voices + Memes · Music · Games · Anime · Sfx + Upload Sound + Log in | ❌ **完全不同的 Nav**，无面包屑回 `/` |
| 404 页 | Vercel 默认模板 | ❌ 无品牌 Nav、无 Footer |

### 8.2 规范

- `/community-sounds` **必须共享主营销页 Nav**（或至少包含 Logo + 回到首页的链接）。
- 404 页**替换为品牌自定义页面**（含 Nav + Footer + 品牌色），不再使用 Vercel 默认模板。

---

## 9. 大小写规范总表

| 元素 | 规则 | 示例 |
|------|------|------|
| **H1 / H2 / H3** | Title Case，小词全小写 | `Best Free Real-Time AI Voice Changer` |
| **按钮 CTA** | Title Case | `Download for Free`（非 `Download For Free`） |
| **Nav 标签** | Title Case | `Voice Changer`、`Useful Tools` |
| **正文** | 正常句子大小写 | `Change your voice in real time.` |
| **产品名** | `Dubbing AI` | 始终 "D" 大写 + "AI" 大写 |
| **URL 路径** | 全小写 kebab-case | `/discord-voice-changer` |
| **缩写** | 全大写 | `SDK`、`SFX`、`API`、`AI` |
| **品牌/平台名** | 官方写法 | `TikTok`、`Discord`、`VRchat` |

---

## 10. 组件体系 — 当前与目标

### 10.1 当前问题

- 无共享组件体系，每页独立构建。
- `/community-sounds` 使用完全独立的 Nav、按钮颜色、布局。
- 404 使用 Vercel 默认模板。
- Sticky CTA bar 使用独立的渐变方案。

### 10.2 目标组件

| 组件 | 用途 | 关键约束 |
|------|------|---------|
| `BrandNav` | 全站导航 | 所有页面（含 /community-sounds）共享 |
| `BrandFooter` | 全站页脚 | 所有页面共享 |
| `HeroSection` | 页面 Hero | H1 64px/800、cyan 描边、可选 brand-wash 背景 |
| `CTAPill` | 主 CTA 按钮 | cyan→indigo 渐变、`rounded-full` |
| `StickyBar` | 底部固定栏 | 品牌渐变（非橙→粉） |
| `NotFoundPage` | 404 | 品牌 Nav + Footer + 插画 |

---

## 11. 实施优先级

| 优先级 | 行动 | 当前问题 | 影响范围 |
|--------|------|---------|---------|
| **P0** | 创建 CSS Token 体系（`--color-*`） | 全站无品牌色变量 | 全站 |
| **P0** | 统一 H1 规范（64px/800/cyan 描边） | 56–80px 浮动，首页无描边 | 6+ 页面 |
| **P0** | 统一 H2 规范（40px/800/无描边） | 36–56px 浮动 | 5+ 页面 |
| **P0** | 统一字体栈（Inter + Element Plus 覆盖） | 3–4 套字体并存 | 全站 |
| **P0** | 统一按钮体系（3 级，1 套渐变） | 5 种变体，2 套渐变 | 全站 |
| **P1** | 统一链接色（indigo #6366F1） | 两种链接色并存 | 全站 |
| **P1** | 统一缩略词写法（SFX、TikTok、Real-Time） | Sfx/Tiktok/Realtime | 全站 |
| **P1** | /community-sounds 共享主 Nav | 独立 Nav | 1 页面 |
| **P1** | Sticky bar 改用品牌渐变（废弃橙→粉） | 第二套渐变 | 全站 |
| **P2** | 替换 404 为品牌页面 | Vercel 默认模板 | 1 页面 |
| **P2** | 废弃紫色按钮，统一 indigo | 紫色额外色 | /community-sounds |

---

## 12. 验证命令（部署后）

在部署品牌规范后，在各页面 Console 运行以下脚本验证一致性：

```javascript
// 检查 H1 字号一致性
const h1s = document.querySelectorAll('h1');
h1s.forEach(h => console.log(getComputedStyle(h).fontSize, h.innerText?.slice(0,60)));
// 期望：全部输出 64px（±2px）

// 检查 --color-primary 是否存在
console.log(getComputedStyle(document.documentElement).getPropertyValue('--color-primary'));
// 期望：#6366F1 或等效值，非空

// 检查字体
console.log(getComputedStyle(document.body).fontFamily);
// 期望：含 "Inter"

// 检查 Sticky bar 渐变
const sticky = document.querySelector('[class*="sticky"], [class*="fixed-bottom"]');
if (sticky) console.log(getComputedStyle(sticky).background);
// 期望：含 cyan/indigo，非 orange/pink
```

---

*Last updated: 2026-05-19 · based exclusively on live dubbingai.io audit + DevTools Console extraction*
