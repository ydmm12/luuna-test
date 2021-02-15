from flask import Flask, request
from flask.views import MethodView
from flask_restful import Api
from controllers.usersController import *
from controllers.productsController import *

app = Flask(__name__)
api = Api(app)

class Users(MethodView):
    def get(self, user_id):
        if user_id:
            return get_user(user_id)
        else:
            return get_users()
    def post(self):
        return create_user(request.get_json())
    def put(self, user_id):
        return modify_user(user_id, request.get_json())
    def delete(self, user_id):
        return delete_user(user_id)

class Products(MethodView):
    def get(self, product_id):
        if product_id:
            return get_product(product_id)
        else:
            return get_products()
    def post(self):
        return create_product(request.get_json())
    def put(self, product_id):
        return modify_product(product_id, request.get_json())
    def delete(self, product_id):
        return delete_product(product_id)

user_view = Users.as_view('users')
app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

product_view = Products.as_view('products')
app.add_url_rule('/products/', defaults={'product_id': None}, view_func=product_view, methods=['GET',])
app.add_url_rule('/products/', view_func=product_view, methods=['POST'])
app.add_url_rule('/products/<int:product_id>', view_func=product_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)