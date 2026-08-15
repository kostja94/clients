# 图片尺寸参考

> **本文档职责**：汇总 Oginify 涉及的所有图片尺寸知识——哪些场景用 1200×630、哪些容易混淆、平台具体要求、一图多用的隐性价值，以及 **1.91:1 限定** 的数字与线下印刷规格。  
> **引用**：[index.md](./index.md) 场景总览 | [by-page-type.md](./by-page-type.md) 页面类型 | [by-site-type.md](./by-site-type.md) 网站类型 | [by-style.md](./by-style.md) 风格 | [主文档](../oginify.md) 概览

---

## 为什么 1200×630

Oginify 默认输出 1200×630，因为这个尺寸是互联网社交预览的事实标准。一个数字背后是一整套兼容逻辑：

- **1.91:1 宽高比**：源自 Facebook 2010 年的 Open Graph 协议，之后被几乎所有平台采纳
- **2× Retina 安全**：社媒卡片通常在 600px 宽左右渲染，1200px 源图确保高清屏不糊
- **跨平台通用**：Facebook、LinkedIn、X、Slack、Discord、WhatsApp、iMessage、Pinterest——一张图全兼容

---

## 图片类型 × 尺寸对照

### 一、1200×630 精确使用（或 1200×628，完全互通）

#### 社交预览类（OG 图）

| 图片类型 | 精确尺寸 | 平台 | 英语名称 |
|----------|---------|------|----------|
| Open Graph 预览图 | **1200 × 630** | Facebook、LinkedIn、Slack、Discord、WhatsApp、iMessage、Pinterest | OG Image / Social Share Preview |
| Twitter/X 大图卡片 | **1200 × 628** | X / Twitter | Twitter Summary Large Image Card |
| 博客 Featured Image | **1200 × 630** | WordPress、Ghost、Medium | Blog Featured Image / Post Thumbnail |

> **💡 Featured Image = OG Image**：博客 CMS 自动将 Featured Image 设为 `og:image`。Oginify 生成的图直接上传为 Featured Image，一张图同时服务文章阅读和社交传播。

#### 广告投放类（非 OG 图）

**横版 1.91:1 可直接复用或完全匹配：**

| 图片类型 | 横版尺寸 | 平台 | 英语名称 |
|----------|---------|------|----------|
| Google 自适应展示广告（横版） | **1200 × 628** | Google Ads | Responsive Display Ad — Landscape |
| Meta 即阅文广告 | **1200 × 628** | Facebook Instant Articles | Instant Articles Ad |
| Microsoft 受众网络广告（横版） | **1200 × 628** | Microsoft Audience Network | Microsoft Audience Ad — Landscape |
| Amazon 赞助展示广告 | **1200 × 628** | Amazon | Amazon Sponsored Display |
| 程序化展示广告（通用横版） | **1200 × 628** | 通用程序化 | Programmatic Display — Landscape |
| LinkedIn 信息流广告（横版） | **1200 × 628** | LinkedIn | LinkedIn Feed Ad — Landscape |

**横版可用，但平台现以方形/竖版为主推：**

| 图片类型 | 横版可用 | 平台主推 | 平台 | 英语名称 |
|----------|---------|---------|------|----------|
| Meta 信息流单图广告 | **1200 × 628** | **1080 × 1350**（4:5）或 **1080 × 1080**（1:1） | Facebook / Instagram | Feed Image Ad |
| Meta Collection 广告封面 | **1200 × 628** | **1080 × 1080**（1:1） | Facebook / Instagram | Collection Ad Cover |

> **Meta 广告说明（2026）**：上表横版 1200×628 均可上传，但 Feed / Collection 等 placement 现多以方形或竖版获得更大 feed 占比。Oginify 1200×630 适合「OG + Google 横版广告 + 部分 Meta 横版位」的一图多用；若专门投 Meta Feed 轮播或 Marketplace，需另出 1080×1080 方形素材（见下文「容易混淆」）。

> **628 vs 630**：1200 ÷ 628 = 精确 1.91:1（Google / Meta / Microsoft 统一标准）。1200 ÷ 630 ≈ 1.905，差 2px。所有平台两者互通，实际可以互换使用。Oginify 用 630 是因为 OG 协议原始推荐值，向下兼容。

