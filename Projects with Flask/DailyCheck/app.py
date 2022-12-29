from flask import Flask, render_template
from . import create_app


app = create_app()


@app.route('/')
def home_page():
    return render_template(
        'landing_page.html'
    )


@app.route('/login')
def login():
    return render_template(
        'login.html'
    )


@app.route('/register')
def register():
    return render_template(
        'register.html'
    )


