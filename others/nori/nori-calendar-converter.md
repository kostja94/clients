# Nori Calendar Converter — xxx to Calendar 功能汇总

> **本文档职责**：整合所有「将内容转换为日历中的事件」相关功能——Photo to Calendar、Email to Calendar、Voice to Calendar；含市场调研（流行场景、竞品、关键词）。  
> **引用**：功能页结构见 [nori-features.md](./nori-features.md)；关键词与 URL 模式见 [nori-keywords.md](./nori-keywords.md)；网站层级见 [nori-site-structure.md](./nori-site-structure.md)；竞品见 [nori-competitors.md](./nori-competitors.md) §8.2；Use Cases 见 [nori-use-cases.md](./nori-use-cases.md)。

**统一意图**：「免输入添加」——用户关心「能否免打字添加事件」，不关心「用哪种方式」。Photo、Email、Voice 为同一意图的三种输入方式。

**URL 与关键词一致性**：所有 Calendar Converter 页面统一使用 `/xxx-to-calendar` 模式，与关键词「xxx to calendar」一一对应；**不**作为 /automatic-scheduling 子页，均为独立 URL。

---

## 一、概览

| 输入方式 | URL | 目标关键词 | 优先级 |
|----------|-----|------------|--------|
| **Photo to Calendar** | /photo-to-calendar | photo to calendar, flyer to calendar, school flyer to calendar | P0 |
| **Email to Calendar** | /email-to-calendar | email to calendar, forward email to calendar | P0 |
| **Voice to Calendar** | /voice-to-calendar | voice to calendar, voice to schedule | P1 |
| **Text to Calendar** | /text-to-calendar | text to calendar | P2（可探索） |
| **PDF to Calendar** | /pdf-to-calendar | PDF to calendar | P2（可探索；或由 /photo-to-calendar 扩展） |

**说明**：/automatic-scheduling 为 family calendar Hub，可链出至各 xxx-to-calendar 页；各页为独立 URL，非子路径。

### 1.1 通用关键词（不区分 input）

| 关键词 | 说明 | 目标页 |
|--------|------|--------|
| **AI calendar generator** | 不区分输入方式；用户搜「AI 生成日历」时可能指 photo/email/voice/text 任一方式 | 首页、/automatic-scheduling、各 xxx-to-calendar 页均可覆盖 |
| AI calendar app | 同上 | 首页、/automatic-scheduling |
| AI family calendar | 家庭场景 | 首页、/automatic-scheduling |

**竞品**：Texta.ai、Fotor、CalendAI、Motion、Text2Cal 等均有「AI calendar generator」定位。Nori 可于首页、Hub 页、各子页首屏自然出现该词。

---

## 二、Photo to Calendar | /photo-to-calendar

### 2.1 功能与卖点

**核心能力**：拍海报/传单/截图→AI 提取 date、time、location→一键加入家庭日历。

**目标关键词**：photo to calendar, flyer to calendar, school flyer to calendar, photo flyer to calendar, snap schedule

**扩展关键词**：screenshot to calendar, photo schedule capture, photo to calendar app, flyer to calendar app, photo to family calendar

**典型场景**：学校传单、运动日程、活动海报、会议邀请、手写日程

### 2.2 页面内容

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/photo-to-calendar |
| **Title** | Photo to Calendar App \| Snap Flyers & Add to Calendar Instantly \| Nori |
| **Meta Description** | Snap a photo of any flyer, poster, or schedule—AI extracts details and adds to your family calendar instantly. School flyers, sports schedules. Better than Photo2Calendar. |
| **H1** | Photo to Calendar App |

**核心卖点**：
- 拍海报/传单/截图→AI 提取日期、时间、地点→一键加入家庭日历
- 学校传单、运动日程、活动海报
- 与 Google/Apple/Outlook 同步；家庭共享

**差异化 vs Photo2Calendar**：Nori 与家庭日历、任务、餐食一体化；支持 voice+photo+email 多模态；核心免费

**内链**：→ /voice-to-calendar、/email-to-calendar、/family-to-do-list、/use-cases/for-parents

### 2.3 关键词汇总

