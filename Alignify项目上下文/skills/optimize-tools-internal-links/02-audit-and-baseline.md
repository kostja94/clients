# 审计与 Baseline

从**部署仓根目录**执行（路径指向上下文仓脚本）：

```bash
# CI 阻断（部署仓）：R0 404/路由 + 图均衡 + R1/R4/R7
npm run audit:internal-links
# 或
python scripts/permanent/run-internal-links-audit.py

# 全库 baseline（internal-links + anchor + cross-page）
python ../../项目文档/Alignify项目上下文/scripts/ops/run-tools-internal-links-baseline.py --locale both --json

# R0 — 无效 slug / 错误 tools|blog 路由（阻断）
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-internal-href-registry.py --violations-only

# 主审计 — tools + blog（默认 both）
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-tools-internal-links.py --locale both --violations-only

# 链接图均衡 — 合并 EN+ZH，孤页=0、入链≥3
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-cross-page-links.py --orphans-only

# 区块分布 / FAQ 堆链
python ../../项目文档/Alignify项目上下文/scripts/audit/audit-link-distribution.py --flags-only

# EN/ZH 对称性
python ../../项目文档/Alignify项目上下文/scripts/ops/report-en-zh-link-parity.py
```

## CI 阻断项

| 检查 | 脚本 | 标准 |
|------|------|------|
| **R0** | `audit-internal-href-registry.py` | 0 high（无效 slug、Blog/Tools 路由段错误） |
| **图均衡** | `audit-cross-page-links.py` | `orphan_count=0`，`inbound_below_threshold_count=0`（阈值 3） |
| **R1/R4/R7** | `audit-tools-internal-links.py` | 0 high |
| R2 密度 | 同上 | medium，枢纽页可豁免（`documentation`、`agent-skills` 等） |

## 部署仓修复脚本

| 脚本 | 用途 |
|------|------|
| `fix-broken-internal-hrefs.py` | 按 R0 报告批量修正无效 href |
| `apply-inbound-backlinks.py` | 低入链页补链（图均衡） |
| `spread-link-density.py` | P0/P1 FAQ 堆链分散到正文区块 |
| `remediate-internal-links-quality.py` | 清理模板句、锚文本、parity |

## 报告位置

`项目文档/Alignify项目上下文/scripts/reports/`

- `internal-href-registry-{date}.json` — R0
- `cross-page-links-{date}.json` — 孤页 / 入链<3
- `link-distribution-{date}.json` — 区块分布
- `internal-links-baseline-{date}.json` — 综合 baseline
