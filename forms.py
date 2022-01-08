from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class Register(FlaskForm):
    username = StringField(label='Username:')
    email_address = StringField(label='Email Address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Retype Password:')
    submit = SubmitField(label='Create Account')