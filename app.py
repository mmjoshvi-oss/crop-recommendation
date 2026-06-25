import streamlit as st
import pandas as pd
import pickle

try:
    with open("crop_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error("Model loading failed. Check your pickle file and requirements.txt versions.")
    st.exception(e)
    st.stop()
