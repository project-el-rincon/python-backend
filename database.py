from typing import Optional
from mysql.connector import Error, MySQLConnection
from mysql.connector.types import RowType

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

def execute_select_query(connection: MySQLConnection, query: str) -> Optional[Error] | Optional[list[RowType]]:
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Query executed successfully")
        return cursor.fetchall()
    except Error as e:
        print(f"Error: '{e}'")
        return e

def execute_command_with_write(connection: MySQLConnection, query: str) -> Optional[Error]:
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return None
    except Error as e:
        print(f"Error: '{e}'")
        return e
# # Example usage
# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         close_connection(conn)