from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DBCONFIG

def getUrl():
    return "mysql://{user}:{password}@{server}/{database}".format(
        user = DBCONFIG['user'],
        password = DBCONFIG['password'],
        server = DBCONFIG['server'],
        database = DBCONFIG['db']
    )