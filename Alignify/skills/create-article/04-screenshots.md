# Step 4 — 产品截图（best-ranking）

> **范围**：**仅 Brief `Product roster` 内产品**（默认 3 款 = 3 张；不必为凑数加截图）；数量 / 独占 → [`product-coverage.md`](product-coverage.md)  
> **适用**：Tools 型 **Best / Ranking** 文章 —— `articleType: best-ranking`（含 legacy `/tools/` 场景）、`bestTools` 产品数据或 Markdown `###` 产品块中的 `![...](...)`  
> **工具**：Firecrawl `scrape` + `formats: [{ type: "screenshot", fullPage: false }]`（首屏 viewport）  
> **Meta 硬约束**：本类型 Meta title/description 含「最佳」/ `Best` 的硬约束见 [`meta.md`](meta.md) §1.3（与本步骤同步，见下文 §五）

---

## 一、核心原则（URL 选型）

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

在创建 JSON / Markdown **之前**为每款产品填写：

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

**输出 / 参数硬规则**：输出 `public/blog/{slug}/{product}.jpg`（或 legacy `/tools/` 路径）；`fullPage: false`，首屏 viewport。

**部署仓脚本（Blog 专用）**：`scripts/permanent/capture-blog-screenshots.py --slug {slug}`

**Alignify 主脚本（注册表驱动，推荐）**：在部署仓根目录执行：

```bash
# 注册表：Alignify/scripts/data/tools-screenshot-registry.json
# 环境：ALIGNIFY_DEPLOY_ROOT 指向部署仓（若不在默认路径）
python ../../clients/Alignify/scripts/ops/screenshot-tools-products.py --page git-hosting --force
```

Blog 截图条目写入 `tools-screenshot-registry.json`（`outputPath`: `blog/{slug}/{file}.jpg`），与 Tools 页共用同一 Firecrawl 流水线。规范见 [`sections.md`](sections.md) Part 3.3（**fullPage: false**，首屏 viewport）。

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key=os.environ["FIRECRAWL_API_KEY"])
resp = app.scrape(
    screenshot_url,
    formats=[{"type": "screenshot", "fullPage": False, "quality": 85}],
)
# 下载 resp.screenshot URL → public/blog/{slug}/{file}.jpg
```

**质量门控**：
- [ ] 文件 ≥ 10 KB（过小多为失败页）
- [ ] 肉眼确认页面主体是 **目标产品**（非 404、非 IDE 通用首页误截）
- [ ] Markdown / JSON 中 `imageAlt` 与 manifest 一致
- [ ] `npm run build` 前 `public/blog/{slug}/` 下文件齐全

---

## 四、Markdown 正文引用（部署仓现行）

```markdown
### 1. Cursor Origin: Agent-scale Git Forge {#cursor-origin}

![Cursor Origin 文档页截图](/blog/git-hosting/cursor-origin.jpg)

[试试 Cursor Origin](https://cursor.com/docs/origin?utm_source=kostja&utm_medium=blog)
```

路径规则：`/blog/{slug}/{file}.jpg`（对应 `public/blog/{slug}/`）；`{file}` 用 manifest `file` 名（generic 写法 `/blog/{slug}/product.jpg` 亦可）。每个 Best 产品 H3 下按此格式引用对应 jpg。

---

## 五、Meta 硬约束（Best Ranking 文章 · 与本步骤同步）

Meta title/description 含「最佳」/ `Best` 的硬约束见 [`meta.md`](meta.md) §1.3（每类型 Meta 规则）。

---

## 六、常见错误

| 错误 | 修复 |
|------|------|
| Cursor 条目截 `cursor.com` IDE 营销页 | 改截 `cursor.com/docs/origin` 或 Origin changelog |
| 全站统一 homepage | 按 §一表格逐产品选 URL |
| Meta title 缺「最佳」/ `Best` | 按 [`meta.md`](meta.md) §1.3 改 `blog-meta.ts`；H1 仍不含「最佳」 |
| 图片在 repo 外、正文已引用 | 先 Firecrawl 落盘再 merge 正文 |

---

## 检查

- [ ] 每个 Best 产品 H3 有对应 jpg
- [ ] manifest / registry 已登记（如使用 Firecrawl 流水线）
- [ ] §三质量门控四项全过（`imageAlt` 与 manifest 一致）

下一步：[`content-locale.md`](content-locale.md) Part 2（Step 05）
