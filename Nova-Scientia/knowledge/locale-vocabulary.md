# 语言变体差异对照表（Locales Vocabulary Reference）

> 供内容编辑与 AI 助手在**多语言内容翻译/改写**时查阅。编辑 `content/locales/{locale}/` 前先读本表，避免用错地域词汇或句式。
> **Last updated**: 2026-08-08（v2：精简为 5 市场，移除 es-CO/es-AR/es-CL，新增 en-US）

---

## 一、用途与使用方式

1. 翻译产品/主题/公司 JSON 前 → 查阅本文档对应语言列
2. 核心原则：**变体之间不是「逐词翻译」，而是「按地域改写」**——同一含义用不同词、不同句式、不同人称
3. 优先级：**人称变位 + 核心词汇 + 元数据关键词** 是差异最大的三层，必须本地化
4. 可完全复用（不区分）：产品 slug、图片 URL、外链 URL、toc id、stats 数值

---

## 二、语言与地区总览

| Locale | 地区 | 语言 | `<html lang>` | OG locale | 人称系统 |
|--------|------|------|---------------|-----------|----------|
| `pt-br` | 巴西 | 葡萄牙语（巴西） | `pt-BR` | `pt_BR` | `você` |
| `pt-pt` | 葡萄牙 | 葡萄牙语（欧洲） | `pt-PT` | `pt_PT` | `você`（书面）/ `tu`（口语） |
| `es-mx` | 墨西哥 | 西班牙语（墨西哥） | `es-MX` | `es_MX` | `tú` |
| `es-es` | 西班牙 | 西班牙语（卡斯蒂利亚） | `es-ES` | `es_ES` | `tú`（单数）/ **`vosotros`**（复数） |
| `en` | 美国 | 英语（美国） | `en-US` | `en_US` | `you` |

---

## 三、人称与语法差异

### 3.1 葡萄牙语：pt-BR vs pt-PT

| 语法维度 | pt-BR | pt-PT | 示例（BR → PT） |
|----------|-------|-------|-----------------|
| 现在进行体 | 动名词 `-ndo` | `estar a + 不定式` | `estou testando` → `estou a testar` |
| 第二人称 | `você`（全站统一） | 书面 `você`；口语 `tu` | `você pode` → `podes`（tu） |
| 代词位置 | 动词前（proclítico） | 动词后（enclítico） | `me ajuda` → `ajuda-me` |
| 完成时使用 | 简单过去为主 | `ter + particípio` 表持续 | `já usei` → `tenho usado` |
| 祈使句 | `veja` / `acesse` | `vê`（tu）/ `veja`（você） | 统一写 `veja` 两边都安全 |

**黄金规则**：拿不准时用 `você` + 动词第三人称变位 + 动名词改为 `estar a` 结构——pt-PT 通用。

### 3.2 西班牙语：es-MX vs es-ES

| 人称 | es-MX | es-ES |
|------|-------|-------|
| 单数你 | `tú` | `tú` |
| 复数你们 | `ustedes` | **`vosotros`** |
| 动词示例（拥有） | `tienes` | `tienes` / `tenéis` |
| 祈使 | `mira` | `mira` / `mirad` |
| 时态偏好 | 简单过去（`vi`） | **现在完成**（`he visto`） |

**es-ES 特别注意**：`vosotros` 只影响"你们"；正文多用 `tú` + 现在完成时态。

### 3.3 英语：en-US

| 维度 | 说明 |
|------|------|
| 人称 | `you`（无 T-V 区分），祈使 = 动词原形（`Click here`、`Explore tools`） |
| 时态 | 无口语/书面变位差异；美国英语拼写（`optimize`、`color`、`analyze`） |
| 注意事项 | 科技/AI 术语直接用英文（`prompt`、`image generator`、`AI tools`）；产品名保持品牌原文 |

---

## 四、葡萄牙语核心词汇对照（pt-BR ↔ pt-PT）

### 4.1 高频生活/科技词

