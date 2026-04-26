import streamlit as st
import requests

st.title("AI Audit Dashboard")

income = st.number_input("Income")
age = st.number_input("Age")

if st.button("Predict"):
    data = {"income": income, "age": age}
    res = requests.post("http://localhost:8000/predict", json=data)

    st.write(res.json())