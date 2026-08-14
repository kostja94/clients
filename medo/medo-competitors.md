# MeDo 竞品分析

> **本文档职责**：竞品矩阵、场景对比、差异化；功能见 [medo-features.md](./medo-features.md)。  
> **引用**：[medo.md](./medo.md) | [medo-keywords.md](./medo-keywords.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [medo.md](./medo.md) |
| 功能 | [medo-features.md](./medo-features.md) |
| 关键词 | [medo-keywords.md](./medo-keywords.md) |
| 使用场景 | [medo-use-cases.md](./medo-use-cases.md) |
| 网站结构 | [medo-site-structure.md](./medo-site-structure.md) |
| 增长策略 | [medo-growth-strategy.md](./archive/medo-growth-strategy.md) |

---

## 一、竞品分层

| 层级 | 代表 | 与 MeDo 关系 |
|------|------|----------------|
| **全栈 AI Builder** | Lovable、Bolt.new、Replit Agent | 直接争夺「对话 → 可上线 App」 |
| **前端/组件 AI** | v0 (Vercel)、Framer AI | UI 强；后端与 DB 常需另配 |
| **传统低代码** | Bubble、Glide、FlutterFlow | 可视化强；AI 原生程度较低 |
| **云厂商 App Builder** | Firebase Studio、AWS PartyRock 等 | 生态绑定；MeDo 绑 **Baidu AI Cloud** 叙事 |
| **国内平台** | 各厂「妙搭/通义/App Builder」 | 区域与合规竞争（**待验证** 功能表） |

---

## 二、直接竞品拆解（≥3）

### 2.1 Lovable

| 维度 | Lovable | MeDo |
|------|---------|------|
| **定位** | AI 全栈 Web App，React + Supabase 常见 | 全栈 + 多 Agent；广场 + Baidu 背书 |
| **优势** | 社区声量大、模板与 Remix 成熟 | credits 低价叙事、分类广场规模、Hackathon |
| **后端** | 深度集成 Supabase | 案例含 Supabase；官方称数百 API（**待验证** 默认栈） |
| **机会** | 用户嫌贵或要中文支持 | /vs/lovable + 价格对比 |

**最后验证**：2026-06-04 | **AI 可见度**：高

### 2.2 Bolt.new

| 维度 | Bolt.new | MeDo |
|------|----------|------|
| **定位** | 浏览器内全栈原型与部署 | 对话 + Agent；发布至 MeDo 托管 URL |
| **优势** | StackBlitz 生态、即时预览 | 多 Agent、PRD 快捷流、应用广场 UGC |
| **差异** | 偏开发者即时编码环境 | 偏「非技术也可」+ 运营活动（联盟/Hackathon） |
| **机会** | 非技术用户觉得 Bolt 偏工程 | 强调 *no programming experience*（官方文档） |

**最后验证**：2026-06-04 | **AI 可见度**：高

### 2.3 Replit Agent

| 维度 | Replit Agent | MeDo |
|------|--------------|------|
| **定位** | IDE + Agent 生成并运行项目 | 无代码对话优先 |
| **优势** | 完整 IDE、多语言、协作 | 更低门槛、credits 定价、百度云企业叙事 |
| **差异** | 仍面向会看代码的用户 | 截图标注改 UI、跳过闲聊 PRD |
| **机会** | 教育者/PM 不要 IDE 复杂度 | /for/education、/for/product-managers |

**最后验证**：2026-06-04 | **AI 可见度**：中

---

## 三、场景级对照表（≥2）

### 表 A：「48 小时验证付费 SaaS MVP」

| 选项 | 全栈 DB | 支付插件 | 非技术友好 | 定价入门 |
|------|---------|----------|------------|----------|
| MeDo | ✓（叙事+案例） | Stripe 插件 | 高 | $5/2000 credits（PH） |
| Lovable | ✓ | 集成 | 高 | **待验证** |
| Bolt | ✓ | 依栈 | 中 | **待验证** |
| v0 | UI 为主 | 需自建 | 中 | N/A |

### 表 B：「做小游戏并要排行榜」

| 选项 | 持久化 | 资产/音效 | 广场传播 |
|------|--------|-----------|----------|
| MeDo | Supabase 等自动（案例） | 对话生成 | 首页 Game 分类 |
| 纯前端 AI | 常无 | 有限 | 弱 |
| 传统引擎 | 强 | 强 | 需自行发行 |

---

## 四、对比矩阵（摘要）

| 维度 | MeDo | Lovable | Bolt | v0 |
|------|------|---------|------|-----|
| 全栈默认 | 强调 | 强调 | 强调 | 弱 |
| 多 Agent | ✓ 官方 | **待验证** | **待验证** | — |
| 作品广场 | 超大规模 UGC | 有 | 有 | 弱 |
| 大厂背书 | Baidu | — | StackBlitz | Vercel |
| 联盟/Hackathon | ✓ 官网 | **待验证** | **待验证** | — |

---

## 五、MeDo 差异化话术（对外）

1. **真全栈**：前后端、库表、逻辑一次生成，而非静态页。  
2. **多 Agent 分工**：复杂需求并行，缩短等待。  
3. **极低试错成本**：credits + 每日免费额度（需定价页坐实）。  
4. **社会证明**：PH #1 + 万级广场作品。  
5. **增长飞轮**：Hackathon + 30% Affiliate 拉动创作者与推广者。

---

## 六、威胁与机会

| 类型 | 内容 |
|------|------|
| **威胁** | Lovable/Bolt 品牌心智、OpenAI/Anthropic 内置 App 生成、平台锁定与导出限制质疑 |
| **机会** | 教育/小游戏/问卷垂直模板 SEO；中文与亚太云背书；联盟 KOL 规模化 |

---

*对比页建设见 [medo-site-structure.md](./medo-site-structure.md) Phase 2*
