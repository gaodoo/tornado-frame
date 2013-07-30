#!/user/bin/env python
# encoding: utf-8

from os import path
from urls import urls_pattern as url_handlers
from tornado.options import define, options

#define('mysql_host', default='localhost', help="Main User")

settings = {
    'debug': True,
    'cookie_secret': 'test', # TODO: get the real secret
    'login_url': '/login',
    'xsrf_cookies': True,
    'static_path': path.join(path.dirname(__file__), 'static')
    'ui_modules': '' # TODO: the ui modules file
}
