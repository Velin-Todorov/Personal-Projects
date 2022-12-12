from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy_utils as su
import secrets

db = SQLAlchemy()
DB_Name = 'flask_pm'
success=False

def secret_key():
    return secrets.token_hex()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    create_database(app)
    return app

def create_database(app):
    if not su.functions.database_exists(app.config['SQLALCHEMY_DATABASE_URI'] + DB_Name):
        try:
            su.functions.create_database(app.config['SQLALCHEMY_DATABASE_URI'] + DB_Name)
            success = True
            if success:
                app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/' + DB_Name   
                db.create_all(app=app)
                print('Table created successfully!')

            print('Database created successfully!')
        except Exception as e:
            print('Failed')