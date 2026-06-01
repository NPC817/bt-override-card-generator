"""Rebuild data/units.zip from MUL_Files MTF/BLK files.

Headless script — no Qt needed. Uses the same parse → resolve → TIC assign →
serialize pipeline as the BatchProcessor GUI export.
"""
import json
import os
import shutil
import sys
import tempfile
import time
import traceback
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

# ── Path setup ─────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.parsers.mtf_parser import parse_mtf
from src.parsers.blk_parser import parse_blk
from src.models.data_store import DataStore
from src.models.battle_armor import BattleArmor
from src.settings.profile import ConversionProfile
from src.engine.tic_grouper import resolve_weapons, auto_assign_tics

# ── Source directories ─────────────────────────────────────────────────────
SOURCES = [
    ("battlearmor", r"D:\Dropbox\Battletech\MUL_Files\battlearmor"),
    ("convfighter",  r"D:\Dropbox\Battletech\MUL_Files\convfighter"),
    ("fighters",     r"D:\Dropbox\Battletech\MUL_Files\fighters"),
    ("meks",         r"D:\Dropbox\Battletech\MUL_Files\meks"),
    ("vehicles",     r"D:\Dropbox\Battletech\MUL_Files\vehicles"),
]

ZIP_PATH = PROJECT_ROOT / "data" / "units.zip"


def _parse_file(path: str):
    """Dispatch to the correct parser by file extension."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".mtf":
        return parse_mtf(path)
    elif ext == ".blk":
        return parse_blk(path)
    return None


def run() -> None:
    t0 = time.time()

    # ── Init ─────────────────────────────────────────────────────────────
    print("Loading weapon & equipment databases...", flush=True)
    DataStore.load()
    profile = ConversionProfile.default()
    print("Profile: Default\n", flush=True)

    status_counts: Counter[str] = Counter()
    folder_counts: dict[str, Counter[str]] = defaultdict(Counter)
    warning_patterns: Counter[str] = Counter()
    crashes: list[tuple[str, str, str]] = []
    total = 0
    written = 0
    dupes = 0

    tmp_dir = tempfile.mkdtemp(prefix="ovr_build_")
    try:
        # ── Process each source directory ────────────────────────────────
        for folder_name, folder_path in SOURCES:
            folder = Path(folder_path)
            if not folder.exists():
                print(f"  [SKIP] Folder not found: {folder_path}")
                continue

            files = sorted(folder.rglob("*.mtf")) + sorted(folder.rglob("*.blk"))
            print(f"\n{folder_name}: {len(files)} files", flush=True)

            for i, fpath in enumerate(files):
                total += 1
                if i > 0 and i % 500 == 0:
                    print(f"  ... {i}/{len(files)}", flush=True)

                status = "ok"
                warnings_list: list[str] = []

                try:
                    result = _parse_file(str(fpath))
                    if result is None:
                        status = "crash"
                        crashes.append((folder_name, fpath.name, "Unknown extension"))
                        status_counts[status] += 1
                        folder_counts[folder_name][status] += 1
                        continue

                    unit = result.unit
                    warnings_list = list(result.warnings)
                    for w in warnings_list:
                        pattern = w.split(":")[0].strip() if ":" in w else w
                        warning_patterns[pattern] += 1

                    # Resolve weapons and auto-assign TICs
                    tonnage = getattr(unit, "tonnage", 0)
                    resolved = resolve_weapons(unit, tonnage, profile=profile)
                    auto_assign_tics(resolved, is_ba=isinstance(unit, BattleArmor))

                    # Write .ovr to temp directory
                    stem = fpath.stem
                    ovr_path = os.path.join(tmp_dir, f"{stem}.ovr")
                    if os.path.exists(ovr_path):
                        dupes += 1
                        # Prefix with folder to de-duplicate
                        ovr_path = os.path.join(tmp_dir, f"{folder_name}_{stem}.ovr")

                    with open(ovr_path, "w", encoding="utf-8") as fh:
                        json.dump(unit.to_dict(), fh, indent=2)
                    written += 1

                    if warnings_list:
                        status = "warn"

                except Exception as e:
                    status = "crash"
                    exc_str = f"{type(e).__name__}: {e}"
                    tb = traceback.format_exc().splitlines()
                    exc_str += " || " + " | ".join(tb[-3:])
                    crashes.append((folder_name, fpath.name, exc_str))

                status_counts[status] += 1
                folder_counts[folder_name][status] += 1

        # ── Zip all .ovr files ────────────────────────────────────────────
        ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
        print(f"\nWriting {ZIP_PATH} ({written} files)...", flush=True)

        with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for fname in sorted(os.listdir(tmp_dir)):
                if fname.endswith(".ovr"):
                    zf.write(os.path.join(tmp_dir, fname), arcname=fname)

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    # ── Summary ───────────────────────────────────────────────────────────
    elapsed = time.time() - t0
    print("\n" + "=" * 60)
    print(f"TOTAL FILES: {total}")
    print(f"  ok:      {status_counts['ok']}")
    print(f"  warn:    {status_counts['warn']}")
    print(f"  crash:   {status_counts['crash']}")
    print(f"  written: {written}")
    if dupes:
        print(f"  duplicate stems (renamed): {dupes}")

    print("\nPER-FOLDER:")
    for folder_name, _ in SOURCES:
        c = folder_counts[folder_name]
        if c:
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
            print(f"  ... and {len(crashes) - 50} more")

    zip_size = ZIP_PATH.stat().st_size if ZIP_PATH.exists() else 0
    print(f"\nZip size: {zip_size:,} bytes")
    print(f"Done in {elapsed:.1f} seconds.")


if __name__ == "__main__":
    run()
