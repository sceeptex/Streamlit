import streamlit as st



fname = st.text_input("Enter Firstname", max_chars=30)
st.title(fname)

fname_area = st.text_area("Enter Address", height = 300)
st.write(fname_area)

number = st.number_input('Enter the number')