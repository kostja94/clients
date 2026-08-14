# MeDo 双域名 SEO 策略：medo.dev + miaoda.io 并行运营方案

> **本文档职责**：medo.dev 收录崩溃后，新增 miaoda.io 新域名的双站并行 SEO 策略，包括 `sameAs` 结构化数据声明、风险分析、内容差异化与分阶段执行。  
> **来源**：2026-06-30 策略讨论 + 网络调研  
> **状态**：草案

**Last updated**: 2026-06-30 | 模式：双域名并行期

---

## 互链表

| 文档 | 链接 | 关联点 |
|------|------|--------|
| 主文档 | [medo.md](../medo.md) | 产品定位、ICP、品牌信息 |
| Schema 实施 | [medo-schema-spec.md](./medo-schema-spec.md) | Organization.sameAs 字段位置、JSON-LD 模板 |
| 收录诊断 | [medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md) | medo.dev 收录崩溃根因与时间线 |
| 网站结构 | [medo-site-structure.md](../medo-site-structure.md) | URL IA、分阶段落地 |
| 增长策略 | [medo-growth-strategy.md](./medo-growth-strategy.md) | 内容战役、SEO 方向 D |
| 关键词 | [medo-keywords.md](../medo-keywords.md) | 关键词矩阵与目标页 |

---

## 一、背景与决策

### 1.1 现状

| 维度 | medo.dev | miaoda.io |
|------|----------|-----------|
| 状态 | Google 收录崩溃（6,444 → 2 页），根因批量 `/apps/*` 薄内容被拒索引 | **新域名，无历史包袱，需从零做 SEO** |
| GSC 已索引 | 2 页（截至 2026-06-05） | 0（新站） |
| 品牌曝光 | 97% 品牌词搜索（medo / medo ai），自然流量不依赖 SEO 收录 | 尚未建立 |
| 内容 | Ghost Blog 26 篇 + SPA App 广场 | 待建设 |
| 产品功能 | 不变 — 两站均可正常使用 | 同左 |
| 运营策略 | 维持现有品牌流量、Blog 内容更新 | 独立内容策略、SEO 冷启动 |

### 1.2 核心决策

- **两个域名都继续运营**，不做 301 重定向
- `medo.dev`：保留品牌流量承接 + Blog 内容阵地
- `miaoda.io`：独立内容营销阵地，从头构建 SEO 权重
- 通过 Schema `sameAs` 声明两站为同一实体

---

## 二、sameAs 结构化数据声明

### 2.1 字段说明

`sameAs` 是 Schema.org 中 `Thing` 类型的属性。在 Organization schema 的 `sameAs` 数组中声明多个 URL，告诉 Google 这些 URL 指向**同一实体**。

### 2.2 当前 schema（medo-schema-spec.md 附录 A）

当前 `medo.dev` 的 Organization schema 中 `sameAs` 仅含：

```json
"sameAs": [
  "https://www.producthunt.com/products/medo",
  "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"
]
```

**缺失**：未声明 `miaoda.io`。

### 2.3 修正方案（两个站点都要加）

#### medo.dev 端（附录 A 更新）

```json
"sameAs": [
  "https://www.producthunt.com/products/medo",
  "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en",
  "https://miaoda.io/"
]
```

#### miaoda.io 端（新增 Organization schema）

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://miaoda.io/#organization",
  "name": "MeDo",
  "legalName": "Sailai Private Limited",
  "url": "https://miaoda.io/",
  "inLanguage": "en-US",
  "logo": {
    "@type": "ImageObject",
    "url": "https://s3-us-east-2.amazonaws.com/miaoda-cms-ghost-resource/2026/03/favicon.png",
    "width": 512,
    "height": 512
  },
  "sameAs": [
    "https://medo.dev/",
    "https://www.producthunt.com/products/medo",
    "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "Admin@medo.dev",
    "contactType": "customer support"
  }
}
```

> **注意**：`miaoda.io` 的 Organization `@id` 和 `url` 字段使用 `https://miaoda.io/`，但 `sameAs` 中互指对方域名。

### 2.4 实施位置

