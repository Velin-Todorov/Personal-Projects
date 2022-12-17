from flask import Flask, render_template, request, flash, current_app, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from . import create_app
from .models import User
from . import db
from .login_form import LoginForm
from .register_form import Register_Form
from flask_login import login_required

# from .validations import check_if_email_in_db, check_if_username_in_db, check_if_passwords_match
from werkzeug.security import generate_password_hash, check_password_hash


app = create_app()


@app.route('/')
def landing_page():
    """This view is concerned with the initial screen"""
    return render_template('landing_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """This view handles registration"""
    form = Register_Form()

    if request.method == 'POST':
        if form.validate_on_submit():

            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            repeat_pass = request.form['repeat_pass']

            hashed_pass = generate_password_hash(password)
            hashed_re_pass = generate_password_hash(repeat_pass)

            user = User(email=email, username=username, password=hashed_pass)

            exists_username = User.query.filter_by(username=username).first()
            exists_email = User.query.filter_by(email=email).first()

            if len(username) < 3:
                flash('Username too short!')
                return render_template('register.html', form=form)

            if exists_username is not None or exists_email is not None:
                flash('User already exists')
                return render_template('register.html', form=form)

            else:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('landing_page'))

    return render_template(
        'register.html',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """This view handles login form"""
    form = LoginForm()

    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user is not None:
            if check_password_hash(user.password, password):
                return render_template('all_items.html')
            else:
                flash('Invalid password or username!')
        else:
            return render_template(
                'login.html',
                form=form
            )

    return render_template(
        'login.html',
        form=form
    )

@app.route('/all-items')
@login_required
def home():
    """This is  the homepage that will display all the "cards" """
    return render_template('landing_page.html')


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
