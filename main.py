import streamlit as st
st.title("Yes you can do it!")
st.header("you can improve your skills")
st.subheader("...UV...")

name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father name:")
address = st.text_input("Enter your text:")
class_ = st.text_input("Enter your class:")

button = st.button("Submit")

if button:
    st.markdown(f"""
    Name: {name}
    Father Name: {fname}
    Address: {address}
    Class: {class_}
    """)

 
