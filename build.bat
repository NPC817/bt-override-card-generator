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

REM -- Clean previous build output (retry -- AV may lock DLLs) ----------
echo.
echo Cleaning previous build output...
set CLEAN_RETRY=0
:clean_retry
if not exist "dist\BT_Override_Card_Generator" goto clean_done
rmdir /S /Q "dist\BT_Override_Card_Generator" 2>NUL
if not exist "dist\BT_Override_Card_Generator" goto clean_done
set /a CLEAN_RETRY+=1
if !CLEAN_RETRY! GEQ 5 (
    echo [ERROR] Cannot delete dist\BT_Override_Card_Generator -- files locked.
    echo Close any running instances of the app, wait for AV scan to finish.
    pause
    exit /b 1
)
echo Clean attempt !CLEAN_RETRY! failed (files locked). Retrying in 3s...
timeout /t 3 /nobreak >NUL
goto clean_retry
:clean_done
if exist build rmdir /S /Q build 2>NUL
echo Clean done.

REM -- Build with PyInstaller (retry on file-lock failures) ------------
echo.
echo Building BT Override Card Generator...
set BUILD_RETRY=0
:build_retry
.venv_build\Scripts\pyinstaller bt_override.spec --log-level WARN
if !ERRORLEVEL! EQU 0 goto build_ok
set /a BUILD_RETRY+=1
if !BUILD_RETRY! GEQ 3 (
    echo.
    echo [ERROR] PyInstaller failed 3 times. Last exit code: !ERRORLEVEL!.
    echo Check output above for missing imports or file errors.
    pause
    exit /b !ERRORLEVEL!
)
echo PyInstaller attempt !BUILD_RETRY! failed (exit !ERRORLEVEL!). Retrying in 5s...
timeout /t 5 /nobreak >NUL
goto build_retry
:build_ok

REM Verify EXE was created
set EXE_PATH=dist\BT_Override_Card_Generator\BTOverrideCardGenerator.exe
if exist "!EXE_PATH!" goto exe_ok
echo.
echo [ERROR] PyInstaller completed but EXE not found at: !EXE_PATH!
echo Contents of dist\BT_Override_Card_Generator:
dir dist\BT_Override_Card_Generator 2>NUL
pause
exit /b 1
:exe_ok
echo EXE verified: !EXE_PATH!

REM -- Create release zip ----------------------------------------------
echo.
echo Creating release zip...
if not exist dist\Release mkdir dist\Release

REM Remove user data from dist so it does not end up in the zip
if exist "dist\BT_Override_Card_Generator\data\profiles" rmdir /S /Q "dist\BT_Override_Card_Generator\data\profiles"

REM Brief pause -- let AV finish scanning freshly-built DLLs
echo Waiting 5s for AV scan to release file handles...
timeout /t 5 /nobreak >NUL

set ZIP_RETRY=0
:zip_retry
powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('dist\BT_Override_Card_Generator', 'dist\Release\BT_Override_Card_Generator_v%VERSION%.zip')"
if !ERRORLEVEL! EQU 0 goto zip_done
set /a ZIP_RETRY+=1
if !ZIP_RETRY! GEQ 5 (
    echo [ERROR] Zip failed after !ZIP_RETRY! attempts.
    echo A DLL in dist\BT_Override_Card_Generator is locked by another process.
    echo Close any running instances of the app, wait for AV scan to finish, and try again.
    pause
    exit /b 1
)
echo Zip attempt !ZIP_RETRY! failed ^(DLL likely locked by AV scan^). Retrying in 3s...
timeout /t 3 /nobreak >NUL
goto zip_retry
:zip_done

echo.
echo Build complete.
echo Distribution:  dist\BT_Override_Card_Generator\
echo Release zip:   dist\Release\BT_Override_Card_Generator_v%VERSION%.zip
pause
