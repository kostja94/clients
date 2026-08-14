# 05 — 部署指南

> **这一篇教你从本地改代码到线上生效的完整流程。**  
> 第一次操作让 Kostja 带你走一遍，之后你自己就能独立完成。  
> 下一步 → [06-seo-checklist.md](./06-seo-checklist.md)（发布前的 SEO 检查）

---

## 前置准备（第一次操作时让 Kostja 帮你确认）

在开始之前，确认以下事情已经就绪：

- [ ] 本地电脑已克隆代码仓库（`finalround-web`）
- [ ] 已安装 Node.js（版本 ≥ 18）
- [ ] 已安装 Git
- [ ] 有 Vercel Dashboard 访问权限（项目名：`finalround-nextjs`）
- [ ] 本地能运行 `npm run dev`，在 `http://localhost:8080` 看到页面

**如果有任何一项没完成，先找 Kostja。**

---

## 完整部署流程（5 步）

### 第 1 步：本地修改代码

按场景选择操作：

| 场景 | 操作 |
|------|------|
| 只改公司数据 | 编辑 `src/data/companies/{slug}.json`，改数字/文案 |
| 新增一家公司 | 复制 [04-page-template.md](./04-page-template.md) 模板 → 创建 `src/data/companies/{slug}.json` |
| 改组件/样式 | 编辑 `src/components/` 或 `src/views/` 下的文件 |

### 第 2 步：本地验证

```bash
# 1. 如果是新增/删除公司，先生成 barrel index
node scripts/generate-company-index.mjs

# 2. 完整构建验证
npm run build

# 3. 跑数据验证（确保 JSON 文件无误）
python3 scripts/add-sources.py   # 或手动 python3 -c "..." 验证脚本
```

**`npm run build` 必须成功**——这会自动执行 prebuild（barrel 生成）然后构建 151 个静态页面。如果失败，看报错信息修复。

本地开发预览：

```bash
npm run dev
```

浏览器打开 **`http://localhost:8080`**（不是 3000！），确认页面正常。

### 第 3 步：提交推送

确认无误后：

```bash
git add .
git commit -m "update: {简短描述}"
git push
```

**Commit message 规范**：
- `update: refresh Amazon layoff data` — 更新已有公司数据
- `add: new company page for NVIDIA` — 新增公司页（含 JSON + index.ts）
- `fix: correct Oracle total_count` — 修正错误

**新增公司时必须同时提交**：`{slug}.json` + 自动更新的 `src/data/companies/index.ts`。

### 第 4 步：Vercel 自动部署

推送后 Vercel 自动开始部署（1–2 分钟）。在 Vercel Dashboard Deployments 页面看进度。部署完成后可在 Vercel 生成的预览 URL 初步检查。

### 第 5 步：验证线上生效

分两步验证——**两步都要做，不要只看第一步**。

#### 5a. 验证 origin（Vercel 子域名）

```
https://finalround-nextjs.vercel.app/tech-layoffs
```

确认改动已经生效。新增公司页时要直接访问 `/tech-layoffs/{slug}` 确认。

#### 5b. 验证主域（用户实际看到的）

```
https://www.finalroundai.com/tech-layoffs
```

确认：
- [ ] 地址栏显示 `finalroundai.com`（不是 vercel.app）
- [ ] 页面内容和 5a 看到的一致
- [ ] 样式正常、没有 404
- [ ] 图片和链接都正常

**如果 5a 正常但 5b 不正常**（内容没更新、样式错乱、404）→ 找 **Mohit**（主站 Rewrite 规则维护），可能需要确认 Rewrite 配置或缓存。

---

## 常见操作场景速查

### 场景 A：只改已有公司的数据

比如更新 Amazon 的裁员人数。

```
1. 编辑 src/data/companies/amazon.json，改 total_count 和相关 content
2. npm run build（验证通过）
3. git add → git commit → git push
4. 等 Vercel 部署（1–2 分钟）
5. 验证主域
```

### 场景 B：新增一家公司页

```
1. 复制 04-page-template.md 模板 → 创建 src/data/companies/{slug}.json
2. 填写所有字段，确保 FAQ ≥ 3 条
3. npm run build（自动 run prebuild → 重新生成 barrel index）
4. 跑数据验证脚本
5. git add {slug}.json src/data/companies/index.ts
6. git commit -m "add: company page for {Company Name}"
7. git push → Vercel 部署 → 验证
```

### 场景 C：批量导入（从 CSV）

如果有很多公司数据需要一次性导入：

```bash
node scripts/import-company-layoffs-csv.mjs path/to/export.csv
```

这会自动写入 JSON 文件 + 重新生成 barrel index。之后 `npm run build` 验证。

### 场景 D：改了页面组件

```
1. 修改 src/components/ 或 src/views/ 下的文件
2. npm run dev（本地预览，http://localhost:8080）
3. 抽测 3–5 个已有公司页确认没被改坏
4. npm run build（全量验证）
5. git add → git commit → git push → 验证
```

---

## 部署故障排查

| 症状 | 可能原因 | 怎么解决 |
|------|----------|----------|
| `npm run build` 失败 | JSON 文件格式错误或 slug 不匹配 | 看构建日志定位到具体文件,修复 JSON |
| Vercel 部署失败（红色） | 同上或代码语法错误 | 看 Vercel Build Log,修复后重新 push |
| 新增公司页在聚合页看不到 | barrel index 未重新生成 | `node scripts/generate-company-index.mjs` + 重新构建 |
| origin 有更新,主域没更新 | 主站缓存 / Rewrite 延迟 | 等 2–3 分钟；持续 > 10 分钟找 **Mohit** |
| 主域样式错乱 | CSS/JS 资源路径（assetPrefix）问题 | 找 Kostja，可能是 Vercel 环境变量 |
| 页面 404 | 路由或 JSON slug 不匹配 | 检查文件是否在 `src/data/companies/`、slug 是否一致 |

**区分责任**：
- 代码/数据/构建问题 → 找 Kostja
- 主域 Rewrite/代理/缓存 → 找 **Mohit**

---

## 一个好习惯

每次部署后记录：

> {日期} — {改了什么} — {效果确认}

这样万一出问题，能快速定位是哪个改动引起的。

---

## 可用脚本速查

| 命令 | 用途 |
|------|------|
| `npm run dev` | 本地开发，端口 **8080** |
| `npm run build` | prebuild → next build（151 静态页） |
| `node scripts/generate-company-index.mjs` | 手动重新生成 barrel index |
| `node scripts/import-company-layoffs-csv.mjs <file>` | CSV 批量导入 |
| `python3 scripts/add-sources.py` | 数据来源补充/验证 |
| `python3 scripts/optimize-seo-data.py` | SEO 数据优化 |

---

*下一步 → [06-seo-checklist.md](./06-seo-checklist.md) 每次发布前过一遍*
