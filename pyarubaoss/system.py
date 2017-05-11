#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

def get_system(auth):
    headers = {'cookie': auth.cookie}
    url_system = "http://" + auth.ipaddr + "/rest/v1/system"
    r = requests.get(url_system, headers=headers)
    system = json.loads(r.text)
    return system

def get_system_status(auth):
    headers = {'cookie': auth.cookie}
    url_status = "http://" + auth.ipaddr + "/rest/v1/system/status"
    r = requests.get(url_status, headers=headers)
    status = json.loads(r.text)
    return status

def get_system_status_switch(auth):
    headers = {'cookie': auth.cookie}
    url_status = "http://" + auth.ipaddr + "/rest/v1/system/status/switch"
    r = requests.get(url_status, headers=headers)
    switch_status = json.loads(r.text)
    return switch_status

def get_system_cpu(auth):
    headers = {'cookie': auth.cookie}
    url_cpu = "http://" + auth.ipaddr + "/rest/v1/system/status/cpu"
    r = requests.get(url_cpu, headers=headers)
    cpu = json.loads(r.text)
    return cpu

def get_system_memory(auth):
    headers = {'cookie': auth.cookie}
    url_memory = "http://" + auth.ipaddr + "/rest/v1/system/status/memory"
    r = requests.get(url_memory, headers=headers)
    memory = json.loads(r.text)
    return memory


def get_system_storage(auth):
    headers = {'cookie': auth.cookie}
    url_storage = "http://" + auth.ipaddr + "/rest/v1/system/status/storage"
    r = requests.get(url_storage, headers=headers)
    storage = json.loads(r.text)
    return storage


def get_system_time(auth):
    headers = {'cookie': auth.cookie}
    url_time = "http://" + auth.ipaddr + "/rest/v1/system/time"
    r = requests.get(url_time, headers=headers)
    time = json.loads(r.text)
    return time