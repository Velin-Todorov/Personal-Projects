from app import app
import bcrypt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, force_auto_coercion

Base = declarative_base()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

force_auto_coercion()

class User(db.Model):
    """Table for users"""
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key = True)
    email = db.Column(String, unique=True)
    username = db.Column(String, unique=True)
    password_hash = db.Column(Text)
    phone_number = db.Column(Text)
    country = db.Column(String)


    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        password = b'password'
        self.password_hash = bcrypt.hashpw('password', bcrypt.gensalt())