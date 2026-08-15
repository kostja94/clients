# Morph Studio 网站结构（IA）

> 关联：[morphstudio.md](./morphstudio.md) | [morphstudio-keywords.md](./morphstudio-keywords.md) | [morphstudio-features.md](./morphstudio-features.md)

**Last updated**: 2026-03-25

---

## 1. 顶层导航（观测）

App、Products、Pricing、About Us、Feedback、语言（English）、**Get Started For Free**

---

## 2. Must Have（SEO / 转化）

| 优先级 | 路径/页 | 目的 |
|--------|---------|------|
| P0 | / | 品牌、模型总览、主 CTA |
| P0 | /pricing 或等价 | 订阅与转化 |
| P0 | 登录/注册流 | Google、Discord、Email |
| P1 | 各 **Image / Video / Audio** 工具落地页（页脚列表） | 长尾词、内链枢纽 |
| P1 | Models 子页（Seedance、Nano Banana 2、Veo…） | 模型词、信任背书 |
| P1 | About：Mission、Newsroom、Contact | 品牌与外链 |
| P2 | Discord、Feedback / Book a call | 社区与销售线索 |
| P2 | `/for-filmmakers` 或 `/solutions/filmmaking`（可选） | 承接 *AI video for filmmaking* 等长尾，内链至 text-to-video、Open Canvas；与首页分工见 [morphstudio-use-cases.md](./morphstudio-use-cases.md) §4 待填充 |

---

## 3. 技术 SEO 注意

- 首页与模块若 **重复输出相同区块**（多段相同标题/列表），需检查 HTML 重复与 CWV。  
- 工具页数量大时：统一 **面包屑**、**hub 页**（Image Tools / Video Tools）避免孤儿页。  
- **错别字**（如产品名拼写）影响品牌词与 E-E-A-T 观感，建议全站替换并做 301（若改 URL）。

---

## 4. 内链策略（摘要）

- 首页 → 三大块（Image / Video / Canvas）→ 代表工具页 → Pricing  
- 各工具页 → 相关模型页 → 注册 CTA  
- Newsroom → 可支撑品牌词与外链自然增长  

---

## 5. 待工程确认

- [ ] 实际 slug 与本文假设是否一致（尤其带 `/` 尾或不带）  
- [ ] App 子域或路径是否与主站 SEO 分工（若分离）  
