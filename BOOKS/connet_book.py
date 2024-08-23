import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('books.csv')

st.header('로맨스 소설')
st.dataframe(data=df, width=1000, height=1000)

