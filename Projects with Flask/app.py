from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from login_form import LoginForm
from register_form import Register_Form
from flask_wtf import CSRFProtect
from utils import environmental_vars, auth
from flask_sqlalchemy import SQLAlchemy
from database import User

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = environmental_vars.secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def landing_page():
    """This view is concerned with the initial screen"""
    return render_template('landing_page.html')

@app.route('/register', methods=['POST'])
def register():
    """This view handles registration"""
    form = Register_Form()

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('email')
    re_pass = request.form.get('email')

    email = User.query.filter_by(email=email).first()
    user = User.query.filter_by(username=username)

    if email or user:
        flash('Username or email already in user')
        return render_template('register.html', form=form)

    else:
        new_user = User(email=email, username=username, password= auth.hash_password(password))
        db.session.add(new_user)
        db.session.commit()
        app.redirect('/')

    return render_template(
        'register.html', 
        form=form, 
        email=email, 
        username = username,
        password=password,
        re_pass=re_pass,
    )   

@app.route('/login', methods=['POST'])
def login():
    """This view handles login form"""
    form = LoginForm()
    username = None
    password = None
    if form.validate_on_submit():
        email = form.username.data
        password = form.password.data

    return render_template(
        'login.html', 
        form=form,
        email = username,
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

db.create_all()