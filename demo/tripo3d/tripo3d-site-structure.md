# Tripo3D 网站结构（IA 推断）

> 关联：[tripo3d.md](./tripo3d.md) | [tripo3d-features.md](./tripo3d-features.md) | [tripo3d-keywords.md](./tripo3d-keywords.md)

**Last updated**: 2026-05-08

**说明**：以下基于 [tripo3d.ai](https://www.tripo3d.ai/) 公开可见内容、博客文章与第三方报道推断；**非**经完整爬虫验证的站点地图。路由变更后需更新。

---

## 一、顶层导航（推断）

| 项 | 说明 |
|----|------|
| 品牌 | Tripo3D / Tripo AI |
| 主导航（推断） | Products（下拉：Text-to-3D / Image-to-3D / Tripo Studio / Models）· Pricing · Blog · API · Game Hub · About |
| 账户 | Log in · Sign up（Google / Email / 等） |
| 语言 | 英文为主（中文博客存在但未知是否有 `/zh` 主站） |
| 信任 | About、Contact、Privacy、Terms（基础必备页） |

---

## 二、首页信息架构（逻辑块推断）

| 模块（顺序示意） | 内容 | 备注 |
|------------------|------|------|
| Hero | 核心价值主张 + 主要 CTA（Text-to-3D / Image-to-3D 入口） | 应包含关键数字（6.5M+ 创作者 / 100M 模型） |
| 模型矩阵 | H3.1 / P1.0 / W1.0 / Tripo 3.0 的视觉与简要定位 | 适合做型号对比卡片，可分 H / P / W 三列 |
| Tripo Studio 亮点 | 智能分割 / Smart Low-Poly / Magic Brush / Uni-Rig 四大能力 | 适合 GIF / 视频演示工作流 |
| 行业方案 | Gaming / Filmmaking / 3D Printing / XR / Robotics 的轻量入口 | 下拉或 Tab，内链到垂直落地页 |
| 社会证明 | 用户数 / 开发者数 / 合作品牌（Sony / 网易 / Replit） / 融资信息 | 融资 $50M 应突出 |
| 社区 / Game Hub | 精选可玩项目 / 模板 | 吸引开发者与玩家双人群 |
| CTA | Start for free / Try Tripo Studio / API access | 区分 C/开发者/企业三条路径 |

---

## 三、主要 URL 推断（已验证或高度可能）

| 路径 | 用途 |
|------|------|
| https://www.tripo3d.ai/ | 首页 |
| /products/text-to-3d | Text-to-3D 功能页 |
| /products/image-to-3d | Image-to-3D 功能页 |
| /tripo-studio | Tripo Studio 工作台（Web 入口） |
| /models | 模型矩阵总览页（H3.1 / P1.0 / 3.0 / W1.0 卡片） |
| /models/h3-1 | H3.1 详情 + API 入口 |
| /models/smart-mesh-p1 | P1.0 详情 + API 入口 |
| /pricing | 定价页（免费层 / API 按量 / 企业方案） |
| /blog | 博客首页 |
| /blog/introducing-tripo-studio | Tripo Studio 发布文 |
| /api | 开发者文档 / API 控制台 |
| /game-hub | Tripo Game Hub |
| /about | 关于 VAST / 团队 / 使命 |
| /contact | 联系页（企业咨询 / 商务） |

---

## 四、建议新增的核心落地页（内容机会）

### 4.1 行业垂直页（P0，承接高意图长尾）

| 路径（建议） | 覆盖关键词簇 | 内链策略 |
|--------------|-------------|----------|
| `/for-games` | AI 3D for games, game asset generator, Unity AI 3D | → /models/smart-mesh-p1, /tripo-studio, /text-to-3d |
| `/for-3d-printing` | AI for 3D printing, STL generator, photo to 3D print | → /products/image-to-3d, /pricing |
| `/for-filmmaking` | AI for filmmaking, previs, concept design 3D | → /models/h3-1, /tripo-studio |
| `/for-xr` | AI for AR/VR, XR asset generation | → /models/smart-mesh-p1 |
| `/for-robotics` | AI for robotics simulation, 3D training data | → /api, /models |

### 4.2 对比页（P1，承接竞品搜索）

| 路径（建议） | 覆盖 |
|--------------|------|
| `/vs/meshy` | Tripo3D vs Meshy |
| `/vs/luma` | Tripo3D vs Luma AI |
| `/vs/csm` | Tripo3D vs CSM |
| `/alternatives/meshy` | Meshy alternatives（搜索综述承接） |

### 4.3 工具/能力单页（P1，承接 Studio 长尾）

| 路径（建议） | 覆盖 |
|--------------|------|
| `/intelligent-segmentation` | AI 3D segmentation |
| `/smart-low-poly` | AI low poly generator |
| `/magic-brush` | AI 3D texture brush |
| `/uni-rig` | AI auto rigging |
| `/features/pbr-materials` | PBR 材质生成说明 |

### 4.4 中文站（P2，若扩展中国市场）

| 路径 | 说明 |
|------|------|
| `/zh` 或独立子域 `zh.tripo3d.ai` | 中文主站，hreflang 双链路 |
| `/zh/blog` | 中文博客 |
| 各行业页的中文版 | /zh/for-games 等 |

---

## 五、技术 SEO 检查清单

| 项 | 要求 |
|----|------|
| **Canonical** | 每页自引用 canonical；`www` vs 裸域选一 301 |
| **Hreflang** | 若中英双语站：en / zh / x-default 完整声明 |
| **Structured Data** | 首页 `Organization` / `WebSite`（含 SearchAction 若适用）；模型页 `SoftwareApplication`；Blog `Article`；FAQ 页 `FAQPage` |
| **Sitemap** | 分片 sitemap（/models/、/blog/、/tools/ 按需），主 sitemap.xml 汇总 |
| **Core Web Vitals** | 3D 模型预览可能影响 LCP——建议用缩略图 + 点击加载，避免首屏 WebGL 阻塞 |
| **内链** | 首页 → 模型总览 → 单模型页 → API/Pricing；行业页 → 对应功能页；Blog → 产品页 CTA |
| **Robots** | API 控制台 / 登录 / 用户生成内容页按需 `noindex` |
| **URL 规范** | 全站小写 + 连字符 slug；避免带参 URL（?ref=）产生重复索引 |

---

## 六、内容 / SEO 优先级建议

| 优先级 | 动作 |
|--------|------|
| **P0** | Home / Pricing / Models 核心三页内容核对与内链闭环；确保品牌词 SERP 首页干净（融资报道、官网、百科） |
| **P0** | Text-to-3D / Image-to-3D 两个核心入口页 H1+描述+CTA 完整；避免仅依赖导航 |
| **P0** | 行业垂直页 `/for-games` + `/for-3d-printing`（两个最高意图行业长尾） |
| **P1** | 模型卡片页（H3.1 / P1.0 / 3.0 / W1.0）每页独立、有参数表 + 示例 + API 入口 |
| **P1** | Tripo Studio 四大能力单页（Segmentation / Low-Poly / Magic Brush / Uni-Rig） |
| **P1** | Blog 持续产出：技术深度文（原生 3D 扩散原理）、行业案例（游戏/打印/影视）、对比评测 |
| **P1** | `/vs/*` 对比页首发 3 篇（Meshy / Luma / CSM） |
| **P2** | Game Hub 的 SEO 化（可搜索项目、可索引模板）——平衡 Robot 索引与动态内容质量 |
| **P2** | 中文站（若中国市场有投入）hreflang + 独立中文内容管线 |
| **P2** | `/for-robotics`、`/for-xr` 等长尾行业页 |

---

## 七、技术栈推测

- 前端框架：需通过 Response header、静态资源路径（`/_next` / `/_nuxt` 等）判断  
- 3D 预览：可能使用 Three.js / WebGL（在模型详情页与 Studio 内）  
- API 网关：需查看 API 文档域（可能为独立子域或第三方如 WaveSpeedAI）  
- CMS：Blog 可能基于 MDX / Headless CMS；需查看页面结构判断  

---

## 八、待工程确认

- [ ] 实际 slug 与本文推断路径的一致性（尤其 `/tripo-studio` vs `/studio` 等变体）  
- [ ] App 子域（如 `app.tripo3d.ai`）与主站 SEO 分工  
- [ ] API 文档域（独立域 or 同域 `/docs` 子路径）与索引策略  
- [ ] Game Hub 是否为独立 Web 应用 / 子域——是否需要独立 SEO 策略  
- [ ] 中文站的实际存在形态（子域 / 路径 / 独立站）与 hreflang 配置  

---

*文档日期：2026-05-08*
