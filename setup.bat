@echo off
REM Setup script for Student Performance Prediction System

echo.
echo ===============================================
echo Student Performance Prediction System
echo ===============================================
echo.

echo [1] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo [2] Installing required packages...
pip install flask scikit-learn numpy joblib

echo.
echo [3] Training the prediction model...
python model.py

if %errorlevel% neq 0 (
    echo ERROR: Model training failed
    pause
    exit /b 1
)

echo.
echo ===============================================
echo Setup completed successfully!
echo ===============================================
echo.
echo Next steps:
echo 1. Run: python app.py
echo 2. Open browser: http://localhost:5000/
echo.
pause
