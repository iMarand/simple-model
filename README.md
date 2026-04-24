# Names: HAKIZIMANA MARTIN Armand

# Student Performance Prediction System

A machine learning model using Logistic Regression to predict student PASS/FAIL status based on study hours and attendance.

## Project Structure

```
Flask/
├── app.py                    # Flask application (main server)
├── model.py                  # Model training script
├── prediction_model.pkl      # Trained model (generated after running model.py)
├── scaler.pkl               # Feature scaler (generated after running model.py)
├── form.html                # Prediction form (HTML/CSS/JS)
├── README.md                # This file
└── templates/               # Flask templates folder (for form.html)
    └── form.html            # Move form.html here for Flask
```

## Installation

1. **Install required packages:**
```bash
pip install flask scikit-learn numpy joblib
```

2. **Project setup:**
   - Ensure all files are in the `d:\Projects\Flask\` directory
   - Move `form.html` to a `templates` subfolder for Flask to serve it

## Usage

### Step 1: Train the Model

Run the model training script to create the prediction model:

```bash
python model.py
```

This will:
- Train a Logistic Regression model on sample data
- Save the model as `prediction_model.pkl`
- Save the feature scaler as `scaler.pkl`
- Display test predictions and accuracy

**Output:**
```
✓ Model trained and saved successfully!
✓ Model accuracy on training data: 95.00%
```

### Step 2: Run the Flask Application

Start the Flask server:

```bash
python app.py
```

The server will run on `http://localhost:5000/`

### Step 3: Use the Prediction Form

1. Open your browser and go to `http://localhost:5000/`
2. Enter:
   - **Study Hours**: Number of hours studied (e.g., 5)
   - **Attendance**: Attendance percentage (0-100, e.g., 75)
3. Click **Predict** button
4. View the result:
   - PASS or FAIL prediction
   - Confidence percentage
   - Probability breakdown (PASS/FAIL chances)

## Model Details

### Features (Inputs)
- **Study Hours**: 0 to 10+ hours
- **Attendance**: 0 to 100%

### Target (Output)
- **PASS**: 1
- **FAIL**: 0

### Algorithm
- **Logistic Regression** (Binary Classification)
- Standardized features for better performance
- Training accuracy: ~95%

### Prediction Logic
The model learns patterns from training data:
- Generally: Study hours ≥ 4 and Attendance ≥ 75% = PASS
- Generally: Study hours ≥ 5 and Attendance ≥ 60% = PASS
- Otherwise = FAIL

## API Endpoint

### POST /predict

**Request:**
```json
{
  "study_hours": 5,
  "attendance": 75
}
```

**Success Response:**
```json
{
  "success": true,
  "result": "PASS",
  "confidence": "92.3%",
  "study_hours": 5,
  "attendance": 75,
  "pass_probability": "92.3%",
  "fail_probability": "7.7%"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Invalid input. Please enter valid numbers."
}
```

## UI Features

- **Light Theme**: White background with blue accents
- **Responsive Design**: Works on desktop and mobile
- **Real-time Validation**: Input validation before prediction
- **Visual Feedback**: 
  - Animated result display
  - Probability bars (PASS/FAIL)
  - Confidence percentage
  - Error messages with styling
- **Interactive**: Button to make multiple predictions

## Customization

### To retrain with different data:
Edit the `X_train` and `y_train` arrays in `model.py` with your own data.

### To change port:
In `app.py`, modify the last line:
```python
app.run(debug=True, port=YOUR_PORT)
```

### To modify UI colors:
Edit the CSS in `form.html` to change the blue theme to your preferred colors.

## Troubleshooting

**Error: "Model files not found"**
- Solution: Run `python model.py` first to train the model

**Error: "Template not found"**
- Solution: Ensure `form.html` is in a `templates` subfolder

**Port already in use**
- Solution: Change the port in `app.py` or kill the process using port 5000

## License

Free to use and modify.
