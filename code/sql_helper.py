import sqlite3

def _create_connection():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return connection , cursor

def _end_connection(connection):

    connection.commit()
    connection.close()

def create_table():
    connection , cursor = _create_connection()
    create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
    _end_connection(connection)

def create_user(username,password):
    connection , cursor = _create_connection()
    add_user = "INSERT INTO users VALUES (NULL , ? , ?)"
    cursor.execute(add_user ,(username, password,))
    _end_connection(connection)
