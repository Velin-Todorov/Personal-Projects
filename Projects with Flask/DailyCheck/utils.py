from DailyCheck import db
from db_models import User
from werkzeug.security import check_password_hash

def check_user_exist(user: User):
    username = User.query.filter_by(username=user.username).first()
    email = User.query.filter_by(email=user.email).first()

    if username is not None or email is not None:
        return True
    
    return False

def get_user_from_db(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return user
    
    return None