| 类型 | 关键词 |
|------|--------|
| 核心 | **photo to calendar**, **flyer to calendar**, photo flyer to calendar |
| 核心 | school flyer to calendar, snap schedule |
| 扩展 | screenshot to calendar, photo schedule capture |
| 长尾 | photo to calendar app, flyer to calendar app |

---

## 三、Email to Calendar | /email-to-calendar

### 3.1 功能与卖点

**核心能力**：转发学校学期日历、活动邮件、日程链接→AI 自动提取所有日期→加入家庭日历。

**目标关键词**：email to calendar, forward email to calendar, forward schedule to calendar

**扩展关键词**：email to calendar automatic, forward schedule to calendar, school email to calendar, forward school email to calendar, forward email to family calendar

**典型场景**：学校学期日历、体育日程邮件、活动邀请、会议邀请转发

### 3.2 页面内容

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/email-to-calendar |
| **Title** | Email to Calendar \| Forward School Emails & Auto-Import to Family Calendar \| Nori |
| **Meta Description** | Forward school emails or schedule links—AI extracts all dates and adds to your family calendar. No manual entry. School semester calendars, sports schedules. |
| **H1** | Email to Calendar |

**核心卖点**：
- 转发学校学期日历、活动邮件→AI 自动提取所有日期→加入家庭日历
- 与 Sense/MailToCal 竞品区隔
- 与家庭日历、photo to calendar、call alert 一体化；家庭共享

**内链**：→ /voice-to-calendar、/photo-to-calendar、/call-alert、/use-cases/for-parents

### 3.3 关键词汇总

| 类型 | 关键词 |
|------|--------|
| 核心 | **email to calendar**, **forward email to calendar**, forward schedule to calendar |
| 扩展 | email to calendar automatic, forward schedule to calendar |
| 长尾 | school email to calendar, forward school email to calendar |

---

## 四、Voice to Calendar | /voice-to-calendar

**说明**：Voice 作为输入方式之一，将语音转为日历事件。独立 URL `/voice-to-calendar`，与 photo、email 保持「xxx to calendar」一致性。

**目标关键词**：voice to calendar, voice to schedule, hands-free scheduling, speak to add event

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/voice-to-calendar |
| **Title** | Voice to Calendar \| Add Events by Voice, Hands-Free \| Nori |
| **Meta Description** | Say it, don't type it. Add events to your family calendar by voice—hands-free. Voice to calendar, voice to schedule. |
| **H1** | Voice to Calendar |

**与 /voice-to-do-list 关系**：/voice-to-do-list 覆盖 voice to-do、voice to task；/voice-to-calendar 专注「语音→日历事件」。可 301 /voice-to-do-list → /voice-to-calendar 若合并，或两页并存、互相内链。

---

## 五、市场调研：流行 Calendar Converter 场景（关键词/竞品视角）

> **来源**：网络搜索（2025-03）；竞品官网、Product Hunt、工具评测。按「输入类型」与「使用场景」分类。

### 5.1 按输入类型（竞品有独立页/主推）

| 输入类型 | 关键词 | 竞品/产品 | 说明 |
|----------|--------|-----------|------|
| **Photo** | photo to calendar, flyer to calendar | Photo2Calendar、EventScan、Smart Calendars AI | Nori 已有 ✅ |
| **Email** | email to calendar, forward to calendar | Sense、MailToCal、AddToCal | Nori 已有 ✅ |
| **Voice** | voice to calendar, voice to schedule | Smart Calendars AI（Voice+Photo+Text 合一） | Nori 已有 ✅ |
| **Text** | text to calendar | **Text2Calendar**、**Calendulate**、**Text2Cal** | 粘贴文本→事件；Calendulate 支持 emails、websites、PDFs |
| **PDF** | PDF to calendar, PDF to Google Calendar | **PDF to Cal**、**Doc2Calendar**、Text2Calendar、Smart Calendars AI | 上传 PDF→提取事件→.ics |
| **Screenshot** | screenshot to calendar | Photo2Calendar、Smart Calendars AI、Calendarize | 与 photo 重叠，部分竞品单独强调 |
| **Document/Word** | Word to calendar, document to calendar | **Doc2Calendar**、**PDF to Cal**（Word 支持） | 文档日程→日历 |
| **Link/URL** | link to calendar, URL to calendar | Calendulate（websites）、AddToCalendar（网站添加按钮） | 转发链接/网页内容→事件 |
| **Message** | WhatsApp to calendar, SMS to calendar | **Text2Cal**（Share from WhatsApp、Messages、Slack） | 分享消息→事件 |
| **Meeting Notes** | meeting notes to calendar, transcript to calendar | **Text2Calendar**（Meeting Notes 场景）、Syncally、MeetingAfter | 会议记录/转录→任务+日历 |

