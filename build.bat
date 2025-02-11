@echo off
"C:\Users\ridoy\py\venv\Scripts\pyside6-rcc.exe" src/battery_monitor/resources.qrc -o src/battery_monitor/data/resources_rc.py
if errorlevel 1 (
    echo ERROR: Failed to compile resource file.
    pause
    exit /b 1
)
echo Resource file compiled successfully.
pause