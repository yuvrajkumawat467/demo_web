import streamlit as st
st.title("Yes you can do it!")
st.header("you can improve your skills")
st.subheader("...UV...")

name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father name:")
address = st.text_input("Enter your text:")
classdata = st.selectbox("Enter your class:",["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th"])

button = st.button("Submit")

if button:
    st.markdown(f"""
    Name: {name}
    Father Name: {fname}
    Address: {address}
    Class: {classdata}
    """)

 
