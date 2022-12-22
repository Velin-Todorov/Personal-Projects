from flask import Flask, render_template, request, flash, current_app, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from . import create_app
from .models import User, Password
from . import db
from .login_form import LoginForm
from .register_form import Register_Form
from flask_login import login_required, logout_user, current_user, login_user, current_user
import bleach
from flask_login import AnonymousUserMixin
from .password_form import PasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
import os
from cryptography.fernet import Fernet
from .encryption import generate_key, load_key



app = create_app()
@app.route('/')
def landing_page():
    """This view is concerned with the initial screen"""
    return render_template(
        'landing_page.html'
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    """This view handles registration"""
    form = Register_Form()

    if request.method == 'POST':
        if form.validate_on_submit():

            username = bleach.clean(request.form['username'])
            email = bleach.clean(request.form['email'])
            password = request.form['password'].strip()
            repeat_pass = request.form['repeat_pass'].strip()

            hashed_pass = generate_password_hash(password)
            hashed_re_pass = generate_password_hash(repeat_pass)

            user = User(email=email, username=username, password=hashed_pass)

            exists_username = User.query.filter_by(username=username).first()
            exists_email = User.query.filter_by(email=email).first()

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
    
        email = bleach.clean(request.form['email'])
        password = request.form['password'].strip()
        
        user = User.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('user_page', name=user.username)
                return redirect(next)
            
        else:
            flash('Invalid password or username!')

            return render_template(
                'login.html',
                form=form
            )

    return render_template(
        'login.html',
        form=form
    )

@app.route('/user_page/<name>')
@login_required
def user_page(name=None):
    user = current_user
    return render_template(
        'user_page.html', 
        user=user
    )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    """This view deals with logout"""
    return redirect(url_for('landing_page'))

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PasswordForm()
    key = None

    if form.validate_on_submit():
        name = bleach.clean(request.form['name'])
        uri = bleach.clean(request.form['uri'])
        password_from_form = bleach.clean(request.form['password'].strip())

        if os.path.exists(os.path.abspath('secret.key')):
            key = load_key()

        else:
            generate_key()
            key = load_key()
        
        f = Fernet(key)

        password = Password(name=name, uri=uri, password=f.encrypt(password_from_form.encode()), user_id=current_user.id)

        db.session.add(password)
        db.session.commit()
        return redirect(url_for('vault', name=current_user.username))        
    
    return render_template(
        'create.html', 
        form=form
    )

@app.route('/vault/<name>')
@login_required
def vault(name):

    passwords_info = []
    user_passwords = Password.query.filter(Password.user_id == current_user.id).all()
    key = load_key()
    f = Fernet(key)
    
    for attr in user_passwords:
        password_obj = {
            'name': attr.name,
            'uri': attr.uri,
            'password': f.decrypt(attr.password).decode()
        }
        passwords_info.append(password_obj)



    return render_template('vault.html', user_passwords = passwords_info)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(e):
#     return render_template('500.html'), 500
