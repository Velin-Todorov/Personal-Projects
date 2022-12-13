from . import db

class User(db.Model):
    # type: ignore 
    """Table for users"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String, unique=True)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)