| 中文 | pt-BR | pt-PT |
|------|-------|-------|
| 手机 | celular | telemóvel |
| 电脑 | computador | computador（同） |
| 鼠标 | mouse | rato |
| 键盘 | teclado | teclado（同） |
| 下载 | baixar / download | transferir |
| 上传 | enviar / upload | carregar / enviar |
| 软件应用 | aplicativo | aplicação |
| 登录 | entrar / logar | iniciar sessão |
| 注销 | sair | terminar sessão |
| 密码 | senha | palavra-passe |
| 用户名 | usuário / nome de usuário | utilizador / nome de utilizador |
| 免费试用 | teste grátis | teste gratuito（同义，`grátis` BR 口语） |
| 订阅 | assinatura | subscrição |
| 退款 | reembolso | reembolso（同） |
| 发票 | nota fiscal | fatura |
| 公交车 | ônibus | autocarro |
| 冰柜 | geladeira | frigorífico |
| 冰激凌 | sorvete | gelado |
| 男孩/女孩 | garoto / menina | rapaz / miúda |
| 非常棒 | legal / maneiro | fixe |
| 现在 | agora | agora（同） |
| 点击 | clicar | clicar（同）/ carregar（口语） |
| 搜索 | pesquisar | pesquisar（同）/ procurar |
| 广告 | anúncio | anúncio（同）/ publicidade |

### 4.2 AI 工具站专属词

| 中文 | pt-BR | pt-PT |
|------|-------|-------|
| 提示词 | prompt | prompt（同，原样用） |
| 大语言模型 | modelo de linguagem grande / LLM | modelo de linguagem de grande escala / LLM |
| 生成 | geração | geração（同） |
| 训练 | treinamento | treino / treinamento |
| 功能 | funcionalidades | funcionalidades（同）/ recursos |
| 价格 | preço | preço（同） |
| 计划/套餐 | plano | plano（同）/ pacote |
| 客户支持 | suporte ao cliente | apoio ao cliente |
| 工作区 | espaço de trabalho | espaço de trabalho（同）/ área de trabalho |
| 集成 | integração | integração（同） |
| 企业版 | versão empresarial | versão empresarial（同）/ corporativa |
| 评分 | avaliação | avaliação（同）/ classificação |
| 对比 | comparação | comparação（同） |
| 优点/缺点 | prós e contras | prós e contras（同）/ vantagens e desvantagens |

> **提示**：pt-BR 与 pt-PT 大量科技词相同（`geração`、`preço`、`funcionalidades`），真正差异集中在**生活词、登录/下载类操作词、进行时句式**。

---

## 五、西班牙语核心词汇对照（es-MX ↔ es-ES）+ 英语参考

### 5.1 高频生活/科技词

| 中文 | es-MX | es-ES | en-US |
|------|-------|-------|-------|
| 电脑 | computadora | **ordenador** | computer |
| 手机 | celular | **móvil** | cell phone / mobile |
| 下载 | descargar | descargar（同） | download |
| 上传 | subir | subir（同） | upload |
| 密码 | contraseña | contraseña（同） | password |
| 用户名 | usuario | usuario（同） | username |
| 登录 | iniciar sesión | iniciar sesión（同） | sign in / log in |
| 免费试用 | prueba gratis | prueba gratuita | free trial |
| 订阅 | suscripción | suscripción（同） | subscription |
| 退款 | reembolso | reembolso（同） | refund |
| 开车 | manejar | **conducir** | drive |
| 公交车 | camión | **autobús** | bus |
| 果汁 | jugo | **zumo** | juice |
| 草莓 | fresa | fresa（同） | strawberry |
| 很棒 | padre/chido | guay/chulo | great / awesome |
| **`coger`** | ⚠️ 冒犯 | ✅ 正常（拿/搭乘） | —（用 `take`/`grab`） |

### 5.2 AI 工具站专属词

