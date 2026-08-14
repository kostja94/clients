# Floatboat Skills 生态策略

> Combo Store 关键词优化、Skills Leaderboard、用户提交、Skills 比赛、Agent Skill Creator 工具。
>
> **关联**：[floatboat.md](./floatboat.md) · [floatboat-keywords.md](./floatboat-keywords.md) · [floatboat-site-structure.md](./floatboat-site-structure.md)

**Last updated**: 2026-05-06

---

## 1. 整体路线图

| Phase | 内容 | 优先级 |
|-------|------|--------|
| **Phase 1** | Combo Store 关键词 SEO 优化（原路由不变，Title/Meta 对齐品类词） | P0 |
| **Phase 1** | Skills Leaderboard MVP 上线 | P0 |
| **Phase 2** | Skills 详情页模板重设计 + 高搜索量 skill 独立页填充 | P0 |
| **Phase 3** | `/submit` 用户提交 + 审核流程 | P1 |
| **Phase 4** | Skills 比赛策划（一人公司主题） | P1 |
| **Phase 5** | Agent Skill Creator 工具调研与 MVP | P2（前瞻） |

---

## 2. Combo Store 关键词策略

**核心判断**："Combo Store" 是产品内部品牌名，搜索量低于品类通用词。

| 优化方向 | 品类关键词 | 说明 |
|----------|-----------|------|
| **主攻** | Agent Skills Store | 品类词，搜索意图明确 |
| **次攻** | Skills Marketplace | 替代/对比类检索 |
| **覆盖** | Skills Platform / AI Skills Platform | 平台型关键词 |
| **长尾** | reusable AI skills / no-code agent skills | 功能描述向 |

**执行**：
- `/combo-store` 路由不变
- Title 用 `Agent Skills Store — Browse & Reuse AI Skills for Your Desktop`
- H1 可保留 Combo Store 品牌名 + 副标题解释

---

## 3. Skills Leaderboard

**定位**：纯 SEO 导向页面，借鉴 [skills.sh](https://skills.sh)（Vercel 运营的 Agent Skills 目录，75,000+ skills）模式。

**排名维度（择一或并行）**：

| 维度 | 数据源 | 说明 |
|------|--------|------|
| **安装量/使用量**（推荐首选） | 自有数据 | 与 skills.sh 的排名逻辑一致（skills.sh 按 `npx skills add` 安装量排序）；体现产品生态真实活跃度 |
| **GitHub Stars** | 公开数据 | 覆盖面广，但并非 skills.sh 的排名方式；适合初始填充时做冷启动 |
| **综合排名** | 二者加权 | 较复杂，后期可考虑 |

**页面对 SEO 的意义**：
- 承载长尾词：best AI skills、top agent skills、skills leaderboard 2026
- 内链枢纽：每条 skill 链接至详情页 → 回 Leaderboard
- 更新频率代表站内活跃度

**推荐初始填充**：
- **方式 A（冷启动）**：基于公开 GitHub 仓库的 AI agent skills，按 Star 数排列
- **方式 B（有数据后切换）**：按 Floatboat 用户实际安装量/使用量排列，与 skills.sh 逻辑一致
- **skills.sh Top 参考**（2026年初）：find-skills（120万+ 安装）、vercel-react-best-practices（35万+）、frontend-design（34万+）、web-design-guidelines（28万+）— 头部效应明显，长尾覆盖空间大

---

## 4. Skills 详情页模板

### 4.1 问题

现有详情页模板需重新设计，当前版本信息层级和信息密度不足。

### 4.2 新模板结构（建议）

```
Hero 区：Skill 名称 + 一句话用途 + 作者 + ⭐ 数/安装量
├── 功能亮点（3-5 点 bullet）
├── 使用场景 / 适用人群
├── 效果展示 / Screenshot / Demo
├── 安装与使用方式
├── Requirements / 依赖
├── FAQ
└── 相关 Skills（内链 3-5 条）
```

### 4.3 高搜索量 Skill 目标（按搜索数据确认）

| Skill | 说明 |
|-------|------|
| Gstack | 技术受众，搜索量稳定 |
| Lenny's Podcast Skill | 内容营销/创作者受众 |
| Superpowers (Jesse Vincent) | 个人效能类别 |

后续迭代按搜索数据持续扩展。

---

## 5. 用户提交 Skills（`/submit`）

### 5.1 流程

用户 → `/combo-store/submit` → 填写模板（名称、描述、技能文件、标签） → 审核 → 上线 → Leaderboard 计数

### 5.2 审核标准

- 格式合规（skills.md 规范）
- 功能可运行
- 不含恶意代码
- 标签分类正确

### 5.3 激励

- Leaderboard 展示 + 作者署名
- 参赛/评选曝光
- 内链流量回创作者来源

---

## 6. Skills 比赛策划（P1）

**参考**：Youmind 技能比赛，以内容营销为主要驱动力。

### 6.1 建议方向

| 元素 | 建议 |
|------|------|
| **主题** | 一人公司效率 Skills（与产品定位一致） |
| **赛制** | 提交 + 社区投票 + 评委评选 |
| **奖项** | 曝光、Featured 位置、产品内勋章 |
| **推广** | 参赛者自发社媒传播、官博发文、邮件通知 |

### 6.2 内容营销价值

- 每位参赛者 = 一个传播节点（X/LinkedIn/博客）
- 参赛作品自动填充 Skills Store 内容库
- 比赛公告 + 结果公布 = 两篇高质量 blog

---

## 7. Agent Skill Creator（前瞻 — P2）

**核心概念**：将用户的本地工作流程/文档 → 转为符合规范的 skills.md。

### 7.1 市场判断

| 维度 | 分析 |
|------|------|
| **当前搜索量** | 低 — 属于功能缺口而非流量缺口 |
| **趋势** | Skills 生态 → 更多人需要写 skill → 需要创作工具 |
| **先发价值** | 如果一人公司 + 本地文件 + skills 趋势成立，早期入场有优势 |

### 7.2 MVP 定义（初案）

| 功能 | 说明 |
|------|------|
| **输入** | 用户描述工作流程（自然语言 / 步骤列表）、参考文档（md 文件） |
| **处理** | 基于 skill 规范 + best practice 模板，生成结构化 skills.md |
| **输出** | 可直接使用的 skill 文件 |
| **UI** | Web 小工具页或内嵌于 workspace 功能 |

### 7.3 内容配合

- 教程系列：「如何写好一个 Skill」「Skill 最佳实践指南」
- 模板库：提供常见场景的 skill 模板供用户修改
- 降低最佳实践门槛：规范格式易学，高质量 skill 需要引导

---

## 8. 内链闭环

```
Leaderboard ──→ Skill Detail ──→ Submit
    ↑                               │
    └────────── Store ←──────────────┘
```

- Skills Leaderboard → 每条 skill 链接详情页
- Skill Detail → 相关 skills + 回 Leaderboard
- Submit → 提交成功 → 引导浏览 Leaderboard
- Combo Store → 全部 skills 列表 → 链接详情页
