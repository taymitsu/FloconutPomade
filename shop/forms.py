from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from shop.models import User

class RegisterForm(FlaskForm):
    def validate_user(self, user_check):
        username = User.query.filter_by(user=user_check.data).first()
        if username:
            raise ValidationError('Username Already Exists. Please enter a different username')
    def validate_email(self, email_check):
        email = User.query.filter_by(email=email_check.data).first()
        if email:
            raise ValidationError('Email Address Already Exists. Sign in!')

    user = StringField(label='Username', validators=[Length(min=5, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Retype Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    user = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')