const fs = require("fs");
const path = require("path");
const dir = "E:/客户部署项目/luciusai-blog/content/blog/zh";
const bad = [];
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".md"))) {
  const t = fs.readFileSync(path.join(dir, f), "utf8");
  const m = t.match(/^description:\s*"(.*)"/m);
  if (!m) continue;
  const d = m[1];
  if (d.length < 80) bad.push([d.length, f]);
}
bad.sort((a,b)=>a[0]-b[0]);
console.log('under 80:', bad.length);
bad.forEach(([n,f]) => console.log(n, f));
