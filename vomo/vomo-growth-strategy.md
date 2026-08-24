# VOMO — 增长策略

> **文档范围**：一个月 SEO 计划，分三部分。  
> ① 治理并批量更新现有 `/tools` · ② 楔子式**新建** Tools · ③ 博客（约 10 篇/周）  
> **Tools 产能硬指标**：**每周「更新老页 + 创建新页」合计 30**（月约 **120**）

## 0. 一个月 SEO 计划总览


| 部分       | 范围                        | 状态        |
| -------- | ------------------------- | --------- |
| **第一部分** | 更新 / 深优 / 止血现有 `/tools/`* | ✅ 本文 §1–2 |
| **第二部分** | 新建楔子与长尾 Tools（Podcast 等）  | ✅ 本文 §3–4 |
| **第三部分** | `/guide` 博客 ≈ **10 篇/周**  | ✅ 本文 §5   |



| 部分     | 4 周目标                                      |
| ------ | ------------------------------------------ |
| 第一+二部分 | **每周 30 个 Tools 任务**（更新+新建合计）；四周 ≈ **120** |
| 第三部分   | 博客约 **40 篇/月**，主链指向当周上线/更新的 Tools          |


### 0.1 任务量（按「每周 30」落地）


| 口径            | 数量       | 说明                           |
| ------------- | -------- | ---------------------------- |
| **Tools 周产能** | **30**   | **更新老页 + 创建新页** 合计，不再拆成两套周目标 |
| **Tools 月产能** | **≈120** | 4 × 30；可 ±10% 按上线窗口微调        |
| **博客周产能**     | **≈10**  | 独立计数，**不占用**上述 30            |
| **博客月产能**     | **≈40**  |                              |


#### 每周 30 的建议配比（可按周微调）


| 类型            | 每周约       | 四周合计约     | 内容                                                   |
| ------------- | --------- | --------- | ---------------------------------------------------- |
| **更新老 Tools** | **20–22** | **80–88** | 深优、止血、补差异化、修串页、统一模块；优先导航/场景/高展示，语种页用「标准增强包」批量        |
| **创建新 Tools** | **8–10**  | **32–40** | 楔子枢纽+平台/任务长尾（Podcast 先行，再 TED / Zoom / YouTube L3 等） |


> 默认取中间值：**更新 21 + 新建 9 = 30/周**。  
> 若某周楔子集中上线，新建可提到 **12**，更新降为 **18**；治理周反之。

#### 更新深度分层（避免 30 个都做成「伪改标题」）


| 档位       | 占当周更新的大致比例      | 要求                                  |
| -------- | --------------- | ----------------------------------- |
| **深优**   | ~25%（约 5–6/周）   | 达 §2.3；不可互换模块 ≥2；FAQ 独有             |
| **标准更新** | ~60%（约 12–14/周） | 来源/场景独有首段 + 3 条独有 FAQ + 内链到枢纽 + 去串页 |
| **轻量治理** | ~15%（约 3–4/周）   | Pricing/CTA 一致、断链、明显口径不一致；语种薄页可先打标+轻改 |


新建页默认按 **楔子规范**（§3），计 1 个任务；禁止再批量新建无来源逻辑的换词页。

#### 四周滚动后的覆盖预期


| 对象            | 预期                                               |
| ------------- | ------------------------------------------------ |
| 现有 ~240 Tools | 约 **1/3 完成有意义更新**（80–88）；其余进下月队列或 merge/noindex  |
| 新建            | **32–40** 个 URL（含 Podcast 全组 + 至少再开 1 个楔子的枢纽/长尾） |
| 全站 Pricing 模板 | W1 **工程一次改**，不计入 30（或计 0）                        |


---

## 1. 第一部分：`/tools` 页面审计

### 1.1 盘点范围（来源：others.md）


| 子集              | 数量                | 导航可见 | 初步风险               |
| --------------- | ----------------- | ---- | ------------------ |
| 主导航 Tools       | 19（+1 未进 sitemap） | 是    | 中：结构模板化，但关键词意图强    |
| 扩展格式转换          | 42                | 否    | 高：格式名替换为主          |
| 场景 / 功能 SEO     | 63                | 否    | 高：深浅不一，存在文案串页      |
| 语种 programmatic | 116               | 否    | **最高**：语言名插槽 + 短正文 |
| **合计**          | **~241**          | —    | —                  |


