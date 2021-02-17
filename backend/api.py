from flask import Flask, request
from flask.views import MethodView
from flask_restful import Api
from services.database import getUrl
from views.masterDB import db
from controllers.productsController import *
from controllers.usersController import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = getUrl()
db.init_app(app)
db.app = app
db.create_all()


class Users(MethodView):
    def get(self, user_id):
        try:
            if user_id:
                response = get_user(user_id)
            else:
                response = get_users()
            return {
                "result": response
            }
        except:
            return {
                "Error": "Doesn't exist"
            }
    def post(self):
        try:
            response = decode_auth_token(request.headers.get('Authorization'))
            if type(response) is not str:
                user = create_user(request.get_json())
                db.session.add(user)
                db.session.commit()
                return {
                    "result": user.to_json()
                }
            else:
                return {
                    "Error": response
                }
        except:
            return {
                "Error": "Data error"
            }
    def put(self, user_id):
        try:
            response = decode_auth_token(request.headers.get('Authorization'))
            if type(response) is not str:
                user = modify_user(user_id, request.get_json())
                if user:
                    db.session.commit()
                    return {
                        "result": user.to_json()
                    }
                else:
                    return {
                        "Error": "User doesn't exist"
                    }
            else:
                return {
                    "Error": response
                }
        except:
            return {
                "Error": "Data error"
            }
    def delete(self, user_id):
        response = decode_auth_token(request.headers.get('Authorization'))
        if type(response) is not str:
            result = delete_user(user_id)
            db.session.commit()
            return {
                "result": result
            }
        else:
            return {
                "Error": response
            }

class LoginAPI(MethodView):
    def post(self):
        response = authenticateUser(request.get_json())
        db.session.commit()
        return {
            "result": response
        }

class Products(MethodView):
    def get(self, product_id):
        try:
            if product_id:
                response = get_product(product_id)
            else:
                response = get_products()
            db.session.commit()
            return {
                "result": response
            }
        except:
            return {
                "Error": "Doesn't exist"
            }
    def post(self):
        try:
            response = decode_auth_token(request.headers.get('Authorization'))
            if type(response) is not str:
                product = create_product(request.get_json())
                db.session.add(product)
                db.session.commit()
                return {
                    "result": product.to_json()
                }
            else:
                return {
                    "Error": response
                }
        except:
            return {
                "Error": "Data error"
            }
    def put(self, product_id):
        try:
            response = decode_auth_token(request.headers.get('Authorization'))
            if type(response) is not str:
                product = modify_product(product_id, request.get_json(), response)
                if product:
                    db.session.commit()
                    return {
                        "result": product.to_json()
                    }
                else:
                    return {
                        "Error": "Product doesn't exist"
                    }
            else:
                return {
                    "Error": response
                }
        except:
            return {
                "Error": "Data error"
            }
    def delete(self, product_id):
        response = decode_auth_token(request.headers.get('Authorization'))
        if type(response) is not str:
            result = delete_product(product_id)
            db.session.commit()
            return {
                "result": result
            }
        else:
            return {
                "Error": response
            }

user_view = Users.as_view('users')
app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

user_auth_view = LoginAPI.as_view('login')
app.add_url_rule('/login/', view_func=user_auth_view, methods=['POST'])

product_view = Products.as_view('products')
app.add_url_rule('/products/', defaults={'product_id': None}, view_func=product_view, methods=['GET'])
app.add_url_rule('/products/', view_func=product_view, methods=['POST'])
app.add_url_rule('/products/<int:product_id>', view_func=product_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)