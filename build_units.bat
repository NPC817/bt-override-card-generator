@echo off
cd /d "%~dp0"
echo === Rebuilding data/units.zip from MUL_Files ===
echo.
call .venv\Scripts\activate
python scripts/build_unit_database.py
echo.
pause
