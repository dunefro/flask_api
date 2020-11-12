import sqlite3
from models import sql_helper

class User(object):
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    # This function accepts the username and find the row with the username value
    @classmethod
    def find_by_username(cls,username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # select_query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(select_query , (username ,))
        # row = result.fetchone()
        # # We need to return an User object
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        item = sql_helper.check_for_user(username)
        if item:
            user = cls(*item)
        else:
            user = None
        return user
    @classmethod
    def find_by_id(cls,_id):

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # select_query = "SELECT * FROM users where id=?"
        # result = cursor.execute(select_query , (_id ,))
        # row = result.fetchone()
        
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        item = sql_helper.check_for_id(_id)
        user = cls(*item)
        return user