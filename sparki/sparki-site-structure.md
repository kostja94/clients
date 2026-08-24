# Sparki 网站结构（推断）

## 一、首页信息架构（逻辑块）

| 模块（顺序示意） | 内容 | 备注 |
|------------------|------|------|
| Hero | *the first AI Editing Agent*、主 CTA（Try For Free） | 品牌定位 |
| 功能快捷标签 | Copy Style、Long to Short、AI Caption、AI Commentary、Video Resizer、Highlight Reels | 可能为锚点或未来独立页 |
| 场景展示 | Vlog、Commentary、Montage、Talking-head | 重复区块（首页常见排版） |
| Why Sparki | 三大卖点：AI editor、Chat to edit、Multi-round revision | 转化支撑 |
| FAQ | 是什么、怎么用、是否免费、工作原理、支持的视频类型 | 适合 FAQ schema |
| Pricing | Free / Starter / Plus / Enterprise | 含年付折扣展示 |
| Footer CTA | Try Now / Sign In | — |

---

## 二、URL 与页面假设

| 路径（待验证） | 可能用途 |
|----------------|----------|
| `/` | 首页 |
| `#pricing` 或 `/pricing` | 定价（若存在独立页利于投放与分享） |
| 登录/注册流 | Sign In / Register（具体路径需抓包或站点地图） |
| Enterprise | 邮件 **enterprise@sparki.io**，或未来 `/enterprise` |

---

## 三、技术栈（未审计）

- 需通过 DevTools、`_headers`、或公开资料确认框架（Next.js / 其他）与国际化策略。  
- 建议提供 **sitemap.xml**、**canonical** 与核心页的 **Open Graph** 以便社媒与 AI 预览。

---

## 四、内容/SEO 优先级建议

| 优先级 | 动作 |
|--------|------|
| P0 | 定价、功能定义、隐私/条款链接清晰可爬 |
| P1 | 场景页或博客集群（四类视频 + 六大功能标签） |
| P1 | FAQ 扩展为结构化数据（JSON-LD） |
| P2 | 案例研究、教程视频、YouTube 与站内互链 |

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[主文档](./sparki.md) | [features](./sparki-features.md)*
*说明：以下基于 [sparki.io](https://sparki.io/) 首页可见模块推断；非站内爬虫地图，上线新路由后需人工更新。*
*Last updated: 2026-04-08*
