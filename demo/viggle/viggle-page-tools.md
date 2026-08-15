# Viggle Page Type: /tools/ 工具页

> URL 模式：`/tools/[slug]/`  
> 关联：[viggle.md](./viggle.md)（产品功能、SEO 体系）| [viggle-keywords.md](./viggle-keywords.md) | [viggle-page-vs.md](./viggle-page-vs.md) | [viggle-page-for.md](./viggle-page-for.md)

---

## 1. 页面定位

| 项目 | 说明 |
|------|------|
| **Page Type** | Tool pages |
| **用途** | 覆盖具体功能/产品关键词，如 face swap、AI dance、meme maker、image-to-video |
| **与产品功能映射** | 工具页按**关键词/场景**划分，非 1:1 产品功能；可调用 Mix、Animate、Move、Mic、Ideate |

---

## 2. 工具页列表（首期）

| Slug | 目标关键词 | 调用的 Viggle 功能 | 优先级 |
|------|------------|---------------------|--------|
| face-swap | face swap, face swap AI | Multi、Custom Multiswap | P0 |
| ai-dance | AI dance, make image dance | Mix、Move（舞蹈模板） | P0 |
| meme-maker | meme maker, AI meme generator | Mix、Animate、Move、Mic | P0 |
| image-to-video | image to video, image to video AI | Mix、Animate、Ideate | P0 |

---

## 3. 数据文件结构（Data）

每页对应 1 个 data 文件，供模板渲染。示例：

```ts
// data/face-swap.ts
export default {
  slug: 'face-swap',
  title: 'Face Swap AI | Swap Faces in Videos | Viggle',
  metaDescription: '...',
  h1: 'Face Swap AI',
  hero: { ... },
  features: [ ... ],
  howItWorks: [ ... ],
  cta: { ... },
  faq: [ ... ],
  media: { video: '...', screenshots: [...], gallery: [...] }
}
```

---

## 4. 工具页与 Viggle 功能映射

| 工具页 | Viggle 功能 | 说明 |
|--------|-------------|------|
| **face-swap** | Multi、Custom Multiswap | 多角色/人脸替换 |
| **ai-dance** | Mix、Move | 图片+舞蹈视频混合；4000+ 动作模板 |
| **meme-maker** | Mix、Animate、Move、Mic | Meme 创作全流程 |
| **image-to-video** | Mix、Animate、Ideate | 图转视频核心能力 |

---

## 5. 可选区块（Section）

| 区块 | 必填 | 说明 |
|------|------|------|
| Hero | ✅ | 标题、副标题、CTA |
| Features | ✅ | 3–4 个核心能力 |
| How it works | 可选 | 步骤说明 |
| Comparison | 可选 | 与竞品/传统方式对比 |
| Gallery | 可选 | 示例图/视频 |
| FAQ | 可选 | 常见问题 |
| CTA | ✅ | 引导试用/订阅 |

---

## 6. 待扩展工具页（候选）

| Slug | 目标关键词 |
|------|------------|
| character-animation | character animation AI |
| voice-to-animation | voice to animation, AI lip sync |
| text-to-video | text to video AI |
| ai-lip-sync | AI lip sync |

---

## 7. 文档导航

| 文档 | 用途 |
|------|------|
| [viggle.md](./viggle.md) | 产品功能（Mix、Animate、Move、Mic、Ideate）、定价、SEO 体系 |
| [viggle-page-vs.md](./viggle-page-vs.md) | /vs/ 竞品对比（可内链） |
| [viggle-page-for.md](./viggle-page-for.md) | /for/ 受众页（可内链） |
| [viggle-keywords.md](./viggle-keywords.md) | 关键词映射 |
