import pandas as pd
import streamlit as st

st.title("Hello World!")
st.header("Ein, zwei, drei")
st.text("ava")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))
st.dataframe(my_fruit_list)
