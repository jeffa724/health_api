# 🏥 Healthcare Analytics API

A machine learning API that predicts patient test results as **Normal**, **Abnormal**, or **Inconclusive** using a trained XGBoost/Random Forest model. Built with FastAPI and deployed on Vercel.

---

## 📁 Project Structure

```
HEALTH/
├── data/
│   ├── healthcare_dataset.csv     # Raw dataset from Kaggle
│   └── cleaned_data.csv           # Cleaned dataset
├── notebooks/
│   ├── 01_data_ingestion.ipynb    # Data loading & cleaning
│   ├── database.ipynb             # Database setup & storage
│   ├── ml_data_preparation.ipynb  # Feature engineering
│   └── train_model.ipynb          # Model training & evaluation
├── api_fastapi.py                 # FastAPI application (alternative)
├── api.py                         # API entry point
├── main.py                        # Main application file
├── predict.py                     # Prediction logic
├── xgboost_model.json             # Saved trained model
├── requirements.txt               # Python dependencies
├── vercel.json                    # Vercel deployment config
└── README.md
```

---

## 📖 Project Description

This project builds an end-to-end healthcare analytics system using the [Kaggle Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset/data).

**What it does:**
- Cleans and preprocesses 10,000+ patient records
- Trains a machine learning model to predict lab test results
- Serves predictions through a REST API
- Auto-retrains the model every **Saturday at 12:00 noon UTC**

**Target:** `test_results` → Normal | Abnormal | Inconclusive

**Features used:**

| Feature | Type | Description |
|---|---|---|
| `age` | Numerical | Patient age — clinical predictor |
| `billing_amount` | Numerical | Treatment complexity proxy |
| `length_of_stay` | Numerical | Severity indicator |
| `gender` | Categorical | Biological sex |
| `blood_type` | Categorical | Disease susceptibility |
| `medical_condition` | Categorical | Primary clinical driver |
| `admission_type` | Categorical | Elective / Emergency / Urgent |
| `medication` | Categorical | Treatment type |
| `insurance_provider` | Categorical | Care access patterns |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/jeffa724/health_api.git
cd health_api
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
```
DATABASE_URL=postgresql://user:password@localhost:5432/healthcare_db
```

### 5. Run the notebooks in order
Open Jupyter and run each notebook in the `notebooks/` folder:
```bash
jupyter notebook
```
Run in this order:
1. `01_data_ingestion.ipynb` — clean and load data
2. `database.ipynb` — store data in PostgreSQL
3. `ml_data_preparation.ipynb` — prepare features
4. `train_model.ipynb` — train and save the model

---

## 🚀 How to Run the API

### Locally
```bash
uvicorn main:app --reload --port 8000
```
Then open: **http://localhost:8000/docs**

### With api.py directly
```bash
python api.py
```

---

## 🌐 Live API

The API is deployed on Vercel:
```
https://health-api-jeffa724.vercel.app
```

---

## 📡 Example Request / Response

### `GET /health`
Check if the API is running.

**Request:**
```bash
curl https://health-api-jeffa724.vercel.app/health
```

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true,
  "next_retraining": "2026-04-26 12:00:00+00:00"
}
```

---

### `POST /predict`
Predict a patient's test result.

**Request:**
```bash
curl -X POST https://health-api-jeffa724.vercel.app/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "gender": "Male",
    "blood_type": "A+",
    "medical_condition": "Diabetes",
    "admission_type": "Elective",
    "medication": "Metformin",
    "billing_amount": 15000.00,
    "insurance_provider": "Aetna",
    "length_of_stay": 5
  }'
```

**Response:**
```json
{
  "predicted_result": "Normal",
  "confidence": 0.82,
  "probabilities": {
    "Normal": 0.82,
    "Abnormal": 0.11,
    "Inconclusive": 0.07
  },
  "model_accuracy": 0.87
}
```

---

### `POST /retrain`
Manually trigger model retraining.

**Request:**
```bash
curl -X POST https://health-api-jeffa724.vercel.app/retrain
```

**Response:**
```json
{
  "message": "Retraining complete",
  "accuracy": 0.87
}
```

---

## 🔁 Automatic Retraining

The model retrains automatically **every Saturday at 12:00 UTC** using APScheduler.
To trigger a manual retrain anytime:
```bash
curl -X POST http://localhost:8000/retrain
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| FastAPI | REST API framework |
| XGBoost / Scikit-learn | ML model |
| Pandas | Data cleaning |
| APScheduler | Scheduled retraining |
| PostgreSQL + SQLAlchemy | Database |
| Vercel | Deployment |
| Jupyter Notebooks | Exploration & training |