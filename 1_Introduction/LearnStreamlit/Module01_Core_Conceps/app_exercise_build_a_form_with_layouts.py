# Core Pkgs
import streamlit as st 

# Exercise Build a simple form
def main():
	st.title("Layout in Streamlit")
	st.subheader("Exercise: Build A Simple Form")
	
	# Firstname,Lastname,Age
	# Message,Contact

col1,col2 = st.columns(2)


with col1:
	
	fname = st.text_input("Firstname")
	age = st.number_input("Age",1,100)
	message = st.text_area("Message")

# st.help(st.form)

with col2:
	with st.form(key ='key1',clear_on_submit = True):
		lname = st.text_input("name")
		dob = st.date_input("Date of Birth")
		message = st.text_input("Contact Address")
		
		# Every form must have a submit button.
		submitted_form1 = st.form_submit_button("Submit")
		
if submitted_form1:
	template = f"Your name is {lname} and you were born on {dob}. You said {message}"
	st.write(template)



	

if __name__ == '__main__':
	main()










































