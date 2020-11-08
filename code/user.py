import sqlite3
import sql_helper
from flask_restful import Resource , reqparse
from flask import request

class User(object):

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    # This function accepts the username and find the row with the username value
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(select_query , (username ,))
        row = result.fetchone()
        # We need to return an User object
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    @classmethod
    def find_by_id(cls,_id):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM users where id=?"
        result = cursor.execute(select_query , (_id ,))
        row = result.fetchone()
        
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='This field cannot be blank')
    parser.add_argument('password',type=str,required=True,help='This field cannot be blank')

    def post(self):    
        if request.is_json:
            data = UserRegister.parser.parse_args() #request.get_json()
            username = data['username']
            if sql_helper.check_for_user(username):
                return {'Message': 'User with username [{}] Already exists'.format(username)},400
            password = data['password']
            sql_helper.create_user(username , password)
            return {'Message': 'User create successfully'},201
        else:
            return {'Message': 'Request was not of type JSON'},400