#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_mactable(auth):
    """
    Function to get list of mac-addresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mac-addresses
    :rtype list
    """
    url_mactable = "http://" + auth.ipaddr + "/rest/" + auth.version + "/mac-table"
    try:
        r = requests.get(url_mactable, headers=auth.cookie)
        mactable = json.loads(r.text)['mac_table_entry_element']
        return mactable
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mactable: An Error has occurred"


def print_mactable(auth):
    """
    Function to print mac-address, port id and vlan id in a table
    :param auth: AOSSAuth class object returned by pyarubaoss.auth
    :return prints mac-address table
    :rtype string
    """
    mac_table = get_mactable(auth)
    print('-' * 10)
    print('{:>10}{:>15}{:>15}'.format('MAC-address:', 'Port ID:', 'VLAN ID:'))
    for x in mac_table:
        print('{:>10}{:>15}{:>15}'.format(x['mac_address'], x['port_id'], str(x['vlan_id'])))
