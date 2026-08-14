# Nori Features 功能页总结

> **本文档职责**：功能页详情、页面结构、能力归属、Title/Meta/内容摘要。  
> **引用**：关键词与 P0 词表见 [nori-keywords.md](./nori-keywords.md) §1–§2（**权威来源**，本文不重复维护同一张主词表）；Use Cases 与 Features 边界见 [nori-use-cases.md](./nori-use-cases.md) 文首；网站层级见 [nori-site-structure.md](./nori-site-structure.md)；竞品见 [nori-competitors.md](./nori-competitors.md)；converter 见 [nori-calendar-converter.md](./nori-calendar-converter.md)；产品概览见 [nori.md](./nori.md)。  
> **维护规范**：[元文档-通用文档规范.md](../../../通用知识库/元文档-通用文档规范.md) | 通用-多文件文档联动精炼与增量循环.md

**Features vs Use Cases**：定义与示例表以 [nori-use-cases.md](./nori-use-cases.md) 文首为准；本文只写**能力页**级内容。

---

## 一、功能页概览与价值评估

| 功能页 | URL | 目标关键词 | 价值评估 | 建议 |
|--------|-----|------------|----------|------|
| **Recipe Manager** | /recipe-manager | recipe manager (4.6K), recipe organizer, import recipes, save recipes from website, recipe scanner | **高** | 核心词；与 Paprika、Recipe Keeper 竞争 |
| **Meal Planning** | /meal-planning | meal planning app (1.8K), AI meal planner, fridge to recipe, meal plan with grocery list, allergy-aware meal planning | **高** | 核心词；fridge to recipe、meal plan with grocery list 为 P0；意图「规划吃什么」 |
| **Family To-Do List** | /family-to-do-list | family to-do list, shared to-do list, family to-do list app | **高** | **新建**；主任务页，与 Any.do 竞争 |
| **Voice To-Do List** | /voice-to-do-list | voice to-do list, best voice to-do list app | **高** | 语音输入专项（任务/清单） |
| **Voice to Calendar** | /voice-to-calendar | voice to calendar, voice to schedule, hands-free scheduling | **高** | **新建**；与 photo、email 统一 xxx-to-calendar 模式 |
| **Automatic Scheduling** | /automatic-scheduling | family calendar app, AI calendar assistant | **高** | **Hub 页**；链出至各 xxx-to-calendar 页；主攻 family calendar |
| **Photo to Calendar** | /photo-to-calendar | photo to calendar, flyer to calendar, school flyer to calendar, snap schedule | **高** | **新建**；P0；与 Photo2Calendar 竞争 |
| **Email to Calendar** | /email-to-calendar | email to calendar, forward email to calendar, forward schedule to calendar | **高** | **新建**；P0；与 Sense/MailToCal 竞争 |
| **Call Alert** | /call-alert | call reminder, phone alert for events, call alert for calendar | **高** | **新建**；P0 |
| **AI Trip Planning** | /ai-trip-planning | AI trip planning, family trip planner, vacation itinerary | **中高** | **新建**；家庭行程规划 |
| **AI-Generated Tasks** | /ai-generated-tasks | AI generated tasks, automatic task creation, AI to-do list, voice to task | **中高** | 任务/项目分解差异化 |

**结论**：recipe manager、family calendar app、meal planning app、photo to calendar、email to calendar、fridge to recipe、call alert、meal plan with grocery list 为 P0 核心词/功能；/family-to-do-list 主攻 family to-do list；/voice-to-do-list 定位为 voice 输入专项。

**URL 与关键词对齐**：功能页 URL 与主关键词一致；旧 URL 需 301 重定向至新 URL。

---

## 二、页面结构策略（搜索意图导向）

> 原则：**同一搜索意图 = 一个页面**。voice to schedule、photo to calendar、email to calendar、hands-free scheduling 为同一意图「免输入添加」，用户关心「能否免打字」而非「用哪种方式」。

