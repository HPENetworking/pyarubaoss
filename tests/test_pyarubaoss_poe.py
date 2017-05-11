# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.poe import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetPOEPorts(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_POE_Ports(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password)
        ports = get_poe_ports(auth)
        self.assertIs(type(ports), list)
        if 'message' in ports:
            self.assertNotEqual(ports['message'], 'Error 404: Not Found.')
        auth.logout()

