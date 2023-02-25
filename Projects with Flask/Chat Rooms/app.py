from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os


def secret_key():
    return os.urandom(12) 



def create_app():

    app = Flask(__name__)
    csrf = CSRFProtect(app)
    manager = Couc

    app.config['SECRET_KEY'] = secret_key()



    csrf.init_app(app)
