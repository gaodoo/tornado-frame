#!/usr/bin/env python
# encoding: utf-8

from base import *


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


class AdminUserHandler(AdminBaseHandler):
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
