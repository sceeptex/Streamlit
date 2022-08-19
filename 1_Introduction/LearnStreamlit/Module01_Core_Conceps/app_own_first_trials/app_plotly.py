import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px


def main():
    st.title('Hello Streamlit lovers')
    df = pd.read_csv('data\prog_languages_data.csv')
    st.dataframe(df)

    fig = px.pie(df, values='Sum', names='lang', title='Pie chart of languages')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()