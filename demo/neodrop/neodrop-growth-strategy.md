# NeoDrop — 增长策略

> 遵循 [客户文档规范](../../client-template.md)
> **本文档职责**：增长渠道、实验、内容计划、SEO/GEO 策略。  
> **引用**：[neodrop-keywords.md](./neodrop-keywords.md) 关键词 | [neodrop-site-structure.md](./neodrop-site-structure.md) 站点结构

**最近更新**：2026-05-22（初建）

---

## 一、当前增长状态

| 指标 | 数据 | 说明 |
|------|------|------|
| Discover 频道数 | 数十个（可见榜单各 12+） | 早期生态 |
| 头部 Channel 订阅 | ~12（Daily AI R&B 等） | 双边市场极早期 |
| 官方示范 Channel | NeoDrop Official（Editor's Picks） | 质量锚点已有 |
| 定价 | $0 / $3.99 / $20 / $200 | 低门槛 Starter |
| 内容资产 | 高质量 Drop（如 AI Agent 生态速报） | 可复用于 SEO/社交 |
| 第三方评测 | ⚠️ 未见 | 社会证明缺口 |

---

## 二、增长渠道

### 1. 产品驱动增长（PLG）

**目标**：Discover 订阅 → 创建 Channel → 付费 Credits

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **Editor's Picks 质量** | 维持 Official Channel 作为「样板间」 | P0 |
| **Feed 推荐冷启动** | 新用户注册后默认推荐 3–5 个高质 Channel | P0 |
| **Create Channel 降低摩擦** | 未登录可预览向导，登录后再生成 | P1 |
| **Drop 分享卡片** | `/feed/{id}` 增加 OG 图 + 一键分享 X/LinkedIn | P0 |
| **Credits 用量仪表盘** | 让用户感知「还剩多少 Drop 产能」 | P1 |

### 2. 内容营销（SEO + 示范 Drop）

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **官方 Research Drop 系列** | 每周「AI Agent 生态速报」类长文 → 外链与 SEO | P0 |
| **Channel 分类 Landing** | `/channels/ai` 等，聚合 Discover 优质 Channel | P1 |
| **竞品对比内容** | vs Yournalist / Perceptive / Feedly（见 keywords） | P1 |
| **Creator Story** | 采访 Fastest Growth Channel 创建者 | P2 |
| **中文 AI 资讯 Channel** | 已有中文 Drop，可针对中文 SEO | P2 |

### 3. 社区与分发

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **Product Hunt 发布** | 定位 *Create your own AI content channel* | P0 |
| **Hacker News Show** | 以「AI Agent 生态速报」样例 Drop 为引子 | P0 |
| **Reddit** | r/artificial、r/LocalLLaMA、r/sidehustle — 分享 Channel 创建体验 | P1 |
| **X/Twitter** | 官方账号转发 Daily Drop + Creator Channel | P1 |
| **Discord 社区** | Channel 创建者交流模板与 credits 技巧 | P2 |

### 4. 创作者增长（Supply Side）

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **Fastest Growth 榜单运营** | 激励竞争，制造「榜上有名」叙事 | P1 |
| **Starter $3.99 推广** | *Launch your first channel for less than a coffee* | P0 |
| **Pro 首月 bonus** | 5,000 credits 作为升级钩子 | P1 |
| **MCN/Studio  outreach** | 定向邀请多账号团队试用 Studio | P2 |

### 5. 付费转化

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **Free → Starter 触发** | Credits 用尽时提示「$3.99 维持 Channel」 | P0 |
| **Pro Deep Research 展示** | 对比 Free 与 Pro Drop 深度 side-by-side | P0 |
| **年付折扣** | ⚠️ 当前仅月付，可考虑年付 -20% | P2 |

---

## 三、SEO 内容策略（内容层级）

```
品牌认知
  ├── 「The content about you, by you, for you」品牌叙事
  └── 官方 Research Drop（AI Agent 生态速报等）
      │
功能搜索
  ├── /features — AI content channel platform
  ├── /create/agent — create AI newsletter channel
  └── /pricing — AI credits content pricing
      │
场景搜索
  ├── Discover 分类页（AI / Side Hustle / Finance）
  └── Use case Landing（developers / creators）
      │
竞品拦截
  ├── /vs/yournalist
  ├── /vs/perplexity-discover
  └── /alternatives/feedly-leo
```

---

## 四、战役方向（§0.3 达标）

### 战役 1：「第一条 Channel」激活

| 要素 | 内容 |
|------|------|
| **目标** | 7 日内注册 → 创建 Channel 转化率 |
| **受众** | AI/科技 Twitter、HN、PH 访客 |
| **内容主题** | *Describe your obsession, get a weekly AI channel* |
| **栏目对应** | `/create/agent`、官方教程 Drop |
| **实验** | A：先订阅再创建 vs B：先创建再订阅 |

### 战役 2：Research Drop 外链建设

| 要素 | 内容 |
|------|------|
| **目标** | 单篇 Drop 获 10+ 高质量外链 |
| **受众** | AI 从业者、Newsletter 读者 |
| **内容主题** | 每日/每周 AI Agent 生态速报 |
| **栏目对应** | `/feed/{id}`、未来 `/blog` 镜像 |
| **实验** | 在 X 发布 Thread 摘要链回全文 |

### 战役 3：Discover 供给侧

| 要素 | 内容 |
|------|------|
| **目标** | 30 天内 Fastest Growth 频道 ≥20 个 |
| **受众** | 个人创作者、垂直 KOL |
| **内容主题** | *Run a channel without writing every word* |
| **栏目对应** | Discover 榜单、Creator Story |
| **实验** | 首月 Pro bonus 仅对公开 Channel 开放 |

---

## 五、GEO / AI 可见度

| 动作 | 说明 |
|------|------|
| **结构化 Drop** | Research Brief + 引用 + 章节标题，利于 AI 摘要引用 |
| **FAQ 页扩展** | Pricing FAQ 扩至全站 FAQ（Channel、credits、版权） |
| **llms.txt** | 提供产品定义、定价、官方 Channel 链接 |
| **对比页** | 「NeoDrop vs X」供 AI 检索时引用差异表 |

---

## 六、调研 Backlog

| ID | 需查证 | 优先级 | 计划来源 |
|----|--------|--------|----------|
| R1 | 是否支持 Email 订阅/export RSS | P0 | 产品实测 |
| R2 | 公司主体与团队背景 | P1 | 联网/LinkedIn |
| R3 | Drop 内容版权与引用政策 | P1 | `/paid-terms`、FAQ |
| R4 | 移动端 App 路线图 | P2 | 官方渠道 |
| R5 | Channel 是否可设 Private | P2 | 产品实测 |

---

*文档创建日期：2026-05-22 | 模式：冷启动*
