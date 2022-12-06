from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from login_form import LoginForm
from register_form import Register_Form


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
bootstrap = Bootstrap(app)


@app.route('/')
def landing_page():
    """This view is concerned with the initial screen"""
    return render_template('landing_page.html')

@app.route('/register')
def register():
    """This view handles registration"""
    form = Register_Form()
    return render_template('register.html')

@app.route('/login')
def login():
    """This view handles login form"""
    form = LoginForm()
    if form.validate_on_submit():
        name = form.email.data
    return render_template('login.html', form=form)


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








@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500