from re import L
import streamlit as st
import pandas as pd
import numpy as np

# static
import matplotlib.pyplot as plt
import seaborn as sns

st.header('matplotlib and seabon')
df = pd.read_csv('./tips.csv')
st.dataframe(df.head())

st.markdown('---')

with st.container():
    st.write('1. 남성과 여성의 분포 수를 찾기')
    value_counts = df['sex'].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Pie Chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct='%0.2f%%',labels=['Male','Female'])
        st.pyplot(fig)
    with col2:
        st.subheader('Bar Chart')
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)