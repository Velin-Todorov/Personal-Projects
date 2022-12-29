from flask import Flask, render_template
from . import create_app
from forms import LoginForm, RegisterForm
import bleach


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
        email = bleach.clean(requests.form['email'])
        password = requests.form['password'].strip()



    return render_template(
        'login.html',
        form=form
    )


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template(
        'register.html',
        form = form
    )


