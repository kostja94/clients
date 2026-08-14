# FloatCup 2026 — Floatboat 内容生成能力清单与热门关键词

> Floatboat 能为世界杯 Campaign 具体产出什么内容，以及对应的 SEO / 传播关键词策略。
>
> **关联**：[floatcup-2026-campaign-plan.md](./floatcup-2026-campaign-plan.md) · [floatboat-features.md](../floatboat-features.md) · [floatboat-keywords.md](../floatboat-keywords.md)
>
> **Last updated**: 2026-06-01（v2 — 修正：social-cards-skill 为 Alignify 项目资产，非 Floatboat 内置能力）

---

## 重要更正

- **social-cards-skill（v2.0.0）是 Alignify 项目的 OG/Twitter 卡片生成系统**，包含 6 种 Satori 视觉风格模板和 Agent-Native 内容感知工作流。它**不属于 Floatboat 项目**。
- 该 skill 的架构思路（风格模板 + 代理驱动匹配 + Satori 渲染）是本方案的参考来源之一，但不是 Floatboat 已具备的能力。
- 以下能力映射严格基于 **Floatboat 自身现有功能**，视觉卡片生成标注为「需新建」或「需外部工具」。

---

## 1. Floatboat 原生能力 → 内容产出映射

### 1.1 Floatboat 自身具备的能力（可直接复用）

| 现有能力 | 来源 | Campaign 中的具体应用 |
|---------|------|---------------------|
| **AI Calendar Assistant** | Floatboat 核心功能 | 订阅 ICS 赛程、开赛前自动推送提醒、自动准备比赛上下文（球队数据、近期战绩） |
| **Agentic Workspace（分屏+拖拽）** | Floatboat 核心功能 | 浏览器看 ESPN 数据 + 文件区写文案 + Chat 编排内容 — 三屏并列操作 |
| **AI File Manager** | Floatboat 核心功能 | 自动归档所有 Campaign 素材（图片/文案/数据/截图），赛后一键检索与复盘 |
| **浏览器自动化** | Floatboat 核心功能 | 自动抓取 ESPN/BBC 比赛数据、球队新闻、积分榜；驱动 Canva/Figma 模板生成视觉卡片 |
| **Combo Skills** | Floatboat 核心功能 | 把上述流程封装为一键执行的复用技能（Match Recap、Prediction Pipeline 等） |
| **Tacit Engine™** | Floatboat 核心功能 | 学习团队编辑偏好、赛事关注点，逐渐减少手动干预 |
| **Scattered Notes → Publish-ready** | Floatboat 使用场景 | 语音碎片/笔记 → 结构化战报 → 多平台社媒文案 |

### 1.2 Floatboat 目前不具备的能力（需要新建或借助外部工具）

| 能力缺口 | 说明 | 解决方案（见 §3） |
|---------|------|-----------------|
| **视觉卡片/海报图像生成** | Floatboat 没有内置图像生成引擎 | 方案 A：浏览器自动化 + Canva 模板 · 方案 B：轻量 HTML 卡片渲染器 · 方案 C：接入外部 AI 图像生成 API |
| **Satori/JSX 模板渲染** | Floatboat 没有 Satori 依赖 | 方案 B 或 C |
| **多尺寸自适应输出（OG/X/小红书/Discord）** | 没有自动尺寸适配管道 | 需新建 Combo Skill 封装 |

### 1.3 Floatboat 的差异化叙事（即使没有内置图像引擎）

Floatboat 的核心价值不是「画出一张海报」，而是**把内容生产从数据到分发的全流程在桌面端自动化闭环**。

其他工具只能做其中一环：

| 工具类型 | 能做什么 | 不能做什么 |
|---------|---------|-----------|
| Canva / Figma | 设计视觉卡片 | 不抓数据、不写文案、不分发、不归档 |
| ChatGPT / Claude | 写文案 | 不出图、不自动触发、不管理文件 |
| Pixlr / Midjourney | 生成图像 | 不编排流程、不感知数据、不跨平台联动 |
| Zapier / Make | 自动化触发 | 无 AI 内容编排、无文件管理、无桌面端 |
| **Floatboat** | **上述所有环节串联：抓数据 → 写文案 → 驱动出图 → 分发 → 归档，一个桌面窗口内完成** | 不原生生成图像（现阶段需借力外部工具） |

**叙事建议**：在 Campaign 传播中不回避「我们用了 Canva 出图」，而是强调「Floatboat 编排了整个流程，Canva 只是它调用的一个工具」——这才是 Agentic Workspace 的真实价值。

