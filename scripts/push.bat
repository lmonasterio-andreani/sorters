@echo off
title Sincronizar Cambios con GitHub - Andreani
echo ========================================================
echo   Empujando cambios a ambos repositorios GitHub:
echo   1. infrastructure-services/observabilidad-sorters
echo   2. lmonasterio-andreani/sorters
echo ========================================================
echo.

cd /d "%~dp0\.."
git push origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Intentando push al remoto personal directamente...
    git push personal main
)

echo.
echo ========================================================
echo   Proceso finalizado.
echo ========================================================
echo.
pause
