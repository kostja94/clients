# Hellyeah Use Cases 与 Persona

> **职责**：Arena（**`/for/{slug}`**）、Persona、故事线。  
> **关联**：[hellyeah-keywords.md](./hellyeah-keywords.md) | [hellyeah-others.md](./hellyeah-others.md) §1.4

**Last updated**: 2026-06-02

---

## 1. Arenas（行业）

落地页 **`/for/{slug}`**（线上 nav 称 **Arena**，非 `/arenas/`）。

| Arena（nav 英文） | slug | 线上 URL | 案例关联 |
|-------------------|------|----------|----------|
| Mobile Applications | mobile-apps | `/for/mobile-apps` | BeFreed, The Dyrt |
| B2B & Enterprise | b2b-enterprise | `/for/b2b-enterprise` | Eragon |
| Consumer Tech | consumer-tech | `/for/consumer-tech` | Final Round AI, Viggle, Fish Audio |
| E-Commerce | ecommerce | `/for/ecommerce` | （能力页链入） |
| Gaming & Entertainment | gaming | `/for/gaming` | Playco |
| Fintech | fintech | `/for/fintech` | Truist |
| EduTech | edutech | `/for/edutech` | |

**页内机制**（`/for` 索引）：垂直 benchmark、合规规则、同一 command layer 切换 context。

| 旧 slug（文档废弃） | 新 slug |
|---------------------|---------|
| enterprise-b2b | b2b-enterprise |
| gaming-entertainment | gaming |
| fintech-saas | fintech |
| education-learning | edutech |

---

## 2. Persona

| Persona | 目标 | 痛点 | 叙事 / 页面 |
|---------|------|------|-------------|
| CMO / VP Marketing | 可预测增长 | 工具栈碎 | `/solutions/improve-marketing-roi` |
| Head of Growth | 实验速度 | 人工队列 | Agentic + Déjà Vu |
| Performance Lead | ROAS | 夜间浪费 | `/capabilities/performance-marketing` |
| Lifecycle Lead | 留存 | 静态 drip | `/capabilities/lifecycle-automation` |
| Influencer Lead | 达人 ROI | 协调成本 | `/capabilities/influencer-marketing` |
| RevOps | 归因 | 数据孤岛 | Mutation + Forge |
| Founder / Indie | 少人头 | 无 agency | `/aima` Free + CLI |
| Growth engineer | 可编程 | 集成 | CLI / SDK / About |

---

## 3. 情境故事线（与案例对齐）

- **大促（E-Commerce）**：Mutation 信号 + Performance 优化 + Creative 测试 → `/for/ecommerce`  
- **PLG B2B（Eragon）**：Mutation 归因 + Lifecycle → `/customers/eragon`  
- **消费 App 爆发（Final Round AI）**：AIMA paid + SEO/GEO → `/customers/final-round-ai`  
- **物流事件（J&T）**：Mutation + Influencer → `/customers/jt-express`  
- **银行合规（Truist）**：Forge pod + Lifecycle → `/customers/truist`

---

## 4. 待填充

- [ ] 每 Arena 1 条匿名案例（若不能具名）  
- [ ] EduTech / E-commerce 案例页补全（sitemap 暂无 dedicated case）
