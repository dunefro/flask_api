from flask_restful import Resource , reqparse
from flask_jwt import jwt_required
from models import sql_helper
from flask import request
from models.item import ItemModel
from models.store import StoreModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be blank!'
    )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help='This field cannot be blank!'
    )
    

    @jwt_required()
    def get(self , name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json() , 200        
        return {'Message': 'Item with the following name doesn\'t [{}] exists'.format(name)} , 400
    
    def post(self,name):

        if request.is_json:
            item = ItemModel.find_by_name(name)
            if item:
                return {'Message': 'Item with the following name [{}] exists'.format(name)} , 400
            data = Item.parser.parse_args()
            if not StoreModel.find_by_id(data['store_id']):
                return {'Message': 'Store with the following ID [{}] doesn\'t exists'.format(data['store_id'])}
            item = ItemModel(name , **data)
            item.save_to_db()
            return item.json() , 201
        else:
            return {'Message': 'Body must be JSON'},400

    def delete(self , name):
        
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'Message': 'Item Removed'}, 200
        return {'Message': 'Item with the name [{}] was not found'.format(name)}, 404

    def put(self, name):
        
        if request.is_json:
            data = Item.parser.parse_args()
        else:
            return {'Message': 'Required type is JSON'}
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name , **data)
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json() , ItemModel.query.all()))}