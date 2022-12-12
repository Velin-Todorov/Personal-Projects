from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    # type: ignore 
    """Table for users"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.Text)

    def __init__(self, id, email, username, password) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.password = password
