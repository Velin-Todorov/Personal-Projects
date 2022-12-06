from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from login_form import LoginForm

class Register_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    repeat_pass = StringField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('submit')

    
    