### 2.1 两种方案

| 维度 | 激进（搜索意图导向） | 保守（保留专项页） |
|------|----------------------|-------------------|
| 功能页数量 | **4** | **5** |
| /voice-to-do-list | 合并入 /automatic-scheduling；Voice 作为首屏卖点 | 保留，强化 voice 专项 + 链入 scheduling |
| /ai-generated-tasks | 合并入 /family-to-do-list 作为子模块 | 保留独立页 |

### 2.2 决策标准

**/voice-to-do-list 是否合并？**
- **依据**：查 GSC/GA4，voice to-do list app、hands-free scheduling 等词是否有独立流量
- **有显著流量** → 保留页，或作为 /automatic-scheduling#voice 子锚点
- **无/可忽略** → 301 合并入 /automatic-scheduling

**/ai-generated-tasks 是否合并？**
- **依据**：AI generated tasks vs family to-do list 意图是否重叠、搜索量对比
- **意图区分明显、量高** → 保留独立页
- **意图重叠、量低** → 合并入 /family-to-do-list 作为子模块

**recipe 与 meal planning**：已确认 recipe 4.6K、meal 1.8K，意图不同 → **保持独立**

### 2.3 意图-功能-关键词对齐（核心：meal planning + recipe manager）

> **recipe manager** 与 **meal planning app** 为最核心关键词；同一意图 = 一页；功能命名、目标关键词、页面内容需一致。

| 意图 | 用户要什么 | 主关键词（量级） | 功能页 | 内容边界 |
|------|------------|------------------|--------|----------|
| **食谱管理** | 保存、导入、整理食谱 | **recipe manager (4.6K)**, recipe organizer, import recipes, save recipes from website, recipe scanner | /recipe-manager | 导入方式、AI 提取、食谱库、云端同步；**不**主推 meal planning |
| **餐食规划** | 规划吃什么、周菜单、购物清单 | **meal planning app (1.8K)**, AI meal planner, allergy-aware meal planning, meal plan with grocery list | /meal-planning | 周菜单、冰箱匹配、购物清单、过敏过滤；食谱为**输入**，链入 recipe 页 |

**竞品参考**：Paprika 主品牌「Recipe Manager」，meal planning 为子功能；Cozi 按产出分 Calendar / To Do / Shopping / Recipes；Ollie AI 主攻 meal planning。Nori 两意图独立成页，与 Paprika（recipe 主）、Ollie（meal 主）均对齐。

### 2.4 若合并 voice 页：301 与内链

- 301 /voice-to-do-list → /automatic-scheduling；301 /add-anything-by-voice → /voice-to-do-list（若保留 voice 页）
- voice to-do list、hands-free scheduling 关键词由 /automatic-scheduling 覆盖
- 首页、Use Cases 内链更新

### 2.5 产品能力 → 页面归属

| 产品能力 | 归属页面 | 说明 |
|----------|----------|------|
| Forward links to magic import（食谱） | /recipe-manager | 核心词 4.6K |
| Provide recipe suggestions（拍冰箱） | /meal-planning | **P0 核心功能**；fridge to recipe、recipe suggestions；冰箱→食谱=规划吃什么 |
| AI meal planning | /meal-planning | 餐食规划 |
| Auto-generate shopping lists | /meal-planning | **P0 核心功能**；meal plan with grocery list、auto grocery lists；食材自动分解→购物清单 |
| Photo capture for events（拍海报→日历） | /photo-to-calendar | **P0 核心功能**；photo to calendar、flyer to calendar、school flyer to calendar |
| Forward email to magic import（转发邮件→日历） | /email-to-calendar | **P0 核心功能**；email to calendar、forward email to calendar；学校学期日历等 |
| Voice to schedule | /voice-to-calendar | voice to calendar；免输入添加 |
| Ask AI to look up data | 首页/产品核心 | 非独立页 |
| AI trip planning、Online search & auto import | /ai-trip-planning | 智能添加；家庭行程规划 |
| Call Alert | /call-alert | **P0 核心功能**；call reminder、phone alert for events；重要事件电话呼叫提醒 |
| AI generated tasks / voice to task | /family-to-do-list | 任务页子能力 |
| Use Nori anywhere | /download | 产品形态 |

