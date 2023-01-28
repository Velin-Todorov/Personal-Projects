from flask import Flask, render_template, Blueprint, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user
from auth.email_confirm import generate_confirmation_token, confirm_token, send_mail
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from DailyCheck import db
from DailyCheck.db_models import User
from user.forms import ChangePassword, ChangeUsername
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint(
    "user",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/user"
)


@user.route('/profile')
@login_required
def profile():
    return render_template(
        'user_page.html'
    )


@user.route('/news')
@login_required
def news():

    return render_template(
        'news.html',
    )


@user.route('/weather')
@login_required
def weather():
    return render_template(
        'weather.html'
    )


@user.route('/edit-profile')
@login_required
def edit():
    return render_template(
        'edit_profile.html'
    )


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))


@user.route('/confirm-email')
@login_required
def confirm():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for(
        'auth.confirm_email',
        token=token,
        _external=True
    )
    html = render_template('email.html', confirm_url=confirm_url)
    subject = 'Email confirmation'
    send_mail(current_user.email, subject, html)
    logout()
    return render_template(
        'email_confirm.html'
    )


@user.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():

    form = ChangePassword()

    user = User.query.filter_by(id=current_user.id).first()

    print('before validating form')
    if form.validate_on_submit():

        old_password = request.form['old_password'].strip()
        new_password = request.form['new_password'].strip()
        repeat_pass = request.form['repass'].strip()

        if check_password_hash(current_user.password, old_password):

            if new_password == old_password:
                flash('Your new password cannot be your old password!')

                return render_template(
                    'change_password.html',
                    form=form
                )

            if new_password != repeat_pass:
                flash("Passwords don't match!")
                return render_template(
                    'change_password.html',
                    form=form
                )

            user.password = generate_password_hash(new_password)
            db.session.commit()

            logout()
            flash('Password successfully changed! You can now login with your new password')
            return redirect(url_for('auth.login'))
            
        else:
            flash('Wrong password')
            return render_template(
                'change_password.html',
                form=form
            )
    
    return render_template(
        'change_password.html',
        form=form
    )
