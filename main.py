# main.py

import streamlit as st
from TYPES_OF_WINE import display_wine_types
from HOMEPAGE import display_homepage

# Create a sidebar navigation option
selected_page = st.sidebar.radio("Select Page", ("📚Home Page", "🍷Types of Wine"))

# Run the appropriate Streamlit script based on the selected page
if selected_page == "📚Home Page":
    display_homepage()
elif selected_page == "🍷Types of Wine":
    display_wine_types()
