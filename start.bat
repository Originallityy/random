@echo off
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Redirecting to the download page...
    start "" "https://www.python.org/downloads/"
    exit /b
)
REM Only run the code if Python is installed
python home.py