---

## 2. Floatboat 可产出的内容类型（按自主程度分级）

### 2.1 Tier 1 — 完全由 Floatboat 原生能力独立完成（零外部依赖）

这些内容类型不需要任何外部图像生成工具，仅靠 Floatboat 自身的文字处理、数据抓取、文件管理能力即可产出。

| 内容类型 | Floatboat 工作流 | 产出格式 | 自动化程度 |
|---------|-----------------|---------|-----------|
| **双语战报**（赛后 200 词 EN + 200 字 ZH） | 浏览器抓取赛果 → AI 编排双语战报 → 存档为 Markdown | `.md` 文件 | ★★★★★ 全自动 |
| **每日比赛数据摘要**（比分、射门、控球率、黄牌） | 浏览器抓取 ESPN 数据表 → AI 格式化为结构化文本 | `.md` / Discord Embed | ★★★★★ 全自动 |
| **社媒文案模板**（预测帖、结果帖、互动帖） | Agentic Workspace 内 AI 批量生成当日全部帖文 | `.md` / 纯文本 | ★★★★☆ 高 |
| **预测数据统计**（用户预测准确率、Top 榜单） | 后端数据 → AI 格式化 + 生成排行榜文字版 | `.md` / Discord | ★★★★☆ 高 |
| **每周 Campaign 周报**（下载量、订阅数、互动量汇总） | AI File Manager 读取当周数据 → AI 生成摘要 | `.md` | ★★★★☆ 高 |
| **X Thread 拆条**（一篇长战报拆成 5-7 条推文串） | AI 分析战报结构 → 按 X 字数限制自动拆条 | `.md` / 纯文本 | ★★★★☆ 高 |
| **FAQ / 客服话术**（用户常见问题标准回复） | AI 基于活动规则生成多语言 FAQ 库 | `.md` | ★★★★☆ 高 |

### 2.2 Tier 2 — Floatboat 编排 + 外部设计工具出图（浏览器自动化桥接）

这些内容类型的**流程编排、数据注入、触发调度**在 Floatboat 内完成，**视觉渲染**通过浏览器自动化驱动 Canva / Figma / Pixlr 模板完成。

| 内容类型 | Floatboat 负责 | 外部工具负责 | 产出格式 | 预计自动化程度 |
|---------|--------------|------------|---------|-------------|
| **Pre-Match Prediction Card** | 抓取球队数据 → 选模板 → 填文案 → 驱动 Canva 出图 → 归档 | Canva 模板渲染 + 导出 PNG | OG 1200×630 / X Card | ★★★★☆ |
| **Match Result Card**（赛果卡） | 抓取比分数据 → 填模板 → 出图 → 存档 | Canva 模板 | OG / X Card / 小红书 | ★★★★☆ |
| **Daily Leaderboard Card** | 提取 Top 10 数据 → 排版 → 出图 | Canva 模板 | OG / X Card | ★★★☆☆ |
| **Prediction Deadline Reminder** | 基于 ICS 判断时间 → 触发 → 生成提醒文案 | Canva 模板 | OG / Discord Embed | ★★★★★ |
| **Countdown Card**（倒计时） | 基于 ICS 计算倒计时 → 每日自动更新数字 | Canva 模板 | OG / X Card | ★★★★★ |
| **Sharp Predictor Announcement**（中奖公示） | 后端数据 → 筛选中奖者 → 匿名化 → 生成公示卡 | Canva 模板 | X Card / Discord | ★★★☆☆ |
| **Combo Skill Showcase Card** | Skill 元数据 → 功能介绍文案 → 填模板 | Canva 模板 | OG / Combo Store | ★★★☆☆ |
| **UGC 分享模板**（「我预测了 X vs Y」） | 用户预测数据 → 注入模板变量 → 出图 | Canva 模板 | X Card | ★★★★★ |

**Canva 模板准备要求**（开赛前必须完成）：

基于 Floatboat 品牌视觉体系（[floatboat-brand-visual.md](../floatboat-brand-visual.md)），预先在 Canva 中创建以下模板：

