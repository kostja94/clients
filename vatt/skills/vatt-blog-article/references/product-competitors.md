# Vatt — Product & Competitors Reference

> 加载时机：Phase 0R（R1）· Phase 4（Draft 对比文）
> 主文件：SKILL.md §1 速查

---

## 1. 产品事实（创作可用）

**One-line**：
> Vatt is an AI video editor that understands footage, performs real edits, and keeps every result adjustable on an editable timeline. Built for reaction creators: understand long footage, find the moments that matter, organise source and face-cam recordings, shape layouts around the conversation, and keep every AI edit under control.

**官网 Highlight（vatt.ai 2026-08-14 抓取，P1 来源）**：

| 能力 | 说明 |
|------|------|
| **Reaction Recognition** | 读 speech、pauses、faces、sound cues，定位反应开始/构建/峰值时刻 |
| **Smart Layout** | 跟随说话者与反应峰值，将每个来源构图为随时刻移动的可编辑布局 |
| **ReAmp（Reaction Amplification）** | 选中素材中的某时刻，放大其视觉冲击，结果仍可继续编辑 |
| **Record + Edit** | 录屏/摄像头/麦克风/系统音频，同一工作流内继续编辑 |
| **Multi-source Auto Sync** | 多源素材自动对齐到一条共享时间线 |
| **AI Hook Generation / Creative Effects / AI Creative Finishing / AI Captioning** | 结构、包装、收尾、字幕 |
| **Automated Rights & Compliance** | 版权合规自动化辅助（**不作 Fair Use 保证**） |
| **Bad-Take Detection & Removal** | 失败镜头检测与移除 |
| **Agent-Callable Editing** | Codex / Claude Code / OpenClaw 可调用编辑（"视频编辑领域的 Cursor"叙事） |

**产品形态**：Desktop app（macOS 14+ / Windows 64-bit）· 邀请制早期 · "Get started for free"。

**营销原文归档**：官网标语 "World 1ST AI Editor for Reaction Videos" —— 无品类证据时**不得**作为产品事实承诺（G3/G5）。

**Reaction 场景定位**：真人 reaction 编辑（非 AI 虚拟人生成、非固定双画面拼接）。

**Beachhead Tier 1 能力**：

| 能力 | 说明 | Status |
|------|------|--------|
| **Long-Footage Understanding** | 数小时原片 + Reaction 录制整理成可检索时间线地图 | Conditional |
| **Reaction Highlight Detection** | 自动找出大笑、惊讶、震惊、兴奋等强 Reaction 时刻 | Conditional |
| **Source and Facecam Sync** | 按音频/时间线索对齐原片与 Face-Cam | Conditional |
| **Dead Air and Rough-Cut Cleanup** | 清理静音/空录，生成可编辑粗剪（"remove dead air without flattening the reaction"） | Conditional |
| **Editable AI Timeline** | AI 生成的剪切/布局/字幕/音频/效果均为可编辑时间线对象 | **Current** |
| **Manual Refinement and Undo** | AI 之后可手调；可 Undo 某次 AI 编辑 | **Current** |

**Feature Status 语义**（写作前必读，G5 对照）：
| Status | 含义 |
|--------|------|
| **Current** | 有当前产品证据；可作能力描述 |
| **Conditional** | 能力存在，但依赖登录、云服务、credits、权限、硬件、素材质量或分析完成——写作须加限定 |
| **Opportunity** | 已验证需求或方向；**不得写成已上线** |
| **Claim-Restricted** | 话题可作教育，不得承诺法律/平台/质量/性能保证 |

**官方任务流**：Record/Import → Understand → Sync & Organise → Rough Cut → Find Reactions & Hooks → Layout → Amplify Emotion → Captions/Audio/GFX → Adapt for Platform → Review on Timeline → Export

**画布/平台**：16:9 YouTube Long-Form · 9:16 Shorts/TikTok/Reels · 1:1 Square · Export Presets 按平台预设

**关键指标**：无已验证量化承诺（"10x faster" / "first AI editor" 为营销原文，无方法论证据不作产品事实）。

**定价**（as of Aug 2026，**待验证**）：Free 一次性 credits；Starter/Pro/Team 具体价格动态加载——写作**勿写死具体数字**，可用品类参考区间并标注 "pricing not yet public"。

**访问模式**：邀请制（Enter invite code）。CTA 指向 https://vatt.ai/（邀请码入口 / 登录）。

**案例客户**：无公开（不得虚构）。

---

## 2. 竞品矩阵

