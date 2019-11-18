from models.Users import UsersModel


def authenticate(username,password):
    user = UsersModel.find_by_username(username)
    if user and user.password == password:
        return user
def identity(payload):
    user_id = payload['identity']
    return UsersModel.find_by_id(user_id)