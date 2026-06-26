import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("crop_recommendation_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Crop Recommendation System")
st.write("Enter the soil and weather details below.")

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=90)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=42)
K = st.number_input("Potassium (K)", min_value=0, max_value=250, value=43)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=20.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=500.0,
    value=200.0
)

# Prediction
if st.button("Predict Crop"):

    input_data = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })

    prediction = model.predict(input_data)

    st.success(f"🌱 Recommended Crop: {prediction[0]}")
