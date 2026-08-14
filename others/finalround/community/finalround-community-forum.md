# Final Round AI — 社区 / 论坛（Discourse）

> **目的**：记录 **已上线** 的 Final Round 用户社区现状、与主站集成情况，以及后续优化待办；与 [finalround-project-tasks.md](../finalround-project-tasks.md) §2 站内 Forum 对齐。  
> **语言**：策略与审计中文；产品名、URL、Discourse 术语英文。  
> **线上入口**：https://www.finalroundai.com/community

**Last updated**: 2026-06-04（线上审计 + 公开 Community 竞品 / Blind / Reddit 调研）

**站点**：https://www.finalroundai.com/

---

## 0. 执行摘要

| 项 | 现状 |
|----|------|
| **平台** | **Discourse**（已确认：分类页、主题 URL、`/community/c/`、`/community/t/` 路径） |
| **接入形态** | **子路径** `www.finalroundai.com/community/`（**非**子域；与 2026-03 草案「优先子域」不同，见 §2） |
| **上线状态** | **已上线**；sitemap 含 `community` 子 sitemap（见 [finalround-site-structure.md](../finalround-site-structure.md) §6.8） |
| **规模** | **6 分类**、**39 主题**、**2 标签**；单帖 Views 多为个位数（早期阶段） |
| **主站内链** | `/explore` → Resources → **Community** 已收录 |
| **竞品公开社区** | Copilot 赛道仅 **VirtualInterview.ai `/forum`** 对标；详见 **§7** |
| **第三方 UGC** | **Blind**、**Reddit** 为真实讨论主战场；详见 **§8** |
| **运营 Playbook** | 可执行 Pipeline 见 [community-ops-playbook.md](./community-ops-playbook.md) |
| **下一步** | 见 **§4 优化待办**（集成深化、内容运营、SEO、SSO 等待验证项） |

---

## 1. 线上现状审计（2026-06-04）

> 数据来源：直接抓取 https://www.finalroundai.com/community 首页、`/categories`、`/tags`、`/latest?page=1` 及规则帖 `/t/read-this-before-posting-community-rules-and-content-standards/14`。

### 1.1 基础信息

| 项 | 值 |
|----|-----|
| **Canonical 首页** | https://www.finalroundai.com/community |
| **Meta title** | Final Round AI Community |
| **Meta description** | Join the Final Round AI community to share interview tips, discuss AI interview copilots, get feedback from real candidates, and land your dream job. |
| **结构化数据** | `WebSite` + `SearchAction`（`target`: `https://finalroundai.com/community/search?q={search_term_string}`）— 注意 schema 中 URL **无 `www`**，与页面实际域名需统一 canonical |
| **Discourse sitemap** | `https://www.finalroundai.com/community/sitemap.xml` 抓取时 **500** — 待工程排查；主站 sitemap index 仍含 `community` 子 sitemap |

### 1.2 分类（6）

| 分类 | Slug / ID | Topics | 描述（线上） |
|------|-----------|--------|--------------|
| **Interview Prep** | `interview-prep` / 5 | 15 | Tactical prep for coding, system design, behavioral, case, and HireVue interviews. |
| **Resume & Career** | `resume-career` / 6 | 11 | Resume reviews, LinkedIn tips, career switches, salary negotiation. |
| **General** | `general` / 4 | 5 | Topics that don't fit other categories. |
| **Success Stories** | `success-stories` / 7 | 5 | Offer announcements and lessons from the loop. |
| **Product Feedback** | `product-feedback` / 8 | 3 | Feature requests and feedback on Final Round AI products. |
| **Site Feedback** | `site-feedback` / 2 | **0** | Discussion about this site, organization, and improvements. |

**URL 模式**：

- 分类：`/community/c/{slug}/{id}` — 例 `/community/c/interview-prep/5`
- 主题：`/community/t/{slug}/{id}` — 例 `/community/t/best-way-to-structure-star-method-answers/35`

### 1.3 标签（Tags）

