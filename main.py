# main.py

import streamlit as st
from TYPES_OF_WINE import display_wine_types
from HOMEPAGE import display_homepage, what_is_wine
from MAKING_PROCESS import making_process

# Create a sidebar navigation option
selected_page = st.sidebar.radio("**Select Page**", ("📚Home Page", "🍇Making Process", "🍷Types of Wine"))

# Run the appropriate Streamlit script based on the selected page
if selected_page == "📚Home Page":
    display_homepage()
    what_is_wine()
elif selected_page == "🍇Making Process":
    making_process()
elif selected_page == "🍷Types of Wine":
    display_wine_types()
