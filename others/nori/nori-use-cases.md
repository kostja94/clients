# Nori Use Cases 总结

> **本文档职责**：Persona 与情境、Use Case 页面内容（谁在什么情境下用）；**并维护「非人群维度」的场景分类**（生活事件、活动域、协调方式等），供博客、功能页首屏、FAQ 与内链选题。  
> **引用**：功能页 URL 与内链见 [nori-features.md](./nori-features.md) §四、§五；目标关键词见 [nori-keywords.md](./nori-keywords.md) §9；网站内链树与优先级见 [nori-site-structure.md](./nori-site-structure.md)；产品概览见 [nori.md](./nori.md)。  
> **结构方法（脱敏）**：Use Case 文档可按 **场景类型**（活动域）、**用户阶段**（筹备期 vs 执行期）、**垂直领域** 拆表；Nori 将「领域」落地为「家庭活动域」与「生活节律」。不引用其他客户专案路径。  
> **维护规范**：[元文档-通用文档规范.md](../../../通用知识库/元文档-通用文档规范.md) | 通用-多文件文档联动精炼与增量循环.md

**产品形态**：App（Web、iOS、Android、iPad）+ Family Hub 硬件（计划 2026 年 6 月）。各 Use Case 页面 CTA 链至 /app 或 /download。详见 [nori.md](./nori.md) §5。

**Features 与 Use Cases 严格区分**（二者不重叠）：

| 类型 | 回答的问题 | 组织维度 | 示例 |
|------|------------|----------|------|
| **Features** | 产品**能做什么**？ | 能力 | Automatic Scheduling、AI Meal Planning、Family To-Do List |
| **Use Cases（站内核心里程碑）** | **谁**在**什么情境**下用？ | **Persona** + 典型情境 | For parents、For grandparents、For caregivers、For families |
| **Use Cases（扩展表达）** | 同一产品在**哪类生活事件 / 活动 / 协调方式**下被需要？ | **场景维度**（不必各开独立 URL） | 返校季传单、家庭旅行、医疗预约、房屋维修节律、语音免提录入 |

**边界**：站内 **URL 仍按 Persona** 收敛（避免 `/use-cases` 爆炸）；**场景维度**用于：Persona 页内 H2/H3、博客 pillar（如 back-to-school）、功能页「谁适合」模块、以及 [nori-keywords.md](./nori-keywords.md) 长尾。**情境** = 何时/为何/何任务；**人群** = 谁主导或谁受益（可重叠）。

**市场共性**（网络检索与家庭日历类内容常见母题）：集中日历降低遗漏与冲突、纸质传单/邮件进数字日历、接送与「谁去接」协调、医疗与罚款风险、大型一次性活动（旅行/派对）与日常重复节律并存——见下文 §1.1、§四。

---

## 一、Use Cases 概览

| 页面 | URL | 优先级 | 覆盖人群 |
|------|-----|--------|----------|
| **For parents** | /use-cases/for-parents | P0 | 忙碌家长、职场父母、多孩、daycare 家长、保姆协调、轻量共同抚养 |
| **For grandparents** | /use-cases/for-grandparents | P1 | 祖父母、多代家庭 |
| **For caregivers** | /use-cases/for-caregivers | P1 | 子女照护老人、照护协调 |
| **For families** | /use-cases/for-families | P2 | 通用家庭 |

**URL 原则**：按 persona 区分，URL 通用化（不区分 busy/working parents）。

### 1.1 除「人群」以外：场景可从哪些轴展开？

以下维度与 **Persona 正交**——同一家长可能同时落在多个格子里；写作时用来选 **H2 故事线** 与 **博客选题**，而不是再拆四个新 Persona。