---

## 三、功能页关键词汇总

### 3.1 /recipe-manager（核心词 4.6K）

| 类型 | 关键词 |
|------|--------|
| 核心 | **recipe manager** (4.6K), **recipe organizer**, **import recipes** |
| 核心 | save recipes from website, recipe scanner |
| 扩展 | AI recipe import, digitize cookbook, photo to recipe |
| **长尾** | best recipe manager app, recipe app that imports from website |

### 3.2 /meal-planning（核心词 1.8K；P0：fridge to recipe + meal plan with grocery list）

| 类型 | 关键词 |
|------|--------|
| 核心 | **meal planning app** (1.8K), AI meal planner, AI-powered meal planning, allergy-aware meal planning |
| 核心（P0） | **fridge to recipe**, recipe suggestions from fridge, photo fridge to meal ideas |
| 核心（P0） | **meal plan with grocery list**, auto grocery lists, automatic shopping list from meal plan |
| 扩展 | family meal planner, meal planning for families |
| **长尾** | AI meal planner for families with allergies, meal planning for busy families |
| **长尾** | nut-free meal planner, picky eater meal planning, meal plan with grocery list automatic |

### 3.3 /family-to-do-list（新建）

| 类型 | 关键词 |
|------|--------|
| 核心 | family to-do list, family to-do list app, shared to-do list |
| 核心 | shared to-do list app for families, best family to-do list app |
| 扩展 | family task app, shared family lists, family chore app |
| 差异化 | voice photo email input, add tasks by voice, no typing |

### 3.4 /voice-to-do-list

| 类型 | 关键词 |
|------|--------|
| 核心 | voice to-do list, voice to-do list app, best voice to-do list app |
| 核心 | hands-free scheduling, hands-free scheduling app |
| 扩展 | voice to calendar, voice to schedule, organize by voice |
| 扩展 | voice shopping list, voice grocery list, voice family assistant, hands-free family organizer |
| **长尾** | voice to-do list app for families, best voice to-do list app 2025, hands-free scheduling for busy parents |

### 3.5 /automatic-scheduling（Hub 页；family calendar 主）

| 类型 | 关键词 |
|------|--------|
| 核心 | **family calendar app**, best family calendar app, shared family calendar |
| 核心 | automatic scheduling, AI scheduling, AI calendar assistant |
| 核心 | voice to schedule |
| 扩展 | family calendar sync, shared family schedule |
| **说明** | 链出至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning、/voice-to-do-list |

### 3.5a /photo-to-calendar、3.5b /email-to-calendar、3.5c /voice-to-calendar（P0/P1）

*Photo、Email、Voice to Calendar 完整内容见 [nori-calendar-converter.md](./nori-calendar-converter.md)。统一 URL 模式：/xxx-to-calendar。*

| 页 | 核心关键词 |
|----|------------|
| /photo-to-calendar | photo to calendar, flyer to calendar, school flyer to calendar |
| /email-to-calendar | email to calendar, forward email to calendar |
| /voice-to-calendar | voice to calendar, voice to schedule |

### 3.5c /call-alert（P0）

| 类型 | 关键词 |
|------|--------|
| 核心 | **call reminder**, **phone alert for events**, call alert for calendar |
| 扩展 | calendar call reminder, event phone alert |

### 3.5d /ai-trip-planning

| 类型 | 关键词 |
|------|--------|
| 核心 | **AI trip planning**, **family trip planner**, **vacation itinerary** |
| 扩展 | AI itinerary builder, family vacation planner |
| **长尾** | AI trip planner for families, Disney trip planner family |

### 3.6 /ai-generated-tasks

