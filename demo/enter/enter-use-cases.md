# Enter Pro — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[enter.md](./enter.md) | [enter-features.md](./enter-features.md) | [enter-keywords.md](./enter-keywords.md)

**Last updated**: 2026-06-25

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Sam — Solo Founder** | 一人公司 / Indie Hacker | 无预算雇全栈；需快速验证 PMF | 一周内上线 Landing + waitlist/支付 | 低–中（会写 prompt） |
| **Riley — PM** | B2B SaaS 产品经理 | 依赖工程排期做原型；Figma 无法跑通 | 可交互原型给 stakeholder 点 | 低（不写代码） |
| **Devon — Indie Dev** | 全栈兼职接案 | 重复 CRUD/landing 耗时 | Cursor 里 CLI 一键交付 live URL | 高 |
| **Maria — 小商家** | 本地零售转线上 | 建站/小程序门槛高 | 网店 + Stripe 收款 | 低 |
| **Alex — 初创 CTO（2–5 人）** | 早期技术负责人 | MVP 要快但要能导出代码 | Workspace 协作 + GitHub Sync | 高 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Sam | 黑客松前夜 | 用对话生成 SaaS Landing + 邮箱收集 | AI Website Builder + Deploy | ai saas landing page builder |
| Sam | 拿到首批付费用户 | 加 Stripe 订阅页 | Cloud + Stripe | build saas with ai |
| Riley | 评审会前 | 改按钮文案和配色不改代码 | Visual Editor | visual editor ai prototype |
| Riley | 与工程师对齐 | 导出 React 代码进 GitHub | Export + GitHub Sync | ai prototype to code |
| Devon | 客户要改 landing | 在 Cursor 粘贴 Enter CLI prompt | Enter CLI | enter cli cursor deploy |
| Devon | 本地 monorepo bug | Enter Code 跑测试修完交 PR | Enter Code | ai terminal coding agent |
| Maria | 旺季促销 | 上线商品 catalog + 购物车 | Online Shop Builder | ai online shop builder |
| Alex |  sprint 启动 | PM+Dev 同 Workspace 并行 session | Collaborative Coding | ai team coding workspace |
| Alex | 合规审查 | 证明代码可迁出、无 lock-in | Code Export FAQ | export ai generated react code |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| MVP Landing | Sam | AI Website Builder | ai landing page generator | `/features/ai-page-generator` |
| 全栈 SaaS | Sam/Alex | Cloud + Stripe | ai saas builder | `/features/saas-website-builder` |
| 原型演示 | Riley | Visual Editor | ai prototype builder | `/features/visual-editor` |
| IDE 交付 | Devon | Enter CLI | cursor ai deploy | `/cli` |
| 本地工程 | Devon | Enter Code | ai coding agent terminal | `/code` |
| 电商 | Maria | App Builder + Stripe | ai ecommerce app builder | `/features/online-shop-builder` |
| AI 客服 Bot | Alex | Agent Builder | build chatbot no code | `/features/ai-agent-builder` |
| 模板冷启动 | Sam | Templates | website template ai | `/templates` |

---

## 4. 用户旅程

```
认知：Google「ai app builder」· YouTube Enter Pro · X @EnterProAI · Discord
  ↓
考虑：首页 FAQ（免费 Credits、代码所有权、非技术可用）
  ↓
试用：描述 idea → 预览 → Visual Editor 微调
  ↓
转化：Credits 用尽 → Basic/Pro（Custom Domain、GitHub、协作）
  ↓
扩展：Enter CLI 进日常 IDE · Team 扩员 · 导出至自有 infra
  ↓
留存：Changelog 新能力 · Forum · School 教程
```

---

## 5. 未覆盖场景

| 场景 | 机会 | 关键词需求 |
|------|------|-----------|
| **企业采购** | SSO、审计、私有部署 | ai app builder enterprise |
| **移动原生 Store 上架** | 官网叙事含 iOS/Android，**待验证** 商店打包流程 | ai build ios app no code |
| **中国区小程序** | 首页提及 WeChat/Alipay mini program | wechat mini program ai builder |
| **Agency 白标** | 批量为客户建站 | white label ai website builder |

---

*来源：官网 Features/FAQ、[ai-app-builder](https://enter.converge.ai/features/ai-app-builder) 2026-06-25*
