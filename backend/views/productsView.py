from sqlalchemy import Column, Integer, String, Float
from views.masterDB import db

class ProductView(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(Integer, unique=True)
    name = Column(String(100), unique=True)
    brand = Column(String(100))
    price = Column(Float)
    views = Column(Integer)

    def to_json(self):
        return {
            "id" : self.id,
            "sku" : self.sku,
            "name" : self.name,
            "brand" : self.brand,
            "views" : self.views,
            "price" : self.price
        }