### 5.2 按使用场景（Doc2Calendar 等竞品细分页）

| 场景 | 典型输入 | 竞品示例 |
|------|----------|----------|
| **Sports Schedule** | 球队日程 PDF、海报 | Doc2Calendar /solutions/sports-schedules |
| **Class/Syllabus** | 课表、学期日历 | Doc2Calendar /solutions/class-schedules |
| **Real Estate** | 交割、验房日程 | Doc2Calendar /solutions/real-estate-closings |
| **Legal Dockets** | 法庭日期、文件 | Doc2Calendar /solutions/legal-dockets |
| **Medical** | 用药、复诊日程 | Doc2Calendar /solutions/medication-schedules |
| **Construction** | 项目时间线 | Doc2Calendar /solutions/construction-project-timelines |
| **Weddings** | 婚礼流程、行程 | Doc2Calendar /solutions/event-schedules |
| **Travel** | 航班确认、行程 | Doc2Calendar /solutions/travel-itineraries |
| **Conferences** | 议程、研讨会 | Doc2Calendar /solutions/conference-schedules |

### 5.3 Text2Calendar 三大场景（官网主推）

| 场景 | 输入 | 说明 |
|------|------|------|
| Email Invitations | 转发邮件 | 会议邀请、社交活动 |
| Event Posters | 上传海报图 | 音乐会、会议、社区活动 |
| Meeting Notes | 粘贴会议记录 | 截止日期、跟进会议、任务提醒 |

### 5.4 竞品产品与官网（参考）

| 竞品 | 官网 | 主推输入 |
|------|------|----------|
| Text2Calendar | text2calendar.com | Text、Image、PDF；场景：Email、Poster、Meeting Notes |
| Calendulate | calendulate.com | Text（emails、websites、PDFs）；时区、地点、 recurring |
| Text2Cal | text2cal.app | Text、Photo、Business Card；Share from WhatsApp/Messages/Slack |
| Doc2Calendar | doc2calendar.com | PDF、Image；场景页：Sports、Class、Real Estate、Legal、Medical、Wedding、Travel、Conference |
| PDF to Cal | pdftocal.com | PDF、Word、Image |
| Smart Calendars AI | smartcalendars.ai | Photo、Screenshot、PDF；Voice+Photo+Text 合一 |
| Calendarize | calendarize.ai | Screenshot、PDF、Email、Text |
| Photo2Calendar | photo2calendar.com | Photo、Screenshot、PDF |

### 5.5 Nori 可扩展方向（建议）

| 场景 | Nori 能力 | 建议 URL | 说明 |
|------|-----------|----------|------|
| **Text to Calendar** | 粘贴文本→事件；Nori 支持「转发链接」magic import | /text-to-calendar | 新建独立页，与「转发链接」能力对齐 |
| **PDF to Calendar** | 当前未单独强调 | /pdf-to-calendar 或 /photo-to-calendar 扩展 | 若支持 PDF，可新建 /pdf-to-calendar 或于 photo 页扩展 |
| **Link to Calendar** | 转发链接→AI 提取（recipe、schedule） | /email-to-calendar 或 /link-to-calendar | 与 email 重叠；可强化「forward link to calendar」 |
| **Screenshot to Calendar** | 与 photo 同能力 | /photo-to-calendar | 扩展词，无需独立页 |
| **Message to Calendar** | 当前未覆盖 | /message-to-calendar | P2 探索；WhatsApp to calendar、message to calendar |
| **场景细分页** | 学校、运动、旅行等 | /photo-to-calendar#school 或博客 | 锚点或博客长尾 |

---

## 六、竞品对应（Nori 已覆盖）

### 6.1 Photo-to-Calendar 竞品

