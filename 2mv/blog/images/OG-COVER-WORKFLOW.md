# 2mv Blog OG 封面图生成流程

> 本目录存放 2mv 博客文章的 OG 封面图（1200×630）与生成规范。所有封面由 AI 生图 + 后期叠加 logo 完成。

---

## 1. 生成总览

```
fal.ai 生图 (flux dev) → 缩放裁剪 1200×630 → 叠加 2mv logo（右下角）→ 保存到本目录
```

每张封面 = **主体画面**（AI 生成）+ **2mv logo 徽章**（后期叠加），分两步保证 logo 永远清晰。

---

## 2. 文件命名规范

| 文件 | 对应文章 | 风格 |
|------|---------|------|
| `what-is-2mv-og.jpg` | #01 What Is 2mv | 官网深色版 |
| `best-social-media-marketing-agencies-og.jpg` | #02 Best Agencies | 官网深色版 |
| `introducing-2mv-reports-og.jpg` | #03 Introducing 2mv Reports | 官网深色版 |
| `what-is-2mv-editorial-og.jpg` | #01 What Is 2mv | 纸拼贴 editorial 版 |
| `best-social-media-marketing-agencies-editorial-og.jpg` | #02 Best Agencies | 纸拼贴 editorial 版 |
| `introducing-2mv-reports-editorial-og.jpg` | #03 Introducing 2mv Reports | 纸拼贴 editorial 版 |

**规则**：`{slug}-og.jpg` 默认官网深色版；`{slug}-editorial-og.jpg` 为纸拼贴 editorial 备用版。全部 1200×630。

---

## 3. 风格基线（所有封面统一）

> **品牌色与视觉风格规范以 [2mv-brand-visual.md](../../2mv-brand-visual.md) 为准**（官网实测 token + 视觉语言）。

### 3.1 封面风格 = 官网深色科技 editorial（非纸拼贴）

```
Dark tech-editorial style. Deep charcoal background (#131313), large bold Plus Jakarta Sans
headline in off-white (#f2f2f2), lime-green (#d6fd70) accents (underline/keywords/numbers),
bright blue (#2453ff) secondary accent. Video card grid / phone mockup / data cards as
visual elements. Rounded card corners (2.15rem), pill buttons. High contrast, confident,
data-driven. 1200x630 landscape, 1.91:1 ratio.
```

### 3.2 品牌色（from tokens）

| 色 | 值 | 用途 |
|----|-----|------|
| 黄绿 | `#d6fd70` | 主强调（下划线/关键词/数字） |
| 深墨 | `#131313` | 背景面板 |
| 米白 | `#f2f2f2` | 深底上文字 |
| 亮蓝 | `#2453ff` | 次强调 |

**注意**：**禁用电光绿 `#00FF66`**（误判色）；黄绿上的文字用深橄榄 `#4f6208`。

---

## 4. 提示词模板（含防乱码规则）

### 4.1 模型选择（重要）

| 模型 | fal 端点 | 文字渲染 | 适用 |
|------|---------|:---:|------|
| **gpt-image-2（推荐）** | `openai/gpt-image-2` | ⭐⭐⭐ 原生清晰 | **所有含文字封面** |
| flux dev | `fal-ai/flux/dev` | ⭐ 易乱码 | 无文字构图 |

**规则**：封面需要标题文字时，**优先用 gpt-image-2**——它的 production-ready text rendering 能原生渲染清晰文字，无需后期 PIL 叠加，杜绝重叠/乱码问题。

### 4.2 gpt-image-2 参数

```json
{
  "prompt": "...",
  "image_size": "landscape_16_9",
  "quality": "high",
  "num_images": 1
}
```

端点：`https://queue.fal.run/openai/gpt-image-2` · 输出约 1088×608

### 4.3 提示词模板

```
{风格基线} + {主题构图，含具体文字内容} + {防乱码句}
```

防乱码句（gpt-image-2 下可放心写文字，但仍加保险）：
```
Spell all words correctly, no gibberish, no fake letters.
Leave the bottom-right corner clean for logo placement.
```

**文字写法**：直接把标题/标签写进提示词，指定排版位置：
```
Layout: large bold black headline at top-left reading 'INTRODUCING 2MV REPORTS'
(two lines: 'INTRODUCING' then '2MV REPORTS' in larger type), with a short subtitle
below reading 'Viral Video Breakdowns You Can Film'.
```

---

## 5. 执行步骤

### 5.1 fal.ai 生图

