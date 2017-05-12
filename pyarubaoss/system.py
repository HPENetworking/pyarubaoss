#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

def get_system(auth):
    headers = {'cookie': auth.cookie}
    url_system = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system"
    try:
        r = requests.get(url_system, headers=headers)
        system = json.loads(r.text)
        return system
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system: An Error has occured"

def get_system_status(auth):
    headers = {'cookie': auth.cookie}
    url_status = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status"
    try:
        r = requests.get(url_status, headers=headers)
        status = json.loads(r.text)
        return status
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_status: An Error has occured"

def get_system_status_switch(auth):
    headers = {'cookie': auth.cookie}
    url_status = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/switch"
    try:
        r = requests.get(url_status, headers=headers)
        switch_status = json.loads(r.text)
        return switch_status
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_status_switch: An Error has occured"

def get_system_cpu(auth):
    headers = {'cookie': auth.cookie}
    url_cpu = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/cpu"
    try:
        r = requests.get(url_cpu, headers=headers)
        cpu = json.loads(r.text)
        return cpu
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_cpu: An Error has occured"

def get_system_memory(auth):
    headers = {'cookie': auth.cookie}
    url_memory = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/memory"
    try:
        r = requests.get(url_memory, headers=headers)
        memory = json.loads(r.text)
        return memory
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"


def get_system_storage(auth):
    headers = {'cookie': auth.cookie}
    url_storage = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/storage"
    try:
        r = requests.get(url_storage, headers=headers)
        storage = json.loads(r.text)
        return storage
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_storage: An Error has occured"


def get_system_time(auth):
    headers = {'cookie': auth.cookie}
    url_time = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/time"
    try:
        r = requests.get(url_time, headers=headers)
        time = json.loads(r.text)
        return time
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"


### LLDP Section

def get_lldp_neigh(auth):
    headers = {'cookie': auth.cookie}
    url_lldp_neigh = "http://" + auth.ipaddr + "/rest/"+auth.version+"/lldp/remote-device"
    try:
        r = requests.get(url_lldp_neigh, headers=headers)
        neigh = json.loads(r.text)['lldp_remote_device_element']
        return neigh
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"
