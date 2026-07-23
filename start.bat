@echo off
title Webhook Spammer
chcp 65001 >nul 2>&1
echo.
echo Starting Webhook Spammer...
if not exist "%cd%\venv" (
    echo Installing dependencies...
    pip install -r requirements.txt --quiet
)
py webhook-spammer.py
pause
