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
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError

    def getlist(self, key):
        """ docstrings for """
        try:
            values = []
            for v in self[key]:
                v = to_unicode(v)
                if isinstance(v, unicode):
                    v = re.sub(r"[\00-\x08\x0e-\x1f]", " ", v)
                values.append(v)
                return values
        except KeyError:
            raise AttributeError


class LoginForm(Form):
    """
    the login form
    """
    email = TextField(
            label=u'邮箱',
            validators=[validators.Length(min=6, max=64)])
    password = PasswordField(
            label=u'密码',
            validators=[validators.Length(min=6, max=30)])
    remind_me = BooleanField(
            label='记住我',
            default=False)


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
