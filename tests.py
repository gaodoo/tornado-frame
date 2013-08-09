#!/usr/bin/env python
# encoding: utf-8

import unittest
from core import Base
from core import db_session_test as db_session
from core import engine_test as engine
from core import create_all_for_test as create_all
from core import drop_all_for_test as drop_all
from models import User
from forms import LoginForm, RegisterForm


class FixtureTest(unittest.TestCase):
    """
    the base test for use tmp_db and install self.fixture
    """
    def setUp(self):
        self._test_db_setup()
        self._fixture_setup()

    def tearDown(self):
        self._fixture_remove()
        self._test_db_uninstall()

    def _test_db_setup():
        create_all()

    def _fixture_setup(self):
        if self.fixture:
            # TODO: install fixture
            pass

    def _fixture_remove(self):
        pass



class LoginUtilsTest(unittest.TestCase):
    """
    test for utils.user_login
    """
    def setUp(self):
        drop_all()
        create_all()
        email = 'tmp@tmp.com'
        password = '123456'
        u = User(email, password, 'firstname', 'lastname')
        db_session.add(u)
        db_session.commit()

    def tearDown(self):
        #self._fixture_remove()
        #self._test_db_uninstall()
        drop_all()

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
