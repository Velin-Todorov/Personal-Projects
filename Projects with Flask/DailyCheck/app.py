from flask import Flask, render_template, request, flash, redirect, url_for
from . import create_app
from forms import LoginForm, RegisterForm
import bleach
from flask_login import logout_user
from db_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from utils import check_user_exist, get_user_from_db
from . import db
from itsdangerous import TimedJSONWebSignatureSerializer

app = create_app()


@app.route('/')
def home_page():
    return render_template(
        'landing_page.html'
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = bleach.clean(request.form['email'])
        password = requests.form['password'].strip()
    
        user = get_user_from_db(email, password)
        if user is not None:
            login_user(user)
            return redirect(url_for('user', name=user.username))

        else:
            flash('Invalid password or email')

            return render_template(
                'login.html',
                form=form
            )

    return render_template(
        'login.html',
        form=form
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = bleach.clean(request.form['username'])
            email = bleach.clean(request.form['email'])
            password = request.form['password'].strip()
            repass = request.form['repass'].strip()

            user = User(email=email, username=username, password = generate_password_hash(password))

            if check_user_exist(user):
                flash('User already exists')
                return render_template('register.html', form=form)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))


    return render_template(
        'register.html',
        form = form
    )


