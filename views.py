#!/user/bin/env python
# encoding: utf-8

import tornado.web


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
        self.write('hello world')
        body = self.br.find_element_by_name(body)
        self.assertIn('hello world', body.text)
