from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return '<h1> Welcome to our online catalog!</h1>'

@app.route('/user')
@app.route('/user/<name>')
def user_profile(name=None):
    return render_template('user.html', name=name)

@app.route('/shop')
def shop():
    return '<p>Welcome to our online shop</p>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500