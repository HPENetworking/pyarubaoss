#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_mstp(auth):
    """
    Function to get dict of mstp global status
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return dict of mstp status
    :rtype dict
    """
    url_mstp = "http://" + auth.ipaddr + "/rest/"+auth.version+"/mstp"
    try:
        r = requests.get(url_mstp, headers=auth.cookie)
        mstp = json.loads(r.text)
        return mstp
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mstp: An Error has occured"

def get_mstp_port(auth):
    """
    Function to get list of mstp port status
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mstp port status
    :rtype dict
    """
    url_mstp_port = "http://" + auth.ipaddr + "/rest/"+auth.version+"/mstp/port"
    try:
        r = requests.get(url_mstp_port, headers=auth.cookie)
        mstp_port = json.loads(r.text)['mstp_port_element']
        return mstp_port
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mstp_port: An Error has occured"