| 竞品 | 核心能力 | Nori 对应 |
|------|----------|----------|
| Photo2Calendar | Gemini AI 扫描照片、截图、PDF 创建事件；98% 准确率 | /photo-to-calendar |
| 其他 | EventSnap、Snap Event、Image2Cal、Calendara、Smart Calendars AI | photo to calendar, flyer to calendar, school flyer to calendar |

### 6.2 Email-to-Calendar 竞品

| 竞品 | 核心能力 | Nori 对应 |
|------|----------|----------|
| AddToCal、MailToCal、Sense | email to calendar, forward to calendar | /email-to-calendar |

### 6.3 Nori 差异化

- 家庭共享、与 meal planning/to-do 一体化
- 多模态输入（Voice + Photo + Email）同一平台
- 核心免费；无 30 天日历限制

---

## 七、主关键词表（Calendar Converter 相关）

### 7.1 Nori 已覆盖 / 规划

| 意图 | 关键词 | 目标页（URL = xxx-to-calendar） | P |
|------|--------|----------------------------------|---|
| **通用（不区分 input）** | **AI calendar generator**, AI calendar app, AI family calendar | 首页、/automatic-scheduling、各子页 | 0 |
| 照片转日历 | photo to calendar, flyer to calendar, school flyer to calendar | /photo-to-calendar | 0 |
| 邮件转日历 | email to calendar, forward email to calendar | /email-to-calendar | 0 |
| 语音转日历 | voice to calendar, voice to schedule | /voice-to-calendar | 1 |

### 7.2 市场流行、Nori 可探索（统一 xxx-to-calendar URL）

| 意图 | 关键词 | 竞品有独立页 | Nori 建议 URL |
|------|--------|--------------|---------------|
| 文本转日历 | text to calendar | Text2Calendar、Calendulate、Text2Cal | /text-to-calendar |
| PDF 转日历 | PDF to calendar, PDF to Google Calendar | PDF to Cal、Doc2Calendar | /pdf-to-calendar 或 /photo-to-calendar 扩展 |
| 截图转日历 | screenshot to calendar | Photo2Calendar、Smart Calendars AI | /photo-to-calendar（扩展词） |
| 链接转日历 | link to calendar, URL to calendar | Calendulate（websites） | /email-to-calendar 或 /link-to-calendar |
| 消息转日历 | WhatsApp to calendar, message to calendar | Text2Cal | /message-to-calendar |
| 会议记录转日历 | meeting notes to calendar, transcript to calendar | Text2Calendar、Syncally | /meeting-notes-to-calendar（P2） |

---

## 八、内链规划

**原则**：各 xxx-to-calendar 页为独立 URL，互相平级内链；/automatic-scheduling 为 family calendar Hub，可链出至各页。

```
/photo-to-calendar    ← photo to calendar、flyer to calendar（P0）
/email-to-calendar    ← email to calendar、forward email to calendar（P0）
/voice-to-calendar    ← voice to calendar、voice to schedule（P1）
/text-to-calendar     ← text to calendar（P2，可探索）
/pdf-to-calendar      ← PDF to calendar（P2，可探索）

/photo-to-calendar    → /voice-to-calendar、/email-to-calendar、/family-to-do-list、/use-cases/for-parents
/email-to-calendar    → /voice-to-calendar、/photo-to-calendar、/call-alert、/use-cases/for-parents
/voice-to-calendar    → /photo-to-calendar、/email-to-calendar、/family-to-do-list、/use-cases/for-parents
/automatic-scheduling → /photo-to-calendar、/email-to-calendar、/voice-to-calendar（链出，非父路径）
```

---

## 九、Use Cases 中的调用

| 情境 | 你做什么 | 调用的功能 |
|------|----------|------------|
| 收到学校/活动传单 | 拍一张照片，Nori 自动提取日期并加入家庭日历 | [Photo to Calendar](/photo-to-calendar) |
| 收到学校/活动邮件 | 转发邮件，Nori 自动提取所有日期并加入家庭日历 | [Email to Calendar](/email-to-calendar) |
| 开车接送途中 | 说一句「Hey Nori, add soccer practice for Leo every Thursday at 4」 | [Voice to Calendar](/voice-to-calendar) |

---

## 十、SEO 待办（Calendar Converter）

