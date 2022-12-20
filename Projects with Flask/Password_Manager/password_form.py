from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Regexp

class PasswordForm(FlaskForm):
    name = StringField('Name')
    uri = StringField('URI')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = StringField('Add')