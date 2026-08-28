# Dubbing AI OG 封面规则

> 脚本 SSOT：`scripts/ops/generate-og-cover.py` · registry：`data/og-prompt-registry.json`  
> 对照 Alignify：`Alignify/skills/ops/og-covers.md`

---

## 1. 三条硬规则

### R1 — 与文章强相关

每张 OG 的视觉主体必须让人一眼看出「这篇讲什么」，不能是通用 voice-tech 装饰。

| 文章类型 | 应出现的视觉（示例） |
|----------|---------------------|
| Voice changer 选型 hub | 游戏耳机 + 波形、preset 头像网格 |
| Google Assistant 文 | 手机 Assistant 语音设置 UI（非游戏耳机 hero） |
| Live mic How-to | 麦克风路由流程图（virtual cable → app） |
| Alternative 对比 | 公平左右对比面板（无可读竞品 logo） |
| Soundboard / meme | 音效 tile 网格 + 游戏/梗视觉 |

### R2 — 文字像 PPT，适中即可

AI 画布上只允许 registry 里的标题文字，其余用图表达。

| 允许 | 禁止 |
|------|------|
| `headline` + 可选 `headline_line2` | 排名列表、App 名、脚注、slogan |
| 可选一行 `subtitle` + 可选 `tagline` | 箭头旁标签、多张小卡片说明文字 |

**作者名 `Kostja` 不由 AI 渲染**，由脚本后期叠加。

### R3 — 品牌标记（三选一）

**Kostja · Dubbing AI 字标 · Logo** 不由 AI 渲染，脚本后期叠加 —— **每张图只选其中一个**。

| 模式 | 样式 |
|------|------|
| `kostja` | 小号 byline，半透明纸纹底 |
| `dubbingai` | 小号 「Dubbing AI」字标 |
| `logo` | 小号 logo（~44px），soft shadow |

品牌色：cyan `#22D3EE` → indigo `#6366F1` 渐变点缀。

### R0 — 先 LLM 分析（推荐）

生图前产出 `data/og-briefs/blog/{slug}/brief.json`：
- `visual_anchors` — 必选视觉，#1 为 HERO
- `anti_patterns` — 禁止出现的错误隐喻
- `locales.en.composition` — 英文视觉描述

工具：`scripts/ops/analyze-og-page.py`（GPT-4o，需 `OPENAI_API_KEY`）

---

## 2. 尺寸与 API（硬约束）

| 项 | 值 |
|----|-----|
| **最终输出** | **1200×630** WebP q≥92 |
| **API** | **APINEED**（默认，`gpt-image-2`） |
| **生成参数** | `quality=high`, `output_format=jpeg`, `n=1` |
| **后处理** | 居中裁切 → 验证 `img.size == (1200, 630)` → 叠加品牌 → 存 WebP |

APINEED 请求尺寸为 `1536x1024`（high）或 `1024x1024`（low/fallback），脚本 **top-aligned trim** 裁切为 **1200×630**。

| 阶段 | 说明 |
|------|------|
| **Prompt** | 自动注入 `APINEED CROP SAFE ZONE`：标题区 10% top / 8% left 安全边距；主体避开底部将被裁掉的 band |
| **裁切** | APINEED 用 `top` bias（保留顶部标题，裁底部）；fal 用 `center`（1216×632 ≈ OG 比例） |
| **质量** | 默认 `--quality high`；禁止依赖 `OG_APINEED_QUALITY=low` 除非调试 |

**禁止**：标题贴边、两行超长 headline 超出左 48% 宽度 — 会导致裁切后或缩略图下「出界」。

---

## 3. Registry 字段

```json
{
  "section": "blog",
  "slug": "best-ai-voice-changer",
  "locale": "en",
  "style": "editorial-collage",
  "accent": "dubbing-gradient",
  "author": "Kostja",
  "headline": "BEST AI VOICE CHANGERS",
  "headline_line2": "(2026)",
  "subtitle": "Gaming · Discord · Streaming · Real-Time",
  "composition": "Visual-only collage: (1) headset + waveform HERO. (2) preset grid. (3) Discord mock.",
  "status": "pending"
}
```

| accent | 说明 |
|--------|------|
| `dubbing-cyan` | `#22D3EE` |
| `dubbing-indigo` | `#6366F1` |
| `dubbing-gradient` | cyan→indigo 渐变点缀（默认） |

---

## 4. 输出路径

| 模式 | 路径 |
|------|------|
| **默认（上下文仓）** | `blog/images/og/{slug}/{slug}-og-en.webp` |
| **部署仓**（`--deploy`） | `{DUBBINGAI_DEPLOY_ROOT}/public/blog/images/og/{slug}/{slug}-og-en.webp` |

CMS 上传时对齐 URL：`/blog/images/og/{slug}/{slug}-og-en.webp`

---

## 5. 验收清单

- [ ] 不看 URL 也能猜出文章主题
- [ ] 画布除标题/副标题外无多余文字块
- [ ] 仅 1 个品牌标记，融入自然
- [ ] **严格 1200×630** WebP · EN only
- [ ] registry `status: approved`

---

## 6. 安全

- **APINEED_API_KEY** 只放环境变量或 `.secrets/apineed-key`，禁止写入 git