### 1.2 抽样方法

抓取日期：2026-07-22。按四类各抽 1–3 页对照正文结构与独有信息密度：


| 样本 URL                                     | 类别     | 独有度初判                         |
| ------------------------------------------ | ------ | ----------------------------- |
| `/tools/youtube-transcript`                | 导航主推   | 较好（有 Persona 场景块）             |
| `/tools/mp3-to-text`                       | 导航格式   | 中（标准模板 + 格式词替换）               |
| `/tools/flac-to-text`                      | 导航长尾格式 | 中上（无损/无需转码角度较具体）              |
| `/tools/mov-to-text`                       | 扩展格式   | 中上（QuickTime / iPhone / 免转码）  |
| `/tools/video-to-pdf`                      | 导航输出格式 | 中（场景三块，其余模板）                  |
| `/tools/ai-meeting-summarizer`             | 场景 SEO | **偏薄**                        |
| `/tools/zoom-meeting-summarizer`           | 场景 SEO | **偏薄 + 待对齐优化**                |
| `/tools/transcribe-japanese-audio-to-text` | 语种     | **薄**                         |
| `/tools/armenian-to-text`                  | 语种短路径  | **薄**（有方言钩子但仍短）               |
| `/tools/transcribe-zulu`                   | 语种特例   | 中上（点击音 / code-switching 有差异化） |


### 1.3 结论：是否薄内容？是否过于模板化？

**是——整体高度模板化；按类别薄内容程度不同。**

#### 共用骨架（几乎全站 Tools 复用）

以下区块在多数页面中文案高度雷同，仅替换 `{format}` / `{language}` / `{scene}`：

1. How To（固定 4 步）
2. CTA：`Ready to convert your media?` + `No credit card required · Free daily credits…`（逐字相同）
3. Supported Formats（同一音视频列表）
4. Why Choose（3–6 张能力卡，能力点重复：95%+、speaker ID、Ask AI、导出）
5. Pricing Free / Pro（条款几乎相同；官方三档均为**每周折算价**：Weekly `$7.99` / Monthly `$4.66` / Yearly `$1.92`，年付 Save 75%。部分 Tools 页 CMS 三档与角标口径待对齐——默认 Yearly 却显示 `$4.66` + Save 20%，与 `[/pricing](https://vomo.ai/pricing)` 不一致）
6. FAQ（准确率 / 是否免费 / 格式 / 时长 题库复用）
7. Explore More transcription tools

**判定**：对 Google 而言，这是典型的 **programmatic SEO 模板页集群**。独有信息若只占整页一小部分，即构成「薄内容 / 近似重复」风险。

#### 按类别评级


| 等级            | 含义                                      | 覆盖子集                               | 证据                                                                                                             |
| ------------- | --------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **A 可保留加深**   | 有明确搜索意图 + 至少 1–2 段不可互换的差异化文案            | 部分导航页（YouTube、FLAC、MOV）；个别语种（Zulu） | YouTube 有创作者/学生/商务 Persona；FLAC 强调无损与免转码；Zulu 写 clicks / code-switching（⚠️ 内容达 A，但 Pricing 口径待对齐，见下表）                                        |
| **B 模板主导**    | 可索引但需补「仅本页成立」的内容，否则差异化不足                 | 多数导航格式页、扩展格式转换（42）、中等场景页           | MP3 / Video-to-PDF：换词后结构与卖点与兄弟页可互换                                                                             |
| **C 待加深 / 优先治理** | 独有正文偏短，或存在串页/模块不全；优先 enrich / noindex / 合并 | 大量语种页（~116）、部分场景页（63）              | 日语页 How-to/Pricing 深度可补；Armenian 目前以 Why+FAQ+Formats 为主；Zoom 页混入 **「Free Google Meet Summaries」** 等跨产品文案，步骤与利益点可再收紧 |


#### 一致性与体验待优化项（非「薄」，但影响信任与转化）


