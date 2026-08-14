# Nori 关键词与目标页面映射

> **本文档职责**：关键词与目标页映射、搜索意图、待办、URL 模式（**路径详表以本文 §11 为权威**）。  
> **引用**：功能页 Title/Meta 与模块结构见 [nori-features.md](./nori-features.md)；网站优先级见 [nori-site-structure.md](./nori-site-structure.md)；竞品关键词见 [nori-competitors.md](./nori-competitors.md)；对比截留见 [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md)；converter 见 [nori-calendar-converter.md](./nori-calendar-converter.md)；赛程见 [nori-schedules.md](./nori-schedules.md)；产品入口见 [nori.md](./nori.md)；proof 出处索引见 [nori-others.md](./nori-others.md)。  
> **维护规范**：[元文档-通用文档规范.md](../../../通用知识库/元文档-通用文档规范.md) | 通用-多文件文档联动精炼与增量循环.md

---

## 1. 主关键词表

| 意图 | 关键词 | 目标页 | 覆盖 | P |
|------|--------|--------|------|---|
| AI 家庭助手核心 | AI family assistant, AI family organizer, AI family app, AI household assistant, AI household organizer | 首页、/app | ✅ | 0 |
| **家庭组织（高量）** | **family organizer app** (4.6K), **family organizer** (4.6K) | 首页、/app | 部分 | 0 |
| 家庭日历 | family calendar app, **best family calendar app**, shared family calendar, family calendar sync | 首页、/automatic-scheduling | ✅ | 0 |
| 照片转日历（P0 核心功能） | photo to calendar, flyer to calendar, photo flyer to calendar, school flyer to calendar, snap schedule | /photo-to-calendar | ✅ | 0 |
| 邮件转日历（P0 核心功能） | email to calendar, forward email to calendar, forward schedule to calendar | /email-to-calendar | ✅ | 0 |
| 呼叫提醒（P0 核心功能） | call reminder, phone alert for events, call alert for calendar | /call-alert | ✅ | 0 |
| 旅行规划 | AI trip planning, family trip planner, vacation itinerary | /ai-trip-planning | ✅ | 1 |
| 家庭任务/清单 | family task app, family to-do app, shared family lists, **family to-do list**, **shared to-do list**, AI generated tasks, automatic task creation | 首页、**/family-to-do-list**、/ai-generated-tasks | ✅ | 1 |
| 餐食规划 | **meal planning app** (1.8K), family meal planning app, AI meal planning, meal planner for families | /meal-planning | ✅ | 1 |
| 拍冰箱→食谱建议（P0 核心功能） | fridge to recipe, recipe suggestions from fridge, photo fridge to meal ideas | /meal-planning | ✅ | 0 |
| 餐食规划→自动购物清单（P0 核心功能） | meal plan with grocery list, auto grocery lists, automatic shopping list from meal plan | /meal-planning | ✅ | 0 |
| 食谱导入 | **recipe manager** (4.6K), recipe organizer, import recipes, save recipes from website, recipe scanner | /recipe-manager | ✅ | 1 |
| 购物清单 | family shopping list app, shared shopping list | 首页、/meal-planning | ✅ | 1 |
| 语音转日历（P1） | voice to calendar, voice to schedule, hands-free scheduling | /voice-to-calendar | ✅ | 1 |
| 语音任务 | voice to-do list app, voice to-do list, voice calendar, speak to schedule | /voice-to-do-list | ✅ | 1 |
| 竞品替代 | Cozi alternative, FamilyWall alternative, Sense alternative, Kora alternative | 待建 /comparison | ❌ | 1 |
| 移动端 | family calendar app Android, family calendar app iOS, best family app iPhone, family organizer app mobile | 首页、/download | 部分 | 1 |
| 工具选型 | **best family calendar app**, best AI family organizer, best family calendar app 2025, **best meal planning app** | 首页、博客 | 部分 | 1 |
| 长尾 | AI family calendar for busy parents, family organizer with meal planning, **AI family manager**, **manage family with AI**, family manager app | 专题 [nori-ai-family-manager.md](./nori-ai-family-manager.md)；落地 /automatic-scheduling、/meal-planning | 部分 | 2 |
| 心理负担 | mental load family app, reduce mental load parents | 首页、/use-cases/for-parents | 部分 | 1 |
| 语音+家庭 | voice first family organizer, hands-free family organizer | /voice-to-calendar、/voice-to-do-list | 部分 | 1 |
| 学校传单 | school flyer to calendar, photo flyer to calendar | /photo-to-calendar | ✅ | 0 |

