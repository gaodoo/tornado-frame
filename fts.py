#!/user/bin/env python
# encoding: utf-8

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    index_url = 'localhost:8000'

    def setup(self):
        self.br = webdriver.Firefox()
        self.br.implicitly_wait(3)

    def teardowm(self):
        self.br.quit()

    def test_signup_and_login_to_index(self):
        """
        go to the index page without login,
        then we were take to the login page
        login with error password fails,
        signup and go back to the login url,
        login success and we were take to the index page
        """

        # go to the index page without login
        self.br.open(self.index_ulr)
        body = self.br.find_element_by_name(body)
        self.assertIn('hello world', body.text)
