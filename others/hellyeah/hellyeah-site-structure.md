# Hellyeah 网站结构（IA）

> **职责**：层级、优先级、内链；**路径权威** → [hellyeah-others.md](./hellyeah-others.md) §1（2026-06-02 全站 + sitemap.xml）。  
> 关联：[hellyeah.md](./hellyeah.md) | [hellyeah-keywords.md](./hellyeah-keywords.md) | [hellyeah-use-cases.md](./hellyeah-use-cases.md)

**Last updated**: 2026-06-02

---

## 1. 观测导航（官网）

**顶栏产品**：CLI beta · Platforms（`/aima` `/forge` `/mutation` `/deja-vu`）· Capabilities（6）· Solutions（5）· Customers · Manifesto · About · Careers · Contact · **Request a demo** → `/demo`

**Footer Arena**：`/for/mobile-apps` … `/for/edutech`（7 个，标签名与 nav 一致）

**Footer 合规**：Privacy · Terms · **Trust Center** → `/security`（非 `/trust-center`）

**语言**：页脚多语言切换存在；具体 hreflang 以工程为准。

---

## 2. Must Have（均已上线）

| 优先级 | 路径 | 目的 |
|--------|------|------|
| P0 | `/` | CLI + RCLL + 案例 + CTA |
| P0 | `/aima` `/forge` `/mutation` `/deja-vu` | 四平台 |
| P0 | `/demo` | 主转化 |
| P0 | `/capabilities/*`（6） | 能力 SEO |
| P1 | `/customers` + `/customers/{slug}` | 社会证明 |
| P1 | `/security` | Trust |
| P1 | `/manifesto` `/about` | 品牌与使命 |
| P2 | `/for/*`（7） | 垂直 Arena |
| P2 | `/solutions/*`（5） | Outcome 落地 |
| P2 | `/brand` `/contact` `/careers` | 支持页 |

---

## 3. Great to Have / 待确认

| 路径 | 状态 |
|------|------|
| `/blog` | ⚠️ 旧文档有；**当前 sitemap 未收录** |
| `/login` | ⚠️ 待工程确认 |
| `/hellyeah-explained` | ⚠️ 规划教育页；sitemap 无 |
| `/alternatives/*` | 规划竞品拦截 |
| `/integrations` | ❌ 404（首页用 `#platform-trust`） |

---

## 4. 技术 SEO

- 首页 `<title>`：**Hellyeah · npm install your growth engine**（非旧版「AI Growth Engine for Ambitious Companies」alone）  
- Capabilities / Solutions / Arena 页有独立 title 与面包屑（Home > Capabilities > …）  
- 评估重复 DOM / CWV 仍以 Lighthouse 为准。

---

## 5. 内链（推荐）

```
/ → /aima + /capabilities + /demo
/aima → /capabilities/performance-marketing + /demo
/capabilities/seo-geo → /solutions/improve-marketing-roi（按需）
/for/{arena} → 2+ capabilities + /customers/{相关案例}
/manifesto → /about → /customers
```

Arena 页底已有 Capabilities / AIMA / Forge / Mutation 三层说明。

---

## 6. Breadcrumb 建议（与线上一致）

- `Home > Capabilities > {Capability}`  
- `Home > Arena > {Vertical}`（线上文案为 Arena）  
- 平台页无独立 breadcrumb 块时：`Home > Platforms > AIMA`（可选增强）

---

## 7. 已废弃路径（勿链、勿写 sitemap）

| 废弃 | 替代 |
|------|------|
| `/platforms/aima` 等 | `/aima` 等 |
| `/trust-center` | `/security` |
| `/about-us` | `/about` |
| `/arenas/{slug}` | `/for/{slug}` |
| `/capabilities/geo` | `/capabilities/seo-geo` |
| `/capabilities/lifecycle` | `/capabilities/lifecycle-automation` |
| `/capabilities/influencer` | `/capabilities/influencer-marketing` |
