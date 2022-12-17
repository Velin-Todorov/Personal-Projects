from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class Register_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 64)])
    email = EmailField('Email', validators=[DataRequired(), Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    repeat_pass = PasswordField('Repeat Password', validators=[DataRequired(),
        EqualTo('password', message='Password must match!'), Length(8, 128)
    ])
    submit = SubmitField('Register')

    