import streamlit as st

name = "Tobias"
if st.button('Submit'):
    st.write("Name: {}".format(name.upper()))

if st.button('Submit', key='button2'):
    st.write("Name: {}".format(name.lower()))

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")


option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)



if st.checkbox('How would you like to be contacted?',):
    st.success('Active')

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)


age = st.slider("Age",1,100)

color = st.select_slider("Choose Color", options=['red', 'blue', 'green', 'white'], value=['red','blue'])
