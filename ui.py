import streamlit as st
import requests

st.title("Healthcare Test Result Predictor")

age = st.number_input("Age", 0, 120)
gender = st.selectbox("Gender", ["Male", "Female"])
blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
admission_type = st.selectbox("Admission Type", ["Emergency", "Urgent", "Elective"])
billing_amount = st.number_input("Billing Amount")
medical_condition = st.text_input("Medical Condition")
medication = st.text_input("Medication")

if st.button("Predict"):

    payload = {
        "age": age,
        "gender": gender,
        "blood_type": blood_type,
        "medical_condition": medical_condition,
        "admission_type": admission_type,
        "medication": medication,
        "billing_amount": billing_amount
    }

    response = requests.post(
        "https://health-api-1-4862.onrender.com",
        json=payload
    )

    st.write(response.json())