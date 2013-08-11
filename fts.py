#!/usr/bin/env python
# encoding: utf-8

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaseFtsTest(unittest.TestCase):
    """
    the base class for fts test, setUp the firefox,
    and teardown after test finish, default the Base_url
    """
    base_url = 'http://localhost:8000'

    def setUp(self):
        self.br = webdriver.Firefox()
        self.br.implicitly_wait(3)
        #self.setUphooks()

    def tearDown(self):
        #self.tearDownhooks()
        self.br.quit()


class LoginTest(BaseFtsTest):

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
        self.br.get(self.base_url)
        body = self.br.find_element_by_tag_name('body')
        self.assertNotIn('index page', body.text)
        title = self.br.title
        self.assertEqual(u'login or register CGK', title)

        # login with wrong email and password, fails

        # after three fail we need input the 验证码

        # we now register to the cgk and success

        # we login with the new register email and password,
        # and we sucessed goto the index page

        # we signout and found need login again

        # we cheese the remind-me and login seccussd

        # we close the browser and reopen the index tobe login

        # done


class AdminTest(BaseFtsTest):
    """
    test for the admin pages
    """
    admin_base_url = 'http://localhost:8000/admin'

    def _admin_login(self, email, password):
        email = self.br.find_element_by_name('email')
        password = self.br.find_element_by_name('password')
        submit = self.br.find_element_by_css_selector('input[type="submit"]')
        email.send_keys('123456@qq.com')
        password.send_keys('123456')
        submit.click()

    def test_login_admin_page_need_to_be_admin(self):
        # we goto the page /admin without login,
        # we were take to the admin_login page
        self.br.get(self.admin_base_url)
        self.assertEqual(u'CGK Admin', self.br.title)
        url = '/'.join([self.admin_base_url, 'login'])
        self.assertEqual(url, self.br.current_url)

        # the page have a login form, whose action is
        # /admin/login, method is post
        adminform = self.br.find_element_by_name('fm')
        form_action = adminform.get_attribute('action')
        form_method = adminform.get_attribute('method')
        self.assertTrue(form_method == 'post')
        self.assertTrue(form_action.find('/admin/login') != -1)

        # we fill the form and submit with wrong user
        # and we were back here with error message
        err_email = '123456@qq.com'
        err_password = '123456'
        self._admin_login(err_email, err_password)
        self.assertTrue(self.br.current_url.find('/admin/login') != -1)
        #email = self.br.find_element_by_name('email')
        #password = self.br.find_element_by_name('password')
        #submit = self.br.find_element_by_css_selector('input[type="submit"]')
        #email.send_keys('123456@qq.com')
        #password.send_keys('123456')
        #submit.click()


if __name__ == '__main__':
    unittest.main()
