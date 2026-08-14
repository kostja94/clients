# VOMO — Product & Competitors Reference

> 加载时机：Phase 0R（R1）· Phase 4（Draft 对比文）
> 主文件：SKILL.md §1 速查

---

## 1. 产品事实（创作可用）

**One-line**：
> VOMO is an AI meeting notes and audio transcription tool — record, upload, or paste a YouTube link, and get a transcript, smart notes, and action items. Bot-free: no AI joins your calls.

**四大核心能力**：

| 能力 | 说明 | 关键数据 |
|------|------|---------|
| **AI Transcription** | 双引擎 ASR（OpenAI Whisper + Nova-2/Deepgram） | 95–99% 准确率、90+ 语言 |
| **Smart Notes** | 自动摘要、关键要点、行动项（含负责人）、章节、决策 | 忠实对话，不编造 |
| **Ask AI** | GPT-4o 对话式问答转录内容（无限使用） | 自然语言查询 |
| **VOMO CLI** | 转录/笔记拉取到 AI Agent 工作流（Claude Code, Codex, OpenCode） | 竞品首创 |

**输入方式**：实时录音 · 文件上传（MP3/WAV/M4A/MP4 等，最多 10 个）· 粘贴 YouTube 链接

**其他功能**：说话人识别+时间戳 · 多格式导出（TXT/DOCX/PDF/SRT/HTML）· 公开分享链接 · 会议模板（团队/站立/销售/面试/播客）· 笔记编辑 · 工具转换集

**三步工作流**：Record → Transcribe → Extract（Smart Notes / Ask AI）

**关键指标**：
- 400K+ 用户（PR Newswire 2026-07）
- 转录 1,000,000+ 小时（官网）
- 95–99% 准确率（官网 + 第三方评测）
- 90+ 语言（官网）
- App Store 4.4★ / 347 评分（2026-07）
- Product Hunt #2 Product of the Day（官网）
- 处理速度 ~15 分钟/1 小时音频（用户评测）

**定价**（as of July 2026）：
- Free：$0（30 分钟/周）
- Pro：$1.92/周（≈$8.32/月，年付省 75%；无限制转录、3 小时/文件）

**对比价格锚点**（写定价对比时用）：
- Otter.ai Pro：$16.99/月
- Fireflies：$10/月起
- Descript：$24/月起

**Hero 叙事**："No credit card required · Free daily credits"

**用户评价引用**："saves me hours of post-meeting documentation"

---

## 2. 竞品矩阵

| 竞品 | 类型 | 优势（写作必须承认） | 限制 | 参考 URL |
|------|------|---------------------|------|---------|
| **Otter.ai** | 实时会议转录 | 实时字幕专利、品牌知名度最高、教育市场渗透深、团队协作成熟 | Bot 加入会议、嘈杂环境准确率波动（评测 ~85%）、免费额度 300 分钟/月、价格 $16.99/月 | otter.ai |
| **Fireflies.ai** | 会议智能平台 | 集成生态最丰富（50+）、CRM 集成（Salesforce/HubSpot）、情感/参与度分析 | Bot 加入、配置复杂、YouTube 转录弱 | fireflies.ai |
| **Descript** | 音视频编辑+转录 | 文字编辑音视频独一无二、Overdub AI 配音、5M+ 用户 | 转录是附属功能、价格高（$24/月）、面向创作者 | descript.com |
| **Granola** | Bot-free 会议笔记 | 同为 Bot-free 定位、对隐私敏感用户友好 | 功能范围窄、品牌知名度低 | granola.ai |
| **Fathom** | AI 会议笔记 | 销售场景聚焦、CRM 集成、要点高亮 | Bot 加入、CRM 集成用 Bot | fathom.video |

### 对比表模板（Comparison/Alternative 使用）

```
| 特性 | VOMO | {竞品1} | {竞品2} |
|------|--------|---------|---------|
| Bot-free 录音 | ✅ | | |
| 双引擎 ASR 准确率 | 95–99% | | |
| Ask AI 对话式查询 | ✅ | | |
| YouTube 链接转录 | ✅ | | |
| 免费层 | 30 分钟/周 | | |
| 最低付费 | $1.92/周 | | |
```

---

## 3. 竞品公平描写规则

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势（非敷衍） | 从 §2 竞品矩阵优势列取 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" / "basically just" |
| 对比表无二元化 | 不把需要 nuance 的能力简化为 Yes/No；如有简化加脚注 |
| ≥1 场景推荐非 VOMO 方案 | 写在正文，非脚注（如团队协作 → Otter/Fireflies；视频编辑 → Descript） |

---

## 4. 产品能力边界（G5 对照）

| 可声称 | 须限定 |
|--------|--------|
| 95–99% 准确率 | 标注"清晰音频下"，来源为官网+第三方评测 |
| 400K+ 用户 | 标注来源 PR Newswire 2026-07 |
| Ask AI 基于 GPT-4o | 官网声明 |
| 90+ 语言 | 官网声明 |
| Bot-free | 核心差异化，可强调 |
| VOMO CLI 对接 Agent | 可强调，竞品首创 |

**不可声称**：
- VOMO 可编辑音视频（那是 Descript 的能力，G5）
- 100% 准确率
- 任何未在 GA 版本中的功能
- 无来源的与竞品直接性能对比数字（除非有公开 benchmark）
- SOC 2 / HIPAA 合规认证（除非已验证）

---

## 5. 中文区/区域竞品注意

- 喜马拉雅、小宇宙等中文平台为内容平台非转录工具，写中文场景时作内容来源而非直接竞品
- 避免与中文平台比较定价（市场不同）

---

*product-competitors · v1.0.0 · 2026-08-03*
