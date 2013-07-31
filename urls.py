#!/user/bin/env python
# encoding: utf-8

from views import (
    HelloHanlder,
    IndexHandler,
    LoginHandler,
)


urls_pattern = [
    ('/', IndexHandler),
    ('/hello', HelloHanlder),
    ('/login', LoginHandler),
]
