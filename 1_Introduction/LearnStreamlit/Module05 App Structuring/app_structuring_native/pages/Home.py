import streamlit as st

# Sharing variables among pages
from app import my_variable, choice

st.header('Home page')
st.write(my_variable)
