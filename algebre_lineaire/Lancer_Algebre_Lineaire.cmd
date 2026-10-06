@echo off
setlocal
cd /d "%~dp0"
set "algebre_python=%~dp0..\.venv\Scripts\python.exe"
if exist "%algebre_python%" goto dependencies
set "algebre_python=%~dp0.venv\Scripts\python.exe"
if exist "%algebre_python%" goto dependencies
where py >nul 2>nul
if not errorlevel 1 goto create_py
where python >nul 2>nul
if not errorlevel 1 goto create_python
set "algebre_bundled=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%algebre_bundled%" goto create_bundled
echo Python 3.10 ou plus recent est requis.
echo Installez Python avec Ajouter Python au PATH, puis relancez ce fichier.
pause
exit /b 1
:create_py
py -3 -m venv .venv
goto created
:create_python
python -m venv .venv
goto created
:create_bundled
"%algebre_bundled%" -m venv .venv
:created
if errorlevel 1 goto failed
:dependencies
"%algebre_python%" -c "import numpy,sympy" >nul 2>nul
if not errorlevel 1 goto launch
echo Premiere ouverture : installation de NumPy et SymPy depuis PyPI. Connexion Internet requise.
"%algebre_python%" -m pip install -r requirements.txt
if errorlevel 1 goto failed
:launch
"%algebre_python%" -X utf8 algebre_lineaire.py %*
if errorlevel 1 goto failed
exit /b 0
:failed
echo Le lancement a echoue. Consultez LISEZ_MOI.md pour le lancement manuel.
pause
exit /b 1
