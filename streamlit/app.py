
import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_db():
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='1234',
            db='sakila',
            charset='utf8')
        return conn
    except pymysql.Connect.Error as err:
        st.error(f"Error: {err}")
        return None

def fetch_movies():
    conn = connect_to_db()

    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT film_id, title, release_year FROM film LIMIT 20;")
        movies = cursor.fetchall()
        cursor.close()
        conn.close()
        return movies
    return []

def fetch_movie(title):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        SQL = "SELECT film_id, title, release_year FROM film WHERE title = '" + title + "';"
        cursor.execute(SQL)
        rows = cursor.fetchall()
        #print(rows)
        return rows 

def fetch_movie_details(film_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, description, release_year, length, rating
            FROM film WHERE film_id = %s;
            """,(film_id))
        movie_detail = cursor.fetchone()
        cursor.close()
        conn.close()
        return movie_detail
    return None       
def update_movie(film_id, title, description):
    conn = connect_to_db();

    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE film SET title = %s, description = %s 
        WHERE film_id =  %s;
        """, (title, description, film_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False



#Streamlit App
st.title("Sakila Movie Database Management")

# Main menu
menu = ["View Movies","Search Movie","View Movie Details","Update Movie"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Movies":
    st.subheader("View Movie List")
    movies = fetch_movies()
    if movies:
        for movie in movies:
            st.write(f"ID:{movie[0]},Title:{movie[1]},Year:{movie[2]}")
    else:
        st.write("No movies found.")
elif choice == "Search Movie":
    st.subheader("Search for a Movie")
    title = st.text_input("Enter movie title")
    if st.button("Search"):
        movies = fetch_movie(title)
        if movies:
            for movie in movies:
                st.write(f"ID:{movie[0]},  Title:{movie[1]}, Year:{movie[2]}")
        else:
            st.write("No movies found.")

elif choice == "View Movie Details":
    st.subheader("View Movie Details")
    film_id = st.text_input("Enter movie ID")
    if st.button("Get Details"):
        details = fetch_movie_details(film_id)
        if details:
            st.write(f"Title: {details[0]}")
            st.write(f"Description: {details[1]}")
            st.write(f"Release Year: {details[2]}")
            st.write(f"Length: {details[3]} minutes")
            st.write(f"Rating: {details[4]}")
        else:
            st.write("Movie not found")

elif choice == "Update Movie":
    st.subheader("Update Movie")
    film_id = st.text_input("Enter movie ID")
    title = st.text_input("Enter new title")
    description = st.text_area("Enter new description")
    if st.button("Update Movie"):
        if update_movie(film_id,title,description):
            st.success("Movie update successfully")
    else:
        st.error("Failed to update movie.")
    