| 类型 | 关键词 |
|------|--------|
| 核心 | AI generated tasks, automatic task creation |
| 核心 | AI to-do list, AI task manager |
| 扩展 | voice to task, photo to task, AI project breakdown, family task app with AI |
| **长尾** | AI generated tasks for families, voice to task app |

---

## 四、功能页内容摘要（可直接用于网站优化）

### 1. Recipe Manager | /recipe-manager（核心词 4.6K）

**URL**: /recipe-manager  
**301**：/import-recipes-instantly → /recipe-manager  
**Title**: Recipe Manager App | Import & Save Recipes from Any Website | Nori  
**Meta Description**: The best recipe manager for families. Import recipes from any website, paste a link, or scan handwritten notes. Save, organize, and sync recipes—allergy-aware. Better than Paprika.

**目标关键词**：recipe manager (4.6K), recipe organizer, import recipes, save recipes from website, recipe scanner

**内容边界**：导入方式（link/screenshot/scan）、AI 提取、食谱库、云端同步、过敏标记；**不**主推 meal planning，冰箱匹配由 [Meal Planning](/meal-planning) 页覆盖

**核心卖点**：
- **输入**：paste web link、upload screenshot、scan handwritten note
- **AI 提取**：ingredients、instructions、serving sizes、prep times、allergens
- **家庭同步**：共享食谱库、过敏标记
- **与 Meal Planning 联动**：食谱库→周菜单规划，链入 /meal-planning

**Benefits**：Save Recipes from Anywhere、Organize Your Cookbook、Allergy-Aware & Safe、Sync Across the Family

**适用 Use Cases**：[For Families](/use-cases/for-families)、[For Parents](/use-cases/for-parents)

**Testimonials**：Sarah J（500 截图导入）、Jessica L（Share to Nori）、David W（祖母手写食谱）

**差异化 vs Paprika/Recipe Keeper**：Nori 支持 link/screenshot/scan 三种导入；与家庭 meal planning 一体化

**内链**：→ /meal-planning、/automatic-scheduling、/photo-to-calendar

---

### 2. Meal Planning | /meal-planning（核心词 1.8K）

**URL**: /meal-planning  
**301**：/ai-powered-meal-planning → /meal-planning  
**Title**: Meal Planning App for Families | AI Meal Planner, Grocery Lists | Nori  
**Meta Description**: The best meal planning app for busy families. Snap a photo of your fridge—AI suggests meals you can make. Allergy-aware menus, auto grocery lists. Plan dinners without the stress.

**目标关键词**：meal planning app (1.8K), AI meal planner, fridge to recipe, recipe suggestions from fridge, allergy-aware meal planning, family meal planner, meal plan with grocery list

**内容边界**：周菜单、**冰箱匹配（拍冰箱→食谱建议，P0 核心卖点）**、**自动购物清单（食材自动分解→购物清单，P0 核心卖点）**、过敏过滤；食谱库由 [Recipe Manager](/recipe-manager) 提供，本页侧重「规划吃什么」

**首屏卖点（P0）**：Snap a photo of what's left in your fridge—ask AI what meals you can make. Meal plan ingredients automatically break down and get added to your shopping list. Fridge to recipe, auto grocery lists—no typing.

**适用 Use Cases**：[For Parents](/use-cases/for-parents)、[For Families](/use-cases/for-families)

*目标词与场景见 [nori-keywords.md](./nori-keywords.md) §8.4*

---

### 3. Family To-Do List | /family-to-do-list（新建）

**URL**: /family-to-do-list  
**Title**: Family To-Do List App | Shared Lists, Voice & Photo Input | Nori  
**Meta Description**: The only family to-do app that adds tasks by voice, photo, or email—no typing. Shared lists, calendar, and meal planning in one place. Better than Any.do.

**目标关键词**：family to-do list, shared to-do list, family to-do list app, shared to-do list app for families

