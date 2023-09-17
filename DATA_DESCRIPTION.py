import streamlit as st
import pandas as pd

def data_description():
    st.title("Red Wine Dataset Description")
    st.write("The dataset for this research is about the red wine called “Vinho Verde” from Portuguese. This dataset has been collected from Kaggle website. The dataset contains 12 columns and 1599 rows. The attributes of the dataset including fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol and quality.")
    
    wine_data = pd.read_csv('winequality-red.csv')
    st.dataframe(wine_data)

    st.write("***Fixed Acidity*** – The majority of the acids in wine are fixed or non-volatile.")
    st.write("***Volatile Acidity*** - The quantity of acetic acid in wine, which at too high of level can give wine a bad or vinegar-like flavour.")
    st.write("***Citric Acid*** – Found in small quantities and may give the wine a 'freshness' flavour.")
    st.write("***Residual Sugar*** – The quantity of sugar left over after fermentation is complete.")
    st.write("***Chlorides*** – The wine's salt content.")
    st.write("***Free Sulfur Dioxide*** – The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfited ion; it prevents microbial growth and oxidation of wine.")
    st.write("***Total Sulfur Dioxide*** – The amount of both free and bound forms of SO2. Low concentrations of SO2 are mostly imperceptible in wine, but when free SO2 levels exceed 50 ppm, it can be detected in the aroma and taste of the wine.")
    st.write("***Density*** – Density is comparable to that of water and is dependent on the alcohol and sugar content.")
    st.write("***pH*** – pH is a measure of a wine's acidity or basicity on a scale of 0 to 14 with most wines falling between 3 and 4 on the pH scale.")
    st.write("***Sulphates*** – Sulphates are an additive in wine that can raise the level of sulfur dioxide (SO2) gas, which functions as an antioxidant and antimicrobial.")
    st.write("***Alcohol*** – Alcohol percentage refers to the amount of alcohol present in the wine.")
    st.write("***Quality*** – The wine quality rating from 3 to 8.")