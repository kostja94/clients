# SoberVoice 杂项汇编（Others）

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)  
> **本文档职责**：集中维护**非六主文档循环**材料——路由明细、技术 SEO 占位、合规、数据引用、定价备忘、GEO/Schema、项目任务与 Backlog。  
> 关联：[sobervoice.md](./sobervoice.md) | [sobervoice-keywords.md](./sobervoice-keywords.md) | [sobervoice-site-structure.md](./sobervoice-site-structure.md) | [sobervoice-growth-strategy.md](./sobervoice-growth-strategy.md)  
> 流程依据：[通用-多文件文档联动精炼与增量循环.md](../../client-template.md) **v8**（六主文档 + `*-others.md`）

**Last updated**: 2026-03-20（**重构**：由原 `sobervoice-sitemap`、`pricing`、`trust-compliance`、`proof`、`geo-schema-brief`、`project-tasks` 合并迁入，**内容不压缩**）

---

## Routes and sitemap（路由总表与索引占位）

*原 `sobervoice-sitemap.md` 全文迁入。*

### 路由总表（占位域名下路径）

| 路径 | 类型 | 对应文档中的角色 | 状态 |
|------|------|------------------|------|
| / | 首页 | 主文档 IA | 待建 |
| /features/voice-coach | 功能 | features | 待建 |
| /features/urge-support | 功能 | features | 待建 |
| /features/check-in | 功能 | features | 待建 |
| /features/insights | 功能 | features | 待建 |
| /for/cravings | Use Case | use-cases | 待建 |
| /for/drink-less | Use Case | use-cases | 待建 |
| /for/social-drinking | Use Case | use-cases | 待建 |
| /for/stress-drinking | Use Case | use-cases | 待建 |
| /for/night-drinking | Use Case | use-cases | 待建 |
| /for/workplace | Use Case | use-cases | 待建 |
| /for/after-relapse | Use Case | use-cases | 待建 |
| /for/voice-coach | Use Case | use-cases | 待建 |
| /pricing | 商业 | 见本文 **Pricing** 节 | 待建 |
| /learn/* | 教育 | features Library | 待建 |
| /blog | 内容 | keywords / growth-strategy | 待建 |
| /resources | 资源聚合 | keywords / growth-strategy | 待建 |
| /alternatives | 对比（可选） | competitors | 待建 |
| /medical-disclaimer | 合规 | trust | 待建 |
| /privacy、/terms | 法律 | trust | 待建 |
| /about | 品牌信任 | site-structure | `待验证` |
| /contact | 联系 | site-structure | `待验证` |
| /faq 或 /help | 支持 | site-structure | 待建 |
| /download（可选） | 重定向 | 统一跳转 App Store / Play | `待验证` |

### 重定向与 URL 规范（占位）

| 规则 | 说明 |
|------|------|
| **尾随斜杠** | 全站统一一种风格，避免重复收录 | `待验证` |
| **/download** | 短链至商店，便于广告与外链 | 与本文 **Pricing** §0 CTA 一致 |
| **http→https** | 301 强制 | 工程实施 |

### 索引与 canonical（占位）

| 类型 | 处理 |
|------|------|
| **staging / 预览** | `noindex` 或 Basic Auth | 勿与生产 sitemap 混用 |
| **/blog 分页** | 分页页 canonical 指向自身或首屏 | `待验证` |
| **多语言** | hreflang 与主域策略见 [SEO-多语言与-locale-指南.md](../../SEO/SEO-多语言与-locale-指南.md)；回填 **Tasks** 节 Backlog R4 |

### Phase 1 建议仅建站内的最小集合

与 [sobervoice-use-cases.md](./sobervoice-use-cases.md) P1 一致：`/`、`/features/voice-coach`、`/features/urge-support`、`/for/cravings`、`/for/drink-less`、`/medical-disclaimer`。

### 与 App 内屏的映射（`待验证`）

