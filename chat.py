import streamlit as st
a=st.chat_input("Enter your command:")
if a:
	st.chat_message("user").write(a)
	if a.lower()=="hi":
		st.chat_message("ai").write("hello")
	elif a.lower()=="bye":
		st.chat_message("ai").write("goodbye")
