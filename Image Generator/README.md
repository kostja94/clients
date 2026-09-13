# Image Generator — 统一 OG 封面生图管线

为各 client 生成 **1200×630** OG 社交封面图（GPT Image 2；provider 三选一：fal / apineed / gitaigc）。
原散落在 `Alignify/scripts/ops/` 与 `dubbingai/scripts/ops/` 的重复脚本已合并为这一份实现，
client 差异（品牌、配色、section、locale、输出路径）全部收进 `clients/<name>.json`。

**本 README 是唯一使用入口**——任何 agent 从零开始按本文档即可完成生图任务。

## 硬性指标（不可妥协）

| 指标 | 要求 |
|------|------|
| 尺寸 | 精确 **1200×630** WebP（脚本自动 scale-to-cover 裁剪并校验） |
| 文字 | 仅 headline + 可选一行 subtitle（PPT 原则），禁止排名/脚注/slogan；语言按 locale 分图（en/zh），zh 更严格 |
| 品牌 | 恰好 **1 个**品牌角标（Kostja 署名 / wordmark / logo 三选一，PIL 后期叠加，**不由 AI 渲染**） |
| 相关性 | 视觉必须体现该页主题——由 registry 的 `composition` 与 LLM brief 驱动，禁止 generic 装饰 |

## 快速开始（copy-paste 即用）

前置：`pip install pillow`；密钥见下节。**dry-run 不调 API 不花钱，实跑会产生 API 费用。**

```powershell
# 1) 预览 prompt（免费，先看再生成）
python "E:\clients\Image Generator\generate-og-cover.py" --client dubbingai --slug best-ai-voice-changer --dry-run

# 2) Dubbing AI 新文章封面（默认 apineed → 写入 output\dubbingai\{slug}\）
python "E:\clients\Image Generator\generate-og-cover.py" --client dubbingai --slug best-ai-voice-changer

# 3) Alignify 页面封面（默认 fal → 直写部署仓 public\{section}\{slug}\）
python "E:\clients\Image Generator\generate-og-cover.py" --client alignify --section tools --slug image-generator --locale en

# 4) 批量（alignify 默认 en+zh 双语；并行对齐 provider 并发）
python "E:\clients\Image Generator\batch-generate-og-covers.py" --client alignify --section seo --slugs serp,geo --workers 8 --skip-existing

# 5) Alignify 全管线（seo→tools→blog，slug 自动从部署仓发现）
python "E:\clients\Image Generator\run-og-pipeline.py" --workers 8

# 6) 查看某 client 的 registry 条目
python "E:\clients\Image Generator\generate-og-cover.py" --client dubbingai --list
```

常用参数：`--provider fal|apineed|gitaigc`（默认取 client 配置：alignify=fal，dubbingai=apineed）、
`--locale en|zh`、`--deploy` / `--staging`（强制输出位置）、`--fallback-fal`（所选 provider 失败回退 fal）、
`--keep-raw`（保留裁剪前原图 `<out>.raw.png` 供对比）、`--crop-bias top|center|bottom`、
`--no-branding`、`--brand-mode kostja|<wordmark>|logo|none`。

## 密钥

| Provider | 环境变量 | 备选文件 |
|----------|----------|----------|
| fal | `FAL_KEY` | `<client>/.secrets/fal-key`（Alignify 已有）或 `~/.fal-key` |
| apineed | `APINEED_API_KEY` | `<client>/.secrets/apineed-key`（Alignify 已有）或 `~/.apineed-key` |
| gitaigc | `GITAIGC_API_KEY` | 明文见 `E:\个人知识库\工作流管理\本地API密钥-API-Keys-Local.md`（Rainbow/gitaigc 条目） |

- 密钥查找顺序：环境变量 → `<client>/.secrets/<provider>-key` → **任意其他 client 的
  `.secrets/`（自动跨 client 发现，dubbingai 会自动复用 Alignify 已存的 key）** → `~/.<provider>-key`
  → 也可用 `--fal-key-file` / `--apineed-key-file` / `--gitaigc-key-file` 显式传文件
- `--analyze-first` 及各 client 的 `analyze-og-page.py` 另需 `OPENAI_API_KEY`（或 `<client>/.secrets/openai-key`）
- **禁止把任何 key 写进文档、registry 或代码**

## 生成后流程（agent 必做）

1. **目视验收**成品 webp：尺寸 1200×630、标题无裁损、主题相关、仅 1 个品牌标。
   怀疑裁剪丢内容 → 用 `--keep-raw` 对比 `.raw.png` 与成品，必要时 `--crop-bias top`。
2. 验收通过 → 在该 client 的 `data/og-prompt-registry.json` 把对应条目 `status` 改 `approved`
   （生成后默认 `pending`）。
3. **上线**：alignify 新图已直写部署仓（历史迁移/注册 `OG_LOCALE_READY` 用
   `Alignify/scripts/ops/migrate-og-covers.py`）；dubbingai 加 `--deploy` 写部署仓
   `public/blog/images/og/{slug}/` 或手动上传 CMS（URL 对齐 `/blog/images/og/{slug}/`）。

## 新页 / 重生成的完整流程

