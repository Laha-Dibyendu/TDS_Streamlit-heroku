import streamlit as st
string = "Sum of Two Numbers"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Sum two numbers')
x = st.number_input('Enter a number')
y = st.number_input('Enter another number')

st.write("The sum of the two given numbers is :", x+y)