| 标签 | 使用次数 | 对应产品（推断） |
|------|----------|------------------|
| `resume-checker` | 8 | [Resume Checker](/resume-checker) |
| `linkedin-optimizer` | 2 | [LinkedIn Profile Optimizer](/linkedin-profile-optimizer) |

标签体系刚起步；可扩展至 `interview-copilot`、`ai-mock-interview`、`hirevue` 等，与产品页互链。

### 1.4 主题内容概览（39 篇）

**运营 / 置顶类（General）** — 管理员 `mohitnagaraj` 发布于 2026-03～04：

| 主题 | 用途 |
|------|------|
| [Read this before posting (community rules and content standards)](/community/t/read-this-before-posting-community-rules-and-content-standards/14) | 社区规则（10 条，见 §1.6） |
| [How to ask for resume or interview feedback (and actually get it)](/community/t/how-to-ask-for-resume-or-interview-feedback-and-actually-get-it/15) | 发帖指南 |
| [Welcome to the Final Round AI Community](/community/t/welcome-to-the-final-round-ai-community/13) | 欢迎帖 |
| [Welcome to Final Round AI Community! 👋](/community/t/welcome-to-final-round-ai-community/5) | 系统欢迎帖（与上条重复，可合并或 pin 其一） |
| [Weekly interview wins and challenges - Week 1](/community/t/weekly-interview-wins-and-challenges-week-1/17) | 周常互动模板 |
| [Introduction thread - where is everyone interviewing?](/community/t/introduction-thread-where-is-everyone-interviewing/…) | 自我介绍串 |

**Interview Prep（15）** — 覆盖 STAR、HireVue、McKinsey case、Amazon LP、Google PM、Meta coding、Netflix culture、system design 等；与 [interview-prep](/interview-prep)、[interview-questions](/interview-questions)、Blog 高度可互链。

**Resume & Career（11）** — ATS 格式、career switch、gap year、薪资谈判、follow-up 等；与 `/resume-checker`、`/cover-letter-generator` 相关。

**Success Stories（5）** — Google PM offer、Amazon 第三次通过、Teacher→PM、HireVue 成功案例等；转化向内容，可链 `/interview-copilot`、`/ai-mock-interview`。

**Product Feedback（3）** — Mock 反馈质量、行业 case 练习需求、咨询 case 练习需求。

### 1.5 互动数据（早期信号）

| 指标 | 观察 |
|------|------|
| **Views** | 多数主题 **1–11** 次浏览 |
| **Replies** | 运营帖 0–1 回复；讨论帖多为 **5–6** 回复（疑似种子内容） |
| **最近活动** | 2026-03-17 ～ 2026-04-24 |
| **管理员** | `mohitnagaraj`（规则与指南）；`system`（Discourse 默认欢迎） |

*上线初期以种子帖建立讨论氛围；优化阶段需引入真实 UGC 与外部引流。*

### 1.6 社区规则摘要（线上已发布）

完整正文：[Read this before posting…](/community/t/read-this-before-posting-community-rules-and-content-standards/14)

1. **Be specific** — 公司、职级、时间线要写清楚  
2. **One question per post** — 一帖一题，便于搜索  
3. **No leaked NDA questions** — 只谈策略与自身体验  
4. **No fabricated offers/salaries** — 真实故事 only  
5. **Redact personal data** — 简历/截图脱敏  
6. **Respect people's stories** — 禁止嘲讽  
7. **No promotion of competing interview tools** — 可分享公开免费资源  
8. **Product feedback → Product Feedback 分类** — 其他区提及产品应自然非硬广  
9. **Human moderation** — 可 flag，移除可申诉  
10. **Have fun** — 友好氛围  

规则与 Final Round 品牌、合规方向一致；优化时可 pin 至各分类顶部并链回主站 FAQ。

### 1.7 与主站集成（当前）

