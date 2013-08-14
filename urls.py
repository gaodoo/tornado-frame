#!/usr/bin/env python
# encoding: utf-8

__all__ = ['urls_pattern']


from views import (
    IndexHandler,
    LoginHandler,
    RegisterHandler,
    RegisterStepHandler,
)
from views import (
    AdminIndexHandler,
    AdminLoginHandler,
    AdminUserHandler,
)


urls_pattern = [
    ('/', IndexHandler),
    ('/login', LoginHandler),
    ('/register', RegisterHandler),
    ('/register/step', RegisterHandler),
]

urls_pattern_admin = [
    ('/admin', AdminIndexHandler),
    ('/admin/login', AdminLoginHandler),
    ('/admin/user', AdminUserHandler),
]

urls_pattern.extend(urls_pattern_admin)


