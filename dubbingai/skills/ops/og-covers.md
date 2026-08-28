# Dubbing AI OG 封面图生成流程

> 为 dubbingai.io/blog 各文章生成 **1200×630** 专属 OG 图。  
> **默认 APINEED API** · **英文 only** · 对照 [Alignify OG 流程](../../../Alignify/skills/ops/og-covers.md)。

---

## 1. 三阶段工作流

```
阶段 0 — LLM 文章分析（新文/重生成推荐）
  读取 dubbingai/blog/*-{slug}-*.md 或 cms-export/{slug}.md
    → analyze-og-page.py（GPT-4o）
    → data/og-briefs/blog/{slug}/brief.json
    → visual_anchors + anti_patterns + composition
    → --merge-registry 写入 og-prompt-registry.json

阶段 A — 生图（APINEED 默认）
  generate-og-cover.py（注入 brief + QUALITY 指令）
    → APINEED gpt-image-2 (high / jpeg)
    → 居中裁切 → 严格 1200×630 WebP
    → blog/images/og/{slug}/{slug}-og-en.webp
    → 目视验收 → registry status=approved

阶段 B — 部署（可选）
  --deploy 写入 {DUBBINGAI_DEPLOY_ROOT}/public/blog/images/og/
  或手动上传 CMS
```

**一键分析+生成**：`generate-og-cover.py --analyze-first`（需 `OPENAI_API_KEY` + `APINEED_API_KEY`）

---

## 2. 文件路径

| 用途 | 路径 |
|------|------|
| **OG 成品（默认）** | `blog/images/og/{slug}/{slug}-og-en.webp` |
| **元数据** | `blog/images/og/{slug}/{slug}-og-en.meta.json` |
| **Prompt / brief** | `data/og-prompt-registry.json` · `data/og-briefs/` |
| **规则** | `data/og-cover-rules.md` |

---

## 3. 视觉风格

editorial-collage 默认 — 纸拼贴 zine 封面感 + gaming/streaming 年轻调性 + cyan→indigo 品牌点缀。

完整规则见 **[data/og-cover-rules.md](../../data/og-cover-rules.md)**。

---

## 4. 模型与参数

| 项 | 值 |
|----|-----|
| **Provider** | APINEED（唯一默认） |
| **Model** | `gpt-image-2` |
| **Quality** | `high` |
| **API size** | `1536x1024`（fallback `1024x1024`） |
| **最终尺寸** | **1200×630** WebP（APINEED：top-aligned trim；fal：center crop） |
| **APINEED raw** | high → `1536x1024` · prompt 含 CROP SAFE ZONE · 标题 10%/8% 安全边距 |

---

## 5. 执行步骤

### 5.1 环境

```powershell
$env:APINEED_API_KEY = "your-apineed-key"
pip install pillow
```

可选分析阶段：

```powershell
$env:OPENAI_API_KEY = "your-openai-key"
```

密钥也可放 `dubbingai/.secrets/apineed-key`（或复用 `Alignify/.secrets/apineed-key`）。

### 5.2 分析文章（新文推荐）

```powershell
python E:\clients\dubbingai\scripts\ops\analyze-og-page.py `
  --slug best-ai-voice-changer --merge-registry
```

### 5.3 查看 registry

```powershell
python E:\clients\dubbingai\scripts\ops\generate-og-cover.py --list
```

### 5.4 预览 prompt

```powershell
python E:\clients\dubbingai\scripts\ops\generate-og-cover.py `
  --slug best-ai-voice-changer --dry-run
```

### 5.5 生成

```powershell
python E:\clients\dubbingai\scripts\ops\generate-og-cover.py `
  --slug best-ai-voice-changer
```

输出：`E:\clients\dubbingai\blog\images\og\best-ai-voice-changer\best-ai-voice-changer-og-en.webp`

### 5.6 批量生成（Track S 四篇）

```powershell
python E:\clients\dubbingai\scripts\ops\batch-generate-og-covers.py `
  --slugs best-ai-voice-changer,how-to-change-google-assistant-voice,how-to-change-your-voice,dubbing-ai-vs-voicemod `
  --skip-existing
```

### 5.7 写入部署仓（可选）

```powershell
$env:DUBBINGAI_DEPLOY_ROOT = "E:\path\to\dubbingai-deploy"
python E:\clients\dubbingai\scripts\ops\generate-og-cover.py `
  --slug best-ai-voice-changer --deploy
```

---

## 6. Registry

路径：`data/og-prompt-registry.json`

已预置 Track S 四篇（status=pending）。验收通过后改 `status: "approved"`。

---

## 7. 质量检查

- [ ] **1200×630** WebP（脚本输出含 verified 字样）
- [ ] 英文标题正确
- [ ] 仅标题+副标题有字
- [ ] 视觉与文章主题强相关（Assistant 文 ≠ 游戏耳机 hero）
- [ ] 仅 1 个品牌标记

---

## 8. 关联

- [data/og-cover-rules.md](../../data/og-cover-rules.md)
- [dubbingai-brand-visual.md](../../dubbingai-brand-visual.md)（品牌色）
- Alignify 对照：[Alignify/skills/ops/og-covers.md](../../../Alignify/skills/ops/og-covers.md)
- [dubbingai-blog-article SKILL](../dubbingai-blog-article/SKILL.md) Phase 6 OG 步骤
