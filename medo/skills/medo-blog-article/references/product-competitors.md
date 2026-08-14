# MeDo 产品事实表与竞品矩阵

> Agent 在 Phase 4（Draft）与 Phase 5（SelfCheck）前加载。所有 claim 须对照本表 + citations.md。

---

## 1. 三分类决策框架（Blog 核心差异化）

AI mobile app builders 分为三类——**分类比品牌选择更重要**：

| 类别 | 技术路径 | 移动体验 | App Store 风险 | 典型工具 |
|------|----------|----------|----------------|----------|
| **Native generators** | Swift (iOS) + Kotlin (Android)，各平台独立 | 平台原生滚动、手势、组件 | 最低（为商店设计） | **MeDo**、部分新兴 builder |
| **Cross-platform generators** | React Native / Expo 或 Flutter | 接近原生，有 JS/Dart 运行时 | 中等（性能/手势偶发问题） | Replit、Rork、Newly、Anything |
| **Web wrappers** | 响应式网站 + Capacitor/PWA/Median.co 包装 | 常像「网站假装是 App」 | 较高（Guideline 4.2 薄应用） | Lovable、Bolt（移动路径）、v0 |

**A1 Gate**：不得将 Web wrapper 描述为 native generator。Lovable/Bolt 移动 = 生成 Web → 导出/包装，非直接 Swift/Kotlin。

---

## 2. MeDo 产品事实表

每条标注验证状态。不在表中 → 不能声称已实现。

| # | 能力 | 对外表达 | 验证状态 |
|---|------|----------|----------|
| 1 | **移动输出** | Native Swift + Kotlin from prompts | Blog 叙事核心；**待验证** 现网导出细节 |
| 2 | **真机测试** | QR code → app on your phone within ~1 min | Blog 叙事；**待验证** 全流程 |
| 3 | **上架路径** | TestFlight + Google Play guided submission | Blog 叙事；**待验证** 自动化程度 |
| 4 | **对话构建** | Conversational Build — multi-turn context in one project | 官方文档 + 社区评测 |
| 5 | **多 Agent** | Multi-Agent role分工，days → minutes | 官方 MIAODA 文档 |
| 6 | **全栈输出** | UI + API + DB + logic + deploy — working system, not mockup | 官方文档 + DEV 案例 |
| 7 | **PRD 快捷流** | Skip chat → requirements doc → Generate APP | 首页/广场卡片暗示 |
| 8 | **插件集成** | Stripe、Supabase、数百 API | 官方 Plugins 文档 |
| 9 | **代码导出** | Yes（Blog 对比表叙事） | **待验证** 许可与格式 |
| 10 | **发布** | Publish to shareable Live URL | 官方文档 |
| 11 | **应用广场** | Gallery with 17k+ UGC apps | **待验证** 实时计数 |
| 12 | **定价** | Credits-based; $5/2000 credits (PH narrative) | **待验证** 定价页 |
| 13 | **免费层** | Credit-limited free tier + daily free credits (PH) | **待验证** |
| 14 | **背书** | MeDo by Baidu; Baidu AI Cloud MIAODA docs | 可查证 |
| 15 | **运营** | Hackathon $50k; Affiliate 30% recurring | 官网 Banner；条款 **待验证** |

### MeDo 最适合人群（诚实定位）

- 非开发者要 **真原生** iOS/Android，不想学 Xcode/Android Studio
- 要 QR 真机测试、TestFlight 路径，不想折腾 Expo/EAS
- 第一个 App：habit tracker、niche community、internal tool、small marketplace
- 接受 credits 计费、较年轻的集成目录

### 何时不选 MeDo（A3 Gate 必填场景）

| 场景 | 更好选择 | 原因 |
|------|----------|------|
| 纯 Web SaaS / landing page | Lovable、Bolt | Web-first 成熟、Remix 生态 |
| 需要完整 IDE 可见性、会看代码 | Replit Agent | 全 IDE、多语言 |
| 经典可视化拖拽 no-code | Adalo、Thunkable | 画布式、非 vibe coding |
| 3D 游戏、重度 AR、实时视频管线 | 专业引擎 / 原生团队 | AI builder 甜蜜区外 |
| 银行/远程医疗等强监管 | 工程团队 + 合规审查 | 无论何种生成方式 |

---

## 3. 竞品事实表

对比文须逐工具对照。定价须 `as of June 2026`。

### 3.1 Lovable

| 维度 | 事实 |
|------|------|
| **定位** | AI full-stack **Web** app builder (React + Supabase) |
| **移动输出** | Web app → Capacitor/Median.co 包装；**非** 原生 Swift/Kotlin |
| **真机测试** | Web preview；移动需额外 wrap 步骤 |
| **App Store** | 可提交 wrapped app；Guideline 4.2 风险较高 |
| **优势** | 社区声量、Remix 模板、Web SaaS 极快 |
| **劣势（移动）** | 移动 = 网站包装；原生感弱 |
| **最适合** | Web SaaS、landing、内部 dashboard |
| **验证** | 2026-06-04；lovable.dev/guides + FAQ |

### 3.2 Bolt.new

