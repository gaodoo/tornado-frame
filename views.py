#!/user/bin/env python
# encoding: utf-8

import tornado.web
from core import Session
from forms import RegisterForm, LoginForm


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        # TODO: the login url to set the uesr in session
        if self.session and 'user' in self.session:
            return session['user']
        else:
            return None

    @property
    def session(self):
        sessionid = self.get_secure_cookie('sid')
        session = Session(self.application.session_store, sessionid)
        if not sessionid:
            self.set_secure_cookie('sid', session._sessionid)
        return session

    @property
    def db(self):
        return self.application.db

    def write_error(self, status_code, **kw):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(RequestHandler, self).write_error(status_code, **kw)

class HelloHanlder(BaseHandler):
    def get(self):
        """ write hello world """
        self.write('hello world')


class IndexHandler(BaseHandler):
    def get(self):
        """
        if not login redirect to the login page
        else go to the index page
        """
        if not self.current_user:
            self.redirect('/login')

        self.write('index page')

class LoginHandler(BaseHandler):
    def get(self):
        """
        render the login page and login form
        """
        lform = LoginForm()
        rform = RegisterForm()

        self.render('login.html', lform=lform, rform=rform)

    def post(self):
        """
        validate the form data,
        if fails, return the login url,
        after fails three times use yanzheng code
        else if success, set the user to session and
        go to the index page
        """
        print self.request.arguments
        form = LoginForm(self.request.arguments)
        print form.data
        if not form.validate():
            self.render('login.html', form=form)

        #user = self.user_login(form.)
        self.render('index.html')