### 二、接近但不同

| 图片类型 | 实际尺寸 | 与 1200×630 的差异 | 英语名称 |
|----------|---------|-------------------|----------|
| LinkedIn 文章封面 | **1200 × 644** | 高 14px，1.86:1；1200×630 可勉强复用，上下轻微裁剪 | LinkedIn Article Cover |
| Google Discover 大图 | **≥1200 宽，16:9 优先**（1200×675） | 比 630 高 45px；不是 1.91:1 | Google Discover Large Image |

### 三、容易混淆——不是 1200×630

| 图片类型 | 实际尺寸 | 为什么容易搞混 | 英语名称 |
|----------|---------|---------------|----------|
| Mailchimp 邮件头图 | **600–660 × 200–400** | 社媒分享 Newsletter 时弹出的是 1200×630 OG 图，但邮件内部的头图是宽扁横幅 | Email Header Banner |
| Substack 邮件头图 | **1100 × 220** | 同上——分享时的 OG 图是 1200×630，邮件内头图不是 | Substack Email Banner |
| 播客单集封面 | **3000 × 3000**（Apple）、**1:1**（Spotify） | 分享播客链接时的 OG 预览是 1200×630，但单集封面本身是正方形 | Podcast Episode Artwork |
| Google Display 标准横幅 | **300×250、728×90、160×600** 等 | 完全不同尺寸体系，IAB 标准 | Display Banner Ads |
| YouTube 缩略图 | **1280 × 720** | 16:9，不是 1.91:1 | YouTube Thumbnail |
| Meta 轮播广告 | **1080 × 1080** / 卡 | Feed 轮播主推方形，OG 横图需裁切或留白 | Carousel Ad |
| Meta Marketplace 广告 | **1080 × 1080** 或 **1200 × 1200** | Marketplace 主推方形，非 1.91:1 | Marketplace Ad |

---

## 1.91:1 限定尺寸清单

本节只列**必须（或规范上要求）保持 1.91:1 宽高比**的物料。  
印刷业**没有**像 A4、名片那样的 1.91:1 标准纸型——线下要印只能**自定裁切**，或从 Oginify 导出后按下列像素/毫米换算。

### 判定规则

| 类型 | 精确 1.91:1（广告/部分平台） | OG 惯例（Facebook 系） | 是否互通 |
|------|------------------------------|------------------------|----------|
| 公式 | 宽 ÷ 高 = **1.91**（或高 = 宽 ÷ 1.91） | 宽 ÷ 高 ≈ **1.905**（1200÷630） | 2px 高度差，可互换 |
| 1200 宽时的高度 | **628 px** | **630 px** | ✓ |
| 600 宽时的高度 | **314 px** | **315 px** | ✓ |

**不属于 1.91:1 限定**（即使常被误用）：16:9（1.78）、2:1、A 系列（≈1.41）、名片（1.75:1）、明信片（1.5:1）、方形（1:1）——见上文「接近但不同」「容易混淆」。

### 数字渠道——须 1.91:1

| 类别 | 推荐像素 | 最小像素（仍保持 ≈1.91:1） | 渠道 |
|------|---------|---------------------------|------|
| **OG / 社媒链接预览** | 1200 × **630** | 600 × **315** | Facebook、LinkedIn、Slack、Discord、WhatsApp、iMessage、Pinterest |
| **X 大图卡片** | 1200 × **628** | 300 × **157** | X / Twitter `summary_large_image` |
| **LinkedIn 链接预览** | 1200 × **627** | 宽 ≥1200、比例 ≈1.91:1 | LinkedIn Post / 链接卡片 |
| **博客 Featured Image** | 1200 × **630** | 600 × **315** | WordPress、Ghost、Medium（并写入 `og:image`） |
| **Google 自适应展示广告（横版）** | 1200 × **628** | 600 × **314** | Google Ads Responsive Display |
| **Meta 横版广告位** | 1200 × **628** | 600 × **314** | Feed 横版、Instant Articles、Collection 横版、Audience Network 横版 |
| **Microsoft 受众网络（横版）** | 1200 × **628** | — | Microsoft Advertising |
| **Amazon 赞助展示（横版）** | 1200 × **628** | — | Amazon Sponsored Display |
| **程序化/IAB 横版展示** | 1200 × **628** | 600 × **314** | 通用 programmatic landscape |

