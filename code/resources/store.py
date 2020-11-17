from flask_restful import Resource
from models.store import StoreModel
from flask import request

class Store(Resource):
    
    def get(self,name):

        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'Message': 'Store with the following name [{}] doesn\'t exist'.format(name)} , 400
    
    def post(self,name):

        store = StoreModel.find_by_name(name)
        if store:
            return {'Message': 'Store with the following name [{}] exists'.format(name)} , 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json() , 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'Message': 'Store removed'.format(name)} , 200
        return {'Message': 'Store with the following name [{}] doesn\'t exist'.format(name)} , 400

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