| 官网路径 | 可能的 App 内对应 | 备注 |
|----------|-------------------|------|
| /features/voice-coach | Voice Coach 主 tab / 首次引导 | 来源:推演 |
| /features/urge-support | Urge 紧急入口 / Widget | 来源:推演 |

*变更时同步 [sobervoice-keywords.md](./sobervoice-keywords.md) 承接列。*

---

## Trust and compliance（信任与合规）

*原 `sobervoice-trust-compliance.md` 全文迁入。*

饮酒行为改变涉及**身体与心理风险**（包括**戒断急症**）。以下为内容与产品**底线摘要**；**正式对外以法务与医疗顾问审定为准**。

### 1. 产品定位（合规视角）

| 陈述 | 说明 |
|------|------|
| **是什么** | 面向成年人的**自助与健康教育类**数字工具，以**语音交互**提供行为支持与技巧提示 |
| **不是什么** | **不是**医疗服务、**不是**心理治疗或成瘾医学诊疗、**不是**危机干预热线替代品；**不**用于诊断酒精使用障碍（AUD）或开具治疗 |

### 2. 戒断与安全（强制提示）

- **严重依赖**突然停酒可能导致**震颤、抽搐、谵妄等危及生命**的情况。  
- App 与官网须在显著位置提示：**有戒断症状或每日大量饮酒者，停酒前应咨询医生**；出现急症应拨打当地急救。  
- AI 对话中若识别到**自伤、伤人、急性戒断描述**风险（按产品能力设计），应引导至**紧急服务**与**专业资源**，而非继续「教练」对话。  
- **驾驶中**：不得鼓励或暗示在驾驶时使用需注视屏幕或手持设备的交互；语音场景营销须写清 **「停车后 / 非驾驶」**（与 [sobervoice-features.md](./sobervoice-features.md) 一致）。

### 3. 对外表述禁区（摘要）

- 不承诺**治愈率、复饮率降低百分比**（除非有严格 RCT 且法务批准）。  
- 不将 App 与**药物、住院脱瘾**效果做不当对比。  
- 不使用「医生」「治疗」等用语描述 AI，除非取得相应资质与许可。  
- **减量**与**戒酒**叙事须在目标市场法律下区分；部分司法辖区对酒精广告与健康宣称有额外限制。  

#### 3.5 订阅、试用与付费墙（与 Pricing 对齐）

- **禁止**：将「更多语音分钟 / Pro 模型」等与**治愈率、复饮率、医学疗效**挂钩。  
- **试用结束**：避免羞辱式文案；宜提示可继续免费层能力，并**重复可见**戒断安全与危机资源入口（§7）。  
- **付费墙时机**：若用户在对话中表露急性戒断或自伤风险，应**暂停**推销，优先安全引导（与 §2 一致）。  
- 详表与档位见本文 **Pricing** 节；合规底线以本节为准。

### 4. 建议落地页 / App 模块（示例占位 — 须法务定稿）

**通用免责声明**：

> SoberVoice 提供一般性教育信息与自助工具，不构成医疗建议或专业治疗。饮酒与健康问题请咨询合格医疗专业人员。出现戒断症状或紧急情况，请立即寻求医疗帮助或拨打当地紧急电话。

**戒断风险提示（可加粗或独立卡片）**：

> 若您每日大量饮酒或曾有戒断反应，请勿自行突然停酒；请先咨询医生。

### 5. 与场景文档的联动

| 场景类型 | Use Cases | 合规注意 |
|----------|-----------|----------|
| 渴求应对 | /for/cravings | 技巧为主，不保证「压制成功」 |
| 社交拒酒 | /for/social-drinking | 避免煽动危险行为 |
| 复饮重启 | /for/after-relapse | 强调安全与专业支持可选路径 |
| 减量 | /for/drink-less | 与医疗建议不冲突；高危用户导向评估 |
| 职场应酬 | /for/workplace | 拒酒话术为沟通技巧教育；不鼓励职场违法歧视或危险对抗 `需法务` |

### 6. 隐私与数据