**核心卖点**：Voice/Photo/Email 多模态输入；AI 自动分类（任务/事件/购物）；与 Calendar、Meals、Shopping 一体化；家庭共享

**差异化 vs Any.do**：Any.do 仅支持手动+语音；Nori 支持 voice + photo + email，且与餐食规划、日历深度打通

**适用 Use Cases**：[For Parents](/use-cases/for-parents)、[For Grandparents](/use-cases/for-grandparents)、[For Caregivers](/use-cases/for-caregivers)、[For Families](/use-cases/for-families)

**内链**：链入 /voice-to-do-list、/automatic-scheduling、/photo-to-calendar、/email-to-calendar、/call-alert、/ai-generated-tasks、/recipe-manager、/meal-planning

---

### 4. Voice To-Do List | /voice-to-do-list

**URL**: /voice-to-do-list  
**301**：/add-anything-by-voice → /voice-to-do-list  
**Title**: Add Anything by Voice with Nori | Organize Family Life Hands-Free  
**Meta Description**: Talk, don't type. Add events, groceries, and chores to your shared family hub with voice—hands-free. The best voice to-do list app for families.

**目标关键词**：voice to-do list, voice to-do list app, hands-free scheduling, voice to calendar

**核心卖点**：Smart Categorization（任务/事件/购物自动分类）、Shared by Design、Family Context Aware、Natural Language

**定位**：Voice 作为多种输入方式之一；链入 /family-to-do-list（主任务页）

**适用 Use Cases**：[For Parents](/use-cases/for-parents)、[For Grandparents](/use-cases/for-grandparents)、[For Caregivers](/use-cases/for-caregivers)、[For Families](/use-cases/for-families)

**Testimonials**：Sarah J. "best voice to-do list app"、Amanda & Tom、Mike T. "hands-free scheduling"、Emily R.

---

### 5. Automatic Scheduling | /automatic-scheduling（Hub 页）

**URL**: /automatic-scheduling  
**Title**: Family Calendar App | Shared Schedule, Voice & Photo Input | Nori  
**Meta Description**: The best family calendar app. Add events by voice, photo, or email—no typing. Shared calendar, call alerts, AI trip planning. 20,000+ families.

**目标关键词**：family calendar app, best family calendar app, shared family calendar, automatic scheduling, AI calendar assistant

**定位**：**Hub 页**；精简内容，链出至各子页；主攻 family calendar app

**核心卖点**：Family Calendar（共享日历、日程同步）；Voice、Photo、Email 三模态免输入添加；与 Calendar、Tasks、Meals 一体化

**子页入口**：
- [Photo to Calendar](/photo-to-calendar) — 拍海报/传单→AI 提取→日历
- [Email to Calendar](/email-to-calendar) — 转发邮件→AI 自动导入
- [Voice to Calendar](/voice-to-calendar) — 语音添加事件
- [Call Alerts](/call-alert) — 重要事件电话呼叫提醒
- [AI Trip Planning](/ai-trip-planning) — 家庭行程规划
- [Voice To-Do List](/voice-to-do-list) — 语音添加任务

**Proof**：20,000+ 家庭、1M+ 事件、2M+ 小时、98% 减轻心理负担、4.9/5

**适用 Use Cases**：[For Parents](/use-cases/for-parents)、[For Grandparents](/use-cases/for-grandparents)、[For Caregivers](/use-cases/for-caregivers)、[For Families](/use-cases/for-families)

**内链**：→ /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning、/voice-to-do-list、/family-to-do-list、/meal-planning、/recipe-manager

---

### 5a. Photo to Calendar、5b. Email to Calendar | /photo-to-calendar、/email-to-calendar（新建）

*完整内容（Title、Meta、卖点、关键词、内链、竞品）见 [nori-calendar-converter.md](./nori-calendar-converter.md)。*

---

### 5c. Call Alert | /call-alert（新建）