| 维度 | 事实 |
|------|------|
| **定位** | Browser full-stack prototype + deploy (StackBlitz) |
| **移动输出** | Web-first；移动需导出/wrap |
| **优势** | 即时预览、开发者友好 |
| **劣势** | 偏工程向；非开发者门槛高于 MeDo |
| **最适合** | 会看代码的 builder、快速 Web MVP |
| **验证** | 2026-06-04 |

### 3.3 Replit Agent

| 维度 | 事实 |
|------|------|
| **定位** | IDE + Agent；React Native/Expo 移动路线 |
| **移动输出** | Cross-platform (RN/Expo) |
| **真机测试** | Expo Go QR |
| **App Store** | Guided flow via EAS |
| **优势** | 完整 IDE、多语言、协作 |
| **劣势** | 仍面向会看代码的用户；非纯 no-code |
| **最适合** | 教育者/半技术用户要 RN + IDE |
| **验证** | 2026-06-04；replit.com/blog/mobile-apps |

### 3.4 Rork

| 维度 | 事实 |
|------|------|
| **定位** | Mobile-only vibe coding |
| **移动输出** | React Native / Expo |
| **真机测试** | Device preview |
| **App Store** | EAS submit workflow |
| **优势** | 移动专注、vibe coding 体验 |
| **劣势** | RN 运行时；非 Swift/Kotlin 原生 |
| **最适合** | 要移动专注的 cross-platform builder |
| **验证** | 2026-06（Blog 对比表叙事） |

### 3.5 Newly

| 维度 | 事实 |
|------|------|
| **定位** | RN/Expo + store compliance automation |
| **移动输出** | Cross-platform |
| **优势** | 合规辅助提交 |
| **最适合** | 担心审核合规的 RN 路线 |
| **验证** | 2026-06（Blog 对比表叙事） |

### 3.6 Anything

| 维度 | 事实 |
|------|------|
| **定位** | RN (Expo) prototype → production |
| **移动输出** | Cross-platform |
| **优势** | Cloud-signed builds、GitHub sync |
| **最适合** | 原型到生产的 RN 管线 |
| **验证** | 2026-06（Blog 对比表叙事） |

### 3.7 Adalo / Thunkable

| 维度 | 事实 |
|------|------|
| **定位** | 经典可视化 no-code mobile |
| **移动输出** | 专有运行时 / 可视化画布 |
| **优势** | 成熟画布、非 vibe coding 用户熟悉 |
| **劣势** | AI 原生程度低；非 Swift/Kotlin 导出 |
| **最适合** | 偏好拖拽而非对话的 no-code 用户 |
| **验证** | 2026-06 |

### 3.8 v0 (Vercel)

| 维度 | 事实 |
|------|------|
| **定位** | AI UI / 组件生成 |
| **移动输出** | UI 为主；后端/DB 需另配 |
| **最适合** | 前端/UI 原型 |
| **验证** | 2026-06-04 |

### 3.9 Capacitor / Median.co（非 builder，是包装层）

| 维度 | 事实 |
|------|------|
| **角色** | 将现有 Web 应用包装为可提交的移动 binary |
| **风险** | Guideline 4.2 — minimum functionality |
| **Blog 用法** | 解释 Web wrapper 路径，非独立 builder |

---

## 4. 对比表标准列（Comparison / Alternative 必用）

| 列名 | 说明 |
|------|------|
| Tool | 产品名 |
| Category | Native / Cross-platform / Web wrapper |
| Mobile output | Swift+Kotlin / RN+Expo / Wrapped web |
| Real-device test | QR / Expo Go / Browser preview |
| App Store path | TestFlight+EAS / Guided / Extra wrap steps |
| Code export | Yes / Limited / Locked |
| Free tier | Credit-limited / Trial / None |
| Best for | 诚实一句话 |

---

## 5. 成本参考区间（DecisionGuide / Pillar 可引用）

| 项目 | 典型成本（2026） | 来源级别 |
|------|------------------|----------|
| AI builder subscription | $20–50/month | P1 — 标注 as of date |
| Apple Developer Program | $99/year | P0 — developer.apple.com |
| Google Play Console | $25 one-time | P0 — play.google.com |
| Backend free tier (Supabase/Firebase) | $0–25/month at low scale | P1 |
| **总计首年（单平台）** | ~$150–250 + builder | 分析衍生 |

禁止写死 MeDo Credits 具体数值而不加 as-of。

---

## 6. 场景级对照（快速参考）

### 「48 小时验证付费 MVP（移动原生）」

| 选项 | 原生输出 | 非技术友好 | 真机 QR | 支付集成 |
|------|----------|------------|---------|----------|
| MeDo | ✓（叙事） | 高 | ✓（叙事） | Stripe 插件 |
| Lovable | ✗（Web wrap） | 高 | 需额外步骤 | 集成 |
| Replit | RN/Expo | 中 | Expo Go | 依配置 |
| Rork | RN/Expo | 中高 | ✓ | 依配置 |

### 「上架 App Store 非开发者」

| 选项 | 原生过审风险 | TestFlight 路径 | 账户删除模板 |
|------|-------------|-----------------|--------------|
| MeDo | 低（叙事） | 引导（叙事） | 须自测 |
| Lovable wrap | 较高 | 需 Mac/signing 或第三方 | 须自测 |
| Replit/Rork | 中 | EAS + Expo | 须自测 |
