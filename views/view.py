#!/usr/bin/env python
# encoding: utf-8

from base import *


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
            self.redirect('/')


class RegisterHandler(BaseHandler):
    """ handler for register"""
    def get(self):
        lform = LoginForm()
        rform = RegisterForm()

        self.render('login.html', lform=lform, rform=rform)

    def post(self):
        rform = RegisterForm(self.request.arguments)
        if not rform.validate():
            lform = LoginForm()
            self.render('login.html', lform=lform, rform=rform)
        # register uesr
        user = User(rform.email.data, rform.password.data,
                rform.firstname.data, rform.lastname.data)
        self.db.add(user)
        self.db.commit()
        # set user into the session
        self.session['user'] = user
        self.render('register_step.html')

class RegisterStepHandler(BaseHandler):
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