> **排除**：Google IAB 固定横幅（300×250 等）、Meta 轮播/Marketplace 方形、YouTube 1280×720、Google Discover 16:9、Twitter Card Generator 专用 1200×675——均**不是** 1.91:1 限定。

### 线下印刷——须 1.91:1（自定裁切，无标准纸型）

印刷必须保持 **宽 ÷ 高 = 1.91**；下列为常用成品尺寸与对应像素（**300 DPI** 近距阅读；更大尺寸请同比放大像素，勿只拉伸低分辨率 OG 原图）。

| 成品宽 × 高 | 英寸 | 毫米 | 300 DPI 像素（精确 1.91:1） | Oginify 导出可直用 | 典型用途 |
|-------------|------|------|---------------------------|-------------------|----------|
| 小横条 | 4″ × 2.09″ | 101.6 × 53.0 | **1200 × 628** | **1200 × 630** | 贴纸、标签、QR 桌牌顶图、包装腰封 |
| 中横条 | 6″ × 3.14″ | 152.4 × 79.8 | **1800 × 942** | **1800 × 945** | 活动手卡、插入页窄横幅 |
| 大横条 | 8″ × 4.19″ | 203.2 × 106.4 | **2400 × 1257** | **2400 × 1260** | 传单插页、货架条、展会扫码条 |
| 特大横条 | 10″ × 5.24″ | 254 × 133.0 | **3000 × 1571** | **3000 × 1575** | 小灯箱片、背板横条 |
| 横幅局部 | 19.1″ × 10″ | 485 × 254 | **5730 × 3000** | 同左 | 易拉宝/横幅中的横图区（整幅易拉宝为竖版，仅**局部**可限定 1.91:1） |

> **精确 vs Oginify 列**：左列为严格 1.91:1（÷1.91）；右列为 Oginify 默认 1200×630 同比放大，高度多 2‰ 左右，印刷肉眼无差。

**150 DPI**（稍远观看，像素减半）：如 4″×2.1″ → **600 × 315 px**（与 Facebook 最小 OG 一致）。

**印刷注意**：

- 色彩：**RGB → CMYK**，饱和色会偏暗，重要物料需打样。
- 出血：裁切边加 **3 mm**（或 0.125″）；文字/Logo 离裁切线 ≥ **5 mm**。
- 源图：Oginify 默认 **1200×630 px** 仅够印约 **4″×2.1″**；更大成品需矢量重制或高分辨率重新导出。

### 线下常见物料——是否 1.91:1 限定

| 物料 | 是否 1.91:1 限定 | 说明 |
|------|------------------|------|
| QR 桌牌 / 台卡（仅顶图横条） | **是**（自定） | 与 OG 同图，比例须 1.91:1 |
| 定制贴纸 / 包装腰封 | **是**（自定） | 按上表英寸或毫米下单 |
| 活动手卡 / 传单插页横条 | **是**（自定） | 非整页 A4/A5，只是其中的横条模块 |
| A4 / A5 / Letter 整页传单 | **否** | √2 或 Letter 比例，需重排版 |
| 美国名片（3.5″×2″） | **否** | 1.75:1 |
| 明信片（6″×4″ 横版） | **否** | 1.5:1 |
| DL 传单（210×99 mm） | **否** | ≈2.12:1，更扁 |
| 2:1 横条（8″×4″） | **否** | 2:1，比 1.91:1 宽约 5%，不能算限定 |
| 易拉宝 / 海报整幅 | **否** | 竖版为主；仅局部横条可限定 1.91:1 |
| 16:9 展架屏 / PPT | **否** | 1.78:1，用 1200×675 而非 630 |

---

## 平台 OG 图具体限制

| 平台 | 推荐尺寸 | 最小尺寸 | 最大文件 | 格式 |
|------|---------|---------|---------|------|
| **Facebook** | 1200 × 630 | 600 × 315 | 8 MB | JPG、PNG、WebP |
| **X / Twitter** | 1200 × 628 | 300 × 157 | 5 MB | JPG、PNG、WebP、GIF |
| **LinkedIn** | 1200 × 627 | — | 5 MB | JPG、PNG |
| **Slack** | 1200 × 630 | — | 1 MB | JPG、PNG |
| **Discord** | 1200 × 630 | — | 8 MB | JPG、PNG |
| **WhatsApp** | 1200 × 630 | 宽 ≥300px | **600 KB**（官方） | JPG、PNG |
| **iMessage** | 1200 × 630 | — | 无硬限制 | JPG、PNG |
| **Pinterest** | 1200 × 630 | — | 10 MB | JPG、PNG |

