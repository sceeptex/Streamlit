import streamlit as st  

# Fxn
MIRROR_LOOKUP = {'a':'ɐ','b':'q','c':'ɔ','d':'p', 'e':'ǝ','f':'ɟ','g':'ɓ','h':'ɥ', 'i':'ᴉ','j':'ſ','k':'ʞ','l':'ן', 'm':'ɯ','n':'u','o':'o','p':'d', 'q':'b','r':'ɹ','s':'s','t':'ʇ', 'u':'n','v':'ʌ','w':'ʍ','x':'x', 'y':'ʎ','z':'z', 'A':'ꓯ','B':'ꓭ','C':'Ↄ','D':'ꓷ', 'E':'Ǝ','F':'Ⅎ','G':'⅁','H':'Η', 'I':'I','J':'ᒋ','K':'ꓘ','L':'⅂', 'M':'W','N':'N','O':'O','P':'ꓒ', 'Q':'Ò','R':'ꓤ','S':'S','T':'ꓕ', 'U':'ꓵ','V':'ꓥ','W':'M','X':'X', 'Y':'⅄','Z':'Z', '0':'0','1':'Ɩ','2':'ᘔ','3':'Ɛ', '4':'Һ','5':'૬','6':'9','7':'ㄥ', '8':'8','9':'6', '!':'¡','"':',,','#':'#','$':'$', '%':'%','&':'⅋','`':',','(':')', ')':'(','*':'*','+':'+',',':'"', '-':'-','.':'˙','/':'\\',':':':', ';':';','<':'>','=':'=','>':'<', '?':'¿','@':'@','[':']','\\':'/', ']':'[','^':'^','_':'‾','`':',', '{':'}','|':'|','}':'{','~':'~', ' ':' ', }
INVERSE_MIRROR_LOOKUP = {'ɐ': 'a', 'q': 'b', 'ɔ': 'c', 'p': 'd', 'ǝ': 'e', 'ɟ': 'f', 'ɓ': 'g', 'ɥ': 'h', 'ᴉ': 'i', 'ſ': 'j', 'ʞ': 'k', 'ן': 'l', 'ɯ': 'm', 'u': 'n', 'o': 'o', 'd': 'p', 'b': 'q', 'ɹ': 'r', 's': 's', 'ʇ': 't', 'n': 'u', 'ʌ': 'v', 'ʍ': 'w', 'x': 'x', 'ʎ': 'y', 'z': 'z', 'ꓯ': 'A', 'ꓭ': 'B', 'Ↄ': 'C', 'ꓷ': 'D', 'Ǝ': 'E', 'Ⅎ': 'F', '⅁': 'G', 'Η': 'H', 'I': 'I', 'ᒋ': 'J', 'ꓘ': 'K', '⅂': 'L', 'W': 'M', 'N': 'N', 'O': 'O', 'ꓒ': 'P', 'Ò': 'Q', 'ꓤ': 'R', 'S': 'S', 'ꓕ': 'T', 'ꓵ': 'U', 'ꓥ': 'V', 'M': 'W', 'X': 'X', '⅄': 'Y', 'Z': 'Z', '0': '0', 'Ɩ': '1', 'ᘔ': '2', 'Ɛ': '3', 'Һ': '4', '૬': '5', '9': '6', 'ㄥ': '7', '8': '8', '6': '9', '¡': '!', ',,': '"', '#': '#', '$': '$', '%': '%', '⅋': '&', ',': '`', ')': '(', '(': ')', '*': '*', '+': '+', '"': ',', '-': '-', '˙': '.', '\\': '/', ':': ':', ';': ';', '>': '<', '=': '=', '<': '>', '¿': '?', '@': '@', ']': '[', '/': '\\', '[': ']', '^': '^', '‾': '_', '}': '{', '|': '|', '{': '}', '~': '~', ' ': ' '}
# lookup and replace
def upsidedown_encoder(term):
	result = "".join([MIRROR_LOOKUP.get(i,i) for i in list(term)])
	return result

def upsidedown_decoder(term):
	result = "".join([INVERSE_MIRROR_LOOKUP.get(i,i) for i in list(term)])
	return result


def main():
	st.title("Mirror-Your-Text App")
	st.subheader("Hello Streamlit")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		# Form
		with st.form(key="myform"):
			raw_text = st.text_area("Enter Text Here")
			task_choice = st.selectbox("Tasks",["upsidedown","reverse"])
			c1,c2 = st.columns(2)
			encode_button = c1.form_submit_button(label="Encode")
			decode_button = c2.form_submit_button(label="Decode")
	
		if encode_button:
			col1,col2 = st.columns(2)

			with col1:
				st.info("Original Text")
				st.write(raw_text)

			with col2:
				st.success("Results")
				if task_choice == "upsidedown":
					result = upsidedown_encoder(raw_text)
				elif task_choice == "reverse":
					result = str(raw_text)[::-1]
				st.code(result)

		if decode_button:
			col1,col2 = st.columns(2)

			with col1:
				st.info("Original Text")
				st.write(raw_text)

			with col2:
				st.success("Results")
				if task_choice == "upsidedown":
					result = upsidedown_decoder(raw_text)
				elif task_choice == "reverse":
					result = str(raw_text)[::-1]
				st.code(result)

	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