- 饮酒与情绪数据属**敏感个人信息**；收集目的、保留期与跨境传输以**隐私政策**为准。  
- 文档包内不粘贴用户可识别信息。  

### 7. 危机资源（按市场填充）

| 市场 | 资源类型 | 占位 |
|------|----------|------|
| US | 988 Suicide & Crisis Lifeline 等 | 填正式号码与链接 |
| UK | NHS、Samaritans | 占位 |
| 其他 | 本地化 | 占位 |

*产品内应一键外呼或复制，而非仅静态文。*

*Demo · 非法律意见*

---

## Proof and citations（可公开数据与引用）

*原 `sobervoice-proof.md` 全文迁入。*

**Demo**：本产品为虚构，**无真实评分与用户规模**。正式项目在此维护：

- App Store / Google Play 评分与评论数（附截图日期）  
- 公开发布的用户数、留存（若有且经法务同意）  
- **研究引用**：MI、CBT 在饮酒干预中的一般性结论，须引用**同行评审或权威机构**（如 NIAAA、Cochrane 等），且**不**暗示本产品等效于临床试验干预  
- **竞品对比**：凡在 [sobervoice-competitors.md](./sobervoice-competitors.md) 或 `/alternatives` 中出现的**功能对比、用户数、价格**，均须在此表或脚注中给出**来源 URL + 抓取日期**；无来源则标 **`待验证`** 且不得对外发布为事实陈述  
- **商店定价与订阅条款**：对外引用「我方月费/年费」时，保存 **App Store Connect / Play Console 截图或导出** 及日期，与本文 **Pricing** 节同步  

### 引用规则（摘要）

1. 任何「研究表明…」须有**可追溯来源**与**访问日期**。  
2. 不夸大单一研究适用于 App 内语音场景。  
3. 教育内容优先链接至**公立卫生机构**页面。  
4. 竞品「语音功能」类断言须引用对方商店截图或官方说明，避免误标 **`待验证`**。  
5. 价格促销、区域价差以商店后台为准；博客或邮件中的数字须能回溯到本节归档。  

### 占位表

| 数据项 | 值 | 来源 | 日期 |
|--------|-----|------|------|
| App 评分 | — | — | — |
| 下载量 | — | — | — |

---

## Pricing（商业与定价）

*原 `sobervoice-pricing.md` 全文迁入；文内「trust」交叉引用改为指向本文 **Trust and compliance** 节。*

### 0. 核心转化路径（占位）

| 触点 | 主 CTA | 备注 |
|------|--------|------|
| 官网首页 / | Download / Start free | 与 [sobervoice-keywords.md](./sobervoice-keywords.md) P1 簇一致 |
| /pricing | 查看计划、跳转商店订阅 | 疗效与戒断承诺边界见上文 **Trust and compliance** §3.5 |

*来源:推演*

### 1. 售卖对象

| 项目 | 说明 |
|------|------|
| **卖什么** | **订阅**：高级语音教练时长/模型、深度 Insights、教育库全访问等（具体以产品为准） |
| **不卖什么** | 医疗服务、一对一持证治疗；详见上文 **Trust and compliance** |

### 2. 渠道与转化

| 渠道 | 作用 | 备注 |
|------|------|------|
| **官网（占位）** | 品牌、教育、下载导流 | 与 [sobervoice-keywords.md](./sobervoice-keywords.md)、本文 **Routes** 节对齐 |
| **App Store / Google Play** | 订阅 IAP、评分 | 档位 `待验证` |

### 3. 套餐层级（占位）

| 层级 | 意图说明 | 验证状态 |
|------|----------|----------|
| **Free** | 有限次语音或仅文字 Check-In | `待验证` |
| **Plus / Pro** | 无限或高额语音、Insights、导出 | `待验证` |
| **（可选）家庭** | 多成员 | 若无可删 |

**闸口示例（`待验证`）**：Free 层可按「每日语音分钟数 / 深聊次数」限制；**不得**在商店截图或文案中把解锁语音表述为「治疗升级」「医学级支持」。