| 维度 | 含义 | 示例（可写进文案） | 建议承载 |
|------|------|-------------------|----------|
| **生活节律 / 季节事件** | 一年中可预期的「高压窗」 | 返校（flyer/家长会/校车时刻表）、暑假夏令营与 camp pickup、感恩节/圣诞行程、春假旅行、tax/bill 季与家庭财务提醒（若只做日程提醒则弱） | 博客；for-parents 内章节；对齐 [nori-blog.md](./nori-blog.md)、[nori-schedules.md](./nori-schedules.md) |
| **活动域（领域）** | 日程从哪类事务来 | K–12 / daycare、俱乐部与联赛、音乐课、牙科正畸复诊、家庭医疗、宗教或社区活动、志愿者、家庭装修/搬家里程碑 | Persona 页「场景表」行；功能页 Use case 模块 |
| **事件时间结构** | 重复 vs 一次性 | 每周训练 vs 单次婚礼/搬家日；周期性 chore vs 大型 trip 打包清单 | 强调 Voice/Photo/Email 对「一次性洪流」的价值；Meal plan 对「每周重复」的价值 |
| **协调类型** | 家人之间交接什么 | 接送权交接、配偶双职工「谁早退」、与保姆/祖辈的只读或协作、照护轮班（兄弟姐妹） | for-parents / for-caregivers / for-grandparents 已覆盖主干 |
| **录入与情境（输入通道）** | 用户在什么物理情境下记一笔 | 开车免提（语音）、校门口传单（照片）、收件箱学校邮件（转发）、厨房/超市（语音加购物项） | 对齐 [nori-calendar-converter.md](./nori-calendar-converter.md) 与各 Input 功能页 |
| **后果强度（动机）** | 搞砸的代价 | 错过比赛/演出、牙医 no-show 费用、老人复诊遗漏、旅行误机 | 用于 CTA 与标题情绪，不单开 URL |

**与通用写法的对照**（不指向他案文件）：**「按场景类型」** ≈ 本表 **活动域 + 生活事件**；**「按用户阶段」** ≈ 家庭的 **筹备期（规划旅行菜单） vs 执行期（当天提醒与接送）**。

### 1.2 活动域速查（非独立 Persona）

| 活动域 | 典型痛点 | Nori 叙事重点 | 归属 Persona 页（承接） |
|--------|----------|---------------|-------------------------|
| **教育 / 课后** | 传单多、临时停课、多孩不同校 | Photo/Email→日历；颜色/成员区分（若产品支持） | for-parents |
| **运动 / 联赛** | 场地变更、集训周、拼车 | 语音改期；共享可见；Call reminder | for-parents |
| **医疗 / 牙科** | 复诊间隔长、易忘、no-show | 日历 + 电话提醒；照护分工 | for-parents；for-caregivers（老人） |
| **旅行 / 长假** | 机酒景点碎片化 | [AI Trip Planning](/ai-trip-planning)；共享日历 | for-parents；for-families |
| **家庭仪式 / 社交** | 生日派对、亲友来访、学校演出 | 一次性任务清单 + 日历 | for-families；for-parents |
| **房屋 / 车 / 订阅** | 低频维护、续约 | 周期性任务 / 清单 | for-families |
| **工作影响家庭** | 出差、晚开会、on-call | 「配偶可见」+ 快速改期入口 | for-parents |
| **宠物** | 兽医、粮、寄养 | 日历 + 清单 | for-families |

*来源归纳：家庭日历类公开内容常见主题（如返校传单、医疗预约、共享可见降低冲突、旅行与大型活动规划）；与 Nori 官网示例（旅行、晚餐、购物）一致。*

---

## 二、Use Case 页面内容（可直接用于网站）

### 1. For parents

**URL**: /use-cases/for-parents  
**Title**: For Parents | AI Family Organizer | Nori  
**Meta Description**: Organize schedules, meals, sports, and chores without the mental load. Voice, photo, and AI—no typing. Join 20,000+ families.

**目标关键词**：family organizer for busy parents, family calendar for daycare parents, family calendar for sports parents, family chore app, family organizer for ADHD, organize preschool schedule, family calendar for nanny, shared calendar for co-parents, blended family calendar

---

#### Headline

For Parents: Organize Family Life Without the Mental Load

