import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col_1, col_2 = st.columns(2)
with col_1:
    st.image("./images/pic1.png", width=400)

with col_2:
    st.title("Kevin Hui")
    content = """
    Hello and welcome to my webpage!
    My name is Kevin Hui, I graduated in 2023 with a Bachelor in Science 
    in Information Technology, Summa Cum Laude, from University of Massachusetts Boston.
    I have experience with IT troubleshooting and programming language 
    such as Python, HTML, and Javascript.
    """
    st.write(content)

content_2 = """Below are some of the Python apps that I have made. 
Feel free to contact me!"""
st.write(content_2)

col_3, col_4 = st.columns(2)
df = pd.read_csv("data_2.csv", sep=",")

with col_3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col_4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
