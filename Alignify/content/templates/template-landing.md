# 落地页/首页模板

本文档定义首页（Landing）页面的结构，用于 `/`、`/zh` 等首页。

**参考**：app/page.tsx、app/zh/page.tsx、[section-consistency](../section/section-consistency.md)（内容型页面一致性）

---

## 〇、一致性规范

**落地页**：Hero、TrustedBy、ContentValue 等区块的文案长度与风格需在中英文首页之间保持一致。**内容型页面**（Tools、SEO、Marketing）：见 [section-consistency](../section/section-consistency.md)。

---

## 一、适用范围

| 路径 | 文件位置 | 说明 |
|------|----------|------|
| `/` | `app/page.tsx` | 英文首页 |
| `/zh` | `app/zh/page.tsx` | 中文首页 |

---

## 二、页面结构

首页由上至下包含：

1. **HeroSection**：主视觉区，H1、CTA、特色介绍（locale prop 控制中英文）
2. **TrustedBySection**：合作品牌/客户 Logo 展示
3. **ContentValueSection**：内容价值说明、分类导航（locale prop 控制中英文）

---

## 三、专用组件

| 组件 | 适用 | 说明 |
|------|------|------|
| HeroSection | 中英文首页 | 主视觉区，含 H1、描述、CTA 按钮；locale prop 控制语言 |
| TrustedBySection | 中英文 | Logo 展示，素材见下方五 |
| ContentValueSection | 中英文首页 | 内容价值、SEO/工具/洞察分类入口；locale prop 控制语言 |

---

## 四、Metadata 与 Schema

- 首页包含 WebSite、Organization Schema
- alternates 含 zh、en、x-default
- OpenGraph、Twitter 配置完整

---

## 五、TrustedBySection Logo 素材

将以下 logo 文件放置在 `public/logos/` 目录中：

| 文件名 | 描述 |
|--------|------|
| dubbing-ai.png | Dubbing AI 的 logo |
| collov-ai.png | Collov AI 的 logo |
| logo-3.png | 几何形状 logo |
| logo-4.png | 黑色圆形背景，白色 OIO 图案 |
| logo-5.png | 极简主义 logo |

**图片要求**：PNG（透明背景）或 SVG；建议宽度 150-200px；文件名需与 `TrustedBySection.tsx` 中配置一致。若文件不存在，该 logo 自动隐藏。
