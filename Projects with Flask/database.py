from app import app
from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    """Table for users"""
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key = True)
    email = db.Column(String, unique=True)
    username = db.Column(String, unique=True)
    password = db.Column(Text)
    phone_number = db.Column(Text)
    country = db.Column(String)

    def __init__(self, id, email, username, password, phone_number, country) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.country = country
        


