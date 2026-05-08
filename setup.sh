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
echo "[2] Creating virtual environment..."

if [ ! -d "venv" ]; then
    python3 -m venv venv

    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        echo "Trying to install python3-venv..."

        apt update
        apt install -y python3-venv

        python3 -m venv venv

        if [ $? -ne 0 ]; then
            echo "ERROR: Could not create virtual environment"
            exit 1
        fi
    fi
fi

echo ""
echo "[3] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[4] Installing required packages..."
pip install flask scikit-learn numpy joblib

if [ $? -ne 0 ]; then
    echo "ERROR: Package installation failed"
    exit 1
fi

echo ""
echo "[5] Training the prediction model..."
python model.py

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
echo "1. Activate environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run server:"
echo "   python app.py"
echo ""
echo "3. Open browser:"
echo "   http://69.169.109.243:5200/"
echo ""
echo "IMPORTANT:"
echo "Make sure app.py contains:"
echo "app.run(host='0.0.0.0', port=5200)"
echo ""