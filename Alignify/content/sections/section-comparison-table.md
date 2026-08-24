# 对比表格（Table）章节最佳实践

本文档定义对比表格章节的规范，适用于 Tools 页面的产品功能对比。

**来源**：`src/components/Table.tsx` → `src/content/render/ArticleFromJson.tsx`（部署仓源码）。

---

## 〇、两种 JSON block type

Table 组件通过 ArticleFromJson 以两种 JSON block type 调度：

### 1. `comparisonSection`（推荐，最常用）

```json
{
  "type": "comparisonSection",
  "h2Id": "best-tools-comparison",
  "h2Text": "{工具类型}对比",
  "introHtml": "以下是主流{工具类型}工具的对比...",
  "table": {
    "toolType": "AI图片工具",
    "toolTypeEn": "AI Image Tools",
    "columns": ["功能类型", "核心特点", "主要应用场景", "定价模式"],
    "items": [
      {
        "toolName": "产品名",
        "coreFeatures": "关键词1、关键词2、关键词3",
        "bestFor": "最适合场景",
        "pricing": "定价",
        "integrations": "扩展信息"
      }
    ]
  }
}
```

**字段说明**：
- `h2Id` / `h2Text`：H2 标题（优先使用 `h2Text`，fallback `title`）
- `introHtml`：引导段落（优先使用 `introHtml`，fallback `introduction`）
- `table.items`：**嵌套在 `table` 下，不是顶层字段**

### 2. `table`（可选 H2 + intro）

```json
{
  "type": "table",
  "id": "optional-anchor",
  "title": "可选 H2 标题",
  "introduction": "可选引导段",
  "table": {
    "items": [...]
  }
}
```

**区别**：`title` 和 `introduction` 均可选，无则直接渲染表格。

### 3. `html` 块中手写 Table 组件

在 `html` block 中直接使用 React `<Table>` 组件的三种模式（见 §二）。适用于无法用 JSON 结构化的场景。

---

## 一、字数与规范层级：硬底线 vs 建议（必读）

| 层级 | 适用 | 说明 |
|------|------|------|
| **A 硬底线** | bestFor/pricing/toolName 不得为空、coreFeatures 每条 2–4 个关键词、items ≥ 2 条、无空 intro、列结构统一 | 不因「样式化」放宽 |
| **B 强建议** | H2 标题含「对比」/ `Comparison`、intro 段落存在、列标题含语义、5 列扩展语义明确 | 跨页格式一致 |
| **C 软建议** | 每表 4–8 条 items、ZH/EN 页面对齐、同类型工具扩展列语义统一 | 以信息密度与可读性为先 |

**一致性重新定义**：跨页优先对齐 **列数、列标题语义、H2 格式、intro 段落存在性**；条目数量与 coreFeatures 个数值允许在建议区间内随工具品类复杂度浮动。

---

## 二、定位与作用

**对比表格**是展示多款工具/产品核心差异的章节，核心作用是：

- **快速对比**：一屏内对比工具名称、核心特点、应用场景、定价
- **移动端友好**：外层 `overflow-x-auto`，小屏横向滚动查看全表
- **SEO 与可访问性**：表格含 caption、scope 等属性

---

## 三、Table 组件三种数据传入模式

`Table` 组件本身支持三种 Props 模式（通过 `renderTable()` 在 ArticleFromJson 中自动调用）：

**用法 A：items 格式**（兼容原 ComparisonTable）
- `items`：`{ toolName, coreFeatures, bestFor, pricing?, integrations? }[]`
- `toolType`、`toolTypeEn`：工具类型名称（用于 caption）
- `columnHeaders`：可选，自定义列标题

**用法 B：columns + data**（通用数据驱动）
- `columns`：`{ key, header, align?, className?, render? }[]`
- `data`：`Record<string, any>[]`
- `caption`：表格描述（SEO）

**用法 C：children**（自定义内容）
- 包裹原生 `<table>`，适用于完全自定义结构

**导入**：`import Table from "@/components/Table";`

---

## 四、表格列结构（统一规范）

**同类型 Tools 页面必须保持列数、列标题、内容格式一致**。

### 3.1 标准 4 列（必选）

| 列 key | 中文标题 | 英文标题 | 内容规范 |
|--------|----------|----------|----------|
| toolName | 工具名称 | Tool Name | 产品名称，用 `<strong>` 标注 |
| coreFeatures | 核心特点 | Core Features | 2–4 个关键词，中文顿号（、）分隔 |
| bestFor | 主要应用场景 | Best For | 2–4 个场景，**必填**，不空 |
| pricing | 定价模式 | Pricing | 订阅制/按量付费/免费/待定，**必填**，无则填「待定」 |

### 3.2 可选第 5 列（扩展列）

仅当工具类型有明确、统一的附加维度时使用，且须在 `columnHeaders` 中明确命名：

