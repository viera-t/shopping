import mysql.connector

DATABASE_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'shopping',
}

db_connection = mysql.connector.connect(**DATABASE_CONFIG)
db_cursor = db_connection.cursor()