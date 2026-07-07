@echo off
setlocal enabledelayedexpansion
echo === BT Override Card Generator Build ===
echo.

REM -- Parse version and generate version_metadata.txt ------------------
for /f %%a in ('python build_metadata.py') do set VERSION=%%a
if "%VERSION%"=="" set VERSION=0.1.0
echo Building version: %VERSION%

REM -- Clean build venv ------------------------------------------------
set RECREATE_VENV=0
if not exist .venv_build (
    set RECREATE_VENV=1
) else (
    REM Check if requirements.txt changed since last venv creation
    for /f %%h in ('certutil -hashfile requirements.txt MD5 2^>NUL ^| findstr /v "hash CertUtil"') do set REQ_HASH_CUR=%%h
    if exist .venv_build\requirements_hash.txt (
        set /p REQ_HASH_OLD=<.venv_build\requirements_hash.txt
    ) else (
        set REQ_HASH_OLD=
    )
    if not "!REQ_HASH_CUR!"=="!REQ_HASH_OLD!" set RECREATE_VENV=1
)

if "!RECREATE_VENV!"=="1" (
    echo Creating clean build venv...
    if exist .venv_build rmdir /S /Q .venv_build
    python -m venv .venv_build
    REM Store hash for future comparison
    for /f %%h in ('certutil -hashfile requirements.txt MD5 2^>NUL ^| findstr /v "hash CertUtil"') do echo %%h>.venv_build\requirements_hash.txt
)

echo Installing dependencies...
.venv_build\Scripts\pip install --upgrade --quiet PyQt6>=6.6.0 PyYAML>=6.0.1 reportlab>=4.1.0 Pillow>=10.0.0 pyinstaller>=6.0 certifi

echo.
echo Building BT Override Card Generator...
.venv_build\Scripts\pyinstaller bt_override.spec --clean

REM -- Create release zip ----------------------------------------------
echo.
echo Creating release zip...
if not exist dist\Release mkdir dist\Release

REM Remove user data from dist so it does not end up in the zip
if exist "dist\BT_Override_Card_Generator\data\profiles" rmdir /S /Q "dist\BT_Override_Card_Generator\data\profiles"

powershell -Command "Compress-Archive -Path 'dist\BT_Override_Card_Generator' -DestinationPath 'dist\Release\BT_Override_Card_Generator_v%VERSION%.zip' -Force"

echo.
echo Build complete.
echo Distribution:  dist\BT_Override_Card_Generator\
echo Release zip:   dist\Release\BT_Override_Card_Generator_v%VERSION%.zip
pause
