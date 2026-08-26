# Alignify OG 封面图生成流程

> 为 alignify.co 各频道页面生成 **1200×630** 专属 OG 图，与正文 BestTools **产品截图**分离。  
> **EN / ZH 分开出图**：英文页只用英文画布，中文页只用中文画布。

---

## 1. 三阶段工作流（v4 — 先分析后生图）

```
阶段 0 — LLM 页面分析（必做，新页/重生成）
  读取 deploy 仓 content/{section}/{locale}/{slug}.md
    → analyze-og-page.py（GPT-4o）
    → data/og-briefs/{section}/{slug}/brief.json
    → visual_anchors + anti_patterns + composition
    → --merge-registry 写入 og-prompt-registry.json

阶段 A — 直写部署仓（唯一存储）
  generate-og-cover.py（注入 brief + QUALITY 指令）
    → fal GPT Image 2
    → {DEPLOY_ROOT}/public/{section}/{slug}/{slug}-og-{locale}.webp
    → 目视验收 → registry status=approved

阶段 B — 注册上线（可选）
  migrate-og-covers.py --no-register  # 仅历史 staging move，新图不需要
  或手动 / migrate 写入 OG_LOCALE_READY
```

**一键分析+生成**：`generate-og-cover.py --analyze-first`（需 `OPENAI_API_KEY`）

**Section 视觉签名**：`data/og-section-signatures.json`（GEO ≠ SEO 等硬规则）

---

## 1b. 单仓原则

**OG 图只存一处：部署仓 `public/`。** 禁止 copy 到两边各留一份。

| 操作 | 说明 |
|------|------|
| 默认生成 | 直写 `{DEPLOY_ROOT}/public/...` |
| `--to-staging` | 仅临时预览，用完 move 或删 |
| `migrate-og-covers.py` | **shutil.move**，源文件删除；`--purge-duplicates` 清遗留 staging |

上下文仓保留：registry · brief · 脚本 · 规则文档。**不存成品 webp**（`assets/og/` 已废弃）。

---

## 2. 文件路径

| 用途 | 路径 |
|------|------|
| **OG 成品（唯一）** | `{DEPLOY_ROOT}/public/{section}/{slug}/{slug}-og-en.webp` · `{slug}-og-zh.webp` |
| **品牌 logo（生成叠加用）** | `assets/brand/icon-192x192.png` |
| **Prompt / brief（上下文仓）** | `data/og-prompt-registry.json` · `data/og-briefs/` |

**规则**
- 不再把 `flux.jpg` 等产品截图当 OG
- 产品截图仍放 `public/tools/{slug}/{product}.jpg`，仅用于正文 BestTools

---

## 3. 视觉风格（v3）

完整规则见 **[data/og-cover-rules.md](./data/og-cover-rules.md)**。

### 3.1 editorial-collage（默认）

纸拼贴 zine 封面感 + **PPT 级文字量** + **页面强相关视觉**。

| 原则 | 说明 |
|------|------|
| **R1 页面强相关** | `composition` 写 2–3 个与 slug 直接相关的视觉，禁止 generic 装饰 |
| **R2 文字适中** | 画布仅 headline + 可选一行 subtitle；禁止排名、脚注、slogan |
| **R3 品牌** | 三选一（Kostja / Alignify / Logo），无缝融入，无双色块徽章 |

registry 字段：`headline` · `headline_line2` · `subtitle`（宜短）· `composition`（英文、纯视觉描述）· `author`（默认 Kostja）

### 3.2 swiss-grid（备选）

极简瑞士网格 + 大留白，适合纯概念页。见 `style: "swiss-grid"`。

---

## 4. 模型与参数

| 场景 | 模型 | fal 端点 |
|------|------|----------|
| **含标题 OG（默认）** | GPT Image 2 | `openai/gpt-image-2` |
| 无字纯视觉 hero | flux / Codex skills | 见 aesthetic-references |

**GPT Image 2 参数**

```json
{
  "prompt": "...",
  "image_size": { "width": 1216, "height": 632 },
  "quality": "high",
  "num_images": 1,
  "output_format": "jpeg"
}
```

生成后居中裁切为 **1200×630**。

