#!/user/bin/env python
# encoding: utf-8

from views import HelloHanlder, IndexHandler


urls_pattern = [
    ('/', IndexHandler),
    ('/hello', HelloHanlder),
]
