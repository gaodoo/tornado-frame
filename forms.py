#!/user/bin/env python
# encoding: utf-8

from wtforms import Form, validators
from wtforms import (PasswordField, BooleanField, TextField)


class LoginForm(Form):
    email = TextField('email', [validators.Length(min=6, max=64)])
    password = PasswordField('password', [validators.Length(min=6, max=30)])

class RegisterForm(Form):
    email = TextField(
        label='email',
        validators=[valudators.Length(min=6, max=64)],
        description='your email, be serious'
    )
    username = TextField(
        label='username',
        validators=[],
        description='',
    )
    password = PasswordField('password')
    rpassword = PasswordField('rpassword')
