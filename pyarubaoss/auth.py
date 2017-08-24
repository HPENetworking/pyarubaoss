#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

class AOSSAuth():
    """
    This class requests and stores an authentication cookie for the Aruba AOS
    Switch Software.
    """
    def __init__(self, switchip, username, password, version="v3"):
        url_login = "http://" + switchip + "/rest/v1/login-sessions"
        payload_login = {"userName": username, "password": password}
        s = requests.Session()
        response = s.post(url_login, data=json.dumps(payload_login), timeout=1)
        print(response.text)
        print(response.json()["cookie"])
        #  r_cookie = get_cookie.json()['cookie']
        self.cookie = {'cookie': response.json()["cookie"]}
        self.ipaddr = switchip
        self.version = version


    def logout(self):
        url_login = "http://" + self.ipaddr + "/rest/v1/login-sessions"
        r = requests.delete(url_login, headers=self.cookie)
        return r.status_code



