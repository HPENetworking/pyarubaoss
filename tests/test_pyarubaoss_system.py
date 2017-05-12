# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.system import *
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
        auth = AOSSAuth(switch, username, password, version=version)
        system = get_system(auth)
        self.assertIs(type(system), dict)
        if 'message' in system:
            self.assertNotEqual(system['message'], 'Error 404: Not Found.')
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
        auth = AOSSAuth(switch, username, password, version=version)
        status = get_system_status(auth)
        self.assertIs(type(status), dict)
        if 'message' in status:
            self.assertNotEqual(status['message'], 'Error 404: Not Found.')
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
        auth = AOSSAuth(switch, username, password, version=version)
        switch_status = get_system_status_switch(auth)
        self.assertIs(type(switch_status), dict)
        if 'message' in switch_status:
            self.assertNotEqual(switch_status['message'], 'Error 404: Not Found.')
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
        if skiptest is True:
            raise SkipTest
        auth = AOSSAuth(switch, username, password, version=version)
        cpu = get_system_cpu(auth)
        self.assertIs(type(cpu), dict)
        if 'message' in cpu:
            self.assertNotEqual(cpu['message'], 'Error 404: Not Found.' )
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
        if skiptest is True:
            raise SkipTest
        auth = AOSSAuth(switch, username, password, version=version)
        memory = get_system_memory(auth)
        self.assertIs(type(memory), dict)
        if 'message' in memory:
            self.assertNotEqual(memory['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetSystemStorage(TestCase):
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
        if skiptest is True:
            raise SkipTest
        auth = AOSSAuth(switch, username, password, version=version)
        storage = get_system_storage(auth)
        self.assertIs(type(storage), dict)
        if 'message' in storage:
            self.assertNotEqual(storage['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetSystemTime(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_system_time(self):
        """
        test case for get_system_memory

        """
        auth = AOSSAuth(switch, username, password, version=version)
        time = get_system_time(auth)
        self.assertIs(type(time), dict)
        if 'message' in time:
            self.assertNotEqual(time['message'], 'Error 404: Not Found.')
        auth.logout()


class TestGetLLDPNeigh(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass

    def test_get_lldp_neigh(self):
        """
        test case for get_system_memory

        """
        auth = AOSSAuth(switch, username, password, version=version)
        neigh = get_lldp_neigh(auth)
        self.assertIs(type(neigh), list)
        if 'message' in neigh:
            self.assertNotEqual(neigh['message'], 'Error 404: Not Found.')
        auth.logout()