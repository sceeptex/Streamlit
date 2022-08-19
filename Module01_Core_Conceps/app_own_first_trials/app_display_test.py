import streamlit as st

import pandas as pd

df = pd.read_csv('iris.csv')

# display df
st.dataframe(df, height=200, width=1000)

# highlight in df
st.dataframe(df.style.highlight_max(axis=0))

# static table
st.table(df)

st.write(df)


st.write(df.head(5))

st.json({'data':'name'})

mycode = """
def sayhello():
    print("hello")
"""

st.code(mycode, language='python')