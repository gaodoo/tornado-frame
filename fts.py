#!/usr/bin/env python
# encoding: utf-8

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    index_url = 'localhost:8000'

    def setUp(self):
        self.br = webdriver.Firefox()
        self.br.implicitly_wait(3)

    def tearDown(self):
        self.br.quit()

    def test_signup_and_login_to_index(self):
        """
        go to the index page without login,
        then we were take to the login page
        login with error password fails,
        signup and go back to the login url,
        login success and we were take to the index page
        """

        # go to the index page without login, and we
        # were take to the login page
        self.br.get(self.index_url)
        body = self.br.find_element_by_tag_name('body')
        self.assertNotIn('index page', body.text)
        title = self.br.find_element_by_tag_name('title')
        self.assertEqual(u'login or register cgk', title)

        # login with wrong email and password, fails

        # after three fail we need input the 验证码

        # we now register to the cgk and success

        # we login with the new register email and password,
        # and we sucessed goto the index page

        # we signout and found need login again

        # we cheese the remind-me and login seccussd

        # we close the browser and reopen the index tobe login

        # done

if __name__ == '__main__':
    unittest.main()