| 集成点 | 状态 | 说明 |
|--------|------|------|
| **/explore 聚合** | ✅ | Resources 区块含 **Community** 链接 |
| **Footer / 全站 Navbar** | ⚠️ 待核 | [finalround-project-tasks.md](../finalround-project-tasks.md) §5.2 Footer 关键链接仍为 Pending |
| **Blog / interview-prep 互链** | ❌ 未系统化 | 高相关 Blog 与社区主题未建立固定互链表 |
| **SSO / 统一账号** | ⚠️ 待核 | 是否已与 `accounts.finalroundai.com` 打通需工程确认 |
| **品牌视觉** | ⚠️ 待核 | Discourse 主题是否与 [finalround-brand-visual.md](../finalround-brand-visual.md) 对齐 |
| **Schema `sameAs`** | ⚠️ 待核 | 主站 Organization JSON-LD 是否含 community URL（见 [finalround-schema.md](../technical/finalround-schema.md)） |

---

## 2. 与历史选型方案的对照

2026-03-28 草案结论 vs 实际上线：

| 维度 | 草案建议 | **实际上线** |
|------|----------|--------------|
| **平台** | Discourse 优先 | ✅ Discourse |
| **接入形态** | 优先 **子域** `community.finalroundai.com` | ✅ **子路径** `/community/` |
| **部署** | 自建 Docker 或官方托管 | 未公开；子路径暗示 **反向代理 / Rewrite** 至 Discourse 实例（类似 [tech-layoffs](../tech-layoffs/README.md) 模式，负责人可能含 **Mohit**） |
| **任务状态** | project-tasks §2.1 / §2.2 为 Pending | **2.1 选型与部署：实质已完成**；**2.2 主站集成：部分完成**（explore 有链，Footer/SSO/互链待完善） |

**子路径利弊（已接受）**：

- ✅ 主域 SEO 权重集中、用户感知同一品牌  
- ⚠️ Discourse 与主站 Next 栈分离，需维护 Rewrite、`/_next` 或 Discourse 静态资源代理（参考 [finalround-production-routing.md](../technical/finalround-production-routing.md)）  
- ⚠️ Search Console 中 community 页面归属主域属性即可，无需独立子域属性  

---

## 3. 技术参考（Discourse + 子路径）

> 以下为运维/工程备忘；**线上已跑通**，细节以 Mohit / 工程仓库为准。

### 3.1 子路径反向代理要点

| 项 | 说明 |
|----|------|
| **路径前缀** | 所有 Discourse 链接以 `/community` 为 base（Discourse 后台 `force_hostname` + `relative_url_root` 或等价配置） |
| **Rewrite** | 主站将 `/community` 与 `/community/*` 转发至 Discourse origin |
| **WebSocket** | 实时通知需代理 WS |
| **上传 / CDN** | `/community/uploads/` 路径需可达 |
| **Canonical** | 统一 `https://www.finalroundai.com/community`（与 schema、href 一致，避免 www / non-www 分裂） |

### 3.2 自建 Discourse（若迁移或扩容）