| 模板编号 | 名称 | 尺寸 | 变量字段 | 品牌规范 |
|---------|------|------|---------|---------|
| T01 | Prediction Card | 1200×630 | `{home_team}`, `{away_team}`, `{match_time}`, `{cta_text}` | 品牌色 `--brand` 琥珀，Cormorant Garamond H1，Inter 正文，奶油白底 |
| T02 | Match Result Card | 1200×630 | `{home_score}`, `{away_score}`, `{goal_scorers}`, `{key_stat}` | 同上 |
| T03 | Leaderboard Card | 1200×630 | `{rank_1}`–`{rank_10}` (name + points) | Swiss Minimal 风格，数字突出 |
| T04 | Countdown / Deadline | 1080×1080 | `{days_left}`, `{match_name}`, `{cta_text}` | Swiss Minimal，大数字 |
| T05 | Winner Announcement | 1200×630 | `{winner_name_masked}`, `{prize}`, `{match_name}` | Magazine Editorial |
| T06 | Skill Showcase | 1200×630 | `{skill_name}`, `{skill_desc}`, `{install_cta}` | Swiss Minimal 信息卡 |
| T07 | UGC Share Template | 1200×630 | `{user_name}`, `{prediction}`, `{match}` | Pixel Retro 趣味风格 |

### 2.3 Tier 3 — 需要额外开发或外部 API 接入（中期迭代）

这些内容类型需要新建 Combo Skill 或接入外部 AI 图像生成 API，开赛前可能来不及，可作为活动期间的增强功能。

| 内容类型 | 需要的开发 | 建议实现方式 | 优先级 |
|---------|-----------|------------|--------|
| **HTML 卡片渲染器 Combo Skill** | 在 Floatboat 内搭建一个轻量 HTML/CSS → PNG 渲染管道（headless browser） | 浏览器自动化截取本地 HTML 页面 → 保存为 PNG | P1 |
| **AI 图像生成 Combo Skill**（接入 DALL-E / Midjourney / Stable Diffusion API） | 封装 API 调用为 Combo Skill | Agent Chat 中写 prompt → API 返回图像 → 自动存档 | P2 |
| **Satori 模板移植**（参考 Alignify social-cards-skill 的 6 风格体系） | 将 Satori 渲染流程封装为 Floatboat 的 Selfware 或 Combo Skill | 移植 magazine/swiss/newspaper 等模板 | P2（赛后） |

---

## 3. 三套视觉卡片生成方案对比（决策参考）

鉴于 Floatboat 自身没有图像生成引擎，需要在以下方案中做出选择：

### 方案 A：浏览器自动化 + Canva 模板（推荐，最快落地）

| 维度 | 评估 |
|------|------|
| **原理** | Floatboat 浏览器自动化打开 Canva，选择预设模板，填入数据变量，导出 PNG，归档到 AI File Manager |
| **开发量** | 低。模板设计 1-2 天 + 自动化脚本 1-2 天 |
| **风险** | Canva UI 变更可能导致脚本失效（需预留手动备选方案） |
| **优势** | Canva 社区有海量 sports template 可直接修改；团队可视化编辑模板无需开发介入 |
| **劣势** | 渲染速度受 Canva 响应时间制约；每张卡约 5-10 秒 |
| **6/11 前可完成吗** | ✅ 可以（共需约 3 天） |

### 方案 B：轻量 HTML 卡片渲染器（Floatboat-native，中期优选）

| 维度 | 评估 |
|------|------|
| **原理** | 在 Floatboat 内搭建一个本地 HTML/CSS 模板 → headless browser 截图 → PNG |
| **开发量** | 中。HTML 模板设计 + 渲染脚本 + Combo Skill 封装 |
| **风险** | 字体渲染一致性、emoji 跨平台显示差异 |
| **优势** | 完全 Floatboat-native，不依赖外部服务；渲染速度快（<1 秒）；可离线运行 |
| **劣势** | 需要开发时间，风格迭代不如 Canva 灵活 |
| **6/11 前可完成吗** | ⚠️ 有风险（至少要 5-7 天，排期紧） |

### 方案 C：AI 图像生成 API 接入（灵活但不可控）

| 维度 | 评估 |
|------|------|
| **原理** | 封装 DALL-E / Midjourney API 为 Combo Skill，AI 根据数据自动编写 prompt → 调用 API → 返回图像 |
| **开发量** | 低（API 封装 1 天）但 prompt 调优周期长 |
| **风险** | 风格一致性难以保证；每次生成的图像不完全可控；API 费用 |
| **优势** | 创意灵活，可以生成高度定制化的图像 |
| **劣势** | 不适合需要品牌一致性的批量内容；可能出现「AI 味」 |
| **6/11 前可完成吗** | ✅ API 封装可以，但产出质量不可控 |

