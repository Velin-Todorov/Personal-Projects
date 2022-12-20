from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Regexp

class PasswordForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    uri = StringField('URI', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')