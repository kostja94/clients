# Vatt — 能力规格（产品模块 × 用户决策路径）

---

## 0. 文档结构与分部门索引

### 0.1 每个模块的固定结构

```
模块名 + 目标页面
├── 模块说明（一句话）
├── 对口部门
├── 用户决策路径
├── 用户问题表（问题 / 搜索词 / Vatt 答案 / Status / 营销）
├── 能力清单（从 vatt-features 迁移，供甲方核对 Status）
└── 分部门待确认清单
```

### 0.2 模块 ↔ 部门 ↔ 旧文档对照

| 模块 | 工作流 Step | 目标页 | 主问 | 协同 | 旧文档 |
|------|------------|--------|------|------|--------|
| M1 采集与导入 | ① | 待建 `/features` | **产品** | Web 客户端 | features §3.1 |
| M2 素材理解 | ② | `/features` | **AI/ML** | 产品 | features §3.2 |
| M3 同步与组织 | ③ | `/features` | **AI/ML** | 客户端 | features §3.3 |
| M4 粗剪与清理 | ④ | `/features` | **产品** | AI/ML | features §3.4 |
| M5 反应检测与 Hook | ⑤ | `/features` | **AI/ML** | 产品 | features §3.5–3.6 |
| M6 动效与包装 MG | ⑥–⑧ | `/features` | **产品** | 设计/MG | [motion-graphics](./vatt-motion-graphics.md) |
| M7 音频工程 | ④·⑧ | `/features` | **产品** | 客户端 | features §3.8 |
| M8 长素材与 Shorts | ②·⑤·⑨ | `/features` | **AI/ML** | 产品 | features §3.9 |
| M9 平台与导出 | ⑨·⑪ | `/features` | **客户端** | 产品 | features §3.10 |
| M10 可编辑时间线 | ⑩ | `/features` · FAQ | **产品** | 客户端 | features §3.11 |
| M11 版权意识剪辑 | Movie 栈 | Blog / FAQ | **产品** | **合规** | features §3.12 |
| M12 评论与社群 | — | Blog | **产品** | 增长 | features §3.13 |
| M13 信任与获取 | — | `/` · `/pricing` | **增长** | 合规、产品 | vatt.md |

### 0.3 用户问题表字段

| 字段 | 说明 |
|------|------|
| **用户问题** | Reaction 创作者心里的话；可作 FAQ / Blog H2 |
| **搜索词** | SEO 目标词 → [vatt-keywords.md](./vatt-keywords.md) |
| **Vatt 答案** | 对外一句话；🔲 = 待甲方确认 |
| **Status** | Current · Conditional · Opportunity · Claim-Restricted（见 §0.4） |
| **营销** | 首页 / Features / Blog / 对比页 / FAQ |

### 0.4 Feature Status（与 features 真源一致）

| Status | 对外写法 | 甲方需确认 |
|--------|---------|-----------|
| **Current** | 可写进 Landing（仍建议 release-scope 确认） | 邀请用户是否默认可用 |
| **Conditional** | 写「支持，但取决于…」并列出条件 | credits / 云分析 / 素材质量等 |
| **开发中** | **不得写已上线**；可写「正在开发 / 即将推出」，不承诺发布日期 | 上线范围与验收状态 |
| **Opportunity** | **不得写已上线**；可作 roadmap / Blog 方向 | 是否改 Status |
| **Claim-Restricted** | 仅教育话题；**禁止产品承诺** | 合规审阅 |

---

## M1 · 采集与导入（Capture & Import）

**模块说明**：素材从哪来——录屏、Face-Cam、麦克风、本地文件。

**目标页**：待建 `/features` · 首页 Demo

**对口部门**：产品（主）· Web 客户端

### 用户决策路径

