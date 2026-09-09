# today-seo（/articles）发版流程

> 适用范围：`today.ai/articles` 的 SEO 站内容/代码变更发版（仓库 `todayai-labs/today-seo`，
> 本地目录 `E:\客户部署项目\today-seo-main`）。
> 维护日期：2026-09-09，依据当日多次真实发版（healthcare/cycle-stress spokes、finance spokes）复盘。

---

## 一、铁律

- **main 有分支保护，禁止直接 `git push origin main`**（远程会拒：
  `remote: Changes must be made through a pull request`）。
- 一切变更走 **feature 分支 + Pull Request + rebase 合并**。
- **CI 即部署**：合并进 main 后由 GitHub Actions 自动部署到 Vercel 生产
  （`article.today.ai`，`today.ai/articles` 由主站 today-web 反代），**无需**手动进 Vercel。

---

## 二、标准发版流程

```powershell
# 0) 前置：在 today-seo-main 里本地改好内容/代码
#    可选本地自检（推荐，先于提交暴露问题）
npm run validate:content   # zod schema + en/zh 页面集一致 + 本地资产存在性
npm run typecheck          # tsc
npm run build              # 全量 next build（慢，仅大改跑）

# 1) 从干净的 main 起分支
git checkout main
git pull --ff-only
git checkout -b feat/<描述>

# 2) 提交（只 add 本次相关文件，勿顺手带 temp/或无关改动）
git add <文件/目录…>
git commit -m "feat(scope): 一句话说明"

# 3) 推送 + 建 PR
git push -u origin feat/<描述>
gh pr create --base main --head feat/<描述> --title "…" --body "…"
#    → CI 自动跑 preview job，并在 PR 评论贴 preview 地址：
#      today-seo-pr-<编号>.preview.todayai.dev/articles/  （内容验证在 CI 内执行）

# 4) 核对 CI preview 通过后合并
gh pr merge <编号> --rebase --delete-branch
#    注意：即使本地出现 “Not possible to fast-forward” 之类噪音输出，
#    以 gh pr view <编号> --json state 的 MERGED 为准。

# 5) 本地 main 对齐
git checkout main
git pull --ff-only
```

---

## 三、合并后发生了什么（CI production job 自动执行）

合并 push 到 main 会触发 `.github/workflows/deploy-seo.yml` 的 **production** job：

1. checkout + Node 24 + `npm install`
2. `npm run validate:content`（不通过则部署中止）
3. 校验 Vercel 项目为 nextjs preset / outputDirectory 为空
4. `vercel build --prod`（本地产物上传，非远端构建）
5. 捕获**当前**生产 deployment（用于失败回滚）
6. `vercel deploy --prod --prebuilt --skip-domain` 生成生产候选
7. 验证候选产物资产 → 通过后 `vercel cache purge`（清 CDN）
8. `vercel promote` 把候选推上生产域名
9. 对 `article.today.ai` 做最终验证；**失败自动 rollback 到步骤 5 的旧版本并报红**

另：PR 存在期间每次 push 会自动更新 preview（preview job），供上线前人工抽查。

---

## 四、上线后线上复核（实测约 1–2 分钟内生效）

```powershell
# hub/列表页：确认新内容已上线
curl.exe -s -L https://today.ai/articles/finance | Select-String "新标题片段"

# 新页面可达性（en / zh-Hans）
curl.exe -s -o NUL -w "%{http_code}" https://today.ai/articles/finance/<slug>
curl.exe -s -o NUL -w "%{http_code}" https://today.ai/articles/zh-Hans/finance/<slug>
# 期望 200；未生效时 sleep 20s 重试（本次实测轮询 ~5 次内转为新内容）
```

> 中文路径前缀约定：`/articles/zh-Hans/<slug>`（语言段插在 `/articles/` 之后）。

---

## 五、快速命令速查

| 场景 | 命令 |
|---|---|
| 查改动 | `git status` / `git diff --stat` |
| 建 PR | `gh pr create --base main --head <分支> --title "…"` |
| 看 PR/CI | `gh pr view <编号>` / `gh pr checks <编号>` |
| 合并 | `gh pr merge <编号> --rebase --delete-branch` |
| 合并结果确认 | `gh pr view <编号> --json state` → `MERGED` |
| 对齐 main | `git checkout main && git pull --ff-only` |
| 内容校验 | `npm run validate:content` |

## 六、踩坑记录

- **直接 push main 必被拒** → 已由分支保护强制走 PR，无需尝试。
- **rebase 合并本地偶发报错/噪音**：以 GitHub 上 PR 状态为准，别反复重试 merge。
- **assets 变更**（如新增 hero 图）必须先把真实文件放进
  `public/images/<目录>/`，否则 CI 的 `validate:content` 直接失败
  （"missing on disk"），preview 都不会出。
- **hero 图生成**：Alignify apineed 管线写 `temp/today_hero_gen.py`；
  `gpt-image-2` 通道故障时以 `$env:APINEED_MODEL="gpt-image-1"` 兜底，生成后拷入 public 再走本流程。
- **article.today.ai 上的 301 防直连重定向**（`vercel.json`）属保护逻辑，不要动；
  相关 308 问题的修复在主站 today-web 侧（见 `_archive/today-ai-articles-redirect-fix.md`）。
