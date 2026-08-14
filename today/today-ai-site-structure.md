# Today AI — 站点结构

**Last updated**: 2026-07-22 | 识别方式：landing withAllLinks + downloads/waitlist/privacy/terms（[today.ai/landing](https://today.ai/landing)）

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 | 状态 |
|------|---------|-----------|--------|------|
| `/landing` | 产品落地长页（Memories / Proactive / Capabilities / Use Cases） | AI personal assistant, proactive AI assistant, AI with memory | P0 | 已上线 |
| `/` | 简版首页 / Waitlist 入口 | Today AI, meet Today | P0 | 已上线 |
| `/downloads` | 客户端下载（Mac / iOS TF / Android） | Today AI download, Today Mac app | P0 | 已上线 |
| `/waitlist` | Early access 候补 | Today AI waitlist, early access | P0 | 已上线 |
| `/login` | 登录 | Today AI login | P1 | 已上线 |
| `/privacy` | 隐私政策（含 HealthKit / Health Connect / AI Providers） | Today AI privacy | P1 | 已上线（生效 2026-05-13） |
| `/terms` | 服务条款（Beta、新加坡法域） | Today AI terms | P1 | 已上线（生效 2026-04-14） |

访问日期：2026-07-22。来源：[today.ai](https://today.ai/)

---

## 2. URL 层级与信息架构

```
today.ai
├── /                         # 简版 Meet Today + Join Waitlist
├── /landing                  # 主营销长页（锚点 IA）
│   ├── #memories             # Living memory
│   ├── #proactive            # 主动介入
│   ├── #capabilities         # 模型 / 任务执行 / 连接器 / 云电脑 / 跨端 / Skills
│   └── #use-cases            # 生活与工作场景叙事
├── /downloads                # Mac arm64/x86_64 DMG；iOS TestFlight；Android APK
├── /waitlist                 # 候补（与 / 高度同构）
├── /login
├── /privacy
└── /terms

releases.today.ai             # 安装包 CDN（如 today-macos-arm64.dmg）
```

### `/landing` 结构

| 区域 | 内容 | CTA |
|------|------|-----|
| Nav | Memories / Proactive / Capabilities / Use Cases | Download / Log in |
| Hero | Meet Today — knows you & acts before you ask | Download App |
| Product demo | Morning Brief、Body Signals、任务、旅行等互动示意 | Ask Today… |
| Memories | Living memory：日子/人/偏好/目标，用户可控 | — |
| Proactive | 睡眠不足+会议 → 改行程；需求变更 → Organize changes；定时自动化 | — |
| Use Cases | 9 张角色卡滑动条（writer / cat mom / teacher / marathoner / young parents / freelancer / couple / musician / founder） | — |
| Capabilities | Frontier models、task execution、connectors、cloud computers、cross-device、Community Skills | — |
| Footer | Join early access / Downloads / Log in / Privacy / Terms / Socials | Waitlist / Download |

---

## 3. 技术架构

| 维度 | 观测 | 依据 |
|------|------|------|
| 前端 | 现代 SPA/营销站（大量视频与动效）；框架 ⚠️ 未确认 | 页面渲染特征 |
| 客户端 | **macOS 15+**（Apple Silicon + Intel）；**iOS/iPadOS**（TestFlight）；**Android**（APK） | `/downloads` |
| 发行 CDN | `releases.today.ai` | DMG 直链 |
| 健康数据 | Apple HealthKit；Android Health Connect | Privacy §1A/1B |
| AI 推理 | 自有系统 + 第三方：**AWS / Anthropic / OpenAI** 等 | Privacy §1C |
| 法域 | 条款适用 **新加坡**法律 | Terms §16 |
| robots.txt | **404** | 2026-07-22 |
| sitemap.xml | **404** | 2026-07-22 |
| 多语言 | 根页有 EN 标识；privacy/terms 有 `?language=en` | 浅本地化，深度 ⚠️ 待验证 |

---

## 4. 多语言

| 项 | 状态 |
|----|------|
| 主语言 | 英文 |
| URL | 无 `/zh/` 等前缀；隐私页 `?language=` 参数 |
| 中文站 | 未见独立中文营销站 |

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| 无 sitemap | — | — | — |
| 手工枚举核心站 | `/` `/landing` `/downloads` `/waitlist` `/login` `/privacy` `/terms` | 7 | — |
| Programmatic / Blog | 无 | 0 | — |

> **P0**：补 `robots.txt` + `sitemap.xml`，将 `/landing` 与下载页纳入索引。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/landing` | 锚点 + Download/Login/Waitlist/Legal | 教育 + 转化 |
| `/` `/waitlist` | Download / Login / Legal | 候补转化 |
| `/downloads` | 平台安装包 | 激活 |
| Footer | Product + Legal + Socials | 信任与合规 |

**缺失**：Blog、定价、About/团队、对比页、功能独立 URL、案例页。

---

## 7. URL 分阶段规划

| 阶段 | 建议新增 | 对标关键词 | 说明 |
|------|---------|-----------|------|
| 短期 | robots/sitemap；`/about`（公司/产品）；功能锚点页或 `/features` | P0 品牌+品类 | 信任与索引 |
| 中期 | `/blog`；`/compare/today-vs-chatgpt`；`/use-cases/{persona}` | P0–P1 | 教育与商业意图 |
| 长期 | 定价页（Beta 结束后）；中文落地；硬件/Agent 终端叙事页（若产品线落地） | P1–P2 | 与媒体「Agent 手机」叙事对齐或澄清 |

---

## 待验证项

- [ ] `/` 与 `/landing` 主入口策略（哪个为规范首页）
- [ ] 前端框架与托管商
- [ ] Community Skills 目录是否有公开 URL
- [ ] Today AI 对外英文主体名与新加坡实体关系

---

*关联：[主文档](./today-ai.md) | [keywords](./today-ai-keywords.md) | [capabilities](./today-ai-capabilities.md) | [competitors](./today-ai-competitors.md) | [use-cases](./today-ai-use-cases.md) | [growth-strategy](./today-ai-growth-strategy.md)*

*Last updated: 2026-07-22*
