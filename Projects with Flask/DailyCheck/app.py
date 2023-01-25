from flask import Flask, render_template
from DailyCheck import create_app
import bleach
from flask_login import logout_user
from auth.auth import auth
from user.user_views import user

app = create_app()

app.register_blueprint(auth)
app.register_blueprint(user)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template(
        'landing_page.html'
    )