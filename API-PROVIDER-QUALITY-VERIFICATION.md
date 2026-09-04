# API 提供方生成质量验证（元文档）

> **用途**：在接入或更换第三方 AI API 网关（fal、APINEED、其他 OpenAI 兼容代理）时，用**可复现**的对照实验判断：返回的是否为宣称模型的**满血路由**，还是**降级 / 盗版 / 换模型**。
>
> **适用范围**：以 **GPT Image 2** 等生图 API 为主；LLM 文本 API 可复用同一套「同 prompt、多提供方、量化 + 判据」框架。
>
> **最后更新**：2026-08-28 · 依据仓库内 APINEED vs fal 生图 API 对照实验结论整理（**与任何客户项目解耦**，探针产物见 `api-quality-probes/`）。

---

## 1. 核心原则

| 原则 | 说明 |
|------|------|
| **先对齐流程，再比模型** | 不同 `size`、不同 prompt 风格（如 2mv 深色 vs Alignify 纸拼贴）造成的差距，**大于**很多「假模型」差距。必须 **同一 prompt、同一后处理、同一画幅策略**。 |
| **代理 ≠ 假** | fal、APINEED 都是代理；验证的是**该代理背后的路由**是否等同官方/参考路由，而非「是不是直连 OpenAI」。 |
| **一次实验不下终审** | 单次通过只说明「在该 prompt + 该参数下可用」；换尺寸/quality/并发后应抽检。 |
| **量化 + 目视 + 元数据** | 三者缺一不可；只看图或只看 HTTP 200 都不够。 |

---

## 2. 何时必须跑验证

- 新接入 API 提供方或新模型 slug（如 `gpt-image-2`）
- 账单/体积/耗时相对历史基线**突变**（变快 + 变小 + 变差）
- 网关 **`/v1/models` 元数据**与模型能力不符（例如图像模型标成 `text_generation`）
- 用户反馈「同 prompt 官方/playground 好、代理图糊/模板化」
- 提供方**静默改写请求参数**（请求 `1216×632` 返回 `1536×1024`）

---

## 3. 标准对照实验（生图）

### 3.1 固定变量（Single Source of Truth）

选定**一条已验证满意**的内部流程作为基准（推荐 **Alignify OG 流程**，而非 2mv 深色模板——除非被测场景就是 2mv 博客）：

```
brief（visual_anchors + anti_patterns）
  → build_prompt（editorial-collage / swiss-grid）
  → gpt-image-2 · quality=high · 1216×632 · jpeg · n=1
  → LANCZOS 裁切 1200×630
  → 品牌叠加（与生产一致）
  → WebP q≥92 或 JPEG q=92
```

**参考实现**

| 项目 | 路径 |
|------|------|
| Alignify 生图脚本（**fal / APINEED 共用同一 pipeline**） | `Alignify/scripts/ops/generate-og-cover.py` |
| Brief / prompt 规则 | `Alignify/data/og-cover-rules.md` · `Alignify/scripts/ops/og_brief_lib.py` |
| 页面分析 → brief | `Alignify/scripts/ops/analyze-og-page.py` |
| 2mv 流程（仅 2mv 场景，非本探针默认） | `2mv/blog/images/OG-COVER-WORKFLOW.md` |

**双提供方对照（同一 registry 条目，仅改 `--provider`）**

```powershell
$env:FAL_KEY = "..."
$env:APINEED_API_KEY = "..."
$env:ALIGNIFY_DEPLOY_ROOT = "E:\自有部署项目\alignify production"   # 或 --to-staging 预览

python Alignify/scripts/ops/generate-og-cover.py --provider fal --section tools --slug image-generator --locale en --to-staging --dry-run
# 确认 prompt 后分别生成：
python Alignify/scripts/ops/generate-og-cover.py --provider fal     --section tools --slug image-generator --locale en --to-staging
python Alignify/scripts/ops/generate-og-cover.py --provider apineed --section tools --slug image-generator --locale en --to-staging
```

将两次输出的 raw/crop/final 与 `prompt.txt` 复制到 `api-quality-probes/{YYYY-MM-DD}_{slug}/` 存档（见 §3.3）。

> **2026-09 起**：APINEED 通道为**异步提交**（`media/generations`，无 `size` 参数，比例由 prompt 控制）——与 fal 的固定 `1216×632` 请求不再同构，对照结论请同步见 §11.2。

### 3.2 实验矩阵（最少 3 次调用 / 提供方）

| # | 类型 | prompt | 目的 |
|---|------|--------|------|
| A | **极简探针** | 纯色底 + 精确文字 `TEST-123`，无其它元素 | 看文字渲染、平坦区域压缩、体积是否异常 |
| B | **生产级** | 目标 brief 的完整 `build_prompt` 输出 | 与满意基线比构图、风格、信息密度 |
| C | **交叉模型**（可选） | 与 B **完全相同**，仅改 `model`（如 `gpt-image-1` vs `gpt-image-2`） | 若两模型输出几乎相同 → 可疑 |

