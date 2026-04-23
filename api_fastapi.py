from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from xgboost import XGBClassifier

app = FastAPI()

model = XGBClassifier()
model.load_model("xgboost_model.json")
# preprocessor = joblib.load("preprocessor.joblib")

LABEL_MAP = {0: "Normal", 1: "Abnormal", 2: "Inconclusive"}

class Patient(BaseModel):
    age: int
    gender: str
    blood_type: str
    medical_condition: str
    admission_type: str
    medication: str
    billing_amount: float

@app.get("/")
def home():
    return {"status": "FastAPI is running ✓"}

@app.post("/predict")
def predict(patient: Patient):
    data   = pd.DataFrame([patient.model_dump()])
    X      = preprocessor.transform(data)
    pred   = model.predict(X)[0]
    return {"prediction": LABEL_MAP[int(pred)]}