> **WhatsApp 压缩建议**：官方 Link Preview 上限 **600 KB**，但实践中超过 **300 KB** 仍可能静默不显示。若图要同时在 WhatsApp 上稳定出现，压缩目标建议 **≤300 KB**（与博客 Featured Image 的 100–200 KB 建议一致）。

---

## 博客 Featured Image 尺寸补充

| 布局 | 推荐尺寸 | 宽高比 |
|------|---------|--------|
| **通用标准**（绝大多数主题） | **1200 × 630** | 1.91:1 |
| **16:9 宽屏主题** | 1200 × 675 | 16:9 |
| **全宽 Hero 布局** | 1920 × 1080 | 16:9 |
| **方形布局** | 1200 × 1200 | 1:1 |

**文件建议**：JPEG 或 WebP，≤ 100–200KB。CMS 自动将 Featured Image 设为 `og:image`——一张图两个用途。

---

## 对 Oginify 的意义

一张 Oginify 生成的 1200×630 图，实际用途：

```
一张图
  ├── 【完全兼容】社交预览（Facebook / LinkedIn / X / Slack / Discord 等链接展开图）
  ├── 【完全兼容】博客头图（CMS Featured Image → og:image）
  ├── 【完全兼容】Google 广告横版素材（Responsive Display Ad）
  ├── 【完全兼容】Microsoft / Amazon 横版展示广告
  ├── 【可用，非最优】Meta 横版广告位（Feed 横版、Instant Articles、Collection 横版）
  └── 【需另出图】Meta 轮播 / Marketplace（1080×1080 方形为主推）
```

X / Twitter 专用 **1200×675** 见 [Twitter Card Generator](../oginify-features.md#7-twitter-card-generator) 与 [by-page-type](./by-page-type.md#图片尺寸参考)。

**用户生成一次，至少覆盖 OG 预览、博客头图、Google 横版广告等 4+ 个高价值场景**；加上 Microsoft / Amazon 与部分 Meta 横版位，横版 1.91:1 的复用面仍然很宽。这个「一图多用」是 Oginify 产品价值里被低估的部分——不只是 OG 图生成器，也是通用的 1.91:1 营销素材起点（Meta 方形广告需另出规格）。

---

## 必填 Meta 标签（参考）

完整的 OG 图部署需要以下 HTML meta 标签：

```html
<!-- Open Graph -->
<meta property="og:title" content="页面标题" />
<meta property="og:description" content="页面描述，建议 150–160 字符" />
<meta property="og:image" content="https://你的域名.com/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="OG 图的替代文字" />
<meta property="og:url" content="https://你的域名.com/页面路径" />
<meta property="og:type" content="website" />

<!-- Twitter/X -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="页面标题" />
<meta name="twitter:description" content="页面描述" />
<meta name="twitter:image" content="https://你的域名.com/og-image.png" />
```

**常见错误**：使用相对路径（必须用 `https://` 绝对 URL）、缺少 `og:image:width/height`（平台要额外下载检测）、图片被 robots.txt 拦截（必须公开可访问）。

---

## 调试工具

| 平台 | 工具 |
|------|------|
| Facebook | [Sharing Debugger](https://developers.facebook.com/tools/debug) |
| X / Twitter | 官方 Card Validator 已于 2022 年停用；可用 [Oginify Validator](https://oginify.com/open-graph-validator) 预览 X 卡片，或贴 URL 到 X 草稿框测试 |
| LinkedIn | [Post Inspector](https://www.linkedin.com/post-inspector/) |
| Discord | 直接贴 URL 到聊天框 |
| Slack / WhatsApp / iMessage | 直接贴 URL；更新 OG 图后可在 URL 后加 `?v=2` 绕过缓存 |

---

*Last updated: 2026-05-31. 新平台尺寸变化、新发现图片类型或线下 1.91:1 印刷规格时同步更新。*
