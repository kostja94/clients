/**
 * 部署后检查脚本 — 验证所有 API 端点和 dashboard 是否正常工作
 *
 * 用法：node scripts/permanent/check-deploy.mjs [baseUrl]
 *   默认 baseUrl = https://alignify.co
 */

const BASE = process.argv[2] || "https://alignify.co";

const checks = [
  {
    name: "GA4 Overview API",
    url: "/api/ga4/overview?days=7&limit=5",
    method: "GET",
    validate: (data) => data.overview && typeof data.overview.totalUsers === "number",
  },
  {
    name: "GSC Search Analytics",
    url: "/api/gsc/search-analytics",
    method: "POST",
    body: {
      startDate: new Date(Date.now() - 7 * 86400000).toISOString().slice(0, 10),
      endDate: new Date(Date.now() - 3 * 86400000).toISOString().slice(0, 10),
      dimensions: ["page"],
      rowLimit: 3,
    },
    validate: (data) => Array.isArray(data.rows),
  },
  {
    name: "GSC Sitemaps",
    url: "/api/gsc/sitemaps",
    method: "GET",
    validate: (data) => Array.isArray(data.sitemaps),
  },
  {
    name: "Dashboard Page",
    url: "/dash",
    method: "GET",
    validate: (html) => html.includes("Alignify SEO") || html.includes("__NEXT"),
  },
];

async function main() {
  console.log("═".repeat(55));
  console.log(`部署检查 — ${BASE}`);
  console.log("═".repeat(55));
  console.log("");

  let passed = 0;
  let failed = 0;

  for (const check of checks) {
    process.stdout.write(`  ${check.name.padEnd(28)} `);
    try {
      const opts = {
        method: check.method,
        headers: { "Content-Type": "application/json" },
      };
      if (check.body) opts.body = JSON.stringify(check.body);

      const res = await fetch(`${BASE}${check.url}`, opts);
      const contentType = res.headers.get("content-type") || "";

      if (!res.ok) {
        const text = await res.text().catch(() => "");
        console.log(`✗ HTTP ${res.status}: ${text.slice(0, 100)}`);
        failed++;
        continue;
      }

      let data;
      if (contentType.includes("application/json")) {
        data = await res.json();
      } else {
        data = await res.text();
      }

      if (check.validate(data)) {
        console.log("✓");
        passed++;
      } else {
        console.log("✗ 数据格式不符");
        console.log(`     ${JSON.stringify(data).slice(0, 200)}`);
        failed++;
      }
    } catch (err) {
      console.log(`✗ ${err.message.slice(0, 60)}`);
      failed++;
    }
  }

  console.log("");
  console.log("═".repeat(55));
  console.log(`结果: ${passed} 通过 · ${failed} 失败 · ${checks.length} 总计`);
  if (failed > 0) {
    console.log("");
    console.log("排查:");
    console.log("  1. Vercel 部署是否成功？");
    console.log("  2. 环境变量 GA_PROPERTY_ID / GSC_CLIENT_EMAIL / GSC_PRIVATE_KEY / GSC_SITE_URL 是否已配置？");
    console.log("  3. Google Analytics Data API 是否在 GCP Console 启用？");
    console.log("  4. 服务账号是否已添加到 GA4 和 GSC？");
  }
  console.log("═".repeat(55));
  process.exit(failed > 0 ? 1 : 0);
}

main();
