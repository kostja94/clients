# 2mv — Internal Links Rules

> 加载时机：Phase 3（Outline 内链规划）· Phase 4（Draft 内链执行）· Phase 5（SelfCheck 内链复核）
> 主文件：SKILL.md §3 各 Phase 指针

---

## R1 — 内链数量

| 规则 | 标准 |
|------|------|
| **blog 互链** | ≥2（全文上下文分布） |
| **product page** | 1–2（自然嵌入正文，非每段推） |
| **外链** | 2–6（权威来源；竞品用 `rel="nofollow noopener"`） |

---

## R2 — 锚文本标准

| 规则 | 标准 |
|------|------|
| 描述性 | "our guide to going viral on tiktok"、"how teams find viral content ideas" |
| 禁止 | "click here"、"learn more"、"read more" |
| 竞品外链 | HTML `<a href="URL" rel="nofollow noopener">Company Name</a>`（与其他项目文章一致） |
| 站内内链 | Markdown `[描述性锚文本](/insights/{slug})`（与其他项目文章一致） |

---

## R3 — Canonical Concept 引用

每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + link：

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| What is 2mv / 品牌定位 | `what-is-2mv` | 品牌定义 canonical；他文引用 1–2 句 + link |
| How to find viral videos | `how-to-find-viral-videos` | Hub 完整定义；spoke 引用 1–2 句 + link |
| Find viral content ideas | `how-to-find-viral-content-ideas-before-they-peak`（官网） | 官网 canonical；新文不得重写完整流程 |

---

## R4 — Hub-Spoke 双向互链

- **Hub**（`how-to-find-viral-videos`）→ 链接所有 spoke（或主要 spoke）
- **Spoke** → 必须回链 hub
- **Spoke ↔ Spoke**：语义相关时互链（如 what-makes-a-video-go-viral ↔ how-to-find-viral-videos-on-instagram）

---

## R5 — 禁止链接

- 未上线产品页（G6）：`/pricing`、`/service`、`/niches/{slug}`
- Forthcoming 页面（正文核心流程 ≥0；脚注 ≤1）
- `rel="dofollow"` 的竞品链接（必须 `nofollow noopener`）
- 站内路径全部使用 `/insights/{slug}`（2mv 博客前缀，非 `/blog/`）

---

## 内链验证清单（Phase 5 对照）

- [ ] ≥2 blog 互链（全文上下文分布，非集中末尾）
- [ ] Spoke 回链 hub（如适用）
- [ ] 锚文本描述性（无 "click here"）
- [ ] 竞品外链 `rel="nofollow noopener"`（HTML 形式）
- [ ] 无未上线页面链接（对照 project-config.md §2 白名单）
- [ ] Forthcoming ≤1（仅脚注）
- [ ] Canonical 概念 1–2 句 + link（非重定义）

---

*internal-links · v1.0.0 · 2026-08-14 · 2mv 定制*
