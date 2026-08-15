# BiP · 即刻 — FIFA World Cup 2026 专题页

> **状态**：draft（待发）  
> **主题**：Build in Public · 世界杯 vertical landing（设计 / SEO / preset）  
> **语言**：ZH · 深度长文 · 正式语气  
> **关联页面**：https://oginify.com/fifa-world-cup-image-generator

---

## 正文（纯文本 · 可直接粘贴即刻）

Build in Public 进度记录：Oginify 已上线 2026 FIFA World Cup 专题页。距赛事开幕（2026 年 6 月 11 日）约两周，页面以「时效性 vertical landing + 产品 preset 预调优」为定位先行发布，后续将依据 GSC 检索表现与生成转化数据迭代。

本页在信息架构上独立于通用 OG Generator 首页。通用首页主要承接「og image generator」类交易型检索；世界杯页则按输出规格与用户场景拆分为三个内容模块——Banner generator（1200×630）、Poster generator（1080×1080）、Story generator（1080×1350），分别覆盖链接预览、社媒方图、竖版 Story / 倒计时等检索 intent。页面 Title、Meta Description、FAQ 及结构化数据（SoftwareApplication、FAQPage）均按上述规格与场景单独撰写，与站内 Twitter Card 页、use case pSEO 线路同属「按搜索 intent 切片、复用同一生成能力」的增长策略，差异在于本次绑定全球赛事时间窗口。

视觉层面，整页采用六层纵向连续手绘背景（Hero、Generator、Banner、Poster、Story、Closing），形成统一的赛事视觉系统，而非在通用 SaaS 模板上替换标题文案。交互区下方三个 section 各自主打一种输出比例，并对应一座 2026 主办国球场意象：Banner 模块为墨西哥阿兹特克球场（1200×630 横版），Poster 模块为美国现代球场（1080×1080 方图），Story 模块为多伦多 BMO Field 与 CN Tower（1080×1350 竖版）。三块背景共用同一设计语法——一侧为奶油色文案区，另一侧为球场摄影；卡片区域在背景中预先绘制形状与画面，前端通过透明内区、描边框与文字 overlay 叠加，使球场影像从背景层透出。设计意图在于：用户滚动至各 section 时，无需先执行 Generate，即可建立对输出形态的直观预期，降低首次使用的心理门槛。

功能层未另起技术栈，仍沿用 Oginify 现有 AI 管线（页面理解、图像生成、浏览器端裁切）。与通用 Generator 的差异在于 preset 层：六个赛事 scene（赛报海报、球场、奖杯、球员致敬、倒计时、球迷横幅）替换通用 style chip；尺寸列表调整为赛事期间高频分享的五种格式；prompt 固定 2026 语境，并内置商标护栏（默认不生成 FIFA 官方标识、2026 官方 emblem、Jules Rimet 造型等）。FAQ 已明确说明与 FIFA 无隶属或许可关系，输出适用于 fan、editorial 及多数独立商业场景。输入支持 Text、URL、Reference image 三种模式，其中 URL 模式读取目标页的 og:title 与 og:description 作为生成上下文，适用于赛报、赛程及球队页面。

当前阶段尚处 early stage，event vertical 相对通用首页的转化效率有待 GSC 与 GA 数据验证。若您从事内容运营、体育媒体或赛事相关传播，欢迎就页面信息架构、scene 覆盖范围及生成效果提供反馈。

https://oginify.com/fifa-world-cup-image-generator

---

## 发布后回填

- [ ] 将 [post.meta.yaml](./post.meta.yaml) 中 `jike.status` 改为 `published`
- [ ] 填入 `jike.url` 与 `jike.published_at`
- [ ] 更新 [index.md](../../index.md) BiP 帖列表

---

*Archived: 2026-06-01*
