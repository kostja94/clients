## §EEAT — E-E-A-T 信号框架与引用标准

> **Phase 4 / Phase 5 加载 · Hellyeah B2B enterprise growth 适配版**
> **来源**：templates/02-fact-eeat.md v3.0 + Google QRG Sept 2025 + Helpful Content System 2025

---

### 1. E-E-A-T 四信号详解

| 信号 | 含义 | Hellyeah 博客体现方式 |
|------|------|----------------------|
| **Experience** | 第一手经验 | 真实客户案例（链 `/customers/{slug}`）、部署数据、具体 Growth 工作流描述、实操场景 |
| **Expertise** | 行业专业度 | 作者 Kostja 署名、Growth/性能营销领域深度分析、RCLL 框架应用、spend caps/approvals 边界意识 |
| **Authoritativeness** | 权威性 | 外部引用（Nielsen/行业报告）、客户案例公开可验证、竞品描述基于官方资料 |
| **Trustworthiness** | 可信度 | 来源引用、SOC 2 in flight（非 certified）、结果声明加 "results vary"、利益声明、方法论说明 |

---

### 2. Claim 类型 × 证据要求

| Claim 类型 | 最低证据要求 | 无证据处理 |
|------|------|------|
| **竞品产品能力** | 官方 docs / 官网 / pricing page | **P0**，改写或删除 |
| **产品状态**（GA/Preview/Beta/Alpha） | 官方公告 / changelog / 官网页 | **P0** |
| **ROI / 百分比 / 时间节省** | case study 文档 / 客户材料 / 内部单源 | **P0** |
| **市场数据 / funding** | GitHub / Crunchbase / 官方公告 / 可核查页面 | P1 或 P0（如用于核心论证） |
| **行业趋势** | Gartner / Forrester / Nielsen / 多来源交叉验证 | P1；加 "likely""emerging" 限定 |
| **技术定义** | 官方 docs / 标准文档 / 项目文档 | P1 |
| **自有产品能力** | docs / 官网 product page / internal source of truth | P1 |
| **准确率区间**（如 60–80%） | internal deployment data / public benchmark | P1；否则加 "based on internal deployments" |
| **Hellyeah 能力页统计**（如 3.2× ROAS） | 对应 `/capabilities/{slug}` 页 | P1；标注 "as stated on Hellyeah capability page" |

---

### 3. 引用优先级

1. 官方文档、官方 changelog、GitHub repo
2. 标准组织（W3C、IETF、ISO）
3. 一手研究或年度行业报告（Nielsen、Gartner、Forrester）
4. 权威媒体或行业分析
5. 二手 SEO/blog 资料
6. Reddit / forum（仅可作为用户观点引用，不作为事实依据）

---

### 4. 每篇文章类型最低引用数量

| 文章类型 | 最低外部证据 | 说明 |
|------|:---:|------|
| Pillar | 4–6 个来源，至少 2 个一手来源 | 品类定义文需最高证据标准 |
| Framework | 3–5 个来源 | 方法论文需支撑框架可信度 |
| CommercialEducational | 3–5 个来源 | 品类教育需行业数据 |
| PlatformExplainer | 2–4 个来源 | 平台介绍可以产品页面为主 |
| Alternative | 每个主要竞品至少 1 个官方来源 | 对比文必须公平 |
| UseCase | 2–4 个来源 + 案例 | 垂直场景需行业 + 案例 |
| Diagnosis | 3–5 个来源 | 问题诊断需数据支撑 |
| Compliance | 3–5 个权威来源 | 合规文需最高可信度 |

---

### 5. EEAT 信号检查清单（8 项）

| # | 检查项 | 标准 | Hellyeah 特定 |
|---|------|------|------|
| E1 | 量化数据有来源 | §2 Claim 类型表对齐 | 客户案例指标链 case study 页 |
| E2 | 竞品信息可核实 | 官方 docs / 官网；状态标注正确 | G4 阻断 |
| E3 | 时效性标注 | GA/Beta/Private Alpha + 核实日期 | Déjà Vu = private alpha |
| E4 | 无绝对化营销语 | 见 Voice §8.2 禁止措辞 | "designed to""aims to" 替代 "guaranteed" |
| E5 | 准确率区间有依据或弱化 | "based on internal deployments" | — |
| E6 | ≥1 个非自有产品推荐 | Wirecutter 式诚实 | Alternative 文必须有竞品优势段 |
| E7 | 署名真实 | author: Kostja（真实人名） | 不虚构署名 |
| E8 | 利益声明 | 产品文可接受透明漏斗；Research/Glossary 应有声明 | 不伪装独立研究 |

---

### 6. Google Who/How/Why 三问（HCU 2025）

| 问 | Hellyeah 博客体现 |
|------|------|
| **Who** created it? | `author: Kostja` — 真实创始人署名，有行业背景（Alignify 创始人、AI/SaaS 增长营销） |
| **How** was it created? | 方法论说明（RCLL 框架、一手客户部署经验、产品 docs 交叉验证） |
| **Why** does it exist? | 帮助增长团队做采购/组织决策 — 非纯 SEO 流量 |

**Pillar / Framework 类型强制**：文内须含一段 Who/How/Why 声明（Voice §8.3 已覆盖）。

---

### 7. AI 内容信号抑制（Google QRG Sept 2025）

Google 2025 年 9 月 QRG 新增 AI 内容评估维度。以下模式触发 AI 生成嫌疑，须主动规避：

| 高风险信号 | Hellyeah 规避策略 |
|------|------|
| 通用化措辞、无具体对象 | 每 300–500 词出现行业具体对象（广告平台名、客户名、metric 名） |
| 重复结构跨页 | 跨文章审计 Phase 5.5 检测 |
| 无作者署名 | 始终署 Kostja |
| 事实不准确 | G1–G7 + P1–P5 Gate 阻断 |
| 无人工 oversight 痕迹 | Voice Who/How/Why + spend caps/approvals 叙事 |

---

### 8. Source Map 模板（Phase 5 留存，不发布）

```markdown
## Source Map
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|
| Final Round AI $12M ARR, 4.2× ROAS | §4 | /customers/final-round-ai | 2026-06-15 | High |
| Cometly unified ad view | §3 | cometly.com/features/ads-manager | 2026-06-15 | High |
| 3.2× ROAS avg | §6 | /capabilities/performance-marketing | 2026-06-15 | Medium |
```

Confidence: **High** = 官网一手 / **Medium** = 能力页宣称 + 产品确认 / **Low** = 单案例。**Low 不得支撑核心论证。**

---

### 9. 跨篇数字一致性

同一数字跨篇出现须满足：
- 每篇都给引用链接
- 精度一致（$12M ARR vs $12 million ARR → 统一）
- Canonical 最完整上下文在 Pillar 或 capability 页

---

*eeat-framework · v1.0 · 2026-06-15 · adapted from templates/02-fact-eeat.md v3.0*
