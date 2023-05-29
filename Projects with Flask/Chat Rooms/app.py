from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def secret_key():
    return os.urandom(12) 



def create_app():

    app = Flask(__name__)
    csrf = CSRFProtect(app)


    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql//velin:123456@localhost'


    login_manager.init_app(app)
    db.init_app(app)    
    csrf.init_app(app)
