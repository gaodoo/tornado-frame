#!/usr/bin/env python
# encoding: utf-8

from base import *


class AdminIndexHandler(AdminBaseHandler):
    """
    the admin index handler
    """
    def get(self):
        self.render('admin/index.html')

class AdminListHandler(AdminBaseHandler):
    """
    the admin list page of models
    """
    _model_name_d = {
        'user': User,
    }

    def get(self, model_name):
        """
        分页显示models数据
        """
        model = self._model_name_d[model_name]
        page = self.get_argument('page', 1)
        if page < 1: page = 1

        model_len = self.db.query(model).count()
        pagesize = 35;
        if model_len / pagesize < page :
            page = model_len / pagesize
        offset = page * pagesize

        results = self.db.query(model)[offset:pagesize]
        print results[0]
        print dir(results[0])
        self.render('admin/list.html', results=results, page=page, pagesize=pagesize)


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
        user = self.user_login(form.email.data, form.password.data)
        if not form.validate() or not user:
            self.render('admin/login.html', form=form)

        self.redirect('/admin')
