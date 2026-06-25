import pickle
import pandas as pd
import streamlit as st

with open("your_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Crop Recommendation App")

N = st.number_input("Nitrogen (N)", min_value=0.0, value=90.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, value=42.0)
K = st.number_input("Potassium (K)", min_value=0.0, value=43.0)
temperature = st.number_input("Temperature", min_value=0.0, value=21.0)
humidity = st.number_input("Humidity", min_value=0.0, value=82.0)
ph = st.number_input("Soil pH", min_value=0.0, value=6.5)
rainfall = st.number_input("Rainfall", min_value=0.0, value=203.0)

if st.button("Recommend Crop"):
    input_data = pd.DataFrame([{
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Recommended Crop: {prediction.title()}")
