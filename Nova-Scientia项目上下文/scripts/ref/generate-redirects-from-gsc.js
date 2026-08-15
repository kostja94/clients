/**
 * 从 GSC organic positions xlsx 生成 301 重定向规则
 * 用法: node scripts/generate-redirects-from-gsc.js <path-to-xlsx>
 *
 * 输出：
 * - 产品页根路径 /slug → /products/slug
 * - 特殊映射：leonardo-ia→leonardo-ai, suno-ia→suno, janitor-ia→janitor-ai, vidu-ia→vidu
 */
const XLSX = require("xlsx");
const fs = require("fs");
const path = require("path");
const { getDeployRoot } = require("../lib/deploy-root");

const inputPath = process.argv[2];
if (!inputPath) {
  console.error("用法: node scripts/generate-redirects-from-gsc.js <path-to-xlsx>");
  process.exit(1);
}

// 根路径 → 目标 slug 的特殊映射（旧 slug 与现有一致则无需映射）
const SLUG_MAP = {
  "leonardo-ia": "leonardo-ai",
  "suno-ia": "suno",
  "janitor-ia": "janitor-ai",
  "vidu-ia": "vidu",
};

// 已在 next.config 中单独配置 301 的葡语长尾 slug，跳过
const SKIP_SLUGS = new Set([
  "ferramentas-ia-design-interiores",
  "melhores-detectores-de-ia",
  "melhores-ferramentas-cli",
  "melhores-geradores-de-tatuagem",
  "melhores-geradores-de-voz-de-ia",
  "melhores-geradores-imagem-ia",
  "melhores-geradores-podcast-ia",
  "melhores-modificadores-de-voz-com-ia",
  "melhores-sites-para-troca-de-rosto-com-ia",
  "melhores-tts-ferramentas-texto-para-fala",
]);

const wb = XLSX.readFile(inputPath);
const sheet = wb.Sheets[wb.SheetNames[0]];
const data = XLSX.utils.sheet_to_json(sheet, { header: 1 });

const header = data[0] || [];
const urlCol = header.findIndex((h) => /url/i.test(String(h)));
const rows = data.slice(1);

const paths = new Set();
for (const row of rows) {
  const url = row[urlCol];
  if (!url || typeof url !== "string") continue;
  const u = new URL(
    url.startsWith("http") ? url : "https://novascientia.com.br" + (url.startsWith("/") ? url : "/" + url)
  );
  const pathname = u.pathname.replace(/\/$/, "") || "/";
  if (pathname === "/" || pathname.startsWith("/products") || pathname.startsWith("/tools"))
    continue;
  paths.add(pathname);
}

// 生成重定向规则（仅产品页；其它路径见 next.config）
const redirects = [];
for (const p of [...paths].sort()) {
  const slug = p.replace(/^\//, "");
  if (SKIP_SLUGS.has(slug)) continue;
  const destSlug = SLUG_MAP[slug] || slug;
  const dest = `/products/${destSlug}`;
  redirects.push({ source: p, destination: dest });
  redirects.push({ source: p + "/", destination: dest });
}

// 输出 next.config 格式
const lines = redirects.map(
  (r) => `      { source: '${r.source}', destination: '${r.destination}', permanent: true },`
);
console.log("// 从 GSC 导出的产品页根路径 301 重定向");
lines.forEach((l) => console.log(l));

// 写入 JSON 供 next.config 引用
const outPath = path.join(getDeployRoot(), "config", "product-root-redirects.json");
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(redirects, null, 2), "utf-8");
console.log("\nWritten to", outPath);
