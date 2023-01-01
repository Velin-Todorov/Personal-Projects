from flask import Blueprint, render_template, request, url_for, redirect, flash
from auth.forms import LoginForm, RegisterForm
from DailyCheck import db
from DailyCheck.db_models import User
from auth.email_confirm import generate_confirmation_token, confirm_token, send_mail
from DailyCheck import login_manager
import bleach
from flask_login import login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from user.user_views import profile


auth = Blueprint(

    "auth",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/auth"

)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = bleach.clean(request.form['email'])
        password = request.form['password'].strip()

        from DailyCheck.utils import get_user_from_db

        user = get_user_from_db(email, password)

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('user.profile'))

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


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = bleach.clean(request.form['username'])
            email = bleach.clean(request.form['email'])
            password = request.form['password'].strip()
            repass = request.form['repass'].strip()

            user = User(email=email, username=username,
                        password=generate_password_hash(password))

            from utils import check_user_exist

            if check_user_exist(user):
                flash('User already exists')
                return render_template('register.html', form=form)

            if password != repass:
                flash("Passwords don't match")
                return render_template('register.html', form=form)

            db.session.add(user)
            db.session.commit()

            token = generate_confirmation_token(user.email)
            
            confirm_url = url_for('auth.confirm_email',
                                  token=token, _external=True)
            html = render_template('email.html', confirm_url=confirm_url)
            subject = "Email confirmation"
            send_mail(user.email, subject, html)

            flash('A confirmation mail has been sent to the provided email address.')
            return redirect(url_for('auth.login'))

    return render_template(
        'register.html',
        form=form
    )


@auth.route('/email/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired')
    user = User.query.filter_by(email=email).first()
    if user.confirmed:
        flash('Account already confirmed. Please login')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account.!')
    return redirect(url_for('auth.login'))
