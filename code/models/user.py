import sqlite3
from models import sql_helper
from db import db
class UserModel(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # This function accepts the username and find the row with the username value
    @classmethod
    def find_by_username(cls,username):

        user = cls.query.filter_by(username=username).first()
        # if item:
        #     user = cls(*item)
        # else:
        #     user = None
        return user
    @classmethod
    def find_by_id(cls,_id):

        # item = sql_helper.check_for_id(_id)
        user = cls.query.filter_by(id=_id)
        # user = cls(*item)
        return user

    def save_to_db(self):
        
        db.session.add(self)
        db.session.commit()