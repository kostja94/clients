## §4 已有内容图谱

### 4.1 文件表与下一序号

| NN | 文件 | slug | 类型 | 文稿 | 主站 | 主关键词 |
|----|------|------|------|:---:|:---:|---------|
| 01 | 01-what-is-hellyeah-ai.md | `/blog/what-is-hellyeah-ai` | PlatformExplainer | ✅ | draft | Hellyeah AI |

> **状态说明**：文稿 ✅ = 本地已有完整稿；主站 draft = sitemap 未收录（2026-06-02）；主站 live = hellyeahai.com 可访问。

**下一序号：02**

### 4.2 Hub-Spoke 结构（规划）

```
                    ┌─────────────────────────────────────┐
                    │  01 What Is Hellyeah AI (Intro Hub)  │
                    │  Command layer + four-platform OS    │
                    └──────────────┬──────────────────────┘
                                   │
     ┌─────────────┬───────────────┼───────────────┬─────────────┐
     │             │               │               │             │
  (02 planned) (03 planned)   (04 planned)    (05 planned)  (06 planned)
  programmatic continuous   what-is-ai-    aima-vs-       enterprise
  geo pillar   growth       ads-manager    forge          security
               experiments
```

**阅读旅程**：平台介绍 → GEO 全景 → 实验方法论 → AI ads 教育 → 合规采购

### 4.3 P0 队列

| 优先级 | 类型 | slug | 主关键词 | 内链锚 |
|--------|------|------|---------|--------|
| P0 | Framework | `continuous-growth-experiments` | continuous growth experiments | `/deja-vu` |
| P1 | CommercialEducational | `what-is-ai-ads-manager` | AI ads manager | `/aima` |
| P1 | PlatformExplainer | `aima-vs-forge-vs-mutation` | AI growth platform architecture | 四平台 |
| P2 | Compliance | `enterprise-marketing-platform-security` | SOC 2 marketing platform | `/security` |

### 4.4 Canonical Concept Registry

| 概念 | Canonical slug / 路径 | 引用方式 |
|------|----------------------|---------|
| Programmatic GEO 定义与能力 | `/capabilities/seo-geo` | 1–2 句 + **必须 link**（P5） |
| GEO vs SEO 分工地图 | `programmatic-geo-vs-seo` | Pillar 全文；Spoke 引述 + link |
| 连续实验方法论 | `continuous-growth-experiments`（planned） | 1–2 句 + link |
| AI ads manager 品类 | `what-is-ai-ads-manager`（planned） | 1–2 句 + link |
| 四平台 OS 分层 | `aima-vs-forge-vs-mutation`（planned） | 1–2 句 + link |
| RCLL 增长循环 | `/` · `/about` | 定义在此；他文引用不展开 |

### 4.5 冲突表（MERGE 对照）

| 新选题关键词 | 已有 canonical | 判定 |
|-------------|---------------|------|
| programmatic GEO / generative engine optimization / LLM SEO | 01 Pillar + `/capabilities/seo-geo` | Spoke 链 Pillar；不重复 Pillar 核心表 |
| AI search visibility how-to | 01 + seo-geo | MERGE 进 Pillar 或写 Spoke（KEEP 若角度为 vertical） |
| what is GEO | 01 + seo-geo | MERGE 除非 vertical-specific |
| continuous A/B testing platform | 02 planned | KEEP 若 Framework 角度 |
| AI ads manager vs dashboard | 03 planned | KEEP CommercialEducational |

### 4.6 跨篇边界声明模板

**Spoke 开篇（链 GEO Pillar）**：
> If you are still mapping how programmatic GEO fits alongside classic SEO, start with our [programmatic GEO vs SEO division of labor](/blog/programmatic-geo-vs-seo).

**GEO ↔ capability 页**：
> For Hellyeah's programmatic GEO engine specs and output volume, see the [SEO / GEO capability page](/capabilities/seo-geo) — this article explains the strategic framework, not product configuration.

---

## §7 文件命名与 README 同步

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{working-slug}.md` |
| NN | 两位递增；当前下一号为 **02** |
| frontmatter `slug` | `/blog/{url-slug}` |
| 成稿路径 | `hellyeah/blog/NN-{slug}.md` |

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 管理）。

**成稿后**：Agent 提示人类更新 `hellyeah/blog/README.md` 文件表。**Skill 不自动改 README。**
