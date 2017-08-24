#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

def get_system(auth):
    url_system = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system"
    try:
        r = requests.get(url_system, headers=auth.cookie)
        system = json.loads(r.text)
        return system
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system: An Error has occured"

def get_system_status(auth):
    url_status = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status"
    try:
        r = requests.get(url_status, headers=auth.cookie)
        status = json.loads(r.text)
        return status
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_status: An Error has occured"

def get_system_status_switch(auth):
    url_status = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/switch"
    try:
        r = requests.get(url_status, headers=auth.cookie)
        switch_status = json.loads(r.text)
        return switch_status
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_status_switch: An Error has occured"

def get_system_cpu(auth):
    url_cpu = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/cpu"
    try:
        r = requests.get(url_cpu, headers=auth.cookie)
        cpu = json.loads(r.text)
        return cpu
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_cpu: An Error has occured"

def get_system_memory(auth):
    url_memory = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/memory"
    try:
        r = requests.get(url_memory, headers=auth.cookie)
        memory = json.loads(r.text)
        return memory
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"


def get_system_storage(auth):
    url_storage = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/status/storage"
    try:
        r = requests.get(url_storage, headers=auth.cookie)
        storage = json.loads(r.text)
        return storage
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_system_storage: An Error has occured"


def get_system_time(auth):
    url_time = "http://" + auth.ipaddr + "/rest/"+auth.version+"/system/time"
    try:
        r = requests.get(url_time, headers=auth.cookie)
        time = json.loads(r.text)
        return time
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"


### LLDP Section

def get_lldp_neigh(auth):
    url_lldp_neigh = "http://" + auth.ipaddr + "/rest/"+auth.version+"/lldp/remote-device"
    try:
        r = requests.get(url_lldp_neigh, headers=auth.cookie)
        neigh = json.loads(r.text)['lldp_remote_device_element']
        return neigh
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_lldp_neigh: An Error has occured"
