# ZenFit

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)

**Last updated**: 2026-03-20

---

## 文档体系（各文档职责与引用关系）

| 文档 | 职责 | 引用 |
|------|------|------|
| **zenfit.md**（本文） | 产品概览、定位、ICP、摘要级关键词/竞品/网站结构 | 详述见各专项；**商业**见 zenfit-pricing；**合规**见 zenfit-trust-compliance |
| [zenfit-features.md](./zenfit-features.md) | 功能页详情、URL、链至 Use Cases | 关键词见 zenfit-keywords；场景见 zenfit-use-cases |
| [zenfit-use-cases.md](./zenfit-use-cases.md) | Persona、情境、/for/* 规划 | 功能见 zenfit-features；**高利害场景**对齐 zenfit-trust-compliance |
| [zenfit-keywords.md](./zenfit-keywords.md) | 关键词、目标页、**承接载体**、待办 | URL 见 zenfit-features |
| [zenfit-competitors.md](./zenfit-competitors.md) | 竞品、差异化、Gaps | zenfit-features |
| [zenfit-pricing.md](./zenfit-pricing.md) | 订阅/渠道/套餐逻辑（对外口径） | zenfit-trust-compliance |
| [zenfit-trust-compliance.md](./zenfit-trust-compliance.md) | 高利害表述底线、免责声明模块 | zenfit-use-cases、zenfit-pricing |
| [zenfit-proof.md](./zenfit-proof.md) | 可公开数据、研究引用规则 | zenfit-competitors、主文档数字摘要 |

**原则**：每条重要信息**一处详述**、他处摘要+链接；zenfit.md 为入口。

*产品入口*：Web [zenfit.health](https://www.zenfit.health/) | 移动端 [App Store](https://apps.apple.com/app/id6744635674)（Google Play 即将上线）

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C / 健康健身 / 中式养生 / Mind-Body Fitness |
| 网站 | https://www.zenfit.health/ |
| 公司 | Everblessed Technology Inc. |
| 当前阶段 | 增长期（2025 年 2 月上线） |
| 核心产品 | **ZenFit**：定制化太极、气功、八段锦课程（非工具型 App，课程为核心售卖点） |
| Slogan | Rediscover Health Through Chinese Wisdom |
| 使命 | East Meets West in Wellness — 将 5000 年中医养生智慧与现代健身科学结合，帮助用户实现身心平衡 |
| 目标市场 | **海外中老年用户**（40+、50+、60+）；50+ 国家、10K+ 活跃用户 |
| 产品形态 | **定制化课程** 通过 App 交付；App 为课程载体，非工具型产品 |
| 更新日期 | 2026-03-20（文档包联动更新） |

### 能力与边界（Scope）

| 维度 | 说明 |
|------|------|
| **提供** | 定制化中式养生**课程**（太极、气功、八段锦、TCM 营养、正念等）的数字化学习与练习；AI 辅助推荐组合与强度 |
| **不提供** | 医疗诊断、治疗建议、急症处理；**非医疗器械**。疼痛、术后、严重平衡障碍等情境下，用户应咨询合格医疗人员后再练习 |
| **合规详述** | 见 [zenfit-trust-compliance.md](./zenfit-trust-compliance.md) |

### 商业摘要

用户购买的是**课程的订阅访问**（具体档位与试用以应用商店为准），App 为交付载体。详见 [zenfit-pricing.md](./zenfit-pricing.md)。

### 可公开数据摘要

评分、用户规模、课程量级等**以可复查来源为准**，统一维护在 [zenfit-proof.md](./zenfit-proof.md)；主文档叙述与营销引用请与之对齐。

---

## 2. 产品定位

### 产品摘要

**ZenFit** 面向**海外中老年用户**，核心售卖**定制化课程**（太极、气功、八段锦、TCM 营养等），而非通用健身工具。根据体质、目标、场景（如背痛、平衡、减压）定制课程内容与强度，AI 辅助个性化推荐。App 为课程交付载体；**量化背书**见 [zenfit-proof.md](./zenfit-proof.md)。

### 产品定位

**ZenFit** 面向 **海外 40+ 中老年用户**，定位为「**定制化中式养生课程**」——核心卖点**不是工具，而是因人制宜的课程**。与通用健身 App 不同，ZenFit 强调：
- **Customized Courses**：根据体质、目标、场景（背痛、平衡、减压、康复等）定制课程
- **AI-Personalized**：AI 推荐适合的课程组合与强度
- **Low-impact**：关节友好，无需跑跳
- **Mind-body**：身心合一，兼顾呼吸与冥想
- **TCM-rooted**：基于中医阴阳、气血、五行理论
- **Holistic**：运动课程 + 营养课程 + 正念课程，全链路养生

| Persona | 年龄 | 需求 | 痛点 |
|---------|------|------|------|
| **中老年健身入门者** | 50–70 | 改善平衡、柔韧、关节 | 高强度运动吃不消，健身房不适 |
| **慢性疼痛/康复者** | 45+ | 温和运动、缓解背痛/关节痛 | 传统健身加重不适 |
| **压力大/失眠者** | 40+ | 减压、助眠、正念 | 久坐、焦虑、睡眠差 |
| **中式文化爱好者** | 全龄 | 体验太极、气功、中医养生 | 线下课程少、难坚持 |
| **退休/银发族** | 60+ | 保持活力、社交、健康管理 | 时间多但不知如何科学养生 |

*详细 Persona 与场景*：见 [zenfit-use-cases.md](./zenfit-use-cases.md)

---

## 3. 目标受众 / ICP

- **银发健身者**（60–75）：保持活力、防跌倒、关节养护
- **慢性疼痛者**（45–65）：背痛、膝痛、关节炎的温和运动
- **压力/失眠者**（40–60）：减压、助眠、正念
- **退休探索者**（55–70）：新爱好、文化体验、中医养生
- **健身入门者**（50+）：零基础、易上手、不受伤

*Persona 详情与 Use Case 映射*：见 [zenfit-use-cases.md](./zenfit-use-cases.md)

---

## 4. 核心产品线

**核心售卖点**：**定制化课程**（非工具）。课程按体质、目标、场景定制，而非通用内容库。

| 课程类型 | 说明 |
|----------|------|
| **Tai Chi 课程** | 5–15 分钟，初级到高级，含经典 24 式；可定制强度与时长 |
| **Qigong 课程** | 能量与放松，8–15 分钟；可定制场景（减压、助眠、晨间等） |
| **Eight Brocades 课程** | 八段锦等传统养生功法 |
| **AI 定制课程计划** | 根据体质、目标、场景（背痛、平衡、康复等）推荐课程组合 |
| **TCM 营养课程** | 基于中医食物性味，日常饮食建议 |
| **正念与呼吸课程** | 冥想、呼吸练习，减压助眠 |
| **健康追踪** | 辅助课程效果反馈，非核心售卖 |

### 核心价值主张

- **Customized Courses, Not Tools**：核心卖点是**因人制宜的课程**，而非通用健身工具
- **AI-Personalized**：根据体质、目标、场景定制课程组合
- **Ancient Wisdom, Modern Life**：5000 年中医智慧，适配现代快节奏
- **Yin & Yang Balance**：阴阳平衡，身心和谐
- **Preventive Care**：预防为主，治未病

### 市场洞察

- **银发经济**：全球 50+ 人口增长，健康消费升级
- **温和健身趋势**：低强度、身心合一类运动（瑜伽、太极、普拉提）持续增长
- **中医出海**：TCM、太极、气功在欧美认知提升，但优质数字化产品稀缺
- **工具 vs 课程**：多数健身 App 卖「工具/内容库」；ZenFit 卖**定制化课程**，按体质、目标、场景匹配，差异化明显
- **在线课程 vs App 订阅**：Udemy、Class Central 等聚合 80+ 太极课程，多为**一次性长课程**（1–10 小时），如 [Tai Chi Chuan For Beginners](https://www.classcentral.com/course/udemy-tai-chi-chuan-for-beginners-33036)（1h34min、24 式杨氏、免费）。ZenFit 差异化：**5–15 分钟短课**、**每日练习**、**AI 定制**、**订阅制**，非一次性学习

**金句**（来自官网）：
> "Why is it that yoga has become so widely embraced around the world, while other time-honored practices from the East—like Tai Chi, Qigong, and Baduanjin—are still unfamiliar to so many?"

> "ZenFit is not just about exercise. It's about giving people a way to breathe a little deeper, move a little softer, and carry a sense of calm into their everyday lives."

*功能页详情见 [zenfit-features.md](./zenfit-features.md)*

---

## 5. 关键词摘要

| 类型 | 示例 |
|------|------|
| **Primary** | tai chi app, qigong app, tai chi for seniors, gentle fitness app |
| **Secondary** | tai chi for beginners, qigong for energy, eight brocades app, TCM fitness, personalized tai chi, customized tai chi courses |
| **Long-tail** | tai chi app for seniors over 50, low impact exercise app for elderly, tai chi for back pain |
| **品牌** | ZenFit, ZenFit health |

*完整映射*：见 [zenfit-keywords.md](./zenfit-keywords.md)

---

## 6. 竞品摘要

- **直接竞品**：多款「太极/气功 + 中老年」垂直 App（代表名与数据见竞品文档）。
- **间接竞品**：瑜伽/普拉提/冥想 App；**在线长课程**（Udemy、Class Central 等聚合）。
- **差异化（一句）**：ZenFit 卖**可定制的短课订阅 + AI 组合 + TCM/八段锦一体化**；多数竞品为固定课表或一次性长课。

*表格、课程级对比、Class Central 生态*：见 [zenfit-competitors.md](./zenfit-competitors.md)

---

## 7. 网站结构

| 路径 | 说明 |
|------|------|
| / | 首页：Rediscover Health Through Chinese Wisdom |
| /features/* | 功能页：tai-chi、qigong、eight-brocades、mind-body-balance |
| /learn/* | 学习：tai-chi-101、qigong-basics、tai-chi-vs-yoga、chinese-wellness-philosophy |
| /about | 品牌故事：Bridging Ancient Wisdom with Modern Life |
| /blog | 博客 |
| /faq | 常见问题 |
| / | CTA：Download on App Store（Google Play coming soon） |

**当前状态**：官网为品牌落地页，主要转化入口为 App Store 下载；**核心卖点**为定制化课程，官网/App 文案应强化「personalized courses」「customized for you」而非「fitness app」。

**售卖逻辑**：用户购买的是**定制化课程**（按体质、目标、场景匹配），App 为课程交付载体。

**产品路线**：
- Google Play 上线
- 更多语言本地化（当前以英文为主）
- 社区/社交功能（待确认）

---

## 8. 内容营销

- **已有**：Learn 栏目（Tai Chi 101、Qi Gong Basics、Tai Chi vs Yoga、Chinese Wellness Philosophy）
- **定位**：中式养生教育、温和健身、中老年健康
- **待建**：Persona 页（/for/seniors、/for/beginners）、场景页（balance、back pain、stress）、竞品对比（tai chi app alternatives）
- **可选**：博客「Tai Chi Course vs App：Udemy/Class Central 一次性课程 vs ZenFit 定制化短课」— 拦截 learn tai chi online 等搜索

### 页面落地顺序（基于海外中老年定位）

| 阶段 | 页面 | 理由 |
|------|------|------|
| **Phase 1** | /for/seniors、/for/beginners | 核心 Persona；上线前关键词可暂由首页 + `/features/*` + Learn 承接（见 [zenfit-keywords.md §1.1](./zenfit-keywords.md)） |
| **Phase 2** | /for/back-pain、/for/stress、/for/balance | 高利害场景页须套 [zenfit-trust-compliance.md](./zenfit-trust-compliance.md) 模块 |
| **Phase 3** | /alternatives、/vs/* | 竞品拦截 |
| **Phase 4** | 博客：tai chi benefits for seniors、qigong for beginners | 教育、长尾 |
| **Phase 5** | GEO：best tai chi app 等 | AI 答案可见性 |

---

## 9. 优化建议

- §8 落地顺序 + [zenfit-keywords.md](./zenfit-keywords.md) 待办。  
- 新建 /for/* 前：核对 **承接载体** 列，避免「词已铺、页全无」的薄站风险。  
- 涉及疼痛/康复/平衡的文案：先过 [zenfit-trust-compliance.md](./zenfit-trust-compliance.md)。

---

## 10. 文档导航

| 文档 | 用途 |
|------|------|
| [zenfit-features.md](./zenfit-features.md) | 功能页、URL、内链 |
| [zenfit-use-cases.md](./zenfit-use-cases.md) | Use Cases、Persona |
| [zenfit-keywords.md](./zenfit-keywords.md) | 关键词、承接、待办 |
| [zenfit-competitors.md](./zenfit-competitors.md) | 竞品 |
| [zenfit-pricing.md](./zenfit-pricing.md) | 商业与定价 |
| [zenfit-trust-compliance.md](./zenfit-trust-compliance.md) | 信任与合规 |
| [zenfit-proof.md](./zenfit-proof.md) | 证据与数据 |

---

*文档生成日期：2025-03-10 | 文档包更新：2026-03-20 | 来源：官网 [zenfit.health](https://www.zenfit.health/)、App Store*
