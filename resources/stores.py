from flask_restful import Resource
from models.stores import StoreModel

class Store(Resource):
    
    
    def get(self,name):
        store = StoreModel.find_store_name(name)
        if store:
            return store.json()
        return {"message":"store not found"},404
    def post(self,name):
        store = StoreModel.find_store_name(name)
        if store:
            return {"message":"Store Already exists"},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"error occured while saving"},500
        return store.json(),201    

    def delete(self,name):
        store = StoreModel.find_store_name(name)
        if store:
            store.delete_from_db()
        return({'message':'store has been deleted'})

class StoreList(Resource):
    def get(self):
       return {'store': [store.json() for store in StoreModel.query.all()]}