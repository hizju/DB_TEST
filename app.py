from shutil import move
import streamlit as st 
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_db():
    try:
        conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user='root',
        passwd='9787',
        db='sakila',
        charset='utf8')
        return conn
    except pymysql.Connect.Error as error:
        st.error(f"Error: {error}")
        return None
        
def fetch_food():
    conn = connect_to_db()
    
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FILM LIMIT 20;")
        movies = cursor.fetchall()
        cursor.close()
        conn.close()
        return movies
    return []
        
# Streamlit App
st.title("♥ hiz House ♥")

# Menu menu
menu = ["희주네 메뉴판 >_<", "음식 찾기"]

choice = st.sidebar.selectbox("Menu",  menu)
print(choice)

print(type(choice))

if choice == "희주네 메뉴판 >_<":
    st.subheader("음식 메뉴")
    foods = fetch_food()
    if foods:
        for food in foods:
            st.write(food)
    else: 
        st.write("no food in here")
elif choice == "음식 찾기":
    st.subheader("음식이 없당 ㅠ.ㅠ")
    foods = fetch_food()
    if foods:
        for food in foods:
            st.write(food)
    else: 
        st.write("no food in here")