| 竞品 | 类型 | 优势（写作必须承认） | 限制 | 参考 URL |
|------|------|---------------------|------|---------|
| **Sparki** | AI 视频剪辑 Agent | 同赛道 Agentic AI；多品类覆盖（解说/访谈/Vlog/蒙太奇）；A 轮数百万美元（BAI 领投） | 泛品类覆盖，非 Reaction 垂直专精 | sparki.cc（待验证） |
| **Nemo Video** | AI 视频编辑 Agent | 爆款仿剪、电商带货方向；"高产低预算" | 非 Reaction 情感编辑方向 | nemovideo.com（待验证） |
| **Revid.ai** | AI reaction 生成器 | 无需真人出镜；AI avatar + 脚本快速出片（~5 分钟）；低门槛；Free plan + Hobby ~$39/月 | 虚拟人缺真实感；faceless 受众；编辑限于裁剪/字幕/音乐 | revid.ai |
| **Creatify** | AI reaction maker | URL→视频、800+ avatar、140+ 语音、A/B test 仪表盘；Starter ~$33/月 | 偏营销素材生成，非真人素材编辑 | creatify.ai |
| **Medeo** | AI reaction 生成器 | AI avatar 反应 + 分屏 + 动态字幕；快速从趋势到出片 | 同 Revid 路线；非真人编辑 | medeo.app |
| **VClip** | AI avatar 分屏生成器 | 语言自动检测；脚本/voiceover/B-roll 自动；faceless 快速起量 | 无真人素材编辑能力 | getvclip.com |
| **ReactionMaker** | 免费双画面工具 | 浏览器端免费、无 watermark、无登录；快速 split-screen | 无 AI 理解/高光检测/时间线智能 | reactionmaker.com |
| **VEED.IO** | 通用在线编辑器 | 通用编辑能力强；Magic Cut AI 裁剪；模板/字幕/协作丰富 | 非 Reaction 专属；无长素材情感理解 | veed.io |
| **CapCut** | 免费/轻量视频编辑器 | 免费主力；移动端普及；模板/字幕/特效丰富；上手极快；2026 短形式默认工具 | 无 Reaction 专属理解；长素材高光检测有限；专业控制弱 | capcut.com |
| **Descript** | 通用 AI 编辑器 | 文本编辑视频；去口癖强；播客+视频双覆盖；reaction/访谈被官方列为适用场景；品牌知名 | 无 Reaction 专属情感高光检测；偏转录工作流 | descript.com |
| **Adobe Premiere Pro** | 专业 NLE | 全功能专业编辑；行业标准；插件生态；多机位同步强（reaction 频道主推荐）；~63% YouTuber 使用 | 手动找高光耗时；学习曲线陡；订阅价高 | adobe.com/products/premiere |
| **DaVinci Resolve** | 专业 NLE | 免费版功能强（调色/剪辑/音频）；专业调色标杆；无订阅；~58% YouTuber 使用 | 手动 workflow；Reaction 无 AI 高光检测 | blackmagicdesign.com/products/davinciresolve |
| **Final Cut Pro** | 专业 NLE（Mac） | 磁性时间线整理快；Mac 原生；一次性买断 | Mac only；无 Reaction AI 智能 | apple.com/final-cut-pro |
| **Cutsio** | AI 预剪辑（rough-cut） | 自动静音删除/找时刻/最佳 take；导出可编辑时间线到 NLE（XML） | 通用 rough-cut；非 Reaction 垂直；web 工具 | cutsio.com |
| **Eddie AI** | AI 助理剪辑 | 专业访谈/叙事 rough cut；导出到 Premiere/FCP/Resolve；50K+ 编辑使用 | 偏访谈/纪录片；非 Reaction 垂直 | heyeddie.ai |
| **Pyromi** | AI 编辑器（时间线） | 描述式搜素材 + 生成可编辑时间线；每刀可改 | 通用；非 Reaction 情感垂直 | pyromi.com |
| **ChatCut** | 浏览器 AI 编辑器 | 文本式编辑；prompt 驱动找强时刻；跨机器项目 | 偏 talking-head/访谈；非 Reaction 垂直 | chatcut.io |

> 价格均标注 "as of Aug 2026，多来源存在出入，写作勿写死精确数字，用 from/roughly + 待验证"。

**纯编辑器分层（2026-08 调研）**：
| 层级 | 工具 | 创作者实际使用情况 |
|------|------|-------------------|
| 专业 NLE | Premiere Pro / DaVinci Resolve / Final Cut Pro | 长形式 + 多机位同步主力；高光靠手动 |
| 轻量/短形式 | CapCut / iMovie / Clipchamp | 短形式默认；模板快、无长素材智能 |
| AI 转录式 | Descript / Vozo | 文本编辑；reaction/访谈适用；无反应识别 |
| AI 预剪辑 | Cutsio / Eddie AI / Pyromi / ChatCut | 自动 rough cut + 导出可编辑时间线到 NLE；通用非 Reaction 垂直 |

