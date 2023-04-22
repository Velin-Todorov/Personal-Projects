from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
import secrets
import os


mail = Mail()
db = SQLAlchemy()

# login_manager = LoginManager()
# login_manager.login_view = 

def secret_key():
    return secrets.token_hex()

def password_salt():
    return os.urandom(15)


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    
    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://velin:1234567@localhost/doctors'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf.init_app(app)
    
    

