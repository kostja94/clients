# SenseNova — 使用场景

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./sensenova.md) | [features](./sensenova-features.md) | [keywords](./sensenova-keywords.md) | [competitors](./sensenova-competitors.md) | [site-structure](./sensenova-site-structure.md) | [growth-strategy](./sensenova-growth-strategy.md) | [README](./README.md)

**Last updated**: 2026-07-27

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **P1 知识工作者 / 分析师** | 咨询、投研、战略、运营分析；经常要「表→结论→PPT」 | 多源 Excel/PDF 清洗耗时；纯聊天模型给建议不给成稿；长任务 Token 烧不起 | 一次跑出可汇报的报告与幻灯片 | 中（会 API/Agent 更好） |
| **P2 设计师 / 内容运营** | 新媒体、科普、内容团队；要高信息密度图 | 通用生图文字乱、版式「AI 味」；反复抽卡赶不上发稿 | 可直接发的信息图/海报，还能改字改模块 | 中低–中 |
| **P3 品牌 / 电商视觉** | 品牌设计、电商设计负责人 | 主视觉与活动海报要专业美感+可控文案；印刷/详情页要高清 | 交付级出图、8K/大图、风格稳定可迭代 | 中 |
| **P4 开发者 / AI 原生团队** | 搭建内部 Agent、接入 Hermes/OpenClaw 等 | 拼接多模型管线脆；缺开源可改的统一多模态底座 | API + Skills + 自部署选项，成本可控 | 高 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| P1 | 月底拿到 10 份绩效 Excel | …自动出带图表的分析报告，别让我再手贴透视表 | Flash-Lite + 数据分析/报告 Skills | AI Excel report agent |
| P1 | 领导下周要路演 | …从材料一键生成结构清楚的 PPT，还能对话改页 | PPT 生成 + PPT 对话精修 | AI PPT generator |
| P1 | 要写行业深度研报 | …多源检索+成章+参数表，像买方研报而不是科普 | 多源检索 + 报告撰写 | AI industry research agent |
| P2 | 要发一篇科普长图 | …一图说清机制，中文标注别错字 | U1 Fast / U1 Pro 信息图 | AI infographic generator |
| P2 | 活动海报今晚截稿 | …版式像杂志，文字层级清楚，少抽卡 | U1 Pro | AI poster generator |
| P3 | 详情页 / 主视觉要印刷级 | …高清、可局部改文案与风格统一 | U1 Pro 8K + 可控编辑 | 8K AI image, delivery-grade AI image |
| P3 | 要做系列分镜/设定 | …世界观一致的多镜交付，而不是互不相关的单图 | U1 Pro 长程闭环（媒体案例） | AI storyboard generator |
| P4 | 给 Agent 挂多模态能力 | …一个模型又能看又能画，少维护三条管线 | U1 开源 + API + Skills | native multimodal model, SenseNova API |
| P4 | 长链路任务怕爆预算 | …Token 更省还能跑完办公闭环 | Flash-Lite + Token Plan | token efficient multimodal agent |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| Excel→绩效报告 | P1 | Flash-Lite + 表格理解 + 报告 | AI Excel to report | `/models` |
| 路演 PPT | P1 | PPT 生成/精修 | AI PPT agent | `/models` |
| 产业研报 | P1 | 多源检索 + 报告 | AI research report agent | `/models` |
| 科普信息图 | P2 | U1 Fast / U1 Pro | AI infographic | `/models` · `/u1-pro` |
| 品牌海报 | P2/P3 | U1 Pro | AI poster professional | `/u1-pro` |
| 8K 大图交付 | P3 | U1 Pro | 8K AI image | `/u1-pro` |
| 开源评测/自部署 | P4 | SenseNova U1 | SenseNova U1 GitHub | GitHub · `/` |
| API 接入公测 | P4 | Token Plan | SenseNova API free | `/token-plan` · console |
| Agent 框架集成 | P4 | Hermes / OpenClaw 声明支持 | OpenClaw SenseNova | `/token-plan` |

---

## 4. 用户旅程

| 阶段 | 触达 | 关键动作 | 成功标准 |
|------|------|---------|---------|
| 认知 | WAIC/开源论文/GitHub/小浣熊口碑；海外域内容（规划） | 理解「原生统一」差异 | 记住 U1 / NEO-unify |
| 考虑 | `/models` 案例、`/u1-pro` 作品、对比文 | 对比 BAGEL/GPT/Midjourney | 认可「可交付」 |
| 转化 | Token Plan Free → Console API Key | 跑通第一个 Skill 任务 | 出第一份 pptx/信息图 |
| 扩展 | 小浣熊 / Seko / Skills 市场 | 从 API 到日常应用 | 周活任务数上升 |
| 付费 | Lite/Pro、U1 Pro API（待上线） | 升档跑长任务/旗舰创图 | 付费转化 |
| 留存 | 文档、案例更新、开源社区 | Star/PR、企业 Token 用量 | 用量与社区贡献 |

---

## 5. 未覆盖场景

| 机会场景 | 关键词信号 | 现状 | 建议 |
|----------|-----------|------|------|
| 视频成片全流程 | AI video agent（Seko 有入口但营销站浅） | 首页点到为止 | 独立 Seko/视频案例页 |
| 私有化/政企部署说明 | 商汤私有化、专有云 | 官网公开页弱 | 解决方案页（合规允许范围） |
| 教育课件本地化海外 | lesson plan AI | models 有教育行，缺 EN 案例 URL | 海外域教育垂直页 |
| 实时协作编辑 | multiplayer PPT AI | 未强调 | 产品路线图沟通，勿过度承诺 |
| 与设计工具插件 | Canva/Figma plugin | 未见 | 生态合作评估 |

---

*Persona 标签供 [growth-strategy](./sensenova-growth-strategy.md) 复用*
