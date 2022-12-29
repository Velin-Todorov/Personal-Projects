from flask_login import UserMixin
from DailyCheck import db
from DailyCheck import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users_dailyCheck'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)


class SavedPosts(db.Model):
    __tablename__ = 'saved_posts'
    user = db.orm.relationship('User')
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_dailyCheck.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))