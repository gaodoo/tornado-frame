#!/usr/bin/env python
# encoding: utf-8

from views import (
    HelloHanlder,
    IndexHandler,
    LoginHandler,
    RegisterHandler,
)


urls_pattern = [
    ('/', IndexHandler),
    ('/hello', HelloHanlder),
    ('/login', LoginHandler),
    ('/register', RegisterHandler),
]
