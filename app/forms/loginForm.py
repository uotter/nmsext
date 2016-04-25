from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('PassWord', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
