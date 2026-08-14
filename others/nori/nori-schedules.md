# Nori 赛程页面规划（体育赛程与扩展方向）

> 关联：[nori.md](./nori.md) | [nori-keywords.md](./nori-keywords.md) | [nori-site-structure.md](./nori-site-structure.md) | [nori-features.md](./nori-features.md) | [nori-use-cases.md](./nori-use-cases.md)
> 参考：Cozi MLB 赛程、学校日历、体育导入；Nori 路由：/schedules/mlb、/schedules/mlb/{team-slug} 等
> 基于网络调研与竞品分析（2025 年 3 月）

---

## 一、方向概览

| 方向 | 可行性 | 规模 | 搜索量 | 产品契合 |
|------|--------|------|--------|----------|
| **体育赛程**（MLB/NFL/NBA/NHL） | **高** | 120+ 页 | 高 | 家庭日历、sports parents |
| **学校/学区日历** | **高** | 13,000+ 学区 | **极高** | 家长刚需；Cozi 专门支持；school flyer to calendar |
| **公共假期/节日** | **高** | 按国家/州 | 高 | 基础需求；iCal 数据源成熟（CalendarLabs、Hebcal 等） |
| **电影/电视剧上映日** | 中高 | 按年度/IP | 高（如 Marvel 电影 80 万+/月） | 家庭娱乐计划 |
| 演唱会/巡演 | 中 | 按艺人/城市 | 中 | 家庭出行、购票规划 |
| 主题公园活动 | 中 | 按园区 | 中 | 家庭旅行；季节性活动（万圣节、圣诞节） |
| 宗教节日 | 中 | 按宗教 | 中 | Cozi 已支持；多元文化家庭 |
| 游戏发售日 | 低 | 按平台 | 中 | 青少年家庭、生日礼物 |
| 天文/自然事件 | 低 | 少量 | 低 | 家庭户外活动 |
| 食谱（食材） | 低 | 大量 | 中 | 易稀释主定位 |

**优先推荐**：体育赛程（已验证）→ 学校日历、公共假期（模板可复用、搜索量最大）

---

## 二、体育赛程程序化页（主方向）

### 2.1 产品与关键词契合

| Nori 能力 | 对应场景 | 关键词 |
|-----------|----------|--------|
| 家庭日历 | 体育家长、课外活动 | family calendar for sports parents, manage kids activities |
| Photo to Calendar | 拍赛程表/传单→日历 | school flyer to calendar, photo flyer to calendar |
| 日历同步 | 订阅赛程到家庭日历 | [team name] schedule, add to calendar |

### 2.2 URL 与规模

| 联赛 | URL 示例 | 规模 |
|------|----------|------|
| **MLB** | /schedules/mlb/minnesota-twins, /schedules/mlb/houston-astros | 30 页 |
| **NFL** | /schedules/nfl/philadelphia-eagles, /schedules/nfl/dallas-cowboys | 32 页 |
| **NBA** | /schedules/nba/lakers, /schedules/nba/boston-celtics | 30 页 |
| **NHL** | /schedules/nhl/boston-bruins, /schedules/nhl/new-york-rangers | 32 页 |

**Hub 页**：/schedules（主入口）；/schedules/mlb、/schedules/nfl、/schedules/nba、/schedules/nhl（联赛入口）

### 2.3 页面结构（参考 Cozi）

| 区块 | 内容 |
|------|------|
| **H1** | [Team Name] Schedule |
| **说明** | 将 [球队] 赛程加入 Nori 家庭日历 |
| **CTA** | Add Schedule to Nori |
| **管理** | Family > Settings > Manage Calendars |
| **差异化** | 也可拍赛程传单，用 Photo to Calendar 一键添加 |
| **内链** | Back to [League] Schedules（/schedules/mlb 等） |

### 2.4 Nori 差异化

- **Photo to Calendar**：除订阅外，可拍赛程传单/海报，AI 提取→日历
- **语音**：语音添加单场比赛
- **Call Alert**：重要比赛/接送时间电话提醒

### 2.5 落地前提

| 前提 | 说明 |
|------|------|
| **日历订阅能力** | 需支持 Internet Calendar 订阅（iCal/ICS），类似 Cozi 的 Stanza API |
| **数据源** | MLB/NFL/NBA/NHL 官方或第三方赛程数据 |
| **Hub 页** | /schedules；联赛入口 /schedules/mlb、/schedules/nfl 等 |

---

## 三、扩展方向（三梯队，按 SEO 搜索量和家庭实用性排序）

### 3.1 第一梯队：高搜索量 + 高家庭需求

