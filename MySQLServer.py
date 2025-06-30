import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (not a specific database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # 🔁 Change if your MySQL server has a password
    )

    # If connection is successful
    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Clean up database connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")
