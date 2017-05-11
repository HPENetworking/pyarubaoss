# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaaoss.auth import *
from pyarubaaoss.system import *
from test_machine import *


# TODO Remarked out failing tests

class TestGetSystem(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password)
        system = get_system(auth)
        self.assertIs(type(system), dict)
        auth.logout()


class TestGetSystemStatus(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_status(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password)
        status = get_system_status(auth)
        self.assertIs(type(status), dict)
        auth.logout()


class TestGetSystemStatusSwitch(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_status_switch(self):
        """
        test case for get_system

        """
        auth = AOSSAuth(switch, username, password)
        switch_status = get_system_status_switch(auth)
        self.assertIs(type(switch_status), dict)
        auth.logout()


class TestGetSystemCPU(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_cpu(self):
        """
        test case for get_system_cpu

        """
        auth = AOSSAuth(switch, username, password)
        cpu = get_system_cpu(auth)
        self.assertIs(type(cpu), dict)
        auth.logout()


class TestGetSystemMemory(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_memory(self):
        """
        test case for get_system_memory

        """
        #if skiptest is True:
         #   raise SkipTest
        auth = AOSSAuth(switch, username, password)
        memory = get_system_memory(auth)
        self.assertIs(type(memory), dict)
        auth.logout()


class TestGetSystemMemory(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_storage(self):
        """
        test case for get_system_memory

        """
        auth = AOSSAuth(switch, username, password)
        storage = get_system_storage(auth)
        self.assertIs(type(storage), dict)
        auth.logout()