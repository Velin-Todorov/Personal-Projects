from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy_utils as su
from flask_login import LoginManager, AnonymousUserMixin
import secrets
import cryptography
from cryptography.fernet import Fernet
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'


def secret_key():
    return secrets.token_hex()

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username= 'Guest'

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    csrf = CSRFProtect(app)
    
    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://velin:123456@localhost/project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.anonymous_user = Anonymous

    with app.app_context():
        from . import models
        db.create_all()

    return app