### 推荐策略

**6/11 前：方案 A（Canva 自动化）** — 最快、最可控、品牌一致性最好。

**6/11–7/19 期间：方案 B（HTML 渲染器）并行开发** — 作为 2.0 升级，逐步替换 Canva 依赖。

**赛后：方案 B + C 结合** — 沉淀为 Floatboat 永久的「内容工厂」Combo Skill 套件，成为产品功能而非一次性 Campaign 工具。

---

## 4. 热门关键词全景

### 4.1 市场验证

| 指标 | 数据 | 来源 |
|------|------|------|
| AI 广告生成器市场规模（2025） | ~$92 亿 | 行业报告 |
| 预计市场规模（2032） | ~$293 亿 | 行业报告 |
| 年复合增长率 | ~18% | 行业报告 |
| 社媒+电商广告需求占比 | 82% | Salesforce 2026 调查 |
| 使用 AI 的营销人员每周节省时间 | 5 小时 | Salesforce 2026 调查 |

### 4.2 按内容类型分类的热门关键词

#### 比赛预测卡 / Match Prediction Cards

| 关键词 | 搜索意图 | 竞争度 | Floatboat 叙事匹配 |
|--------|---------|--------|-------------------|
| `AI match prediction card generator` | 工具搜索 | 低–中 | ★★★ 「浏览器抓数据 + 一键出卡」 |
| `football prediction card maker` | 工具搜索 | 低 | ★★★ 同上 |
| `World Cup prediction game card` | 活动搜索 | 低 | ★★★ 直接匹配 FloatCup |
| `create match prediction poster AI` | 工具搜索 | 低 | ★★☆ 需结合 Canva 自动化 |
| `sports betting prediction card design` | 工具搜索 | — | ❌ 不匹配品牌调性 |

#### 营销海报 / Marketing Posters

| 关键词 | 搜索意图 | 竞争度 | Floatboat 叙事匹配 |
|--------|---------|--------|-------------------|
| `AI marketing poster generator` | 工具搜索 | 高 | ★★☆ 「编排流程 + 调用 Canva」 |
| `automated social media poster creator` | 工具搜索 | 中 | ★★★ 核心叙事：「全流程自动化」 |
| `sports event poster maker AI` | 工具搜索 | 低–中 | ★★★ 直接匹配世界杯场景 |
| `editorial style sports poster AI` | 风格搜索 | 低 | ★★★ 匹配 Floatboat 编辑风品牌调性 |
| `retro vintage sports poster generator` | 风格搜索 | 中 | ★★☆ 可作为 UGC 模板风格 |

#### 社媒卡片 / Social Media Cards

| 关键词 | 搜索意图 | 竞争度 | Floatboat 叙事匹配 |
|--------|---------|--------|-------------------|
| `AI social media card generator` | 工具搜索 | 高 | ★★☆ 需结合外部工具 |
| `automated social media content creation AI` | 工具搜索 | 中 | ★★★ 核心叙事 |
| `multi-platform social card creator` | 工具搜索 | 中 | ★★★ Agentic Workspace |
| `social media card automation workflow` | 工具搜索 | 低 | ★★★ 工作流自动化是 Floatboat 强项 |
| `share card generator sports` | 工具搜索 | 低 | ★★★ 场景匹配 |

#### 内容管线 / Content Pipeline（Floatboat 独占叙事）

| 关键词 | 搜索意图 | 竞争度 | Floatboat 匹配度 |
|--------|---------|--------|-----------------|
| `AI content automation workflow` | 工作流搜索 | 中 | ★★★ 桌面端独占 |
| `automated sports content generation` | 工具搜索 | 低 | ★★★ 蓝海词 |
| `AI match report generator` | 工具搜索 | 低 | ★★★ 完美匹配 Tier 1 能力 |
| `match data to social post automation` | 工作流搜索 | 极低 | ★★★ 蓝海词 |
| `sports content repurposing AI` | 工具搜索 | 极低 | ★★★ 蓝海词 |
| `AI campaign report generator` | 工具搜索 | 低 | ★★★ 匹配 Tier 1 能力 |
| `calendar triggered content generation` | 工作流搜索 | 极低 | ★★★ 独家优势 |

### 4.3 视觉风格热门关键词（可用于 Canva 模板设计和 AI Prompt）

以下关键词来自 2026 年 AI 视觉生成趋势，可用于指导 Canva 模板风格和外部 AI 图像生成的 prompt 写作。它们不是 Floatboat 内置的「风格选择器」，而是**内容团队的风格参考指南**。

