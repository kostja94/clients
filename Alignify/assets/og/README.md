# OG 封面图（已废弃 staging 目录）

**OG 图只保存在部署仓一处**，不再写入本目录。

## 唯一存储路径（部署仓）

```
{DEPLOY_ROOT}/public/{section}/{slug}/{slug}-og-en.webp
{DEPLOY_ROOT}/public/{section}/{slug}/{slug}-og-zh.webp
```

线上 URL：`https://alignify.co/{section}/{slug}/{slug}-og-{locale}.webp`

## 工作流

1. **生成** → `scripts/ops/generate-og-cover.py`（**默认直写部署仓 public/**）
2. **验收** → 目视 + `scripts/audit/audit-og-coverage.mjs --deploy`
3. **注册**（可选，上线前）→ `migrate-og-covers.py --no-register` 仅用于把历史 staging 文件 **move** 到 deploy；新图无需迁移

临时预览才用 `--to-staging`（写回本目录，验收后应 move 或删除，不要长期双份保存）。

规则 v3.5：[../../data/og-cover-rules.md](../../data/og-cover-rules.md)

详见 [og-covers.md](../../skills/ops/og-covers.md)。
