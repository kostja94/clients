# Quriov — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[quriov.md](./quriov.md) | [quriov-keywords.md](./quriov-keywords.md) | [quriov-features.md](./quriov-features.md) | [quriov-others.md](./quriov-others.md)

**Last updated**: 2026-07-06 | 识别方式：首页 + 主导航 + 页脚抓取（[quriov.com](https://quriov.com/)）

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [quriov.md](./quriov.md) |
| 关键词 | [quriov-keywords.md](./quriov-keywords.md) |
| 功能 | [quriov-features.md](./quriov-features.md) |
| 使用场景 | [quriov-use-cases.md](./quriov-use-cases.md) |
| 竞品 | [quriov-competitors.md](./quriov-competitors.md) |
| 增长策略 | [quriov-growth-strategy.md](./quriov-growth-strategy.md) |
| Sitemap 明细 | [quriov-others.md](./quriov-others.md) |

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 品牌首页（单页叙事） | smart ring, ai wearable, private ai assistant | P0 |
| `/products/quriov-smart-ring` | 商品详情页 | quriov smart ring, sleep tracker ring, affordable smart ring | P0 |
| `/collections/all` | 商品目录 | quriov products, smart ring shop | P1 |
| `/pages/about` | 关于我们 | quriov about, ai wearable company | P2 |
| `/pages/contact` | 联系我们 | quriov contact, quriov support | P2 |
| `/policies/privacy-policy` | 隐私政策 | — | P3 |
| `/policies/terms-of-service` | 服务条款 | — | P3 |
| `/policies/shipping-policy` | 配送政策 | — | P3 |
| `/policies/refund-policy` | 退货政策 | — | P3 |
| `/cart` | 购物车 | — | P3 |
| `/checkout` | 结账 | — | P3 |

---

## 2. URL 层级与信息架构

```
quriov.com（Shopify 建站）
├── /                                          # 首页：品牌叙事（单页，含 Intelligence + Journey + Glasses Waitlist）
│
├── 商店
│   ├── /collections/all                       # 商品目录（当前仅 1 个 SKU）
│   └── /products/quriov-smart-ring            # Smart Ring 商品详情页
│       ├── 颜色选择（Black / Silver / Gold）
│       ├── 尺寸选择（US 7–13）
│       ├── 产品描述 + 规格 + FAQ
│       ├── 评价区（94 条，4.79 分）
│       └── Add to cart → /cart → /checkout
│
├── 品牌
│   ├── /pages/about                           # 品牌故事：Why we exist / Journey / Beliefs
│   └── /pages/contact                         # 联系方式 + 表单
│
├── 政策（Shopify 默认页面）
│   ├── /policies/privacy-policy
│   ├── /policies/terms-of-service
│   ├── /policies/shipping-policy
│   └── /policies/refund-policy
│
├── 购物
│   ├── /cart                                   # 购物车
│   └── /checkout                               # Shopify 结账
│
└── 全局
    ├── 多币种选择器（200+ 国家/地区，货币自动切换）
    ├── 搜索栏
    ├── 账户（登录/注册）
    └── 页脚导航
```

### 主导航（2026-07-06 观测）

| 区域 | 项 |
|------|-----|
| 顶栏 | Home · Catalog · Contact |
| 搜索 | 全局搜索（商品/页面） |
| 账户 | 登录/注册 |

### 页脚

| 区域 | 项 |
|------|-----|
| Shop | Smart Ring · All products |
| Company | About · Contact |
| Support | Shipping · Returns · Privacy · Terms |
| Contact | support@quriov.com · +1 585-618-2202 · 30 N Gould St STE R, Sheridan, WY 82801, US |

---

## 3. 首页结构与叙事流

首页为 **单页叙事设计**（One-Page Brand Story），自上而下分节：

| 节序 | 区域 | 内容 | CTA |
|------|------|------|-----|
| Hero | Meet Quriov | 主标题 + 副标题（Glasses, a ring, an app — different ways in） | Explore the ring / See the journey |
| Section 1 | The Intelligence | 三原则：① It learns you ② Dependable first ③ Yours over time | — |
| Section 2 | The Journey | 三步路线图：Ring（In stock）→ App（Coming soon）→ Glasses（In development） | Shop the ring |
| Section 3 | The Glasses Waitlist | 眼镜 waitlist 邮件收集 | Email 提交 |

---

## 4. 技术架构

| 维度 | 观测 |
|------|------|
| 建站平台 | **Shopify**（Privacy Policy 明确声明 powered by Shopify） |
| 前端栈 | Shopify 主题（**待验证** 主题名，推测 Dawn 或定制主题） |
| 支付 | Shopify Payments + 多币种支持 |
| 货币 | 200+ 国家/地区货币选择器，自动按 IP/地区切换 |
| 语言 | 仅英语 |
| 配送 | 仅美国发货（Shipping Policy 声明） |
| CDN / 安全 | Shopify CDN / Cloudflare **待验证** |
| 认证 | Shopify 账户系统 |
| SEO | Shopify 自带 SEO 功能（title/meta/alt/sitemap 自动生成） |
| 评价 | Shopify 内置评价系统（94 条，4.79 分） |
| 邮件 | waitlist 邮件收集（首页底部，**待验证** 邮件服务商） |

---

## 5. 多币种支持

货币选择器覆盖 200+ 国家/地区（2026-07-06 观测），包括但不限于：

| 区域 | 货币示例 |
|------|---------|
| 北美 | USD $（US）、CAD $（Canada） |
| 欧洲 | EUR €、GBP £、CHF |
| 亚太 | JPY ¥、KRW ₩、AUD $、SGD $、CNY ¥ |
| 中东 | AED、SAR、QAR |
| 拉美 | MXN、BRL、ARS |
| 东南亚 | THB ฿、IDR Rp、MYR RM、PHP ₱、VND ₫ |

*注：支持多币种展示但当前仅美国发货，显示全球化拓展意图。*

---

## 6. robots.txt 与 Sitemap

| 项 | 内容 |
|----|------|
| robots.txt | **待验证**（抓取超时；Shopify 默认 Allow 所有并自动生成 sitemap.xml） |
| Sitemap | Shopify 自动生成 `sitemap.xml`（**待验证** 具体 URL 量级） |
| AI 爬虫 | **待验证** Shopify 默认规则 |

---

## 7. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/`（首页） | CTA（Explore the ring / Shop the ring / Join waitlist） | 商品页、waitlist |
| `/products/quriov-smart-ring` | Add to cart / Size guide / Reviews / FAQ | 购物车 |
| `/pages/about` | 品牌故事 + Journey 介绍 | 商品页（间接） |
| `/collections/all` | 商品卡片 → 详情 | 商品页 |
| 页脚 | 全站导航 + 联系信息 | 各政策页、Contact |

---

## 8. URL 分阶段规划（SEO 建议）

| 阶段 | 建议新增 | 链关键词 |
|------|---------|---------|
| **短期** | `/blogs/smart-ring-guide` Blog 体系搭建（Shopify 内置 Blog） | smart ring guide, best smart ring |
| **短期** | `/pages/vs-oura` 对比页 | oura ring alternative, quriov vs oura |
| **短期** | `/pages/size-guide` 独立尺码指南（含视频） | smart ring sizing guide |
| **中期** | `/pages/app` App 预注册页 | quriov app, little q ai app |
| **中期** | `/blogs/*` 睡眠健康/可穿戴科普内容矩阵 | sleep tracking tips, wearable health guide |
| **中期** | 加拿大/英国/澳洲发货页面更新 + 本地化 | smart ring canada, smart ring uk |
| **长期** | `/products/quriov-glasses` 眼镜产品页 | ai smart glasses |
| **长期** | 多语言站（/ja /ko /de 等） | smart ring japan, smart ring germany |

---

*来源：首页、商品页、导航、页脚抓取 2026-07-06*