| 风格 | 适用内容类型 | 热门 Prompt 关键词 | Floatboat 品牌适配 |
|------|------------|-------------------|-------------------|
| **编辑排版风** | 预测卡、赛果卡、品牌主视觉 | `editorial layout`, `bold serif headline`, `warm cream background`, `score typography` | ✅ 天然匹配（品牌色暖色系 + Cormorant Garamond 衬线） |
| **瑞士极简** | 排行榜、数据卡、赛程表 | `clean grid`, `number-focused`, `asymmetric layout`, `international style` | ✅ 匹配（Inter 无衬线 + 克制美学） |
| **复古 1970s 体育** | 品牌主视觉替代方案、UGC 模板 | `retro 1970s sports aesthetic`, `warm orange/brown tones`, `vintage stadium` | ✅ 与 Floatboat 暖色调天然契合 |
| **扁平矢量插画** | 产品功能介绍、Combo Skill 展示 | `flat vector illustration`, `dynamic sweeping lines`, `geometric icons` | ✅ 匹配 brand-visual 手绘风插画规范 |
| **终端/数据风** | 实时比分、预测统计、API 数据展示 | `monospace data display`, `green/amber terminal`, `live score feed` | ⚠️ 仅数据场景使用，非日常品牌风格 |
| **报纸专栏风** | 战报卡、深度复盘、引用卡 | `newsprint columns`, `headline hierarchy`, `ink texture` | ⚠️ 可用于 Blog 配图，非常规社媒风格 |

**品牌合规提醒**：
- 不使用 FIFA / World Cup 官方标识、字体、吉祥物
- 不使用可辨识的球员面部（肖像权）
- 使用 `football` 而非 `soccer`（全球用户为主），或按渠道区分
- AI 生成的视觉内容标注「AI-generated, for illustration only」

---

## 5. Floatboat 可捕获的 SEO 蓝海词

### 5.1 内容生成工具类（蓝海）

| 关键词 | 月搜索量（估算） | 竞争度 | 建议落地页 | 优先级 |
|--------|---------------|--------|-----------|--------|
| `AI match report generator` | 500–1000 | 极低 | Combo Skill 详情页 | P0 |
| `football prediction card generator` | 300–800 | 极低 | FloatCup Landing Page 功能展示区 | P0 |
| `automated social card sports` | 200–500 | 极低 | Agentic Workspace 功能介绍 | P1 |
| `sports score poster AI` | 200–500 | 低 | Combo Skill 详情页 | P1 |
| `calendar triggered AI content` | 100–300 | 极低 | AI Calendar Assistant 页 | P1 |
| `AI campaign visual generator` | 300–600 | 低 | Combo Skills Store | P2 |
| `match data to social post AI` | 100–300 | 极低 | Blog / Use-case 页 | P2 |

### 5.2 世界杯 + AI 交叉词（季节性热度）

| 关键词 | 月搜索量（估算） | 竞争度 | 建议落地页 | 优先级 |
|--------|---------------|--------|-----------|--------|
| `World Cup AI assistant` | 1000–3000（赛季） | 中 | FloatCup Landing Page | P0 |
| `AI World Cup schedule` | 500–2000（赛季） | 低 | FloatCup Landing Page | P0 |
| `World Cup prediction AI` | 500–1500（赛季） | 中 | FloatCup Landing Page | P0 |
| `AI football match analysis` | 500–1000（赛季） | 低–中 | Combo Skill 详情页 | P1 |

### 5.3 品类截流词

| 关键词 | Floatboat 差异化叙事 |
|--------|---------------------|
| `Canva alternative for automated content` | 「不是替代 Canva，是不用手动打开 Canva」— 浏览器自动化代劳 |
| `AI poster generator with workflow automation` | 「数据→文案→出图→分发→归档，一个桌面窗口闭环」 |
| `Predis.ai alternative` | 桌面端 + 本地文件 + 非 SaaS 订阅 |
| `AdCreative.ai alternative for sports` | 赛事数据自动抓取 + 多格式输出 |

---

## 6. 执行路线图

### 6.1 方案决策（需团队在 6/2 前确认）