**覆盖**：✅ 已覆盖 | ❌ 未覆盖 | 部分 = 部分已覆盖  
**量级说明**：括号内为月搜索量参考（K=千），数据来源 Clicks.so、ASOTools

---

## 2. 功能关键词表

### 2.1 核心能力

| 功能 | 关键词 | URL |
|------|--------|-----|
| 家庭日历 | family calendar, shared calendar, family schedule | 首页 |
| 家庭任务 | family tasks, family to-do, shared task list, family to-do list, shared to-do list | 首页、/family-to-do-list |
| 食谱 | family recipes, recipe organizer, recipe manager, import recipes | 首页、/recipe-manager |
| 餐食规划 | meal planning, meal plan, dinner planner, AI meal planner, AI-powered meal planning | /meal-planning |
| 购物清单 | shopping list, grocery list, shared shopping list | 首页 |

### 2.2 输入方式

| 方式 | 关键词 | URL |
|------|--------|-----|
| 语音（日历） | voice to schedule, voice to calendar, hands-free scheduling, speak to add event | /voice-to-calendar |
| 语音（任务） | voice to-do list, voice calendar app | /voice-to-do-list |
| 照片 | photo to calendar, snap flyer to calendar, photo schedule capture | /photo-to-calendar |
| 邮件 | email to calendar, forward email to schedule | /email-to-calendar |

### 2.3 高级功能

| 功能 | 关键词 | URL |
|------|--------|-----|
| 电话提醒 | call reminder, phone alert for events | /call-alert |
| 旅行规划 | AI trip planning, family trip planner, vacation itinerary | /ai-trip-planning |
| 餐食规划（独立页） | AI meal planner, AI-powered meal planning, allergy-aware meal planning, family meal planner | /meal-planning |
| 日历同步 | family calendar sync, Google Calendar family, Apple Calendar family | 首页 |
| 多端/硬件 | family AI device, AI family hub, smart home family assistant | 首页、/download |
| 语音（日历） | voice to calendar app, hands-free scheduling app | /voice-to-calendar |
| 语音（任务） | voice to-do list app, best voice to-do list app, voice grocery list | /voice-to-do-list |
| AI 任务 | AI generated tasks, automatic task creation, AI to-do list, voice to task, AI project breakdown | /ai-generated-tasks |
| 照片/邮件 | photo flyer to calendar, school flyer to calendar, email to calendar automatic | /photo-to-calendar、/email-to-calendar |
| 食谱导入 | recipe manager, recipe organizer, import recipes, save recipes from website, recipe scanner | /recipe-manager |

---

## 3. 受众与场景

| 受众 | 关键词 | URL |
|------|--------|-----|
| 忙碌家长 | family organizer for busy parents, parent calendar app | 首页、/use-cases/for-parents |
| 多孩家庭 | family calendar for multiple kids, family schedule app | 首页、/use-cases/for-parents |
| 祖父母 | family organizer for grandparents | 首页、/use-cases/for-grandparents |
| Daycare 家长 | family calendar for daycare parents, organize preschool schedule, daycare pickup schedule | /use-cases/for-parents |
| 照护协调 | family caregiver coordination, elder care schedule, multi-generational family calendar | /use-cases/for-caregivers |
| 保姆/看护 | family calendar for nanny, babysitter schedule access | /use-cases/for-parents |
| 轻量共同抚养 | shared calendar for co-parents | /use-cases/for-parents |
| Sports/课外活动 | family calendar for sports parents, manage kids activities, extracurricular schedule | /use-cases/for-parents |
| 家务/Chores | family chore app, chore tracker for kids | /use-cases/for-parents |
| 混合家庭 | blended family calendar, stepfamily organizer | /use-cases/for-parents |
| ADHD/神经多样性 | family organizer for ADHD, neurodivergent family calendar | /use-cases/for-parents |
| 宠物 | family calendar for pets, pet vet appointment, pet food reminder | /use-cases/for-families |
| 家务管理 | home maintenance schedule, household task reminder | /use-cases/for-families |

