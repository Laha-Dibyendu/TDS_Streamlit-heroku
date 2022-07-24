import streamlit as st
string = "Sum of Two Numbers"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Sum two numbers')
x = st.number_input('Enter a number')
y = st.number_input('Enter another number')
# if (x).is_integer() :
#     if x%2==0:st.write("your number is even")
#     elif x%2!=0:st.write("your number is odd")
# else:
#st.write("The sum of the two given numbers is :", x+y)
p=x+y
if (p).is_integer():
    st.write("The sum of the two given numbers is :", p)
else:
    st.write("The sum of the two given numbers is :"+round(p,2)+" (rounded off upto 2 decimals)")
