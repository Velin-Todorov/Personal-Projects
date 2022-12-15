from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

class Register_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_pass = PasswordField('Repeat Password', validators=[DataRequired(),
        EqualTo('password', message='Password must match!')
    ])
    submit = SubmitField('Register')

    
    