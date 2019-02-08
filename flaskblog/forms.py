from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    user = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                            validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_user(self, user):
        user_dup = User.query.filter_by(username=user.data).first()
        if user_dup:
            raise ValidationError('Username is already in use. Please use a different one.')

    def validate_email(self, email):
        user_dup = User.query.filter_by(email=email.data).first()
        if user_dup:
            raise ValidationError('Email is already in use. Please use a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                            validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