| 优先级 | 动作 |
|--------|------|
| **P0** | 新建 /photo-to-calendar 主攻 photo to calendar、flyer to calendar、school flyer to calendar |
| **P0** | 新建 /email-to-calendar 主攻 email to calendar、forward email to calendar |
| **P1** | 新建 /voice-to-calendar 主攻 voice to calendar、voice to schedule（与 /voice-to-do-list 关系见 §四） |
| **P0** | 首页/导航优先展示 photo to calendar、email to calendar、voice to calendar 入口；链至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar |
| **P1** | /photo-to-calendar 强化 school flyer to calendar、photo flyer to calendar |
| **P2** | 博客：How to add school flyers to calendar、Best photo to calendar app 2026 |
| **P2** | 可探索 /text-to-calendar、/pdf-to-calendar（若产品支持） |
| **P1** | 首页、/automatic-scheduling 强化 **AI calendar generator**（不区分 input 的通用词） |

---

## 十一、Types of Calendar（日历类型与关键词机会）

> **用途**：按日历用途分类，供探索更多可覆盖的关键词。Nori 核心为 **family calendar**；其他类型可作长尾或场景锚点。

### 11.1 按用途（Use Case）

| 类型 | 英文关键词 | 典型场景 | Nori 覆盖 |
|------|------------|----------|-----------|
| **Family calendar** | family calendar, family calendar app, shared family calendar | 家庭日程、接送、活动、多人共享 | ✅ 核心 |
| **Personal calendar** | personal calendar, personal schedule | 个人日程、提醒 | 部分（与 family 重叠） |
| **Academic / School calendar** | school calendar, academic calendar, class schedule | 课表、学期、家长会、作业 | ✅ photo、email |
| **Sports calendar** | sports calendar, sports schedule, team schedule | 训练、比赛、联赛 | ✅ photo |
| **Work calendar** | work calendar, professional calendar, meeting calendar | 会议、项目、客户 | 部分 |
| **Meal planning calendar** | meal calendar, meal planning calendar, dinner calendar | 周菜单、食谱安排 | ✅ /meal-planning |
| **Content calendar** | content calendar, editorial calendar | 博客、社媒排期 | ❌ 非 Nori 定位 |
| **Social media calendar** | social media calendar, posting calendar | 社媒发帖排期 | ❌ 非 Nori 定位 |
| **Travel calendar** | travel calendar, trip itinerary calendar | 行程、航班、酒店 | ✅ /ai-trip-planning |
| **Medical / Health calendar** | medication calendar, appointment calendar | 用药、复诊、体检 | 部分 |
| **Real estate calendar** | closing calendar, inspection calendar | 交割、验房 | 部分（photo） |
| **Legal calendar** | court calendar, docket calendar | 法庭日期、文件 | 部分（photo） |

### 11.2 按形态

| 类型 | 说明 |
|------|------|
| **Digital calendar** | 数字日历（vs 纸质） |
| **Shared / Collaborative calendar** | 多人共享、协作 |
| **Printable calendar** | 可打印（Nori 不覆盖） |
| **Subscription calendar** | 订阅式（如 iCal feed） |

### 11.3 可探索关键词（按类型）

| 类型 | 可探索关键词 |
|------|--------------|
| Family | family calendar app, best family calendar, shared family calendar, family schedule app |
| School | school calendar app, school flyer to calendar, class schedule to calendar |
| Sports | sports calendar app, sports schedule to calendar, team schedule app |
| Meal | meal planning calendar, dinner calendar, weekly meal calendar |
| Travel | travel itinerary calendar, trip calendar |
| Medical | appointment calendar, medication reminder calendar |

---

## 十二、文档导航

| 文档 | 职责 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、ICP |
| [nori-features.md](./nori-features.md) | 功能页结构、能力归属 |
| [nori-keywords.md](./nori-keywords.md) | 关键词映射、待办 |
| [nori-use-cases.md](./nori-use-cases.md) | Use Cases、Persona + 情境 |
| [nori-competitors.md](./nori-competitors.md) | 竞品分析、Photo2Calendar/Sense 等 |
| **nori-calendar-converter.md** | **本文档**：Photo/Email/Voice to Calendar 汇总 |

---

**Last updated**: 2025-03-07（§1.1 AI calendar generator；§11 Types of Calendar）
