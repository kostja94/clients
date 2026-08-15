# Volumn.ai 网站结构（推断）

> 关联：[volumn.md](./volumn.md) | [volumn-features.md](./volumn-features.md)

**说明**：以下基于 [volumn.ai](https://www.volumn.ai/) 首页与导航**可见**内容、以及 [pricing](https://www.volumn.ai/pricing) 抓取结果推断；**非**经完整爬虫验证的站点地图，路由变更后需更新。

---

## 一、导航与入口

| 项 | 说明 |
|----|------|
| 品牌 | Volumn.ai |
| 主导航（首页抓取） | Feature · Pricing · **Solutions**（下拉：Single Creators / Founders / Startups / Big Companies）· **Resources**（Blog、Doc、Changelog、FAQ、Free tools）· Affiliate · API |
| 账户 | Log in · Sign up for free |
| 信任 | 首页列出 About Us、Contact、Privacy、Terms、FAQ、Blog、Documentation、**prcrecluse@gmail.com** |

---

## 二、首页信息架构（逻辑块）

| 模块（顺序示意） | 内容 | 备注 |
|------------------|------|------|
| Hero | *The #1 AI Growth Tool for X/Twitter*、副文案、**Get started for free** | 标题竞品性强，需落地页与性能支撑 |
| 社会证明 | Trusted by：Alibaba、GitHub 等 logo（以线上为准） | 适合 Press/About 互链 |
| 信任/E-E-A-T | 指向 About、Contact、Privacy、Terms | 利于 YMYL 类评估 |
| 产品深层价值 | 「AI growth infrastructure」「trust, compliance, measurable pipeline」 | 可拆为独立解决方案页 |
| 分段 CTA | For Freelancers / For Startup（首页抓取片段） | 与 Solutions 叙事呼应 |

*注：官网可能还有 Ghost Writer 预览、Agent 四象限等模块；完整区块请以 DevTools 或内容库存为准。*

---

## 三、主要 URL（已验证或高度可能）

| 路径 | 用途 |
|------|------|
| https://www.volumn.ai/ | 首页 |
| https://www.volumn.ai/pricing | 定价与套餐对比 |
| https://www.volumn.ai/signup | 注册（首页 CTA 链） |
| https://volumn.ai/faq | FAQ（路径可能与 www 并存，注意 **canonical**） |
| https://volumn.ai/?ref_type=organic | 带参版本；SEO 需统一规范化 |
| Resources | Blog / Doc / Changelog / Free tools 等子路径需站内再点验 |

---

## 四、技术栈（未审计）

- 需通过 Response、`/_next` 或静态资源判断框架。  
- 建议：**Organization**、**WebSite**（含 SearchAction 若适用）、核心页的 **FAQPage**（FAQ）、产品页的 **SoftwareApplication**（若符合 Google 指南）。

---

## 五、内容/SEO 优先级建议

| 优先级 | 动作 |
|--------|------|
| P0 | **Pricing、FAQ、About、Privacy、Terms** 可爬、内链一致；`www` vs 裸域 **301 + canonical** |
| P0 | Solutions 四类人群各 **1 个可索引落地**（勿仅 nav 下拉无独立页） |
| P1 | Doc 侧补齐 **Integration（CRM）**、**API**、**积分消耗表** —— 利于比较类搜索 |
| P1 | 开源/第三方节选（如 [Power Up Tools](https://poweruptools.com/ai/volumn-ai)）监控品牌词 SERP |
| P2 | 英文与中文落地并行时，明确 **hreflang** 与主站定位，避免重复内容 |

---

*文档日期：2026-05-03*
