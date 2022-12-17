from . import db
from . import login_manager


class Password(db.Model):
    __tablename__ = 'user_passwords'
    user = db.orm.relationship('User')
    id=db.Column(db.Integer, primary_key=True)
    hashed_password = db.Column(db.Text)
    website = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

class User(db.Model):
    # type: ignore 
    """Table for users"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String, unique=True)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))