```
选型：能录屏+露脸一起录吗？还是只能导本地文件？     → 是否适合我的录制习惯
  ↓
导入：能一次拖进多段素材吗？YouTube 链接行吗？       → 工作流是否省事
  ↓
使用中：录完轨道还能分开调吗？                       → 与 M3 同步、M10 时间线
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M1.1 | 能录屏幕吗？ | screen record reaction video | 全屏/窗口/区域录制 | Current | Features |
| M1.2 | 能同时录摄像头（Face-Cam）吗？ | record facecam reaction | 同步录创作者画面 | Current | Features |
| M1.3 | 能录麦克风和电脑里的原片声音吗？ | record system audio reaction | 支持录制麦克风和电脑系统音频 | Current | FAQ |
| M1.4 | 一次性能录屏+摄像头+麦克风吗？ | multi-source reaction recording | 支持同时录制屏幕、摄像头和麦克风 | Current | Features |
| M1.5 | 能导入本地视频吗？ | import video ai editor | 本地视频/音频/图片/文件夹 | Current | 首页 |
| M1.6 | 能批量导入多段素材吗？ | batch import video editor | 支持 | Current | FAQ |
| M1.7 | 能用 YouTube 链接导入吗？ | import youtube video editor | 开发中；目前不支持 YouTube 链接导入，URL 录制入口用于录制网页，不等同于下载/导入视频 | 开发中 | Blog |
| M1.8 | 录完后原片和 Face-Cam 是分开的轨道吗？ | separate source facecam tracks | 原片和 Face-Cam 保持为独立可编辑轨道 | Current | M3 联动 |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | M1.3–M1.4 已确认 Current；补充浏览器和权限细节即可 |
| **客户端** | Web 录制支持哪些浏览器/OS？与 Desktop 录制 roadmap？ |

---

## M2 · 素材理解（Footage Understanding）

**模块说明**：AI 先「看懂」长素材——镜头、语音、情绪、可搜索地图。

**对口部门**：AI/ML（主）· 产品

### 用户决策路径

```
听说「AI 理解素材」：几小时的电影/直播能处理吗？         → 是否比 Descript 适合 Reaction
  ↓
试用：能搜「他说 shocked 在哪」吗？                     → 找 moment 效率
  ↓
信任：识别准吗？                                       → 与 M5 反应检测
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M2.1 | 能处理多长的视频？ | ai long video editor | 最长支持 3 小时视频 | Current | Features P0 |
| M2.2 | AI 能「看懂」素材讲什么吗？ | understand long reaction footage | 长素材地图 + 镜头/语音/情绪信号 | Current | 核心差异化 ★ |
| M2.3 | 能按内容搜片段吗？ | search video by transcript and signals | 开发中；目标是按 ASR 文本及情绪、视觉、镜头信号搜索片段，当前底层仅有正则/子串匹配，不是完整语义搜索 | 开发中 | Blog |
| M2.4 | 能识别说话内容吗？ | ai speech recognition video | 语音转文字 | Current | FAQ |
| M2.5 | 能识别笑/惊讶等表情吗？ | ai emotion detection video | 情绪信号检测 | Current | M5 联动 |
| M2.6 | 能分清哪条是原片、哪条是我吗？ | source vs creator track | Source-vs-Creator 角色识别 | Current | Movie Reaction |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **AI/ML** | 最长 3 小时（已确认）；分析完成前用户看到什么；其他 Conditional 依赖项清单 |
| **产品** | 对外如何说「理解」而不 over-promise（vs 100% 准确禁令） |

---

## M3 · 同步与组织（Sync & Alignment）

**模块说明**：原片与 Face-Cam、多机位、波形对齐——Reaction 最耗时环节之一。

**对口部门**：AI/ML（主）· 客户端

### 用户决策路径

```
痛点：原片和脸 cam 对不齐怎么办？                       → 核心购买理由
  ↓
导入后：会自动对齐吗？还要手动拖波形吗？               → 省多少时间（禁写 10x 除非甲方给证据）
  ↓
多机位：两个摄像头能 sync 吗？                         → 进阶用户
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M3.1 | 原片和 Face-Cam 能自动对齐吗？ | sync facecam with source video | 选择两条含音频的 Clip 后可一键自动计算并对齐；不会在导入后自动发生 | Current（需主动触发） | P0 差异化 ★ |
| M3.2 | 还要手动对波形吗？ | align reaction video audio | 无需手动匹配波形；选择两条含音频 Clip 并触发 Audio Align 后自动计算偏移 | Current（需主动触发） | FAQ |
| M3.3 | 删一段会自动保持轨道对齐吗？ | ripple delete multi track | Ripple Delete 可以对指定时间范围全轨联动删减；普通单 Clip 删除不会全轨联动 | Current（Ripple Delete 工作流） | Features |
| M3.4 | 多机位能 sync 吗？ | multi camera sync video | 多机位批量同步开发中；当前只支持两条含音频 Clip 成对对齐 | 开发中 | Blog |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **AI/ML** | 波形 sync vs 通用对齐：对用户怎么说一句？失败时 fallback？ |
| **客户端** | Multi-Source Timeline Setup 默认轨道结构（Source/Creator 标签） |

---

## M4 · 粗剪与清理（Rough Cut & Cleanup）

**模块说明**：删 dead air、缩停顿、降噪、响度——得到可继续编辑的第一版。

**对口部门**：产品（主）· AI/ML

### 用户决策路径

```
：能自动剪掉空白和废话吗？                           → 省时间
  ↓
