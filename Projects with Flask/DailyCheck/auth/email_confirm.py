from threading import Thread
from flask import current_app
from flask_mail import Message
from DailyCheck import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipents, text_body, html_body):
    pass
