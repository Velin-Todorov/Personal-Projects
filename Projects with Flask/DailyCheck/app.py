from flask import Flask
from . import create_app

app = create_app()

@app.route('/')
def home_page():
    return '<h1>Welcome to the daily check</h1>'
