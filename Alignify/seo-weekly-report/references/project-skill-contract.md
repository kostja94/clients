# 项目配置契约

复制本文件夹为 `{project}-seo-weekly-report/` 时，除改 `config/` 外可选覆盖下列项。

---

## 必填（config/）

| 文件 | 用途 |
|------|------|
| project-config.yaml | 站点 ID、URL、health 阈值、conversionEvents |
| brand-query-registry.yaml | 品牌词拆分 |

---

## 可选

| 文件 | 用途 |
|------|------|
| landing-page-rules.yaml | GA4 落地页分类 |
| content-catalog.yaml | 内容清单（slug、date、title）— merge 填 content.weeklyNewPosts |
| backlink-registry.yaml | 未来：Referral 自动匹配 |

---

## SKILL 覆盖（同目录可选）

若需定制语气/阈值/章节，可新增 `project-skill-overlay.md`：

- 站点一句话定位
- 周点击「正常」基线描述
- 额外章节（如多语言、多属性）
- **禁止**引用文件夹外路径

Agent 加载顺序：`SKILL.md` → `project-skill-overlay.md`（若存在）→ `config/*`

---

## 自包含检查清单（发给客户前）

- [ ] 无其他仓库路径、无客户名、无内网 URL  
- [ ] `.env` 不在包内（仅 `.env.example`）  
- [ ] `data/`、`reports/` 示例已剥离或脱敏  
