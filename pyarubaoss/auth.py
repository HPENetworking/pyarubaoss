#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

class AOSSAuth():
    """
    This class requests and stores an authentication cookie for the Aruba AOS
    Switch Software.
    """
    def __init__(self, switchip, username, password):
        url_login = "http://" + switchip + "/rest/v1/login-sessions"
        payload_login = '{\"userName\": \"' + username + '\", \"' + password + '\": \"password\"}"'
        get_cookie = requests.request("POST", url_login, data=payload_login)
        r_cookie = get_cookie.json()['cookie']
        self.cookie = r_cookie
        self.ipaddr = switchip


    def logout(self):
        url_login = "http://" + self.ipaddr + "/rest/v1/login-sessions"
        headers = {'cookie': self.cookie}
        r = requests.delete(url_login, headers=headers)
        return r.status_code






