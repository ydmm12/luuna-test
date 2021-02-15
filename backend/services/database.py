from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DBCONFIG

def getEngine():
    return create_engine(getUrl(), pool_recycle=3600)

def getDB():
    Session = sessionmaker(bind=getEngine())
    session = Session()
    return session

def getUrl():
    return "mysql://{user}:{password}@{server}/{database}".format(
        user = DBCONFIG['user'],
        password = DBCONFIG['password'],
        server = DBCONFIG['server'],
        database = DBCONFIG['db']
    )