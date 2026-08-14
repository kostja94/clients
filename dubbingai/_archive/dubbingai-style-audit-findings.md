# Dubbing AI — 样式不一致汇总

> **归档说明**：本文档已于 2026-06-22 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> **数据来源**：dubbingai.io 线上实测（2026-05-19，1440×900 桌面视口）+ DevTools Console CSS 抓取  
> **关联**：[dubbingai-brand-visual.md](../dubbingai-brand-visual.md)（规范方案）· [BRAND_GUIDELINES.md](../BRAND_GUIDELINES.md)（原始审计数据）

---

## 一、根本原因：无品牌设计系统

线上实测发现 dubbingai.io **没有 CSS 自定义属性体系**：

- `--primary` → 空值（无品牌色 Token）
- `--color-background` → 存在但仅来自 VitePress 默认主题，非品牌定义
- 颜色值以裸 hex 分散在各组件中，无统一引用

同时 **3–4 套字体并存**、**VitePress + Element Plus 各自携带独立样式**，缺乏全局约束。

---

## 二、H1 不一致（严重）

| 页面 | 文案 | 视觉字号 | 颜色处理 |
|------|------|---------|---------|
| `/` | Best Free Real-Time AI Voice Changer | ~72px | 纯黑实心 |
| `/voice-changer` | Free Real-Time AI Voice Changer | ~60px | 黑 + cyan 外描边 |
| `/soundboard` | Level Up Your Content with the Ultimate AI Soundboard | ~64px | 黑 + cyan 外描边 |
| `/sdk` | The Best Real-Time AI Voice Transformation SDK | ~56px | 黑 + cyan 外描边 |
| `/blog` | Blog | ~80px | 黑 + cyan 外描边 |
| `/community-sounds` | Meow Soundboard by Dubbing AI | ~64px | 黑 + cyan 外描边 |

**问题**：
- 字号范围 56–80px，差距 24px
- 首页是**唯一无 cyan 描边**的 H1
- 首页 Console 抓到 `<h1>` 是 "Voice Transformation Made Easy"（48px），视觉 H1 "Best Free..." 可能不是 `<h1>` 标签——**语义 H1 与视觉 H1 分离**

---

## 三、H2 不一致

| 页面 | 视觉字号 | 额外问题 |
|------|---------|---------|
| `/voice-changer` | ~36px | "Realtime" 与 H1 "Real-Time" 拼写不同 |
| `/soundboard` | ~56px | 含 `FREE` 单词 ALL-CAPS（全站唯一） |
| `/sdk` | ~40px | — |
| `/community-sounds` | ~40px | 与 H1 同样带 cyan 描边 |

**问题**：字号 36–56px 无规律；同站两种拼写；单词级 ALL-CAPS 仅 1 例。

---

## 四、字体体系混乱

| 位置 | 字体 |
|------|------|
| Logo | 自定义 italic 粗体 |
| H1（产品页） | 几何 sans（类似 PingFang / MiSans） |
| 首页 H1 | 同上家族但无描边 |
| 正文 | Inter + system fallback |
| Element Plus 组件 | Helvetica Neue / PingFang SC（**无 Inter**） |

---

## 五、按钮体系

5 种视觉变体 + 2 套渐变：

| 渐变体系 | 出现位置 | 颜色 |
|----------|---------|------|
| **品牌渐变** | 各页主 CTA pill | cyan `#22D3EE` → indigo `#6366F1` |
| **冲突渐变** | Sticky bottom bar | 橙 `#F97316` → 粉 `#EC4899` |

次级实心按钮颜色两套：indigo（首页）vs purple（/community-sounds）。

CTA 文案同义双写：`Download for Free` / `Download Dubbing for Free`。

---

## 六、颜色额外色

品牌色板外的颜色：

| 颜色 | 出现位置 | 是否品牌色 |
|------|---------|-----------|
| 紫 `#7C3AED` | /community-sounds 上传按钮、404 插画 | ❌ |
| 橙→粉渐变 | Sticky bar | ❌ |
| 蓝紫 `#5B5BFF` | 部分行内链接 | ❌（与 indigo `#6366F1` 并存） |

---

## 七、缩略词/拼写不一致

| 词 | 不同写法 |
|----|---------|
| Real-Time | `Real-Time` / `Realtime` |
| SFX | `Sfx` / `SFX` |
| TikTok | `Tiktok` / `TikTok` |
| 链接色 | `#5B5BFF` / cyan `#22D3EE` |

---

## 八、Nav 与 404

- `/community-sounds` 使用**完全独立**的导航栏，无品牌 Nav，无面包屑回首页。
- 404 页使用 **Vercel 默认模板**，无品牌 Nav / Footer / 颜色。
- `/pricing`、`/voice-changer/<slug>` 等不存在路径均落到 Vercel 404。

---

## 九、对得上：审计报告 vs Console 数据

| 维度 | 审计报告（视觉实测） | Console CSS 抓取 | 一致？ |
|------|-------------------|-----------------|--------|
| 字体 | 正文 Inter | `font-family: Inter, ...` ✅ | ✅ |
| 品牌 Token | 无 | `--primary` 空值 ✅ | ✅ |
| 框架 | VitePress（`--vt-c-*`） | 同文件含 `--vt-c-white` 等 ✅ | ✅ |
| Element Plus | `--el-*` Token | 同文件含 `--el-font-size-*` 等 ✅ | ✅ |
| 首页 H1 不一致 | 视觉 H1 ~72px 实心黑 | Console `<h1>` 48px "Voice Transformation Made Easy" | ❗**视觉 H1 与语义 H1 不同** |

---

*基于 2026-05-19 线上实测 + Console CSS 抓取交叉验证*