**语言规则（硬约束）**
- `locale=en` → prompt 内全部可见文字英文
- `locale=zh` → prompt 内全部可见文字简体中文（品牌 Alignify 除外）

---

## 5. 执行步骤

### 5.1 环境

```powershell
$env:FAL_KEY = "your-fal-key"
$env:ALIGNIFY_DEPLOY_ROOT = "E:\自有部署项目\alignify production"
pip install pillow
```

### 5.2 分析页面（新页必做）

```powershell
$env:OPENAI_API_KEY = "your-openai-key"
python E:\clients\Alignify\scripts\ops\analyze-og-page.py `
  --section marketing --slug geo --merge-registry
```

输出：`data/og-briefs/marketing/geo/brief.json`

### 5.3 查看 registry

```powershell
python E:\clients\Alignify\scripts\ops\generate-og-cover.py --list
```

### 5.4 预览 prompt

```powershell
python E:\clients\Alignify\scripts\ops\generate-og-cover.py `
  --slug image-generator --locale en --dry-run
```

### 5.5 生成（默认 → 部署仓 public/）

```powershell
python E:\clients\Alignify\scripts\ops\generate-og-cover.py `
  --slug image-generator --locale en

python E:\clients\Alignify\scripts\ops\generate-og-cover.py `
  --slug image-generator --locale zh
```

输出：`E:\自有部署项目\alignify production\public\tools\image-generator\image-generator-og-en.webp`

验收通过后 registry 改 `status: "approved"`。上线前注册 `OG_LOCALE_READY`：

```powershell
python E:\clients\Alignify\scripts\ops\migrate-og-covers.py `
  --slug image-generator --locale en
# migrate 对新图主要是注册；文件已在 deploy 则跳过
```

**临时预览到上下文仓**（勿长期保留）：

```powershell
python E:\clients\Alignify\scripts\ops\generate-og-cover.py `
  --to-staging --slug image-generator --locale en
```

### 5.6 审计覆盖

```powershell
node E:\clients\Alignify\scripts\audit\audit-og-coverage.mjs
node E:\clients\Alignify\scripts\audit\audit-og-coverage.mjs --both   # 查 staging 遗留副本
```

---

## 6. Registry

路径：`data/og-prompt-registry.json`

每条记录字段：
- `section`：`tools` | `blog` | `seo` | `marketing` | `insights` | `events`
- `slug`
- `locale`：`en` | `zh`
- `headline` / `headline_line2` / `subtitle`（一行，宜短）
- `composition` — 2–3 个页面相关视觉，英文，**不含**额外 on-image 文字
- `author` — 默认 `Kostja`（脚本左下叠加，不由 AI 渲染）
- `accent` · `status`

---

## 7. 部署仓接线

`migrate-og-covers.py` 对历史 staging 用 **move**（非 copy）；并可更新 `src/lib/og-image-path.ts` 中的 `OG_LOCALE_READY`。

OG 解析优先级：

1. `public/{section}/{slug}/{slug}-og-{locale}.webp`（已在 `OG_LOCALE_READY` 注册）
2. 旧 `*-article-images.ts` 产品截图映射（过渡期）
3. 站点默认 `og-image.png`

生成并验收后，把 `{section}/{slug}:{locale}` 加入 `OG_LOCALE_READY`（**由 migrate-og-covers.py 自动完成**）。

---

## 8. 质量检查

- [ ] 1200×630 WebP q≥90
- [ ] 语言正确（EN/ZH 分图）
- [ ] 仅标题+副标题有字，无多余文字块（PPT 原则）
- [ ] 视觉与页面主题强相关
- [ ] 仅 1 个品牌标记，融入自然（非贴纸感）
- [ ] `audit-og-coverage.mjs` 通过

---

## 9. 安全

- **FAL_KEY** 只放环境变量，禁止写入 git
- 切勿在 markdown / registry 中保存 API key

---

## 10. 关联文档

- [scripts/README.md](./scripts/README.md)
- [knowledge/design/aesthetic-references.md](./knowledge/design/aesthetic-references.md)
- 2mv 参考流程：`../2mv/blog/images/skills/ops/og-covers.md`
