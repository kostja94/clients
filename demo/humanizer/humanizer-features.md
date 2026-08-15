# Humanizer 功能与能力

> 关联：[humanizer.md](./humanizer.md) | [humanizer-use-cases.md](./humanizer-use-cases.md) | [humanizer-keywords.md](./humanizer-keywords.md)

**产品入口**：[humanizer.help](https://humanizer.help/)

---

## 一、核心能力（产品叙事）

| 能力 | 说明 |
|------|------|
| **AI Text Humanization** | 将 AI 生成文本转化为自然流畅的人类写作风格，消除"机械味" |
| **Bypass AI Detection** | 降低被 GPTZero、Turnitin、Originality.ai、ZeroGPT、Copyleaks 等检测器标记的概率 |
| **Preserve Original Meaning** | 改写不改变原意、事实信息、关键论点 |
| **Real-Time Processing** | 粘贴即处理，秒级返回结果 |
| **Multi-Mode Output** | 不同人性化强度 / 写作风格可选 |

---

## 二、功能矩阵

### 2.1 文本人性化（核心）

| 功能 | 说明 | 推测可用性 |
|------|------|-----------|
| **Standard Humanize** | 基础改写：调整句式、替换 AI 高频词 | ✅ 免费 |
| **Advanced / Deep Humanize** | 深度重组句子结构、增加 burstiness、模拟人类写作的不规则性 | ✅ 付费 |
| **Academic Mode** | 保留学术语气与结构，降低检测率（适合论文/研究报告） | 推测付费 |
| **Creative / Casual Mode** | 轻松、口语化风格（适合博客/社媒） | 推测 |
| **Business / Professional Mode** | 商务正式语气（适合邮件/报告） | 推测 |
| **SEO Mode** | 优化可读性 + 保留关键词密度 | 推测 |

### 2.2 AI 检测器（辅助）

| 功能 | 说明 |
|------|------|
| **Built-in AI Detector** | 改写前显示 AI 概率分数 |
| **Post-Humanize Score** | 改写后显示降低后的分数 |
| **Multi-Detector Support** | 覆盖 GPTZero、Originality.ai、Turnitin、ZeroGPT、Copyleaks、Writer、Sapling 等 |

### 2.3 附加能力（推测）

| 功能 | 说明 |
|------|------|
| **Plagiarism Check** | 改写后查重（与 Copyscape / Originality.ai 集成或内置） |
| **Grammar & Readability** | 改写同时修正语法、提升可读性分数 |
| **Multi-Language Support** | 支持英语以外的输入输出（西/法/德/中等） |
| **Batch Processing** | 批量改写多段文本（Pro 功能） |
| **API Access** | 开发者 API 集成（Enterprise） |
| **Browser Extension** | Chrome 扩展一键改写（推测） |

---

## 三、输出质量维度

| 维度 | 说明 | 用户期望 |
|------|------|---------|
| **Human Score** | AI 检测器给出的"人类写作概率" | >90% |
| **Burstiness** | 句子长度与结构的变化程度 | 接近人类写作分布 |
| **Perplexity** | 文本的不可预测性 | 高（人类写作特征） |
| **Meaning Preservation** | 改写后原意保留 | 95%+ |
| **Grammar** | 语法正确性 | 无错误 |
| **Plagiarism** | 原创性 | 0% 重复 |

---

## 四、支持的 AI 检测器（行业通用参考）

| 检测器 | 类型 | 说明 |
|--------|------|------|
| **GPTZero** | 教育场景 | 学校最常用 |
| **Turnitin** | 学术诚信 | 论文查重 + AI 检测 |
| **Originality.ai** | 专业/出版 | 严格，常用于 SEO 与内容审核 |
| **ZeroGPT** | 通用免费 | 广泛使用 |
| **Copyleaks** | 企业/教育 | AI + 抄袭双检 |
| **Writer** | 企业 | 内容团队常用 |
| **Sapling** | 客服/邮件 | 轻量检测 |
| **Crossplag** | 学术 | 多语言支持 |

---

## 五、定价推断（行业参考）

| 层级 | 推测价格 | 内容 |
|------|---------|------|
| **Free** | $0 | 每日 N 次或不限次数但字数限制（如 500 words/次）；仅 Standard Mode |
| **Pro / Premium** | $9.99–$19.99/月 | 无限次数、Advance Mode、多模式、无字数限制 |
| **Business / Team** | $29.99–$49.99/月 | 批量处理、API、团队协作 |
| **Enterprise** | 定制 | API 大批量、SLA、白标 |

---

## 六、与竞品功能对比（摘要）

| 功能 | Humanizer | Undetectable AI | WriteHuman | QuillBot | StealthWriter |
|------|-----------|-----------------|------------|----------|---------------|
| 文本人性化 | ✅ | ✅ | ✅ | ✅（Paraphraser） | ✅ |
| 多级强度 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 内置 AI 检测 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 多语言 | 推测 ✅ | ✅ | ✅ | ✅ | ✅ |
| 免费层 | ✅ | ✅（限额） | 有限 | ✅ | 有限 |
| API | 推测 | ✅ | — | ✅ | ✅ |
| 浏览器扩展 | 推测 | ✅ | — | ✅ | — |

*完整竞品分析*：[humanizer-competitors.md](./humanizer-competitors.md)

---

## 七、可拓展功能方向（增长建议）

| 方向 | 说明 | 优先级 |
|------|------|--------|
| **Chrome Extension** | 在 Google Docs / Word 中一键改写 | P0 |
| **WordPress Plugin** | 博客后台直接人性化 | P1 |
| **API Docs & SDK** | 开发者生态 + 集成 | P1 |
| **Team Dashboard** | 企业用量管理、品牌语气定制 | P2 |
| **Humanize by URL** | 粘贴网页 URL 直接抓取改写 | P2 |
| **AI Image Humanizer** | 图片内文字 OCR → 改写 | P3 |

---

*Demo 文档包 · Humanizer · https://humanizer.help/*
