from xgboost import XGBClassifier
import joblib
import pandas as pd

# Load model and preprocessor
model = XGBClassifier()
model.load_model("xgboost_model.json")
preprocessor = joblib.load("preprocessor.joblib")

# New patient data
new_patient = pd.DataFrame([{
    "age": 45,
    "gender": "Male",
    "blood_type": "A+",
    "medical_condition": "Diabetes",
    "admission_type": "Urgent",
    "medication": "Aspirin",
    "billing_amount": 20000
}])

# Preprocess and predict
X_new      = preprocessor.transform(new_patient)
prediction = model.predict(X_new)

label_map  = {0: "Normal", 1: "Abnormal", 2: "Inconclusive"}
print(f"Predicted result: {label_map[prediction[0]]}")