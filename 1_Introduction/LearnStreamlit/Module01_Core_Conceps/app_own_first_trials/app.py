import streamlit as st

def main():
    st.title('Hello')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.markdown('This is a Mardown')

    genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn't select comedy.")

    # Inform user
    st.success('Successful')
    st.warning('This is danger')
    st.info('This is an information')
    st.error('This is an error')
    st.exception('This is an exception')

    # Superfunction
    st.write('This is a test')
    st.write('## This is a test')
    st.write('This is a test', [1,2,3])

    # Help info
    st.help(range)
    # st.help(st.write)
    st.write(dir(st))

    


if __name__ == '__main__':
    main()