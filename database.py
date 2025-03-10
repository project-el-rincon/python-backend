from mysql.connector import Error

import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='192.168.211.155',
            user='home_data',
            password='vBujy@vvXjOVCcuD',
            database='home_data'
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

# # Example usage
# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         close_connection(conn)