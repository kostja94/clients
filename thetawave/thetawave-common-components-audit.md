# ThetaWave 通用组件审计 — FAQ & Final CTA（线上实测）

> **本文档职责**：基于 [thetawave.ai](https://thetawave.ai/) **线上 HTML 实测**，审计全站 FAQ 与 Final CTA 的现状，为统一组件与样式提供依据。  
> **数据来源**：`thetawave.ai/sitemap.xml` + **297** URL 线上 HTML 解析（2026-06-24；**272** 成功 / **25** 失败）。原始 JSON 快照已删除；结论与表格见本文。  
> **页面清单**：与 [thetawave-site-structure.md](./thetawave-site-structure.md)（2026-06-24）对齐  
> **不含**：本地草稿、规划文档、archive spec、sitemap 404 页

**Last updated**: 2026-06-24

---

## 一、执行摘要

### 1.1 总体结论：**营销详情页 FAQ+CTA 已统一；Comparison FAQ 标题、Hub/KH 仍是分叉**

| 维度 | 2026-06-24 抽检结论 |
|------|---------------------|
| **是否全站同一套？** | **否**。Feature / Use Case / Study / Blog **详情** = F1 + C1；Comparison 详情 = **F3 FAQ + C1 CTA**；Hub / KH / Legal 多数无组件 |
| **FAQ** | 营销详情 **65/65** 有 FAQ（Feature/Use Case/Study/Blog = **F1**；Comparison = **F3** 页专属 H2） |
| **Final CTA** | 营销详情 **65/65** 有 C1 统一壳（3 badges + Open App）；较 6/22 **Comparison 已从 C3 升级为 C1** |
| **Blog** | **7/7** 线上详情均为 F1 + C1（非此前仅 1 篇） |
| **Pricing** | 已升级为 **F1 + C1**（6/22 为 F2 + C2） |
| **Knowledge Hub** | 抽检 **191** 内容页 + 首页：**0** FAQ · **0** FinalCTA |
| **Sitemap 404** | 10 条 marketing path + 14 条 KH `IncompleteRead`（抓取失败，非 404） |

### 1.2 同一套组件？——按页面 tier

| Tier | 页面 | FAQ | Final CTA | 与 F1/C1 一致？ |
|------|------|-----|-----------|----------------|
| **A** | Feature / Use Case / Study / Blog **详情** | F1 | C1 | ✅ **是**（54 页） |
| **B** | Comparison **详情** + 索引 | F3 | C1 | ⚠️ **CTA 同套；FAQ 标题不同**（12 页） |
| **C** | `/pricing` | F1 | C1 | ✅ 是 |
| **C′** | `/study` 聚合 | — | C1 | ⚠️ 仅 CTA |
| **C″** | `/download` | F1 | C3 | ⚠️ 有 badges 但无 Open App 信号 |
| **D** | 首页、Explore、Changelog、Legal、Feature/Use Case/Blog 聚合、KH | — | — | ❌ 否 |
| **E** | `/thetawave-vs-chatgpt`（遗留） | other | none | ❌ 旧版，待废弃 |
| **E′** | `/creator-program` | F2 `<details>` | none | ❌ 运营页独立实现 |
| **E″** | `/chrome-extension` | 弱 F1 信号 | none | ❌ 仅 FAQ 壳 |

### 1.3 覆盖率（272 页成功，不含 KH 内容 191 页）

| 指标 | 非 KH 页面（80） | 营销详情（65） |
|------|-----------------|---------------|
| **有 FAQ** | 70/80（88%） | **65/65（100%）** |
| **C1 统一壳（3 badges）** | 68/80（85%） | **65/65（100%）** |
| **FAQ+CTA 均与 Tier A 一致** | — | **54/65（83%）**（Comparison 12 页为 F3+C1） |

> KH 191 页占 sitemap 可访问主体积，均无 FAQ/FinalCTA；若计入全站，组件统一率显著低于营销详情页。

---

## 二、审计方法（线上实测）

### 2.1 数据获取

| 步骤 | 说明 |
|------|------|
| Sitemap | 抓取 `https://thetawave.ai/sitemap.xml`；KH 使用带 `?id=` 的 canonical URL |
| HTML | **297** URL：82 path 营销页 + 205 KH canonical + sitemap 404 抽检 |
| 解析 | Radix accordion、`<details>`、H2/H3、FAQPage JSON-LD、3 trust badges、`Open App` |
| 原始数据 | 已删除（2026-07-28）；汇总见本文 §三–§五 |

### 2.2 抽检范围

| 类型 | 策略 | URL 数 | 成功 |
|------|------|--------|------|
| Feature | 详情全量 | 16 | 16 |
| Use Case | 详情全量（含 ⚠️ `for-graduate-students`） | 18 | 18 |
| Study | 聚合 + 详情全量 | 14 | 14 |
| Comparison | 详情 + 索引 + 遗留 | 14 | 13（1×IncompleteRead） |
| Blog | 索引 + 线上 7 篇 + sitemap 404 | 16 | 8 |
| Knowledge Hub | canonical 全量 | 205 | 191（14×IncompleteRead） |
| Hub / 静态 | 全量 | 15 | 15 |
| Legal | 全量 | 2 | 2 |
| **合计** | | **297** | **272** |

### 2.3 检测信号

| 组件 | 统一壳（F1 / C1） | 变体 |
|------|------------------|------|
| **FAQ** | H2 `Frequently Asked Questions` + subtitle + Radix + FAQPage | F3 Comparison 自定义 H2；F2 `<details>`（creator-program） |
| **FinalCTA** | 3 badges + `Open App` + signup | C3 有 badges 但缺 Open App（download）；none（Hub/KH/Legal） |

**Golden pages（线上参考）**：

- FAQ + Schema：[ai-study-assistant](https://thetawave.ai/feature/ai-study-assistant)  
- Final CTA Persona：[for-pre-med-students](https://thetawave.ai/use-case/for-pre-med-students)  
- Feature 自定义 CTA：[notes-generator](https://thetawave.ai/feature/notes-generator)  
- Blog（唯一 live 详情）：[how-to-turn-past-exam-papers-into-study-notes](https://thetawave.ai/blog/how-to-turn-past-exam-papers-into-study-notes)  
- Comparison（待统一）：[thetawave-vs-chatgpt](https://thetawave.ai/comparison/thetawave-vs-chatgpt)

---

## 三、FAQ 审计

### 3.1 按页面类型（2026-06-24）

| 页面类型 | 抽检 OK | 有 FAQ | FAQ 变体 | C1 统一壳 | 与 Tier A 一致 |
|----------|---------|--------|----------|-----------|---------------|
| **Feature** 详情 | 16 | 16 | F1 | 16 | ✅ |
| **Use Case** 详情 | 18 | 18 | F1 | 18 | ✅ |
| **Study** 详情 | 13 | 13 | F1 | 13 | ✅ |
| **Blog** 详情 | 7 | 7 | F1 | 7 | ✅ |
| **Comparison** 详情 | 11–12 | 11–12 | **F3** | 11–12 | ⚠️ FAQ 不同 |
| **Comparison** 索引 | 1 | 1 | F3 | 1 | ⚠️ |
| **Pricing** | 1 | 1 | F1 | 1 | ✅ |
| **Download** | 1 | 1 | F1 | 0 | ⚠️ C3 |
| **Study** 聚合 | 1 | 0 | — | 1 | ⚠️ 仅 CTA |
| **Creator Program** | 1 | 1 | F2 | 0 | ❌ |
| **Chrome Extension** | 1 | 1* | 弱 F1 | 0 | ❌ |
| **Knowledge Hub** | 191 | 0 | — | 0 | ❌ |
| **首页 / Explore / Legal / 多数 Hub** | 9 | 0 | — | 0 | ❌ |
| **遗留** `/thetawave-vs-chatgpt` | 1 | 1 | other | 0 | ❌ |

\* chrome-extension 有 Radix 但 FAQ 信号弱（无 schema/subtitle）

### 3.2 FAQ 实现变体（4 种，线上检出）

| ID | 名称 | DOM / 行为 | 典型页面 | 实测数量 |
|----|------|-----------|----------|---------|
| **F1** | Radix SiteFAQ | `section` + H2 + subtitle + Radix accordion + `<h3>` | Feature、Use Case、Study 详情、1 篇 Blog | 56 |
| **F2** | Pricing FAQ（`<details>`） | 原生 `<details>`/`<summary>` | `/pricing` | 2 |
| **F3** | Comparison FAQ | 页专属 H2 + Radix accordion + FAQPage | 全部 Comparison 详情 | 6 检出 F3 标题；其余 7 页 H2 为 `{竞品} comparison questions` 等 |
| **F4** | 无 FAQ | — | Explore、Hub 聚合、KH、首页、Blog 404 | — |

**F1 线上示例（notes-generator）**：

- H2：`Frequently Asked Questions`  
- Subtitle：`Everything you need to know about ai-powered notes generator.`  
- Accordion：Radix  
- Schema：`FAQPage` JSON-LD ✅  

**F3 线上示例（vs-chatgpt）**：

- H2：`Questions, answered`  
- Schema 题示例：`Is ThetaWave better than ChatGPT for notes?`  
- 无标准 subtitle  

**F3 变体示例（vs-anki）**：H2 为 `Anki comparison questions`（非 `Questions, answered`）

### 3.3 FAQ 不一致清单（剩余）

| 问题 | 影响 | 建议 |
|------|------|------|
| Comparison 非标准 H2（F3） | 12 详情 + 索引 | 保留 override 或统一 subtitle |
| Creator Program 用 F2 | 1 页 | 换 F1 或明确为运营页例外 |
| 遗留 `/thetawave-vs-chatgpt` | 1 页 | 301 至 `/comparison/…` 并下线 |
| KH 无 FAQ | 191 页 | 独立内容策略 |
| 聚合 Hub 无 FAQ | `/feature`、`/use-cases`、`/blog` 等 | 低优先级 |

### 3.4 缺失 FAQ 的页面（优先级）

| 优先级 | 页面 | 理由 |
|--------|------|------|
| P1 | Comparison（已有 FAQ，需 **标准化 H2/subtitle**） | 高转化，内容已有 |
| P2 | Blog 404 详情（8 篇） | sitemap 与路由不一致 |
| P3 | `/pricing`（F2 → F1） | 定价异议集中 |
| P4 | Knowledge Hub（可选） | 体量大，需独立策略 |
| P5 | 聚合 Hub（`/feature`、`/use-cases`） | 低优先级 |

---

## 四、Final CTA 审计

### 4.1 按页面类型（2026-06-24）

| 页面类型 | 抽检 OK | C1 统一壳 | 主要变体 | 较 6/22 变化 |
|----------|---------|-----------|----------|-------------|
| **Feature** 详情 | 16 | **16（100%）** | C1 | — |
| **Use Case** 详情 | 18 | **18（100%）** | C1 | +1（`for-graduate-students`） |
| **Study** 详情 | 13 | **13（100%）** | C1 | — |
| **Blog** 详情 | 7 | **7（100%）** | C1 | **+6 篇新稿已接入** |
| **Comparison** 详情 | 11–12 | **11–12（100%）** | C1 | **✅ 已从 C3 升级** |
| **Pricing** | 1 | **1** | C1 | **✅ 已从 C2 升级** |
| **Download** | 1 | 0 | C3 | 有 badges，缺 Open App |
| **Study** 聚合 | 1 | 1 | C1 | — |
| **Comparison** 索引 | 1 | 1 | C1 | **新增 C1** |
| **Knowledge Hub** | 191 | 0 | — | — |
| **首页 / Explore / Legal** | 4 | 0 | Hero / none | — |
| **Creator / Legacy** | 2 | 0 | none | — |

### 4.2 Final CTA 实现变体（2026-06-24 检出）

| ID | 名称 | 结构 | 实测数量 | 典型页面 |
|----|------|------|---------|----------|
| **C1** | FinalCTA 统一壳 | headline + subheadline + 3 badges + Open App + signup | **68**（非 KH） | Feature / Use Case / Study / Blog / **Comparison** / pricing |
| **C3** | 半统一 | 3 badges，缺 Open App | 1 | `/download` |
| **C2** | 简版 | `Ready to study smarter?` | **0** | *6/22 有；6/24 已清零* |
| **none** | 无壳 | — | Hub / KH / Legal / creator / legacy | — |

> **6/22 → 6/24 最大变化**：Comparison 12 详情 **已全部接入 C1**；Pricing **F2/C2 → F1/C1**。

**C1 线上结构（notes-generator）**：

```
Headline:  Start Generating Notes in Seconds
Subhead:   Join 300,000+ students who use Thetawave AI to generate study notes…
Badges:    Free to Start · No Credit Card Required · Results in Under 2 Minutes
Primary:   Generate Notes Free  → /auth/signup
Secondary: Open App             → /app
```

**C3 Comparison（vs-anki，线上实测）**：

```
H2:        Create the study kit first.
（无三 badge 行；有 signup 链但结构不同于 C1）
```

**C2 Comparison（vs-chatgpt，线上实测）**：

```
H2:        Ready to study smarter?
Subcopy:   Join 300,000+ students who switched from ChatGPT…
Button:    Start Free（无三 badge 行）
```

### 4.3 线上观察：FinalCTA 文案差异

| 观察 | 详情 |
|------|------|
| Feature 页专属 headline 为主 | 16/16 详情页用页专属 headline；仅 `ai-study-assistant` 接近默认句式 |
| trust_badges 顺序 | 有 C1 的页面三 badge 文案一致 |
| Comparison 无统一壳 | 12/12 详情页均无 `Free to Start` 三 badge |
| Blog live 文 | 已接入 C1，废弃旧式 `Try Thetawave on your own materials` |

### 4.4 仍未接入 C1 的页面

| 优先级 | 页面 | 现状 |
|--------|------|------|
| **P1** | `/download` | F1 FAQ + C3（缺 Open App） |
| **P1** | `/thetawave-vs-chatgpt` | 遗留路径，无 C1 |
| **P2** | `/creator-program` | F2 FAQ，无 FinalCTA |
| **P2** | `/chrome-extension` | 弱 FAQ，无 CTA |
| **P3** | Knowledge Hub（191 页） | 无 FAQ / CTA |
| **P4** | 首页 / Explore / Legal / 聚合 Hub | 产品决策是否加文末 CTA |

---

## 五、推荐统一组件 API

> 基于线上 **C1 / F1 golden pages** 抽象，供后续实现参考。

### 5.1 `<SiteFAQ />`

```tsx
<SiteFAQ
  id="faq"
  title="Frequently Asked Questions"       // Comparison 可 override
  subtitle="Everything you need to know about {topic}."
  items={[{ question: string, answer: string | ReactNode }]}
  variant="marketing"                      // marketing | pricing | comparison
  schema={true}                            // FAQPage JSON-LD，DOM parity 必填
/>
```

| Prop | 必填 | 说明 |
|------|------|------|
| `items` | ✅ | 3–8 题 |
| `subtitle` | 推荐 | Feature/Study 线上已有；Comparison 建议补齐 |
| `title` | 可选 | Comparison 暂保留页专属 override |
| `schema` | 默认 true | 线上 Comparison / Feature 多数已有 |

### 5.2 `<FinalCTA />`

```tsx
<FinalCTA
  headline="Start Generating Notes in Seconds"
  subheadline="Join 300,000+ students…"
  primaryLabel="Generate Notes Free"
  primaryHref="https://thetawave.ai/auth/signup"
  secondaryLabel="Open App"
  secondaryHref="https://thetawave.ai/app"
  // trust_badges 组件内固定：
  // Free to Start · No Credit Card Required · Results in Under 2 Minutes
/>
```

| 页面类型 | headline 公式（来自线上 C1b 样本） | primaryLabel 公式 |
|----------|-----------------------------------|------------------|
| Feature | 动作 + 收益 | `{Verb} {Object} Free` |
| Use Case | 痛点/结果 | `Try Free for {Persona}` |
| Study | 学科 | `Start {Subject} Notes Free` |
| Comparison | 迁移/对比 | 默认 `Start Studying Free` |
| Blog | 主题 +  outcome | 默认 `Start Studying Free` |

---

## 六、优先迁移顺序（更新于 2026-06-24）

| 阶段 | 范围 | 状态 |
|------|------|------|
| ~~**1**~~ | Comparison → C1 | ✅ **已完成** |
| ~~**2**~~ | Pricing → F1 + C1 | ✅ **已完成** |
| ~~**3**~~ | Blog 新稿 6 篇 → F1 + C1 | ✅ **已完成** |
| **4** | Comparison FAQ H2/subtitle 标准化（F3→可配置 F1） | 待做 |
| **5** | `/download` C3 → C1；legacy `/thetawave-vs-chatgpt` 下线 | 待做 |
| **6** | Blog/Use Case sitemap 404 清理（10 条） | 待做 |
| **7** | Creator Program / Chrome Extension / KH | 待决策 |

---

## 七、页面类型 × FAQ × CTA × 变体（2026-06-24）

| 页面类型 | 抽检 OK | FAQ | FAQ 变体 | C1 | 同一套？ |
|----------|---------|-----|----------|-----|---------|
| Feature 详情 | 16 | ✅ | F1 | ✅ | ✅ |
| Use Case 详情 | 18 | ✅ | F1 | ✅ | ✅ |
| Study 详情 | 13 | ✅ | F1 | ✅ | ✅ |
| Blog 详情 | 7 | ✅ | F1 | ✅ | ✅ |
| Comparison 详情 | 12 | ✅ | **F3** | ✅ | ⚠️ FAQ 不同 |
| Pricing | 1 | ✅ | F1 | ✅ | ✅ |
| Download | 1 | ✅ | F1 | ❌ C3 | ⚠️ |
| Study 聚合 | 1 | ❌ | — | ✅ | ⚠️ |
| Comparison 索引 | 1 | ✅ | F3 | ✅ | ⚠️ |
| Blog 索引 | 1 | ❌ | — | ❌ | ❌ |
| Knowledge Hub | 191 | ❌ | — | ❌ | ❌ |
| 首页 / Legal / Explore | 4 | ❌ | — | ❌ | ❌ |
| Creator / Legacy | 2 | 部分 | F2/other | ❌ | ❌ |

---

## 八、Blog / Use Case sitemap 异常（2026-06-24）

| URL | HTTP | FAQ | CTA | 备注 |
|-----|------|-----|-----|------|
| 7 篇 Blog 线上稿 | **200** | ✅ F1 | ✅ C1 | 见 [site-structure §2.6](./thetawave-site-structure.md) |
| 8 篇 Blog sitemap slug | **404** | — | — | 待从 sitemap 移除或修复路由 |
| `/use-case/korean-history-exam-prep` | **404** | — | — | sitemap 残留 |
| `/use-case/toeic-prep` | **404** | — | — | sitemap 残留 |
| `/use-case/for-graduate-students` | **200** | ✅ F1 | ✅ C1 | **未进 sitemap** |

---

## 九、参考：线上 golden pages

| 用途 | URL | FAQ | Final CTA |
|------|-----|-----|-----------|
| FAQ + Schema | [/feature/ai-study-assistant](https://thetawave.ai/feature/ai-study-assistant) | F1 + subtitle + schema | C1 默认 copy |
| Final CTA Persona | [/use-case/for-pre-med-students](https://thetawave.ai/use-case/for-pre-med-students) | F1 | C1b `Try Free for Pre-Med` |
| Feature 自定义 CTA | [/feature/notes-generator](https://thetawave.ai/feature/notes-generator) | F1 | C1b `Generate Notes Free` |
| Blog live 文 | [/blog/best-ai-note-takers](https://thetawave.ai/blog/best-ai-note-takers) | F1 | C1 |
| Comparison（FAQ 仍 F3） | [/comparison/thetawave-vs-anki](https://thetawave.ai/comparison/thetawave-vs-anki) | F3 | **C1** ✅ |
| 非统一参考 | [/download](https://thetawave.ai/download) | F1 | C3 |

---

## 十、建议下一步（给实现 / 内容）

1. **Comparison FAQ**：统一 H2/subtitle，保留对比语境 override。  
2. **Download / Legacy**：补齐 C1 或 301 下线 `/thetawave-vs-chatgpt`。  
3. **Sitemap  hygiene**：移除 10 条 404；补收录 6 篇 Blog + `for-graduate-students`。  
4. **KH / Hub**：是否加轻量 FinalCTA — 需产品决策。  
5. **QA**：CI 检测 Tier A 详情页须 F1 + C1 + signup + 3 badges。

---

*审计原始 JSON（`_audit_components_20260624.json`、`_audit_full.json`）已于 2026-07-28 删除；本文保留 2026-06-24 抽检结论。*