担心：会不会把「憋笑停顿」也剪没了？                   → 粗剪原则叙事
  ↓
进阶：能用一句话生成粗剪吗？                           → NL editing → M10
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M4.1 | 能自动删 silence / dead air 吗？ | remove dead air reaction video | 开发中；计划基于 speech/silence 信号执行 Ripple Delete，并保留用户复核 | 开发中 | P0 |
| M4.2 | 会删掉反应里重要的停顿吗？ | ai rough cut reaction | 开发中；无法保证不会误删，必须允许用户预览、调整和 Undo | 开发中（仍不得保证不会误删） | FAQ 信任 |
| M4.3 | 能去 um uh 吗？ | filler word removal video | 开发中；计划结合 ASR 与编辑操作移除已识别的 filler words，准确性取决于转写 | 开发中 | Blog |
| M4.4 | 能降噪、统一音量吗？ | normalize audio reaction video | 降噪 + 响度标准化 | Current | Features |
| M4.5 | 说话时能自动压低原片声吗？ | audio ducking reaction | Automatic Ducking | Current | M7 联动 |
| M4.6 | 能用一句话描述生成粗剪吗？ | ai rough cut from prompt | Rough Cut from Prompt | Current | Demo |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | Dead Air vs Pause Shortening 对用户默认行为；M4.2 原则有无产品开关 |
| **AI/ML** | Rough Cut from Prompt 已上线范围与 Conditional 条件 |

---

## M5 · 反应检测与 Hook（Reaction & Hook）

**模块说明**：找大笑、惊讶、高能 moment；冷开场 Hook。

**对口部门**：AI/ML（主）· 产品

### 用户决策路径

```
核心：能自动找出最好笑的/最 shock 的时刻吗？            → Beachhead 差异化 ★★★
  ↓
Shorts：能从长视频里摘竖屏高光吗？                     → M8 联动
  ↓
开场：能把后面高能剪到开头当 hook 吗？                   → Retention
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M5.1 | 能自动找 strong reaction 时刻吗？ | ai reaction highlight finder | 笑/惊讶/震惊/兴奋等 | Current | P0 ★ |
| M5.2 | 能按情绪强度排序吗？ | find best reaction moments | Emotional Peak Ranking | Current（按 emotion confidence/score 排序） | Features |
| M5.3 | 能把高能 moment 放到视频开头吗？ | reaction video hook generator | Cold-Open Hook | Current | Blog |
| M5.4 | AI 会建议几个开场 hook 吗？ | ai hook suggestions video | AI Hook Suggestions | Current | FAQ |
| M5.5 | 能在时间线上看到标记吗？ | reaction timeline markers | Reaction Timeline Markers | Current（选中 Clip 时显示） | Demo |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **AI/ML** | M5.1 准确率对外怎么说（避开 §Claims 禁令）；Tier 1 是否全部 Current 可写 |
| **产品** | 官网/ Demo 展示的 highlight 是否真实 pipeline 输出 |

---

## M6 · 动效与包装（Motion Graphics）

**模块说明**：布局（PIP/分屏）、字幕、花字、贴纸、转场、情绪强化——均在可编辑时间线上。

**详表**：→ **[vatt-motion-graphics.md](./vatt-motion-graphics.md)**（MG 唯一维护处，本文只列用户问题）

**对口部门**：产品（主）· 设计/MG · 客户端

### 用户决策路径

```
：能做 PIP / 分屏吗？还是固定模板？                   → vs 拼接工具
  ↓
Shorts：竖屏双画面、字幕安全区？                        → TikTok/Reels
  ↓
情绪：大笑时能自动 zoom/shake 吗？                      → ReAmp
  ↓
