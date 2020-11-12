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

        item = sql_helper.check_for_user(username)
        if item:
            user = cls(*item)
        else:
            user = None
        return user
    @classmethod
    def find_by_id(cls,_id):

        item = sql_helper.check_for_id(_id)
        user = cls(*item)
        return user