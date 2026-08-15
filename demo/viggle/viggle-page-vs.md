# Viggle Page Type: /vs/ 竞品对比页

> URL 模式：`/vs/[slug]/`  
> 关联：[viggle.md](./viggle.md) | [viggle-competitors.md](./viggle-competitors.md) | [viggle-keywords.md](./viggle-keywords.md) | [viggle-page-tools.md](./viggle-page-tools.md)

---

## 1. 页面定位

| 项目 | 说明 |
|------|------|
| **Page Type** | Competitor comparison pages |
| **用途** | 拦截「Viggle vs X」「X alternative」搜索；对比 Viggle 与竞品 |
| **关键词** | Viggle vs Kling、Viggle vs Runway、Viggle vs Pika 等 |

---

## 2. 对比页列表（首期）

| Slug | 目标关键词 | 竞品 | 优先级 |
|------|------------|------|--------|
| kling | Viggle vs Kling, Kling alternative | Kling（快手系） | P0 |
| runway | Viggle vs Runway, Runway alternative | Runway | P0 |
| pika | Viggle vs Pika, Pika alternative | Pika | P0 |
| heygen | Viggle vs HeyGen | HeyGen | P1 |
| synthesia | Viggle vs Synthesia | Synthesia | P1 |
| luma | Viggle vs Luma | Luma AI | P1 |

---

## 3. 数据文件结构（Data）

```ts
// data/vs/kling.ts
export default {
  slug: 'kling',
  competitor: 'Kling',
  title: 'Viggle vs Kling | Compare AI Video Tools | Viggle',
  metaDescription: '...',
  h1: 'Viggle vs Kling',
  comparison: {
    viggle: { features: [...], pros: [...], cons: [...] },
    competitor: { features: [...], pros: [...], cons: [...] }
  },
  comparisonTable: [ ... ],
  verdict: '...',
  cta: { ... }
}
```

---

## 4. 对比维度（建议）

| 维度 | 说明 |
|------|------|
| **定位** | Meme/角色 vs 通用视频/企业 |
| **核心功能** | Mix/Move/Mic vs 竞品功能 |
| **物理模型** | JST-1 vs 竞品技术 |
| **定价** | Free/Pro 起 vs 竞品定价 |
| **平台** | Web/iOS/Android/Discord vs 竞品 |
| **适用场景** | Meme、跳舞、角色动画 vs 竞品场景 |

---

## 5. 可选区块

| 区块 | 必填 | 说明 |
|------|------|------|
| Hero | ✅ | Viggle vs [竞品] |
| 对比表 | ✅ | 功能/定价/平台对比 |
| Viggle 优势 | ✅ | 差异化说明 |
| 竞品特点 | 可选 | 客观描述 |
| Verdict | 可选 | 适用人群建议 |
| CTA | ✅ | 引导试用 Viggle |

---

## 6. 文档导航

| 文档 | 用途 |
|------|------|
| [viggle.md](./viggle.md) | 产品功能、SEO 体系 |
| [viggle-competitors.md](./viggle-competitors.md) | 竞品分析（对比维度来源） |
| [viggle-page-tools.md](./viggle-page-tools.md) | /tools/ 工具页（可内链） |