**硬性要求**

- A、B 的 **prompt 字节级一致**（存 `prompt.txt`）
- 同一 **`quality` / `output_format` / 请求 `size`**
- 记录 **原始响应 JSON**（脱敏 key，可删 `b64_json` 本体）

### 3.3 输出目录约定

```
api-quality-probes/{YYYY-MM-DD}_{slug}/
  prompt.txt
  brief.json            # 可选；来自 og-briefs 或手写探针 brief
  summary.json          # 量化指标（手写或脚本汇总）
  {provider}-raw.jpg
  {provider}-crop.webp
  {provider}-final.webp
  {provider}-response.json
```

> 目录在 **monorepo 根** [`api-quality-probes/`](./api-quality-probes/README.md)（与本文同级），不绑定任何客户文件夹。

---

## 4. 量化指标（自动记录）

每次生成写入 `summary.json`：

| 字段 | 说明 | 异常信号 |
|------|------|----------|
| `provider` | fal / apineed / … | — |
| `model` | 请求 model slug | 与响应不一致 |
| `requested_size` | 如 `1216x632` | — |
| `actual_size` | 解码后宽高 | **与请求不符且未文档化** → 可疑 |
| `raw_bytes` | 原图字节 | 同尺寸下比参考提供方 **小一个数量级** → 可疑 |
| `bytes_per_pixel` | raw_bytes / (w×h) | 跨提供方差 **>5×** 需目视 |
| `output_image_tokens` | 响应 `usage`（若有） | 同 size/quality 下与参考差 **>30%** 需记录 |
| `elapsed_s` | 端到端耗时 | **<5s** 且声称 high/4K → 可疑；**>180s** 记录即可 |
| `http_status` | 200/4xx/524 | 524/1010 记网关稳定性，不单判假 |
| `quality` / `output_format` | 响应回显 | 与请求不一致 → 可疑 |

**参考基线（2026-08-28，GPT Image 2，Alignify 生产 prompt）**

| 提供方 | 请求 size | 实际 size | raw_bytes | 备注 |
|--------|-----------|-----------|-----------|------|
| fal | 1216×632 | 1216×624 | ~163 KB | 参考满血路由 |
| APINEED | 1216×632 | **1536×1024** | ~254 KB | 静默改尺寸；Alignify prompt 下**目视可接受** |
| APINEED | 1216×632（2mv 深色 prompt） | 1536×1024 | ~1.5 MB（复杂场景） | 风格差主要来自 **prompt**，非唯一模型因素 |

---

## 5. 元数据与目录探针

在生图前/后各跑一次：

```http
GET {base_url}/v1/models
Authorization: Bearer {key}
```

检查项：

| 检查 | 满血/正常 | 降级/配置错误信号 |
|------|-----------|-------------------|
| 目标 model 是否存在 | 存在 | 404 / `model_not_found` |
| `supported_endpoint_types` | 含 `image-generation` 或文档声明的图像端点 | **图像模型标成 `openai` + `text_generation`** |
| `workflows` / `output_modalities` | `text_to_image` / `image` | 仅 `text` |
| 单价 | 与官方量级同阶 | **离谱低价**且无说明 |

另：对 **同一极简 prompt** 分别请求 `gpt-image-2` 与 `gpt-image-1`——若体积/像素/构图无法区分，提高怀疑等级。

---

## 6. 目视验收清单（生图）

与**内部满意样张**并排（如 Alignify 已 approved OG、2mv 已交付封面），逐项打分 1–5：

- [ ] **标题/副标题**：拼写正确、笔画清晰、缩略图可读（120×63）
- [ ] **风格约束**：brief 中 `anti_patterns` 是否被违反（neon glow、versus 图、空卡片等）
- [ ] **HERO 是否成立**：`visual_anchors[0]` 是否占画布主导
- [ ] **信息密度**：非「空大图 + 小字」或「字多图乱」
- [ ] **压缩伪影**：平坦区色带、JPEG 块效应、文字边缘糊
- [ ] **与参考提供方 A/B**：同 prompt 下是否**同一档位**（允许构图随机，不应差一整档审美）

**目视结论不应单独定性**；必须与 §4、§5 一起看。

---

## 7. 判定 taxonomy（Verdict）

| 等级 | 代号 | 含义 | 典型条件 |
|------|------|------|----------|
| ✅ | **GENUINE** | 与参考路由同档 | 同 prompt 下量化+目视与 fal/官方基线一致；元数据合理 |
| 🟢 | **ACCEPTABLE_PROXY** | 可生产使用 | 有静默改 size 等网关行为，但 B 实验目视达标（本次 APINEED + Alignify prompt） |
| 🟡 | **SUSPICIOUS** | 需换路由或参数 | 体积/ token 异常 + 目视略差；或 models 目录明显错误 |
| 🔴 | **LIKELY_DOWNGRADED** | 不建议生产 | 同 prompt 明显劣于参考；或交叉模型无法区分；或极简探针质量崩坏 |
| ⛔ | **FAKE_OR_WRONG_MODEL** | 停用 | 返回无关图、秒回、无 image tokens、与声明 model 完全不符 |

