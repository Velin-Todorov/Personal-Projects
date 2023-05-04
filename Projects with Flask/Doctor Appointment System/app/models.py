from  .app import db
#from .main import login_manager
from flask_login import UserMixin
import datetime
from sqlalchemy.dialects.postgresql import JSON

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String, unique=True)
    age = db.Column(db.Integer)
    is_patient = db.Column(db.String, default=False)
    username = db.Column(db.String, index=True)
    password = db.Column(db.Text)
    confirmed = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime(), default=datetime.date.today)



class Patient(User, db.Model):
    __tablename__= 'patients'
    user = db.orm.relationship('User')
    patients_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # A user becomes a patient when is_patient is True
    #patient_to = the doctor the user chose



class Doctor(UserMixin, db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    patients = db.Column(JSON)


