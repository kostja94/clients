# Sparki — Product & Competitors Reference

> 加载时机：Phase 0R（R1）· Phase 4（Draft 对比文/产品事实）· Phase 5（G1/G4/G5 对照）
> 主文件：SKILL.md §1 速查

---

## 1. 产品事实（创作可用；对照 sparki.io 官网验证）

**One-line**：
> Sparki is the first AI editing agent — upload footage, chat about the cut you want, and an AI agent plans and executes the edit in the cloud, then refines it through conversation.

**核心功能**（features 页 URL 均为可链白名单）：

| 功能 | 能力要点（写作可用） | 官方页 |
|------|---------------------|--------|
| **Copy Style** | 上传/粘贴参考视频（TikTok/Reels/Shorts/本地），AI 解析切频、转场、节奏、文字叠加与 pacing，把风格应用到自有素材；克隆"剪辑配方"而非内容 | /features/copy-style |
| **Long to Short** | 长视频（最长 ~3 小时）→ TikTok/Reels/Shorts；分析叙事流、情绪峰值自动找高光；Chat-to-Cut 多轮调整；批量 10–20 clips；贴 YouTube URL | /features/long-to-short |
| **AI Caption** | 自动转写 + 动画字幕；50+ 语言、多说话人；宣称 95% 转写准确率；100+ 样式 | /features/ai-caption |
| **AI Commentary** | 为游戏/反应/教程/体育等生成同步解说；50+ AI 音色或克隆声音；时间轴对齐 | /features/ai-commentary |
| **Video Resizer** | 智能 crop + reframing 适配 9:16/1:1/16:9 等；自动跟踪人脸/说话者/文字 | /features/video-resizer |
| Highlight Reels | 高光集锦（solutions 下，非 /features） | /solutions/highlight-reels |

**平台/模型形态**：
- 云端处理；Web Agent 交互（对话 → 计划 → 执行 → 多轮修订）
- 常见素材类型：游戏、反应、Vlog、口播、教程、体育集锦、播客/Webinar 长改短、电商/产品演示

**定价**（as of；官网 #pricing）：
- Free：300 credits + 3GB
- Starter / Plus：月付或年付（年付约 −40%）
- Enterprise：定制（API、SLA、并发）→ enterprise@sparki.io

**可声称 / 须限定**（G3/G5）：

| 可声称 | 限定 |
|--------|------|
| "95% 转写准确率" | 标注 "per Sparki's AI Caption page"（官网能力声明，非独立测评） |
| "最长约 3 小时"、"10–20 条批量" | 同源标注；用 "up to / roughly" |
| "50+ 语言 / 50+ 音色" | 标注官网来源 |
| 云端、多轮修订 | 属产品形态，正常描述 |

**不可声称**：
- 超出官网 features 的能力（G5）
- 与竞品的直接性能对比数字（除非有公开 benchmark）
- 红人 Creator 与 Sparki 存在合作/使用关系（除非官网明确，G7）
- 任何"保证"类表述

---

## 2. 竞品矩阵（写作必须承认各家优势）

| 竞品 | 类型 | 优势（必须写） | 限制 | 参考 URL |
|------|------|---------------|------|---------|
| **CapCut / 剪映** | 移动/消费级模板剪辑 | 免费模板生态强、上手快、海量素材/特效、社区大 | 模板驱动，逐条手动套；时间线操作密集 | capcut.com |
| **Descript** | AI 原生文本驱动剪辑 | 转录编辑成熟、播客工作流强、Overdub/Studio Sound 口碑 | 定位偏播客/口播；时间线编辑能力有限 | descript.com |
| **OpusClip** | 长改短 Clip 工具 | 自动化切片专注、多平台预设成熟 | 减法式抽 clip，较少"重建结构/精修叙事" | opus.pro |
| **Vizard / Klap** | 长改短/垂直化 | 快速切片、字幕自动化 | 深度编辑与叙事重构能力有限 | vizard.ai / klap.app |
| **Gling.ai** | YouTube 剪辑 | 自动去停顿/口水音、定位清晰 | 面向 YouTuber 粗剪，功能面窄 | gling.ai |
| **Runway / Pika 等** | 生成式视频 | 文生视频/素材生成 | 编辑既有素材的场景弱 | runwayml.com |
| **Premiere/DaVinci/FCP** | 传统 NLE | 专业控制力、生态与插件 | 学习曲线高 | adobe.com 等 |

**Sparki 差异化（写作叙事）**：
- **Agent 优先**：对话式 → 计划 → 执行 → 多轮修订（非一次性自动生成，非模板套用）
- **复制风格**：Copy Style 参考任何视频的剪辑配方（竞品多为内置模板）
- **云端 + 订阅 credits**：低配置门槛、无本地算力依赖
- 对比文基调：*different, not better* —— 明确"哪种工作流用谁"，而非"我们最好"

---

## 3. 竞品公平描写规则

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势 | 从 §2 优势列取，写进正文非列表堆砌 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" / "basically just" |
| 对比表无二元化 | 需 nuance 的能力不简化 Yes/No；必要时加脚注 |
| ≥1 场景推荐非 Sparki 方案 | 写在正文（如纯本地/私有化需求 → NLE；纯移动端快剪 → CapCut） |
| 竞品外链 | `rel="nofollow noopener"` |

---

## 4. 红人/创作者生态（CreatorClone 依据）

- 参考公开账号：官网 `/creators`（18 页）、TikTok/YouTube/IG 公开内容。
- 素材原则：写拆解时引用的切点/转场/字幕观察必须来自 Phase 0R 实际抓取的公开素材；不臆测 creator 的创作动机或工具选择。
- 合规：不暗示 affiliation/代言/授权；标题用 "How to Edit Like X"（教育），不用 "X uses Sparki"。
- 详情：SKILL.md §5 Gotchas + article-types.md CreatorClone 模板。

---

*product-competitors · sparki v1.0.0 · 2026-09-04*
