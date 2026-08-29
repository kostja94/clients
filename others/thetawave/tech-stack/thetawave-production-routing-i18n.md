# 反向代理下的多语种路径（`/fr/...` 等）

本文是 [thetawave-production-routing.md](./thetawave-production-routing.md) 的补充：**主域 `thetawave.ai` 已通过 Rewrite/反向代理把英文路径**（如 `/features/notes-generator`、`/use-cases/for-medical-students`）**转到营销子站（Next.js on Vercel）时，带语言前缀的 URL**（如 [https://thetawave.ai/fr/use-cases/for-medical-students](https://thetawave.ai/fr/use-cases/for-medical-students)）**应如何配置与实现**。

---

## 1. 核心结论（先读这段）

| 要点 | 说明 |
|------|------|
| **代理层要「原样转发语言前缀」** | 用户访问的路径是 `/fr/use-cases/...`，上游应请求 **`https://<营销子站>/fr/use-cases/...`**，而不是仍请求 `/use-cases/...` 再指望应用猜语言。 |
| **子站必须先有对应路由** | 若 Vercel 上的 Next 应用 **没有** `app/[locale]/use-cases/...`（或等价结构），仅加代理规则会得到 **404**。多语种页面由 **Next 的 i18n 路由 + 文案** 实现，代理只负责把路径指过去。 |
| **英文与每种语言各写一组规则（或一条宽规则）** | 与 [thetawave-production-routing.md](./thetawave-production-routing.md) §5、§9 中 `/use-cases/:path*` 同理，对 `/fr/...` 增加 **平行** 的 rewrites。 |

**一句话**：多语种不是「代理的特殊情况」，而是 **多了一组以 `/<locale>/` 为前缀的 URL**；配置方式与英文路径相同，**路径前缀必须与子站真实路由一致**。

---

## 2. 前置检查：子站（thetawave-three）是否已支持 `/fr/...`

在浏览器直接打开（无需经过主域）：

- `https://thetawave-three.vercel.app/fr/use-cases/for-medical-students`

**若 404**：先在 **营销子站仓库** 完成其一：

- **路径型 i18n**（常见）：`src/app/[locale]/use-cases/[slug]/page.tsx` + `middleware` 或 `next-intl` 等，保证 `fr`、`en` 等与线上一致；或  
- **仅默认语言无前缀**：若线上法文必须是 `/fr/...`，子站也需 **显式提供** `fr` 段，不能只有 `rewrite` 把 `/fr` 剥掉（除非中间层统一剥前缀并设 `Accept-Language` / cookie，复杂度更高，不推荐作为首选）。

**若 200 且内容为法文**：说明子站已就绪，只需在主域 **补 rewrites**（见下节）。

---

## 3. 主域配置：与英文规则「平行」增加 `/<locale>`

配置位置仍遵循 [thetawave-production-routing.md](./thetawave-production-routing.md) **§4**：写在 **托管 `thetawave.ai` 的那一层**（主站 `vercel.json`、Cloudflare、Nginx 或主站 `next.config.ts` 的 `rewrites`）。

### 3.1 方案 A：按语言一条「宽」前缀（适合营销页都在子站）

在已有英文规则之外，对每个已上线的语言前缀增加 **catch-all**，把 **`/<locale>` 下整棵树** 交给子站（**仅当** 主站在该前缀下没有其它产品路由时可用）。

**Vercel `vercel.json` 示例（仅演示 `fr`）**

```json
{
  "rewrites": [
    {
      "source": "/fr/:path*",
      "destination": "https://thetawave-three.vercel.app/fr/:path*"
    }
  ]
}
```

- 若还有 `de`、`es` 等，各加一条 `"/de/:path*"` → `".../de/:path*"`。  
- **风险**：若主站将来在 `/fr/` 下挂了非营销应用路由，会与 catch-all 冲突，需改为 **3.2 窄规则** 或调整匹配顺序。

### 3.2 方案 B：与英文表结构一致，逐前缀列举（更安全）

与 [thetawave-production-routing.md](./thetawave-production-routing.md) §5 中英文明细对齐，为法文（示例）逐条写：

```json
{
  "rewrites": [
    {
      "source": "/fr/use-cases",
      "destination": "https://thetawave-three.vercel.app/fr/use-cases"
    },
    {
      "source": "/fr/use-cases/:path*",
      "destination": "https://thetawave-three.vercel.app/fr/use-cases/:path*"
    },
    {
      "source": "/fr/features",
      "destination": "https://thetawave-three.vercel.app/fr/features"
    },
    {
      "source": "/fr/features/:path*",
      "destination": "https://thetawave-three.vercel.app/fr/features/:path*"
    }
  ]
}
```

按子站实际存在的 **法语路径** 继续追加（如 `/fr/pricing`、`/fr/knowledge-hub/:path*` 等），**不要遗漏** 与英文已代理路径对应的 **`/fr/...` 版本**。

### 3.3 主站为 Next.js：`next.config.ts` 中的 `rewrites`

与 [thetawave-production-routing.md](./thetawave-production-routing.md) §9 相同写法，增加 `fr`（及他语）条目即可：

```ts
async rewrites() {
  return [
    // 已有英文 …
    {
      source: "/fr/use-cases/:path*",
      destination: "https://thetawave-three.vercel.app/fr/use-cases/:path*",
    },
    {
      source: "/fr/features/:path*",
      destination: "https://thetawave-three.vercel.app/fr/features/:path*",
    },
  ];
}
```

根路径法文首页若为 `/fr` 或 `/fr/`，需单独各写一条（视子站路由而定）。

---

## 4. `/_next` 与静态资源（与语种无关）

多语种页面引用的仍是 **`/_next/static/...`**，**路径通常不带 `fr`**。主域若已对英文营销页做了 `/_next` 转发，**一般无需** 为每种语言再复制一套；若尚未处理，见 [thetawave-production-routing.md](./thetawave-production-routing.md) **§10.3**，避免出现「法文页能打开但无样式」。

---

## 5. 默认语言 URL 策略（避免重复与混乱）

常见两种产品形态：

| 策略 | 主域示例 | 代理时注意 |
|------|----------|------------|
| **默认语无前缀** | 英文：`/use-cases/...`；法文：`/fr/use-cases/...` | 英文用现有规则；法文用 §3。 |
| **所有语言都有前缀** | `/en/...`、`/fr/...` | 需为 **`/en` 与 `/fr` 都** 配置 rewrites，且子站路由一致。 |

与 **canonical、`hreflang` alternate** 保持一致（避免同一内容多个 URL 无标注）；细节在营销子站 `metadata` / sitemap 中维护，代理不改变 URL，只转发。

---

## 6. 不建议的捷径（除非团队明确接受代价）

| 做法 | 问题 |
|------|------|
| 主域只代理 `/use-cases/...`，用法文 cookie 在子站「切换语言」但 URL 仍是英文 | URL 与分享链接失去语言信号，SEO/广告落地页易乱；与当前线上 `/fr/...` **不一致**。 |
| 主域 302 到 `*.vercel.app/fr/...` | 与 [thetawave-production-routing.md](./thetawave-production-routing.md) 推荐的 **域名统一** 目标冲突。 |
| 仅在主域做 `redirect`：`/fr/use-cases` → `/use-cases?lang=fr` | 若未在子站实现 query 驱动渲染，仍可能错语言或 404。 |

---

## 7. 验证清单（在 §11 基础上增加）

1. `https://thetawave.ai/fr/use-cases/for-medical-students` 地址栏不变，**内容与** `https://thetawave-three.vercel.app/fr/use-cases/for-medical-students` **一致**。  
2. 法文页 **样式与脚本 200**（检查 `/_next/*`）。  
3. 站内链：法文页中的同站链接应指向 **`/fr/...`** 或相对路径，避免链到无语言前缀的英文页（由 Next `Link` / `next-intl` 配置保证）。  
4. `metadataBase`、canonical 以 **https://thetawave.ai** 为准（参见 [thetawave-production-routing.md](./thetawave-production-routing.md) §10.1）。

---

## 8. 与本仓库的关系

- 本文与 [thetawave-production-routing.md](./thetawave-production-routing.md) 一样，**描述架构与配置位置**；实际 `rewrites` 仍在 **主域托管仓库** 或边缘网关。  
- **子站 Next 的 `[locale]` 路由与翻译资源** 在 **thetawave-three 代码仓库** 中实现；本 `others/thetawave` 目录为营销/项目文档（归档），若子站路由变更，请同步更新两文路径示例。

---

## 9. 参考

- 主文：[thetawave-production-routing.md](./thetawave-production-routing.md)  
- 线上法文用例页示例：[thetawave.ai/fr/use-cases/for-medical-students](https://thetawave.ai/fr/use-cases/for-medical-students)  
- 线上功能页示例：[thetawave.ai/features/notes-generator](https://thetawave.ai/features/notes-generator)

---

*文档版本：与主路由文档配套；新增语言时复制 §3 规则模板并核对子站是否已有对应 `/<locale>` 路由。*
