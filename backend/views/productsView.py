from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class ProductView(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    sku = Column(Integer, unique=True)
    name = Column(String, unique=True)
    brand = Column(String)
    price = Column(Float)
    views = Column(Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)