import streamlit as st
import time

### progress
st.header('st.progress')
st.caption("Display a progress bar")

# my_bar = st.progress(0)
# for pct_complete in range(1,101):
#     time.sleep(0.01)
#     my_bar.progress(pct_complete)


def progress_bar():
    for pct_complete in range(1,101):
        time.sleep(0.07)
        pct_complete = min(pct_complete,100)
        my_bar.progress(pct_complete)

### spinner
# with st.spinner("Something is processing..."):
#     my_bar = st.progress(0)
#     progress_bar()

# info
st.subheader('st.info')
st.info('This is information message')

st.subheader('st.success')
st.success('This is success message')

st.subheader('st.warning')
st.warning('This is warning message')

st.subheader('st.error')
st.warning('This is error message')

time.sleep(1)
st.balloons()