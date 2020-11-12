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
    create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_users_table)
    create_items_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
    cursor.execute(create_items_table)
    _end_connection(connection)

def create_user(username,password):
    print('Username -> {} and password {}'.format(username,password))
    connection , cursor = _create_connection()
    add_user = "INSERT INTO users VALUES (NULL , ? , ?)"
    cursor.execute(add_user ,(username, password,))
    _end_connection(connection)

def check_for_user(username):
    print('Username --------> {}'.format(username))
    connection , cursor = _create_connection()
    check_user = "SELECT * FROM users WHERE username=?"
    result = cursor.execute(check_user,(username,))
    row = result.fetchone()
    _end_connection(connection)
    return row

def check_for_id(user_id):
    connection , cursor = _create_connection()
    check_user = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(check_user,(user_id,))
    row = result.fetchone()
    _end_connection(connection)
    return row

def check_for_item(name):
    connection , cursor = _create_connection()
    check_item = "SELECT * from items WHERE name=?"
    result = cursor.execute(check_item,(name,))
    row = result.fetchone()
    _end_connection(connection)
    if row:
        return row[0] , row[1]
    return None

def create_item(name,price):
    try:
        connection , cursor = _create_connection()
        create_item = "INSERT INTO items VALUES (?,?)"
        cursor.execute(create_item,(name,price))
        _end_connection(connection)
        return True
    except:
        return False

def get_all_items():
    try:
        connection , cursor = _create_connection()
        get_all_items = "SELECT * FROM items"
        result = cursor.execute(get_all_items)
        items = []
        while True:
            item = result.fetchone()
            if item:
                items.append({'name': item[0],'price': item[1]})
            else:
                break
        return {'items': items}
    except:
        return None

def update_item(item):
    try:
        connection , cursor = _create_connection()
        delete_item = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(delete_item,(item['price'],item['name']))
        _end_connection(connection)
        return True
    except:
        return False
def delete_item(name):
    try:
        connection , cursor = _create_connection()
        delete_item = "DELETE FROM items WHERE name=?"
        cursor.execute(delete_item , (name,))
        _end_connection(connection)
        return True
    except:
        return False