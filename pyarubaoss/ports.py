#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_port_stats(auth):
    """
    Function to get list of port statistics from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of ports statistics
    :rtype list
    """
    headers = {'cookie': auth.cookie}
    url_portstats = "http://" + auth.ipaddr + "/rest/"+auth.version+"/port-statistics"
    try:
        r = requests.get(url_portstats, headers=headers)
        portstats = json.loads(r.text)['port_statistics_element']
        return portstats
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_port_stats: An Error has occured"


def get_ports(auth):
    """
    Function to get list of ports from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of ports
    :rtype list
    """
    headers = {'cookie': auth.cookie}
    url_ports = "http://" + auth.ipaddr + "/rest/"+auth.version+"/ports"
    try:
        r = requests.get(url_ports, headers=headers)
        ports = json.loads(r.text)['port_element']
        return ports
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ports: An Error has occured"