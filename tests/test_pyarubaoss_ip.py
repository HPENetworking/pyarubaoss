# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.ip import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetIPAddresses(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_IPAddresses(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password, version=version)
        ipaddresses = get_ipaddresses(auth)
        self.assertIs(type(ipaddresses), list)
        if 'message' in ipaddresses:
            self.assertNotEqual(ipaddresses['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetIPRoutes(TestCase):
    """
    Test Case for pyarubaaoss ip get ip routes function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_IPRoutes(self):
        """
        test case for get_iproutes

        """
        auth = AOSSAuth(switch, username, password, version=version)
        iproutes = get_iproutes(auth)
        self.assertIs(type(iproutes), list)
        if 'message' in iproutes:
            self.assertNotEqual(iproutes['message'], 'Error 404: Not Found.')
        auth.logout()