控制：AI 加的 layout 我能改吗？                         → M10
```

### 用户问题表（入口级；细节见 motion-graphics）

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M6.1 | 原片+脸 cam 有哪些布局？ | reaction video layout pip split | PIP / 分屏 / 竖屏堆叠等可编辑 | Current | P0 |
| M6.2 | 布局会自动切换吗？ | smart layout reaction video | Smart Layout Switching | Current | Features |
| M6.3 | 有自动字幕吗？ | auto captions reaction video | Captions / Kinetic Typography | Current | Features |
| M6.4 | 强反应能自动 zoom/震屏吗？ | reaction zoom shake effect | Reaction Close-Up / Shake 等 | Current | Demo |
| M6.5 | 竖屏 Shorts 字幕不会被挡吗？ | shorts safe zone captions | 平台专属字幕安全区尚未实现 | Opportunity | Blog |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | M6 哪些进 Tier 1 Hero；哪些仅 Conditional |
| **设计/MG** | Style Packs / 默认字幕样式；与 motion-graphics Status 同步 |

---

## M7 · 音频工程（Audio）

**模块说明**：人声 vs 原片 vs 音乐 vs SFX 的协调。

**对口部门**：产品（主）· 客户端

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M7.1 | 解说和原片能都听清吗？ | balance reaction voice source | Voice-Source Balance | Current | FAQ |
| M7.2 | 我说话时原片会自动变小声吗？ | audio ducking reaction video | Automatic Ducking | Current | Features |
| M7.3 | 能单独 mute 某段原片吗？ | mute source audio reaction | Source Audio Mute/Restore | Current | Movie Reaction |

---

## M8 · 长素材与 Shorts（Long-Form & Repurposing）

**模块说明**：数小时原片索引；长切短。

**对口部门**：AI/ML（主）· 产品

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M8.1 | 几小时的 movie/live 能剪吗？ | ai edit long reaction video | Long-Footage Indexing / Overview | Current（已确认可处理数小时素材） | P0 |
| M8.2 | 能从长视频做 Shorts/Reels/TikTok 吗？ | turn long reaction into shorts | 长视频自动生成 Shorts/Reels/TikTok 尚未实现 | Opportunity | P0 |
| M8.3 | 能自动分章节吗？ | ai video chapters | 目前不支持自动章节建议；语义分段信号仍为预留能力 | Opportunity（当前不支持） | Blog |

---

## M9 · 平台与导出（Platform & Export）

**模块说明**：16:9 / 9:16 / 1:1；导出预设。

**对口部门**：客户端（主）· 产品

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M9.1 | 支持 YouTube 横屏和 Shorts 竖屏吗？ | reaction video aspect ratio | 16:9 / 9:16 / 1:1 画布 | Current | Features |
| M9.2 | 有平台导出预设吗？ | export youtube tiktok preset | 支持分辨率、帧率、格式、编码器等通用导出设置；暂无平台专属预设 | Opportunity（平台预设） | FAQ |
| M9.3 | 同一项目能导出长片+多个 Shorts 吗？ | multi version export video | 开发中；目前不支持从同一项目批量导出长片和多个 Shorts，当前一次导出一个时间线版本 | 开发中 | 🔲 |

---

## M10 · 可编辑时间线与 AI 控制（Trust Core）

**模块说明**：Vatt 最大信任机制——AI 改完仍可手调、可 Undo、可看懂 AI 做了什么。

**对口部门**：产品（主）· 客户端

**Landing 核心句**：*understands footage · real edits · editable timeline*

### 用户决策路径

```
对比 Revid/生成器：剪完还能改吗？是一键黑盒吗？         → 路线之争 ★★★
  ↓
试用：AI 剪错了能撤销吗？                              → Undo
  ↓
深度：能用自然语言改某一截吗？                           → NL editing
  ↓
信任：能看到 AI 改了哪里吗？                              → History
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M10.1 | AI 剪完我还能手动改吗？ | editable ai timeline | 剪切/布局/字幕/音频均为可编辑对象 | Current | P0 ★ |
| M10.2 | 能撤销某次 AI 操作吗？ | undo ai video edits | Undo an AI Edit | Current | FAQ P0 |
| M10.3 | 是一键生成不能改的 AI 吗？ | ai video editor vs generator | 不是一键生成后不可修改；AI 完成初剪，人类可在时间线上继续编辑，体现人机协作 | ✅ 定位 | 对比页 P0 |
| M10.4 | 能用自然语言描述怎么剪吗？ | natural language video editing | Natural-Language Editing | Current | Demo |
| M10.5 | 能看到 AI 改了什么吗？ | ai edit history video | Editing History and Explanation | Current | 信任 |
| M10.6 | 能只让 AI 改选中一段吗？ | partial range ai edit | Partial-Range Editing | Current | FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | 首页 FAQ Q4「Manual edit?」官方答案是否与 M10 一致 |
| **客户端** | NL editing 已确认 Current；Preview Before Commitment roadmap |

---

## M11 · 版权意识剪辑（Movie Reaction）