| 列 key | 中文标题示例 | 适用场景 |
|--------|--------------|----------|
| integrations | 处理方式 | 变声器（实时/非实时） |
| integrations | 单张成本 \| 处理速度 | 虚拟家居陈设等按张计费工具 |
| integrations | 生成速度 | 头像生成等强调处理时间的工具 |

**要求**：同类型页面使用相同扩展列语义；若无法统一，则采用标准 4 列。

### 3.3 内容规范

| 字段 | 规范 | 层级 |
|------|------|------|
| toolName | 产品名称，**不得为空** | **A** |
| coreFeatures | 2–4 个关键词，中文顿号（、）分隔，英文逗号分隔；**不得为空** | **A** |
| bestFor | 2–4 个应用场景，**不得为空**；无明确场景时填「多种场景」 | **A** |
| pricing | **不得为空**；无数据时填「待定」或「免费」；可简写如「订阅制」「按量付费」 | **A** |
| items | 每表 **≥ 2 条** | **A** |

### 3.4 文案规范

| 项目 | 中文 | 英文 | 层级 |
|------|------|------|------|
| H2 标题 | [工具类型]工具对比（须含「对比」） | [Tool Type] Tools Comparison（须含 `Comparison`） | **B** |
| H2 可选后缀 | 选择最适合你的 | Choose the Best for You | C |
| intro 段落 | 以下是主流[工具类型]工具的对比，帮助您快速了解各工具的特点、应用场景和适用性： | Below is a comparison of top [tool type] tools to help you quickly understand each tool's features, use cases, and suitability: | **B** |
| intro 必须存在 | 不得为空 | 同左 | **B** |

### 3.5 条目数量（建议）

| 项目 | 建议 | 层级 |
|------|------|------|
| 每表 items | 4–8 条 | C |
| 同页 bestFor 个数 | 各条目宜 2–4 个场景，不宜出现 1 个 vs 6 个悬殊 | C |

---

## 五、样式要求

- **容器**：`min-w-full border-collapse border border-border`
- **表头**：`bg-muted`
- **单元格**：`border border-border p-4 text-left font-semibold`
- **响应式**：组件自动处理移动端折叠

---

## 六、Table 实现示例

```tsx
<Table
  toolType="AI图片工具"
  toolTypeEn="AI Image Tools"
  items={[
    {
      toolName: "AI图片生成",
      coreFeatures: "根据文本描述或参考图像自动生成新图像",
      bestFor: "概念设计、艺术创作、营销素材",
      pricing: "订阅制/按量付费",
      integrations: "Midjourney, Flux, Stable Diffusion"
    },
    // ...
  ]}
  columnHeaders={{
    toolName: "功能类型",
    integrations: "代表工具"
  }}
/>
```

---

## 七、Table + children 实现示例（自定义内容）

```tsx
<Table caption="自定义表格">
  <table className="min-w-full border-collapse border border-border">
    <thead>
      <tr className="bg-muted">
        <th className="border border-border p-4 text-left font-semibold">工具名称</th>
        <th className="border border-border p-4 text-left font-semibold">核心特点</th>
        <th className="border border-border p-4 text-left font-semibold">主要应用场景</th>
        <th className="border border-border p-4 text-left font-semibold">定价模式</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td className="border border-border p-4"><strong>工具A</strong></td>
        <td className="border border-border p-4">...</td>
        <td className="border border-border p-4">...</td>
        <td className="border border-border p-4">...</td>
      </tr>
    </tbody>
  </table>
</Table>
```

---

## 八、适用范围

- **Tools**：工具对比表格 → Table
- **SEO**：HTML 标签参考、数据表 → Table
- **SEO/Marketing**：纯文字或列表为主时，一般不使用表格

---

## 九、检查清单（创建/优化时）

- [ ] **A 层**：所有 items 的 toolName、bestFor、pricing 非空；coreFeatures 每条 2–4 个关键词（中文顿号、英文逗号分隔）；每表 ≥ 2 条 items
- [ ] **A 层**：introHtml 非空
- [ ] **A 层**：所有 items 字段名统一（仅 toolName/coreFeatures/bestFor/pricing，可选 integrations）
- [ ] **B 层**：H2 标题含「对比」/ `Comparison`
- [ ] **B 层**：列标题语义与数据一致（扩展列须在 columnHeaders 中命名）
- [ ] **C 层**：每表 items 在 4–8 条建议区间或能说明理由
- [ ] **C 层**：ZH/EN 两版页面均有 comparisonSection
- [ ] **C 层**：同类型工具页面的扩展列语义一致
- [ ] 表头列数与数据列数一致
- [ ] pricing 格式统一（无「免费试用」与「Freemium」混用等情况）

## 十、常见错误

- ❌ 未导入 Table
- ❌ 表格内容与产品详情重复
- ❌ 列标题与内容不一致
- ❌ bestFor 或 pricing 为空（应填「待定」或「多种场景」）
- ❌ coreFeatures 为 0-1 个关键词或为空
- ❌ 同类型页面列数、列标题不一致
- ❌ intro 段落缺失
- ✅ 使用 Table，列结构统一，内容格式一致
