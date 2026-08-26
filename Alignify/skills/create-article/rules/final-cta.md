# Final CTA（页底 SecondaryCta）规范

> **渲染**：部署仓 `src/components/SecondaryCta.tsx`  
> **数据源 SSOT**：`src/data/cta-config.json` → `slugs.{slug}.{zh|en}`  
> **缺条目时**：回退 `fallback` 通用文案（「你的产品，值得被发现。」）——**禁止**新文上线时落入 fallback。

---

## 何时写入

| 时机 | 动作 |
|------|------|
| **Step 08** Meta + Config | 与 `*-meta.ts` 注册**同批**写入 `cta-config.json` |
| **Step 09 后** | EN 版 title/description 定稿后，**补齐** `slugs.{slug}.en` |
| **改版 slug** | 若结论/主叙事大变，同步更新 CTA；小改可不动 |

---

## JSON 结构

```json
"{slug}": {
  "zh": {
    "title": "一句 punchline，≤28 字为宜",
    "description": "1–2 句，承接结论或 Author POV，≤60 字为宜",
    "cta": "开始合作"
  },
  "en": {
    "title": "One punchline sentence.",
    "description": "1–2 sentences tied to conclusion or thesis.",
    "cta": "Work with us"
  }
}
```

- **href 不写**：组件固定链 `/services`（中文自动加 `/zh` 前缀）
- **cta 按钮文案**：中文常用 `开始合作` · `获取帮助` · `看看我们怎么做`；英文常用 `Work with us` · `Get started` · `Get help`
- **slug 键**：与 md 文件名一致（如 `git-commit-attribution`），**非** URL path

---

## 写法原则

1. **承接正文，不复读 Meta description** — 用结论句、Author POV 或「我会把这篇文章收成…」的提炼  
2. **title = 可独立传播的 punchline** — 读者没读全文也能 get 核心判断  
3. **description = 下一步行动的理由** — 为什么找 Alignify / 为什么现在动  
4. **双语独立撰写** — EN 不是 ZH 直译；语气对齐 [`presentation.md`](./presentation.md)  
5. **Hub 页走 `exact`** — 仅 `/tools`、`/marketing` 等频道首页；**文章详情页一律 `slugs`**

---

## Brief 必填字段（Step 02 定稿）

在 Article Brief 增加：

```markdown
**Final CTA**（Step 08 写入 cta-config.json）:
- ZH title: …
- ZH description: …
- EN title: …
- EN description: …
- cta 按钮: zh「开始合作」/ en「Work with us」（或见上表）
```

Step 05 动笔前 Brief 里 ZH title/description **至少要有草案**；Step 09 EN 完稿后 EN 字段定稿。

---

## 验收

```powershell
node E:\clients\Alignify\scripts\ops\merge-cta-slugs.mjs --check
```

- 输出 `Missing: 0` → Pass  
- 任一 slug 缺失 → Gate C **BLOCK**

---

## 常见错误

| 错误 | 正确 |
|------|------|
| 新文上线无 `slugs.{slug}` | Step 08 与 meta 同批注册 |
| 用 fallback 通用「好产品输的从来不是质量」 | 每篇定制 punchline |
| title 复制 Meta title | 从结论/POV 提炼 |
| EN 逐句翻译 ZH CTA | 独立重写 |
| slug 键写错（如 `git-commit`） | 与 `{slug}.md` 文件名一致 |

见 [`common-errors.md`](./common-errors.md) **E43**。

---

*final-cta · v1.0 · 2026-08-27*