**URL**: /call-alert  
**Title**: Call Alert for Family Calendar | Never Miss Pickup or Appointments | Nori  
**Meta Description**: Nori calls you with alerts to remind you of important events. Never miss pickup, practice, or appointments. Phone alert for family calendar events.

**目标关键词**：call reminder, phone alert for events, call alert for calendar

**核心卖点**：重要事件电话呼叫提醒；接娃、训练、预约不再遗忘；与家庭日历深度打通

**内链**：→ /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/use-cases/for-parents

---

### 5d. AI Trip Planning | /ai-trip-planning（新建）

**URL**: /ai-trip-planning  
**Title**: AI Trip Planning for Families | Hawaii, Disney & Vacation Itinerary | Nori  
**Meta Description**: Plan your trip to Hawaii or Disney—AI helps organize the itinerary and adds to your family calendar. Family trip planner with shared schedule.

**目标关键词**：AI trip planning, family trip planner, vacation itinerary

**核心卖点**：计划夏威夷/迪士尼等家庭旅行→AI 生成行程→自动加入家庭日历；与 Calendar、Tasks、Meals 一体化

**内链**：→ /automatic-scheduling、/family-to-do-list、/use-cases/for-families

---

### 6. AI-Generated Tasks | /ai-generated-tasks

**URL**: /ai-generated-tasks  
**301**：/features/ai-generated-tasks → /ai-generated-tasks  
**Title**: AI-Generated Tasks for Families | Automatic Task Creation & Scheduling | Nori  
**Meta Description**: Turn voice, photos, and emails into organized, assigned tasks. AI breaks down projects. 10,000+ families.

**目标关键词**：AI generated tasks, automatic task creation, AI to-do list, voice to task

**核心卖点**：Capture Anything（voice/photo/email）→ AI Understands Context → Auto-Generate & Assign；AI Breakdown（Plan a trip → 子任务）；Tasks ↔ Meals ↔ Calendar ↔ Shopping 联动

**差异化**：vs Todoist/Notes — 多模态输入、家庭感知、AI 分解与分配

**适用 Use Cases**：[For Parents](/use-cases/for-parents)、[For Caregivers](/use-cases/for-caregivers)、[For Families](/use-cases/for-families)

---

## 五、内链规划

```
首页 (/)
  ├── /recipe-manager       ← P0 核心词 4.6K（recipe manager）
  ├── /meal-planning        ← P0 核心词 1.8K（meal planning app）
  ├── /automatic-scheduling ← Hub（family calendar；链出至各 xxx-to-calendar）
  ├── /photo-to-calendar   ← P0（photo to calendar、flyer to calendar）
  ├── /email-to-calendar   ← P0（email to calendar）
  ├── /voice-to-calendar   ← P1（voice to calendar、voice to schedule）
  ├── /call-alert          ← P0（call reminder、phone alert）
  ├── /ai-trip-planning    ← AI trip planning、family trip planner
  └── /voice-to-do-list    ← 语音输入专项（voice to-do、任务）
  ├── /family-to-do-list    ← 主任务页（与 Any.do 竞争）
  └── /ai-generated-tasks   ← AI 任务生成（AI generated tasks）

/recipe-manager → /meal-planning、/automatic-scheduling、/use-cases/for-families
/meal-planning → /recipe-manager、/automatic-scheduling、/use-cases/for-parents
/family-to-do-list    → /recipe-manager、/meal-planning、/voice-to-do-list、/automatic-scheduling、/photo-to-calendar、/ai-generated-tasks、/use-cases/for-parents
/voice-to-do-list     → /family-to-do-list、/automatic-scheduling、/use-cases/for-parents
/automatic-scheduling → /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning、/voice-to-do-list、/family-to-do-list、/recipe-manager、/meal-planning、/ai-generated-tasks、/use-cases/for-parents
/photo-to-calendar    → /voice-to-calendar、/email-to-calendar、/family-to-do-list、/use-cases/for-parents
/email-to-calendar    → /voice-to-calendar、/photo-to-calendar、/call-alert、/use-cases/for-parents
/voice-to-calendar    → /photo-to-calendar、/email-to-calendar、/family-to-do-list、/use-cases/for-parents
/call-alert           → /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/use-cases/for-parents
/ai-trip-planning     → /automatic-scheduling、/family-to-do-list、/use-cases/for-families
/ai-generated-tasks   → /family-to-do-list、/automatic-scheduling、/meal-planning、/use-cases/for-caregivers
```

