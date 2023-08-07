import streamlit as st
from PIL import Image

welcome_title = st.title("WELCOME TO THE WORLD OF WINE!")
first_image = Image.open('WineIntro.jpg')
image_placeholder = st.empty()
caption_placeholder = st.empty()
image_placeholder.image(first_image, caption='Image by 1Zoom', use_column_width=True)

button1 = st.sidebar.button("RED WINE")
button2 = st.sidebar.button("WHITE WINE")
button3 = st.sidebar.button("ROSE WINE")
button4 = st.sidebar.button("AMBER WINE")
button5 = st.sidebar.button("DESSERT WINE")
button6 = st.sidebar.button("SPARKLING WINE")


if any([button1, button2, button3, button4, button5, button6]):
    welcome_title.empty()
    image_placeholder.empty()
    caption_placeholder.empty()

    if button1:
        st.title("Red Wine Information")
    elif button2:
        st.title("White Wine Information")
    elif button3:
        st.title("Rosé Wine Information")
    elif button4:
        st.title("Amber Wine Information")
    elif button5:
        st.title("Dessert Wine Information")
    elif button6:
        st.title("Sparkling Wine Information")
        st.write("Ops")
        
