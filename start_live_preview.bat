@echo off
echo ==============================================
echo 📚 Course Manual System - Live Preview Builder
echo ==============================================
echo.

echo [1/3] Enabling interactive executable code cells across all modules...
C:\Python313\python.exe scripts\enable_executable_cells.py

echo.
echo [2/3] Scanning content/ folder and building navigation menu...
C:\Python313\python.exe scripts\auto_build_menu.py

echo.
echo [2/2] Starting Jupyter Book Live Server...
echo ⚠️  DO NOT CLOSE THIS WINDOW. Press Ctrl+C to stop the server.
echo 👉 The book will open automatically, or go to http://localhost:3000
echo.

"C:\Users\DENZEN COMPUTER\AppData\Roaming\Python\Python313\Scripts\jupyter-book.exe" start
