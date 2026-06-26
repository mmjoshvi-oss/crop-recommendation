import streamlit as st
import pickle
import os
import sklearn

st.write("Current directory:", os.getcwd())
st.write("Files:", os.listdir())
st.write("Scikit-learn version:", sklearn.__version__)

try:
    with open("crop_recommendation_model.pkl", "rb") as file:
        model = pickle.load(file)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(str(e))
    st.stop()
