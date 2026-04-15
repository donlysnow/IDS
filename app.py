import streamlit as st
import numpy as np
import joblib

# Load files
model = joblib.load("IDS_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("🚨 Intrusion Detection System (IDS)")
st.write("Enter feature values below:")

# Create input fields dynamically
inputs = []

for feature in features:
    value = st.number_input(feature, value=0.0)
    inputs.append(value)

# Predict button
if st.button("Predict"):
    data = np.array(inputs, dtype=float).reshape(1, -1)

    # Scale input
    scaled = scaler.transform(data)

    # Predict
    pred = model.predict(scaled)[0]

    # Output
    if pred == 0:
        st.success("✅ No Attack Detected")
    else:
        st.error("🚨 Attack Detected")