---

## 4. 扩展关键词（锚定 AI family assistant）

| 类型 | 关键词 | 目标页 | 说明 |
|------|--------|--------|------|
| 核心变体 | AI household assistant, AI household organizer, family scheduling app, smart family calendar | 首页、/use-cases/for-families | 更通用家庭/家务管理 |
| Daycare/学前 | family calendar for daycare parents, organize preschool schedule, daycare pickup schedule | /use-cases/for-parents | 家长端，非园所 B2B |
| 老人照护 | family caregiver coordination, elder care schedule, family calendar for aging parents | /use-cases/for-caregivers | 子女协调照护 |
| 多代家庭 | multi-generational family calendar | /use-cases/for-grandparents、/use-cases/for-families | 祖父母 + 父母 + 子女 |
| 保姆/看护 | family calendar for nanny, babysitter schedule access | /use-cases/for-parents | 共享访问 |
| 共同抚养（轻量） | shared calendar for co-parents | /use-cases/for-parents | 共享日历，非法律文档 |
| Sports/课外活动 | family calendar for sports parents, manage kids sports schedule, extracurricular calendar | /use-cases/for-parents | 拍日程表→日历，语音调度 |
| Chores | family chore app, chore tracker for families | /use-cases/for-parents | 任务功能覆盖 |
| ADHD/神经多样性 | family organizer for ADHD, neurodivergent family calendar | /use-cases/for-parents | 语音优先、减轻脑力负担 |
| 混合家庭 | blended family calendar, stepfamily organizer | /use-cases/for-parents | 复杂家庭结构 |
| Pets | family calendar for pets, pet vet appointment, pet food reminder | /use-cases/for-families | 兽医预约、宠物用品 |
| Home maintenance | home maintenance schedule, household task reminder | /use-cases/for-families | 账单、保养等周期性任务 |

**不覆盖**：daycare management software（园所 B2B）、co-parenting app / custody schedule（需法院文档）、caregiver handover app（婴儿喂养/睡眠记录）。

---

## 5. 移动端关键词

| 类型 | 关键词 | 目标页 | 说明 |
|------|--------|--------|------|
| 平台通用 | family calendar app, family organizer app, shared family calendar app | 首页、/download | 主词 |
| Android | family calendar app Android, best family app Android, family organizer app Android | /download | Android 用户 |
| iOS | family calendar app iOS, best family app iPhone, family organizer app iPhone, family app iPad | /download | iOS 用户 |
| 工具选型 | best family calendar app 2025, best AI family organizer app, best family scheduling app | 首页、博客、/download | 选型意图 |
| 下载 | family calendar app download, AI family organizer free | /download | 下载意图 |

---

## 6. 竞品关键词

