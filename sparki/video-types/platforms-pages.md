# Sparki Platforms · 页面结构

> 发布平台/渠道 SEO 页面。聚合页与平台详情页的 IA、模块与 URL 规则。分类编号见 [video-types-taxonomy.md](./video-types-taxonomy.md) 维度 4(P01–P15)。

---

## 一、已上线站点

| 类型 | 正式 URL | 状态 |
|------|----------|------|
| 聚合页 | <https://sparki.io/platforms> | ✅ 已上线 |
| 平台详情页 | `https://sparki.io/platforms/{slug}` | ⏳ **0/15 已上线**（2026-08-26 探测均为 404） |

**URL 规则**：`https://sparki.io/platforms/{slug}`

---

## 二、聚合页结构

**URL**：[sparki.io/platforms](https://sparki.io/platforms)  
**H1**：Every Platform, One Edit  
**定位**：一次剪辑 → 按各平台画幅、节奏与安全区导出多版本成品

页面自上而下模块：

| 模块 | 说明 |
|------|------|
| Hero | 粘贴 X / Instagram / TikTok / Facebook 链接，或上传文件 → Sparki 按目标平台 reframe / re-pace / caption |
| **Platforms Sparki Exports For** | 15 张平台卡，分 3 组 + tab 筛选（All / Short-Form / Long-Form / Commerce） |
| Why Export Per Platform | 3 卡：Native Framing · Pacing Per Placement · One Edit Every Ratio |
| How Multi-Platform Export Works | 3 步：Upload → Pick Platforms → Export Every Master |
| FAQ | 6 条（支持哪些链接导入、是否仅裁剪、多画幅导出、各平台时长、自动字幕、能否直接发布） |
| 底部 CTA | Cut Once, Publish Everywhere → Try For Free |

### 链接导入 vs 文件上传

| 导入方式 | 支持平台 |
|---------|---------|
| **Paste link** | X (Twitter) · Instagram · TikTok · Facebook |
| **Upload file** | 其余全部平台及任意本地素材 |

> 其他来源需先下载视频再上传；导出侧支持聚合页列出的全部 15 个平台。

### Tab 筛选 IA

| Tab | 分组 | 平台数 |
|-----|------|--------|
| All Platforms | 全部 | 15 |
| Short-Form Video | 竖屏短视频 | 6 |
| Long-Form & Landscape | 横屏/长视频 | 4 |
| Commerce & Marketplaces | 电商/广告/店铺 | 5 |

---

## 三、平台卡片清单（聚合页 · 15 个）

### 4-A · Short-Form Video（P01–P06）

竖屏 feed，节奏决定留存。Sparki 去 dead air、烧录字幕、导出 9:16 master。

| 编号 | 平台 | 画幅 · 时长 · 分辨率 | 导入 | 规划 slug | 详情页 |
|------|------|---------------------|------|-----------|--------|
| P01 | **TikTok** | 9:16 · 15–60s · 1080×1920 | Paste link | `tiktok` | ⏳ |
| P02 | **Instagram Reels** | 9:16 · 15–90s · 1080×1920 | Paste link | `instagram-reels` | ⏳ |
| P03 | **YouTube Shorts** | 9:16 · ≤60s · 1080×1920 | Upload file | `youtube-shorts` | ⏳ |
| P04 | **Facebook Reels** | 9:16 · 15–60s · 1080×1920 | Paste link | `facebook-reels` | ⏳ |
| P05 | **Snapchat Spotlight** | 9:16 · 5–60s · 1080×1920 | Upload file | `snapchat` | ⏳ |
| P06 | **Pinterest Idea Pins** | 9:16 · 15–60s · 1080×1920 | Upload file | `pinterest` | ⏳ |

**卡片文案要点**

- TikTok：hook-first 竖屏、on-screen captions、trend-length pacing
- Reels：Reels-safe framing，字幕/CTA 避开 UI overlay，beat-matched cuts
- Shorts：payoff 前置、loop 内节奏、title-safe captions
- Facebook Reels：同一竖屏 master 重新 caption，开场节奏略慢
- Spotlight：快切、字幕偏上安全区
- Idea Pins：分步竖屏、numbered text overlays，how-to / 产品发现

### 4-B · Long-Form & Landscape（P07–P10）

横屏 placement，结构重于速度。Sparki 保留章节、callout 与清晰节奏。

| 编号 | 平台 | 画幅 · 时长 · 分辨率 | 导入 | 规划 slug | 详情页 |
|------|------|---------------------|------|-----------|--------|
| P07 | **YouTube** | 16:9 · 60s–10m · 1920×1080 | Upload file | `youtube` | ⏳ |
| P08 | **Twitch Clips & VODs** | 16:9 / 9:16 · 30–90s · 1920×1080 | Upload file | `twitch` | ⏳ |
| P09 | **LinkedIn** | 1:1 / 16:9 · 30–90s · 1080×1080 | Upload file | `linkedin` | ⏳ |
| P10 | **X (Twitter)** | 16:9 / 1:1 · ≤140s · 1280×720 | Paste link | `x` | ⏳ |

**卡片文案要点**

- YouTube：tight cold open、chaptered structure、搜索静音 autoplay 字幕
- Twitch：VOD 扫描 kills/laughs/clutch → montage 或竖屏 clip
- LinkedIn：更重字幕、更慢 cut rhythm，专业 feed
- X：inline autoplay 优化，payoff 在前 3 秒

### 4-C · Commerce & Marketplaces（P11–P15）

店铺/广告位有硬规格。Sparki 导出 listing-ready master。

| 编号 | 平台 | 画幅 · 时长 · 分辨率 | 导入 | 规划 slug | 详情页 |
|------|------|---------------------|------|-----------|--------|
| P11 | **Amazon Listings** | 16:9 · 30–60s · 1920×1080 | Upload file | `amazon` | ⏳ |
| P12 | **TikTok Shop** | 9:16 · 15–45s · 1080×1920 | Upload file | `tiktok-shop` | ⏳ |
| P13 | **Shopify Product Pages** | 1:1 / 16:9 · 15–30s · 1080×1080 | Upload file | `shopify` | ⏳ |
| P14 | **Meta Ads** | 9:16 / 1:1 · 6–30s · 1080×1920 | Upload file | `meta-ads` | ⏳ |
| P15 | **Etsy & Marketplaces** | 1:1 · 5–15s · 1080×1080 | Upload file | `etsy` | ⏳ |

**卡片文案要点**

- Amazon：feature-by-feature、marketplace spec、卖点 callout
- TikTok Shop：reveal 前置、price callout、closing CTA card
- Shopify：gallery 可 loop、足够短以 autoplay 不拖慢页面
- Meta Ads：hook-first performance creative、多 variant / 多 ratio 同日测试
- Etsy：短 square loop，展示 scale / texture / finish，无旁白

---

## 四、平台详情页结构（规划模板）

详情页尚未上线，预计与 Industries / Product Video 形态页共用结构模式：

| 模块 | 说明 |
|------|------|
| Hero | `AI {Platform} Video Editor` + 该平台专属价值主张 + 上传框 |
| **Why Sparki for {Platform}** | 5–6 条：画幅、时长窗口、caption 安全区、节奏、导入方式 |
| **Best Video Types for {Platform}** | 链回维度 1 形态（如 TikTok → F03 Ad / F10 Montage / F01 Unboxing） |
| How to Export for {Platform} in 3 Steps | Upload or paste link → Pick this platform → Export master |
| **Related Platforms** | 同组其他平台卡 + 链回 `/platforms` |
| FAQ | 5–6 条平台专属（时长、画幅、链接导入、字幕、直接发布等） |
| 底部 CTA | Try For Free |

**SEO 约定（规划）**

- Title 模式：`AI {Platform} Video Editor & Exporter | Sparki`
- 面包屑：Home → Platforms → {Platform}
- 与 [Video Resizer](https://sparki.io/features/video-resizer) 功能线交叉内链，但不重复功能页定位

---

## 五、与其他维度的关系

| 交叉 | 说明 |
|------|------|
| 维度 1 Format | 同一形态在不同平台需不同 pacing；如 F12 Gaming Highlight × P01 TikTok vs P03 Shorts |
| 维度 2 Industry | 本地商户常组合 P01–P04 竖屏 + Google Business（未单列，可走 P04/P13）；电商常组合 P11–P15 |
| 维度 3 Goal | G01 获客偏 P01–P06；G02 转化偏 P11–P15 |
| Gaming 页 "By platform" | 6 张平台卡为**渠道视角摘要**，非独立 URL；长尾应收敛至 `/platforms/{slug}` |
| Product Video 页 "By industry & channel" | 部分 channel（TikTok Shop / Amazon / Meta Ads）与 P11–P15 重叠 |
| creators `platform` 字段 | 红人打标 slug（`tiktok` / `youtube-shorts` 等）应对齐 P 编号，见 [creators-tags.md](../creators/creators-tags.md) |

### 组合示例

| 形态 | 平台 | 行业 | 说明 |
|------|------|------|------|
| F03 Product Ad | P14 Meta Ads | C01 美妆 | 冷流量 6–30s 竖屏/方形投放 |
| F12 Gaming Highlight | P01 TikTok | — | clutch cut，hook-first 15–45s |
| F18 Local Promo | P04 Facebook Reels | B1 餐饮 | 午餐特惠，较慢开场 beat |
| F06 E-commerce Video | P11 Amazon | C03 3C | 30–60s listing spec 视频 |

---

## 六、待定项

| 项目 | 状态 |
|------|------|
| 15 个平台详情页 | ⏳ 聚合页已上线，详情页全部待建 |
| P0 平台详情页优先级 | 待数据定：建议先 TikTok / YouTube Shorts / Instagram Reels / Amazon / Meta Ads |
| `taxonomy.ts` Platform 字段 | ⏳ 与 P01–P15 对齐 |
| 直接发布（publish from Sparki） | FAQ 已列，能力待产品确认 |

---

*遵循 [客户文档规范](../../demo/client-template.md)*  
*关联：[video-types-taxonomy.md](./video-types-taxonomy.md) | [features/video-resizer](../sparki-features.md) | [主文档](../sparki.md)*  
*Last updated: 2026-08-26*
