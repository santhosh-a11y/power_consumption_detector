import streamlit as st
import pickle

@st.Cache_resource

def load_model(LR.pkl):
    with open(LR.pkl, "rb") as f:
        return pickle.load(f)

model = load_model("LR.pkl")

st.title("My Pickle-Powered App")
