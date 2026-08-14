# Today AI — Healthcare（AI Personal Agent for Healthcare）

> **状态**: 原型已上线 · **更新**: 2026-08-12
> **原型页面**: [https://today-ai.lovable.app/healthcare](https://today-ai.lovable.app/healthcare) · 场景子页：[AI Meal Planner](https://today-ai.lovable.app/healthcare/meal-planner) / [AI Sleep Tracker](https://today-ai.lovable.app/healthcare/sleep-tracker) / [AI Fitness Coach](https://today-ai.lovable.app/healthcare/fitness-coach)

---

## 核心定位

这个页面的核心就是一句话：**Today 是 AI Personal Agent for Healthcare** —— 一个替你把健康这件事"办掉"的个人代理，而不是又一个健康记录 App。

它把 living memory + proactive 的通用能力，翻译成健康用户每天真正在乎的几件事：**压力、饮食、睡眠、训练**四大能力，加上**用药复诊、日常习惯**等后台任务。

**核心论点**：Tracking is not the hard part. Acting is.（记录不是难点，行动才是）——用这句话与所有"只记录、不行动"的健康 App 划清界限。

**边界**：Lifestyle support, not medical diagnosis。只做生活方式支持，不做医疗诊断。

---

## 页面结构（叙事顺序）

| 板块 | 作用 |
|------|------|
| Hero | 定义品类 + 主 CTA（Join the waitlist） |
| Trust strip | 数据来源信任（Apple Health / Google Fit / Oura / Whoop / 日历 / 邮件） |
| Interactive demo | **Ask Once. Watch Your Week Rearrange Itself.**——对话即改写当日计划，配 Body Signals 卡片（Sleep / HRV / Movement / Intake） |
| Capabilities（4+4） | 4 主卡：压力情绪 / 饮食+卡路里 / 睡眠+恢复 / 训练（后三张带 Explore 链接到 spoke 页）+ 4 小卡：用药 / 复诊准备 / 睡眠跟踪 / 日常习惯 |
| Healthcare Jobs（4 卡） | 四个健康任务场景卡：坏周预警 / 合时宜的餐食推荐 / 守住的作息 / 混乱月份的坚持 |
| How it works（3 步） | 连接数据 → memory 建立基线 → 它建议、你确认、它执行（可撤销） |
| Compare | Today vs 健康 App vs ChatGPT vs 手动记录 |
| FAQ | 长尾疑问 + 合规免责 |
| Final CTA | 收口 waitlist |

> 说明（2026-08-12 实况）：hub 页已去掉独立的 Problem vs Today 对比区（该对比区保留在三个 spoke 页内）；Tasks 由原 6 卡改为 Healthcare Jobs 4 卡；饮食 / 睡眠 / 训练三张能力卡直接内链到对应 spoke 页，hub-spoke 闭环成型。

场景子页已上线三个：`/healthcare/fitness-coach`（AI Fitness Coach）、`/healthcare/meal-planner`（AI Meal Planner）、`/healthcare/sleep-tracker`（AI Sleep Tracker），hub-spoke 结构成立（详见下节）。

---

## 场景深化页（Spoke）实况（2026-08-12）

三个子页已全部上线，共用 hub 页核心论点（**Tracking is not the hard part. Acting is.**）与合规边界（lifestyle support, not medical），每页按同一叙事模板搭建。

| 子页 | 一句话定位 | 能力卡（主+小） | 场景卡（4 类） | 覆盖关键词（meta 实证） |
|------|-----------|----------------|---------------|------------------------|
| [AI Meal Planner](https://today-ai.lovable.app/healthcare/meal-planner) | 会计划、会采购、会自适应的每周餐单 | 每周餐单生成 / 购物清单+Pantry 换料 / 宏量+高蛋白目标 / 现有食材生成菜谱（+家庭 / 预算 / 素食过敏 / 批量备餐） | 家庭多日程、高蛋白训练、预算硬上限、素食+过敏 | ai meal planner、meal plan generator、ai recipe generator、macro meal planner、family meal planner、budget meal planner |
| [AI Sleep Tracker](https://today-ai.lovable.app/healthcare/sleep-tracker) | 修复睡眠节律，而不是打分 | 作息修正器（15 分钟步进）/ 睡眠债跟踪+偿还计划 / HRV 与恢复跟踪 / 及时的睡前准备（+咖啡因酒类截止 / 晨光锚点 / 时差轮班 / 30 夜临床趋势） | 熬夜晚睡、睡眠债、会议占用夜晚、新手父母 | ai sleep tracker、sleep debt calculator、ai sleep coach、hrv recovery tracking、jet lag planner、shift work sleep |
| [AI Fitness Coach](https://today-ai.lovable.app/healthcare/fitness-coach) | 记得上周、调整本周的私人教练 | 每周个性化训练计划 / 主动恢复教练 / 跨 App 执行（+AI workout generator / 睡眠感知强度 / 营养副驾 / 多端） | 忙碌创始人、新手父母回归、马拉松 taper、伤后复跑 | ai personal trainer、personalized workout plan、ai fitness coach、ai workout generator |

> 说明（2026-08-12 实况）：三页场景卡均由 6 类收敛为 4 类——meal-planner 去掉批量备餐、计划崩坏自适应；sleep-tracker 去掉时差、轮班；fitness-coach 去掉居家力量、减重+营养。被砍主题仍以「小能力卡」形式留在各页（如 sleep-tracker 的 Jet Lag and Shift Plans 小卡、meal-planner 的 Leftovers and Batch Cooking 小卡），FAQ 中亦保留时差/轮班问答——即从场景叙事降级为能力支撑，未整体删除。

**共同叙事模板**（三页同构，验证 hub 页方法论可复制，差异化点逐页复用）：

- Hero 定义品类 + 一句差异化否定式（Plan generator is not a plan / Sleep tracking is not a fix / Workout generator is not a coach）
- Problem vs Today 对比区（Generic app ↔ Today，字段一一对应；该对比区已从 hub 页移入各 spoke 页）
- Capabilities 4 主卡 + 4 小卡
- 同一场景 × 4 种人（One meal planner, four kitchens / One sleep tracker, four nights / One fitness coach, four people）
- 3 步 How it works → Compare 表 → FAQ（含合规免责）→ Join the waitlist 收口

---

## 策略要点

- **转化**：全页收口到唯一动作 Join the waitlist，Beta 免费降低摩擦
- **定位差异化**：不是另一个健康 App，而是"从信号到决定的 agent"；可只开一项，其余静默
- **目标用户**：按 Healthcare Jobs 场景卡细分的健康用户（压力大、减重、睡眠差、习惯难坚持、用药复诊拖延），spoke 页再按各自的 4 类场景承接细分人群
- **关键词**：以任务型词为主（ai meal planner / ai sleep coach / ai stress management 等），主动避开诊断类词（ai doctor / ai symptom checker）
- **合规**：免责贯穿全页，明确不是医疗诊断

---

*关联：[主文档](./today-ai.md) | [use-cases](./today-ai-use-cases.md) | [mobile-app-market](./today-ai-mobile-app-market.md)（外部竞品/关键词池，不在此文档维护）*

*Last updated: 2026-08-12*
