#!/usr/bin/env python
# encoding: utf-8

import re
from tornado.escape import to_unicode
from wtforms import Form as wtForm
from wtforms import validators
from wtforms import (PasswordField, BooleanField, TextField)


class Form(wtForm):
    """
    the base form the tornado request wrap
    """
    def __init__(self, formdata=None, obj=None, prefix='', **kw):
        super(Form, self).__init__(formdata, obj, prefix, **kw)

    def process(self, formdata=None, obj=None, **kw):
        if formdata is not None and not hasattr(formdata, 'getlist'):
            formdata = TornadoArgumentsWrapper(formdata)
        super(Form, self).process(formdata, obj, **kw)


class TornadoArgumentsWrapper(dict):
    """
    wraps for the tornado request form
    """
    def getlist(self, key):
        """ docstrings for """
        return self[key]


class LoginForm(Form):
    """
    the login form
    """
    email = TextField(
        label=u'邮箱',
        validators=[
            validators.Length(min=6, max=64, message=u'邮箱必须介于6-64个字符'),
            validators.email(message=u'错误的邮箱地址'),
    ])
    password = PasswordField(
        label=u'密码',
        validators=[
            validators.Length(min=6, max=30, message=u'密码必须介于6-30个字符'),
    ])
    remind_me = BooleanField(
        label='记住我',
        default='0'
    )


class MessageForm(Form):
    """
    the register message form
    """
    qq = TextField(
        label=u'qq',
        validators=[validators.Length(min=6, max=11)]
    )
    telphone = TextField(
        label=u'联系方式',
        validators=[validators.Length(min=7, max=15)]
    )



class RegisterForm(Form):
    """
    the register form
    """
    email = TextField(
        label=u'邮箱',
        validators=[validators.Length(min=6, max=64)],
        description='your email, be serious')
    firstname = TextField(
        label=u'姓',
        validators=[],
        description='')
    lastname = TextField(label=u'名')
    password = PasswordField(label=u'密码')
    rpassword = PasswordField(label=u'密码确认')
