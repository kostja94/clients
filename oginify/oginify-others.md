# Oginify 杂项汇编

> **本文档职责**：成本拆解、定价依据、待办、调研 Backlog、运营日志索引。  
> **引用**：[主文档](./oginify.md) 概览 | [features](./oginify-features.md) Generator 技术管线 | [site-structure](./oginify-site-structure.md) 技术栈

---

## 定价依据

> **定价主轴**：Oginify 面向互联网尺度的 1200×630 可视化资产需求——**市场足够大**；单个用户用量**两极分化**（小量级 vs 大量级），故定价须分层覆盖长尾与头部，而非用「低频 / 高频」描述市场本身。

### 当前口径（线上 v1 · 已上线）

| 维度 | 说明 |
|------|------|
| **SaaS 免费额度** | 匿名用户 **6 张/天**（`src/lib/quota.server.ts`）；All tools、Validator、Gallery、Templates 等工具页不受此限 |
| **付费版** | 已接入支付（MoR 托管结账） |
| **状态** | v1 过渡结构；v2 五层目标见下文 |

### 需求规模与用量模型（定价前提）

**TAM 层面——需求大：**

- **页面基数**：全球网站数以亿计，每站多 URL；pSEO / 内容站单站可达数百至数千页
- **建站加速**：Vibe Coding 降低建站门槛，新站、新页、改版上线频率上升
- **单页多次刷新**：同一 URL 可随季节、活动、campaign、A/B 测试、改版换不同预览图
- **管线复用**：同一生成管线输出 1200×630，可覆盖 OG、Featured Image、部分横版展示广告等（详见 [by-image-size.md](./use-cases/by-image-size.md)）

需求在 **页面数 × 刷新次数 × 用途** 上放大。

**用户层面——用量两极分化：**

| 用户类型 | 典型月用量 | 举例 | 目标档位 |
|----------|-----------|------|----------|
| **小量级** | 1–20 张 | 个人站、新产品几页、偶发 campaign | Free → PAYG |
| **中量级** | 50–300 张 | 内容站、小型 SaaS、SEO 团队 | Pro / Studio 订阅 |
| **大量级** | 500–10000+ 张 | pSEO 规模化站点、Agency 多客户、CMS / 平台集成 | **Enterprise / API** |

同一管线、同一规格，用量可差**三个数量级**——这正是 Enterprise 与 API 存在的理由，而非「市场小所以不做订阅」。

### 线上定价方案（v1 · 当前）

| 方案 | 定价 | 含图数 | 支付手续费（约 4.5% + $0.30/笔） | 净营收 | 角色 |
|---|---|---|---|---|---|
| PAYG 单次 | $0.99 | 2 张 + 6 次 regenerate 上限 | $0.345 | $0.645 | 冲动入口（过渡） |
| Bundle 10 | $7.90 | 10 张 | $0.656 | $7.244 | 过渡 |
| Bundle 50 | $29.00 | 50 张 | $1.605 | $27.395 | 过渡 |

v1 为支付接入后的**过渡结构**：验证付费意愿、在 MoR 手续费结构下跑通 unit economics。**不是因为总市场需求低**；大量级用户当前无转化路径，是 v2 优先补齐项。

### 目标定价结构（v2 · 规划）

```
小量级          中量级              大量级
  │               │                    │
Free → PAYG → Pro 订阅 → Studio → Enterprise / API
试用   冲动入口   主推（高亮）  升级档    头部（mailto / 第五卡）
```

| 档位 | 目标用户 | 配额 | 规划定价 | 唯一职责 |
|------|----------|------|----------|----------|
| **Free** | 试用 | 6 张/天 | $0 | 试出价值，非长期替代 |
| **PAYG** | 小量级、一次性 | 2 张 + 6 Regenerate | **$2.90**（自 v1 $0.99 上调） | 冲动入口 + 定价锚；不比订阅划算 |
| **Pro** | 中量级站长、SEOer | **100 张/月** | **$19/月** · **$149/年** | **主推档**（Pricing 视觉高亮） |
| **Studio** | 重度用户、小 Agency | **300 张/月** | **$29/月** · **$229/年** | Pro 超额留存；+$10、配额 ×3 |
| **Enterprise / API** | pSEO 站、CMS、平台 | 定制 / 按量 / SLA | Contact | sitemap 批量、Webhook、自动写回 `og:image` |

**叙事链（playbook 校验）：**

```
PAYG $2.90 × 6.5 ≈ Pro $19
Pro $19 + $10 = Studio $29
$19 × 12 × 0.65 ≈ $149/年（档档统一 65 折）
```

