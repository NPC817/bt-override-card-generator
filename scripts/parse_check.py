"""Parse all MTF/BLK files from MUL directories and report errors/warnings."""
import csv
import os
import sys
import traceback
from collections import Counter, defaultdict
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.parsers.mtf_parser import parse_mtf
from src.parsers.blk_parser import parse_blk

SOURCES = [
    ("battlearmor", r"D:\Dropbox\Battletech\MUL_Files\battlearmor"),
    ("convfighter",  r"D:\Dropbox\Battletech\MUL_Files\convfighter"),
    ("fighters",     r"D:\Dropbox\Battletech\MUL_Files\fighters"),
    ("meks",         r"D:\Dropbox\Battletech\MUL_Files\meks"),
    ("vehicles",     r"D:\Dropbox\Battletech\MUL_Files\vehicles"),
]

OUTPUT_CSV = PROJECT_ROOT / "parse_check_results.csv"


def _unit_type_name(unit) -> str:
    return type(unit).__name__ if unit is not None else "Unknown"


def parse_file(path: str):
    ext = Path(path).suffix.lower()
    if ext == ".mtf":
        return parse_mtf(path)
    elif ext == ".blk":
        return parse_blk(path)
    return None


def run():
    rows = []
    status_counts = Counter()
    folder_counts = defaultdict(Counter)
    warning_patterns = Counter()
    crashes = []

    total = 0
    for folder_name, folder_path in SOURCES:
        folder = Path(folder_path)
        if not folder.exists():
            print(f"  [SKIP] Folder not found: {folder_path}")
            continue

        files = sorted(folder.rglob("*.mtf")) + sorted(folder.rglob("*.blk"))
        print(f"\n{folder_name}: {len(files)} files", flush=True)

        for i, fpath in enumerate(files):
            total += 1
            if i % 500 == 0 and i > 0:
                print(f"  ... {i}/{len(files)}", flush=True)

            unit_type = ""
            warnings_str = ""
            exception_str = ""
            status = "ok"

            try:
                result = parse_file(str(fpath))
                if result is None:
                    status = "crash"
                    exception_str = "Unknown extension"
                else:
                    unit_type = _unit_type_name(result.unit)
                    if result.warnings:
                        status = "warn"
                        warnings_str = " | ".join(result.warnings)
                        for w in result.warnings:
                            # Normalize warning to pattern (strip variable parts)
                            pattern = w.split(":")[0].strip() if ":" in w else w
                            warning_patterns[pattern] += 1
            except Exception as e:
                status = "crash"
                exception_str = f"{type(e).__name__}: {e}"
                tb = traceback.format_exc().splitlines()
                # Keep last 3 lines of traceback for brevity
                exception_str += " || " + " | ".join(tb[-3:])
                crashes.append((folder_name, fpath.name, exception_str))

            status_counts[status] += 1
            folder_counts[folder_name][status] += 1
            rows.append({
                "folder": folder_name,
                "filename": fpath.name,
                "status": status,
                "unit_type": unit_type,
                "warnings": warnings_str,
                "exception": exception_str,
            })

    # Write CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["folder", "filename", "status", "unit_type", "warnings", "exception"])
        writer.writeheader()
        writer.writerows(rows)

    # Print summary
    print("\n" + "="*60)
    print(f"TOTAL FILES: {total}")
    print(f"  ok:    {status_counts['ok']}")
    print(f"  warn:  {status_counts['warn']}")
    print(f"  crash: {status_counts['crash']}")

    print("\nPER-FOLDER:")
    for folder_name, _ in SOURCES:
        c = folder_counts[folder_name]
        print(f"  {folder_name:15s}  ok={c['ok']}  warn={c['warn']}  crash={c['crash']}")

    print("\nTOP WARNING PATTERNS (by count):")
    for pattern, count in warning_patterns.most_common(20):
        print(f"  {count:5d}  {pattern}")

    if crashes:
        print(f"\nCRASHED FILES ({len(crashes)}):")
        for folder, fname, exc in crashes[:50]:
            print(f"  [{folder}] {fname}")
            print(f"    {exc[:200]}")
        if len(crashes) > 50:
            print(f"  ... and {len(crashes)-50} more (see CSV)")

    print(f"\nFull results: {OUTPUT_CSV}")


if __name__ == "__main__":
    run()
