# SenseNova — 增长策略

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./sensenova.md) | [keywords](./sensenova-keywords.md) | [features](./sensenova-features.md) | [competitors](./sensenova-competitors.md) | [site-structure](./sensenova-site-structure.md) | [use-cases](./sensenova-use-cases.md) | [README](./README.md)

**Last updated**: 2026-07-27  
**战略背景**：国内站 `sensenova.cn` 运营中；**海外独立域名待发布** —— 增长计划分「国内巩固」与「海外冷启动」双轨。

---

## 1. 增长渠道规划

| 渠道方向 | 目标 Persona | 内容类型 | 优先级 | 预期效果 |
|----------|-------------|---------|--------|---------|
| **开源社区（GitHub / HF / Reddit / 论文）** | P4 开发者 | 模型卡、demo、技术博文、vs BAGEL/Janus | P0 | Star/Fork、二次传播、API 注册 |
| **Token Plan 产品获客** | P1 / P4 | 免费额度、接入教程（Hermes/OpenClaw）、限额说明 | P0 | Console 注册与周调用 |
| **场景 SEO/GEO（信息图 + PPT Agent）** | P1 / P2 | 案例页、How-to、榜单反击内容 | P0 | 商业词进入考虑集 |
| **U1 Pro 发布战役（→2026-08）** | P2 / P3 | 作品墙、邀测→正式、定价页、媒体稿 | P0 | 旗舰心智 + 付费意向 |
| **应用层交叉（小浣熊 / Seko）** | P1 / P2 | 应用内入口、成功故事回链模型站 | P1 | 消费级认知 → 平台升级 |
| **海外独立域名冷启动** | P2 / P4（全球） | EN 全站、hreflang、技术 SEO、Product Hunt/HN | P0（域名就绪后） | 摆脱 `/en` 权重稀释 |
| **对比与评测内容** | P4 / P1 | SenseNova vs GPT / Midjourney / BAGEL | P1 | 截获竞品关键词 |

---

## 2. 内容主题与栏目

| 栏目/主题 | 对标关键词（P0/P1） | 内容形式 | 发布节奏 | 承接页 |
|-----------|-------------------|---------|---------|--------|
| NEO-unify 通俗解释 | native multimodal, NEO-unify | 技术博文 + 图解 | 上线月 1 篇支柱 | 待建 `/blog` 或 Docs |
| U1 开源上手 | SenseNova U1, GitHub | Quickstart、Colab/HF | 随版本 | GitHub + `/models/u1` |
| Excel→报告→PPT 案例 | AI PPT agent, Excel report AI | 案例长页（中英） | 每月 ≥1 | `/cases/...`（待建）从 `/models` 拆 |
| 信息图文字准确性 | AI infographic generator | 对比测评（盲测截图） | U1 Pro 正式前 2 篇 | `/u1-pro` |
| vs BAGEL / Janus | BAGEL alternative, unified multimodal | 架构诚实对比 | 每季度更新 | 待建 `/compare/...` |
| Token Plan 经济学 | token efficient agent, SenseNova pricing | 计算器/成本故事 | Lite/Pro 上线当周 | `/token-plan` |
| 海外 Launch Kit | SenseNova English brand terms | 独立域首页 + PH 文案 | 域名 DNS 就绪后 2 周战役 | 新域 `/` |

---

## 3. 战役节奏

### 短期（0–3 个月）

1. Sitemap 补 `/u1-pro`；上线 U1 独立产品页；案例从 `/models` 拆出可索引 URL。  
2. 维持 Token Plan Free 拉新；补齐中英「如何用 OpenClaw/Hermes 接入」教程。  
3. 产出 2 篇支柱内容：*What is NEO-unify*、*U1 Pro for delivery-grade infographics*。  
4. **海外域名**：确认品牌域名、技术栈镜像、合规与支付；定 hreflang 方案（见 site-structure）。  
5. 建立竞品对比大纲（BAGEL / Midjourney / GPT），先发草稿站内。

### 中期（3–6 个月）

1. **U1 Pro 正式 API + 定价**上线战役（对齐 2026-08 窗口）：定价页、限额、案例、媒体 Kit。  
2. Lite/Pro 付费转化漏斗：Free → 用量触顶 → 升档提示（站内+邮件 ⚠️ 待产品确认）。  
3. 海外独立域全量 EN SEO：核心 P0 词落地、Technical SEO、外链（论文、HF、开源目录）。  
4. 行业页试点：金融研报、电商视觉各 1 条解决方案。  
5. 小浣熊/Seko → 模型站 UTM 与反向链轮。

### 长期（6–12 个月）

1. Skills 市场与开发者生态活动（hackathon / 模板赛）。  
2. 持续模式 C 更新关键词量级（Semrush）与竞品份额。  
3. 多区域合规与企业私有化叙事（若有产品）。  
4. GEO：进入「best multimodal open source 2026」类答案引用。

---

## 4. 竞品差异化方向

来自 [competitors](./sensenova-competitors.md)：

1. **不跟 Midjourney 抢艺术社区** —— 抢「文字正确的信息图/海报/科普图」交付场景。  
2. **不跟 GPT 拼通用助手心智** —— 拼「原生统一 + 办公 Skills + Token 效率」的可验证案例。  
3. **正面对齐 BAGEL/Janus** —— 用开源评测表 + 产品化（Token Plan、U1 Pro、应用）证明「能用的统一多模态」。

---

## 5. 度量指标

| KPI | 建议跟踪 | 工具建议 |
|-----|---------|---------|
| 自然搜索品牌/U1 词排名 | 周 | GSC + Semrush |
| Token Plan / Console 注册与周调用 | 周 | 产品后台（客户侧） |
| GitHub Star / 重要依赖引用 | 周 | GitHub traffic |
| `/models` `/u1-pro` `/token-plan` 转化 | 周 | 站内分析（注意百度统计局限；海外域用 GA4） |
| 案例页与对比页索引量 | 月 | GSC |
| Free→付费转化率 | Lite/Pro 上线后 | 计费系统 |
| 海外域：展示/点击/外链 | 上线后周 | GSC（新属性） |

---

*执行依赖*：关键词 P0 表 → [keywords](./sensenova-keywords.md)；Persona → [use-cases](./sensenova-use-cases.md)
