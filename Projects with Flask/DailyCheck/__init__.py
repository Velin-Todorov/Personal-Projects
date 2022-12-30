from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets
from flask import Flask
from flask_mail import Mail
import os


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

def secret_key():
    return secrets.token_hex()

def password_salt():
    return os.urandom(15)

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://velin:123456@localhost/dailyCheck'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_PASSWORD_SALT'] = password_salt()

    # mail configurations
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'dailycheckflask@gmail.com'
    app.config['MAIL_PASSWORD'] = 'azdrsjnvwdytmujq'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        import DailyCheck.db_models
        db.create_all()


    return app