from sqlalchemy import Column, Integer, String
from views.masterDB import db

class UserView(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

    def to_json(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "email" : self.email
        }