from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.login_view = 'login'


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://velin:123456@localhost/daily_check'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # login_manager.init_app(app)
    csrf.init_app(app)

    return app