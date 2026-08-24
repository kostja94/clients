# 审计与 Baseline

从**部署仓根目录**执行：

```bash
# 主审计 — tools + blog Markdown
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --locale both --violations-only

# 单 slug
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only

# 部署仓内链扫描（href 提取）
python scripts/permanent/audit-internal-links.py
python scripts/permanent/scan-markdown-hrefs.py

npm run verify:content-json
```

> **未注册 npm**：`npm run audit:internal-links` 不存在；直接用上述 python 命令。

## CI / 阻断标准

| 检查 | 标准 |
|------|------|
| R0 无效 href | 0 high |
| R1 最低 distinct | ≥5（Tools 长文） |
| R4 重复 slug | 0 |
| R7 FAQ | FAQ 答案无内链 |

## 报告位置

`E:/clients/Alignify/scripts/reports/`
