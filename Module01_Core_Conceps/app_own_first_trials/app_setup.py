import streamlit as st

PAGE_CONFIG = {"page_icon":'😋'}

st.set_page_config(page_title='Dashboard streamlit', 
page_icon='😋', 
layout='wide', # centered
initial_sidebar_state='collapsed',

# initial_sidebar_state='expanded' # auto
)

def main():
    st.title('Hello Streamlit lovers')

    st.sidebar.success('Menu')

if __name__ == '__main__':
    main()