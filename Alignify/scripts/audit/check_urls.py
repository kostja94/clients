import urllib.request
import urllib.error
import ssl
import concurrent.futures

products = [
    ("Tripo", "https://www.tripo3d.ai"),
    ("Meshy", "https://www.meshy.ai"),
    ("Rodin", "https://rodin.ai"),
    ("Genie by Luma", "https://lumalabs.ai/genie"),
    ("Spline", "https://spline.design"),
    ("3DFY", "https://3dfy.ai"),
    ("Alpha3D", "https://www.alpha3d.io"),
    ("Autodesk 3ds Max", "https://www.autodesk.com/products/3ds-max/overview"),
    ("Rhinoceros", "https://www.rhino3d.com/"),
    ("Shapr3D", "https://www.shapr3d.com/"),
    ("KIRI Engine", "https://www.kiriengine.com/"),
    ("Polycam", "https://polycam.ai/"),
    ("RoomScan Pro", "https://www.roomscan.com/"),
    ("LARKI", "https://www.larki.com/"),
    ("HeyGen", "https://www.heygen.com/"),
    ("Synthesia", "https://www.synthesia.io/"),
    ("D-ID", "https://www.d-id.com/"),
    ("Colossyan", "https://www.colossyan.com/"),
    ("LogoAI", "https://www.logoai.com/"),
    ("Looka", "https://looka.com/"),
    ("Logomaster.ai", "https://www.logomaster.ai/"),
    ("Brandmark", "https://brandmark.io/"),
    ("LOGO.com", "https://www.logo.com/"),
    ("Turbologo", "https://www.turbologo.com/"),
    ("Logopony", "https://www.logopony.com/"),
    ("Molypix", "https://molypix.ai/"),
    ("Piktochart", "https://piktochart.com/"),
    ("Venngage", "https://www.venngage.com/"),
    ("Visme", "https://www.visme.co/"),
    ("Designs.ai", "https://designs.ai/"),
    ("Design.com", "https://www.design.com/"),
    ("Gradium", "https://gradium.ai/"),
    ("GoEnhance", "https://www.goenhance.ai/"),
    ("Domo AI", "https://domoai.app"),
    ("Pollo AI", "https://pollo.ai"),
    ("Rask AI", "https://www.rask.ai"),
    ("FalcoCut", "https://falcocut.ai/"),
    ("Blipcut", "https://blipcut.ai"),
    ("Vozo AI", "https://vozo.ai"),
    ("Captions AI", "https://captions.ai"),
    ("Akool", "https://akool.com"),
    ("Relume", "https://relume.io/"),
    ("Durable", "https://durable.co/"),
    ("Renderforest", "https://www.renderforest.com/"),
    ("Code Design.ai", "https://codedesign.ai/"),
    ("10Web", "https://10web.io/"),
    ("Wegic", "https://wegic.ai/"),
    ("Squarespace", "https://www.squarespace.com/"),
    ("Hostinger", "https://www.hostinger.com/"),
    ("WordPress", "https://wordpress.com/"),
    ("Wix", "https://www.wix.com/"),
    ("1X Technologies", "https://1x.tech"),
]

def check_url(name, url):
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        final_url = resp.geturl()
        domain = url.split("/")[2]
        final_domain = final_url.split("/")[2]
        status = resp.getcode()

        body = resp.read(10000).decode('utf-8', errors='ignore').lower()

        parking_signals = ["domain is parked", "buy this domain", "domain for sale",
                          "this domain has expired", "is for sale", "parked free",
                          "domain name is available", "this site is suspended",
                          "account suspended", "this website is under construction",
                          "this page is reserved", "future home of",
                          "this domain name is for sale"]

        is_parked = any(signal in body for signal in parking_signals)

        if is_parked:
            return (name, url, f"PARKED/DEAD (HTTP {status})", final_url)
        elif final_domain != domain and final_domain not in domain and not domain.endswith(final_domain):
            return (name, url, f"REDIRECT {domain}->{final_domain} (HTTP {status})", final_url)
        elif 400 <= status < 500:
            return (name, url, f"HTTP {status}", final_url)
        else:
            return (name, url, f"OK (HTTP {status})", final_url)
    except urllib.error.HTTPError as e:
        return (name, url, f"HTTP {e.code}", str(e))
    except urllib.error.URLError as e:
        reason = str(e.reason)
        if "getaddrinfo" in reason.lower():
            return (name, url, "DNS FAIL (domain not found)", "")
        if "timed out" in reason.lower():
            return (name, url, "TIMEOUT", "")
        if "certificate" in reason.lower():
            return (name, url, "SSL ERROR", "")
        return (name, url, f"FAIL: {reason}", "")
    except Exception as e:
        return (name, url, f"ERROR: {e}", "")

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    futures = {ex.submit(check_url, name, url): name for name, url in products}
    for f in concurrent.futures.as_completed(futures):
        results.append(f.result())

results.sort(key=lambda r: (0 if r[2].startswith("OK") else 1, r[0]))

for name, url, status, final_url in results:
    marker = "OK" if status.startswith("OK") else "DEAD" if "HTTP 4" in status or "FAIL" in status or "DNS" in status or "PARKED" in status else "WARN"
    print(f"[{marker}] {name}")
    print(f"  {url} -> {status}")
    if final_url and final_url != url:
        print(f"  Final: {final_url}")

ok = sum(1 for r in results if r[2].startswith("OK"))
not_ok = len(results) - ok
print(f"\n=== {ok}/{len(results)} online, {not_ok} issues ===")
