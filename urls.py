#!/usr/bin/env python
# encoding: utf-8

from views import (
    HelloHanlder,
    IndexHandler,
    LoginHandler,
    RegisterHandler,
    AdminIndexHandler,
    AdminLoginHandler,
)


urls_pattern = [
    ('/', IndexHandler),
    ('/hello', HelloHanlder),
    ('/login', LoginHandler),
    ('/register', RegisterHandler),
]

urls_pattern_admin = [
    ('/admin', AdminIndexHandler),
    ('/admin/login', AdminLoginHandler),
]

urls_pattern.extend(urls_pattern_admin)
