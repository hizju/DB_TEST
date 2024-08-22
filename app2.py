def connect_to_db():
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='9787',
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