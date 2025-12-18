import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Polynomial Regression Predictor", layout="centered")

st.title("Polynomial Regression Predictor")
st.write("Enter input value to get prediction from trained model.")

# Load trained model
with open("LR.pkl", "rb") as f:
    model = pickle.load(f)

# User input
x_input = st.number_input("Enter Temperature value", value=0.0)

# Predict button
if st.button("Predict"):
    # model expects 2D input
    x_array = np.array([[x_input]])
    prediction = model.predict(x_array)

    st.success(f"Predicted Output: {prediction[0]:.2f}")

