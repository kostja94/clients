# Dynal 项目文档

> 文档维护遵循 [dynal-文档编写规范](./dynal-文档编写规范.md)：主题一致、去重引用、内容聚焦、相关文档互链。

**说明**：**主产品功能**以 [dynal-features.md](./dynal-features.md) 为准；**`/tools/` 小工具**以 [dynal-tools.md](./dynal-tools.md) 为准（**工具 #1** 另见 [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)），边界见 tools **§0**。*vs ChatGPT* 事实表在 features **第三节**；*品牌/信任* 与 *SEO 执行清单* 在 [dynal.md](./dynal.md) §8、§10；*URL / sitemap* 在 [dynal-site-structure.md](./dynal-site-structure.md)。**增删或更名文档时**，请同步更新下表与 [dynal.md](./dynal.md) 第一节「文档体系」表，避免双源不一致。

## 文档索引

| 文档 | 主题 |
|------|------|
| [dynal.md](./dynal.md) | 产品营销上下文（入口）、信任标识、vs ChatGPT SEO 要点、**执行清单**（§10）、**增长与市场侧重**（§11） |
| [dynal-features.md](./dynal-features.md) | **主产品功能**与工作流、**功能模块拆解**（调研）、Brand DNA、官网对比表、**产品优化备注**（§七）；≠ 小工具 |
| [dynal-use-cases.md](./dynal-use-cases.md) | **目标用户 × 使用场景**、Persona、情境故事线 |
| [dynal-keywords.md](./dynal-keywords.md) | 关键词映射、**搜索量/竞争度估算表**（需工具复核） |
| [dynal-competitors.md](./dynal-competitors.md) | **竞品格局**（Copy.ai、Taplio、ContentIn 等）、差异化与拦截 |
| [dynal-site-structure.md](./dynal-site-structure.md) | **网站结构、多语言 URL、[sitemap](https://dynal.ai/sitemap.xml)、robots** |
| [dynal-production-routing.md](./dynal-production-routing.md) | **主域 Rewrite / 反向代理**：`/linkedin-post-generator` hub 留主应用、子路径转 **https://dynal-nextjs.vercel.app**；多语言 **`/{locale}/...`** 与子站路由对齐 |
| [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md) | **LinkedIn Post Generator**（子文件夹）：路由与定位、**工具 #1**；关键词/竞品/topic 详表见子文档 |
| [dynal-tools.md](./dynal-tools.md) | **`/tools/` 引流小工具**（**#2–#12** 详表）；**§1.7** 竞品工具页侧证（#1 指专档）；边界 **§0** |
| [dynal-文档编写规范.md](./dynal-文档编写规范.md) | **文档撰写与格式规范**：标题、表格、互链、命名约定、自检清单 |

**官网**：[https://dynal.ai/](https://dynal.ai/)

**主产品定位**（权威全文