**模块说明**：Commentary-first 剪辑——减少无评论连续原片；**不是** Fair Use 保证。

**对口部门**：产品（主）· **合规/法务**

**Required Disclaimer（对外必须保留）**

> Vatt can automate commentary-first editing and help creators review source usage, but it cannot determine fair use or guarantee monetisation, claim-free publishing, or freedom from takedowns.

### 用户决策路径

```
Movie 创作者：能帮我少播原片、多留解说吗？              → Commentary-first
  ↓
顾虑：会不会保证不 copyright strike？                   → **绝不能承诺** → Claims 禁令
  ↓
导出前：能看到用了多少原片吗？                            → Source-Usage Overview
```

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M11.1 | 能做 commentary-first movie reaction 吗？ | commentary first movie reaction | AI Commentary-First Edit | Current | Blog P0 |
| M11.2 | 能保证 fair use / 不被 claim 吗？ | fair use reaction video ai | **不能保证**；见 Required Disclaimer | Claim-Restricted（永久合规边界） | FAQ 必写 |
| M11.3 | 能看成片里用了多少原片吗？ | source usage review video | Source-Usage Overview | Current | 教育文 |
| M11.4 | 能做 source-free watch-along 吗？ | watch along without video | Source-Free Watch-Along | Current | 不得写「绝对安全」 |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **合规** | M11 全部对外句式审阅；与 features §6 Claims 禁令同步 |
| **产品** | Movie Reaction Stack 哪些 Opportunity 改 Conditional/Current |

---

## M12 · 评论与社群（Comments）

**模块说明**：YouTube 评论导入、回应结构——当前多为 Opportunity。

**对口部门**：产品 · 增长

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M12.1 | 能导入 YouTube 评论做回应视频吗？ | youtube comment reaction video | 目前不支持 YouTube 评论导入 | Opportunity（已确认未实现） | Blog |
| M12.2 | 能自动排「展示评论→回应」结构吗？ | comment reply video editor | 目前不支持自动生成「展示评论→回应」结构 | Opportunity（已确认未实现） | 路线图 |

---

## M13 · 信任与获取（Trust & Access）

**模块说明**：邀请制、定价、credits、隐私政策可访问性——用户决策最后一环。

**对口部门**：增长（主）· 合规 · 产品

### 用户问题表

