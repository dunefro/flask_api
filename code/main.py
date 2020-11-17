from flask import Flask 
from flask_restful import Api 
from flask_jwt import JWT
from security import authenticate, identity
from models import sql_helper
from resources.user import UserRegister
from resources.item import Item , ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)
app.secret_key = 'abcd'
jwt = JWT(app , authenticate , identity)

@app.before_first_request
def create_tables():
    db.create_all()

# sql_helper.create_table()
api.add_resource(Item , '/item/<string:name>')
api.add_resource(ItemList , '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store , '/store/<string:name>')
api.add_resource(StoreList , '/stores')
