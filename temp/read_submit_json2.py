import json, os
base = r"E:\自有部署项目\alignify production"
for fname in ["tldr-data.json", "faq-data.json", "references-data.json"]:
    p = os.path.join(base, "src", "data", fname)
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    print(fname, "top keys sample:", list(d.keys())[:5])
    # search nested
    def find(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                np = f"{path}/{k}" if path else k
                if "submit-website" in k or (isinstance(v, str) and "submit" in v.lower() and "website" in v.lower()):
                    print("FOUND", fname, np)
                find(v, np)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                find(item, f"{path}[{i}]")
    find(d)
