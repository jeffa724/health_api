from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
import pandas as pd
import joblib
from xgboost import XGBClassifier
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode="require"
)


# Load model and preprocessor
model = XGBClassifier()
model.load_model("xgboost_model.json")
preprocessor = joblib.load("preprocessor.joblib")

# Label map
LABEL_MAP = {0: "Normal", 1: "Abnormal", 2: "Inconclusive"}

# Define the input structure
class Patient(BaseModel):
    age: int
    gender: str
    blood_type: str
    medical_condition: str
    admission_type: str
    medication: str
    billing_amount: float

# Create the app
app = FastAPI()

# Health check endpoint
@app.get("/")
def home():
    return {"status": "API is running ✓"}

# Prediction endpoint
@app.post("/predict")
def predict(patient: Patient):
    # Convert input to dataframe
    data = pd.DataFrame([patient.model_dump()])

    # Preprocess and predict
    X        = preprocessor.transform(data)
    pred     = model.predict(X)[0]
    result   = LABEL_MAP[int(pred)]

    return {
        "prediction": result,
        "input":      patient.model_dump()
    }