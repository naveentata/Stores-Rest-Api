import sqlite3
from flask_restful import Resource,Api,reqparse
from models.Users import UsersModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='User name is required')
    parser.add_argument('password',type=str,required=True,help='Password is required')

    def post(self):
        data = UserRegister.parser.parse_args()

        if(UsersModel.find_by_username(data['username']) != None):
            return({"message": "Sorry user already exists"})
        
        user = UsersModel(**data)
        user.save_to_db()
        return({"message":"User has been sucessfully created"})



