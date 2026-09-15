@echo off
title Portal Sorters Andreani - Servidor Local Docsify
echo ========================================================
echo   Iniciando Portal de Documentacion Sorters Andreani
echo ========================================================
echo.
echo Abriendo en http://localhost:3000 ...
echo Presione CTRL+C en esta ventana para detener el servidor.
echo.

cd /d "%~dp0\.."
start "" "http://localhost:3000"
python -m http.server 3000

pause
