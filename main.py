import streamlit as st

st.set_page_config(layout="wide")
col_1, col_2 = st.columns(2)

with col_1:
    st.image("./images/pic1.png", width=400)

with col_2:
    st.title("Kevin Hui")
    content = """
    Hello and welcome to my webpage!
    My name is Kevin Hui, I am an IT Technician and graduate from 
    University of Massachusetts Boston.
    I have experience with IT troubleshooting and programming language 
    such as Python, HTML, and Javascript.
    """
    st.write(content)