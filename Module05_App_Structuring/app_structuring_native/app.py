import streamlit as st

my_variable = "variable from Main app page"

from pages.eda import my_calc

def main():
    st.title("Streamlit Multi-Page app")
    st.subheader("Main page")
    st.write(my_variable)
    st.write(my_calc)
    st.write(my_calc)

    choice = st.sidebar.selectbox("Submenu",["Pandas", "Tensorflow"])
    if choice == "Pandas":
        st.subheader(choice)

if __name__ == '__main__':
    main()
    