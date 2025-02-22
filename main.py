import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input from the user
user_input = st.text_input("Enter some text:")

# Simple Display of the input text
if st.button("Submit"):
    st.write("You entered:", user_input)

# Additional features
st.sidebar.header("Options")
number = st.sidebar.number_input("Select a number", 0, 100)

if st.sidebar.button("Show square"):
    st.write("Square of", number, "is", number ** 2)

# Adding a chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 100, size=10)
})

# Line chart
st.line_chart(data.set_index('x'))

# Bar chart
st.bar_chart(data.set_index('x'))
