#!/usr/bin/env python
# encoding: utf-8

import unittest
from core import Base
from core import db_session_test as db_session
from core import engine
from core import create_all
from core import drop_all
from models import User
from forms import LoginForm, RegisterForm


class LoginUtilsTest(unittest.TestCase):
    """
    test for utils.user_login
    """
    def setUp(self):
        email = 'tmp@tmp.com'
        password = '123456'
        u = User(email, password, 'firstname', 'lastname')
        db_session.add(u)
        db_session.commit()

    def tearDown(self):
        pass

    def test_login_with_error_msg_return_none(self):
        email = 'tmp@tmp.com'
        password = '12345241231'
        user = User.login(email, password)
        self.assertEqual(None, user)

    def test_login_with_correct_msg_return_User_obj(self):
        email = 'tmp@tmp.com'
        password = '123456'
        user = User.login(email, password)
        self.assertTrue(isinstance(user, User))


class ModelTest(unittest.TestCase):
    """
    model test case
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass


#class LoginFormTest(unittest.TestCase):
    #"""
    #test for login form
    #"""
    #def setUp(self):
        #pass

    #def tearDown(self):
        #pass

    #def test_login_form_with_no_data_output_the_right_html(self):
        #form = LoginForm()
        #self.assertTrue(form.data.has_key('email'))
        #self.assertTrue(form.data.has_key('password'))
        #self.assertTrue(form.data.has_key('remind_me'))


if __name__ == '__main__':
    unittest.main()