Juggling work, kids' activities, daycare pickups, meals, and chores? Nori is the AI family assistant that turns chaos into calm—with voice, photo, and email so you never type twice.

#### The Problem

- **Too many apps**: Calendar here, lists there, reminders everywhere—nothing syncs
- **Manual entry kills time**: Typing schedules, copying flyers, forwarding emails
- **Sports & extracurricular overload**: Multiple kids, multiple teams, schedules change constantly
- **"What's for dinner?" fatigue**: Decision exhaustion after a long day
- **Daycare & preschool chaos**: Pickup times, parent-teacher meetings, school events
- **Nanny or babysitter coordination**: Who's picking up? What's on today's schedule?
- **Chores that slip**: Kids' tasks, household to-dos—hard to track and assign
- **ADHD-friendly?** Traditional apps assume you'll remember to open them
- **Blended families**: Your kids, my kids, our kids—complex schedules, one place

#### 场景与调用的功能

| 情境 | 你做什么 | 调用的功能 |
|------|----------|------------|
| 开车接送途中 | 说一句「Hey Nori, add soccer practice for Leo every Thursday at 4」— 不用停车、不用打字 | [Automatic Scheduling](/automatic-scheduling) |
| 收到学校/活动传单 | 拍一张照片，Nori 自动提取日期并加入家庭日历 | [Photo to Calendar](/photo-to-calendar) |
| 晚餐规划焦虑 | 「Hey Nori, plan dinners for next week based on our allergies」— 自动生成菜单与购物清单 | [Meal Planning](/meal-planning) |
| 关键事件怕忘 | Nori 会打电话提醒，比通知更可靠 | [Call Alert](/call-alert) |
| 保姆/共同抚养协调 | 共享访问，所有人看到同一份日程 | [Family To-Do List](/family-to-do-list)、[Automatic Scheduling](/automatic-scheduling) |
| 家务/任务分配 | 创建共享清单、分配任务给家人 | [Family To-Do List](/family-to-do-list)、[AI-Generated Tasks](/ai-generated-tasks) |
| ADHD/神经多样性 | 语音优先、少开 App、少打字；AI 代劳规划，减轻决策疲劳 | [Voice To-Do List](/voice-to-do-list)、[Meal Planning](/meal-planning) |

#### Proof

> "This app is really incredible. Thanks to Nori, I put my life in order without realizing it. My shopping lists, reminders, schedule and even small travel plans are ready in seconds. It is extremely easy to use and everything flows naturally." — **Ms. Emily**, Mom of 2

> "This one is far superior to anything I have ever used! It incorporates everything from a multitude of apps all into one place and I can connect all members of my family to it! We'll never miss another thing again." — **Sarah Jenkins**, Mom of 3

> "I can finally see the whole week's meals and know my partner and I are on the same page. Hands-free and stress-free with Nori's meal planning!" — **Priya R.**, Working Mom

- 20,000+ families trust Nori | 1M+ events scheduled | 2M+ hours saved | 98% say it reduces mental load | 4.9/5 App Store rating

#### 调用的功能（内链）

- [Automatic Scheduling](/automatic-scheduling) — 家庭日历 Hub
- [Photo to Calendar](/photo-to-calendar) — 拍传单→日历
- [Email to Calendar](/email-to-calendar) — 转发邮件→日历
- [Voice to Calendar](/voice-to-calendar) — 语音→日历
- [Call Alert](/call-alert) — 电话提醒
- [Meal Planning](/meal-planning) — 餐食规划、购物清单
- [Family To-Do List](/family-to-do-list) — 共享任务、家务分配
- [Voice To-Do List](/voice-to-do-list) — 免打字输入
- [For Grandparents](/use-cases/for-grandparents) — 多代家庭同步

#### CTA

[Start Free →](/app)

---

### 2. For grandparents

**URL**: /use-cases/for-grandparents  
**Title**: For Grandparents | Family Organizer App | Nori  
**Meta Description**: Stay in sync with the whole family. Snap flyers to add events, use voice—simple and stress-free. Join 20,000+ families.

