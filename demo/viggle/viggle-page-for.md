# Viggle Page Type: /for/ 受众页

> URL 模式：`/for/[slug]/`  
> 关联：[viggle.md](./viggle.md) | [viggle-use-cases.md](./viggle-use-cases.md) | [viggle-keywords.md](./viggle-keywords.md) | [viggle-page-tools.md](./viggle-page-tools.md)

---

## 1. 页面定位

| 项目 | 说明 |
|------|------|
| **Page Type** | Audience pages |
| **用途** | 覆盖「for [受众]」搜索；为特定用户群体定制内容 |
| **关键词** | for meme creators、for TikTok creators、AI animation for 等 |

---

## 2. 受众页列表（首期）

| Slug | 目标关键词 | 受众 | 优先级 |
|------|------------|------|--------|
| meme-creators | for meme creators, AI meme for creators | Meme 创作者 | P0 |
| tiktok-creators | for TikTok creators, AI video for TikTok | TikTok 创作者 | P0 |
| content-creators | AI animation for creators | 内容创作者 | P0 |
| marketers | AI video for marketing | 营销人员 | P1 |
| influencers | AI animation for influencers | 网红/KOL | P1 |
| social-media-managers | AI video for social media | 社交媒体运营 | P1 |

---

## 3. 数据文件结构（Data）

```ts
// data/for/meme-creators.ts
export default {
  slug: 'meme-creators',
  audience: 'Meme Creators',
  title: 'AI Meme Maker for Meme Creators | Viggle',
  metaDescription: '...',
  h1: 'Viggle for Meme Creators',
  hero: { ... },
  painPoints: [ ... ],
  solution: { ... },
  features: [ ... ],
  useCases: [ ... ],
  cta: { ... }
}
```

---

## 4. 受众与 Viggle 功能映射

| 受众 | 调用的功能 | 典型场景 |
|------|------------|----------|
| **Meme creators** | Mix、Move、Mic | 跳舞、搞笑、病毒式 |
| **TikTok creators** | Mix、Move、Mic | 竖屏、短视频、舞蹈 |
| **Content creators** | Mix、Animate、Move、Mic、Ideate | 全功能 |
| **Marketers** | Animate、Ideate | 营销素材、角色动画 |
| **Influencers** | Mix、Mic | 个人 IP 动画、口播 |

---

## 5. 可选区块

| 区块 | 必填 | 说明 |
|------|------|------|
| Hero | ✅ | For [受众] |
| Pain points | 可选 | 该受众痛点 |
| Solution | ✅ | Viggle 如何解决 |
| Features | ✅ | 相关功能 |
| Use cases | 可选 | 典型场景 |
| Testimonial | 可选 | 用户评价 |
| CTA | ✅ | 引导试用 |

---

## 6. 待扩展受众页（候选）

| Slug | 目标关键词 |
|------|------------|
| instagram-creators | for Instagram creators |
| youtube-creators | AI video for YouTube |
| brands | AI video for brands |
| educators | AI animation for education |

---

## 7. 文档导航

| 文档 | 用途 |
|------|------|
| [viggle.md](./viggle.md) | 产品功能、SEO 体系 |
| [viggle-use-cases.md](./viggle-use-cases.md) | 用例、persona（受众与场景来源） |
| [viggle-page-tools.md](./viggle-page-tools.md) | /tools/ 工具页（可内链） |
