#!/usr/bin/env python
# encoding: utf-8

import tornado.web
from core import Session
from forms import RegisterForm, LoginForm, MessageForm
from models import User, Subject


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        # TODO: the login url to set the user in session
        if self.session and 'user' in self.session:
            return self.session['user']
        else:
            return None

    def user_login(self, email, password):
        # user the utils login and set user
        # on the session. or return none if fails

        login_result = User.login(email, password)
        if login_result:
            self.session['user'] = login_result

        return login_result

    @property
    def session(self):
        sessionid = self.get_secure_cookie('sid')
        session = Session(self.application.session_store, sessionid)
        if not sessionid:
            self.set_secure_cookie('sid', session._sessionid)
        return session

    def on_finish(self):
        """ for session store """
        self.session._save()

    @property
    def db(self):
        return self.application.db

    #def write_error(self, status_code, **kw):
        # TODO: write the 404 and 500 page after almost finish,
        # TODO: or dist the debug and product mode
        #if status_code == 404:
            #self.render('404.html')
        #elif status_code == 500:
            #self.render('500.html')
        #else:
            #super(RequestHandler, self).write_error(status_code, **kw)


class AdminBaseHandler(BaseHandler):
    """
    base handler class for the admin page
    set the child need tobe login and be admin.
    set the login url to admin login.
    """
    def get_current_user(self):
        """
        if user not login or not admin user,
        and the url is not admin/login
        return none
        """
        cur_user = super(AdminBaseHandler, self).get_current_user()
        if not cur_user or not cur_user.is_admin:
            return None
        else:
            return cur_user

    def get_login_url(self):
        """
        return the admin login url
        """
        return "/admin/login"

    def prepare(self):
        """
        the admin page need user to be admin login,
        if not, redirect the admin login url
        """
        if not self.current_user and self.request.path != '/admin/login':
            admin_login_url = self.get_login_url()
            self.redirect(admin_login_url)
