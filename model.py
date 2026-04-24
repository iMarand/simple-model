import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Sample training data: Study Hours, Attendance (%)
X_train = np.array([
    [2, 40],
    [3, 50],
    [4, 60],
    [5, 70],
    [6, 80],
    [7, 85],
    [1, 30],
    [2, 35],
    [3, 40],
    [4, 50],
    [5, 65],
    [6, 75],
    [7, 80],
    [8, 90],
    [9, 95],
    [1, 25],
    [2, 45],
    [3, 55],
    [4, 70],
    [5, 75],
])

# Target: PASS (1) or FAIL (0)
# PASS if: study_hours >= 4 AND attendance >= 75%
# Or: study_hours >= 5 AND attendance >= 60%
# Otherwise FAIL
y_train = np.array([
    0,  # 2 hours, 40% -> FAIL
    0,  # 3 hours, 50% -> FAIL
    0,  # 4 hours, 60% -> FAIL
    1,  # 5 hours, 70% -> PASS
    1,  # 6 hours, 80% -> PASS
    1,  # 7 hours, 85% -> PASS
    0,  # 1 hour, 30% -> FAIL
    0,  # 2 hours, 35% -> FAIL
    0,  # 3 hours, 40% -> FAIL
    0,  # 4 hours, 50% -> FAIL
    1,  # 5 hours, 65% -> PASS
    1,  # 6 hours, 75% -> PASS
    1,  # 7 hours, 80% -> PASS
    1,  # 8 hours, 90% -> PASS
    1,  # 9 hours, 95% -> PASS
    0,  # 1 hour, 25% -> FAIL
    0,  # 2 hours, 45% -> FAIL
    0,  # 3 hours, 55% -> FAIL
    1,  # 4 hours, 70% -> PASS
    1,  # 5 hours, 75% -> PASS
])

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(model, 'prediction_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model trained and saved successfully.")
print(f"Model accuracy on training data: {model.score(X_train_scaled, y_train):.2%}")

# Test predictions
test_data = np.array([
    [5, 75],  # Should be PASS
    [3, 50],  # Should be FAIL
    [7, 90],  # Should be PASS
])

test_scaled = scaler.transform(test_data)
predictions = model.predict(test_scaled)
probabilities = model.predict_proba(test_scaled)

print("\nTest Predictions:")
for i, (study_hours, attendance) in enumerate(test_data):
    result = "PASS" if predictions[i] == 1 else "FAIL"
    confidence = probabilities[i][predictions[i]] * 100
    print(f"Study Hours: {study_hours}, Attendance: {attendance}% -> {result} (Confidence: {confidence:.1f}%)")
