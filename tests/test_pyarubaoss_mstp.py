# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.mstp import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetMSTP(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_mstp(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password)
        status = get_mstp(auth)
        self.assertIs(type(status), dict)
        if 'message' in status:
            self.assertNotEqual(status['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetMSTPPorts(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_mstp_ports(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password, version=version)
        status = get_mstp_port(auth)
        self.assertIs(type(status), list)
        if 'message' in status:
            self.assertNotEqual(status['message'], 'Error 404: Not Found.')
        auth.logout()