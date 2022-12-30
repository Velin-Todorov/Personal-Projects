from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets
from flask import Flask
from flask_mail import Mail


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

def secret_key():
    return secrets.token_hex()


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://velin:123456@localhost/dailyCheck'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        import DailyCheck.db_models
        db.create_all()


    return app