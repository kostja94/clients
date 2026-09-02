import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("audit", r"e:\clients\temp\audit_kb_dedupe.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

ROOT = Path(r"e:\clients\Alignify\knowledge\tools")
folders = ["web-data", "design", "text-content"]
print("file|lines|severity|score")
for folder in folders:
    for fp in sorted((ROOT / folder).glob("*.md")):
        r = audit.audit_file(fp)
        print(f"{r['path']}|{r['lines']}|{r['severity']}|{r['score']}")
        for i in r["issues"]:
            print(f"  [{i['severity']}] {i['type']}: {i['detail']}")
