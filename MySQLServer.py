
import mysql.connector

def create_database():
    connection = None
    cursor = None

    try:
        # Connect to MySQL server (edit credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your MySQL password
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Cleanly close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()