| 问题           | 样本                                                                                                                                               | 影响                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| 文案串页         | `zoom-meeting-summarizer` 多次出现 Google Meet 文案                                                                                                    | 场景意图不够清晰，可信度打折     |
| 定价档位不一致       | Pro 官方：周 `$7.99` / 月 `$4.66` / 年 `$1.92`（均为 /week 折算）。部分页（如 `flac-to-text`、`mov-to-text`、`transcribe-zulu`）默认 Yearly 显示为 `$4.66`、角标 Save 20%（与官网口径 `$1.92` + Save 75% 不一致）；`transcribe-zulu` FAQ 写 `$1.92/week`，与 Pricing 块也不统一 | E-E-A-T / 转化信任     |
| Pricing 英文表述 | `Unlimited transcription minutes every weekly` 多页复用（如 `mp3-to-text`、`zoom-meeting-summarizer`）                                                                                              | 模板痕迹偏重，可统一润色             |
| 语种页深度不均      | Zulu 正文明显长于 Japanese / Armenian（有 How-to、8 FAQ、clicks 钩子）；后者以 Why + Formats + 3 FAQ 为主                                                                                                                    | 同模式页深浅不一，集群整体观感受影响 |


### 1.4 风险归纳（给一个月计划用）

1. **规模风险**：240+ Tools 共享骨架，搜索引擎可能按站点级判定「大量相似页」。
2. **意图错配**：扩展输出格式（`*-to-image` / `*-to-html`）与真实产品能力若弱相关，易产生高跳出与低转化，反过来拖累整站 Tools。
3. **语种页性价比**：116 页不可能在一个月内逐页写深；必须 **分层：保留枢纽语种加深 + 长尾合并/规范/降低抓取优先级**。
4. **场景页深浅不一**：`ai-meeting-summarizer`、`zoom-meeting-summarizer` 等商业意图高，但当前差异化仍不及部分格式页——应 **优先加深场景页，而不是继续加语种页**。

---

## 2. 第一部分行动计划（4 周）

### 2.1 优先级原则


| 优先级 | 规则                                                 |
| --- | -------------------------------------------------- |
| P0  | 导航可见 + 高商业意图场景页；有串页/口径不一致的页先对齐                          |
| P1  | 搜索量大的格式转换（MP3/MP4/Audio/Video/Speech/YouTube）加深差异化 |
| P2  | 扩展格式：只保留有真实查询的组合；其余合并到枢纽页或加 `noindex`（需产品/SEO 拍板）  |
| P3  | 语种页：Top 语种加深；其余维持最低合规模板或合并到「语言能力」枢纽                |


### 2.2 四周节奏（更新份额：约 20–22/周，计入每周 30）

> 与 Part2 新建共享每周 30 名额。下列为**更新侧**优先序；当周新建多则更新少，反之亦然，**周合计仍为 30**。

#### Week 1 — 打标 + 止血 + 开量


| 动作           | 计入 30       | 验收                          |
| ------------ | ----------- | --------------------------- |
| 全量 A/B/C 打标  | 否（表格）       | 覆盖 others 全部 `/tools`       |
| Pricing 模板统一 | 否（工程）       | 抽样无冲突                       |
| 更新队列开工       | **约 20–22** | 优先：串页对齐、偏薄场景、导航 P0；含 Zoom 去串文 |
| 新建（见 §4）     | **约 8–10**  | 播客枢纽定稿/预发                   |


#### Week 2–4 — 持续更新（深更 + 标更 + 轻更）

每周更新池按 §0.1 三档配比，优先序：

1. C 级串页 / 偏薄场景（会议、医疗、法律等）
2. 导航可见 Tools（YouTube、audio/video/speech、MP3…）
3. 与当周新建楔子同簇的老页（如播客相关 summarizer → 链新枢纽）
4. 扩展格式：标更或轻更 + 回链格式枢纽，不追求篇篇深更
5. 语种页：批量**标更/轻更**（补语言钩子 + FAQ + 回链）；深更只挑 Top 语种

**深更页**须满足 §2.3；标更至少：来源钩子或差异段 + 3 条独有 FAQ + 枢纽内链 + 无串文。

### 2.3 新 Tools / 深更发布门槛（防刷量变薄）

上线或记入「深更/新建」前须满足：

- [ ] 标题 / H1 主词清晰，不与同周新建撞车
- [ ] ≥ **300** 英文词独有正文（不含通用 Pricing/CTA/Formats）
- [ ] ≥2 个不可整页对调的模块
- [ ] ≥5 条 FAQ（≥3 条本页独有）
- [ ] Pricing 与全站一致；无串页文案
- [ ] 指向枢纽或相关 Tools

**轻更**可不满足全文 300 词，但必须修错 + 回链，且不得宣称「深更完成」。

### 2.4 一个月成功标准（第一部分 · 更新侧）


