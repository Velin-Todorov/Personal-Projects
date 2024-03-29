from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from flask import flash


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email(message= "Invalid email")])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=20, message='Username must be between 5 and 20 characters long')])
    email = EmailField('Email', validators=[Email(message='Invalid email', check_deliverability=True)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=64, message='Password must be between 8 and 64 characters')])
    repass = PasswordField('Repeat Password', validators=[InputRequired()])
    country= StringField('Country')
    submit = SubmitField('Register')
