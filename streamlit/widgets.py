import streamlit as st
import pandas as pd
import numpy as np

st.title("Widgets")

name = st.text_input("Enter Your Name:")
st.write(f"Hello, {name}")
age = st.slider("Select your age", 0, 100)
st.write(f"Your age is {age}")

options = ["Python", "Swift", "JavaScript", "C++"]
select = st.selectbox("Choose your favorite language", options)
st.write(f"Your Favorite Language is {select}")

data = {
    "Name": ["Peter Parker", "Tony Stark", "Steve Rogers"],
    "Alias": ["Spider Man", "Iron Man", "Captain America"],
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
st.write(df)


uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write(uploaded_df)
