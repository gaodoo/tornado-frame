#!/user/bin/env python
# encoding: utf-8

import unittest
from core.utils import user_login

class LoginUtilsTest(unittest.TestCase):
    """
    test fro utils.user_login
    """

    def test_login_with_error_msg_return_none(self):
        email = 'tmp@tmp.com'
        password = '123456'
        self.assertEqual(None, user_login(email, password))

    def test_login_with_correct_msg_return_Uesr_obj(self):
        # TODO: insert the user msg into test db
        email = 'tmp@tmp.com'
        password = '123456'
        self.assertTrue(isinstance(user_login(email, password)), User)

