import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="🌾 Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------

@st.cache_resource
def load_model():
    with open("crop_recommendation_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------------------
# Title
# -------------------------------

st.title("🌾 Smart Crop Recommendation System")

st.markdown(
"""
Predict the best crop based on:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall
"""
)

st.divider()

# -------------------------------
# User Inputs
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 200, 90)
    P = st.number_input("Phosphorus (P)", 0, 200, 42)
    K = st.number_input("Potassium (K)", 0, 200, 43)
    temperature = st.number_input("Temperature (°C)", value=20.0)

with col2:
    humidity = st.number_input("Humidity (%)", value=80.0)
    ph = st.number_input("Soil pH", value=6.5)
    rainfall = st.number_input("Rainfall (mm)", value=200.0)

# -------------------------------
# Prediction
# -------------------------------

if st.button("🌱 Predict Crop", use_container_width=True):

    sample = pd.DataFrame({
        "N":[N],
        "P":[P],
        "K":[K],
        "temperature":[temperature],
        "humidity":[humidity],
        "ph":[ph],
        "rainfall":[rainfall]
    })

    prediction = model.predict(sample)

    st.success(f"Recommended Crop: **{prediction[0]}**")

    st.balloons()
