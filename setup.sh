#!/bin/bash
# Setup script for Student Performance Prediction System

echo ""
echo "==============================================="
echo "Student Performance Prediction System"
echo "==============================================="
echo ""

echo "[1] Checking Python installation..."
python3 --version

if [ $? -ne 0 ]; then
    echo "ERROR: Python3 is not installed or not in PATH"
    exit 1
fi

echo ""
echo "[2] Installing required packages..."
pip3 install flask scikit-learn numpy joblib

if [ $? -ne 0 ]; then
    echo "ERROR: Package installation failed"
    exit 1
fi

echo ""
echo "[3] Training the prediction model..."
python3 model.py

if [ $? -ne 0 ]; then
    echo "ERROR: Model training failed"
    exit 1
fi

echo ""
echo "==============================================="
echo "Setup completed successfully!"
echo "==============================================="
echo ""
echo "Next steps:"
echo "1. Run: python3 app.py"
echo "2. Open browser: http://69.169.109.243:5200/"
echo ""