| 指标      | 目标                            |
| ------- | ----------------------------- |
| 周产能     | 更新+新建合计每周 **30**（四周约 **120**） |
| 更新量     | 月约 **80–88**（以周报为准）           |
| 深更      | 月 ≥ **20**（约 5/周）达 §2.3       |
| 串页/口径不一致 | P0 已知项清零                     |
| Pricing | 全站一致                          |
| 打标      | A/B/C + 更新档位队列可执行             |


---

## 3. 第二部分：新建内容（切入点模型）

### 3.1 需求逻辑：品类大词背后是「来源 × 任务」

用户搜 `speech to text` / `audio to text` / `video to text` 时，脑子里往往已有**具体来源**，而不是抽象「任意音频」：


| 用户真实情境                  | 更贴近的搜索词                                   | 为何值得做楔子                                             |
| ----------------------- | ----------------------------------------- | --------------------------------------------------- |
| 听完一集播客要写笔记 / show notes | podcast transcription、podcast to text     | 品类词流量的重要切片；平台自带文稿常不可导出                              |
| 想引用 TED 演讲原文            | TED talk transcript、transcribe TED        | 教育/内容引用刚需；现有 `/tools/transcribe-ted-audio-video` 偏薄 |
| 把 YouTube 长视频变文稿/文章     | YouTube transcript、YouTube to text        | 已有较强页，可再拆章节/博客/Shorts 长尾                            |
| 讲座 / 网课复习               | lecture transcription、transcribe lecture  | 学生场景；现有 `transcribe-lecture-to-text` 可升格            |
| Zoom 云录制会后整理            | Zoom transcript、transcribe Zoom recording | 高商业意图；现有页可借楔子升格重做                                 |
| 访谈采访归档                  | interview transcription                   | 记者/招聘/研究；可挂说话人分离卖点                                  |


**楔子公式**（可复用）：

```
枢纽 = 来源品类词（podcast / lecture / Zoom…）
  ├── 平台或品牌长尾（Spotify、Apple、TED、Coursera…）
  ├── 任务长尾（→ show notes / blog / captions / study notes）
  └── （可选）格式入口（MP3 episode、云录制 M4A）链回枢纽
```

相对搜索量层级（⚠️ 具体数字待 Ahrefs/Semrush 回填，此处按意图层级）：


| 层级       | 词性        | 示例                                                                                | 页角色                  |
| -------- | --------- | --------------------------------------------------------------------------------- | -------------------- |
| L1 头词    | 宽、竞争高     | speech to text、audio to text、video to text                                        | 首页 / 通用 Tools，不靠楔子独占 |
| L2 来源品类  | 中高、转化更清   | podcast transcription、YouTube transcript、lecture transcription、Zoom transcription | **楔子枢纽**             |
| L3 平台/品牌 | 中长尾、缺口叙事强 | Spotify podcast transcript、Apple Podcasts transcript download、TED talk to text    | **平台长尾页**            |
| L4 任务/场景 | 长尾、内容友好   | podcast to blog、TED transcript to notes、Zoom recording to meeting minutes         | 长尾页或博客强链枢纽           |


> 不要用 L1 头词去做 50 个换词 Tools；用 **L2 枢纽吃品类，L3/L4 吃需求切片**。

### 3.2 本月样板：Podcast 楔子（含可扩展长尾）

原型已出，待迁正式站：


