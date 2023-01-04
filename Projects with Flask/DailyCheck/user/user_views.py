from flask import Flask, render_template, Blueprint, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from auth.email_confirm import generate_confirmation_token, confirm_token, send_mail
from flask_login import current_user

user = Blueprint(
    "user",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/user"
)

@user.route('/profile')
def profile():
    return render_template(
        'user_page.html'
    )

@user.route('/saved-posts')
def saved_posts():
    pass

@user.route('/news')
def news():
    pass

@user.route('/weather')
def weather():
    pass

@user.route('/history')
def history():
    pass

@user.route('/edit-profile')
def edit():
    pass

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@user.route('/confirm-email')
def confirm():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for(
        'auth.confirm_email',
        token=token,
        _external = True
    )
    html = render_template('email.html', confirm_url=confirm_url)
    subject = 'Email confirmation'
    send_mail(current_user.email, subject, html)
    logout()
    return render_template(
        'email_confirm.html'
    )