---

## 六、SEO 待办

| 优先级 | 动作 |
|--------|------|
| **P0** | /recipe-manager 主攻 recipe manager（4.6K）— Title、H1、首屏、内链 |
| **P0** | 首页、/automatic-scheduling 主攻 family calendar app — Title、H1、首屏 |
| **P0** | **新建 /photo-to-calendar** 主攻 photo to calendar、flyer to calendar、school flyer to calendar — 与 Photo2Calendar 竞品区隔 |
| **P0** | **新建 /email-to-calendar** 主攻 email to calendar、forward email to calendar — 与 Sense/MailToCal 竞品区隔 |
| **P0** | **新建 /call-alert** 主攻 call reminder、phone alert for events |
| **P1** | **新建 /ai-trip-planning** 主攻 AI trip planning、family trip planner、vacation itinerary |
| **P0** | /meal-planning 主攻 meal planning app（1.8K）— Title、H1、首屏、内链 |
| **P0** | /meal-planning 主攻 meal plan with grocery list、auto grocery lists — 首屏卖点、H2 |
| **P0** | 首页/导航优先展示 recipe manager、family calendar、photo to calendar、email to calendar、voice to calendar、call alert、meal planning、meal plan with grocery list 入口；链至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert |
| **P0** | 配置 301：旧 URL → 新 URL（见下表） |
| **P0** | 新建 /family-to-do-list 主攻 family to-do list、shared to-do list、与 Any.do 竞争 |
| **P1** | 新建 /voice-to-calendar 主攻 voice to calendar、voice to schedule（统一 xxx-to-calendar 模式） |
| **P1** | /automatic-scheduling 精简为 Hub 页，链出至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning |
| **P1** | /ai-generated-tasks 强化 AI generated tasks、automatic task creation |
| **P1** | 功能页与 Use Cases 互相内链 |
| **P2** | 首页/Use Cases 布局 mental load、voice first family organizer（见 nori-keywords.md §14） |
| **P2** | 博客：best family calendar app、best recipe manager app、best meal planning app for families、best shared to-do list apps for families 2026、best voice to-do list 2025 |
| **P2** | 新建 /features Hub 页（可选） |

**301 重定向**：/import-recipes-instantly → /recipe-manager | /ai-powered-meal-planning → /meal-planning | /add-anything-by-voice → /voice-to-do-list | /features/ai-generated-tasks → /ai-generated-tasks

**落地检查**：□ 301 配置完成 □ 新建 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning □ /automatic-scheduling 精简为 Hub □ 首页导航更新 □ 内链批量更新 □ nori-keywords.md 同步

---

## 七、文档导航

| 文档 | 职责 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、ICP、品牌（入口文档） |
| [nori-features.md](./nori-features.md) | **本文档**：功能页、能力、卖点、内容摘要 |
| [nori-keywords.md](./nori-keywords.md) | 关键词与目标页映射、待办、URL 模式 |
| [nori-use-cases.md](./nori-use-cases.md) | Use Cases、Persona + 情境、页面内容 |
| [nori-site-structure.md](./nori-site-structure.md) | 网站结构、孤儿页原则 |
| [nori-competitors.md](./nori-competitors.md) | 竞品分析、差异化、竞品关键词 |
| [nori-calendar-converter.md](./nori-calendar-converter.md) | Photo/Email/Voice to Calendar 汇总 |
| [nori-others.md](./nori-others.md) | Proof 索引、杂项 |
