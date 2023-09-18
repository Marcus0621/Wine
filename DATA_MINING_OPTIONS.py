import streamlit as st
from WINE_PREDICTION import wine_quality_prediction
from DATA_DESCRIPTION import data_description
from DATA_VISUALISATION import data_visualisation

def display_wine_insights():
    system_type = st.sidebar.radio("**Select a Wine Prediction**", ["📖DATA DESCRIPTION","📊DATA VISUALISATION","📉WINE QUALITY PREDICTION SYSTEM"])

    if system_type:
        if system_type == "📖DATA DESCRIPTION":
            data_description()
        elif system_type ==  "📊DATA VISUALISATION":
            data_visualisation()   
        elif system_type == "📉WINE QUALITY PREDICTION SYSTEM":
            wine_quality_prediction()