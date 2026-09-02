import json, re, os
base = r"E:\自有部署项目\alignify production"

for fname in ["tldr-data.json", "faq-data.json", "references-data.json"]:
    p = os.path.join(base, "src", "data", fname)
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    for key, val in d.items():
        if "submit-website" in key:
            print("===", fname, key, "===")
            print(json.dumps(val, ensure_ascii=False, indent=2))

meta_path = os.path.join(base, "src", "data", "seo-meta.ts")
with open(meta_path, encoding="utf-8") as f:
    t = f.read()
idx = t.find("submit-website")
print("=== seo-meta.ts ===")
print(t[idx:idx+1800] if idx >= 0 else "not found")
