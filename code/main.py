from flask import Flask , request
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate, identity
import sql_helper
from user import UserRegister
app = Flask(__name__)
api = Api(app)
app.secret_key = 'abcd'
jwt = JWT(app , authenticate , identity)


items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be blank!'
    )
    

    @jwt_required()
    def get(self , name):

        item = next(filter(lambda item: item['name'] == name ,items), None)
        return {'item': item} , 200 if item else 400
    
    def post(self,name):

        if next(filter(lambda item: item['name'] == name ,items), None):
            return {'Message': 'Item with the following name [{}] exists'.format(name)} , 400
        
        if request.is_json:
            data = Item.parser.parse_args()
        else:
            return {'Message': 'Body must be JSON'}
        item = { 'name': name, 'price': data['price'] }
        items.append(item)
        return item,201

    def delete(self , name):
        global items
        for item in items:
            if name == item['name']:
                items.remove(item)
                return {'Message': 'Item Removed'}, 200
        return {'Message': 'Item with the name [{}] was not found'.format(name)}, 404

    def put(self, name):
        
        if request.is_json:
            data = Item.parser.parse_args()
            
        else:
            return {'Message': 'Required type is JSON'}
        
        item = next(filter(lambda x: x['name'] == name,items),None)
        print('This is the value of mem location of ITEM {}',format(hex(id(item))))
        print('This is the value of mem location of ITEMS {} '.format(hex(id(items[0]))))
        if item:
            item.update(data)
        else:
            data = {'name': name, 'price': data['price']}
            items.append(data)
        return item if item else data, 200 if item else 201 

class ItemList(Resource):
    def get(self):
        return { 'items': items}

sql_helper.create_table()
api.add_resource(Item , '/item/<string:name>')
api.add_resource(ItemList , '/items')
api.add_resource(UserRegister,'/register')
# if __name__ == '__main__':
#     print('Lets see \n\n\n\n\n ')
#     sql_helper.create_table()
#     app.run()