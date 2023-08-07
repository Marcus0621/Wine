# HOMEPAGE.py

import streamlit as st
from PIL import Image
import TYPES_OF_WINE  # Importing the types of wine script

def main():
    st.title("WELCOME TO THE WORLD OF WINE!")
    first_image = Image.open('WineIntro.jpg')
    st.image(first_image, caption='Image by 1Zoom', use_column_width=True)
    
    # Create a button to navigate to the types of wine page
    if st.button("Explore Types of Wine"):
        TYPES_OF_WINE.display_wine_types()

if __name__ == "__main__":
    main()
