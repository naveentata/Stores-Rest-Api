import os
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from resources.Users import UserRegister
from security import authenticate,identity
from resources.items import Item, ItemList
from resources.stores import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'naveen'
api = Api(app)



jwt = JWT(app,authenticate,identity)



api.add_resource(StoreList,"/stores")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(UserRegister,"/register")

if __name__ =="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True) 