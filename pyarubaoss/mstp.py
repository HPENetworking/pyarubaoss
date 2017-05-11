#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_mstp(auth):
    headers = {'cookie': auth.cookie}
    url_mstp = "http://" + auth.ipaddr + "/rest/v1/mstp"
    r = requests.get(url_mstp, headers=headers)
    mstp = json.loads(r.text)
    return mstp

def get_mstp_port(auth):
    headers = {'cookie': auth.cookie}
    url_mstp_port = "http://" + auth.ipaddr + "/rest/v1/mstp/port"
    r = requests.get(url_mstp_port, headers=headers)
    mstp_port = json.loads(r.text)
    return mstp_port