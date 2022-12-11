from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

class Register_Form(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), 
        EqualTo('repeat_pass', message='Passwords must match!')
    ])
    repeat_pass = PasswordField('Repeat Password', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired()])
    country = StringField('Country', validators=[Optional()])
    submit = SubmitField('Register')

    
    