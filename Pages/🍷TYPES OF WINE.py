import streamlit as st

# Add custom CSS to style the buttons
st.markdown("""
<style>
.sidebar .widget>div>div>div>button {
    width: 100%; /* Set a fixed width for the buttons */
    padding: 8px; /* Add padding for better appearance */
}
</style>
""", unsafe_allow_html=True)

button1 = st.sidebar.button("RED WINE")
button2 = st.sidebar.button("WHITE WINE")
button3 = st.sidebar.button("ROSE WINE")
button4 = st.sidebar.button("AMBER WINE")
button5 = st.sidebar.button("DESSERT WINE")
button6 = st.sidebar.button("SPARKLING WINE")

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
