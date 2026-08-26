# 产品截图 URL 规则（Best Tools / Ranking 文章）

> **版本**：v1.0 · 2026-08-21  
> **适用范围**：Tools 型 **Best / Ranking** 文章（`bestTools` 或 Markdown `###` 产品块中的 `![...](...)`）  
> **工具**：Firecrawl `scrape` + `formats: [{ type: "screenshot", fullPage: true }]`

---

## 一、核心原则

**截图必须对应该条目所介绍的产品/能力页，禁止一律截厂商首页。**

| 厂商形态 | 截图 URL 选哪 | 示例 |
|----------|--------------|------|
| **单一产品线** | 官网首页或产品 landing 即可 | Graphite → `graphite.com` |
| **多产品平台** | 该条目对应的 **产品文档 / 功能页 / changelog** | Cursor **Origin** → `cursor.com/docs/origin`（**不是** `cursor.com` IDE 首页） |
| **Incumbent + 能力叠加** | 能力/feature 页优先；整页讲 forge 本体时可用首页 | GitHub Agent HQ → `github.com/features/copilot` |
| **博客发布的产品** | 产品 announcement / docs 页 | Zed Delta → `zed.dev/blog/introducing-delta` |

**imageAlt 必须如实描述所截页面**（含「文档页」「功能页」等），禁止统一写「homepage screenshot」当实际截的是 docs。

---

## 二、Manifest 模板（写文前先填）

在创建 JSON / Markdown **之前** 为每款产品填写：

```yaml
# capture-manifest.yaml（示例：git-hosting）
slug: git-hosting
images_dir: public/blog/git-hosting/

products:
  - file: cursor-origin.jpg
    name: Cursor Origin
    screenshot_url: https://cursor.com/docs/origin   # 产品页，非 IDE 首页
    link_url: https://cursor.com/docs/origin
    image_alt_zh: Cursor Origin 文档页截图
    image_alt_en: Cursor Origin documentation page screenshot

  - file: github-agent-hq.jpg
    name: GitHub
    screenshot_url: https://github.com/features/copilot
    link_url: https://github.com/features/copilot
    image_alt_zh: GitHub Copilot 与 Agent 功能页截图
    image_alt_en: GitHub Copilot and agent features page screenshot
```

---

## 三、Firecrawl 批量截图

**环境**：`pip install firecrawl-py`。API Key 优先读 `FIRECRAWL_API_KEY`；未设置时使用 Alignify 既有 fallback（与 `scripts/ops/screenshot-tools-products.py` 一致）。

**部署仓脚本（Blog 专用）**：`scripts/permanent/capture-blog-screenshots.py --slug {slug}`

**Alignify 主脚本（注册表驱动，推荐）**：在部署仓根目录执行：

```bash
# 注册表：Alignify/scripts/data/tools-screenshot-registry.json
# 环境：ALIGNIFY_DEPLOY_ROOT 指向部署仓（若不在默认路径）
python ../../clients/Alignify/scripts/ops/screenshot-tools-products.py --page git-hosting --force
```

Blog 截图条目写入 `tools-screenshot-registry.json`（`outputPath`: `blog/{slug}/{file}.jpg`），与 Tools 页共用同一 Firecrawl 流水线。规范见 `skills/create-article/rules/sections/best-tools.md` §5.3（**fullPage: false**，首屏 viewport）。

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key=os.environ["FIRECRAWL_API_KEY"])
resp = app.scrape(
    screenshot_url,
    formats=[{"type": "screenshot", "fullPage": True, "quality": 85}],
)
# 下载 resp.screenshot URL → public/blog/{slug}/{file}.jpg
```

**质量门控**：
- [ ] 文件 ≥ 10 KB（过小多为失败页）
- [ ] 肉眼确认页面主体是 **目标产品**（非 404、非 IDE 通用首页误截）
- [ ] Markdown / JSON 中 `imageAlt` 与 manifest 一致
- [ ] `npm run build` 前 `public/blog/{slug}/` 下文件齐全

---

## 四、Markdown 正文引用格式（部署仓现行）

```markdown
### 1. Cursor Origin: Agent-scale Git Forge {#cursor-origin}

![Cursor Origin 文档页截图](/blog/git-hosting/cursor-origin.jpg)

[试试 Cursor Origin](https://cursor.com/docs/origin?utm_source=kostja&utm_medium=blog)
```

路径规则：`/blog/{slug}/{file}.jpg`（对应 `public/blog/{slug}/`）。

---

## 五、Best Ranking 文章 Meta 硬约束（与本步骤同步）

Ranking / Best 型文章 **Meta title / description 必须含「最佳」/ `Best`**（见 [`meta-requirements.md`](./meta.md)）：

| 要素 | 中文 | 英文 |
|------|------|------|
| Meta title | `最佳{品类}（2026）：{产品A、B}等 \| Alignify` | `Best {Category} (2026): {A, B} & More \| Alignify` |
| Meta description | 列举 2–3 个代表产品 + 「探索2026年最佳…」 | `Explore the best … in 2026: …` |
| H1（frontmatter `title`） | **不写**「最佳」、不写年份 | 同左 |
| Best 榜单 H2 | `## 2026 年最好的 {品类}` | `## Best {Category} in 2026` |

---

## 六、常见错误

| 错误 | 修复 |
|------|------|
| Cursor 条目截 `cursor.com` IDE 营销页 | 改截 `cursor.com/docs/origin` 或 Origin changelog |
| 全站统一 homepage | 按 §一表格逐产品选 URL |
| Meta title 缺「最佳」/ `Best` | 改 `blog-meta.ts`，H1 仍不含「最佳」 |
| 图片在 repo 外、正文已引用 | 先 Firecrawl 落盘再 merge 正文 |

---

*product-screenshot-pages · create-tools-article · 2026-08-21*
