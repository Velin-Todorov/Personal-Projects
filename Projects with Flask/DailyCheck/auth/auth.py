from flask import Blueprint, render_template, request
from auth.forms import LoginForm, RegisterForm
from DailyCheck import db
from DailyCheck.db_models import User

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

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = bleach.clean(request.form['username'])
            email = bleach.clean(request.form['email'])
            password = request.form['password'].strip()
            repass = request.form['repass'].strip()

            user = User(email=email, username=username, password = generate_password_hash(password))

            from utils import check_user_exist, get_user_from_db

            if check_user_exist(user):
                flash('User already exists')
                return render_template('register.html', form=form)
            
            db.session.add(user)
            db.session.commit()
            token = user.generate_confirmation_token()
            send_email(
                user.email,
                'Confirm your Account using the link below. The link will expire in 2 hours',
                'email/confirm', 
                user=user, 
                token=token
            )
            flash('A confirmation email has been sent to you by email.')
            return redirect(url_for('login'))


    return render_template(
        'register.html',
        form = form
    )