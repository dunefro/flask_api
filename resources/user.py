import sqlite3
from models import sql_helper
from models.user import UserModel
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
            if UserModel.find_by_username(username):
                return {'Message': 'User with username [{}] Already exists'.format(username)},400
            password = data['password']
            user = UserModel(username,password)
            user.save_to_db()
            return {'Message': 'User create successfully'},201
        else:
            return {'Message': 'Request was not of type JSON'},400