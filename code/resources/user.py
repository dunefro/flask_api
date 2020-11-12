import sqlite3
from models import sql_helper
from flask_restful import Resource , reqparse
from flask import request


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