# Today AI Blog — Content Graph

> 加载时机：Phase 0（选题）· Phase 2（路径/日期）· Phase 3.5 / 5.5
> 主文件：SKILL.md §4 · **下一序号：06**

---

## 1. 文件表

| NN | 文件 | slug | 类型 | category | 日期 | 主关键词 | 状态 |
|----|------|------|------|----------|------|---------|------|
| 01 | 01-what-is-today.md | what-is-today | BrandPillar | Product | 2026-08-03 | what is today / today ai | ✅ 已入库 |
| 02 | 02-meet-today.md | meet-today | Opinion | Insights | 2026-08-03 | meet today / today ai vision | ✅ 已入库 |
| 03 | personal-agent/03-what-is-ai-personal-agent.md | what-is-ai-personal-agent | GlossaryGuide | Guide | 2026-08-04 | AI personal agent | ✅ 已入库 |
| 04 | personal-agent/04-ai-personal-assistant-vs-ai-personal-agent.md | ai-personal-assistant-vs-ai-personal-agent | Comparison | Guide | 2026-08-05 | AI personal assistant vs agent | ✅ 已入库 |
| 05 | personal-agent/05-ai-personal-agent-vs-work-agent.md | ai-personal-agent-vs-work-agent | Comparison | Guide | 2026-08-06 | AI personal agent vs work agent | ✅ 已入库 |

**下一序号：06**

---

## 1B. Cluster 注册表（文件路径路由）

> Phase 0/2 对照本表决定 `today/blog/[{folder}]NN-{slug}.md`。
> 公开 URL 始终 `/blog/{slug}`。规则详见 `references/topic-cluster-layout.md`。

| Cluster ID | folder | Hub slug | 主 category | 说明 |
|------------|--------|----------|-------------|------|
| **personal-agent** | `personal-agent/` | what-is-ai-personal-agent | Guide | **AI personal agent** 主题簇（#03 Hub + 对比 spoke） |
| brand | *(root)* | what-is-today | Product | 品牌 / 产品（#01–#02 根目录） |

**standalone 判定**：不在上表 cluster 内 → `folder = (root)`。未来新簇需 ≥2 篇规划后再建子目录。

---

## 2. Hub-Spoke 树（已入库 + 规划）

```
personal-agent/ (Hub: what-is-ai-personal-agent) [#03 ✅]
├── 04-ai-personal-assistant-vs-ai-personal-agent [✅]
├── 05-ai-personal-agent-vs-work-agent [✅]
├── 06-living-memory-ai-assistant [待写]
├── 07-best-ai-personal-assistant [待写]
├── 08-today-vs-chatgpt [待写]
└── 09-ai-morning-brief [待写]

brand (Hub: what-is-today) [根目录 #01 ✅]
├── 02-meet-today [#02 ✅]
└── 链出 personal-agent 簇 + /landing
```

---

## 3. P0 Pipeline 队列

| 优先级 | NN | slug | 类型 | folder | 状态 |
|--------|-----|------|------|--------|------|
| P0 | 06 | living-memory-ai-assistant | BrandPillar | personal-agent/ | TBD |
| P0 | 07 | best-ai-personal-assistant | Comparison | personal-agent/ | TBD |
| P0 | 08 | today-vs-chatgpt | Comparison | personal-agent/ 或 root | TBD |
| P1 | 09 | ai-morning-brief | HowTo | personal-agent/ | TBD |

---

## 4. Canonical Concept Registry

| 概念 | Canonical slug | 他文处理方式 |
|------|---------------|-------------|
| **AI personal agent 定义** | what-is-ai-personal-agent | 1–2 句 + link |
| Assistant vs agent | ai-personal-assistant-vs-ai-personal-agent | 1–2 句 + link |
| Personal agent vs work agent | ai-personal-agent-vs-work-agent | 1–2 句 + link |
| Living memory 定义 | living-memory-ai-assistant | 1–2 句 + link |
| Today 产品定义 | what-is-today | 1–2 句 + link |

---

## 5. 推荐正文互链矩阵

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| what-is-ai-personal-agent | Hub | 04, 05, 01, /landing, /waitlist | 01, 02, 04, 05 |
| ai-personal-assistant-vs-ai-personal-agent | Spoke | 03, 05, 01, /waitlist | 03, 05 |
| ai-personal-agent-vs-work-agent | Spoke | 03, 04, 01, /waitlist | 03, 04 |
| what-is-today | Hub (brand) | 02, 03, 04, 05, /landing | 02, 03, 04, 05 |

---

## 6. 日期占用表

| 日期 | 已占用 slug |
|------|-----------|
| 2026-08-03 | what-is-today, meet-today |
| 2026-08-04 | what-is-ai-personal-agent |
| 2026-08-05 | ai-personal-assistant-vs-ai-personal-agent |
| 2026-08-06 | ai-personal-agent-vs-work-agent |

---

*content-graph · v1.4 · 2026-09-01 · layout: personal-agent/ cluster · next NN: 06*