| 角色  | 原型 / 建议                                                                    | 主词（L2/L3）                                                          | 用户需求逻辑                          |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------- |
| 枢纽  | [podcast-transcription](https://vomo.ai/podcast-transcription) | podcast transcription、podcast to text、podcast transcript generator | 「声音转文字」里很常见的内容形态：多说话人、超长、要章节/摘要 |
| 长尾  | [spotify-podcast](https://vomo.ai/podcast-transcription/spotify-podcast) | Spotify podcast transcript、download Spotify transcript | 应用内能看不能复制/导出 |
| 长尾  | [apple-podcast](https://vomo.ai/podcast-transcription/apple-podcast) | Apple Podcasts transcript download、export Apple podcast transcript | 只读、旧集常缺、非 Apple 设备难用 |
| 长尾  | [amazon-music](https://vomo.ai/podcast-transcription/amazon-music) 等 **13 子页** | 平台 ×10 + 体裁 ×3 | 见 [podcast transcription/](./podcast%20transcription/podcast-platforms.md) §4.2 |


**同楔子可继续加的长尾（本月不做完，列入 backlog）**：


| 长尾方向               | 关键词示例                                                  | 需求逻辑                                                 | 与存量                                  |
| ------------------ | ------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------ |
| YouTube 播客/节目      | YouTube podcast transcript、transcribe YouTube podcast  | 大量播客同步上 YouTube；与通用 `youtube-transcript` 区分「节目/单集」话术 | 可链现有 YouTube Tools，避免抢词则加 podcast 修饰 |
| RSS / 私人源          | podcast RSS transcript、transcribe podcast RSS          | 主播自托管、非 Spotify/Apple                                | 枢纽 Supports 已提 RSS，可独立长尾             |
| 任务：show notes      | podcast to show notes、podcast transcript to show notes | 主播复用内容，偏 L4                                          | 宜博客+枢纽锚点，或轻长尾                        |
| 任务：字幕              | podcast to SRT、podcast captions                        | 分发到视频平台                                              | 导出能力页                                |
| Google Podcasts 遗留 | （量萎缩）                                                  | 迁移用户                                                 | 低优先级或不做                              |


与线上存量：


| 线上页                                   | 现状                 | 处理                   |
| ------------------------------------- | ------------------ | -------------------- |
| `/use-case/podcast`                   | 薄                  | 导流或 canonical → 新枢纽  |
| `/tools/podcast-transcript-generator` | 模板 + FAQ 串 Whisper | 301/合并 → 新枢纽         |
| `/tools/ai-podcast-summarizer`        | 场景薄页               | 任务长尾或并入枢纽「Summary」模块 |


### 3.3 可复用楔子库（按需求优先级）

以下均可套用「枢纽 + 平台/品牌长尾 + 任务长尾」。**相对优先级**综合：意图清晰度、与 VOMO 能力匹配、现有薄页可否升级、和 Podcast 样板的可复制性。搜索量列均为层级判断，待工具复核。

#### 楔子 A — Podcast（本月执行）


|        | 内容                                      |
| ------ | --------------------------------------- |
| L2 枢纽词 | podcast transcription / podcast to text |
| L3 长尾  | Spotify、Apple、（下批）YouTube podcast、RSS   |
| L4 任务  | show notes、blog、SRT                     |
| 为何先做   | 原型已验证；平台缺口叙事清晰；吃掉「音频转文字」的一大内容切片         |


#### 楔子 B — 名源视频 / TED（高复用）


|         | 内容                                                               |
| ------- | ---------------------------------------------------------------- |
| 用户逻辑    | 搜 video to text / lecture 的人，常点名 **TED、公开课、访谈节目**                |
| L2 枢纽词  | TED talk transcript、transcribe TED talk（或更宽：talk transcript hub） |
| L3/品牌长尾 | TED.com 单集、TEDx；可延伸 Khan/公开课（需产品能吃链或上传）                          |
| L4 任务   | study notes、quote with timestamp、subtitle                        |
| 存量      | `/tools/transcribe-ted-audio-video`（薄）→ 升格为楔子枢纽而非再挂模板            |
| 优先级     | **下月首选之一**（教育/引用意图稳、品牌词好写差异）                                     |


#### 楔子 C — YouTube 深化（枢纽已有）


|          | 内容                                                              |
| -------- | --------------------------------------------------------------- |
| 用户逻辑     | L1 `video to text` 大量落到 YouTube；要的是「链接进、文稿/章节/文章出」              |
| L2 枢纽    | 已有 `/tools/youtube-transcript`（Part1 深优对象）                      |
| L3/L4 长尾 | Category/Topic/Sport/Format 子页（如 `youtube-news`、`education`、`shorts`）；任务长尾 YouTube to blog / SRT / 直播回放 |
| 存量       | 枢纽 + 已上线约 17 个子页；`youtube-video-summarizer`；多篇 Guide how-to-youtube* |
| 工厂文档   | [youtube transcription/](./youtube%20transcription/youtube-categories.md)（分类全景）· [page-playbook](./youtube%20transcription/page-playbook.md) |
| 优先级      | **深优枢纽 + 按 playbook 补 404/缺口子页**（P0：`business`）；博客只喂 L4，避免与播客楔子抢 `youtube transcript` |


#### 楔子 D — 讲座 / 网课（Lecture）


|        | 内容                                                        |
| ------ | --------------------------------------------------------- |
| 用户逻辑   | speech to text 里的学生切片：录音笔/网课回放 → 笔记                       |
| L2 枢纽词 | lecture transcription、transcribe lecture to text          |
| L3 长尾  | Zoom lecture、Coursera/上传网课、课堂录音 M4A                       |
| L4 任务  | study notes、flashcards 摘要、多语言听译                           |
| 存量     | `/tools/transcribe-lecture-to-text`、`/use-case/education` |
| 优先级    | M2–M3；与 TED 楔子可共用「学习」内链簇                                  |


#### 楔子 E — 会议平台（Zoom / Teams / Meet）


|        | 内容                                                                                                                                                |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 用户逻辑   | meeting notes / speech to text 的 B2B 切片；要的是**录制文件→纪要**，常伴随「不要 Bot」                                                                                |
| L2 枢纽词 | Zoom transcription、meeting recording to text（或 AI meeting notes 场景枢纽）                                                                             |
| L3 长尾  | Zoom cloud recording、Teams recording、Google Meet recording                                                                                        |
| L4 任务  | meeting minutes、action items、分享链接                                                                                                                 |
| 存量     | `zoom-meeting-summarizer`（待去串）、`transcribe-zoom-recordings-to-text`、`transcribe-teams-recording`、`google-meet-transcription` 等——**适合楔子升格重做，而不是再铺同质薄页** |
| 优先级    | **与 TED 并列的下月强候选**；可消化 Part1 C 级页                                                                                                                 |


#### 楔子 F — 访谈 / 语音备忘录


|        | 内容                                                                             |
| ------ | ------------------------------------------------------------------------------ |
| 用户逻辑   | 记者、招聘、销售回访、个人 Voice Memos → 要说话人与可编辑稿                                          |
| L2 枢纽词 | interview transcription；voice memo transcription                               |
| L3 长尾  | iPhone Voice Memos、WhatsApp 语音、voicemail to text                               |
| 存量     | `transcribe-interview-to-text`、`ai-voice-memos`、`transcribe-voicemail-to-text` |
| 优先级    | M2+；强化 Bot-free / 移动端叙事                                                        |


#### 楔子 G — 短视频 / 社交（审慎）


|       | 内容                                                         |
| ----- | ---------------------------------------------------------- |
| L2/L3 | TikTok to text、Instagram Reels transcript、Vimeo transcript |
| 存量    | 已有对应薄 Tools                                                |
| 优先级   | 低–中；仅在产品链接能力稳定且搜索有量时升格，避免又铺一层换词                            |


### 3.4 原型评审（Podcast 三页）

**结论：相对线上偏模板的 use-case / 旧 Tools，差异化更清晰；长尾保持「同骨架、不同不可互换卖点」。**


| 维度   | 线上现状（可加深）              | Lovable 原型             |
| ---- | ---------------------- | ---------------------- |
| 钩子   | 偏泛「转文字+摘要」              | 平台缺口（不能复制/导出等）         |
| 可信   | 样例与证据偏少                    | 样例转写 UI（说话人+时间码）       |
| 结构   | Related 较散 / 通用 How-to | 面包屑 + 子→父 + 平台专属步骤     |
| 模板风险 | 换词痕迹偏重                  | 可控：H1/钩子/How-to 不可整页对调 |


上线前：收敛旧播客 URL、统一 Pricing、确认链接拉取能力与文案一致。

### 3.5 正式 URL 建议（Podcast 本月）


| 建议路径                                   | 角色                                    |
| -------------------------------------- | ------------------------------------- |
| `/podcast-transcription`               | 枢纽（已上线；合并旧 `podcast-transcript-generator`） |
| `/podcast-transcription/spotify-podcast` | L3（已上线）                              |
| `/podcast-transcription/apple-podcast`   | L3（已上线）                              |
| `/podcast-transcription/{platform}`      | L3 平台（10） |
| `/podcast-transcription/{genre}`         | L3 体裁（business / christian / true-crime） |
| `/use-case/podcast`                    | 导流或 canonical → 枢纽                    |


后续楔子命名同构：`/tools/{source}-transcription` + `/tools/{platform}-{source}-transcription`。

---

## 4. 第二部分行动计划（新建份额：约 8–10/周，计入每周 30）

> 新建与更新共享每周 30。本月新建以 **Podcast 楔子**为主，有余量启动 TED 或 Zoom 簇长尾；禁止为凑 30 而新建无搜索逻辑的格式换词页。

### Week 1 — 定稿 + 开始计数


| 动作                     | 计入新建                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| 定 slug；合并旧播客 URL 方案    | 运维，可不计 30                                                                           |
| 产品确认链接能力               | —                                                                                   |
| 播客枢纽 + 已就绪长尾**上线或可预览** | 计入当周新建（目标凑满 8–10：枢纽、Spotify、Apple，及 RSS/YouTube-podcast/show-notes 等 backlog 中已定稿者） |


### Week 2 — Podcast 簇铺开


| 动作                                                    | 计入新建              |
| ----------------------------------------------------- | ----------------- |
| 枢纽若未上则本周上；补 L3/L4 长尾                                  | 向 8–10 靠齐         |
| 同步更新老页 `podcast-transcript-generator` 等 → 301 或改内容链枢纽 | 301 旁的内容改版算**更新** |


### Week 3 — 长尾加码 + 下一楔子试水


| 动作                                          | 计入新建                      |
| ------------------------------------------- | ------------------------- |
| Podcast 剩余 L3/L4                            | 继续占新建名额                   |
| 若 Podcast 簇已齐：开工 **TED** 或 **Zoom** 枢纽/首批长尾 | 计入新建，单周仍 ≤10 左右，保证更新侧 ≥20 |


### Week 4 — 第二楔子推进 + 词表复核


| 动作                       | 计入新建     |
| ------------------------ | -------- |
| TED 或 Zoom 簇继续按 L2→L3 建页 | 8–10     |
| L2/L3 词搜索量工具复核           | 表格，不计 30 |


### 4.1 第二部分成功标准（新建侧）


| 指标      | 目标                                             |
| ------- | ---------------------------------------------- |
| 周新建     | 约 **8–10**（与更新合计 30）                           |
| 月新建     | 约 **32–40**                                    |
| Podcast | 枢纽 + Spotify + Apple **必上**；其余播客长尾尽量吃满 backlog |
| 第二楔子    | 至少启动 TED **或** Zoom 的枢纽级 1 页 + 若干长尾            |
| 质量      | 新建均达 §2.3；无「纯换词」新建                             |


---

## 5. 第三部分：博客高频产出

### 5.1 节奏与月总量


| 节奏           | 折算                      | 说明                                                    |
| ------------ | ----------------------- | ----------------------------------------------------- |
| **每周约 10 篇** | 或 **每天 1–2 篇**（工作日为主）   | 二选一执行，月合计约 **40**                                     |
| 发布日          | 建议工作日均匀发，避免周末堆 10 篇同日上线 | 利于收录与内链消化                                             |
| 路径           | `/guide/{slug}`         | 现有分类：`ai-transcription` / `ai-insights` / `use-cases` |


### 5.2 与 Part1 / Part2 的分工


|     | Tools（Part1–2）          | 博客（Part3）           |
| --- | ----------------------- | ------------------- |
| 职责  | 交易/工具意图；**每周更新+新建共 30** | 信息/比较/教程；**每周 ~10** |
| 本月量 | Tools **~120**          | 博客 **~40**          |
| 风险  | 为凑 30 做轻更刷量 / 乱建换词页     | 同质化偏高                |


博客**不替代** Tools 深优：高意图词仍以 Tools/楔子为钱页；博文做漏斗上沿与内链燃料。

### 5.3 选题配比（每周 10 篇建议）


| 类型                | 每周约 | 作用                         | 示例方向                                                        |
| ----------------- | --- | -------------------------- | ----------------------------------------------------------- |
| 楔子支撑（Podcast）     | 2–3 | 喂 Spotify / Apple / 通用播客枢纽 | 平台文稿能否导出、show notes、RSS                                     |
| 来源切片预热            | 1–2 | 为下月楔子铺 L3/L4               | TED talk transcript、lecture to notes、YouTube→blog（链现有/未来枢纽） |
| 会议 / Bot-free     | 1–2 | 服务会议深优与未来 Zoom 楔子          | Zoom 云录制、无 Bot 笔记                                           |
| 竞品 / Alternatives | 2   | 延续强势栏目                     | vs Otter/Fireflies/Granola 等                                |
| How-to / 格式       | 1–2 | 喂 audio/video/YouTube      | MP3、语音备忘录；点明「来源」而非纯格式                                       |


> 每周选题表需标注 **唯一主承接 URL**（某个 `/tools/`* 或楔子页），禁止 10 篇都链首页。

### 5.4 四周主题侧重


| 周   | 博客侧重                                | 配合                   |
| --- | ----------------------------------- | -------------------- |
| W1  | 会议 / Zoom·Meet·Teams + 库存对比补强       | Part1 止血；尚未依赖新播客 URL |
| W2  | Podcast 枢纽上线前后：通用播客转录、show notes    | 内链指向新枢纽              |
| W3  | Spotify + Apple 专篇集中放量（各至少 2–3 篇累计） | 长尾页上线当周加码            |
| W4  | Alternatives / Best-of + 下一楔子预热选题   | 为下月会议或 YouTube 楔子铺词  |


### 5.5 发布底线（防博客变薄内容农场）

- 每篇一个主关键词，不与当周其他篇撞同一 slug 意图
- 必须链到 **1 个主 Tools/楔子页** + 可选 1–2 个相关 Guide
- 禁止整篇只换竞品名的「伪 Alternatives」；至少有对比维度或步骤差异
- 与已有 38 篇存量查重：不重复发同题（如再写一篇信息增量不足的 vomo vs otter）
- AI 可起草，**发布前人工过事实与产品能力**（避免再出现 Whisper 串题类错误）

### 5.6 第三部分成功标准


| 指标   | 目标                                   |
| ---- | ------------------------------------ |
| 产出   | ≥ **36** 篇/月（理想 **40**；允许单周 8–10 波动） |
| 内链   | ≥80% 博文有明确 Tools/楔子主链                |
| 楔子配套 | Podcast 相关博文合计 ≥ **8** 篇/月           |
| 质量   | 无大面积互相抄袭段落；无产品能力事实错误                 |


---

## 6. 三部分如何配合（一个月排期示意）

**Tools 每周固定 30 = 更新约 21 + 新建约 9**（可按周在 18–22 / 8–12 间浮动）。


| 周   | 更新老页 ~21               | 新建 ~9                      | 博客 ~10              | 当周 Tools 合计 |
| --- | ---------------------- | -------------------------- | ------------------- | ----------- |
| W1  | 打标+Pricing+止血+导航开改     | Podcast 枢纽+Spotify+Apple 等 | 会议/对比               | **30**      |
| W2  | 场景/YouTube/audio 深优与加厚 | Podcast 长尾收尾 + 第二楔子枢纽      | 播客向                 | **30**      |
| W3  | 格式簇+垂直场景               | 第二楔子长尾                     | Spotify/Apple/TED 向 | **30**      |
| W4  | 语种批量标更/轻更 + GSC 回炉     | 第二楔子收尾 / 第三楔子预埋            | Alternatives+预热     | **30**      |


月终验收：

- [ ] Tools：**4 周 × ≈30 ≈ 120**（更新 ~80–88 + 新建 ~32–40）
- [ ] Podcast 楔子完整；第二楔子至少枢纽+2 长尾
- [ ] Pricing 一致；已知串页清零；旧播客 URL 收敛
- [ ] 博客约 40；Podcast 配套 ≥8
- [ ] 新建无「无来源逻辑」的纯换词页；C 档轻量更新未占比失控

---

## 7. 页数量级怎么理解


| 轨道          | 第一个月           | 逻辑                 |
| ----------- | -------------- | ------------------ |
| Tools 更新+新建 | **~120（30/周）** | 主任务量；更新吃存量，新建走楔子长尾 |
| 博客          | **~40（10/周）**  | 独立轨道，喂内链           |
| 纯换词扩表       | **不计完成**       | 有名额也不做             |


相对全站 ~240 Tools：一个月更新轨道可覆盖 **约 1/3 强**的存量（若含语种批量），新建再增 ~32–40 URL。重点不是「每周凑满 30 个标题微调」，而是 **约 21 个有效更新 + 约 9 个有需求逻辑的新页**。

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[主文档](./vomo.md) | [keywords](./vomo-keywords.md) | [competitors](./vomo-competitors.md) | [use-cases](./vomo-use-cases.md) | [site-structure](./vomo-site-structure.md) | [others](./vomo-others.md)*
*Last updated: 2026-07-23*
*来源：任务基准「Tools 更新+新建 30/周」；楔子与博客节奏据此重算；Pricing 三档口径按官网 `/pricing` 复核*