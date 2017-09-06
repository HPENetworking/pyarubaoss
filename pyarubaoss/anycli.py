#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, base64


def post_cli(auth, command):
    url_cli = "http://" + auth.ipaddr + "/rest/" + auth.version + "/cli"
    command_dict = {"cmd": command}
    try:
        post_command = requests.post(url_cli, headers=auth.cookie, data=json.dumps(command_dict))
        cli_response = post_command.json()['result_base64_encoded']
        decoded_response = base64.b64decode(cli_response).decode('utf-8')
        return decoded_response
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " post_cli: An Error has occurred"


