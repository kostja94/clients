# Dubbing AI 韩国市场本地化与 Naver Blog 增长方案

> **目的**：为在韩国通过 **Naver Blog（네이버 블로그）** 做内容增长提供可执行 SOP，涵盖账号与博客设置、首篇发文、个人/博客资料（profile）、注意事项与与官网的协同。  
> **与仓库内 Naver 资料的关系**：本方案引用并落地 [Naver 项目文档](../../../Naver/Naver-Blog.md) 与 [Naver-Blog-发布与编辑指南](../../../Naver/Naver-Blog-发布与编辑指南.md) 的实务清单；Naver 界面韩英术语与菜单位置会随产品更新，以 **发刊时官方界面** 为准。  
> **产品语境**：见 [../dubbingai.md](../dubbingai.md)（实时 AI 变声、Soundboard、dubbingai.io、游戏/直播 ICP 等）。  
> **泛用版摘要（脱敏、跨客户）**：见 [../naver-blog/korea-naver-blog-playbook-generic.md](../naver-blog/korea-naver-blog-playbook-generic.md)。  
> **整理日期**：2026-04-28

**泛用规则**（开博与法人、공식 인증、商销公示等）已写入仓库 [Naver-Blog.md 第六节](../../../Naver/Naver-Blog.md)；**本篇仅写 Dubbing AI 落地选择**。

---

## 〇、Dubbing AI 相关：账号/主体/命名的内部结论

> 以下为 **Dubbing AI 项目** 在韩渠道上的建议，不替代官方法务意见。

| 话题 | 建议 |
|------|------|
| **必须注册韩国公司才能开 Naver 博客？** | **否**。用 Naver 号即可开博发文；与是否在韩国设法人无必然关系。泛用说明见 [Naver-Blog.md 第六节 · 6.1](../../../Naver/Naver-Blog.md)。 |
| **是否立刻申请「공식 블로그」?** | **首阶段不强制**：先以 **稳定韩语内容 + 与 dubbingai.io 互链** 跑通；若需绿勾/官方背书再评估 **主体材料、官网↔博客 링크、공식 명칭** 等。门槛见 [Naver-Blog.md · 6.2](../../../Naver/Naver-Blog.md)。 |
| **用个人号还是企业邮箱注册的号？** | 推荐 **可长期接管的运营专用 Naver 账号**（公司邮箱与 **2FA 交接** 写进内部清单）；简介里写清 **「Dubbing AI / dubbingai.io 团队运营」** 即可。展示名原则见同文档 **6.3**。 |
| **展示名写「Dubbing AI Official」类英文名？** | 可作 **博客标题风格**，但须与 **商标/对外英文写法** 一致；**未获 공식** 时不要暗示「Naver 已认证官方」。见 [Naver-Blog.md · 6.3](../../../Naver/Naver-Blog.md)。 |
| **博客内卖货？** | Dubbing AI 以 **工具下载 / 订阅引流至官网** 为主，若涉及 **Dubbing Box 硬件** 代购、团购等，再按 [Naver-Blog.md · 6.4](../../../Naver/Naver-Blog.md) 与韩文法务核对 **사업자 정보** 义务。 |
| **与英文站 /blog 的分工** | 英文 Markdown 博客（见 [blog/readme.md](../blog/README.md)）主 SEO 资产在 **自站**；Naver 韩文为 **Naver 生态** 独立 HTML，**不共用** frontmatter 流水线；两边 **定价、Pro、退款** 以 [dubbingai.md](../dubbingai.md) 与线官网为准。 |

**内容选题与关键词（韩国）**：优先串 [dubbingai-features.md](../dubbingai-features.md) 中已有落地页，并对照 [dubbingai-keywords.md](../dubbingai-keywords.md) 与「실시간 보이스 체인저 / 디스코드 음성 변조 / 게임 방송」等韩文意图做 **主题簇**（可在内部 glossary 维护 `ko` 列）。

---

## 一、为什么韩国增长要单独配 Naver Blog

