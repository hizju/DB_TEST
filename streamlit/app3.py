import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

st.header('st.datafram')
st.dataframe(data=df, width=1000, height=1000)

#st.static
st.header('st.table')
st.table(data=df.head(5))

#st.json
st.header('st.json')
json_values = df.head(3).to_dict()
st.json(json_values)