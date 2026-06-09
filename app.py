import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

# User Inputs
tenure = st.slider("Tenure", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])

# Create dataframe with ALL training features
input_data = pd.DataFrame(columns=model.feature_names_in_)

# Fill all values with 0
input_data.loc[0] = 0

# Add user values
input_data['tenure'] = tenure
input_data['MonthlyCharges'] = MonthlyCharges
input_data['TotalCharges'] = TotalCharges
input_data['SeniorCitizen'] = SeniorCitizen

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")