*价格、试用天数与功能闸口变更时：更新本节 + [sobervoice.md](./sobervoice.md) 商业摘要 + 商店文案；商店展示价截图归档见本文 **Proof and citations**。*

### 4. 与叙事的一致性检查

- 不得将订阅包装为「保证戒酒」或医疗疗效。  
- 促销、试用结束与付费墙话术与 **Trust and compliance** **§3.5** 一致。  

### 5. 上线前自检（摘要）

- [ ] 商店副标题 / 截图无疗效与戒断暗示  
- [ ] 试用转付费邮件与 App 内弹窗含安全资源入口（链 Trust §7）  
- [ ] 价格与功能列表与 [sobervoice-competitors.md](./sobervoice-competitors.md) 对比页事实链一致（`待验证` 未清前不上线对比）  

### 6. 营销站 `/pricing` 页面模块（对照 pricing-page skill）

| 模块 | 目的 | SoberVoice 备注 |
|------|------|-----------------|
| **标题区** | 价值导向，非仅「价格」 | 避免疗效承诺；可强调「透明订阅」 |
| **月/年切换** | 展示年付节省（常见 15–25%） | `待验证` 实际比例 |
| **方案对比** | 2–4 档；**Best for** 清晰 | Free / Plus / Pro 与**语音分钟**挂钩，不用「治疗级」话术 |
| **FAQ** | 计费、取消、试用、语音额度 | 措辞过 **Trust**；Schema 见本文 **GEO schema** |
| **信任元素** | 保障、透明、支持渠道 | 替代「治愈案例」；可链医疗免责声明 |
| **主 CTA** | 每卡或统一「Get started」 | 跳转商店与 **Routes** `/download` 策略一致 |
| **主导航** | 自助产品应能发现 Pricing | 与 [sobervoice-site-structure.md](./sobervoice-site-structure.md) Must Have 一致 |

**站内第二触点**：已登录用户的订阅管理放在 App **Settings → Billing**（与营销站分工）。

*Demo · 无真实价格*

---

## GEO schema and FAQ（GEO 与结构化数据）

*原 `sobervoice-geo-schema-brief.md` 全文迁入。*

