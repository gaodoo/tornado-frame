#!/usr/bin/env python
# encoding: utf-8

from os import path
from urls import urls_pattern as url_handlers
from tornado.options import define, options

#define('mysql_host', default='localhost', help="Main User")

DEBUG = True

# the application settings
settings = {
    'debug': DEBUG,
    'cookie_secret': 'test', # TODO: get the real secret
    'login_url': '/login',
    'xsrf_cookies': True,
    'static_path': path.join(path.dirname(__file__), 'static'),
    'template_path': path.join(path.dirname(__file__), 'templates'),
    #'ui_modules': '' # TODO: the ui modules file
}

# the sql database settings
databases = {
    'default': {
        'driven': 'mysql',
        'host': 'localhost',
        'user': 'root'
        'password': 'root',
        'port': 'port',
        'database': 'cgk',
    }
    'test': {
        'driven': 'mysql',
        'host': 'localhost',
        'user': 'root'
        'password': 'root',
        'port': 'port',
        'database': 'cgk_test',
    }
}

# TODO: the reids database settings
reids_db = {

}

# TODO: the log settings


# TODO: memcahce usage
