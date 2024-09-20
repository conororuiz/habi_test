import mysql.connector
from mysql.connector import Error
from settings_local import *

def get_db_connection():
    """
    Establishes a connection to the MySQL database.

    Returns:
        conn: Connection to the database.
    """
    try:
        conn = mysql.connector.connect(
            host=HOSTNAME,
            user=USER,
            password=PASSWORD,
            database=DATABASE_NAME,
            port=PORT
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
