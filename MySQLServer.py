import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (not a specific database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # 🔁 Update if your MySQL has a password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")
