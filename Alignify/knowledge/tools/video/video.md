# AI Video · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网与产品文档、GII/Fortune Business Insights 等第三方市场报告、Variety/WaveSpeed 等媒体横向评测、Bloomberg Law / OpenAI 官方公告等合规追踪）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**。

**站内对照**：[alignify.co/tools/video](https://alignify.co/tools/video) · `/tools/video` · [alignify.co/zh/tools/video](https://alignify.co/zh/tools/video) · `/zh/tools/video` · `content/tools/zh/video.md`、`content/tools/en/video.md` · slug **`video`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 [`#video-tools`](../../product/alignify-keywords-tools.md#video-tools)

**站内相邻**：本页为 **Hub**；生成层主归属 [video-generator.md](video-generator.md) · 实时交互长视频 [interactive-video.md](interactive-video.md) · 输入专论 [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [video-to-video.md](video-to-video.md)

**勿与…混买**：本页只做品类分流与内容分工说明，不替代专页选型；旗舰模型 URL 表与横评 **仅** 见 [video-generator.md](video-generator.md) §外链索引。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`video`（本页）** | **`video-generator`** | **`video-editor`** | **`video-to-video`** |
|------|---------------------|-----------------------|--------------------|-----------------------|
| **典型买家问题** | 「用 AI 做视频有哪些工具？哪类适合我？」 | 「给我一段文字/图片，直接生成视频」 | 「我有素材，需要 AI 帮我剪、加字幕、调色」 | 「把现有视频变成另一种风格/画风」 |
| **交付形态** | 品类总览与分流 | 文生/图生/视频生成模型与平台 | 浏览器端/桌面端时间线编辑器 | 风格迁移、内容变换 |
| **验收核心** | 清楚自己需要哪个子品类 | 生成质量、时长、一致性、音频 | 剪辑效率、字幕、模板 | 风格保真、运动保留 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 子类导航（15 slug → 深度知识块）

| slug | 典型买家问题 | 深度知识块 |
|------|--------------|------------|
| `video-generator` | 哪种模型/平台从零生成视频？ | [video-generator.md](video-generator.md) |
| `interactive-video` | 生成过程中能否改 prompt、连续播多久？ | [interactive-video.md](interactive-video.md) |
| `text-to-video` | 输入是文本/文档？ | [text-to-video.md](text-to-video.md) |
| `image-to-video` | 输入是静态图，要让它动起来？ | [image-to-video.md](image-to-video.md) |
| `video-to-video` | 已有视频要换风格/改场景？ | [video-to-video.md](video-to-video.md) |
| `video-editor` | 已有素材，要剪、字幕、调色？ | [video-editor.md](video-editor.md) |
| `video-clipping` | 长视频自动剪成多条 TikTok？ | [video-clipping.md](video-clipping.md) |
| `video-effects` | 抠像、跟踪、去路人？ | [video-effects.md](video-effects.md) |
| `canvas-video` | 多模型节点画布串管线？ | [canvas-video.md](canvas-video.md) |
| `filmmaking` | 电影级剧本→成片全流程？ | [filmmaking.md](filmmaking.md) |
| `animation-generator` | 动漫/动画风格从零生成？ | [animation-generator.md](animation-generator.md) |
| `short-drama` | 竖屏多集短剧+分发变现？ | [short-drama.md](short-drama.md) |
| `music-video-generator` | 有一首歌，要生成 MV？ | [music-video-generator.md](music-video-generator.md) |
| `video-translator` | 视频多语言翻译/配音？ | [video-translator.md](../voice-audio/video-translator.md)（语音 territory） |

**工作流提示**：专业团队常见组合为 **生成（generator / T2V / I2V）→ 编辑（editor）→ 分发（clipping）**；全片 anime 化走 **video-to-video**，从零生成动漫走 **animation-generator**。

---

## 内容分工（各 slug 写什么、不写什么）

| 内容类型 | 主归属知识块 | 其它块处理方式 |
|----------|--------------|----------------|
| 品类地图 / 子类分流 | **本页 `video`** | 专页只保留与本 slug 相关的一行对比 |
| 通用 T2V/I2V 模型横评 + 完整 URL 表 | [video-generator.md](video-generator.md) | ≤2 个代表 + 「完整对比见 generator §外链索引」 |
| 实时交互 / Live Model / 无限流 steering | [interactive-video.md](interactive-video.md) | generator/world-model 各 ≤2 句 + 链本页 SSOT |
| T2V 定义 + 讲解视频 / 数字人播报 | [text-to-video.md](text-to-video.md) | generator 不展开 Golpo/VideoTutor/Synthesia 专表 |
| I2V + Motion Brush / 品牌保真 / 废片率 | [image-to-video.md](image-to-video.md) | generator 不重复 I2V 长定义 |
| V2V + 时间一致性 / 风格迁移 | [video-to-video.md](video-to-video.md) | video-effects 仅抠像/跟踪；全片风格化链 V2V |
| 节点多模型编排 | [canvas-video.md](canvas-video.md) | generator 不写 ComfyUI 画布长段 |
| 电影全管线（剧本→后期） | [filmmaking.md](filmmaking.md) | 不含短剧专章；生成片段选型链 generator |
| 动漫平台（agent vs style transfer） | [animation-generator.md](animation-generator.md) | 不写 Runway/Veo 通用横评 |
| 竖屏短剧 + 投流变现 | [short-drama.md](short-drama.md) | 底层模型列表链 generator |
| 音频驱动 MV | [music-video-generator.md](music-video-generator.md) | 明确不收录通用 T2V 产品表 |
| 时间线编辑 | [video-editor.md](video-editor.md) | 不含生成模型表 |
| 长→短 repurposing | [video-clipping.md](video-clipping.md) | 不含 T2V |
| VFX / 抠像 / 跟踪 | [video-effects.md](video-effects.md) | 风格迁移见 V2V |
| 通用合规（deepfake/版权/平台标注） | **本页** | 专页各留 ≤3 条品类特有风险 |

**产品表规则**：完整 Runway / Veo / Kling / Pika / Luma / Hailuo URL 表 **仅** 出现在 video-generator；本 Hub **无 URL 表**。

---

## 全簇共享事实（版本号与关停日期以 video-generator 外链索引同步维护）

| 事实 | 统一表述 |
|------|----------|
| Sora 2 关停 | 2026-03-24 OpenAI 宣布关停；Web/App **2026-04-26** 下线；API **2026-09-24** 下线 |
| T2V 市场占比 | 约 **46%**（2026 第三方报告口径；细节见 video-generator） |
| 2026 旗舰模型代际与横评 | **Veo 3.1**（原生音频 + 4K；prompt 遵循度领先）/ **Runway Gen-4.5**（角色一致 + Motion Brush；控制不可替代）/ **Kling 3.0**（多镜头 + 原生音频 5 语言；性价比占优）；2025–2026 无全能冠军；Sora 2 关停标志大厂消费级退场；完整对比见 [video-generator §对比与测评](video-generator.md#对比与测评第三方观点非官方) |
| 推理成本趋势 | 约 10× 下降（2025→2026，~$2.50→~$0.18–0.30/5s 片段量级） |
| 实时交互分支（2026-09） | **Query Model**（离线 clip）vs **Live Model / 交互流**（Orbis、fal.live、Odyssey-2 Pro）——产品 SSOT 见 [interactive-video.md](interactive-video.md) |

---

## 词汇锚点（Hub 级，细节见专页）

- **AI 视频（本页主轴）**：涵盖 **生成**（从无到有）、**编辑**（处理已有像素）、**特效/Repurposing** 与 **垂直场景**（电影、动漫、短剧、MV）。生成子类按 **输入模态** 分为 T2V / I2V / V2V——定义与产品深度见 **§子类导航** 各 spoke，不在此重复。
- **旗舰模型、市场占比、关停时间线**：见 **§全簇共享事实**；完整 URL 表见 [video-generator.md](video-generator.md) §外链索引。
- **讲解视频 / 数字人播报**：专论见 [text-to-video.md](text-to-video.md)（T2V 子类，非通用生成横评）。

---

## 问题域（为何会出现这类产品）

- **视频消费与供给失衡**：移动流量以视频为主（占全球移动网络流量约 65%+），品牌与创作者需高频产出，传统摄制成本与周期难以匹配。
- **短视频平台驱动**：Reels/Shorts/TikTok 使「可发布短片」成为默认内容单元——83% 美国成年人使用 YouTube（Pew 2024），需求频次远超制作能力线性增长。
- **生成式模型跃迁**：2023–2026 从「几秒可用」到 4K/原生音频联合生成；推理成本显著下降（详见 video-generator）。
- **多语言与培训规模化**：数字人口播与讲解视频降低本地化与 LMS 内容成本（专页：text-to-video）。
- **平台依赖风险**：Sora 从发布到关停不足 18 个月——关键模型/API 关停促使多模型管线成为 2026 年最佳实践。

---

## 风险 · 合规 · 伦理与版权（簇总述；专页各留品类特有风险）

- **深度伪造与名誉侵害**：非自愿影像、虚假代言、政治误导——韩国 2024 年修法将深度伪造性犯罪刑罚提至 7 年；OpenAI Sora 2 发布后遭遇好莱坞抵制，平台 opt-in/opt-out 政策分化。
- **版权与训练数据**：模型训练来源不透明；输出权属因法域而异；意大利 2025 年立法要求 AI 辅助作品须有「充分的人类智力贡献」方可受版权保护。
- **平台披露义务**：欧盟 AI 法案第 50 条、印度 2026 年 SGI 标注规则等要求合成内容标识与不可篡改元数据。
- **生物识别与 KYC 欺诈**：AI 视频可让静态证件照「动起来」，传统 KYC 流程面临系统性挑战。
- **供应商锁定**：资产与 workflow 应跨平台备份——勿将生产管线绑定单一模型。

---

## 落地碎片（无先后）

- 先选 **场景轴**：凭空生成 / 已有素材编辑 / 口播培训 / 风格转换 / 多集短剧——再进上表专页。
- 生成仍常需多次迭代（专业创作者平均 10–50 次才有一条可用片段）；预算含试错成本。
- 企业采购优先合规认证（SOC 2、GDPR、训练数据声明），再比功能。
- 不要锁定单一模型；按质量/速度/成本路由多供应商（详见 video-generator）。

---

## 工具与产品类型

品类分流见 **§子类导航**；代表产品与完整 URL 表见各 spoke（生成层 SSOT：[video-generator.md](video-generator.md)）。

---

## 外链索引（Hub 级——产品链接见 video-generator §外链索引）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **AI Video Generator Market Report** | GII / Grand View Research 2026 市场规模（$2.1B→$8.9B by 2033） | [giiresearch.com](https://www.giiresearch.com/report/grvi1942046-ai-video-generator-market-size-share-trends.html) |
| **Sora 2 关停报道** | CNN 2026-03-24 报道 | [cnn.com](https://www.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down) |
| **WaveSpeed AI Video API Guide** | 2026 年视频生成 API 完整指南 | [wavespeed.ai](https://wavespeed.ai/blog/posts/complete-guide-ai-video-apis-2026/) |

### 对比与测评（第三方；观点非官方）

- **Hub 不做产品横评**：旗舰 T2V 规格与 Type 取舍见 [video-generator.md](video-generator.md) §对比与测评；实时交互见 [interactive-video.md](interactive-video.md)。
- **宏观趋势 SSOT**：Sora 关停、三足鼎立、Live Model 分支见 [video-generator.md](video-generator.md) §行业注记与 §全簇共享事实。

*观点非官方。*

---

## 延伸阅读 · 站内外

**站内**

- 生成层：[video-generator.md](video-generator.md) · [interactive-video.md](interactive-video.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [video-to-video.md](video-to-video.md)
- 后期：[video-editor.md](video-editor.md) · [video-clipping.md](video-clipping.md) · [video-effects.md](video-effects.md)
- 垂直/编排：[canvas-video.md](canvas-video.md) · [filmmaking.md](filmmaking.md) · [animation-generator.md](animation-generator.md) · [short-drama.md](short-drama.md) · [music-video-generator.md](music-video-generator.md)

**站外**

Hub 级站外参考见 **§外链索引**；产品 URL 表见 [video-generator.md](video-generator.md) §外链索引。