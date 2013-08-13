#!/usr/bin/env python
# encoding: utf-8

from views import (
    IndexHandler,
    LoginHandler,
    RegisterHandler,
    AdminIndexHandler,
    AdminLoginHandler,
)


urls_pattern = [
    ('/', IndexHandler),
    ('/login', LoginHandler),
    ('/register', RegisterHandler),
]

urls_pattern_admin = [
    ('/admin', AdminIndexHandler),
    ('/admin/login', AdminLoginHandler),
]

urls_pattern.extend(urls_pattern_admin)
