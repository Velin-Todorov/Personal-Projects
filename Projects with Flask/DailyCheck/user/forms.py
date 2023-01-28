from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import Email, InputRequired, Length, EqualTo


class ChangePassword(FlaskForm):
    old_password = PasswordField('Old password', validators=[InputRequired(), Length(min=8, max=64, message='Password must be between 8 and 64 characters')])
    new_password = PasswordField('New password', validators=[InputRequired(), Length(min=8, max=64, message='Password must be between 8 and 64 characters')])
    repass= PasswordField('Repeat new password', validators=[InputRequired(), Length(min=8, max=64, message='Password must be between 8 and 64 characters')])
    submit=SubmitField('Change Password')


class ChangeUsername(FlaskForm):
    new_username = StringField('New username', validators=[InputRequired()])
    submit = SubmitField('Change Username')