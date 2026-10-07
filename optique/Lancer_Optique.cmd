@echo off
setlocal
cd /d "%~dp0"
set "optique_python=%~dp0..\.venv\Scripts\python.exe"
if exist "%optique_python%" goto dependencies
set "optique_python=%~dp0.venv\Scripts\python.exe"
if exist "%optique_python%" goto dependencies
where py >nul 2>nul
if not errorlevel 1 goto create_py
where python >nul 2>nul
if not errorlevel 1 goto create_python
set "optique_bundled=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%optique_bundled%" goto create_bundled
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
"%optique_bundled%" -m venv .venv
:created
if errorlevel 1 goto failed
:dependencies
"%optique_python%" -c "import numpy" >nul 2>nul
if not errorlevel 1 goto launch
echo Premiere ouverture : installation de NumPy depuis PyPI. Connexion Internet requise.
"%optique_python%" -m pip install -r requirements.txt
if errorlevel 1 goto failed
:launch
"%optique_python%" -X utf8 optique.py %*
if errorlevel 1 goto failed
exit /b 0
:failed
echo Le lancement a echoue. Consultez LISEZ_MOI.md pour le lancement manuel.
pause
exit /b 1