> 数据源：ChatCut/clixie 2026 调研、IntelligentHQ/perplexitymagazine 2026 对比、iqyic 2024 调查（Premiere 63% / Resolve 58% / FCP 22% / CapCut 32%）。

### 对比表模板（Comparison/Alternative 使用）

```
| 特性 | Vatt | {竞品1} | {竞品2} |
|------|--------|---------|---------|
| 理解长素材（Long-Footage Understanding） | ✅ | | |
| 自动高光检测（Reaction Highlight Detection） | ✅ | | |
| 原片 + Face-Cam 同步 | ✅ | | |
| 可编辑 AI 时间线 | ✅ | | |
| 真人出镜编辑（vs 虚拟人生成） | ✅ | | |
| 真人情感保真 | ✅ | | |
| 免费层 | Free credits | | |
```

---

## 3. 竞品公平描写规则

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势（非敷衍） | 从 §2 竞品矩阵优势列取 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" / "basically just" |
| 对比表无二元化 | 不把需要 nuance 的能力简化为 Yes/No；如有简化加脚注 |
| ≥1 场景推荐非 Vatt 方案 | 写在正文，非脚注（例：faceless 创作者 → Revid/生成器更合适） |

**Editor vs Generator 路线之争**：客观呈现两条路线（真人编辑 vs AI 虚拟人生成），Vatt 代表"编辑路线"，不做"生成器都是垃圾"式贬低。

---

## 4. 产品能力边界（G5 对照）

| 可声称 | 须限定 |
|--------|--------|
| Editable AI Timeline / Manual Refinement / Undo | Current——可直接描述 |
| 长素材理解、高光检测、同步、粗剪清理 | Conditional——依赖登录/云服务/credits/素材质量，写作加限定（"when processing on Vatt's servers"、"depends on your footage"） |
| 多画布 16:9 / 9:16 / 1:1 + Export Presets | Current |
| Long-to-Short Repurposing | Current |
| 官方 11 步任务流 | 描述为产品工作流 |
| Motion Graphics（Layout/字幕/花字/动效） | 见 vatt-motion-graphics.md（MG 是独立能力域） |

**不可声称**（G5 红线）：
- Opportunity 级能力写成已上线（如 AI Commentary-First Edit、Source Burst Planner 等版权意识功能均为 Opportunity）
- 无证据的 "10x faster" / "first AI editor" 作事实承诺
- 具体套餐价格（待验证）
- 虚构客户案例
- 任何版权保证（见 §6）

---

## 5. 版权敏感区（Movie Reaction / Copyright-Conscious Stack）

**原则**：*Reduce unnecessary source exposure. Increase original commentary. Keep every automated choice reviewable.*

| 可写（教育性） | 不可写（G8 禁令） |
|----------------|------------------|
| 描述 commentary-first 编辑、short source bursts、creator cutaways 等手法 | "Vatt guarantees fair use." |
| 提示创作者注意 Content ID / Reused Content 政策 | "Vatt prevents copyright claims or strikes." |
| 说明可审阅的版权检查流程 | "Vatt bypasses Content ID." |
| 引用权威版权教育资源 | "Clips under N seconds are automatically safe." |
| 注明版权声明（Reaction 内容受版权法影响） | "Mirroring/cropping/blurring/speed/pitch makes footage legal." |
| | "Vatt can determine whether an edit qualifies as fair use." |
| | "Any reaction video becomes monetisable." |

**Required Disclaimer（涉及 Movie Reaction 版权话题时正文必须保留英文）**：
> Vatt can automate commentary-first editing and help creators review source usage, but it cannot determine fair use or guarantee monetisation, claim-free publishing, or freedom from takedowns.

---

## 6. Claims Must Not Publish（对外禁令全文）

以下英文句式**不得作为对外产品承诺**发布：

- "Vatt guarantees fair use."
- "Vatt prevents copyright claims or strikes."
- "Vatt bypasses Content ID."
- "Clips under a specific number of seconds are automatically safe."
- "Mirroring, cropping, blurring, speeding up, or changing pitch makes copyrighted footage legal."
- "Vatt can determine whether an edit qualifies as fair use."
- "Any reaction video becomes monetisable."
- "Vatt automatically creates a perfect finished video."
- "Vatt understands every emotion with 100% accuracy."
- "All processing stays local."
- "Every feature works on every operating system."
- "Vatt is 10x faster,"（无已发布方法论或证据时）
- "Vatt is the first AI reaction editor,"（无站得住的品类证据时）

站点 FAQ / Slogan 中的 "10x" / "first" 仅作营销原文归档；写作时如需引用须标注为站点声称，而非验证事实。

---

*product-competitors · v2.0.0 · 2026-07-06 · vatt 定制 2026-08-14*
