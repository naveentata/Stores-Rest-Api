from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
import sqlite3
from models.items import ItemModel 


class Item(Resource):
    @jwt_required()
    def get(self,name):
        # parser = reqparse.RequestParser()
        # parser.add_argument('name',type=str,required=True,help="Name is required")
        # parser.add_argument('price',type=float,required=True,help="Price is required")
        item = ItemModel.find_item_name(name)

        if item :
            return item.json()
        return({'message':"Item not found"},404)
    

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("price",required=True,type=float,help="This is empty!!")
        parser.add_argument("store_id",required=True,type=float,help="This is empty!!")
        data = parser.parse_args()
        item = ItemModel.find_item_name(name)
        if(item):
            return{'message':"Already exists"}
        item = ItemModel(name,**data) # same as data['price'], data['store_id']
        item.save_to_db()
        return (item.json())
    
    

    def delete(self,name):
        item = ItemModel.find_item_name(name)
        if(item):
            item.delete_from_db()
        return({"message":"Item delted"})
    
    def put(self,name):
        item = ItemModel.find_item_name(name)
        parser = reqparse.RequestParser()
        parser.add_argument('price',type=float,required=True,help="Price is needed")
        parser.add_argument("store_id",required=True,type=float,help="storeid is empty!!")

        data = parser.parse_args()
        up_item = ItemModel(name,**data)
        if item == None:
            
            # item = {"name":name,"price":data["price"]}
            up_item.save_to_db()
            
        else:
            
            up_item.save_to_db()
        return (up_item.json())
    
class ItemList(Resource):
    def get(self):
        return({'items': [item.json()  for item in ItemModel.query.all()]})