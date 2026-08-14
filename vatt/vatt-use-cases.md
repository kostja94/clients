# Vatt — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[vatt.md](./vatt.md) | [vatt-features.md](./vatt-features.md) | [vatt-keywords.md](./vatt-keywords.md)

**Last updated**: 2026-07-24（JTBD 对齐官方 Feature 名）

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Casey — TikTok Reaction 创作者** | 单人创作者，日更 reaction 内容 | 拍摄 30 分钟素材 → 手动回看找反应点 2 小时 → 粗剪 1 小时 → 花 3-4 小时才出 3 分钟片子；跟不上热点节奏 | 10 倍速出片，追热点当天发布 | 中（会用剪辑软件） |
| **Sam — Try Not to Laugh 频道主** | Shorts/长视频搞笑 reaction 合集 | 一次录 30 分钟 Try Not to Laugh，笑点密集但手动找峰值极耗时间；需从一条素材拆 5+ Shorts | 自动检测爆笑瞬间，批量出 Shorts | 中 |
| **Jordan — YouTube Reaction 频道主** | 有固定 reaction 选题的 YouTuber | 每周 3 期 reaction 视频，每期素材 40-60 分钟，剪辑占满周末；积累了大量未剪辑素材 | 批量处理积压素材，提升周产量 | 中–高 |
| **Dana — Live Reaction 主播** | Twitch/YouTube Live 首映/赛事 reaction | 直播 2 小时，下播后要从冗长素材里剪 highlights 和 Shorts，常常拖到第二天 | 下播即出精华 clip | 中–高 |
| **Riley — 内容团队编辑** | reaction 频道的专职剪辑师 | 老板要求多出片子但剪辑时间有限；人工找反应点容易漏掉精彩片段 | AI 先粗筛，自己精修，"人机协作"提效 | 高 |
| **Morgan — 刚起步的 reaction 创作者** | 想做 reaction 但被剪辑劝退 | 不知道怎么剪辑、不知道哪些瞬间值得保留、剪出来的片子节奏差 | 让 AI 帮我找到好瞬间并自动排好，我只需确认和微调 | 低 |
| **Alex — 多平台分发创作者** | TikTok + YouTube + IG 同时更新 | 同一个 reaction 视频要裁剪成不同比例/时长适配不同平台 | 一次粗剪，快速导出多平台版本 | 中 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Casey | 看完一个爆款视频，立刻录了 25 分钟 reaction | 马上导入素材，AI 找到强反应时刻并生成**可编辑**粗剪 | Reaction Highlight Detection + Rough Cut from a Prompt | ai reaction video editor |
| Sam | 录了一期 35 分钟 Try Not to Laugh 合集 | AI 标出爆笑峰值，我选 5 段导出 Shorts | Emotional Peak Ranking + Long-to-Short Repurposing | try not to laugh |
| Dana | 专辑 premiere 直播了 2 小时 | 下播后用长素材索引找 peak，出 Shorts + highlights | Long-Footage Overview + Vertical Highlight Cut | live reaction |
| Casey | 粗剪里有 2 段我觉得不够好 | 在时间线上调整起止点 / Undo AI / 局部再编辑 | Manual Refinement + Undo an AI Edit + Partial-Range Editing | reaction video trimming |
| Jordan | 周末要处理 3 条 reaction 视频的素材 | 批量导入，分别理解/粗剪，再统一精修 | Batch Media Import + Editable AI Timeline | batch video editing ai |
| Jordan | 上个月录的某个素材里有段反应想拿出来用 | 用语义搜索或时间线地图定位片段 | Semantic Footage Search / Long-Footage Overview | reaction footage organizer |
| Riley | 老板说这期要多加点字幕和特效 | 粗剪节奏定好 → Captions / Word Art / ReAmp → 或导出精修 | Automatic Captions + Reaction Word Art | ai rough cut reaction |
| Morgan | 第一次录 reaction，不知道哪些片段值得保留 | AI 标出候选高光，我在时间线上 Keep/Skip 式审阅 | Reaction Timeline Markers + Manual Refinement | ai find best reaction moments |
| Morgan | 担心 AI 剪的不好 | 每个 AI 结果都是可编辑对象，可 Undo | Editable AI Timeline | ai video editor not replacing |
| Alex | 同一个 reaction 要发 TikTok (9:16) 和 YouTube (16:9) | 多画布 + 竖屏高光切 + Export Presets | 9:16 Vertical Canvas + Vertical Highlight Cut | reaction video for tiktok and youtube |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| Try Not to Laugh 出 Shorts | Sam | 笑点检测 + 多 clip | try not to laugh | `/blog/try-not-to-laugh-reaction-videos` |
| Live 下播出 highlights | Dana | 长素材峰值提取 | live reaction | `/blog/live-reaction-videos-guide` |
| 单人快速出片 | Casey | AI 高光 + 粗剪 + 微调 | ai reaction video editor | 首页 / 待建 Features |
| 批量处理积压素材 | Jordan | 高光检测 + 媒体库 | batch reaction video editing | 待建 Features |
| 团队人力提效 | Riley | 粗剪→人工精修 | ai assisted video editing | 待建 Features |
| 零基础入门 | Morgan | AI 高光 + 自动编排 | ai auto edit reaction video | 首页 |
| 多平台分发 | Alex | 粗剪→多比例导出 | reaction video multi platform | 待建 Features |

