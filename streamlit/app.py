import streamlit as st
import pandas as pd
import numpy as np

# title of the webpage

st.title("This is title")

# writing in the webpage

st.write("Hello world")

df = pd.DataFrame(
    {"first Column": [10, 20, 30, 40, 50], "Second Column": [1, 2, 3, 4, 5]}
)

st.write(df)


# displaying line chart

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
