import streamlit as st

st.set_page_config(page_title="Car vs Bike Classification App", layout="wide")

import eda
import prediction

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("EDA", "Prediction"))

if page == "EDA":
    eda.app()
elif page == "Prediction":
    prediction.app()