```
阶段 0（新页/重生成推荐）— LLM 页面分析 → brief：
  Alignify:   python E:\clients\Alignify\scripts\ops\analyze-og-page.py --section {s} --slug {slug} --merge-registry
  Dubbing AI: python E:\clients\dubbingai\scripts\ops\analyze-og-page.py --slug {slug} --merge-registry
  （或一步到位：generate-og-cover.py --analyze-first）
阶段 A — generate-og-cover.py 生图（自动注入 brief + 裁剪感知指令）
阶段 B — 验收 → registry approved → 上线（见上节）
```

- **视觉规则 SSOT**：`<client>/data/og-cover-rules.md`（各 client 的风格/文案/裁剪规则）
- **操作 SOP**：`<client>/skills/ops/og-covers.md`（含各 client 特有约定）
- brief 存于 `<client>/data/og-briefs/{section}/{slug}/brief.json`

## Provider 与故障排查

| Provider | 端点 | 模式 | 备注 |
|----------|------|------|------|
| `fal` | `https://queue.fal.run/openai/gpt-image-2` | 提交 + 轮询 | 1216x632 直出，裁剪≈0；**文字多的图优先用 fal** |
| `apineed` | `https://apineed.com/v1/media/generations` | 异步 task（submit+poll） | 同步 `/v1/images/generations` 已下线（返回 `synchronous_image_generation_unavailable`，勿再用） |
| `gitaigc` | `https://gitaigc.com/v1/images/generations` | OpenAI 兼容同步 | 无 task 流；仅 1536x1024，靠 prompt 安全区保文字 |

常见错误：

- apineed 报 `No available channel for model gpt-image-2` → 上游通道挂了（非脚本问题）。
  换模型：`OG_APINEED_MODEL=gpt-image-1`（裁剪指令自动适配）；或 `--provider gitaigc` / `--fallback-fal`
- 报 `Deploy root not found` → 设环境变量 `ALIGNIFY_DEPLOY_ROOT` / `DUBBINGAI_DEPLOY_ROOT` 或 `--deploy-root`
- 报 `No registry entry for ...` → 先跑阶段 0 分析，或手工往 registry 加条目

## 裁剪感知（1200x630 硬指标的实现）

目标 1.91:1，各 provider 原始画布不同，最终 scale-to-cover + center 裁剪：

| Provider | 原始画布 | 裁剪损失 |
|----------|----------|----------|
| fal | 1216x632 | ≈0.3%（可忽略） |
| gitaigc / apineed+gpt-image-1 | 1536x1024（3:2） | 上下共 **~21%** |
| apineed+gpt-image-2 | prompt 驱动 ~16:9 | ~7% |

脚本按 provider+模型自动注入 **CROP AWARENESS** 安全区指令（3:2 画布 → 内容约束在幸存的
中段 ~79% 竖带、标题内边距从 10% 自动抬到 14%；上下边缘区只放纸纹理等装饰）。
`OG_APINEED_MODEL` 切模型时指令随之调整。**不要**手工改这些百分比——改 `expected_trim_pct()`。

## OG 图归档（output/）

各 client 的 OG 成品统一归档在 `output/<client>/`（2026-09-12 起 context/staging 输出的
默认写入位置，经 `clients/*.json` 的 `context_og_root` 配置；`--deploy` 仍直写部署仓供站点使用）：

```
output/
├── alignify/staging/{section}/{slug}/   # alignify --staging 预览件
├── dubbingai/{slug}/{slug}-og-en.webp + .meta.json
├── 2mv/*.jpg                            # 2mv 手工流程历史 OG
├── floatboat/*.jpg                      # 归档 OG
└── datus/*.jpg
```

## 目录结构与新增 client

```
Image Generator/
├── generate-og-cover.py            # 单张生成（唯一实现）
├── batch-generate-og-covers.py     # 批量（并行 worker / skip-existing 断点续跑）
├── run-og-pipeline.py              # alignify seo→tools→blog 编排（slug 从部署仓发现）
├── wait-and-run-og-pipeline.py     # 等 PID → 补 SEO → tools/blog
├── og_clients.py                   # client 配置加载 + deploy root 解析
├── og_cover_paths.py               # 输出路径计算（deploy / context 两布局）
├── og_brief_lib.py                 # registry/brief/LLM 分析（含各 client 分析 profile）
├── clients/<name>.json             # client 全部差异配置
├── output/<client>/...             # OG 成品归档
└── README.md
```

新增 client 三步：

1. 复制 `clients/dubbingai.json` 为 `clients/<name>.json`，改：`ctx_root`、品牌
   （wordmark / ACCENTS / salt / logo 路径）、`sections` / `locales`、输出布局与
   `context_og_root`、`styles` 风格文案、默认 provider
2. 页面分析方式：config `analyze_source` 选 `deploy-content`（读部署仓 content/，en+zh）
   或 `blog-md`（读 context 仓 blog markdown，en）；分析人设 prompt 在
   `og_brief_lib.py` 的 `ANALYZE_PROFILES` 按 client name 加一份
3. 在该 client 建 `data/og-prompt-registry.json`（`{"entries": [...]}`）后即可 `--list` / 生成

## 周边脚本（留在各 client 仓库）

- `Alignify/scripts/ops/` 的分析/审计工具（`analyze-og-page.py`、`merge-marketing-briefs.py`、
  `audit-og-coverage`、`migrate-og-covers.py` 等）保留原位，内部已指向本目录的统一库
- Prompt registry 与 briefs 仍在各 client 的 `data/` 下（路径见 client 配置）

> 密钥来源参考：`E:\个人知识库\工作流管理\本地API密钥-API-Keys-Local.md`
