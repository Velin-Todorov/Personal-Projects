from flask import Flask, render_template, Blueprint, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user
from auth.email_confirm import generate_confirmation_token, confirm_token, send_mail
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter

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

@user.route('/news')
def news():

    search = True
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    pagination = Pagination(page=page, search=search)
    pagination.per_page = 10
    pagination.page_parameter = 'page'

    return render_template(
        'news.html',
         pagination=pagination
    )
   

@user.route('/weather')
def weather():
    return render_template(
        'weather.html'
    )

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