**目标关键词**：family organizer for grandparents, multi-generational family calendar

---

#### Headline

For Grandparents: Stay Connected and Organized with the Whole Family

Helping with the grandkids? Nori keeps you in sync with your children and grandchildren—without learning a complicated app. Just speak or snap.

#### The Problem

- **Busy grandparent life**: Babysitting, school pickups, activities—schedules change often
- **Out of sync with the family**: "When is the recital again?" "Who's picking up today?"
- **Apps feel complicated**: Too many taps, too much typing
- **Flyers and papers**: School notices, activity schedules—easy to lose or forget

#### 场景与调用的功能

| 情境 | 你做什么 | 调用的功能 |
|------|----------|------------|
| 帮忙带孙辈、接送 | 说「Hey Nori, add piano lesson for Emma next Tuesday at 3」— 不用打字 | [Automatic Scheduling](/automatic-scheduling) |
| 收到学校/活动传单 | 拍照，Nori 自动加入家庭日历 | [Automatic Scheduling](/automatic-scheduling) |
| 与子女日程同步 | 子女添加事件你可见，你添加接送时间他们可见 | [Automatic Scheduling](/automatic-scheduling) |
| 重要活动怕忘 | Nori 电话提醒，不错过接送或演出 | [Automatic Scheduling](/automatic-scheduling) |

#### Proof

> "Nori has made such a difference in how our family stays organized. The call alerts are a lifesaver for reminders, and I especially love that I can upload photos of event flyers and it instantly turns them into clean calendar entries." — **Diana**, Grandma of 3

- 20,000+ families trust Nori | 1M+ events scheduled | 4.9/5 App Store rating

#### 调用的功能（内链）

- [Automatic Scheduling](/automatic-scheduling) — 语音、照片输入
- [For Parents](/use-cases/for-parents) — 家长端家庭组织

#### CTA

[Start Free →](/app)

---

### 3. For caregivers

**URL**: /use-cases/for-caregivers  
**Title**: For Caregivers | Family Care Coordination | Nori  
**Meta Description**: Coordinate family care for aging parents. Shared calendar, tasks, and reminders—everyone stays in sync. Join 20,000+ families.

**目标关键词**：family caregiver coordination, elder care schedule, family calendar for aging parents

---

#### Headline

For Caregivers: Coordinate Family Care Without the Chaos

Managing care for an aging parent? Siblings, spouses, and family members can stay coordinated with one shared calendar, tasks, and reminders.

#### The Problem

- **Scattered schedules**: Doctor appointments, visits, medication reminders—who's doing what?
- **Communication gaps**: "I thought you were taking Mom to the doctor." "No, that's next week."
- **Multiple caregivers**: Siblings, spouses, hired help—hard to keep everyone informed
- **Missed appointments**: No central place to track and remind

#### 场景与调用的功能

| 情境 | 你做什么 | 调用的功能 |
|------|----------|------------|
| 医生预约、探视、用药 | 添加至共享日历，兄弟姐妹/配偶实时可见 | [Automatic Scheduling](/automatic-scheduling) |
| 任务分工 | 分配谁开车、谁取药 | [Family To-Do List](/family-to-do-list)、[AI-Generated Tasks](/ai-generated-tasks) |
| 关键事件提醒 | 设置提醒，重要事项 Nori 电话通知 | [Automatic Scheduling](/automatic-scheduling) |
| 快速录入 | 语音说或拍预约卡照片，Nori 自动添加 | [Automatic Scheduling](/automatic-scheduling) |

#### Proof

- 20,000+ families trust Nori | 1M+ events scheduled | 98% say it reduces mental load | 4.9/5 App Store rating

#### 调用的功能（内链）

- [Automatic Scheduling](/automatic-scheduling) — 语音、照片输入
- [Family To-Do List](/family-to-do-list) — 任务分配
- [For Parents](/use-cases/for-parents) — 家庭组织
- [For Families](/use-cases/for-families) — 家务管理

#### CTA

[Start Free →](/app)

---

### 4. For families

