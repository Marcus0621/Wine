# HOMEPAGE.py

import streamlit as st
from PIL import Image

def display_homepage():
    welcome_title = st.title("WELCOME TO THE WORLD OF WINE!")
    first_image = Image.open('WineIntro.jpg')
    image_placeholder = st.empty()
    caption_placeholder = st.empty()
    image_placeholder.image(first_image, caption='Image by 1Zoom', use_column_width=True)

def what_is_wine():
    st.title("WHAT IS WINE?")
    st.write("Wine is an alcoholic beverage that is made from fermented grapes or other fruits. The fermentation process involves the conversion of sugars present in the fruit into alcohol and carbon dioxide, typically through the action of yeast. Wine has been produced and enjoyed by various cultures for thousands of years and holds cultural, social, and culinary significance in many societies.")
    st.write("The process of making wine including: Harvesting, Crushing, Pressing, Fermentation, Racking, Aging, Blending, Clarification, Bottling, Labeling and Packaging")
