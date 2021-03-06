from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class SignupForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    passport = StringField('passport', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