---

## 4. 用户旅程

```
认知：Google「ai video editor」· TikTok 创作者圈推荐 · YouTube 剪辑教程
  ↓
考虑：vatt.ai 首页 → FAQ 了解能力 → 看到 "10x faster" 价值主张
  ↓
获取：输入邀请码 → 创建账户 → 进入编辑器
  ↓
首次使用：上传第一条 reaction 素材 → AI 自动处理（数分钟）
  → 看到 AI 标注的情感高光 → 惊叹"这确实是我想保留的瞬间"
  ↓
习惯形成：每次录完 reaction → 丢给 Vatt → 粗剪 → 微调 → 发布
  ↓
升级：免费 credits 用完 → 订阅 Starter/Pro → 素材积累 → Team 套餐
```

### 关键转化节点

| 节点 | 动作 | 转化目标 |
|------|------|---------|
| 首页 → 注册 | 输入邀请码 | 账户创建 |
| 首次上传 → Wow Moment | AI 成功识别情感高光 | 产品价值验证 |
| 免费用完 → 订阅 | Credits 耗尽，依赖已形成 | 付费转化 |
| 单人 → 团队 | 团队协作需求出现 | Team 套餐升级 |

---

## 5. 未覆盖场景

| 场景 | 机会 | 关键词需求 |
|------|------|-----------|
| **Try Not to Laugh 合集** | 密集笑点检测，一录多 Shorts | try not to laugh reaction editing |
| **直播 reaction** | 直播录制素材自动找高光，下播即出精华片段 | live reaction highlight ai · **P0** |
| **多人 reaction** | 多人同时反应同一内容（沙发 reaction），AI 区分多面孔情感 | multi person reaction video ai |
| **影视/剧集 reaction** | 整集电视剧/电影 reaction，超长素材的章节化高光检测 | movie reaction video editor |
| **游戏 reaction** | 游戏实况 reaction，AI 识别游戏内高光+玩家反应叠加 | gaming reaction video ai |
| **品牌/商务 reaction** | 品牌委托 reaction 创作者，快速出片满足甲方需求 | sponsored reaction video editor |
| **字幕/特效集成** | 内置字幕自动生成 + reaction 专属特效模板 | reaction video captions ai |

---

*来源：[vatt.ai](https://vatt.ai/) FAQ + [vatt-reaction-video-types.md](./vatt-reaction-video-types.md) 2026-07-23*
