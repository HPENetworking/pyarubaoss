#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_poe_ports(auth):
    headers = {'cookie': auth.cookie}
    url_poe = "http://" + auth.ipaddr + "/rest/v1/poe/ports"
    r = requests.get(url_poe, headers=headers)
    poe_ports = json.loads(r.text)
    return poe_ports