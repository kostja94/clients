# Viggle Page Type: /glossary/ 概念页

> URL 模式：`/glossary/[slug]/`  
> 关联：[viggle.md](./viggle.md)（产品功能，用于 Viggle connection）| [viggle-keywords.md](./viggle-keywords.md) | [viggle-page-tools.md](./viggle-page-tools.md)

---

## 1. 页面定位

| 项目 | 说明 |
|------|------|
| **Page Type** | Concept pages |
| **用途** | 覆盖「what is X」搜索；解释术语、概念，建立权威 |
| **关键词** | what is face swap、what is motion capture、what is AI lip sync 等 |

---

## 2. 概念页列表（首期）

| Slug | 目标关键词 | 说明 |
|------|------------|------|
| face-swap | what is face swap, face swap meaning | 换脸技术 |
| motion-capture | what is motion capture, motion capture meaning | 动作捕捉 |
| ai-lip-sync | what is AI lip sync, lip sync AI | AI 唇形同步 |
| image-to-video | what is image to video, image to video AI | 图转视频 |
| meme-generator | what is meme generator, AI meme generator | Meme 生成器 |
| character-animation | what is character animation |

---

## 3. 数据文件结构（Data）

```ts
// data/glossary/face-swap.ts
export default {
  slug: 'face-swap',
  term: 'Face Swap',
  title: 'What is Face Swap? | Definition & Guide | Viggle',
  metaDescription: '...',
  h1: 'What is Face Swap?',
  definition: '...',
  howItWorks: '...',
  useCases: [ ... ],
  viggleConnection: '...',  // 与 Viggle 的关联
  relatedTerms: [ ... ],
  faq: [ ... ]
}
```

---

## 4. 内容结构建议

| 区块 | 必填 | 说明 |
|------|------|------|
| Definition | ✅ | 术语定义（2–3 句） |
| How it works | 可选 | 技术/原理简述 |
| Use cases | 可选 | 典型应用场景 |
| Viggle connection | 可选 | Viggle 如何实现该功能 |
| Related terms | 可选 | 相关术语内链 |
| FAQ | 可选 | 常见问题 |

---

## 5. 文档导航

| 文档 | 用途 |
|------|------|
| [viggle.md](./viggle.md) | 产品功能（Viggle connection 区块来源） |
| [viggle-page-tools.md](./viggle-page-tools.md) | /tools/ 工具页（相关术语可内链） |