| # | 用户问题 | 搜索词 | Vatt 答案 | Status | 营销 |
|---|---------|--------|----------|--------|------|
| M13.1 | 免费吗？怎么收费？ | vatt pricing | 提供 Free Trial；采用分阶梯收费模式 | Current（具体价格以 `/pricing` 为准） | `/pricing` |
| M13.2 | 需要邀请码吗？ | vatt invite code | 邀请制 | ✅ 站点 | 首页 CTA |
| M13.3 | 是纯 Web 还是要下载？ | vatt desktop editor | macOS / Windows 桌面编辑器，需下载安装 | ✅ | FAQ |
| M13.4 | 比 Descript / Revid 好在哪？ | vatt vs descript, vs revid | 显著差异在于专为 Reaction 设计：Source-vs-Creator 角色识别、反应高光与情绪峰值排序、Hook 建议、Smart Layout、Reaction Close-Up / Shake、Commentary-First、Auto Duck、Source-Usage Overview、Source-Free Watch-Along，以及 AI 初剪后仍可由人类继续编辑的时间线 | ✅ 定位（描述差异，不宣称绝对更好） | 对比页 P0 |
| M13.5 | 数据隐私政策在哪？ | vatt privacy | 已上线：[vatt.ai/privacy](https://vatt.ai/privacy) | ✅ 站点 | Privacy / 信任 |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **增长** | 定价页完整套餐与 credits 规则（动态加载内容固化） |
| **合规** | Privacy 已上线；确认 Terms 状态与 URL |
| **产品** | 「10x faster」「first AI reaction editor」有无可引用方法论 |

---

## 附录 A · 全局用户决策路径（Landing 叙事顺序）

```
1. 这是什么？（AI reaction editor，不是 generator）     → M10, M13
2. 省什么事？（同步、找高光、删 dead air）               → M3, M5, M4
3. 我还能控制吗？（可编辑时间线、Undo）                 → M10
4. 出片包装？（Layout、字幕、Shorts）                   → M6, M9
5. Movie 创作者？（commentary-first，不承诺 fair use）  → M11
6. 多少钱？怎么进？                                     → M13
```

---

## 附录 B · 分部门汇总问卷（一次发一个部门）

### 发给「产品」

- M1 M1.3–M1.4 已确认 Current，补充浏览器/权限细节；M4 粗剪默认行为  
- M5/M6 Tier 1 哪些可写进 Hero  
- M10 FAQ 与定位一致性；M11 Movie stack Status  
- M13 对比 Revid/Descript 官方话术  

### 发给「AI/ML」

- M2 最长 3 小时（已确认）与分析依赖；M3 同步失败 fallback  
- M5 highlight 检测范围与 Conditional 条件  
- M8 长切短 pipeline  

### 发给「Web 客户端 / 工程」

- M1 录制浏览器/OS 支持；M9 导出格式清单  
- M10 NL editing 已确认 Current、Partial-Range 实际上线状态  

### 发给「设计 / MG」

- M6 与 [motion-graphics](./vatt-motion-graphics.md) Status 同步  
- 默认 Layout / 字幕 Style 对外展示  

### 发给「合规 / 法务」

- M11 全部对外表述 + features §6 Claims 禁令  
- M13 Privacy 已上线；Terms 状态待确认；copyright 教育文边界  

### 发给「增长」

- M13 定价、credits、邀请策略  
- 首页 FAQ 四条是否更新为 capabilities 真源  

---

## 附录 C · 营销内容索引

| 内容 | 优先模块 |
|------|---------|
| 待建 `/features` | M1–M10 Tier 1 |
| 首页 FAQ 扩充 | M10.1–3, M13.1–2, M5.1, M3.1 |
| Blog P0 | M11 教育、M10 vs generator、M5 highlight |
| 对比页 | M13.4 vs Revid / Descript / Kapwing |
| Movie Reaction 专题 | M11 + MG Commentary 布局 |

---

## 附录 D · 与旧文档关系（去重说明）

| 文档 | 职责 | 本文关系 |
|------|------|---------|
| **[vatt-features.md](./vatt-features.md)** | Feature Universe 审计真源（§3 详表 + Status + Claims 禁令） | capabilities **不重复** §3 全表；迁移为用户问题 + 问甲方清单 |
| **[vatt-motion-graphics.md](./vatt-motion-graphics.md)** | MG 唯一详表 | M6 只保留用户问题入口 |
| **vatt-use-cases.md** | Persona / 场景 | 不写场景，只写能力 |
| **vatt-keywords.md** | SEO 词 | 用户问题表引用 |

**维护规则**：Status 变更以 features / motion-graphics 为准，capabilities 同步用户问题表的 Status 列。

---

## 附录 E · P0 问甲方清单（阻塞 `/features` 与对比页）

| # | 模块 | 问题 |
|---|------|------|
| 1 | M3 | Source/Facecam 对齐：Current（需主动触发 Audio Align）；多机位批量同步仍为开发中 |
| 2 | M5 | Reaction Highlight：已确认 Current |
| 3 | M10 | Editable Timeline + Undo + NL editing：已确认 Current |
| 4 | M2 | 最长 3 小时（已确认）/ credits 消耗规则 |
| 5 | M1 | 系统音频 + Multi-Source 录制：已确认 Current；补充支持的浏览器 |
| 6 | M6 | Tier 1 Layout/Captions 哪些 Current 可上 Hero |
| 7 | M13 | 已确认 Free Trial + 阶梯收费；具体档位、价格及 credits 规则待固化；Privacy 已上线；Terms 状态待确认 |
| 8 | M11 | Movie Reaction 栈（Commentary-First / Source-Usage / Watch-Along）已确认 Current |
| 9 | 全局 | 「10x faster」「first AI reaction editor」可否继续用 |

---

## 关于本文档

**文档思路**（内容层）：按**用户真正会问、会搜的问题**写 Landing / Blog / FAQ——每条能力 = **用户问题 → 搜索词 → Vatt 答案** → **内容怎么用**。

**文档结构**（收集层）：外层按产品模块 M1–M13 **分部门询问**；模块内嵌用户决策路径；Status 与 [vatt-features.md](./vatt-features.md) 真源对齐。

**范围**：首页 / 待建 Features / Blog / 对比页 / FAQ；场景 → [use-cases](./vatt-use-cases.md)。

*Last updated: 2026-08-26（团队审阅同步）*

*关联：[vatt.md](./vatt.md) | [vatt-features.md](./vatt-features.md) | [vatt-motion-graphics.md](./vatt-motion-graphics.md) | [vatt-keywords.md](./vatt-keywords.md) | [vatt-competitors.md](./vatt-competitors.md)*