| 站点 | 位置 | 说明 |
|------|------|------|
| medo.dev | 根 layout / 首页注入 | 对齐 [medo-schema-spec.md §4.1](./medo-schema-spec.md) |
| miaoda.io | 首页 `<head>` JSON-LD | 新站首次部署 |

---

## 三、传染性风险分析

### 3.1 核心问题

> `sameAs` 声明会把 medo.dev 的 penalty 传染给 miaoda.io 吗？

### 3.2 网络调研结论

| 来源 | 关键结论 |
|------|---------|
| **Google John Mueller 表态**（[seroundtable.com](https://www.seroundtable.com/google-penalty-site-move-18163.html)） | 如果你把被罚站点内容搬到一个新域名（即使没有 301 重定向、没用 GSC 迁移工具），Google 可能会自己识别出"站点搬家"，把 penalty 跟过去 |
| **Semantic Mastery**（[实战经验](https://semanticmastery.com/avoid-seo-penalties-when-changing-domains/)） | 多次实操：换域名 + 301 重定向**没有自动传递 penalty**；但 GSC Change of Address 工具情况未测试（不清楚是否会传 penalty） |
| **Google 官方 FAQ**（[site reputation abuse 政策](https://developers.google.com/search/blog/2024/11/site-reputation-abuse)） | 把被手动处罚的内容搬到新域名：如果新域名无历史声誉且遵守 spam 政策，"far less likely to be an issue" |
| **MetricSpot**（[sameAs 分析](https://metricspot.com/docs/sameas-profile-match/)） | `sameAs` 本身不会造成惩罚传染 —— 最坏情况只是知识图谱归属失败 |
| **AuthorityStack.ai**（[Schema 惩罚分析](https://authoritystack.ai/blog/can-you-get-a-google-penalty-for-incorrect-schema-markup)） | 结构化数据只在涉及**欺骗性行为**时才会被手动处罚，`sameAs` 声明不在惩罚范围内 |

### 3.3 综合判断

| 问题 | 答案 |
|------|------|
| `sameAs` 字段会传染 penalty 吗？ | **不会** — 多个权威来源证实 |
| 什么会传染 penalty？ | **内容重复** — 谷歌通过内容指纹匹配识别站点迁移 |
| 现在可以加 `sameAs` 吗？ | **可以** — 但前提是新站内容独立创作 |
| 最优策略？ | `sameAs` 现在加，但新站内容必须大幅差异化 |

### 3.4 传染路径对比

```
✅ 安全路径：
   medo.dev ──sameAs──► miaoda.io   ← 仅结构化数据声明，不传 penalty
   miaoda.io 独立内容（非复制）      ← 谷歌不会识别为站点搬家

❌ 风险路径：
   medo.dev 内容 ──复制──► miaoda.io ← 谷歌通过内容指纹识别搬家
   + sameAs                          ← 无关——内容重复才是问题源头
```

---

## 四、双站内容差异化策略

### 4.1 核心原则

**miaoda.io 的内容必须 100% 独立创作，不能从 medo.dev 复制任何文章。**

### 4.2 内容定位分工

| 维度 | medo.dev | miaoda.io |
|------|----------|-----------|
| **定位** | 产品门户 + 品牌流量承接 | SEO 内容营销阵地 |
| **主内容类型** | Blog（产品教程、案例、Hackathon） | 深度 SEO 长文（关键词拦截） |
| **关键词策略** | 品牌词 + 产品教程词 | 商业意图词（ai app builder pricing, lovable alternative 等） |
| **目标受众** | 已有品牌认知的用户 | 搜索发现阶段的新用户 |
| **内容风格** | 产品导向、实操教程 | 行业分析、对比评测、综合指南 |
| **域名价值** | 品牌资产 | SEO 获客引擎 |

### 4.3 具体操作

| 规则 | 说明 |
|------|------|
| **禁止直接复制** | 任何 medo.dev 已有文章不得直接搬运到 miaoda.io |
| **主题可重叠，角度必须不同** | 例如"AI app builder 对比"在两个站都可以写，但结构、案例、数据、表达完全不同 |
| **优先覆盖不同关键词** | medo.dev 做品牌词 + 教程长尾；miaoda.io 做商业对比词 + 品类词 |
| **内链隔离** | miaoda.io 的内链体系独立建设，不引用 medo.dev 的 URL |
| **canonical 各自独立** | 两站各自声明自己的 canonical，互不指向对方 |

### 4.4 内容日历建议（miaoda.io 首月）

| 周次 | 内容 | 目标关键词 | 类型 |
|------|------|-----------|------|
| W1 | AI App Builder 完全指南 2026 | ai app builder, best ai app builder | 品类指南 |
| W1 | MeDo vs Lovable 深度对比 | medo vs lovable, lovable alternative | 对比评测 |
| W2 | AI App Builder 定价对比（5 家） | ai app builder pricing, cheapest ai app builder | 对比分析 |
| W2 | 不懂代码如何做 SaaS MVP（2026） | build SaaS without coding, no-code SaaS | 实操指南 |
| W3 | Bolt.new 替代方案全景对比 | bolt.new alternative, bolt vs lovable | 对比评测 |
| W3 | AI 建站工具选型指南 | AI website builder, best AI website builder | 品类指南 |
| W4 | 从零到发布：用 AI 做全栈应用 | build full stack app with AI | 实操教程 |
| W4 | Vibe Coding 入门完全手册 | vibe coding, what is vibe coding | 概念科普 |

> 以上内容与 medo.dev 现有 Blog **主题不直接重叠**，且角度以行业分析/对比为主，区别于 medo.dev 的产品教程导向。

---

## 五、分阶段执行计划

### Phase 0 — 即刻（1–3 天）

| # | 任务 | 站点 | 关联 |
|---|------|------|------|
| 1 | medo.dev Organization schema 的 `sameAs` 追加 `https://miaoda.io/` | medo.dev | [medo-schema-spec.md 附录 A](./medo-schema-spec.md) |
| 2 | miaoda.io 首页部署 Organization + WebSite JSON-LD（含 `sameAs` 互指） | miaoda.io | 本文档 §2.3 |
| 3 | miaoda.io 配置 GSC + 提交站点地图 | miaoda.io | 新站标准流程 |
| 4 | miaoda.io 首页上线基础品牌信息 | miaoda.io | 对齐 [medo.md §1](../medo.md) 产品摘要 |

### Phase 1 — 基础建设（1–2 周）

| # | 任务 | 说明 |
|---|------|------|
| 1 | miaoda.io 部署 Blog（Ghost 或静态） | 新内容发布平台 |
| 2 | miaoda.io 发布首篇内容（品类指南） | 建立初始内容信号 |
| 3 | miaoda.io 补充 `/pricing` 静态页 | 承接商业词 |
| 4 | 两站 `sameAs` 通过 Rich Results Test 验收 | 工具：[validator.schema.org](https://validator.schema.org/) |
| 5 | medo.dev Blog 保持正常更新 | 不因新站减量 |

### Phase 2 — 内容放量（1–3 个月）

| # | 任务 | 频率 |
|---|------|------|
| 1 | miaoda.io Blog 持续发布 SEO 长文 | 每周 1–2 篇 |
| 2 | miaoda.io 补充 `/vs/*` 对比页矩阵 | 每月 2–3 篇 |
| 3 | 监控 GSC 两站收录与排名趋势 | 每周 |
| 4 | medo.dev 核心修复推进（noindex /apps/*、SSR 营销页） | 对齐 [medo-indexing-diagnosis.md §六](./medo-indexing-diagnosis.md) |

### Phase 3 — 交叉联动（3–6 个月后）

| # | 任务 | 说明 |
|---|------|------|
| 1 | 评估 miaoda.io 是否已建立独立搜索引擎信任 | GSC 表现分析 |
| 2 | 若 miaoda.io 排名稳定，可考虑弱化交叉引用限制 | 在 About 页提及双站关系 |
| 3 | 评估是否将主营销重心逐步切到 miaoda.io | 长期决策 |
| 4 | medo.dev 保留品牌门户 + 产品功能 | 不做域名废弃 |

---

## 六、GSC 与监控

### 6.1 两个站点独立管理

| 项目 | medo.dev | miaoda.io |
|------|----------|-----------|
| GSC Property | 现有（已验证） | 新建（需验证） |
| Sitemap | 止血期 < 100 URL | 新建 |
| 收录监控 | 关注 indexed 从 2 回升 | 从 0 开始追踪 |
| 关键词追踪 | 品牌词 + 现有可见词 | SEO 目标词 |

### 6.2 监控项（每周）

| 指标 | medo.dev | miaoda.io | 警戒线 |
|------|----------|-----------|--------|
| GSC 已索引 | 目标 > 50（止血后） | 目标逐月增长 | — |
| 品牌词排名 | 保持前 3 | 期望出现 | 跌出前 5 |
| 商业词曝光 | 3%（现状） | 目标 > 10% | — |
| sameAs 验证 | ✓ Rich Results 无 error | ✓ 同上 | 出现 error |
| 手动操作 | 无 | 无 | 出现通知立即排查 |

---

## 七、与现有文档联动

| 本文要求 | 需更新的文档 | 操作 |
|---------|------------|------|
| Organization `sameAs` 追加 `miaoda.io` | [medo-schema-spec.md](./medo-schema-spec.md) 附录 A | 新增一行 `"https://miaoda.io/"` |
| 项目常量 `same_as` 追加 | [medo-schema-spec.md](./medo-schema-spec.md) Part II §A | yaml `same_as` 数组追加 |
| 代理执行手册中的 sameAs | [medo-schema-spec.md](./medo-schema-spec.md) Part II | 更新常量后自动生效 |
| 主文档客户概览 | [medo.md](../medo.md) §1 | 新增 `网站` 行：`miaoda.io` |
| 增长策略 | [medo-growth-strategy.md](./medo-growth-strategy.md) | 方向 D 追加双域名 SEO 战役 |

---

## 八、禁止事项

```yaml
forbidden:
  - medo.dev 内容复制到 miaoda.io
  - miaoda.io 页面 canonical 指向 medo.dev
  - 放弃 medo.dev 的 Blog 更新（需保持活跃）
  - miaoda.io 使用 medo.dev 的子域名
  - 两站内容完全相同仅供翻译
  - 相同文章两站同时发布（spinning）
```

---

## 九、FAQ（内部）

| 问题 | 回答 |
|------|------|
| **为什么不做 301？** | medo.dev 仍有品牌搜索流量和产品功能，直接重定向会丢失品牌资产 |
| **sameAs 现在加真的安全吗？** | 是。sameAs 只声明实体归属，不传 penalty。真正的风险来自内容重复，而非结构化数据 |
| **两站内容会不会被谷歌判定为重复？** | 只要严格遵循 §4 差异化策略，不会。相同产品有多个域名的内容站点在 Google 规则下是正常可接受的 |
| **多久能看到 miaoda.io 有排名？** | 通常新域名 3–6 个月才能获得稳定排名。Phase 1–2 是打基础阶段 |
| **medo.dev 的 penalty 会自己恢复吗？** | 需要主动修复（见 [medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md)），不会自动恢复 |

---

## 附录 A：miaoda.io 首页最小 JSON-LD

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://miaoda.io/#organization",
      "name": "MeDo",
      "legalName": "Sailai Private Limited",
      "url": "https://miaoda.io/",
      "inLanguage": "en-US",
      "logo": {
        "@type": "ImageObject",
        "url": "https://s3-us-east-2.amazonaws.com/miaoda-cms-ghost-resource/2026/03/favicon.png",
        "width": 512,
        "height": 512
      },
      "sameAs": [
        "https://medo.dev/",
        "https://www.producthunt.com/products/medo",
        "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "email": "Admin@medo.dev",
        "contactType": "customer support"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://miaoda.io/#website",
      "url": "https://miaoda.io/",
      "name": "MeDo",
      "inLanguage": "en-US",
      "description": "Build full-stack apps with a no-code AI platform — frontend, backend, database, and integrations in minutes.",
      "publisher": { "@id": "https://miaoda.io/#organization" }
    }
  ]
}
```

---

*策略制定：2026-06-30 | 参与：[medo-schema-spec.md](./medo-schema-spec.md) | [medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md) | 网络调研*
