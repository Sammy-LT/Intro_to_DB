import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'  # 🔁 Replace this
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # ✅ No SELECT or SHOW used
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # ✅ Proper exception handling
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # ✅ Always close cursor and connection
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except:
            pass  # Safe exit even if something failed earlier

# Run the function
create_database()
