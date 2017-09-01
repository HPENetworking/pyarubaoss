#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_ipaddresses(auth):
    """
    Function to get list of ipaddresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of ipaddresses
    :rtype list
    """
    url_ipaddresses = "http://" + auth.ipaddr + "/rest/"+auth.version+"/ipaddresses"
    try:
        r = requests.get(url_ipaddresses, headers = auth.cookie)
        ipaddresses = json.loads(r.text)['ip_address_subnet_element']
        return ipaddresses
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ipaddresses: An Error has occured"


def get_iproutes(auth):
    """
    Function to get list of ip routes from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of ip routes
    :rtype list
    """
    url_iproutes = "http://" + auth.ipaddr + "/rest/"+auth.version+"/ip-route"
    try:
        r = requests.get(url_iproutes, headers = auth.cookie)
        iproutes = json.loads(r.text)['ip_route_element']
        return iproutes
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_iproutes: An Error has occured"
