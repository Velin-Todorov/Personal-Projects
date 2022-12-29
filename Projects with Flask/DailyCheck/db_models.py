from flask_login import UserMixin
from DailyCheck import db
from DailyCheck import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import app

class User(UserMixin, db.Model):
    __tablename__ = 'users_dailyCheck'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)
    confirmed = db.Column(db.Boolean, default=False)


    def generate_confirmate_token(self, expiration = 7200):
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        
        if data.get('confirm') != self.id:
            return False
        
        self.confirmed = True
        db.session.add(self)
        return True


class SavedPosts(db.Model):
    __tablename__ = 'saved_posts'
    user = db.orm.relationship('User')
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_dailyCheck.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))