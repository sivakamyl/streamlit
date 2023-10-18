import streamlit as st

# To run "streamlit run streamlit_app.py" in Terminal

st.write('Hello world!')
st.write('Hello, *World!* :sunglasses:')
st.header('This is a header')
st.write(1234)
st.write('Let\'s learn :books:')

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')