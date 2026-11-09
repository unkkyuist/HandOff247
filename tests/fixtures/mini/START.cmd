@echo off
REM Double-click to start the web console.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1" serve
start "" "http://127.0.0.1:5050/"
if errorlevel 1 exit /b %errorlevel%
