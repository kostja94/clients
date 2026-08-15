# Morph Studio 关键词与目标页

> 关联：[morphstudio.md](./morphstudio.md) | [morphstudio-features.md](./morphstudio-features.md) | [morphstudio-use-cases.md](./morphstudio-use-cases.md) | [morphstudio-site-structure.md](./morphstudio-site-structure.md)

**Last updated**: 2026-03-25

---

## 1. 品牌与品类（英）

| 类型 | 示例词 | 建议承接 |
|------|--------|----------|
| 品牌 | Morph Studio, morphaistudio, Morph AI | /（首页） |
| 品类 | AI video generator, AI image generator, text to video, image to video | 首页 + 对应工具根路径 |
| 聚合 | AI creative suite, multi model AI video, AI canvas video | 首页 / 产品总览（若有） |
| 风格迁移 | AI video style transfer, video to anime style | /video-style-transfer 或等价路径 |

---

## 2. 模型词 + 「Morph」（长尾）

| 方向 | 示例 | 备注 |
|------|------|------|
| Kling / Veo / Sora / Wan / Seedance / Hailuo… | "{model} video generator", "try {model} online" | 落地页须与真实接入一致，避免虚假宣传 |
| 对比 | Morph Studio vs Runway, vs Luma | 对比页需可验证事实 |

---

## 3. 程序化工具词（与页脚对齐）

每条工具线对应独立 URL（slug 以工程为准），例：

| 关键词簇 | 可能 URL 模式 |
|----------|----------------|
| AI logo generator | /ai-logo-generator |
| text to video | /text-to-video |
| video style transfer | /video-style-transfer |
| AI headshot generator | /ai-headshot-generator |
| AI background remover | /ai-background-remover |

*完整 slug 与索引策略见 [morphstudio-site-structure.md](./morphstudio-site-structure.md)。*

---

## 4. 电影制作与预演（长尾簇）

对应叙事与 Persona 见 [morphstudio-use-cases.md](./morphstudio-use-cases.md) §0、§2.1。此类词与泛词 *AI video generator* 意图不同，建议 **独立落地页或支柱文章**，内链回 `/text-to-video`、Open Canvas 说明页（若有）。

| 意图 | 示例词 / 短语 | 建议承接 |
|------|----------------|----------|
| 品类+人群 | AI video generator for filmmakers, AI video for filmmaking, AI film generator | `/for-filmmakers` 或 `/solutions/filmmaking`（若建站） |
| 工作流 | AI previsualization, AI previs tool, script to storyboard AI | 支柱博客 + CTA 入产品 |
| 分镜 | AI storyboard generator, storyboard to video AI, shot list AI | Open Canvas / 画布功能页 + 案例 |
| 独立/低成本 | indie film AI video, low budget previs AI | 同上，强调概念与比稿阶段 |

---

## 5. 待办

- [ ] GSC 导出后按 URL 聚类，去重 cannibalization（多模型落地页 vs 总览页）  
- [ ] 核对接入模型清单与页面承诺一致  
- [ ] 修正站内错别字关键词（如 Banana 拼写）避免品牌搜索分流  
