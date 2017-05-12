# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.mactable import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetMACTable(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_mactable(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password, version=version)
        mactable = get_mactable(auth)
        self.assertIs(type(mactable), list)
        if 'message' in mactable:
            self.assertNotEqual(mactable['message'], 'Error 404: Not Found.')
        auth.logout()

