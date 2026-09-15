@echo off
title Sincronizador GitOps SPP - Andreani
echo ========================================================
echo   Sincronizando Aplicaciones SPP desde GitOps Platform
echo ========================================================
echo.

cd /d "%~dp0\.."
python scripts\sync-gitops.py

echo.
pause
