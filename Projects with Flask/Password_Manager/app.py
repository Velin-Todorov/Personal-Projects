from flask import Flask, render_template, request, flash, current_app
from Password_Manager import login_form, register_form, models
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from . import create_app

app = create_app()

@app.route('/')
def landing_page():
    """This view is concerned with the initial screen"""
    return render_template('landing_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """This view handles registration"""
    form = register_form.Register_Form()

    if request.method == 'POST':
    	pass       

    return render_template(
        'register.html',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """This view handles login form"""
    form = login_form.LoginForm()
    username = None
    password = None
    if form.validate_on_submit():
        email = form.username.data
        password = form.password.data

    return render_template(
        'login.html',
        form=form,
        email=username,
        password=password
    )


@app.route('/all-items')
def home():
    """This is  the homepage that will display all the "cards" """
    return render_template('home.html')


@app.route('/bank_cards')
def banking(name=None):
    """This view will show bank cards "cards" """
    return render_template('user.html', name=name)


@app.route('/websites')
def websites():
    """This view will show the password "cards" for websites"""
    return '<p>Welcome to our online shop</p>'


@app.route('/other')
def other():
    """This view is concerned with all other passwords that are not labeled"""
    return '<h1>Other</h1>'


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(e):
#     return render_template('500.html'), 500
