from services.database import getEngine
from sqlalchemy.ext.declarative import declarative_base
from views.usersView import UserView
from views.productsView import ProductView

user = UserView
Base = declarative_base()
Base.metadata.create_all(getEngine())
