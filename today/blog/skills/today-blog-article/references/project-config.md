# Today AI Blog — 项目配置与 Gate 清单

> Agent 在 Phase 0 / Phase 5 前加载本文件。创作阶段禁止读取 skill 文件夹外文档。

---

## 1. 品牌与项目配置

| 配置项 | Today AI 值 |
|--------|------------|
| **品牌/产品名** | Today AI / Today |
| **主域名** | today.ai |
| **博客 URL 模式** | `https://today.ai/blog/{slug}` |
| **博客路径前缀** | /blog/ |
| **品类 one-liner** | Proactive personal AI assistant with living memory |
| **Blog 叙事主轴** | Knows you — and acts before you ask |
| **blogLayout** | `cluster-folders` — 见 `topic-cluster-layout.md`；当前簇：`personal-agent/` |
| **当前阶段** | Early-access Beta（Terms：功能可变、当前免费） |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **署名默认** | Today Team |
| **法域** | 新加坡（Terms §16） |
| **客户端** | macOS 15+、iOS/iPadOS（TestFlight）、Android（APK） |

### 1.1 目标受众（ICP）

| 层级 | 画像 |
|------|------|
| **Primary** | 日程与信息过载的知识工作者、创作者、创始人 |
| **Secondary** | 需要生活+健康同一上下文的角色（带娃、马拉松、旅行、宠物） |
| **Tertiary** | 科技早鸟、TestFlight/Skills 社区用户 |

### 1.2 Blog 差异化叙事（每篇须一致）

1. **Living memory** — 日子、人、偏好、目标常驻上下文，用户可控
2. **Proactive** — 在你开口前基于信号行动（睡眠、日程、需求变更）
3. **Execution** — 任务做到完成态，非仅建议（云电脑、连接器、工具调用）
4. **全生活** — 非纯办公 Copilot；官网 9 角色用例为叙事素材
5. **诚实 Beta** — 功能可变、当前免费；不夸大 GA 能力

### 1.3 可链接 URL 白名单

| 类型 | 路径 | 说明 |
|------|------|------|
| 博客 | `/blog/{slug}` | 见 content-graph.md |
| 主落地 | `/landing` | 主转化叙事 |
| 锚点 | `/landing#memories` `#proactive` `#capabilities` `#use-cases` | 能力承接 |
| 下载 | `/downloads` | Mac / iOS / Android |
| 候补 | `/waitlist` | 主 CTA |
| 登录 | `/login` | 已上线 |
| 合规 | `/privacy` `/terms` | 健康数据、AI Provider 披露 |
| Healthcare hub | `/healthcare` | 生活方式健康，非诊断 |
| Healthcare spoke | `/healthcare/meal-planner` `/healthcare/sleep-tracker` `/healthcare/fitness-coach` | 场景子页 |

### 1.4 禁止内链

| 路径 / 域名 | 状态 | 规则 |
|------------|------|------|
| `/pricing` | 无（Beta 免费） | 正文不链；可文字提及 Beta 免费 |
| `/compare/*` | 待建 | 用博客 Comparison 文承接 |
| `article.today.ai` | 子域 origin | **禁止**作为规范 URL 内链；须用 `today.ai` |
| 未上线 use-case 落地页 | 待建 | G6 阻断 |

**G6**：forthcoming 链接全文 ≤1；正文核心流程不得使用 forthcoming 链接。

---

## 2. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **G1** | 事实错误 | 产品能力、Beta 状态与 today.ai 现网矛盾 | 对照 product-competitors.md §Today 事实表 |
| **G2** | 死链 | 内链 404；外链大面积失效 | link_checker.py + 白名单核对 |
| **G3** | 无来源数字 | ROI、准确率、用户量等量化 claim 无 attribution | Source Map 必填 |
| **G4** | 竞品/产品状态错误 | GA/Beta/Deprecated 与官方公告矛盾 | R3 Fetch 竞品官网 |
| **G5** | 产品能力夸大 | 禁将 Beta 功能标为 GA；禁未验证 fastest/only | 用 "designed to"、"in Beta" |
| **G6** | 内链指向未上线页面 | 对照 §1.3 白名单 | forthcoming >1 → Fail |
| **G7** | 品牌/合规风险 | 贬低竞品；健康诊断表述；硬件叙事未经官方确认 | 见 §4 |

---

## 3. T1–T4 Today 专属 Gate

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **T1** | Healthcare 合规越界 | 使用 diagnose / symptom checker / medical advice / treat / cure；未加 lifestyle support 免责 | HealthcareGuide 全文扫描 + FAQ |
| **T2** | Beta 状态失实 | 写具体定价、付费功能 GA、未在 Terms 出现的 SLA | 对照 Terms + 主文档 Beta 声明 |
| **T3** | 产品线叙事混淆 | 将 GUI Agent / 智能终端硬件作为 Today GA 产品描述（除非官方确认） | 官网 software assistant 叙事为准 |
| **T4** | 健康数据 claim 失实 | HealthKit/HRV/睡眠等效果 claim 与 Privacy 矛盾或无来源 | 对照 Privacy §1A/1B |

**G1–G7 + T1–T4 全部 Pass 方可交付。**

---

## 4. 敏感表述与合规

| 禁止 | 替代 |
|------|------|
| 唯一 / 全球首个 / only assistant that | designed for / strongest fit for |
| 医疗诊断 / AI doctor / symptom checker | lifestyle support, not medical diagnosis |
| 保证治愈 / guaranteed health outcomes | may help you notice patterns / supports your routine |
| revolutionary / game-changing / seamless / magic | 具体能力描述 |
| just / merely / only does X（竞品） | 客观对比 |
| click here / learn more（锚文本） | 描述性短语 |

### Healthcare 免责模板（HealthcareGuide 正文必填，T1）

> Today provides lifestyle support, not medical diagnosis or treatment. This is not medical advice. Consult a qualified professional for health decisions.

### Beta 声明模板（产品能力段建议）

> Today is in early-access Beta. Features may change, and the product is currently free during Beta (see Terms).

---

## 5. 转化路径

| CTA 类型 | 路径 | 使用场景 |
|---------|------|---------|
| **主 CTA** | `/waitlist` | BrandPillar、Comparison、HealthcareGuide |
| **次 CTA** | `/downloads` | UseCase、HowTo、已有客户端用户 |
| **能力承接** | `/landing#proactive` `#memories` | Glossary、Opinion |
| **Healthcare spoke** | `/healthcare/meal-planner` 等 | Healthcare 簇 Spoke |

正文 CTA ≤2 次；单一主行动。

---

## 6. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章 |
| **错开方向** | 从锚点日往前排，越重要的文章排越近 |
| **避让已占用日** | 见 content-graph.md 日期占用表 |

*project-config · v1.0 · 2026-09-01*
