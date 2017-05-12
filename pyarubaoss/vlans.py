#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


### Working with VLANs Directory

def get_vlans(auth):
    headers = {'cookie': auth.cookie}
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans"
    r = requests.get(url_vlans, headers=headers)
    try:
        vlans = json.loads(r.text)['vlan_element']
        return vlans
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_vlans: An Error has occured"


def get_vlan(auth, vlan_id):
    headers = {'cookie': auth.cookie}
    url_vlan = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/" + str(vlan_id)
    r = requests.get(url_vlan, headers=headers)
    try:
        vlan = json.loads(r.text)
        return vlan
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_vlan: An Error has occured"


def create_vlan(auth, vlan_id, vlan_name):
    headers = {'cookie': auth.cookie}
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans"
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + ",\"name\":\"" + vlan_name + "\"}"
    try:
        r = requests.post(url_vlans, data = payload_vlan, headers=headers)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_vlan: An Error has occured"

def modify_vlan(auth, vlan_id, vlan_name):
    headers = {'cookie': auth.cookie}
    url_vlan = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/" + str(vlan_id)
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + ",\"name\":\"" + vlan_name + "\"}"
    try:
        r = requests.put(url_vlan, data=payload_vlan, headers=headers)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " modify_vlan: An Error has occured"

def delete_vlan(auth, vlan_id):
    headers = {'cookie': auth.cookie}
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + "}"
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/"+str(vlan_id)
    try:
        r = requests.delete(url_vlans, data = payload_vlan, headers=headers)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_vlan: An Error has occured"

### Working with VLAN Ports

def get_vlan_ports(auth):
    """
    Bug in Code. Needs to be fixed. Don't use this for now.
    :param auth:
    :return:
    """
    headers = {'cookie': auth.cookie}
    url_vlan_ports = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans-ports/"
    r = requests.get(url_vlan_ports, headers=headers)
    vlan_ports = json.loads(r.text)
    return vlan_ports