| 决策项 | 选项 | 推荐 |
|--------|------|------|
| 视觉卡片生成方案 | A（Canva 自动化）/ B（HTML 渲染器）/ C（AI API） | **A**（6/11 前可完成）+ **B**（并行开发，活动期间上线） |
| Canva 模板设计 | 内部设计 / 外包 | **内部设计**（品牌一致性要求高） |
| 工作量评估 | 方案 A：3 天 · 方案 B：7 天 · 方案 C：2 天 | 方案 A 为主 + 方案 B 并行 |

### 6.2 Pre-Launch 技术排期（6/2–6/10）

| 截止日 | 任务 | 负责人 | 优先级 | 依赖 |
|--------|------|--------|--------|------|
| **6/2** | 方案决策：视觉卡片生成方式终选（A/B/C） | Judy + 技术组 | P0 | — |
| **6/3** | Canva 7 套模板设计完成（T01–T07） | 设计 / 喻鹭 | P0 | 6/2 决策 |
| **6/4** | 浏览器自动化脚本：ESPN/BBC 数据抓取 | 技术组 | P0 | — |
| **6/5** | 浏览器自动化脚本：Canva 模板填充 + 导出 | 技术组 | P0 | 6/3 模板 |
| **6/6** | Combo Skill 1: Match Recap Pipeline 开发 | 技术组 | P0 | 6/4 数据抓取 |
| **6/7** | Combo Skill 2: Social Post Generator 开发 | 技术组 | P0 | 6/5 Canva 脚本 |
| **6/7** | Canva → AI File Manager 归档管道搭建 | 技术组 | P1 | 6/5 |
| **6/8** | AI File Manager 世界杯文件夹结构预设 | 技术组 | P1 | — |
| **6/8** | 预测系统（提交/校验/抽奖）联调 | 技术组 | P0 | — |
| **6/9** | 端到端测试：比赛数据 → Canva 出图 → 归档 → 社媒文案 | 技术组 + 喻鹭 | P0 | 6/5–6/8 |
| **6/9** | 方案 B HTML 渲染器原型启动（如决策） | 技术组 | P1 | 6/2 决策 |
| **6/10** | 所有物料最终检查 + 全流程演练 | 全员 | P0 | — |

### 6.3 内容产出预估（45 场比赛，2 种方案对比）

#### 仅方案 A（Canva 自动化 + Floatboat 编排）

| 内容类型 | 单场 | 45 场累计 | Floatboat 负责 | Canva 负责 |
|---------|------|----------|---------------|-----------|
| 双语战报（Tier 1） | 1 EN + 1 ZH | 90 篇 | 100%（全自动） | 0% |
| 社媒文案模板（Tier 1） | 3 条/场比赛日 | ~120 条 | 100%（全自动） | 0% |
| 预测引导卡（Tier 2） | 1 张 | 45 张 | 编排+数据注入 | 模板渲染 |
| 赛果卡（Tier 2） | 1 张 | 45 张 | 编排+数据注入 | 模板渲染 |
| 排行榜日更卡（Tier 2） | 1 张/比赛日 | ~25 张 | 编排+数据注入 | 模板渲染 |
| 中奖公示卡（Tier 2） | 1 张 | 45 张 | 编排+数据注入 | 模板渲染 |
| UGC 预测分享卡（Tier 2） | ~20 张 | ~900 张 | 数据注入 | 模板渲染 |
| **总计** | — | **~1,270 个内容单元** | **编排率 ~75%** | **图像渲染** |

---

## 7. 品牌合规清单

| 规则 | 说明 |
|------|------|
| **不使用 FIFA/World Cup 官方标识** | 商标侵权风险。使用 generic football imagery |
| **不使用球员面部/姓名** | 肖像权风险。使用 silhouettes 或 jersey number 代替 |
| **预测内容标注免责声明** | 所有 AI 生成预测内容标注「For entertainment purposes only. Not betting advice.」 |
| **AI 生成视觉标注** | 「AI-generated image, for illustration only」 |
| **品牌色系统不变** | 所有视觉卡片使用 Floatboat 暖色系（`--brand` oklch(0.74 0.11 75)），不引入绿色/蓝色 |
| **字体系统不变** | H1 Cormorant Garamond 衬线，正文 Inter 无衬线 |
| **不使用 emoji 作为视觉设计元素** | 国旗 emoji 可出现在数据字段中，但不在纯视觉层面依赖 emoji |

---

> **下一步行动**：Judy + 技术组在 6/2 前完成视觉卡片生成方案（A/B/C）决策。喻鹭同步启动 Canva 模板设计（方案 A 的前置条件），技术组启动浏览器数据抓取脚本开发。
