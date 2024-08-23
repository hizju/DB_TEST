import streamlit as st
import pandas as pd
import time

side_bar = st.sidebar

side_bar.header('Sidebar st.sidebar')

df = pd.read_csv('tips.csv')
columns = tuple(df.columns)
st.write(columns)

select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
)
side_bar.write("You selected the column_name = {}".format(select_column))

st.dataframe(df[[select_column]])

# Layout Columns
st.header('Columns-1')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('columns-1')
    st.image('./media/image.jpg')

with col2:
    st.subheader('columns-2')
    st.dataframe(df)

with col3:
    st.subheader('columns-3')
    st.dataframe(df[[select_column]])


# expander
st.header('Expander: st.expander')
with st.expander('Some explanation'):
    st.write("""
        Insert a multi-elemetn
             
        Insert a container into your app

""")