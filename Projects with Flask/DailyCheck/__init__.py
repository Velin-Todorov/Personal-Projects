from flask_wtf.csrf import CSRFProtect
from flask import Flask

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    return app