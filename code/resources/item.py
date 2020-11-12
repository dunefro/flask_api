from flask_restful import Resource , reqparse
from flask_jwt import jwt_required
from models import sql_helper
from flask import request

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be blank!'
    )
    

    @jwt_required()
    def get(self , name):
        item = sql_helper.check_for_item(name)
        if item:
            return {'name': item[0] , 'price': item[1]} , 200        
        return {'Message': 'Item with the following name doesn\'t [{}] exists'.format(name)} , 400
    
    def post(self,name):

        if request.is_json:
            if sql_helper.check_for_item(name):
                return {'Message': 'Item with the following name [{}] exists'.format(name)} , 400
            data = Item.parser.parse_args()
            if sql_helper.create_item(name,data['price']):
                return {'name': name,'price': data['price']},201
            else:
                return {'Message': 'Item with the following name [{}] can\'t be created'.format(name)},500
        else:
            return {'Message': 'Body must be JSON'},400

    def delete(self , name):
        
        item = sql_helper.check_for_item(name)
        if item:
            if sql_helper.delete_item(name):
                return {'Message': 'Item Removed'}, 200
            else:
                return {'Message': 'Item with the following name [{}] can\'t be deleted'.format(name)},500
        return {'Message': 'Item with the name [{}] was not found'.format(name)}, 404

    def put(self, name):
        
        if request.is_json:
            data = Item.parser.parse_args()
        else:
            return {'Message': 'Required type is JSON'}
        item = {'name': name , 'price': data['price']}
        if sql_helper.check_for_item(name):
            if sql_helper.update_item(item):
                return item,201
            else:
                {'Message': 'Item with the following name [{}] can\'t be updated'.format(name)},500
        else:
            if sql_helper.create_item(item['name'],item['price']):
                return {'name': item['name'], 'price': item['price']}, 201
            else:
                return {'Message': 'Item with the following name [{}] can\'t be created'.format(name)},500

class ItemList(Resource):
    def get(self):
        return sql_helper.get_all_items()