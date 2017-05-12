# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.ports import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetPortStatistics(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_port_stats(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password, version=version)
        port_stats = get_port_stats(auth)
        self.assertIs(type(port_stats), list)
        if 'message' in port_stats:
            self.assertNotEqual(port_stats['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetPorts(TestCase):
    """
    Test Case for pyarubaaoss ports get ports function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_ports(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password, version=version)
        ports = get_ports(auth)
        self.assertIs(type(ports), list)
        if 'message' in ports:
            self.assertNotEqual(ports['message'], 'Error 404: Not Found.')
        auth.logout()