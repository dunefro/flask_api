from flask import Flask 
from flask_restful import Api 
from flask_jwt import JWT
from security import authenticate, identity
from models import sql_helper
from resources.user import UserRegister
from resources.item import Item , ItemList

app = Flask(__name__)
api = Api(app)
app.secret_key = 'abcd'
jwt = JWT(app , authenticate , identity)

sql_helper.create_table()
api.add_resource(Item , '/item/<string:name>')
api.add_resource(ItemList , '/items')
api.add_resource(UserRegister,'/register')
