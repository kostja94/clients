# MeDo 面包屑组件优化方案

> **本文档职责**：面包屑组件统一化设计与实施计划  
> **创建日期**：2026-07-02  
> **引用**：[medo.md](../medo.md) | [medo-site-structure.md](../medo-site-structure.md) | [medo-schema-spec.md](./medo-schema-spec.md)

---

## 一、现状诊断

### 1.1 检测结果

| 页面 | JSON-LD BreadcrumbList | 可见面包屑 UI | 状态 |
|------|----------------------|-------------|------|
| `/` (首页) | N/A | 无 | 首页无需面包屑 ✓ |
| `/showcase` | ❌ 缺失 | ❌ 缺失 | 🔴 完全缺失 |
| `/showcase/mobile` | ✅ 存在 | ❌ 缺失 | 🟡 仅结构化数据，无可见 UI |
| `/features` | ❌ 缺失 | ❌ 缺失 | 🔴 完全缺失 |
| `/pricing` | ❌ 缺失 | ❌ 缺失 | 🔴 完全缺失 |
| `/templates` | ❌ 缺失 | ❌ 缺失 | 🔴 完全缺失 |

### 1.2 现有 BreadcrumbList 分析（`/showcase/mobile`）

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://miaoda.io/showcase/mobile#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://miaoda.io" },
    { "@type": "ListItem", "position": 2, "name": "MeDo AI Mobile App Builder", "item": "https://miaoda.io/showcase/mobile" }
  ]
}
```

**现有问题**：
- 缺少 `Showcase` 中间层级（应为 Home → Showcase → Mobile）
- 仅在 JSON-LD 中存在，无对应的可见导航组件
- 最后一层未标记为当前页（缺少 `"position": 2` 层级的标识）

### 1.3 核心问题总结

1. **覆盖不完整**：5 个子页面中仅 1 个有面包屑数据
2. **层级缺失**：深层页面缺少中间层级
3. **UI 与数据脱节**：结构化数据与用户可见组件不一致
4. **无统一设计**：没有全局面包屑组件和样式系统

---

## 二、目标网站结构 (IA)

基于 [medo-site-structure.md](../medo-site-structure.md) 的导航体系，需要覆盖的页面层级关系：

```
Home (/) 
├── Features (/features)
├── Pricing (/pricing)
├── Templates (/templates)
│   └── Templates/{category} (/templates/{category})
├── Showcase (/showcase)
│   ├── Showcase/Mobile (/showcase/mobile)
│   ├── Showcase/Ecommerce (/showcase/ecommerce) [待验证]
│   └── Showcase/... (/showcase/{category})
├── Solutions (/solutions)
│   ├── Solutions/{type} (/solutions/{type})
│   └── ...
├── Comparisons (/comparisons)
│   ├── vs/Lovable (/vs/lovable)
│   ├── vs/Bolt (/vs/bolt)
│   └── ...
└── Blog (/blog)
    └── Blog/{slug} (/blog/{slug})
```

---

## 三、面包屑统一设计规范

### 3.1 组件结构

采用标准的面包屑导航模式，与 MeDo 现有设计语言（Next.js + Tailwind）保持一致：

```tsx
// components/ui/Breadcrumb.tsx
interface BreadcrumbItem {
  label: string;
  href?: string; // undefined = 当前页
}

interface BreadcrumbProps {
  items: BreadcrumbItem[];
  className?: string;
}
```

### 3.2 视觉规范

| 属性 | 值 |
|------|-----|
| 位置 | Hero 区域上方，header 下方 |
| 字体 | `text-sm` (14px) `text-brand-text-secondary` |
| 分隔符 | `/` 或 ChevronRight 图标 |
| 当前页 | `text-brand-text` + `font-medium`，不可点击 |
| 链接态 | `text-brand-text-secondary hover:text-brand-text` transition |
| Hover | `hover:text-brand-text` (颜色过渡) |
| 间距 | `gap-2` between items |
| 容器 | `max-w-[1180px] mx-auto px-5 sm:px-6 pt-24 pb-2`（与 header 对齐） |
| 背景 | 透明 / 继承 |

### 3.3 组件实现（React/Next.js）

```tsx
import Link from "next/link";
import { ChevronRight } from "lucide-react";

interface BreadcrumbItem {
  label: string;
  href?: string;
}