官方路径：[discourse_docker](https://github.com/discourse/discourse_docker) · [INSTALL-cloud.md](https://github.com/discourse/discourse/blob/main/docs/INSTALL-cloud.md)

| 步骤 | 说明 |
|------|------|
| 机器 | ≥2 GB RAM、≥2 vCPU、≥20 GB 磁盘（以官方文档为准） |
| Hostname | 若改子域：`community.finalroundai.com`；保持子路径则配 relative URL root |
| SMTP | 注册验证、通知 — **硬性依赖** |
| HTTPS | Let's Encrypt 或 CDN 终止 TLS |
| SSO | DiscourseConnect 对接 `accounts.finalroundai.com` |

### 3.3 其他曾评估方案（存档）

| 方案 | 何时再考虑 |
|------|------------|
| **Flarum / NodeBB** | 仅当 Discourse 运维成本不可接受 |
| **Circle / Turf 等 SaaS** | 零运维 + 强嵌入，但数据与 SEO 控制力弱 |
| **Discord / Slack** | 仅作辅助渠道，**不替代**公开可索引论坛 |

---

## 4. 优化待办（下一阶段）

与 [finalround-project-tasks.md](../finalround-project-tasks.md) §2、§5、§7 及内容策略对齐。  
**日常运营节奏、KPI、90 天路线图** → [community-ops-playbook.md](./community-ops-playbook.md)。

### 4.1 P0 — 集成与可发现性

| # | 任务 | 说明 |
|---|------|------|
| 4.1.1 | **Footer + 关键页 Navbar** | 全站 Footer 增加 Community；营销/SEO 页顶部导航可见（§5.2） |
| 4.1.2 | **canonical / www 统一** | 修复 schema 中 `finalroundai.com` vs `www.finalroundai.com` 不一致 |
| 4.1.3 | **修复 `/community/sitemap.xml` 500** | 确保 Discourse sitemap 或主站子 sitemap 可抓取 |
| 4.1.4 | **Pin 规则帖 + 去重欢迎帖** | 保留一条 Welcome；各分类 pin「About the {category}」 |

### 4.2 P1 — 内容与 SEO

| # | 任务 | 说明 |
|---|------|------|
| 4.2.1 | **Blog ↔ Community 互链表** | 如 STAR 文 ↔ STAR 帖；HireVue 文 ↔ HireVue 帖；见 [blog-interlinks.md](../blog/blog-interlinks.md) 扩展 |
| 4.2.2 | **interview-prep / interview-questions 链入社区** | 公司+题型页底部「Discuss in Community」 |
| 4.2.3 | **扩展 Tags** | `interview-copilot`、`mock-interview`、`hirevue`、`system-design` 等 → 产品页 |
| 4.2.4 | **Site Feedback 破冰** | 发 1–2 条引导帖，收集导航/分类意见 |
| 4.2.5 | **UGC 运营节奏** | 延续 Weekly wins；鼓励真实用户首帖（可配合 Referral / 产品内 CTA） |
| 4.2.6 | **Organization `sameAs`** | 主站 JSON-LD 增加 `https://www.finalroundai.com/community` |

### 4.3 P2 — 产品与账号

| # | 任务 | 说明 |
|---|------|------|
| 4.3.1 | **SSO** | DiscourseConnect ↔ 主站账号，避免二次注册 |
| 4.3.2 | **产品内入口** | Mock Interview / Copilot 结束后「分享到 Community」或「提问」 |
| 4.3.3 | **Discourse 主题品牌化** | Logo、色板对齐 [finalround-brand-visual.md](../finalround-brand-visual.md) |
| 4.3.4 | **审核与举报 SLA** | 规则已就绪；定响应时间与 escalation |
| 4.3.5 | **Blind / Reddit 舆情监测** | 按月检索 Final Round AI、interview copilot 相关帖；沉淀 FAQ 与 Community 主题（见 **§8**） |

### 4.4 与 Blog 的分工（避免重复）

| 渠道 | 适合内容 | 不适合 |
|------|----------|--------|
| **Blog** | 常青指南、SEO 程序化、产品评测、结构化 How-to | 个人实时问答、争议性 offer 细节 |
| **Community** | 个案提问、经验串、产品反馈、Weekly 互动 | 大篇幅模板化 SEO 文 |

---

## 5. 集成清单（上线 / 变更时自检）

- [ ] **HTTPS** 全站；无 mixed content  
- [ ] **SMTP** 发信正常  
- [ ] **Hostname / canonical** 与 Discourse 后台一致  
- [ ] **主站 ↔ 论坛** 双向导航（explore + Footer + 论坛 header 回主站）  
- [ ] **SSO**（若已启用）注册/登录链路测试  
- [ ] **爬虫**：公开分类可索引；`/community/sitemap.xml` 或主站 community 子 sitemap 正常  
- [ ] **UGC 政策**：规则帖 pin + 举报流程  
- [ ] **测量**：GA4 或 Discourse 分析 + 主题 Views/Replies 周报  

---

## 6. 外部参考

- Discourse 官网：https://www.discourse.org/  
- Discourse Docker：https://github.com/discourse/discourse_docker  
- Meta — HTTPS 与 Docker：https://meta.discourse.org/t/allow-ssl-https-for-your-discourse-docker-setup/13847  
- 主站 URL 树：[finalround-site-structure.md](../finalround-site-structure.md) §6.8  
- 内链规范：[internal-external-links-checklist.md](../technical/internal-external-links-checklist.md)  
- Schema：[finalround-schema.md](../technical/finalround-schema.md)  

---

## 7. 公开 Community 竞品调研（2026-06-04）

> **统计口径**：仅含 **品牌自有域名、可公开 URL、可被搜索引擎索引** 的论坛 / Q&A（含需注册后发帖但可浏览的站点）。  
> **不计入**：Discord、Slack、Facebook 群、付费学员私密群、Reddit / Blind（见 **§8**）。

### 7.1 调研结论（Executive）

| 结论 | 说明 |
|------|------|
| **Copilot 赛道几乎空白** | 直接竞品中，仅 **Final Round AI** 与 **VirtualInterview.ai** 有主域公开论坛 |
| **Final Round 差异化** | `Discourse` + `/community` 子路径；可进 sitemap、沉淀 SEO 长尾 |
| **活跃度差距** | Final Round 39 主题 vs PrepLounge 19k+ Q&A；短期不追量，追 **可索引 UGC 资产** |
| **对标对象** | 产品形态 → **VirtualInterview.ai**；社区运营形态 → **PrepLounge**（咨询向） |

### 7.2 AI Interview Copilot / Mock 直接竞品

| 产品 | 公开社区 | URL | 验证结果 |
|------|----------|-----|----------|
| **Final Round AI** | ✅ | https://www.finalroundai.com/community | Discourse；6 分类、39 主题 |
| **VirtualInterview.ai** | ✅ | https://virtualinterview.ai/forum | 自建论坛；分类含 Interview 等；免费档含 forum access（Terms） |
| **Verve Copilot** | ❌ | `/community` | 404 |
| **OphyAI** | ❌ | `/community` | 404 |
| **Interview Sidekick** | ❌ | `/community` | 404 |
| **LockedIn AI** | ❌ | — | 仅 Discord（非公网论坛） |
| **Beyz AI / Parakeet / Cluely / Sensei** | ❌ | — | 未发现 `/community` 或 `/forum` |
| **Huru / Interviews by AI / MockAI 等** | ❌ | — | 路径探测无公开论坛 |
| **Careerflow** | ❌ | `careerflow.ai/community` | 跳转 Discord，非公网论坛 |
| **Teal / Jobscan** | ❌ | `/community` | 404 |

**VirtualInterview.ai 备注**（最接近的产品对标）：

- 路径：`/forum`（非 `/community`）
- 搜索索引显示多分类（如 Interview 等）及讨论帖；页面部分内容需 JS / 登录后完整渲染
- 与主产品（AI mock、question library、job board）同域，模式类似 Final Round 的「内容 + 社区」

### 7.3 面试准备相邻产品（非 Copilot，公开论坛成熟）

| 产品 | URL | 规模（官方/页面宣称） | 与 Final Round 关系 |
|------|-----|----------------------|---------------------|
| **PrepLounge** | https://www.preplounge.com/en/consulting-forum | 56 万+ 用户；19k+ Q&A | 咨询/金融 case；**社区即产品**；可学 Q&A + Meeting Board 运营 |
| **Levels.fyi Community** | https://www.levels.fyi/community | Tech 群组 90 万+ 成员量级 | 面经、行为面、薪资；第三方平台内社区 |
| **Exponent** | — | 付费 **Slack**（非公网论坛） | Peer mock + 会员社群，不计入本表 |
| **interviewing.io** | Blog / Guides | 无用户发帖式公开论坛 | 内容营销，非 UGC 社区 |

### 7.4 对 Final Round `/community` 的策略含义

| 维度 | 建议 |
|------|------|
| **定位** | 主域 **可搜索知识库** + 产品反馈 + 转化辅助；不试图复制 PrepLounge 体量 |
| **内容** | 将 Reddit / Blind 高频问题（STAR、HireVue、Amazon LP、Copilot 伦理）做成 **常青主题帖**，链到 Blog / interview-prep |
| **竞品话术** | Copilot 赛道仅 VirtualInterview 有同类公开 forum；对外可强调「official community on-domain」 |
| **更新频率** | 每季度复核 **§7.2** 竞品是否新上 `/community`；有变更则更新本文 |

---

## 8. 第三方公开社区：Blind 与 Reddit

> **性质**：非 Final Round 自有；用户讨论 Interview Copilot、面经、裁员、薪资的 **主战场**。  
> **用途**：舆情监测、选题来源、理解用户语言；**不可替代** `/community` 的 SEO 与品牌归属。  
> **调研日期**：2026-06-04。

### 8.1 平台对比

| 维度 | [Blind](https://www.teamblind.com/) | [Reddit](https://www.reddit.com/) |
|------|-------------------------------------|-----------------------------------|
| **访问** | 频道 URL 可浏览；**发帖通常需职场邮箱验证** | 多数 subreddit **公开可读**；发帖需 Reddit 账号 |
| **匿名性** | 高（公司内匿名） | 高（用户名匿名） |
| **SEO** | 有限（登录墙 / 动态内容） | 强（Google 常收录帖子） |
| **与 Final Round 关系** | 科技从业者面经、TC、Copilot 检测讨论 | 更广人群；AI interview assistant 评测与伦理辩论 |
| **Final Round 提及** | Interview Experiences、SWE Interview prep、AI 频道 | r/cscareerquestions、r/recruitinghell、r/jobsearchhacks 等 |

### 8.2 Blind：与面试 / 求职相关的 Channel

> 完整目录：https://www.teamblind.com/channels — 下列为 **Learning & Advising** 与 **Job Function** 中与 Final Round 场景最相关的频道。

#### 8.2.1 Learning & Advising（优先监测）

| Channel | URL | 用途（与 Final Round 场景映射） |
|---------|-----|--------------------------------|
| **Interview Experiences** | https://www.teamblind.com/channels/interview-experiences | 公司面经、流程、结果；↔ Community **Interview Prep** |
| **SWE Interview prep** | https://www.teamblind.com/channels/swe-interview-prep | 算法 / 系统设计准备；↔ Copilot + coding 内容 |
| **Mock Interviews** | https://www.teamblind.com/channels/mock-interviews | 约 mock、反馈；↔ AI Mock Interview |
| **Career Coaching** | https://www.teamblind.com/channels/career-coaching | 职业问答（Open Access；约 236k followers） |
| **Resume Review** | https://www.teamblind.com/channels/resume-review | 简历点评；↔ Resume & Career 分类 |
| **Offer Evaluation** | https://www.teamblind.com/channels/offer-evaluation | Offer / TC 比较；↔ Success Stories、薪资谈判 |
| **OpenAI + Anthropic Prep** | https://www.teamblind.com/channels/openai-anthropic-prep | 大厂 AI 岗面试准备 |
| **MBA🎓** | https://www.teamblind.com/channels/mba%F0%9F%8E%93 | MBA 招聘季、咨询/金融面 |
| **English Fluency** | https://www.teamblind.com/channels/english-fluency | 非母语面试表达；↔ 多语言 Copilot 用户 |
| **Ask Blinders** | https://www.teamblind.com/channels/ask-blinders | 泛职场问答（3.4m followers） |
| **AMA** | https://www.teamblind.com/channels/ama | 嘉宾 AMA；可参考做 Community 活动 |

#### 8.2.2 Job Function（按角色引流 Community 分类）

| Channel | URL |
|---------|-----|
| Software Engineering | https://www.teamblind.com/channels/software-engineering |
| Product Management | https://www.teamblind.com/channels/product-management |
| Data Science | https://www.teamblind.com/channels/data-science |
| Strategy | https://www.teamblind.com/channels/strategy |
| Information Technology | https://www.teamblind.com/channels/information-technology |
| Design | https://www.teamblind.com/channels/design |

#### 8.2.3 相关 Trending / 交叉频道

| Channel | URL | 说明 |
|---------|-----|------|
| **Layoffs** | https://www.teamblind.com/channels/layoffs | 裁员动态；与 `/tech-layoffs` 内容可互证 |
| **Artificial Intelligence** | https://www.teamblind.com/channels/artificial-intelligence | AI 工具、ML 岗面试；Copilot 话题偶发 |
| **Personal Finance** | https://www.teamblind.com/channels/personal-finance | 薪资、谈判语境 |

#### 8.2.4 Blind 上关于 AI Interview Copilot 的讨论特点

- 工具名常被提及：**Final Round AI**、LockedIn AI、Cluely、Interview Sidekick、Sensei AI 等（多在 Interview Experiences / SWE prep 帖）
- 讨论焦点：**检测风险**、伦理、offer 是否 rescind、与 LeetCode / CoderPad 兼容性
- 用户也会问 **Discord / Slack 约练**（非公网 forum）；见例如 [Slack Channels or Discord groups for interview prep](https://www.teamblind.com/post/Slack-Channels-or-Discord-groups-for-interview-prep-m3RwkoTp)

### 8.3 Reddit：与面试 / 求职相关的 Subreddit

> 成员数为约数（第三方文章 / 公开资料，**非实时 API**）；订阅前请在 Reddit 搜索确认。

#### 8.3.1 高相关（Final Round 核心受众）

| Subreddit | URL | 典型内容与 Final Round 关联 |
|-----------|-----|----------------------------|
| **r/cscareerquestions** | https://www.reddit.com/r/cscareerquestions/ | 科技求职、面经、**AI interview copilot** 评测；Final Round 讨论最集中 |
| **r/leetcode** | https://www.reddit.com/r/leetcode/ | 编码面试、FAANG prep、mock 约练 |
| **r/jobsearchhacks** | https://www.reddit.com/r/jobsearchhacks/ | 求职技巧、工具选型；Copilot / mock 工具对比 |
| **r/recruitinghell** | https://www.reddit.com/r/recruitinghell/ | 候选人与 **招聘方双视角**；AI 作弊 / 检测伦理 |
| **r/GetEmployed** | https://www.reddit.com/r/GetEmployed/ | 广义求职、面试困境 |
| **r/interviews** | https://www.reddit.com/r/interviews/ | 面试专项（规模小于 CSQ，但题更集中） |

#### 8.3.2 职级 / 角色 / 行业

| Subreddit | URL | 场景 |
|-----------|-----|------|
| **r/ExperiencedDevs** | https://www.reddit.com/r/ExperiencedDevs/ | 资深工程师、系统设计、领导力面 |
| **r/csMajors** | https://www.reddit.com/r/csMajors/ | 新 grad、实习、初职 |
| **r/ProductManagement** | https://www.reddit.com/r/ProductManagement/ | PM 面试、产品 sense |
| **r/consulting** | https://www.reddit.com/r/consulting/ | 咨询行业；case 面（约 34 万+ 成员） |
| **r/MBA** | https://www.reddit.com/r/MBA/ | MBA 招聘季、咨询/金融面 |
| **r/MBBconsulting** | https://www.reddit.com/r/MBBconsulting/ | MBB case 准备、找练习搭档 |
| **r/financialcareers** | https://www.reddit.com/r/financialcareers/ | 投行 / 金融面试 |
| **r/dataengineering** | https://www.reddit.com/r/dataengineering/ | DE 面试、公司面经 |

#### 8.3.3 通用求职与简历

| Subreddit | URL | 场景 |
|-----------|-----|------|
| **r/jobs** | https://www.reddit.com/r/jobs/ | 通用求职、行为面 |
| **r/careerguidance** | https://www.reddit.com/r/careerguidance/ | 跨行业职业建议 |
| **r/careerchange** | https://www.reddit.com/r/careerchange/ | 转岗 |
| **r/resumes** | https://www.reddit.com/r/resumes/ | 简历点评 |

#### 8.3.4 与 AI Copilot 话题强相关（监测用）

| Subreddit | URL | 说明 |
|-----------|-----|------|
| **r/overemployed** | https://www.reddit.com/r/overemployed/ | 多 offer / 多面试并行；偶发工具讨论 |
| **r/ArtificialIntelligence** | https://www.reddit.com/r/ArtificialIntelligence/ | 泛 AI；Interview Copilot 偶发 |

**Reddit 上 Final Round AI / Copilot 讨论要点**（2025–2026 线程归纳，非官方统计）：

- **Mock / 准备模式**：评价偏正面；「练结构、减 rambling」
- **Live Copilot**：争议大——伦理、检测、Trustpilot 与 Reddit 叙事交叉
- **常被同屏对比的工具**：OphyAI、Cluely、LockedIn AI、Interview Sidekick、Parakeet AI
- **社区共识倾向**：Mock / 简历 / 准备类 AI **普遍接受**；live in-call assistant **需自律且存在风险**

### 8.4 三方社区分工（Final Round 应如何配合）

| 渠道 | Final Round 角色 | 不应做的事 |
|------|------------------|------------|
| **`/community`（自有）** | SEO 长尾、官方规则、产品反馈、Success Stories、Weekly wins | 冒充用户刷帖 |
| **Blind** | 监测面经与舆情；选题反哺 Community / Blog | 违规营销、马甲推广 |
| **Reddit** | 监测 r/cscareerquestions 等；FAQ 与规则帖回应真实痛点 | astroturf、违反 subreddit 自荐规则 |

**内容迁移示例**（Blind/Reddit 问题 → Community 主题）：

| 外部高频话题 | 建议 Community 分类 |
|--------------|---------------------|
| Amazon LP / behavioral | Interview Prep |
| HireVue / 异步视频 | Interview Prep |
| STAR / tell me about yourself | Interview Prep |
| ATS 简历格式 | Resume & Career |
| Copilot 是否 detectable | General（合规说明 + 链 FAQ） |
| Google PM / Meta coding 面经 | Interview Prep |

### 8.5 监测清单（运营 / 增长）

- [ ] 每月 Google：`site:teamblind.com "Final Round AI"`、`site:reddit.com "Final Round AI"`
- [ ] 订阅 Blind：**Interview Experiences**、**SWE Interview prep**、**Career Coaching**
- [ ] 订阅 Reddit：**r/cscareerquestions**、**r/jobsearchhacks**、**r/recruitinghell**
- [ ] 新主题写入 `/community` 后，更新 [finalround-site-structure.md](../finalround-site-structure.md) community 子 sitemap（若适用）
- [ ] 负面舆情（检测、退款、伦理）→ Product Feedback 或 FAQ 联动，**不在 Reddit 上与用户争辩**

---

## 9. 文档互引

| 文档 | 关系 |
|------|------|
| [finalround.md](../finalround.md) | 产品上下文 |
| [finalround-project-tasks.md](../finalround-project-tasks.md) | Forum 任务 §2；内链 §5 |
| [finalround-site-structure.md](../finalround-site-structure.md) | `/community/` URL 权威、 sitemap |
| [finalround-blog.md](../blog/finalround-blog.md) | Blog vs 论坛内容分工 |
| [finalround-production-routing.md](../technical/finalround-production-routing.md) | 子路径 Rewrite 参考 |
| [community-ops-playbook.md](./community-ops-playbook.md) | **运营 Playbook**：Pipeline、周/月节奏、KPI、90 天路线图 |

---

*线上数据以 2026-06-04 抓取为准；Topic 数、Views 随运营变化，优化阶段请定期更新 §1；竞品与 Blind/Reddit 清单每季度复核 §7–§8；运营执行见 [community-ops-playbook.md](./community-ops-playbook.md)。*
