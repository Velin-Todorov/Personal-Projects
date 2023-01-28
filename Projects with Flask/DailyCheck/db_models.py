from flask_login import UserMixin
from DailyCheck import db
from DailyCheck import login_manager
from itsdangerous import URLSafeTimedSerializer as Serializer
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users_dailyCheck'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)
    confirmed = db.Column(db.Boolean, default=False)
    from_country = db.Column(db.Text)
    created_on = db.Column(db.DateTime(), default=datetime.date.today)


    def generate_confirmation_token(self, expiration = 7200):
        from . import app
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        from . import app
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))