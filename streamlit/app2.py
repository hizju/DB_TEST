import streamlit as st
import pandas as pd
import numpy as np

# st.write
st.write('Welcome to Streamlit App APIS')
st.write(1234)

df = pd.DataFrame({
    'first': [1,2,3,4,5],
    'second': [6,7,8,9,10]
})

st.write(df)

# display numpy array
st.write(np.array([1,2,3,4,5]))

st.write("Magic commands")
df1 = pd.DataFrame({'col':[1,2,3,4,5]})
df1

x = 10

x

###### title
st.title("This is Title")
st.caption('Using st.title() ')

#header
st.header('This is header')
st.caption('The text inside st.header()')

st.markdown('---')
st.subheader('Generate Random Numbers')
body = """

import numpy as np

def generate_random(size):
   rand = np.random.random(size=size)
   return rand
number = generate_random(10)
"""
st.code(body,language='python')

# Latex
st.subheader('Latex')
formula = """
 a + ar + ar^2 + ar^3 + \cdots + a r^{n-1} = \sum_{k=0}^{nb-1}a r^k
"""
st.latex(formula)