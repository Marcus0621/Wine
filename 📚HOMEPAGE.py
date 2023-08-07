import streamlit as st
from PIL import Image

welcome_title = st.title("WELCOME TO THE WORLD OF WINE!")
first_image = Image.open('WineIntro.jpg')
image_placeholder = st.empty()
caption_placeholder = st.empty()
image_placeholder.image(first_image, caption='Image by 1Zoom', use_column_width=True)


    
        
