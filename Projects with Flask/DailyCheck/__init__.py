import mimetypes
mimetypes.add_type('application/javascript', '.js', True)
mimetypes.add_type('text/css', '.css')

from dotenv import load_dotenv

from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets
from flask_mail import Mail
import os


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def secret_key():
    return secrets.token_hex()

def password_salt():
    return os.urandom(15)

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    load_dotenv()

    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_PASSWORD_SALT'] = password_salt()

    # mail configurations

    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
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