**URL**: /use-cases/for-families  
**Title**: For Families | AI Household Assistant | Nori  
**Meta Description**: Your AI household assistant. Calendar, tasks, meals, pets, and more—all in one place. Join 20,000+ families.

**目标关键词**：AI household assistant, household organizer, family calendar for pets, pet vet appointment, home maintenance schedule

---

#### Headline

For Families: Organize Your Household Together

One platform for your whole household—calendar, tasks, meals, shopping, pets, and home maintenance. Just ask Nori what you need.

#### The Problem

- **Everything's everywhere**: Calendar, lists, reminders—scattered across apps
- **Household chaos**: Who's doing what? When's the vet? What's for dinner?
- **Pets are family too**: Vet appointments, food runs—easy to forget
- **Home maintenance**: Oil changes, bill due dates, gutter cleaning—out of sight, out of mind

#### 场景与调用的功能

| 情境 | 你做什么 | 调用的功能 |
|------|----------|------------|
| 全家日程统一 | 一个日历，与 Google/Apple/Outlook 同步，所有人共享 | [Automatic Scheduling](/automatic-scheduling) |
| 购物、待办、家务 | 创建共享清单，一起勾选 | [Family To-Do List](/family-to-do-list) |
| 晚餐规划 | AI 建议菜单、自动生成购物清单，家庭同步 | [Meal Planning](/meal-planning) |
| 宠物 | 兽医预约、宠物粮提醒，加入家庭日历 | [Automatic Scheduling](/automatic-scheduling)、[Family To-Do List](/family-to-do-list) |
| 家庭维护 | 车保养、账单到期、房屋维护等周期性任务 | [Family To-Do List](/family-to-do-list)、[AI-Generated Tasks](/ai-generated-tasks) |
| 免输入 | 语音说、拍照、转发邮件，无需打字 | [Voice To-Do List](/voice-to-do-list)、[Automatic Scheduling](/automatic-scheduling) |

#### Proof

- 20,000+ families trust Nori | 1M+ events scheduled | 2M+ hours saved | 4.9/5 App Store rating

#### 调用的功能（内链）

- [Automatic Scheduling](/automatic-scheduling) — 日历、语音/照片/邮件输入
- [Family To-Do List](/family-to-do-list) — 任务、清单、家务
- [Meal Planning](/meal-planning) — 餐食规划、购物清单
- [For Parents](/use-cases/for-parents) — 家长场景
- [For Grandparents](/use-cases/for-grandparents) — 祖父母场景

#### CTA

[Start Free →](/app)

---

## 三、Persona 与功能映射

| Persona | 调用的功能 | URL |
|---------|------------|-----|
| Parents | Automatic Scheduling、AI Meal Planning、Family To-Do List、Add by Voice | /for-parents |
| Grandparents | Automatic Scheduling | /for-grandparents |
| Caregivers | Automatic Scheduling、Family To-Do List、AI-Generated Tasks | /for-caregivers |
| Families | Automatic Scheduling、Family To-Do List、AI Meal Planning | /for-families |

---

## 四、扩展情境适用性

> 以下为**情境**（何时/为何），非功能。各情境由 Use Case 页面覆盖，调用 Features 实现。  
> **§4.1** 为人群/协作结构；**§4.2** 为生活事件与活动域（与 §1.1、§1.2 对应）。

### 4.1 人群与家庭结构

| 情境 | Nori 适用 | 归属 Use Case |
|------|-----------|---------------|
| 幼儿园/daycare 家长 | ✅ | /for-parents |
| 老人照护协调 | ✅ | /for-caregivers |
| 保姆/看护共享 | ✅ | /for-parents |
| 轻量共同抚养 | ⚠️ | /for-parents（共享日历、任务；不主打法院文档） |
| Sports/课外活动 | ✅ | /for-parents |
| Chores/家务 | ✅ | /for-parents |
| ADHD/神经多样性 | ✅ | /for-parents |
| Pets | ✅ | /for-families |
| 混合家庭 | ✅ | /for-parents |
| 园所 B2B 管理 | ❌ | 非 Nori 定位 |
| 深度共同抚养 | ❌ | 需法院文档 |
| 婴儿照护交接 | ❌ | 需喂养/睡眠记录，Pebbi 等更专业 |