| 背景 | 对 Dubbing AI 的含义 |
|------|---------------------|
| 在韩国，大量用户用 **Naver 生态** 搜索与消费长文，与「只押 Google 英文站」的打法不同。 | **실시간 음성 변조 / 게임·방송 보이스 체인저 / 디스코드 설정** 等长意图适合用 **Naver Blog** 承接。 |
| 官网承担 **SSoT（价格、政策、产品真相源）**；Naver 承担 **拉新、韩文教程、讨论与社交证明**。 | 博客中关键承诺与官网 **表述一致**；重要条款以官网为准。 |
| 独立站可继续做 **GSC/GA4**；Naver 内数据看 **平台统计**，两套 **不可混读**。 | 增长汇报需分渠道；外链到 dubbingai.io 时统一 **UTM**（见第十节）。 |
| **韩国市场上「变声器」品类热度预期** | 见单独文档 [korea-voice-changer-market-context.md](./korea-voice-changer-market-context.md)（证据类型、话术边界；**非**官方检索量报表）。 |

---


## 二、开始之前：开号前须定的四件事

（与 [发布与编辑指南 · 一](../../../Naver/Naver-Blog-发布与编辑指南.md#一开写前先定的四件事) 对齐，并加上 Dubbing AI 视角）

| 事项 | 建议 |
|------|------|
| **单篇主意图** | 每篇只主打一个：Discord 变声设置 / Valorant·LOL 场景 / Soundboard 教程 / 与竞品维度对比；避免一篇塞满所有功能。 |
| **读者与语言** | 主读者为 **게이머·스트리머·크리에이터** 时，正文以 **自然韩语** 为主；品牌名、游戏名、平台名为 glossary。 |
| **博客垂类** | 全博客 **2～3 个主类目**（예：**실시간 보이스 체인저**, **게임·방송 설정**, **디스코드/OBS**），避免与无关生活类目混排。 |
| **合规** | 有广告、供稿(협찬)、赞助、礼品关系时，在文首或显著位置做 **法定义务与 Naver 发表规则** 要求的标注（见第十一节与仓库指南第九节）。 |

---

## 三、如何设置：从 Naver 账号到博客与编辑环境

### 3.1 Naver 账号

- 使用 **可长期由团队或指定负责人运营** 的 Naver ID；建议 **公司运营专用号**，非员工私人日常号。
- 内部登记 **账号、恢复方式、绑定手机/邮箱**；若注册邮箱为 **公司域名**，便于交接与审计。

### 3.2 创建或进入博客

- 在 Naver 内进入 **Blog** 服务，按向导 **开通博客**。
- 长文优先 **PC 端博客** 或官方 App 的 **스마트에디터 ONE**（详见 [发布与编辑指南 2.1](../../../Naver/Naver-Blog-发布与编辑指南.md#21-它是什么在哪用)）。

### 3.3 编辑台默认设置（第一次发文前必做）

| 设置项 | 建议 |
|--------|------|
| **기본 에디터** | **스마트에디터 ONE**。 |
| **서체/크기/자간/행간/정렬** | 长文可读；行距略大于 1.0 利手机阅读。 |
| **색상** | 正文高亮 **少而准**。 |

### 3.4 分类结构（Category / 카테고리）

- 先规划 **2～3 个主类**，与韩语选题簇一致。
- **不要**每篇随意新建冷门小类；系列文章用 **同一主类**。

---

## 四、Profile 与「博客层」品牌呈现怎么设

### 4.1 建议检查项（季度或开号时完整填一次）

- **博客名/ 표시名**：与 Dubbing AI 对外写法一致。
- **博客简介（소개）**：谁在用、解决什么问题、与 **dubbingai.io** 的关系。
- **主视觉/封面（若有）**：与品牌色协调；小屏可辨认即可。
- **对外链接**：优先链向 **dubbingai.io**（+ UTM）。

### 4.2 与「多账号/矩阵」的边界

- 避免 **一机多号、互粉互赞、异常频率**（见 [Naver 总览 五](../../../Naver/Naver-Blog.md#五合规与品牌安全)）。

---

## 五、第一篇文章怎么选、怎么写、怎么发

### 5.1 首篇主题（务实建议）

- 选 **高意图、可独立完成、少争议** 的单一场景，例如：  
  - **한 가지 플랫폼**에서 마이크 입력을 보이스 체인저로 연결하는 튜토리얼（Discord / OBS）；或  
  - **실시간 AI 보이스 체인저** 品类里 **한 차원 비교**（非诋毁竞品，以事实与体验为主）。  
- **品牌总览长文**可作后续选题；**第一篇成稿**为 **디스코드 음성 변조 튜토리얼**，见 [01-discord-voice-changer-ko-2026.md](./01-discord-voice-changer-ko-2026.md)（韩语检索中与 voice changer 强相关的 **Discord 설정** 意图簇）。

### 5.2～5.4

结构与 **발행屏检查**、**发后行为** 与仓库 [发布与编辑指南](../../../Naver/Naver-Blog-发布与编辑指南.md) 一致：제목·리드·H2/H3·표·ALT·미리보기·태그·공개·검색·댓글/공감·대표 이미지。

### 5.5 与官网的链接与 CTA

- 文内 CTA 链向 **dubbingai.io** 时带 UTM（第十节）。  
- 价格、订阅、退款等 **以官网为准**；博客可做摘要但避免过期数字长期不更新。  
- 与 [blog/internal-external-links-checklist.md](../blog/internal-external-links-checklist.md) 分层链接精神一致。

### 5.6 附录：第一篇韩文成稿（ONE）— 디스코드 음성 변조 튜토리얼

**成稿位置**：[01-discord-voice-changer-ko-2026.md](./01-discord-voice-changer-ko-2026.md)。**选题**：韩语中与 **voice changer** 强相关的 검색 클러스터 중 **「Discord + 음성 변조 / 보이스 체인저」**（竞品韩语 SERP 高频）；**非**纯 brand intro。**未获 Naver「공식 블로그」认证时，勿暗示 플랫폼 공식 인증**。

**建议 카테고리 / 태그 / UTM**

| 项 | 建议 |
|----|------|
| **카테고리** | **디스코드 / 게임 음성** 또는 **실시간 보이스 체인저** 主类之一。 |
| **태그** | 少而精：`디스코드`, `음성 변조`, `보이스 체인저`, `실시간`（忌堆砌）。 |
| **UTM** | 본문·공식 랜딩：`utm_content=discord_vc_guide`；다운로드 CTA：`discord_vc_download_cta`。 |

**正文大纲要点**（详见成稿）：리드 → 핵심 한눈에 → 준비물 → **디스코드 설정 순서** → 트러블슈팅 → 보이스 체인저 선택 체크리스트 → Dubbing AI 공식 Discord 페이지·다운로드 CTA → FAQ。

---

## 六～八、可发现性、数据复盘、一页 Checklist

与仓库 [Naver-Blog-发布与编辑指南](../../../Naver/Naver-Blog-发布与编辑指南.md) 第四～七节一致；落地时域名与品牌检查项一律按 **dubbingai.io** / **Dubbing AI**。

---

## 九、常见问题（首月高频）

| 问题 | 建议 |
|------|------|
| 必须用 SmartEditor ONE 吗？ | **强烈建议**。 |
| 只发英文稿可以吗？ | 在韩国，**韩语** 通常是触达与信任主体。 |
| CTA 链到哪里？ | **dubbingai.io** `/download-desktop`、`/discord-voice-changer`、`/voice-changer-for-gaming` 等（见 [dubbingai-site-structure.md](../dubbingai-site-structure.md)）。 |

---

## 十、UTM 示例（与官网互链时）

- `https://dubbingai.io/?utm_source=naver_blog&utm_medium=social&utm_campaign=kr_growth_2026&utm_content=first_post`  
- 功能页：`utm_content=discord_vc_guide`、`discord_vc_download_cta`、`valorant_xxx` 等与内部报表对齐。

---

## 十一、合规与品牌安全（韩国 + 平台）

- **광고、협찬** 等按韩国标识义务与 Naver 规则标注（见 [发布与编辑指南 九](../../../Naver/Naver-Blog-发布与编辑指南.md#九合规与标注)）。  
- **游戏条款·反作弊**：各 게임·플랫폼 이용약관을 준수；본문에서 **계정 보장·우회** 암시 금지。  
- **声音克隆·名人音色**：저작권·초상·플랫폼 정책 준수；과장 광고 금지。

---

## 十二、仓库内待补充（由团队本地完善）

- 打码后的后台截图：기본 에디터、발행屏、모바일 미리보기  
- **品牌韩文表记、标语、CTA、禁用词**  
- 已发布 **Naver 文章 URL 登记表**

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [Naver-Blog.md](../../../Naver/Naver-Blog.md) | 泛用：§六 开博/法人/공식 |
| [dubbingai.md](../dubbingai.md) | 产品、URL、ICP |
| [dubbingai-features.md](../dubbingai-features.md) | 功能页路径 |
| [dubbingai-keywords.md](../dubbingai-keywords.md) | 关键词 |
| [blog/readme.md](../blog/readme.md) | 英文 blog 与 Naver 分工 |
| [../naver-blog/README.md](../naver-blog/README.md) | 泛用索引 |
