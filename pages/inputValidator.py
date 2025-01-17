import streamlit as st

def validateString(input_string):
    if not (input_string.strip() or input_string==""):
        st.error("The text input is empty. Please enter some text.")