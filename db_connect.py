import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Soujanya_1009",
            database="expense_tracker"
        )
        return conn
    except Error as e:
        print("Error connecting to database:", e)
        return None
