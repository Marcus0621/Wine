import streamlit as st

button_style = """
    <style>
    .wine-button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
"""

st.sidebar.markdown(button_style, unsafe_allow_html=True)

button1 = st.sidebar.button("RED WINE", key="button1", help="Click for Red Wine")
button2 = st.sidebar.button("WHITE WINE", key="button2", help="Click for White Wine")
button3 = st.sidebar.button("ROSE WINE", key="button3", help="Click for Rosé Wine")
button4 = st.sidebar.button("AMBER WINE", key="button4", help="Click for Amber Wine")
button5 = st.sidebar.button("DESSERT WINE", key="button5", help="Click for Dessert Wine")
button6 = st.sidebar.button("SPARKLING WINE", key="button6", help="Click for Sparkling Wine")

if any([button1, button2, button3, button4, button5, button6]):
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

