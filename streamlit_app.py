import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Load the CSV file to check its columns
file_path = 'peliculas.csv'
data = pd.read_csv(file_path)

# Display the columns in the file
st.write(data.columns.tolist())

# Group the data by 'Year' and count the number of movies per year
movie_counts_by_year = data.groupby('Year').size()

# Plotting the data
plt.figure(figsize=(12, 6))
movie_counts_by_year.plot(kind='bar', color='skyblue')
plt.title('Número de Películas por Año')
plt.xlabel('Año')
plt.ylabel('Número de Películas')
plt.grid(True)
plt.show()

st.pyplot(plt)

