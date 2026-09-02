import os
base = r"E:\自有部署项目\alignify production"
for loc in ["content/seo/zh/submit-website.md", "src/data/seo-meta.ts"]:
    p = os.path.join(base, loc.replace("/", os.sep))
    with open(p, encoding="utf-8") as f:
        t = f.read()
    print("===", loc, "lines", t.count(chr(10)), "===")
    print(t[:800])
    if "platform-properties" in t.lower() or "Platform property" in t:
        print("OK: platform section present")
    if loc.endswith("seo-meta.ts"):
        idx = t.find("submit-website")
        print(t[idx:idx+600])
