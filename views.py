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
            return session['user']
        else:
            return None

    def user_login(self, email, password):
        # user the utils login and set user
        # on the session. or return none if fails

        login_result = User.login(email, password, self.db)
        if login_result:
            self.session.set_session('user', login_result)

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
        if not cur_user or not cur_uesr.is_admin:
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


class AdminIndexHandler(AdminBaseHandler):
    """
    the admin index handler
    """
    def get(self):
        self.render('admin/index.html')


class AdminLoginHandler(AdminBaseHandler):
    """
    the admin login handler
    """
    def get(self):
        form = LoginForm()
        self.render('admin/login.html', form=form)

    def post(self):
        """
        validator the form and login the user and check admin
        return login page or admin index page
        """
        form = LoginForm(self.request.arguments)
        user = User.login(form.data.email, form.data.password)
        if not form.validator() or not user:
            self.render('admin/login.html', form=form)
        self.redirect('/admin')


class UserAdmin(AdminBaseHandler):
    """
    admin the uesr
    """
    def get(self, step):
        if step == 'list':
            self.get_list()
        elif step == 'view':
            self.get_view()
        elif step == 'modify':
            self.get_modify()
        elif step == 'create':
            self.get_create()

    def post(self, step):
        if step == 'delete':
            pass
        elif step == 'update':
            pass
        elif step == 'create':
            pass



class IndexHandler(BaseHandler):
    def get(self):
        """
        if not login redirect to the login page
        else go to the index page
        """
        if not self.current_user:
            self.redirect('/login')
        else:
            self.write('index page')

class LoginHandler(BaseHandler):
    def get(self):
        """
        render the login page and login form
        """
        lform = LoginForm()
        rform = RegisterForm()
        show = 0 # 0 show the register, 1 show the login

        self.render('login.html', lform=lform, rform=rform, show=show)

    def post(self):
        """
        validate the form data,
        if fails, return the login url,
        after fails three times use yanzheng code
        else if success, set the user to session and
        go to the index page
        """
        lform = LoginForm(self.request.arguments)
        if not lform.validate() or not self.user_login(lform.email.data, lform.password.data):
            rform = RegisterForm()
            show = 'l'
            self.render('login.html', lform=lform, rform=rform, show=1)
        else:
            self.write('index page')
            #self.redirect('/')


class RegisterHandler(BaseHandler):
    """ handler for register"""
    def get(self):
        lform = LoginForm()
        rform = RegisterForm()

        self.render('login.html', lform=lform, rform=rform)

    def register(self):
        rform = RegisterForm(self.request.arguments)
        if not form.validate():
            lform = LoginForm()
            self.render('login.html', lform=lform, rform=rform)
        # register uesr
        user = User(rform.data.email, rform.data.password,
                rform.data.firstname, rform.lastname)
        self.db.add(user)
        self.db.commit()
        # set user into the session
        self.set_session('user', user)
        self.render('register_step.html')

class RegisterStep(BaseHandler):
    """
    handler for register steps goon
    """
    def post(self, step):
        # first step
        if step == "info":
            self.render('rstep_one.html')
        # two step, for more info
        elif step == "message":
            form = MessageForm()
            self.render('rstep_two.html', form=form)
        # third step, for attend users
        elif step == "attend":
            users = self.db.query(User).order_by(User.create_time).limit(20)
            self.render('rstep_three.html', users=user)
        # fourth step, for attend subjects
        elif step == "subject":
            subjects = self.db.query(Subject).order_by(Subject.create_time).limit(20)
            self.render('rstep_four.html', subjects=subjects)
        # last, finish and redirect index page
        elif step == "finish":
            self.redirect('/')

