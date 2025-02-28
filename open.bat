@echo off
title Checking python..
python --version >nul 2>&1
if %errorlevel% neq 0 (
    title Python not found, opening webpage..
    echo Python is not installed, opening webpage..
    start "" "https://www.python.org/downloads/"  
    exit
) else (
    title Running multitools..
    echo Meets requirements! Continuing...
    python multitools.py
)