### 4.2 生活事件与节律（非独立 Persona）

| 情境 | Nori 适用 | 归属 Use Case / 内容形式 |
|------|-----------|---------------------------|
| **返校 / 新学期** | ✅ 传单、校历、课外表进日历 | /for-parents；博客 back-to-school（见 [nori-blog.md](./nori-blog.md)） |
| **暑假 / 夏令营** | ✅ 多地点接送、周节律变化 | /for-parents |
| **家庭旅行 / 长假** | ✅ 行程与清单；[AI Trip Planning](/ai-trip-planning) | /for-parents、/for-families |
| **节假日聚会** | ✅ 筹备任务 + 日期 | /for-families |
| **医疗 / 牙科 / 正畸** | ✅ 低频高后果提醒 | /for-parents；老人 → /for-caregivers |
| **搬家 / 大型装修阶段** | ✅ 里程碑与分工清单 | /for-families |
| **工作出差 / 配偶日程突变** | ✅ 共享可见 + 快速改期 | /for-parents |
| **宗教 / 社区 / 志愿者** | ✅ 固定活动与例外日 | /for-parents 或 /for-families |
| **IEP / 家长会 / 学校特殊日程** | ✅ 邮件与纸质通知进日历 | /for-parents |
| **家庭财务截止日**（税季等） | ⚠️ 仅当日历提醒可写；深度记账非主线 | 博客或 for-families 轻触 |

---

## 五、内链规划

```
首页 (/)
  ├── /use-cases/for-parents
  │     ├── → /automatic-scheduling
  │     ├── → /meal-planning
  │     ├── → /family-to-do-list
  │     ├── → /voice-to-do-list
  │     └── → /use-cases/for-grandparents
  ├── /use-cases/for-grandparents
  │     └── → /automatic-scheduling
  ├── /use-cases/for-caregivers
  │     ├── → /automatic-scheduling
  │     └── → /family-to-do-list
  ├── /use-cases/for-families
  │     ├── → /automatic-scheduling
  │     ├── → /family-to-do-list
  │     └── → /meal-planning
  ├── /automatic-scheduling
  ├── /family-to-do-list
  └── /meal-planning
```

---

## 六、SEO 元数据建议

| 页面 | Title |
|------|-------|
| /use-cases/for-parents | For Parents \| AI Family Organizer \| Nori |
| /use-cases/for-grandparents | For Grandparents \| Family Organizer App \| Nori |
| /use-cases/for-caregivers | For Caregivers \| Family Care Coordination \| Nori |
| /use-cases/for-families | For Families \| AI Household Assistant \| Nori |

---

## 七、实施优先级

| 优先级 | 动作 |
|--------|------|
| **P0** | 新建 /use-cases/for-parents |
| **P1** | 新建 /use-cases/for-grandparents、/use-cases/for-caregivers |
| **P2** | 新建 /use-cases/for-families（可选） |
| **P1** | 首页增加 AI household assistant、household organizer |

---

## 八、文档导航

| 文档 | 职责 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、ICP（入口文档） |
| [nori-features.md](./nori-features.md) | 功能页、能力、内容摘要 |
| [nori-use-cases.md](./nori-use-cases.md) | **本文档**：Use Cases、Persona + 情境 + **非人群场景维度**（§1.1–§1.2、§4.2） |
| [nori-site-structure.md](./nori-site-structure.md) | 网站结构、URL 优先级 |
| [nori-others.md](./nori-others.md) | Proof 索引、杂项 |
| [nori-keywords.md](./nori-keywords.md) | 关键词映射、待办、URL 模式 |
| [nori-competitors.md](./nori-competitors.md) | 竞品分析、差异化 |
| [nori-calendar-converter.md](./nori-calendar-converter.md) | Photo/Email/Voice to Calendar 汇总 |