| 类型 | 搜索意图示例 | 为什么适合 Nori | 数据来源/规模 |
|------|--------------|-----------------|---------------|
| **学校日历** | "NYC school calendar 2025-2026"、"CPS school holidays"、"LAUSD calendar" | 家长刚需；半天、假期、家长会等事件频繁。**Cozi 专门支持**：iCal 导入或手动添加；学校日历为 Connected Calendars 核心场景 | 美国约 **13,000+ 学区**；NYC 等大学区提供 Google/Outlook/Apple 订阅；多语言 PDF |
| **公共假期/节日** | "US holidays 2026"、"federal holidays calendar"、"add holidays to calendar" | 基础需求；影响家庭出行和孩子放假。可按国家/州细分 | iCal 数据源成熟：CalendarLabs、CalendarHolidays.net、TrueCalendar；11 个联邦假日 + 各州 |
| **电影/电视剧上映日** | "Marvel movies 2026 release dates"、"Disney+ new releases"、"Avengers Doomsday 2026" | 家庭娱乐计划；有孩子的家庭高度关注。搜索量高且时效性强 | 例：Avengers Doomsday **82.3 万/月**、Spider-Man 2026 **36.8 万/月**（Google 数据） |

### 3.2 第二梯队：中等搜索量 + 强家庭场景

| 类型 | 搜索意图示例 | 为什么适合 Nori |
|------|--------------|-----------------|
| **演唱会/巡演** | "Taylor Swift tour 2026 dates"、"concert schedule [city]" | 家庭出行规划；需提前买票和安排接送 |
| **主题公园活动** | "Disneyland events 2026"、"Universal Studios schedule"、"Disneyland Halloween 2026" | 家庭旅行核心场景；季节性活动（万圣节 8–10 月、圣诞节 11–12 月）需提前规划 |
| **宗教节日** | "Jewish holidays 2026"、"Ramadan 2026 dates"、"Easter 2026" | **Cozi 已支持**；多元文化家庭的强需求；Hebcal、CalendarHolidays 提供 iCal |

### 3.3 第三梯队：差异化 + 长尾价值

| 类型 | 搜索意图示例 | 为什么适合 Nori |
|------|--------------|-----------------|
| **游戏发售日** | "Nintendo Switch games 2026"、"PS5 release dates" | 有青少年的家庭高度关注；生日礼物计划 |
| **天文/自然事件** | "solar eclipse 2026"、"meteor shower dates 2026" | 家庭户外活动灵感；高分享性内容 |
| **本地社区活动** | "farmers market schedule [city]"、"library story time" | 强本地 SEO 价值；内容生成成本高 |

### 3.4 竞品参考：Cozi 日历导入能力

| 类型 | Cozi 支持方式 |
|------|---------------|
| **学校日历** | iCal 自动导入；或手动添加；Connected Calendars 功能 |
| **体育赛程** | TeamSnap、SportsEngine、ArbiterSports、Crossbar 等平台自动导入 |
| **宗教/节日** | 导入 Holidays、Sports Teams 等日历 |
| **通用** | Google、Apple、Outlook 日历同步 |

### 3.5 URL 与规模（扩展方向）

| 类型 | URL 示例 | 规模 |
|------|----------|------|
| 学校日历 | /schedules/school/nyc、/schedules/school/lausd、/schedules/school/[district-slug] | 13,000+ 学区；可先做 Top 100 大学区 |
| 公共假期 | /schedules/holidays/us、/schedules/holidays/[state] | 按国家/州；11 联邦 + 各州 |
| 电影上映 | /schedules/movies/2026、/schedules/movies/marvel-2026 | 按年度/IP |
| 宗教节日 | /schedules/holidays/jewish-2026、/schedules/holidays/ramadan-2026 | 按宗教/年 |

### 3.6 模板复用性

- **学校日历、公共假期** 与体育赛程共享相似数据结构：**日期 + 事件名 + 地点**
- 页面模板可复用；数据源不同（学区官网 vs 体育联盟 API）
- 学校日历数据分散、地域性强；需按学区/州聚合；NYC、LAUSD、CPS 等大学区优先

---

## 四、落地优先级

| 阶段 | 动作 |
|------|------|
| **Phase 1** | 确认是否有日历订阅/feed 能力；若无，先做「Photo to Calendar + 体育赛程」教育内容 |
| **Phase 2** | 若有订阅能力，优先 **MLB 30 队**（与 Cozi 同赛道，已验证） |
| **Phase 3** | 扩展 NFL、NBA、NHL |
| **Phase 4** | **学校日历** 与 **公共假期**（模板可复用、搜索量最大；学校日历数据源：学区官网 iCal；假期：CalendarLabs、Hebcal 等） |
| **Phase 5** | 电影/电视剧上映日（高搜索量；需评估数据源与更新频率） |
| **Phase 6** | 演唱会、主题公园、宗教节日（按优先级评估） |

---

## 五、文档导航

| 文档 | 用途 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、ICP |
| [nori-keywords.md](./nori-keywords.md) | 关键词映射、程序化 URL 模式 |
| [nori-features.md](./nori-features.md) | 功能页、Photo to Calendar、Automatic Scheduling |
| [nori-project-tasks.md](./nori-project-tasks.md) | 项目任务、赛程页待办 |
