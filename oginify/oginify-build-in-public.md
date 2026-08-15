# Build in Public 日志

> **本文档职责**：Oginify 从零到一的每日日志——产品决策、成本账、踩坑、用户反馈。  
> **引用**：[主文档](./oginify.md) 概览 | [changelog](./oginify-CHANGELOG.md) 版本记录

---

---

## 定价策略 BiP 帖 · 归档 — 2026-06-03

### 做了什么

1. **定价叙事定稿** — TAM 大 + 用量两极分化 → 五层结构（Free / PAYG / Pro / Studio / Enterprise·API）；修正「低频工具」误述
2. **文档同步** — [oginify-others.md §定价依据](./oginify-others.md#定价依据)、[oginify.md](./oginify.md) v1/v2 商业模式
3. **即刻长文归档** — Part 1 Oginify 定价 + Part 2 通用 pricing playbook（可收藏向）→ [social-posts/published/bip-pricing/](./social-posts/published/bip-pricing/)

### 对外帖

- 即刻：[bip-pricing/jike.md](./social-posts/published/bip-pricing/jike.md)（archived，待发）

---

## Day 4 — 2026-06-03

> ⚠️ **管线重构**：Day 1–3 的「AI 四张图」管线已废弃。当前权威口径：Generator 主流程 **非 AI**（Firecrawl 截图 + Next.js 模板渲染，2 张输出），AI 仅用于 Regenerate。

> ⚠️ **定价锁定**：PAYG $0.99 / Bundle 10 $7.90 / Bundle 50 $29.00，Clink 支付已接入。

### 今天做了什么

1. **成本核实** — 基于 `src/lib/og-model.server.ts` 和 `src/routes/index.tsx` 确认：
   - Gemini Fast（`google/gemini-3.1-flash-image-preview`）经 Lovable AI Gateway 转售价 **$0.030/张**（非此前文档中的 $0.067 Google 官方价）
   - GPT Precise（`openai/gpt-image-2`, quality=low）**$0.024/张**
   - Firecrawl 轻度抓取 ~$0.003–0.005（主流程），JSON extract ~$0.005（Regenerate 路径）
   - aiBrief ~$0.002
   
2. **管线重构** — Generator 主流程从「AI 生成 4 张」变为「2 张混合输出」：
   - 第 1 张：Firecrawl 首屏截图 → top-crop 1200×630（非 AI）
   - 第 2 张：Next.js 模板渲染（Satori/resvg，非 AI）
   - AI 仅用于 Regenerate（用户手动触发补生成），成本 $0.030/$0.024 一次
   - 主流程从 ~$0.30/次 降至 ~$0.005/次

3. **配额模型变更** — 从「5 次/天」变为「6 张/天」（`src/lib/quota.server.ts`，单桶模型无关）

4. **定价锁定** — Clink 支付已接入，定价方案：
   - PAYG $0.99（2 张 + 6 次 regenerate 上限）
   - Bundle 10 $7.90 / Bundle 50 $29.00
   - Clink 费率：4.5% + $0.30/笔

5. **文档全量同步** — 更新了 oginify.md、oginify-technical.md、oginify-others.md、oginify-features.md、oginify-keywords.md 中的成本、管线、配额、定价口径

### 为什么这样做

- 主流程用 AI 的成本结构（~$0.30/次）不可持续——截图 + 模板覆盖 80% 场景，零 AI 成本
- AI 按需补充（Regenerate）而非每次强制调用——成本从 $0.30 → $0.005（主流程），AI 仅在用户不满意时触发
- Gemini Gateway 转售价 $0.030 是 Google 官方价 $0.067 的 45%——需要持续监控以防 Gateway 调价
- 6 张/天的配额模型比 5 次/天更直观（"我还有几张图可以出" vs "我还有几次可以跑"）

### 待办

- [ ] 给 PAYG 加 6 次 regenerate 硬上限
- [ ] 给免费入口接 Turnstile 验证码（防滥用：Cookie 6 张 + IP fallback ×3 = $0.54/天/IP）
- [ ] 建 `ai_usage_log` 表 + 埋点（独立对账，不受 Lovable balance 工作区污染）
- [ ] 方案 A 实测一次，锁定实测成本
- [ ] 确认 Firecrawl 当前套餐（Hobby vs Standard，6 倍差）

## Day 3 — 2026-05-31

> ⚠️ **定价口径更新**：Day 2 的「全功能永久免费 + Supporter $0.99 打赏 / Clink」已被后续决策取代。当前权威口径见 [oginify-others.md](./oginify-others.md#定价依据)：**5 次/天免费 + 付费版接入中（价格待定）+ Skills MIT 永久免费**。

> ⚠️ **对外叙事更新**：Day 1 的「OG 图是最后一公里 / 先上线后补」表述已修正。权威口径见 [oginify.md §产品价值主张](./oginify.md#产品价值主张)：**OG 图是社媒传播 + programmatic SEO 的每页定制化可视化元素，纳入发布流程而非事后补丁**。

### 今天做了什么

1. **M1 社媒首发** — LinkedIn carousel + X Article（Milestone 1）；归档见 [social-posts/published/M1-first-product/](./social-posts/published/M1-first-product/)
2. **文档与线上一致性审计** — 对照 oginify.com 全站，发现定价、产品矩阵、风格数量等多处文档滞后
2. **文档全面重组** — 按 client-template 六主文档 + others 架构重写；新增 site-structure、others；合并 costs
3. **定价策略最终口径** — 暂时 5 次/天免费；开源 Skills 永久免费；付费版接入中，价格上线后确认
4. **产品事实同步** — Above the Fold 已上线；6 风格；Websites Without 21 站；Templates / Twitter Card 等写入文档
5. **中文版 `/zh` 暂时下线** — 中文界面已撤回，当前仅英文；`/zh` 返回 404
6. **文档托管口径校正** — 确认项目**仍托管 Lovable**，oginify.com 为绑定域名；修正文档中「已迁独立站」误述
7. **OG 尺寸管线文档化** — Lovable 上安全区留白 + 裁切方案；即刻 BiP 帖归档至 [social-posts](./social-posts/published/bip-lovable-og-size/)

### 为什么这样做

- 文档是 SEO、增长、Build in Public 的单一事实源——与产品脱节会误导内容和决策
- client-template 要求 site-structure 标配、杂项进 others，避免主文档重复膨胀
- 5 次/天是在成本（~$0.30/次）与试用门槛之间的平衡点

### 待办

- [ ] 完成支付接入（价格待定）
- [ ] 线上 Pricing / Twitter Card 页 copy 与文档口径对齐
- [ ] Gallery 条目数后台核实
- [ ] Platforms with Built-in OG 页面
- [ ] 中文版 `/zh` 恢复（时间待定）

---

## Day 2 — 2026-05-30

### 今天做了什么

1. **Clink 支付接入** — [oginify.com/pricing](https://oginify.com/pricing) ⚠️ 定价模型已废弃，当前为 5 次/天免费 + 付费接入中
   - 定价模型定为：**全功能永久免费** + **Supporter $0.99 一次性打赏**
   - Clink 托管 PCI 合规结账，只需邮箱收收据，无需账号
   - 状态：**已接入但未完全完成**，想抢先体验的可以抓紧

2. **Open Graph Validator** — [oginify.com/open-graph-validator](https://oginify.com/open-graph-validator)
   - 粘贴 URL → 读取 OG / Twitter Card 标签 → 0–100 评分 + pass/warn/fail 清单
   - 实时预览 X、Facebook、LinkedIn、Slack、Discord 上的链接展开效果
   - 与生成器形成漏斗：校验发现问题 → 引导 AI 生成新 OG 图

3. **OG Image Gallery** — [oginify.com/gallery](https://oginify.com/gallery)
   - 手工 curated 约 **100** 个知名品牌的真实 `og:image`
   - 分类：SaaS、AI、Dev tools、Design、E-commerce、Media、Fintech
   - 定位：设计灵感库 + pSEO 内容资产

4. **开源产品 social-cards-skills** — [github.com/kostja94/social-cards-skills](https://github.com/kostja94/social-cards-skills)
   - MIT 许可，Oginify 的商业化互补品
   - 2 个 Agent Skills：`og-image-generator`（1200×630）+ `twitter-card-image-generator`（1200×675）
   - 6 视觉风格 + Satori/resvg 渲染 + AI 图像管线 + Agent-Native 内容感知工作流
   - 安装：`npx skills add kostja94/social-cards-skills`
   - 配套 [marketing-skills](https://github.com/kostja94/marketing-skills) 负责 SET meta 标签，本仓库负责 CREATE 图像

5. **Websites Without OG Image** — [oginify.com/websites-without-og-image](https://oginify.com/websites-without-og-image)
   - 实测抓取并确认 **20** 个知名站点缺失 `og:image`（后续已更新至 21 站）
   - 覆盖 Hacker 文化（HN、xkcd、motherfuckingwebsite.com）、金融/权威机构（Berkshire Hathaway、W3.org）、老牌技术站（GNU、Linux kernel、LWN）、极简新闻（text.npr.org、lite.cnn.com、old.reddit.com）、学术/博客（arXiv、Paul Graham、Dan Luu）
   - 技术实现：`og_audit_items` 表 + RLS + GRANT，支持按 issue 类型和行业过滤，详情 Dialog + methodology 说明 + takedown 入口
   - Footer 放 takedown 链接防法律风险，每个条目标注抓取时间避免数据过期

6. **内置 OG 生成平台调研** — 已记录，页面待实施
   - 读完 [Vercel 动态 OG 文章](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images)
   - 整理了四大类平台的自动 OG 方案：框架/Hosting（Vercel @vercel/og、Next.js、Nuxt、Astro、SvelteKit）、CMS/Blogging（WordPress Jetpack、Ghost、Substack、Medium、Dev.to、Hashnode）、代码托管/文档（GitHub、GitLab、Mintlify、Docusaurus）、No-code（Framer、Webflow、Notion、Read.cv）
   - 计划建 `/platforms-with-built-in-og` 页面，与 `/websites-without-og-image` 形成正反对照

### 为什么这样做

- **Validator**：SEOer 日常刚需——客户问"为什么分享没图"，以前要逐个平台 debugger 试，现在一个页面搞定
- **Gallery**：OG 设计没有标准答案，看真实案例比看教程有用；同时是天然的 SEO / 内容入口
- **Websites Without OG Image**：和 Gallery 形成正反对照——「看，连这些大牌都漏了，你也该检查一下」。SEO 价值很高：「sites without og image / missing open graph examples」是长尾但精准的搜索词，搜这些词的正是目标用户（排查 OG 问题的开发者/marketer）。每个被列出的知名网站本身自带搜索量，页面标题里的品牌名就是流量
- **Platforms Built-in OG（规划中）**：正面案例清单，定位为「如果你的平台已经内置了 OG 生成，直接用；如果没有，用 Oginify」。本身是决策工具页 + SEO 长尾（"Vercel og image generation""WordPress social image generator" 这类搜索词），和前两个页面形成三件套：正面案例 / 反面案例 / 灵感参考
- **开源 skills**：商业化 SaaS 和开源 Agent 工具不冲突——不想跑 infra 的人用 Oginify，想在 Cursor 里程序化出图的开发者用 skills
- ~~**$0.99 打赏模式**~~ ⚠️ 已废弃：单次生成成本 ~$0.30 时打赏无法覆盖；当前为 6 张/天免费 + PAYG / Bundle 定价

### 内容策略：三层对照

| 页面 | 定位 | 搜索意图 | 产品漏斗角色 |
|------|------|----------|-------------|
| Gallery | 正面灵感 | "og image examples / best og images" | 启发 → 试试生成器 |
| Websites Without | 反面警示 | "sites without og image / missing meta tags" | 焦虑 → 检查自己的站 |
| Platforms Built-in（待建） | 决策参考 | "vercel og / wordpress social image" | 教育 → 没内置？用 Oginify |

三个页面不互相竞争，各自吃不同搜索意图，最终都导向 Generator 和 Validator。

### 定价策略变化 ⚠️ 已废弃，当前为 5 次/天免费 + 付费接入中

| | Day 1 | Day 2 |
|---|-------|-------|
| 免费额度 | 3 次/天（Lovable $1/月额度妥协） | 全功能无限免费 |
| 变现方式 | 待接入 Stripe | Clink $0.99 一次性 Supporter（接入中） |
| 托管 | Lovable MVP | Lovable + 绑定 oginify.com |

### 待办

- [x] 接入支付（Clink，进行中）
- [ ] 迁移 Lovable → 独立商业栈（待定）
- [x] Websites Without OG Image 上线（20 个确认站点，后续已更新至 21 站）
- [ ] 完成 Clink 支付全流程
- [ ] 模型切换功能（降低成本）
- [ ] Gallery / Validator / Websites Without 的 pSEO 和内容分发
- [ ] Platforms with Built-in OG 页面（正反对照第三块）

### 学到了什么

- 产品矩阵比单点工具更有护城河：生成 → 校验 → 灵感库 → 反面清单 → 开源 skills，每条路径都能触达不同用户
- ~~「免费 + 自愿打赏」在 dev tool 圈有先例（如 Excalidraw）~~ ⚠️ 已废弃，定价模型已变更
- 内容页面的 SEO 杠杆：一个手工 curated 的知名网站清单比十篇 AI 生成的文章更有搜索竞争力——真实数据、有故事性、每个条目自带品牌搜索量
- 正反对照是很好的叙事结构：Gallery（好案例）+ Websites Without（反面教材）+ Platforms Built-in（决策工具），三页合在一起比单独一页说服力强得多

---

## Day 1 — 2026-05-29

### 为什么要做

我是 SEOer，日常给客户做站。OG 图不是上线后「有空再补」的最后一步——它是**社媒传播**和 **programmatic SEO** 里每页都需要的定制化可视化元素：链接被分享时的预览图、Discover 引流的视觉入口、pSEO 规模化站点里每一张 URL 的独立面孔。

给一个 **AI Notes Generator** 客户做 SEO 时，我们为各页面配置了定制化 OG 图，配合社媒分发——分享预览立刻变专业，点击表现明显改善。需求真实、高频、自己用得上（Dogfooding），干脆自己下场做工具。

另一个动机：我倒是想试试，做产品到底有多难。

### 今天做了什么

- **域名**：$11.10 拿下 [oginify.com](https://oginify.com)，已绑定 Lovable
- **MVP 在 Lovable 上线**：https://oginify.lovable.app/
- 功能：粘贴 URL → AI 读懂页面 → 一次出四张 1200×630 OG 图
- 四种风格：品牌贴合 × 1、终端风、杂志风、复古印刷风（后续已扩展至 6 风格：Swiss / Magazine / Terminal / Brutalist / Newspaper / Pixel）
- 底层模型：Google Gemini (Nano Banana 2)，通过 Lovable AI Gateway

### 成本账

- 单次生成 4 张 1K 图：~$0.268（约 ¥1.95）
- Lovable 免费 AI 额度：$1/月
- 因此匿名用户限额设为 **3 次/天**——一个恶意用户一天就能烧掉整月额度
- Lovable AI Gateway 不加价，直接按 Google 官方价

### 待办

- [ ] 接入支付（香港银行卡已办，待接入 Stripe/其他）
- [ ] 迁移 Lovable → 独立商业栈
- [ ] 模型切换功能（降低成本）
- [ ] 探讨 OG 图 × 社媒传播 × pSEO 的内容

### 即刻帖子

发了 Build in Public 第一天的帖子，公开了产品、定价、成本结构。

### 想法

如果 Lovable、vibe coding 工具、Shopify 这类平台能内置 OG 图生成功能就好了——开玩笑，但值得记一笔。大 B 集成可能是未来的方向。

---

*格式参考：最新更新在顶部。每条记录包含做了什么、为什么、学到了什么。*
