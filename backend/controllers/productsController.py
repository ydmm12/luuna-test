from views.productsView import ProductView
from services.notifications import send_message

def get_products():
    return [product.to_json() for product in ProductView.query.all()]

def get_product(product_id):
    product = ProductView.query.filter_by(id=product_id).first()
    product.views +=1
    return product.to_json()

def create_product(product):
    productView = ProductView(
        sku = product["sku"],
        name = product["name"],
        brand = product["brand"],
        price = product["price"],
        views = 0
    )
    return productView

def modify_product(product_id, data, user_id):
    changes = {}
    product = ProductView.query.filter_by(id=product_id).first()
    for field in data:
        if getattr(product, field) != data[field]:
            setattr(product, field, data[field])
            changes[field] = data[field]
    send_message(changes, user_id)
    return product

def delete_product(product_id):
    try:
        ProductView.query.filter_by(id=product_id).delete()
        return "Done"
    except:
        return "Error in ID"