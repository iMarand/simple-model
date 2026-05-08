from pathlib import Path

import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "prediction_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"


def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("Model and scaler loaded successfully.")
        return model, scaler, None
    except FileNotFoundError:
        message = "Model files not found. Run: python model.py"
        print(message)
        return None, None, message


model, scaler, load_error = load_artifacts()


def build_prediction(study_hours, attendance):
    input_data = np.array([[study_hours, attendance]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    return {
        "result": "PASS" if prediction == 1 else "FAIL",
        "confidence": f"{probabilities[prediction] * 100:.1f}%",
        "study_hours": study_hours,
        "attendance": attendance,
        "pass_probability": f"{probabilities[1] * 100:.1f}%",
        "fail_probability": f"{probabilities[0] * 100:.1f}%",
    }


@app.route("/", methods=["GET", "POST"])
def index():
    error = load_error
    prediction = None

    if request.method == "POST":
        try:
            study_hours = float(request.form.get("study_hours", ""))
            attendance = float(request.form.get("attendance", ""))
        except ValueError:
            error = "Please enter valid numbers."
        else:
            if study_hours < 0 or attendance < 0 or attendance > 100:
                error = "Study hours must be 0 or more, and attendance must be between 0 and 100."
            elif model is None or scaler is None:
                error = "Model is not loaded. Run: python model.py"
            else:
                prediction = build_prediction(study_hours, attendance)

    return render_template("form.html", error=error, prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)
