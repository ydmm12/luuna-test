from views.usersView import UserView
import jwt
import datetime

SECRET = 'Luuna-secret-key'

def getUsersMail(user_id):
    users = UserView.query.filter(UserView.id != int(user_id)).all()
    return [user.email for user in users]

def get_users():
    return [user.to_json() for user in UserView.query.all()]

def get_user(user_id):
    user = UserView.query.filter_by(id=user_id).first()
    return user.to_json()

def create_user(user):
    userView = UserView(
        username = user["username"],
        email = user["email"],
        password = user["password"]
    )
    return userView

def modify_user(user_id, data):
    user = UserView.query.filter_by(id=user_id).first()
    for field in data:
        if getattr(user, field) != data[field]:
            setattr(user, field, data[field])
    return user

def delete_user(user_id):
    try:
        UserView.query.filter_by(id=user_id).delete()
        return user_id
    except:
        return "Error in ID"

def authenticateUser(user_data):
    user = UserView.query.filter_by(email=user_data['email']).first()
    if user:
        if user_data['password'] == user.password:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
            }
            return jwt.encode(
                payload,
                SECRET,
                algorithm='HS256'
            )
        else:
            return "Error in password"
    else:
        return "Error in email"

def decode_auth_token(auth_header):
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(auth_token, SECRET, algorithms=['HS256'])
            response = payload['sub']
        except jwt.ExpiredSignatureError:
            response = 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            response = 'Invalid token. Please log in again.'
    else:
        response = "Unauthorized"
    return response
