# App Store 与 Google Play 合规（MeDo Blog）

> Agent 在 Phase 4 撰写 PublishGuide / Diagnosis 时加载。所有政策 claim 须 A2 Gate。

**时效标注（必填）**：正文须含 `as of {month} {year}` 时效声明（A2 Gate）——PublishGuide / Diagnosis 用正文引用块承载（见 project-config.md §4），全文 1 处。规则变更快 — 提交前须核对官方最新版。

---

## 1. Guideline 4.2 — Minimum Functionality（Apple）

**核心**：App 不能仅是网站的重新包装；须提供超越移动网站的原生价值。

| 风险信号 | AI-built app 常见触发 |
|----------|----------------------|
| 薄功能 | 仅展示静态 Web 内容 |
| 无离线能力 | 完全依赖远程加载 |
| 无原生交互 | 无 push、无生物识别、无本地存储 |
| Capacitor 包装站 | Lovable/Bolt Web → wrap 路径 |

**Blog 表述**：
- ✅ "Wrapped web apps face higher Guideline 4.2 rejection risk"
- ❌ "Capacitor apps always get rejected"

**官方来源（P0）**：
- <a href="https://developer.apple.com/app-store/review/guidelines/" rel="nofollow noopener">App Store Review Guidelines</a> — Section 4.2

---

## 2. 账户删除要求（2026）

Apple 与 Google 均要求：若 App 支持账户创建，须提供**应用内账户删除**路径。

| 平台 | 要求 | AI-built app 常见失败 |
|------|------|----------------------|
| Apple | In-app account deletion | AI 生成 sign-in 模板但无 deletion flow |
| Google | Account deletion option | 同上 |

**修复清单**：
1. 设置页含 Delete Account 入口
2. 删除须真正清除服务端数据（非仅登出）
3. 隐私政策描述删除流程

**官方来源（P0）**：
- Apple: App Store Review Guidelines — Data Collection and Storage
- Google: <a href="https://support.google.com/googleplay/android-developer/answer/13327111" rel="nofollow noopener">User Data policy</a>

---

## 3. 隐私政策与数据披露

| 检查项 | 要求 |
|--------|------|
| 隐私政策 URL | 必须 live、可访问 |
| App Store Connect 问卷 | 声明须与实际 SDK/Analytics 一致 |
| AI builder 隐藏 SDK | Firebase Analytics 等常被 AI 自动加入 — 须审计 |

**常见 AI app 失败**：声明 "no data collected" 但实际有 analytics SDK。

**Blog 建议**：提交前用设备隐私报告或 builder 集成清单核对。

---

## 4. TestFlight（iOS 非开发者）

### 流程摘要

1. 加入 Apple Developer Program（$99/yr）
2. 在 App Store Connect 创建 App 记录
3. 上传 build（MeDo/云签名 builder 可代劳构建）
4. 添加 internal/external testers
5. 测试者通过 TestFlight app 安装

| 要点 | 非开发者须知 |
|------|-------------|
| 无需 Xcode 全程 | 云签名 builder 可处理 build |
| 仍需开发者账号 | 无法绕过 $99/yr |
| External testing | 可能需 Beta App Review |
| 测试人数 | Internal ≤100；External 更多但需审核 |

**官方来源（P0）**：
- <a href="https://developer.apple.com/testflight/" rel="nofollow noopener">TestFlight — Apple Developer</a>

**独立文候选**：`testflight-non-developers`（Batch 4）

---

## 5. Google Play 发布要点

| 项目 | 2026 要点 |
|------|-----------|
| 注册费 | $25 一次性 |
| 身份验证 | 新账号须身份验证（增加数天） |
| 内部测试 | Play Console internal testing track |
| 数据安全表单 | 须与隐私政策一致 |

**官方来源（P0）**：
- <a href="https://play.google.com/console" rel="nofollow noopener">Google Play Console</a>

---

## 6. 开发者账户成本（P0 数字）

| 平台 | 成本 | 周期 |
|------|------|------|
| Apple Developer Program | $99 | /year |
| Google Play Console | $25 | one-time |

正文引用须链官方 programs 页。

---

## 7. AI-built app 常见拒审原因（Diagnosis 文核心）

| # | 原因 | 修复方向 |
|---|------|----------|
| 1 | **Thin functionality (4.2)** | 加原生功能：push、offline、biometric |
| 2 | **Missing account deletion** | 加 in-app delete + backend purge |
| 3 | **Privacy policy mismatch** | 审计 SDK；更新政策与问卷 |
| 4 | **Broken demo login** | 提供有效 reviewer 账号 |
| 5 | **Incomplete metadata** | 图标、截图、描述齐全 |
| 6 | **Misleading screenshots** | 截图须反映实际 UI |
| 7 | **Guideline 2.1 crashes** | 真机测 3 天无崩溃 |

---

## 8. 发布前 Pre-flight Checklist（PublishGuide 必用）

```
- [ ] Core loop works on physical device (not simulator)
- [ ] Crash-free for 3 days normal use
- [ ] 5 strangers tested via TestFlight/internal track
- [ ] Account deletion works (if sign-in exists)
- [ ] Privacy policy URL live and accurate
- [ ] Demo credentials prepared for reviewer
- [ ] App icon 1024×1024 (iOS) / adaptive icon (Android)
- [ ] Screenshots on correct device sizes
```

每项后须 2+ 句解释「为什么」— 见 Golden Example #04。

---

## 9. 审核时间预期

| 平台 | 典型 | Blog 表述 |
|------|------|-----------|
| Apple | 24–72 hours | 标注 "typically" + as-of |
| Google | 数小时–数天 | 同上 |
| 拒审后复提 | 重新排队 | 修复后再 submit |

禁止 "guaranteed approval in X hours"。

---

## 10. Resubmission 流程

1. 读拒审邮件 — 定位具体 Guideline 条款
2. 修复 — 一项一项对照
3. Resolution Center 回复 — 说明修复内容
4. 重新提交 — 附 reviewer notes
5. 若多次拒审 — 考虑 appeal 或咨询 Apple Developer Support

**Diagnosis 文**：每类拒审给 before/after 修复示例（文字描述，非虚构截图）。