**注意**：「LIKELY_DOWNGRADED」≠ 法律意义上的「盗版」；文档仅描述**技术路由与质量是否匹配宣称**。

---

## 8. 推荐执行顺序（Checklist）

```
□ 1. 选定参考流程（Alignify OG / 2mv OG）与参考提供方（如 fal）
□ 2. 写 brief + 导出 prompt.txt（dry-run）
□ 3. GET /v1/models 截图/存档
□ 4. 探针 A：TEST-123 × 各提供方
□ 5. 探针 B：生产 prompt × 各提供方（脚本并行，同 prompt）
□ 6. 填 summary.json 量化表
□ 7. 并排目视 + 与历史满意图对比
□ 8. （可选）探针 C：gpt-image-1 交叉
□ 9. 写入 Verdict + 日期 + 操作人
□ 10. 通过 ACCEPTABLE 以上 → 才写入生产 skill/文档的默认 provider
```

---

## 9. LLM 文本 API（简版）

生图以外，可复用同一元流程：

| 生图指标 | LLM 等价 |
|----------|----------|
| 同 prompt 目视 | 同题回答质量、推理步骤 |
| raw_bytes | 输出 token 数 |
| actual_size | 是否截断 / 空回复 |
| 交叉模型 | 宣称 Sonnet  vs 实际 Haiku 行为（可用 [api-model-spy](https://github.com/dabaibian/api-model-spy)、[API-Police](https://github.com/Jorwnpay/API-Police) 等探针） |
| models 元数据 | context window、reasoning_tokens 是否符合 o 系列指纹 |

---

## 10. 安全与合规

- API key **仅**放 `{project}/.secrets/` 或环境变量；**禁止**写入本元文档或 git 跟踪的 prompt 存档
- 探针图默认存 `api-quality-probes/`，勿提交密钥；临时 staging 图验收后删除
- 第三方审计工具（ztest.cc、API-Police）仅供参考，**不能替代**同 prompt 业务对照

---

## 11. 历史案例摘要

### 11.1 APINEED `gpt-image-2`（2026-08-28）

| 实验 | 结论 |
|------|------|
| 2mv 深色 prompt + 1536×1024 | fal 远优于 APINEED；**prompt 风格是主因之一** |
| Alignify editorial-collage + 同一 `build_prompt` | **两提供方都可用**，差距大幅缩小 |
| APINEED models 目录 | `gpt-image-2` 标为 text 模型 → **SUSPICIOUS 元数据** |
| APINEED 静默 size | 请求 1216×632 → 返回 1536×1024 → **ACCEPTABLE_PROXY**（目视 OK 时） |

**生产建议（通用 OG）**

- 默认：**fal** `openai/gpt-image-2` + Alignify 流程（`generate-og-cover.py --provider fal`）
- APINEED：成本备选（`--provider apineed`）；**每次换 prompt 风格或 size 需重跑 §3 探针 B**

### 11.2 APINEED 接口迁移（2026-09-04）

| 项 | 说明 |
|----|------|
| 触发 | 网关下线同步 `POST /v1/images/generations`（`synchronous_image_generation_unavailable`），全部 APINEED 通道切至**异步** `POST /v1/media/generations` |
| 请求形态 | `{"workflow":"text_to_image","model":"gpt-image-2","input":{"prompt":...}}` → 返回 `id`（task）→ `GET /v1/media/generations/{id}` 轮询 → `outputs[0].url` |
| 参数限制 | 新接口**不接受 `size` / `quality` / `output_format`**；输出画布随 prompt 构图 |
| 实测 | prompt 显式要求 16:9 宽幅 → 直出 **1730×909**（≈1.9:1）；未指定则偏竖版（1122×1402） |
| 对策 | 脚本已自动在 prompt 追加宽幅 1200×630 比例指令；post trim 到 1200×630 保留 |
| 旧结论 | 11.1「静默 size（请求 1216×632 → 返回 1536×1024）」**仅适用于旧同步网关**，已失效 |

---

## 12. 扩展与维护

- 新提供方接入：在 `generate-og-cover.py` 增加 provider 分支，或临时用 curl 对照；**同一 prompt** 写入 `api-quality-probes/`
- 新模型（如 `gpt-image-2-all` 固定价路由）：单独一行 Verdict，**不得**与标准 `gpt-image-2` 混表
- 本文档随实验更新 **§4 基线表** 与 **§11 案例**；单次实验明细放 **`api-quality-probes/`** 目录

---

*Maintainer: 内容/工程 whoever runs OG pipeline · SSOT for cross-client API quality gates*
