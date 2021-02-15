from views.usersView import UserView
from services.database import getDB

DB = getDB()

def get_users():
    return DB.query(UserView).all()

def get_user(user_id):
    user = DB.query(UserView).filter_by(id=user_id).first()
    return user.to_json()

def create_user(user):
    userView = UserView()
    DB.query(UserView).name = user["username"]
    DB.query(UserView).name = user["email"]
    DB.add(userView)
    DB.commit()

def modify_user(user_id, user):
    user["id"]= user_id
    return user

def delete_user(user_id):
    try:
        return DB.query(UserView).filter_by(id=user_id).delete()
    except:
        return "Error in ID"