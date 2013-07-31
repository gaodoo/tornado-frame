#!/user/bin/env python
# encoding: utf-8

import unittest
import json
from .database import engine_test, create_all_for_test
# parent testcase suppoert fixture for tempdb

class FBTestCase(unittest.TestCase):
    def setup(self):
        self._pre_setup()

    def _pre_setup(self):
        self._fixture_setup()

    def _fixture_setup(self):
        create_all_for_test()

        if hasattr(self, 'fixtures'):
            load_data(self.fixtures)

def load_data():
    pass

