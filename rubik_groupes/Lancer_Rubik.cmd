@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 goto with_py
where python >nul 2>nul
if not errorlevel 1 goto with_python
set "rubik_python=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%rubik_python%" goto with_bundled
echo Python 3.10 ou plus recent est requis.
echo Installez Python avec l'option Ajouter Python au PATH, puis relancez ce fichier.
pause
exit /b 1
:with_py
py -3 -X utf8 rubik_groupes.py %*
goto finished
:with_python
python -X utf8 rubik_groupes.py %*
goto finished
:with_bundled
"%rubik_python%" -X utf8 rubik_groupes.py %*
:finished
if errorlevel 1 pause
endlocal
