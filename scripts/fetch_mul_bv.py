"""
Fetch Battle Value from Master Unit List for all MTF files.
Creates a CSV with: chassis, variant, mul_id, mul_bv, calc_bv, tonnage, tech, file_path

Usage: python scripts/fetch_mul_bv.py
Output: data/mul_bv_reference.csv
"""
import sys, os, glob, csv, re, time, json
sys.path.insert(0, ".")

import requests
from src.models.data_store import DataStore
from src.parsers.mtf_parser import parse_mtf
from src.engine.bv_calculator import calculate_bv

DataStore.load()

MTF_DIR = r"D:\Dropbox\Battletech\MUL_Files\meks"
OUTPUT = "data/mul_bv_reference.csv"
CACHE_FILE = "data/mul_bv_cache.json"

# Load cache of previously fetched BV values
cache = {}
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE) as f:
        cache = json.load(f)
    print(f"Loaded {len(cache)} cached BV values")

def fetch_mul_bv(mul_id):
    """Fetch BV from MUL website. Returns int or None."""
    if mul_id in cache:
        return cache[mul_id]

    url = f"https://masterunitlist.azurewebsites.net/Unit/Details/{mul_id}"
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return None
        # BV appears in: <a href="/Tools/Skill?BaseBV=1477">
        m = re.search(r'BaseBV=(\d+)', resp.text)
        if m:
            bv = int(m.group(1))
            cache[mul_id] = bv
            return bv
        return None
    except Exception as e:
        return None

# Process all MTF files
mtf_files = sorted(glob.glob(os.path.join(MTF_DIR, "**", "*.mtf"), recursive=True))
print(f"Processing {len(mtf_files)} MTF files...")

rows = []
fetched = 0
cached = 0
failed = 0
t0 = time.time()

for i, fpath in enumerate(mtf_files):
    if i % 250 == 0:
        # Save cache periodically
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
        elapsed = time.time() - t0
        rate = i / elapsed if elapsed > 0 else 0
        eta = (len(mtf_files) - i) / rate if rate > 0 else 0
        print(f"  {i}/{len(mtf_files)} ({i/len(mtf_files)*100:.0f}%) "
              f"fetched={fetched} cached={cached} failed={failed} "
              f"ETA={eta/60:.0f}m")

    # Extract mul_id
    mul_id = None
    try:
        with open(fpath, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if line.startswith("mul id:"):
                    mul_id = line.split(":")[1].strip()
                    break
    except:
        pass

    # Parse and calculate BV
    try:
        r = parse_mtf(fpath)
        u = r.unit
        calc_bv = calculate_bv(u)
        tonnage = u.tonnage
        tech = u.tech
        chassis = u.chassis
        variant = u.variant
    except Exception as e:
        print(f"  ERROR parsing {fpath}: {e}")
        continue

    # Fetch MUL BV
    mul_bv = None
    if mul_id:
        if mul_id in cache:
            mul_bv = cache[mul_id]
            cached += 1
        else:
            mul_bv = fetch_mul_bv(mul_id)
            if mul_bv is not None:
                fetched += 1
            else:
                failed += 1

    rows.append({
        "chassis": chassis,
        "variant": variant,
        "mul_id": mul_id or "",
        "mul_bv": mul_bv or "",
        "calc_bv": calc_bv,
        "tonnage": tonnage,
        "tech": tech,
        "file": os.path.relpath(fpath, MTF_DIR),
    })

# Save final cache
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

# Write CSV
with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["chassis", "variant", "mul_id", "mul_bv", "calc_bv", "tonnage", "tech", "file"])
    writer.writeheader()
    writer.writerows(rows)

elapsed = time.time() - t0
print(f"\nDone in {elapsed/60:.1f}m. {len(rows)} rows written to {OUTPUT}")
print(f"Fetched: {fetched}, Cached: {cached}, Failed: {failed}, No mul_id: {sum(1 for r in rows if not r['mul_id'])}")

# Stats
with_bv = [r for r in rows if r["mul_bv"]]
if with_bv:
    diffs = [r["calc_bv"] - int(r["mul_bv"]) for r in with_bv]
    pcts = [abs(d)/int(r["mul_bv"])*100 for r, d in zip(with_bv, diffs) if int(r["mul_bv"]) > 0]
    exact = sum(1 for d in diffs if d == 0)
    within1 = sum(1 for p in pcts if p <= 1.0)
    within5 = sum(1 for p in pcts if p <= 5.0)
    print(f"\nAccuracy (vs MUL, {len(with_bv)} units):")
    print(f"  Exact matches: {exact} ({exact/len(with_bv)*100:.1f}%)")
    print(f"  Within 1%:     {within1} ({within1/len(with_bv)*100:.1f}%)")
    print(f"  Within 5%:     {within5} ({within5/len(with_bv)*100:.1f}%)")
    print(f"  Mean abs err:  {sum(pcts)/len(pcts):.1f}%")
