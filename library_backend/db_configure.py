import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # Default WAMP password is empty
        database="library_management"
    )
    return connection