**Enterprise / API 与 Skills 边界：**

| | social-cards-skills | Enterprise / API |
|---|---|---|
| 用户 | 单个开发者、Agent | 平台、Agency、规模化站点 |
| 交付 | 自托管、MIT 免费 | 托管批量、sitemap / Webhook、SLA |
| 角色 | 开发者入口与 GEO | 大量级商业化 |

Skills 是开发者触达；API / Enterprise 是「不想自运维的规模化需求」——人群不重叠。

**Bundle 处置（v1 → v2）：** Bundle 10/50 在 Pro 上线后标记 Legacy 并下线，避免稀释主推档。

### 支付手续费与 SKU 结构

| SKU 单价 | 通道扣费（约） | 净收 | 通道占定价 |
|---|---:|---:|---:|
| $0.99 | $0.345 | $0.645 | **35%** |
| $2.90 | $0.431 | $2.469 | 15% |
| $7.90 | $0.656 | $7.244 | 8% |
| $19.00 | $1.155 | $17.845 | 6% |

**结论**：v1 的 $0.99 PAYG 通道占比过高，仅宜作首发冲动价；v2 PAYG 地板 **$2.90**；订阅档通道占比 ≤6%，适合作为主推。

### 实施路线图

| 阶段 | 时间 | 动作 |
|------|------|------|
| **Phase 0** | 现在 | 统一叙事（TAM 大 + 用量两极）；Pricing Footer 加 Enterprise mailto |
| **Phase 1** | 1–4 周 | PAYG → $2.90；上线 Pro $19/月；Regenerate 硬上限 + Turnstile；D3 邮件 PAYG→Pro |
| **Phase 2** | 1–3 月 | 上线 Studio $29/月；年付默认 ON；Bundle 下线；`ai_usage_log` 校准配额 |
| **Phase 3** | 有 inbound 后 | Enterprise 页；API 文档；sitemap 批量 MVP（≥3 次 Enterprise 入站后第五卡） |

### 免费额度说明

- **6 张/天** 是单桶模型无关配额（`src/lib/quota.server.ts`）
- Regenerate 只扣 1 张图额度，AI 成本 $0.030/$0.024 一次
- 切换模板 / 截图换图：**不调用 AI**，$0

### Skills 与 SaaS 的边界

| | Oginify SaaS | social-cards-skills |
|---|---|---|
| 收费 | 6 张/天免费 → PAYG/Bundle 付费 | MIT 永久免费 |
| 用户 | 站长、SEOer、营销人 | 开发者、Agent 用户 |
| 基础设施 | 托管，零配置 | 自部署，自带模型 |

---

## 成本拆解

### 主流程成本（用户粘贴 URL → 生成 2 张图）

| 环节 | 调用 | 单个成本 | 备注 |
|------|------|----------|------|
| Firecrawl 抓取 | ~3 次 scrape | ~$0.003–0.005 | 轻度抓取，无 JSON extract |
| 截图（第 1 张） | Firecrawl 首屏 → 裁切 1200×630 | $0 | 非 AI |
| 模板渲染（第 2 张） | Next.js + Satori/resvg | $0 | 非 AI |
| **合计** | | **≈ $0.005** | |

### AI Regenerate 成本（用户手动补生成 1 张）

| 环节 | 调用 | 单个成本 | 备注 |
|------|------|----------|------|
| Firecrawl 抓取 | `v2/scrape` + JSON extract | ~$0.005 | 5 credits |
| LLM 内容理解 (aiBrief) | Gemini 3 Flash Preview | ~$0.002 | |
| 图像生成 — Fast | `google/gemini-3.1-flash-image-preview` | **$0.030** | Lovable AI Gateway 转售价 |
| 图像生成 — Precise | `openai/gpt-image-2` (quality=low) | **$0.024** | |
| **合计 (Fast)** | | **≈ $0.037** | |
| **合计 (Precise)** | | **≈ $0.031** | |

> **来源**: AI 单价 `src/lib/og-model.server.ts`；链路调用 `src/routes/index.tsx`。以上为 Lovable AI Gateway 转售价，非 Google/OpenAI 原厂价。

### 固定成本

| 项目 | 金额 |
|------|------|
| 域名 | $11.10（一次性） |
| 主流程单次生成 | ~$0.005 |
| AI Regenerate (Fast) | ~$0.037 |
| AI Regenerate (Precise) | ~$0.031 |

### 模型价格（AI Regenerate 路径）