- **首选模型**：`openai/gpt-image-2`（文字清晰）→ `https://queue.fal.run/openai/gpt-image-2`
- **备用模型**：`fal-ai/flux/dev`（无文字构图）→ `https://queue.fal.run/fal-ai/flux/dev`
- **认证**：`Authorization: Key {FAL_KEY}`（见安全存储，勿写死在文档）
- **参数**（gpt-image-2）：
  ```json
  {
    "prompt": "...",
    "image_size": "landscape_16_9",
    "quality": "high",
    "num_images": 1
  }
  ```
- **流程**：POST 提交 → 轮询 `status_url` → COMPLETED 后从 `response_url` 取图
- **输出**：gpt-image-2 ≈ 1088×608；flux dev = 1024×576

### 5.2 缩放裁剪到 1200×630

```
1. 等比缩放（LANCZOS）至宽 1200 或高 630（取先达标者）
2. 居中裁剪到 1200×630
3. 保存 JPEG quality=92
```

### 5.3 叠加 2mv logo

- **logo 来源**：官网 `https://www.2mv.ai/icons/apple-touch-icon.png`（180×180，黄绿方块 `#d6fd70` + 黑字 "2mv"）
- **尺寸**：高 84px，等比缩放
- **位置**：右下角，`x = 1200 - logo宽 - 28`, `y = 630 - logo高 - 28`
- **方式**：PIL `paste(logo, (x, y), logo)`（RGBA alpha 作蒙版）

---

## 6. flux 降级方案（gpt-image-2 不可用时的备用）

### 6.1 何时用

gpt-image-2 是首选（原生文字清晰）。仅当其不可用/超时/预算限制时，降级用 flux dev + PIL 叠加文字。

### 6.2 步骤

```
1. 生成无文字主体图（提示词要求 No text, no letters, no words）
2. 缩放裁剪到 1200×630
3. 用 PIL ImageDraw + ImageFont 叠加标题：
   - 字体：Arial Bold (C:\Windows\Fonts\arialbd.ttf)
   - 标题主词：72-88px，黑色 (0,0,0)
   - 强调：黄绿 (#d6fd70) 色块衬底 或 下划线
   - 副标题：30-36px，深灰 (30,30,30)
   - 位置：左上 margin 60px，起始 y=40
4. 叠加 logo（§5.3）
```

**注意**：PIL 叠加文字需确保主体图左上区域预留空白，否则文字与画面重叠（#03 v2 的教训）。

---

## 7. 图片质量检查清单（生成后）

- [ ] 尺寸 = 1200×630
- [ ] 标题文字清晰可读（PIL 叠加版：检查左上区域深色像素）
- [ ] 右下角 logo 完整可见，未超出安全区
- [ ] 风格与官网一致：深色 `#131313` + 黄绿 `#d6fd70` + 大号白粗体标题（见 brand-visual.md §0.1）
- [ ] 构图契合文章主题（见 §8 构图参考）
- [ ] 无 AI 乱码文字（无文字主体图 + PIL 文字为佳）

---

## 8. 现有封面构图参考（官网深色风格）

> 风格统一：深墨背景 `#131313` + 大号白粗体标题 + 黄绿 `#d6fd70` 强调 + 品牌数据元素。

| 文章 | 构图 |
|------|------|
| #01 What Is 2mv | 深色 Hero + 大标题 "From Zero to Millions of Views" + 视频卡片墙 + 增长曲线（1M/10M/100M） |
| #02 Best Agencies | 深色对比布局 "Others Deliver Content. 2mv Delivers Growth." + 排名/评分卡 + 复利柱状图 |
| #03 Introducing Reports | 深色时间轴 + 四拍标注（HOOK/CONTEXT/PROOF/LOOP）+ shot list 卡片 |

> 每张封面：`#131313` 底 · 白粗体标题（Plus Jakarta Sans）· 黄绿下划线/关键词 · 圆角卡片 · 数据元素。

---

## 9. 所需 API key（安全提示）

- **fal.ai key**：`ce060cc7-bce1-4193-8b0b-d9699f1632aa:...`（首次已使用，建议存环境变量 `FAL_KEY`）
- **切勿**将 key 写入提交到 git 的文件
- 本项目文档不保存 key 明文（本文件仅说明流程）

---

## 10. 快速复用清单

```
1. 定主题构图（参考 §8 或新设计，明确文字内容与排版位置）
2. 写提示词（§4.3 模板）
3. fal gpt-image-2 生图 → 轮询取图（文字由 AI 原生渲染）
4. 缩放 1200×630
5. 叠加 logo（§5.3）
6. 质量检查（§7）
7. 若 gpt-image-2 不可用 → §6 flux + PIL 文字降级方案
```
