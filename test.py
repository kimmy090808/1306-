import streamlit as st

col1, col2 = st.columns([2,3])

with col1:
    st.title("here is colunm1")
with col2:
    st.title("here is colunm2")
    st.checkbox("this is a checkbox in colunm2")

col1.subheader("I am a subheader!!")
col2.checkbox("this is checkbox in colunm2")
#