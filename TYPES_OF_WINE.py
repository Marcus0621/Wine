import streamlit as st
from RED_WINE import red_intro, cab, merlot, shiraz

def display_wine_types():
    wine_type = st.sidebar.radio("**Select a Wine Type**", ["🔴RED WINE", "🟡WHITE WINE", "❤️ROSE WINE", "🟠AMBER WINE", "🎂DESSERT WINE", "🫧SPARKLING WINE"])

    if wine_type:
        if wine_type == "🔴RED WINE":
            st.title("INTO THE WORLD OF RED WINE")
            red_intro()
            cab()
            merlot()
            shiraz()
        elif wine_type == "🟡WHITE WINE":
            st.title("White Wine Information")
        elif wine_type == "❤️ROSE WINE":
            st.title("Rosé Wine Information")
        elif wine_type == "🟠AMBER WINE":
            st.title("Amber Wine Information")
        elif wine_type == "🎂DESSERT WINE":
            st.title("Dessert Wine Information")
        elif wine_type == "🫧SPARKLING WINE":
            st.title("Sparkling Wine Information")


