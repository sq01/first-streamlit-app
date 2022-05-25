import pandas as pd
import streamlit as st

st.title("Hello World!")
st.header("Ein, zwei, drei")
st.text("ava")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])

fruit_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruit_to_show)