| 模型 | API ID | 单价/张 | 状态 |
|------|--------|---------|------|
| Fast (Gemini) | `google/gemini-3.1-flash-image-preview` | **$0.030** | 默认（Lovable AI Gateway 转售价） |
| Precise (GPT) | `openai/gpt-image-2` (quality=low) | **$0.024** | 可选 |

### Firecrawl 成本（Regenerate 路径）

| 方案 | 月费 | 5 credits 价 |
|------|------|-------------|
| Hobby | $19 | $0.032 |
| Standard | $99 | $0.005 |

JSON extract 是 **5 credits/次**。若 native `fetch-meta` 已拿到足够 meta，可跳过 Firecrawl 的 JSON extract。

### 降本路径（Regenerate 路径）

**路径 A：减少 AI 生成张数**（已实施——主流程不调用 AI，仅 Regenerate 使用）

**路径 B：换模型**

| 策略 | 成本/张 | 总成本（含 Firecrawl + aiBrief） |
|------|---------|--------------------------------|
| Fast (Gemini NB2) | $0.030 | ~$0.037 |
| Precise (GPT Image 2) | $0.024 | ~$0.031 |

**路径 C：Firecrawl 短路** — 跳过 JSON extract。

### 成本敏感度

| 变量 | 当前值 | 波动影响 |
|------|--------|----------|
| Gateway 转售价浮动 | ±20% | 最大杠杆（Lovable AI Gateway） |
| Regenerate 频率 | 用户行为依赖 | 每张 AI 图 ≈ $0.030–0.037 |
| Firecrawl 套餐 | Hobby → Standard | $0.032 → $0.005/次 |

---

## 待办

- [x] 接入 Clink 支付全流程
- [ ] Phase 1 定价：PAYG $2.90 + Pro $19/月上线
- [ ] Pricing 页 Enterprise mailto + v2 档位视觉
- [ ] D3 邮件 PAYG → Pro 转化叙事
- [ ] 给 PAYG 加 6 次 regenerate 上限
- [ ] 给免费入口接 Turnstile 验证码
- [ ] 实施方案 C：建 `ai_usage_log` 表 + 埋点
- [ ] 确认 Firecrawl 当前套餐（Hobby vs Standard）
- [ ] 方案 A 实测一次，把 $0.030 / $0.024 锁成实测值
- [x] Above the Fold 首屏截图功能（已整合入 Generator）
- [ ] Platforms with Built-in OG 页面
- [ ] Gallery / Validator / Websites Without 的 SEO 内容分发
- [ ] Websites Without 清单扩充至 30–40 个站点
- [ ] 线上 Pricing / Changelog 文案与文档口径对齐
- [ ] Footer 404 链接（Amazon Sponsored Display 等）待建或移除
- [ ] 中文版 `/zh` 恢复（已暂时下线）

---

## 调研 Backlog

| ID | 引出文档/条目 | 需查证 | 优先级 | 计划来源 | 状态 |
|----|-------------|--------|--------|----------|------|
| R1 | Gallery 约 100 条 | 后台实际条目数 | P1 | 后台数据 | 待验证 |
| R2 | 付费价格 | v1 已上线；v2 目标 Pro $19 / Studio $29 / PAYG $2.90 | P0 | 支付已接入 | v1 锁定，v2 规划 |
| R7 | Enterprise / API | ≥3 次 inbound 后第五卡 + sitemap 批量 MVP | P1 | 产品决策 | 规划 |
| R3 | 匿名配额 | 代码 quota.server.ts: **6 张/天/用户** | P1 | 代码 | 以代码为准 |
| R4 | Footer 404 | Amazon Sponsored Display / Responsive Display Ads 是否规划 | P2 | 站点 IA | 待确认 |
| R5 | 中文版 `/zh` | 恢复时间与 hreflang 策略 | P2 | 产品决策 | 已暂时下线 |
| R6 | [by-style.md](./use-cases/by-style.md) 优先扩展四风格 | Text Overlay / Cinematic / Collage / Risograph 实现顺序与 social-cards-skills 对齐 | P1 | 风格调研 | 文档已录入，待实现 |

---

## 运营日志索引

| 文档 | 用途 |
|------|------|
| [oginify-CHANGELOG.md](./oginify-CHANGELOG.md) | 版本变更记录 |
| [oginify-build-in-public.md](./oginify-build-in-public.md) | Build in Public 每日日志 |

---

*Last updated: 2026-06-03. v1 线上价见「线上定价方案」；v2 目标结构与路线图见「目标定价结构」。*
