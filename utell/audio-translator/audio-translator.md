# Audio Translator — 产品文档

> **文档边界**：Audio Translator 产品专项文档。Accent Converter 实时场景见上级 [utell.md](../utell.md) 体系。
>
> **上级文档**：[utell.md](../utell.md) — Utell 产品矩阵总览
>
> **状态**：框架已建立，等待用户提供内容后填充。

**关联**：[utell.md](../utell.md) | [audio-translator-scenarios.md](./audio-translator-scenarios.md) | [audio-translator-page-template-zh.md](./audio-translator-page-template-zh.md) | [utell-keywords.md](../utell-keywords.md) | [utell-use-cases.md](../utell-use-cases.md) | [utell-features.md](../utell-features.md) | [utell-competitors.md](../utell-competitors.md)

**Last updated**: 2026-05-11

---

## 一、产品概览

| 项目 | 内容 |
|------|------|
| 产品名 | Utell Audio Translator |
| URL | https://utell.ai/audio-translator |
| 产品形态 | 桌面软件（macOS、Windows）中的独立功能模块 |
| 当前阶段 | 预发布（Request Demo 获取体验） |
| 一句话定位 | 后制音频的口音优化工具——上传已录制音频，AI 转写并降低口音、提升英语清晰度，保留原声 |

---

## 二、与 Accent Converter 的差异

这是 Utell 产品矩阵中最关键的区分——两者解决不同场景的问题。

| 维度 | Accent Converter | Audio Translator |
|------|-----------------|------------------|
| **处理时机** | 实时（通话/直播进行中） | 后制（录制完成后） |
| **输入** | 麦克风实时音频流 | 已录制的音频文件 |
| **输出** | 实时处理后的音频流 | 处理后的新音频文件 + 转写文本 |
| **延迟要求** | <100ms（超低延迟） | 无实时性要求 |
| **核心场景** | 在线会议、直播、游戏语音、通话 | 播客后期、AI 短剧配音、课程录制、视频配音 |
| **用户心智** | "通话时别人听清我" | "让录制内容听起来更清晰" |
| **竞品对标** | Krisp、Dubbing AI（实时变声） | Descript、Adobe Podcast（音频后制 AI） |

---

## 三、目标受众 / ICP

| Persona | 场景 | 痛点 |
|---------|------|------|
| **AI 短剧创作者** | 微短剧出海，配音/原声需英语清晰化 | 母语配音成本高、周期长；需保留演员原声 |
| **播客 / 内容创作者** | 录制播客、视频内容，非母语英语 | 后期降口音费时；不想改变音色 |
| **教育内容制作者** | 录制在线课程、培训视频 | 学生听不清口音影响学习效果 |
| **企业培训团队** | 内部培训视频、全球化团队沟通 | 讲师口音影响多地区团队理解 |
| **YouTuber / 视频创作者** | 英语频道内容制作 | 非母语口音影响观众留存 |

---

## 四、核心能力（待用户补充）

| 能力 | 说明 | 状态 |
|------|------|:--:|
| **音频口音转换** | 上传音频 → AI 分析口音 → 降低口音、提升清晰度、保留原声 → 输出新音频 | 待确认 |
| **转写（Transcription）** | 音频 → 文本 | 待确认 |
| **批量处理** | 多文件排队处理 | 待确认 |
| **格式支持** | 输入/输出音频格式 | 待确认 |

---

## 五、当前待办

| P | 待办 |
|:--:|------|
| **0** | 用户提供 Audio Translator 实际产品信息（功能边界、格式、工作流等） |
| **1** | 根据用户提供的材料，填充本文内容 |
| **1** | 评估是否需要拆出独立的关键词/场景/功能文档 |

---

## 六、参见

- **子页面场景规划**：[audio-translator-scenarios.md](./audio-translator-scenarios.md) — 12 个文件上传型场景、竞品验证、优先级排序
- **上级入口**：[utell.md](../utell.md)
- **功能详情**：[utell-features.md](../utell-features.md)
- **使用场景**：[utell-use-cases.md](../utell-use-cases.md)
- **关键词**：[utell-keywords.md](../utell-keywords.md)
- **竞品分析**：[utell-competitors.md](../utell-competitors.md)
- **增长策略**：[utell-growth-strategy.md](../utell-growth-strategy.md)

---

*文档创建日期：2026-05-11 | 等待用户内容填充*
