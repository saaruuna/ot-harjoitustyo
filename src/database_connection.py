import sqlite3

connection = sqlite3.connect("labs.db")
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