技能参考：`.cursor/skills/strategies/commercial/geo/SKILL.md`、`.cursor/skills/seo/on-page/schema/SKILL.md`、`.cursor/skills/pages/content/faq/SKILL.md`  
细则：[GEO-落地操作与站内实施.md §四](../../GEO/GEO-落地操作与站内实施.md#四页面日期lastmod与前台展示)

### 1. GEO（文章 / 教育页）

| 实践 | SoberVoice 应用 |
|------|-----------------|
| **可引用段落** | 每段自洽；H2 后 **40–60 词内先答** |
| **TL;DR 或 Key Takeaways** | 长文选一种：文首 **TL;DR（50–100 词）** 或 **5–7 条要点** |
| **QAE** | H2 提问 → 2 句结论 → 列表/数据支撑 |
| **列表与表格** | 提升被 AI 摘录概率 |
| **技术** | 关键内容在 **首屏 HTML**（AI 爬虫多不执行 JS） |

### 2. Schema 优先级

| 类型 | 放置 | 备注 |
|------|------|------|
| **Organization** + **WebSite** | 首页 JSON-LD | 实体信号 |
| **WebPage** | 主要落地页 | 与标题/description 一致 |
| **BreadcrumbList** | 有层级浏览路径的页 | 与可见面包屑一致 |
| **Article** + **Person** | /blog/* | ISO 8601 日期 |
| **SoftwareApplication** | 产品/下载 | **谨慎**：避免医疗疗效；与 Trust 免责声明同屏 |
| **FAQPage** | /pricing、/faq | **YMYL/健康**：富结果限制多；不保证富结果 |

**验证**：[Rich Results Test](https://search.google.com/test/rich-results)

### 3. FAQ 布局

| 场景 | 建议 |
|------|------|
| **定价页** | 3–8 题：计费、取消、试用、语音分钟、是否治疗——答案含合规措辞 |
| **独立 /faq** | 5–10 题：账号、隐私、安全、医疗边界 |

### 4. 与合规的硬边界

- Schema 与文案均**不得**断言治愈成瘾、替代医疗。  
- 危机与戒断提示与本文 **Trust and compliance** 同步。

---

## Project tasks and backlog（项目任务与调研）

*原 `sobervoice-project-tasks.md` 迁入；历史「入口文档」列中的旧文件名仍指合并前路径，实体内容已在本 others 文件各节。*

### 文档重构说明（2026-03-20）

- 采用 [通用-多文件文档联动精炼与增量循环.md](../../client-template.md) **v8**：**六主文档**（keywords / competitors / features / use-cases / **growth-strategy** / site-structure）+ **本 others**。  
- 下列 **1–11 轮**记录保留为沿革，**不删除**。

### 文档联动加载记录（1–11 轮 · 合并前文件名）

| 轮次 | 入口文档（合并前） | 精炼要点摘要 |
|------|-------------------|--------------|
| 1–5 | sobervoice / features / use-cases / keywords / competitors | 术语、sitemap 初版、P1 场景、关键词主表、竞品待验证 |
| 6–8 | pricing / trust / sitemap | 付费墙 §3.5、定价自检、路由与 canonical |
| 9–11 | site-structure / pricing / geo-schema | Must Have 页、定价模块表、GEO/Schema |

### 调研 Backlog

| ID | 需查证什么 | 优先级 | 计划来源 | 结果摘要 | 来源/日期 |
|----|------------|--------|----------|----------|-----------|
| R1 | 美/英/澳**酒类产品推广、健康宣称**政策 | P0 | 联网 + URL | | |
| R2 | 竞品**实时语音**等能力是否属实 | P0 | 联网 + URL | | |
| R3 | 官网路径与 App tab / 深链 | P1 | 推演 + 用户文件 | 草案见本文 Routes | 推演 / 2026-03-20 |
| R4 | 多语言 URL、hreflang | P1 | 联网 | | |
| R5 | 核心词 SERP 结构 → 博客 vs 落地页 | P1 | 联网 | | |
| R6 | 是否单独 geo 文件 | P2 | 推演 | 并入 others 本节 + 仓库 GEO 指南 | 推演 / 2026-03-20 |
| R7 | `/alternatives` 竞品事实表 | P1 | 联网 + URL | | |
| R8 | 订阅展示、含税、自动续费披露 | P1 | 联网 + URL | | |
| R9 | 年龄门槛、商店分级、未成年人定向 | P1 | 推演 + 联网 | 假定成年人 ICP | 推演 / 2026-03-20 |
| R10 | SoftwareApplication / FAQPage 戒酒类富结果 eligibility | P1 | 联网 + URL | | |

### P0 / P1 / P2 任务（依赖已指向 others 各节）

| ID | 任务 | 状态 |
|----|------|------|
| T1 | 法务审定免责声明与戒断提示（Trust） | 待办 |
| T2 | 危机热线按市场填充（Trust §7） | 待办 |
| T3 | 商店类目与年龄分级（Trust + Pricing） | 待办 |
| T4 | 上线 voice-coach / cravings / urge-support 首屏 | 待办 |
| T5 | 首页与功能互链对齐 keywords + Routes 表 | 待办 |
| T6 | 博客大纲：渴求科学、减量 vs 戒酒合规 | 待办 |
| T7 | 竞品功能事实核查 | 待办 |
| T8 | 可选 /alternatives | 待办 |

### Changelog

| 日期 | 说明 |
|------|------|
| 2026-03-20 | 初始化至 11 轮加载（见合并前 project-tasks 历史） |
| 2026-03-20 | **v8 重构**：sitemap、pricing、trust、proof、geo-schema、project-tasks → **sobervoice-others.md**；新增 **sobervoice-growth-strategy.md** |

---

*Demo · Others 单文件维护非核心循环材料*
