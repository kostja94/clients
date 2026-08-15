# 项目配置文件说明

本文件夹用于存放项目配置文件的说明文档。实际的配置文件保留在项目根目录，因为各种工具和框架会从根目录自动查找这些文件。

## 配置文件位置说明

### 必须保留在根目录的配置文件

以下配置文件**必须保留在项目根目录**，因为相关工具和框架会从根目录自动查找：

- **用途**: MDX组件映射配置文件
- **框架**: Next.js MDX

#### 2. `components.json`
- **用途**: shadcn/ui组件库配置文件
- **工具**: shadcn/ui CLI
- **说明**: shadcn/ui CLI工具会从根目录查找此文件，用于配置组件路径、样式等
- **位置**: 根目录（`/components.json`）

#### 3. `next.config.js`
- **用途**: Next.js框架配置文件
- **框架**: Next.js
- **说明**: Next.js会自动从根目录查找此文件，用于配置构建、路由、图片等
- **位置**: 根目录（`/next.config.js`）

#### 4. `tailwind.config.ts`
- **用途**: Tailwind CSS配置文件
- **工具**: Tailwind CSS
- **说明**: Tailwind CSS会从根目录查找此文件，用于配置主题、颜色、字体等
- **位置**: 根目录（`/tailwind.config.ts`）

#### 5. `postcss.config.js`
- **用途**: PostCSS配置文件
- **工具**: PostCSS
- **说明**: PostCSS会从根目录查找此文件，用于配置CSS处理插件
- **位置**: 根目录（`/postcss.config.js`）

#### 6. `tsconfig.json`
- **用途**: TypeScript配置文件
- **工具**: TypeScript编译器
- **说明**: TypeScript编译器会从根目录查找此文件，用于配置编译选项、路径别名等
- **位置**: 根目录（`/tsconfig.json`）

#### 7. `.eslintrc.json`
- **用途**: ESLint配置文件
- **工具**: ESLint
- **说明**: ESLint会从根目录查找此文件，用于配置代码检查规则
- **位置**: 根目录（`/.eslintrc.json`）

#### 8. `package.json` / `package-lock.json`
- **用途**: npm包依赖管理文件
- **工具**: npm/yarn/pnpm
- **说明**: 包管理器会从根目录查找这些文件，用于管理项目依赖
- **位置**: 根目录（`/package.json`, `/package-lock.json`）

## 配置文件说明

- HTML元素样式（h1, h2, h3, p, ul, ol, table等）
- 自定义组件映射（BlogLayout, FAQ, Table 等）
- 链接处理（内部链接、外部链接、YouTube链接）
- 表格已统一使用 Table 组件，原生 table 样式仅作为后备

### shadcn/ui配置 (`components.json`)

配置shadcn/ui组件库的设置，包括：
- 样式风格（default）
- 路径别名（components, utils, ui, lib, hooks）
- Tailwind CSS配置路径

### Next.js配置 (`next.config.js`)

配置Next.js框架的各种设置，包括：
- 图片远程模式配置
- 301重定向规则
- 国际化插件配置

### Tailwind CSS配置 (`tailwind.config.ts`)

配置Tailwind CSS样式系统，包括：
- 内容扫描路径
- 主题扩展（颜色、字体、间距等）
- 暗色模式配置
- 响应式断点

## 配置文件修改注意事项

1. **修改前备份**: 修改配置文件前，建议先备份或提交到Git
2. **测试验证**: 修改配置后，务必测试相关功能是否正常
3. **文档更新**: 如果修改了配置规则，记得更新相关规则文件
4. **团队同步**: 配置文件修改后，需要通知团队成员并更新文档

## 相关文档

- **内容规则**: [.cursor/rules/content-rules.mdc](../../.cursor/rules/content-rules.mdc)
- **技术规范**: [technical](./README.md)
- **章节格式**: [content/sections](../content/sections/REA