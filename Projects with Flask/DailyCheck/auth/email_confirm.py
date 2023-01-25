from threading import Thread
from flask import current_app
from flask_mail import Message
from DailyCheck import mail
from itsdangerous import URLSafeSerializer


def generate_confirmation_token(email):
    from DailyCheck.app import app
    serializer = URLSafeSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration= 7200):
    from DailyCheck.app import app

    serializer = URLSafeSerializer(
        app.config['SECRET_KEY']
    )
    try:
        email = serializer.loads(
            token,
            salt = app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

def send_mail(to, subject, template):
    from DailyCheck.app import app
    msg = Message(
        subject=subject,
        recipients=[to],
        html=template,
        sender= app.config['MAIL_USERNAME']
    )
    mail.send(msg)