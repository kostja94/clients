# Floatboat 全站 SEO/GEO 审计包

> 发给 Floatboat 技术团队 · 自包含 · 无需其他 repo 文件  
> **站点**：https://floatboat.ai · **更新**：2026-08-20

---

## 包里有什么

| 文件 / 目录 | 用途 |
|-------------|------|
| **[floatboat-seo-geo-checklist.md](./floatboat-seo-geo-checklist.md)** | 验收清单 — 逐项打勾，填状态与证据 |
| **[SKILL.md](./SKILL.md)** | Agent 工作流 — 怎么跑 audit、读哪些 reference |
| **[references/](./references/)** | 规则与标准（schema、robots、prompt 库等） |
| **[tools/](./tools/)** | Python 探测脚本（stdlib only，无需 pip install） |

**整包复制给对方即可**，路径保持相对关系不变。

---

## 快速开始（技术团队）

### 1. 环境

- Python **3.10+**
- 可访问 floatboat.ai（跑 curl / 脚本）

### 2. 跑自动化探测

```powershell
cd tools
python crawl_probe.py --tier t0+t1
python sitemap_diff.py --probe-dead
python ai_ua_probe.py
python schema_extract.py
python combo_store_sample.py -n 30 --seed 20260820
```

### 3. 用 Agent 对照清单

在 Cursor（或 Claude）中：

1. 打开本文件夹
2. 将 **SKILL.md** 与 **floatboat-seo-geo-checklist.md** 加入上下文
3. 发送以下触发语：

```
按 floatboat-site-seo-geo-audit skill，对 floatboat.ai 执行 full 审计。

工作方式：
1. 运行 tools/ 下全部脚本
2. 逐项对照 floatboat-seo-geo-checklist.md Part 1–11
3. 在「状态」列填写 ✅ / ⚠️ / ❌ / ❓
4. 在「证据」列写入脚本输出或 curl 结果
5. 汇总 P0/P1/P2 到 checklist 第十四节
6. 更新第十六节审计历史

只报告 findings，不要直接改网站代码。
```

### 4. 修复与复验

- 按 checklist **第十四节 P0** 优先修复
- 修复后 Agent 跑 **delta** 模式复验受影响 Part

---

## 目录结构

```
site-seo-geo-audit/
├── README.md                      ← 本说明
├── floatboat-seo-geo-checklist.md ← 验收清单（主交付对照表）
├── SKILL.md                       ← Agent 入口
├── references/
│   ├── project-config.md          ← 品牌/域名/路由口径
│   ├── page-tier-matrix.md        ← 页面分层与抽样
│   ├── schema-spec.md
│   ├── robots-ai-crawlers.md
│   ├── agent-ready.md             ← llms.txt 模板
│   ├── prompt-library.md          ← 35 条 GEO prompt
│   └── …
└── tools/
    ├── crawl_probe.py
    ├── sitemap_diff.py
    ├── ai_ua_probe.py
    ├── schema_extract.py
    └── combo_store_sample.py
```

---

## 与营销文档的关系

本包 **不依赖** `floatboat.md`、关键词表、博客 skill 等。  
站点策略背景若需要，另行提供营销文档包；技术验收只读本目录即可。

---

*Floatboat Site SEO/GEO Audit Package · v1.0*
