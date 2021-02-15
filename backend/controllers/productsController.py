from views.productsView import ProductView
from services.database import getDB

DB = getDB()

def get_products():
    return {"body":(
        {"id": 1},
    )}

def get_product(product_id):
    return {"id": product_id}

def create_product(product):
    return product

def modify_product(product_id, product):
    Product = ProductView.query.filter_by(id=product_id)
    modified = {}
    for key in product:
        if getattr(Product,key) != product[key]:
            setattr(Product, key, product[key])
            modified[key] = product[key]
    return product

def delete_product(product_id):
    try:
        return ProductView.query.filter_by(id=product_id).delete()
    except:
        return "Error in ID"