| 中文 | es-MX | es-ES | en-US |
|------|-------|-------|-------|
| 提示词 | prompt | prompt（同） | prompt |
| 大语言模型 | modelo de lenguaje grande / LLM | modelo de lenguaje de gran escala / LLM | large language model / LLM |
| 生成 | generación | generación（同） | generation |
| 训练 | entrenamiento | entrenamiento（同） | training |
| 功能 | funciones | funciones（同） | features |
| 价格 | precio | precio（同） | price / pricing |
| 计划 | plan | plan（同） | plan |
| 客户支持 | soporte | soporte（同）/ atención al cliente | customer support |
| 工作区 | espacio de trabajo | espacio de trabajo（同） | workspace |
| 集成 | integración | integración（同） | integration |
| 企业版 | versión empresarial | versión empresarial（同） | enterprise version |
| 评分 | calificación | calificación（同）/ valoración | rating |
| 对比 | comparación | comparación（同） | comparison |
| 优点/缺点 | pros y contras | pros y contras（同） | pros and cons |

> **提示**：西语 AI 科技词高度统一，主要差异在 es-ES 的 `ordenador`/`móvil`/`vosotros`/`gratuito`；英语直接用科技术语原文。

---

## 六、本地货币与定价展示

| Locale | 货币代码 | 显示示例 | 说明 |
|--------|----------|----------|------|
| `pt-br` | BRL | R$ 20/mês | 巴西雷亚尔 |
| `pt-pt` | EUR | 20 €/mês | 欧元 |
| `es-mx` | MXN | $20/mes | 墨西哥比索 |
| `es-es` | EUR | 20 €/mes | 欧元 |
| `en` | USD | $20/mo | 美元 |

> 定价字段 `content.pricing.plans[].monthly` 若原样保留美元产品价（如 `$20/mês`），建议在 `note` 中补充当地币种说明；产品实际售价以官网为准，不臆造本地价。

---

## 七、元数据本地化要点（关键词差异）

### 7.1 葡语元数据关键词

| 中文 | pt-BR | pt-PT |
|------|-------|-------|
| AI 工具 | ferramentas de IA | ferramentas de IA（同） |
| 最佳工具 | melhores ferramentas | melhores ferramentas（同） |
| 图片生成器 | gerador de imagem | gerador de imagem（同） |
| 语音转文字 | voz para texto | voz para texto（同） |

> 葡语两变体元数据关键词几乎无差异（拼写已统一），`seo_title`/`seo_description` 基本可复用，重点改正文句式即可。

### 7.2 西语 + 英语元数据关键词

| 中文 | es-MX / es-ES | en-US |
|------|---------------|-------|
| AI 工具 | herramientas de IA | AI tools |
| 最佳工具 | mejores herramientas | best tools |
| 图片生成器 | generador de imágenes | image generator |
| 免费 | gratis（MX）/ gratuito（ES） | free |
| 对比/评测 | comparación / análisis | review / comparison |

---

## 八、翻译工作流速查（对应分级）

| 级别 | 适用页面 | 必做项 |
|------|----------|--------|
| **L1 深度** | 高流量主题页（llm、image-generator、chatbot、video-generator 等） | 全量改写：人称变位 + 句式 + 核心词 + 元数据 + 本地补充 |
| **L2 中度** | 热门产品评测 | 词汇替换 + 句式调整 + 元数据，正文细节可保留 |
| **L3 轻量** | 长尾产品 | 元数据本地化 + 首段改写 |

**本地化补充示例**（L1 差异化武器）：
- es-MX：用墨西哥定价语境（MXN）
- es-ES：用欧葡/欧西句式（`estar a` 结构 pt-PT、`vosotros`/`he visto` es-ES）
- en-US：英语科技表达 + 美国定价语境（USD）

---

## 九、维护规则

- 编辑某 locale 内容前，先在本表确认该变体的：**人称系统 → 核心词 → 元数据关键词**
- 新增词汇 → 追加到对应语言表格，保持结构一致
- 校对：翻译完成后的 JSON 用 `npm run validate:products` 门禁（仅校验结构，不校验语言）——**语言正确性靠本表人工把关**
- 对照索引：主题关键词规划见 [keyword-map.md](../specs/keyword-map.md)；路由规划见 [i18n-route-plan.md](../specs/i18n-route-plan.md)；翻译流程见 [i18n-content-workflow.md](../specs/i18n-content-workflow.md)
