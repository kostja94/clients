import json, os
base = r"E:\自有部署项目\alignify production"
for fname in ["tldr-data.json", "faq-data.json", "references-data.json"]:
    p = os.path.join(base, "src", "data", fname)
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    for path in ["/seo/submit-website", "/zh/seo/submit-website"]:
        if path in d.get("pages", {}):
            print("===", fname, path, "===")
            print(json.dumps(d["pages"][path], ensure_ascii=False, indent=2))
            print()
