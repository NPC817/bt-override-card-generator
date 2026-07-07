@echo off
cd /d "%~dp0"
start cmd /k ".venv\Scripts\activate && echo Venv active. Run: python main.py"
