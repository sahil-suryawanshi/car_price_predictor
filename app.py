import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Predictor")
st.write("Enter car details to predict its selling price.")

# Input fields
name = st.text_input("Car Name", "Maruti Suzuki Swift")
company = st.text_input("Company", "Maruti")
year = st.number_input("Year", min_value=1990, max_value=2030, value=2019)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

# Prediction button
if st.button("Predict Price"):
    
    input_data = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=["name", "company", "year", "kms_driven", "fuel_type"]
    )

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Car Price: ₹ {prediction:,.0f}")