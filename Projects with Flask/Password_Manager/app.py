from flask import Flask, render_template, request, flash, current_app, redirect
from Password_Manager import login_form, register_form, models
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from . import create_app
from .models import User
from . import db

# from .validations import check_if_email_in_db, check_if_username_in_db, check_if_passwords_match
from werkzeug.security import generate_password_hash


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
        print(1)
        if form.validate_on_submit():
            print(1)
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            repeat_pass_form = request.form['repeat_pass']

            user = User(email=email, username=username, password = generate_password_hash(password))
            
           #TODO: Validations of registration

            db.session.add(user)
            db.session.commit()
            return '<h1>Registration successful</h1>'

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

    #TODO: Implement login

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

@app.route('/logout')
def logout():
    """This view deals with logout"""
    return '<h1>Logout</h1>'
    
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(e):
#     return render_template('500.html'), 500