| 类型 | 关键词 | 目标页 | 说明 |
|------|--------|--------|------|
| 竞品替代 | Cozi alternative, FamilyWall alternative, Sense alternative, Kora alternative, Fami alternative, Maple alternative, **Any.do alternative**, **Paprika alternative** | 待建 /comparison/*、/family-to-do-list、/recipe-manager | 替代竞品 |
| 对比 | Nori vs Cozi, Nori vs FamilyWall, Nori vs Sense, Nori vs Kora, Cozi vs Nori | 待建 /comparison/* | 对比搜索 |
| 工具选型 | best family calendar app, best AI family organizer, best family organizer app 2025 | 首页、博客 | 选型 |
| 品牌 | Nori app, Nori family AI, Nori family organizer | 全站 | 品牌词 |

---

## 7. 待办（优先级）

| P | 待办 | 说明 |
|---|------|------|
| **0** | 查 GSC/GA4：/voice-to-do-list 流量占比 | 决策 voice 页是否合并入 /automatic-scheduling |
| **0** | 首页强化 AI family assistant、family calendar app | 主关键词 title/meta/H1 |
| **0** | **新建 /photo-to-calendar** 主攻 photo to calendar、flyer to calendar、school flyer to calendar | P0 核心功能 |
| **0** | **新建 /email-to-calendar** 主攻 email to calendar、forward email to calendar | P0 核心功能 |
| **0** | **新建 /call-alert** 主攻 call reminder、phone alert for events | P0 核心功能 |
| **0** | /meal-planning 强化 fridge to recipe、recipe suggestions from fridge | P0 核心功能；首屏卖点、H2 |
| **0** | /meal-planning 强化 meal plan with grocery list、auto grocery lists | P0 核心功能；首屏卖点、H2 |
| **1** | **新建 /ai-trip-planning** 主攻 AI trip planning、family trip planner、vacation itinerary | 家庭行程规划 |
| **1** | 新建 Nori vs Cozi、vs FamilyWall、vs Sense、vs Kora 对比页 | 竞品替代词有搜索量 |
| **1** | **新建 /voice-to-calendar** 主攻 voice to calendar、voice to schedule | 统一 xxx-to-calendar 模式 |
| **1** | /automatic-scheduling 精简为 Hub 页，链出至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning | 内容分散至子页 |
| **2** | 博客 How-to 长尾 | how to organize family schedule、AI meal planning for families；见 [nori-blog.md](./nori-blog.md) |
| **2** | /meal-planning 内链与长尾 | 从首页、/automatic-scheduling 链入；覆盖 AI meal planner、allergy-aware meal planning |
| **2** | 工具选型文章 | best AI family organizer 2025、best family calendar app；见 [nori-blog.md](./nori-blog.md) |
| **1** | 新建 /use-cases/for-parents、/for-grandparents、/for-caregivers | 见 §9 Use Cases |
| **1** | 首页增加 AI household assistant、household organizer | 扩展核心词 |
| **1** | /download 页强化移动端关键词 | family calendar app Android/iOS、best family app iPhone |
| **1** | 新建 /family-to-do-list 主攻 family to-do list、shared to-do list、与 Any.do 竞争 | 见 [nori-features.md](./nori-features.md) §四 |
| **1** | /voice-to-do-list 定位为 voice 输入专项，链入 /family-to-do-list | 见 [nori-features.md](./nori-features.md) §五 |
| **1** | /ai-generated-tasks 强化 AI generated tasks | 见 [nori-features.md](./nori-features.md) §四 |
| **1** | /recipe-manager 强化 recipe manager、import recipes | 见 [nori-features.md](./nori-features.md) §四 |
| **1** | /photo-to-calendar 强化 school flyer to calendar、photo flyer to calendar | 见 §17 竞品关键词参考 |
| **1** | 首页/Use Cases 布局 mental load、voice first family organizer | 见 §14 Nori 可拓展核心词 |
| **1** | 301 配置：旧 URL → 新 URL；内链更新 | 见 [nori-features.md](./nori-features.md) §2、§6 |

**落地检查**：□ GSC 流量分析完成 □ 301 配置 □ 新建 /photo-to-calendar、/email-to-calendar、/call-alert、/ai-trip-planning □ /automatic-scheduling 精简为 Hub □ 内链批量更新

---

## 8. 功能页信息

### 8.1 /family-to-do-list（新建，主任务页）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/family-to-do-list |
| **Title** | Family To-Do List App \| Shared Lists, Voice & Photo Input \| Nori |
| **目标词** | family to-do list, shared to-do list, family to-do list app, shared to-do list app for families |
| **核心卖点** | 与 Any.do 竞争；Voice/Photo/Email 多模态输入；Calendar + Meals + Shopping 一体化 |
| **差异化** | "The only family to-do app that adds tasks by voice, photo, or email—no typing." |

### 8.2 /voice-to-do-list（语音输入专项）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/voice-to-do-list |
| **Title** | Add Anything by Voice with Nori \| Organize Family Life Hands-Free |
| **目标词** | voice to-do list, voice to-do list app, hands-free scheduling, voice to calendar |
| **核心卖点** | Smart Categorization、Shared by Design、Family Context Aware |
| **定位** | Voice 作为输入方式之一；链入 /family-to-do-list |

### 8.3 /ai-generated-tasks

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/ai-generated-tasks |
| **Title** | AI-Generated Tasks for Families \| Automatic Task Creation \| Nori |
| **目标词** | AI generated tasks, automatic task creation, AI to-do list, voice to task |
| **核心卖点** | Capture→Understand→Assign；AI 项目分解；Tasks↔Meals↔Calendar 联动 |

### 8.4 /meal-planning（意图：规划吃什么）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/meal-planning |
| **Title** | Meal Planning App for Families \| AI Meal Planner, Grocery Lists \| Nori |
| **核心卖点** | Allergy-aware、周菜单、自动购物清单、冰箱匹配、家庭同步 |
| **场景** | Busy Weeknight Rush、Allergy-Conscious Home、Special Family Events、Grocery Shopping Made Easy |
| **差异化** | Family-First Intelligence、Context-Aware Memory、Truly Hands-Free、Privacy Safe |
| **目标词** | meal planning app (1.8K)、AI meal planner、allergy-aware meal planning、family meal planner、meal plan with grocery list、fridge to recipe |

### 8.5 /recipe-manager（意图：管理/导入食谱）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/recipe-manager |
| **Title** | Recipe Manager App \| Import & Save Recipes from Any Website \| Nori |
| **目标词** | recipe manager (4.6K), recipe organizer, import recipes, save recipes from website, recipe scanner |
| **核心卖点** | paste link / upload screenshot / scan handwritten → AI 提取；allergy-aware；家庭同步；与 meal planning 联动 |
| **场景** | Grandma's Book、TikTok Link Chaos、Allergy Filter、Save from Any Website |

### 8.6 /automatic-scheduling（Hub 页）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/automatic-scheduling |
| **Title** | Family Calendar App \| Shared Schedule, Voice & Photo Input \| Nori |
| **目标词** | family calendar app, best family calendar app, shared family calendar, automatic scheduling, AI calendar assistant |
| **定位** | Hub 页；链出至 /photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning、/voice-to-do-list |

### 8.7 /photo-to-calendar、8.8 /email-to-calendar、8.9 /voice-to-calendar（新建，P0/P1）

*完整内容见 [nori-calendar-converter.md](./nori-calendar-converter.md)。统一 xxx-to-calendar URL 模式。*

| 页 | 目标词 |
|----|--------|
| /photo-to-calendar | photo to calendar, flyer to calendar, school flyer to calendar |
| /email-to-calendar | email to calendar, forward email to calendar |
| /voice-to-calendar | voice to calendar, voice to schedule |

### 8.10 /call-alert（新建，P0）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/call-alert |
| **Title** | Call Alert for Family Calendar \| Never Miss Pickup or Appointments \| Nori |
| **目标词** | call reminder, phone alert for events, call alert for calendar |
| **核心卖点** | 重要事件电话呼叫提醒；接娃、训练、预约不再遗忘 |

### 8.11 /ai-trip-planning（新建）

| 项目 | 内容 |
|------|------|
| **URL** | https://heynori.com/ai-trip-planning |
| **Title** | AI Trip Planning for Families \| Hawaii, Disney & Vacation Itinerary \| Nori |
| **目标词** | AI trip planning, family trip planner, vacation itinerary |
| **核心卖点** | 计划家庭旅行→AI 生成行程→加入家庭日历 |

---

## 9. Use Cases 页面规划

| 页面 | URL | 覆盖人群 | 目标关键词 |
|------|-----|----------|------------|
| For parents | /use-cases/for-parents | 忙碌家长、职场父母、多孩、daycare、保姆、共同抚养、sports、chores、ADHD、混合家庭 | family organizer for busy parents, family calendar for daycare parents, family calendar for sports parents, family chore app, family organizer for ADHD, shared calendar for co-parents, blended family calendar |
| For grandparents | /use-cases/for-grandparents | 祖父母、多代家庭 | family organizer for grandparents, multi-generational family calendar |
| For caregivers | /use-cases/for-caregivers | 子女照护老人、照护协调 | family caregiver coordination, elder care schedule, family calendar for aging parents |
| For families | /use-cases/for-families | 通用家庭、宠物、家务管理 | AI household assistant, household organizer, family calendar for pets, home maintenance schedule |

**URL 原则**：按 persona 区分，URL 通用化（不区分 busy/working parents）。

---

## 10. 产品形态（App + 硬件）

| 形态 | 说明 | 链接 |
|------|------|------|
| **Web** | 在线试用 | heynori.com/app |
| **iOS** | iPhone、iPad | App Store |
| **Android** | 手机、平板（50K+ 下载、4.6 评分） | [Google Play](https://play.google.com/store/apps/details?id=ai.domusnext.nori) |
| **Family Hub** | 家庭端 AI 硬件设备（计划 2026 年 6 月） | 待公布 |

**定价**：核心功能免费；高级 AI 与硬件集成按需升级。

**竞品品牌词 / 对比意图**（含 *digital wall calendar*、*cozi alternative*、*photo2calendar* 等）：承接页规划见 [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md)。

---

## 11. URL 模式

| 类型 | 模式 | 示例 |
|------|------|------|
| 首页 | / | heynori.com |
| 应用 | /app | 在线试用 |
| 功能页 | /automatic-scheduling | 家庭日历 Hub（链出至子页） |
| 功能页 | /photo-to-calendar | 照片转日历（photo to calendar） |
| 功能页 | /email-to-calendar | 邮件转日历（email to calendar） |
| 功能页 | /voice-to-calendar | 语音转日历（voice to calendar） |
| 功能页 | /call-alert | 呼叫提醒（call reminder） |
| 功能页 | /ai-trip-planning | AI 行程规划（family trip planner） |
| 功能页 | /family-to-do-list | 家庭 to-do（主任务页，与 Any.do 竞争） |
| 功能页 | /voice-to-calendar | 语音转日历（voice to calendar） |
| 功能页 | /voice-to-do-list | 语音输入专项（voice to-do list） |
| 功能页 | /meal-planning | 餐食规划（meal planning app） |
| 功能页 | /recipe-manager | Recipe Manager（recipe manager） |
| 功能页 | /ai-generated-tasks | AI 任务生成（AI generated tasks） |
| Use Cases | /use-cases/{persona} | for-parents, for-grandparents, for-caregivers, for-families |
| 下载 | /download | 下载页（含 Web、iOS、Android 入口） |
| 对比页 | 待建 /comparison/{slug} | nori-vs-cozi |
| **程序化** | /schedules/{league}/{team-slug} | /schedules/mlb/minnesota-twins, /schedules/nfl/philadelphia-eagles（待建；见 [nori-schedules.md](./nori-schedules.md)） |
| **程序化** | /schedules/school/{district}、/schedules/holidays/{region} | 学校日历、公共假期（Phase 4；见 nori-schedules） |
| **程序化 Hub** | /schedules、/schedules/mlb、/schedules/nfl 等 | 赛程 Hub；联赛入口（先做） |
| 帮助 | help.heynori.com | 帮助中心 |

---

## 12. 程序化页面关键词（体育赛程与扩展方向）

*完整规划见 [nori-schedules.md](./nori-schedules.md)*

| 类型 | 关键词 | 目标页 | 说明 |
|------|--------|--------|------|
| **MLB** | Minnesota Twins schedule, Houston Astros schedule, Yankees schedule | /schedules/mlb/{team-slug} | 30 队；参考 Cozi |
| **NFL** | Eagles schedule, Cowboys schedule | /schedules/nfl/{team-slug} | 32 队 |
| **NBA** | Lakers schedule, Celtics schedule | /schedules/nba/{team-slug} | 30 队 |
| **NHL** | Bruins schedule, Rangers schedule | /schedules/nhl/{team-slug} | 32 队 |
| **学校日历** | NYC school calendar 2025-2026, CPS school holidays, LAUSD calendar, add school calendar | /schedules/school/{district-slug} | 13,000+ 学区；家长刚需；Cozi 支持 |
| **公共假期** | US holidays 2026, federal holidays calendar, add holidays to calendar | /schedules/holidays/us、/schedules/holidays/{state} | iCal 数据源成熟 |
| **电影上映** | Marvel movies 2026 release dates, Disney+ new releases | /schedules/movies/2026 | 高搜索量；家庭娱乐 |
| **场景** | family calendar for sports parents, add team schedule to family calendar | /use-cases/for-parents、程序化页 | 与 sports parents 场景契合 |

**前提**：需日历订阅能力（iCal/ICS）；若无，先做 Photo to Calendar + 体育赛程教育内容。

---

## 13. 用户意图与 SEO 洞察

| 意图类型 | 特征 | 目标页策略 |
|----------|------|------------|
| **工具选型** | best X app、best X for families、X 2025 | 首页、功能页、博客 |
| **问题解决** | reduce mental load、hands-free、allergy-aware | 功能页、Use Cases |
| **场景驱动** | busy parents、working moms、ADHD | Use Cases |
| **功能搜索** | voice to X、photo to calendar、AI meal planner | 功能页 |
| **替代搜索** | X alternative、vs X | 待建 /comparison |

---

## 14. 核心词搜索量优化

**数据来源**：Clicks.so、ASOTools（具体以 Ahrefs/SEMrush 为准）

| 当前词 | 更高量级替代 | 量级参考 |
|--------|--------------|----------|
| AI family organizer（单独） | family organizer app | 4,605/月 |
| meal planner for families | meal planning app | 1,800/月 |
| voice to-do list（无 app） | voice to-do list app | 加 app 意图更明确 |
| shared family calendar（单独） | family calendar app | 主词量更高 |

**优化原则**：高量词（family organizer app、meal planning app）主攻流量；差异化词（AI family assistant、hands-free）保留转化；工具选型词（best X app）用于博客与列表页。

**具体动作**：首页 title 含 family organizer app 或 family calendar app；/meal-planning 将 **meal planning app** 放 title 靠前（1.8K）；/recipe-manager 将 **recipe manager** 放 title 靠前（4.6K）；/voice-to-do-list 强化 voice to-do list app；博客高量词见 [nori-blog.md](./nori-blog.md)。

---

## 15. Nori 可拓展核心关键词

> 基于产品能力 + 搜索趋势，有能力覆盖但尚未充分布局的词

| 关键词 | 建议目标页 |
|--------|------------|
| mental load family app, reduce mental load parents | 首页、/use-cases/for-parents |
| voice first family organizer, hands-free family organizer | /voice-to-calendar、/voice-to-do-list、首页 |
| multi-modal family calendar, AI family scheduling | /automatic-scheduling |
| school flyer to calendar, photo to family calendar | /photo-to-calendar |
| family chore app AI, ADHD family organizer voice | /ai-generated-tasks、/use-cases/for-parents |
| shared family shopping list voice, family calendar app voice | 首页、/voice-to-calendar、/voice-to-do-list |
| AI household task manager, forward email to family calendar | /ai-generated-tasks、/email-to-calendar |

---

## 16. 长尾词汇总（按目标页）

| 目标页 | 长尾词 |
|--------|--------|
| /family-to-do-list | family to-do list app, shared to-do list for families, best family to-do list app, family task app with voice |
| /voice-to-calendar | voice to calendar app, hands-free scheduling for busy parents, voice to schedule |
| /voice-to-do-list | voice to-do list app for families, best voice to-do list app 2025, voice grocery list app, voice task manager for ADHD, organize by voice, hands-free family organizer |
| /automatic-scheduling | family calendar app, AI calendar assistant for families, multi-modal family calendar |
| /photo-to-calendar | photo flyer to calendar, school flyer to calendar, screenshot to calendar, photo to family calendar |
| /email-to-calendar | email to calendar automatic, forward email to family calendar |
| /call-alert | calendar call reminder, event phone alert |
| /ai-trip-planning | AI itinerary builder, family vacation planner |
| /meal-planning | AI meal planner for families with allergies, meal planning for busy families, AI dinner planner, weekly meal plan AI, nut-free meal planner, gluten-free family meals, picky eater meal planning |
| /recipe-manager | recipe manager app, import recipes from website, save recipes from website, recipe scanner app, digitize cookbook |
| /ai-generated-tasks | AI generated tasks for families, voice to task app, AI project breakdown, break down goals into tasks, family task app with AI, assign tasks to family members AI, AI household task manager, family chore app AI |
| 首页 / Use Cases | mental load family app, reduce mental load parents, voice first family organizer, AI family scheduling, ADHD family organizer voice, family calendar app voice, family calendar for busy parents, family organizer for working moms |

---

## 17. 竞品关键词参考（功能页 SEO）

| 竞品 | 目标词 | Nori 对应 |
|------|--------|-----------|
| **Cozi** | family organizer app, family calendar app, shared family calendar, Cozi alternative, best family organizer app, Cozi vs Nori | 首页、/automatic-scheduling、待建 /comparison/nori-vs-cozi |
| WhisperPlan | voice to-do list, voice task manager ADHD | /voice-to-do-list |
| **Tiimo**（邻近） | tiimo, visual planner app, ADHD planner, AI planner app（与 family calendar 主意图弱重叠） | 长尾 listicle、/voice-to-do-list 或 Use Cases（ADHD 家庭）；可选 `/nori-vs-tiimo`（P2） |
| Photo2Calendar / EventSnap / Snap Event / Image2Cal / Calendara / Smart Calendars AI | photo to calendar, flyer to calendar, school flyer to calendar, screenshot to calendar | /photo-to-calendar |
| AddToCal / MailToCal / Sense | email to calendar, forward to calendar | /email-to-calendar |
| MentalLoad / FamilyOps | mental load app, reduce mental load | 首页、Use Cases |
| TaskGen / Taskade | AI generated tasks, auto task creation | /ai-generated-tasks |
| Musely / PlanMate | AI meal planner, allergy meal planning | /meal-planning |
| **Any.do** | family to-do list, shared to-do list, family task app | /family-to-do-list |
| **Paprika / Recipe Keeper** | recipe manager, recipe organizer, import recipes | /recipe-manager |
| **Grocery AI** | grocery list maker, grocery list app, AI shopping list, photo to grocery list, pantry inventory | /family-to-do-list、/meal-planning、/recipe-manager |
| **AnyList** | grocery shopping list app, shared grocery list, best shopping list app, Siri grocery list, recipe to shopping list | /family-to-do-list、/meal-planning、/recipe-manager |

---

---

## 18. 搜索意图聚类（功能页规划参考）

| 意图 | 用户要什么 | 关键词簇 | 目标页 | 搜索量 |
|------|------------|----------|--------|--------|
| **免输入添加** | 免打字添加事件/任务 | voice to schedule, photo to calendar, email to calendar, hands-free scheduling, voice to-do list, school flyer to calendar, AI calendar assistant | /automatic-scheduling（Hub）、/photo-to-calendar、/email-to-calendar、/voice-to-do-list | 各子页独立覆盖 |
| **家庭任务/清单** | 共享清单、任务分配 | family to-do list, shared to-do list, family chore app, family task app；子意图：AI generated tasks, voice to task | /family-to-do-list、/ai-generated-tasks | — |
| **餐食规划** | 规划吃什么、周菜单 | meal planning app (1.8K), AI meal planner, allergy-aware, meal plan with grocery list, fridge to recipe | /meal-planning | meal planning app 1.8K |
| **食谱管理** | 保存、导入、整理食谱 | recipe manager (4.6K), recipe organizer, import recipes, save recipes from website, recipe scanner | /recipe-manager | recipe 4.6K > meal 1.8K，保持独立 |

---

## 19. 文档导航

| 文档 | 职责 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、ICP（入口文档） |
| [nori-blog.md](./nori-blog.md) | Blog 内容策略、主题、关键词 |
| [nori-features.md](./nori-features.md) | 功能页、能力、内容摘要 |
| [nori-keywords.md](./nori-keywords.md) | **本文档**：关键词映射、待办、URL 模式 |
| [nori-use-cases.md](./nori-use-cases.md) | Use Cases、Persona + 情境 |
| [nori-site-structure.md](./nori-site-structure.md) | 网站结构、URL 优先级 |
| [nori-competitors.md](./nori-competitors.md) | 竞品分析、竞品关键词 |
| [nori-calendar-converter.md](./nori-calendar-converter.md) | Photo/Email/Voice to Calendar 汇总 |
| [nori-others.md](./nori-others.md) | Proof 索引、杂项 |