function Breadcrumb({ items, className = "" }: { items: BreadcrumbItem[]; className?: string }) {
  return (
    <nav aria-label="Breadcrumb" className={className}>
      <ol className="flex items-center gap-2 text-sm">
        {items.map((item, index) => {
          const isLast = index === items.length - 1;
          return (
            <li key={index} className="flex items-center gap-2">
              {index > 0 && (
                <ChevronRight className="h-4 w-4 text-brand-text-muted shrink-0" aria-hidden="true" />
              )}
              {isLast || !item.href ? (
                <span
                  className="text-brand-text font-medium"
                  aria-current="page"
                >
                  {item.label}
                </span>
              ) : (
                <Link
                  href={item.href}
                  className="text-brand-text-secondary hover:text-brand-text transition-colors"
                >
                  {item.label}
                </Link>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
```

### 3.4 JSON-LD 结构化数据生成

```tsx
function BreadcrumbSchema({ items }: { items: BreadcrumbItem[] }) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, index) => ({
      "@type": "ListItem",
      "position": index + 1,
      "name": item.label,
      "item": item.href ? `https://miaoda.io${item.href}` : undefined,
    })),
  };

  // 移除最后一层的 item URL（标记为当前页）
  const lastItem = schema.itemListElement[schema.itemListElement.length - 1];
  if (lastItem) delete lastItem.item;

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}
```

> **注意**：JSON-LD 最后一层不包含 `item` URL 以标记为当前页面

---

## 四、各页面面包屑配置

### 4.1 首页 `/`
无需面包屑。

### 4.2 Features 页 `/features`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Features` | Home → Features |

### 4.3 Pricing 页 `/pricing`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Pricing` | Home → Pricing |

### 4.4 Templates 页 `/templates`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Templates` | Home → Templates |

### 4.5 Templates 分类页 `/templates/{category}`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Templates / {Category}` | Home → Templates → {Category} |

### 4.6 Showcase 页 `/showcase`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Showcase` | Home → Showcase |

### 4.7 Showcase 子页 `/showcase/mobile`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Showcase / Mobile Apps` | Home → Showcase → Mobile Apps |

> **修复点**：当前仅有 `Home → MeDo AI Mobile App Builder`，需补全中间层级

### 4.8 Comparisons 页 `/comparisons`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Comparisons` | Home → Comparisons |

### 4.9 VS 对比页 `/vs/{competitor}`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Comparisons / MeDo vs {Competitor}` | Home → Comparisons → MeDo vs {Competitor} |

### 4.10 Blog 页 `/blog`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Blog` | Home → Blog |

### 4.11 Blog 文章页 `/blog/{slug}`

| 可见 UI | JSON-LD |
|---------|---------|
| `Home / Blog / {Article Title}` | Home → Blog → {Article Title} |

---

## 五、实施计划

### Phase 1 — 创建全局面包屑组件

| 任务 | 说明 |
|------|------|
| 1.1 创建 `Breadcrumb` UI 组件 | 按 3.3 节实现，放入 `components/ui/Breadcrumb.tsx` |
| 1.2 创建 `BreadcrumbSchema` 组件 | 按 3.4 节实现，自动生成 JSON-LD |
| 1.3 添加布局插槽 | 在 `layout.tsx` 中为面包屑预留渲染区域 |

### Phase 2 — 覆盖现有高优先级页面

| 页面 | JSON-LD | 可见 UI |
|------|---------|---------|
| `/features` | ✅ 新增 | ✅ 新增 |
| `/pricing` | ✅ 新增 | ✅ 新增 |
| `/showcase` | ✅ 新增 | ✅ 新增 |
| `/templates` | ✅ 新增 | ✅ 新增 |
| `/showcase/mobile` | ✅ 修复（补全层级） | ✅ 新增 |

### Phase 3 — 覆盖深层页面

| 页面 | 说明 |
|------|------|
| `/vs/{competitor}` | 对比页需三层面包屑 |
| `/templates/{category}` | 分类模板页 |
| `/showcase/{category}` | 案例分类页 |
| `/blog/{slug}` | 文章详情页 |

### Phase 4 — 验证与监控

| 任务 | 说明 |
|------|------|
| 4.1 Google Search Console 验证 | 提交 sitemap，检查面包屑是否正确抓取 |
| 4.2 Schema Markup Validator | 验证 JSON-LD 结构化数据格式 |
| 4.3 Lighthouse / PageSpeed | 确保面包屑不影响性能 |
| 4.4 移动端适配 | 长路径的面包屑在移动端可用省略/折叠 |

---

## 六、SEO 收益预估

| 收益项 | 预期效果 |
|--------|---------|
| SERP 展示增强 | 搜索结果中显示面包屑路径，提升点击率（CTR +5%~15%） |
| 网站结构信号 | 帮助搜索引擎理解站点层级，优化爬取效率 |
| 内部链接增强 | 面包屑作为天然内链，增强页面间关联性 |
| 用户体验提升 | 用户更清楚当前位置，降低跳出率 |

---

## 七、已识别的风险与注意事项

1. **多语言路由**：面包屑需适配 `/[locale]/` 路径前缀，标签走 i18n 翻译
2. **动态路由**：`/showcase/{slug}` 类页面的面包屑需渲染动态标题
3. **移动端**：路径层级 > 3 时需考虑折叠显示（如 `Home / ... / Current`）
4. **与现有 Hero 间距**：面包屑位于 Hero 上方时需调整 Hero section 的 `pt` padding

---

*关联优化：[medo-schema-spec.md](./medo-schema-spec.md) — 结构化数据规范；[medo-site-structure.md](../medo-site-structure.md) — 网站 IA 结构*
