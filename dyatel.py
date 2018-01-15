#!/usr/bin/env python

import os
import time
import requests
from yaml import load, dump
import subprocess


def check_exists_file(filename):
    return os.path.exists(filename)


filename = os.getenv('DYATEL_CONFIG', '/etc/dyatel/default.yaml')

if not check_exists_file(filename):
    exit('Config file not exists: {}'.format(filename))


config = load(open(filename, 'r').read())
status = {}


def do_main_program(config):
    while True:
        for task in config:
            for check in task['task']:
                print(check)
                check_http(check)
    return True

def check_http(c):
    url = c['url']
    method = c['method']
    data = c.get('data', {})
    name = c['name']
    expection = c['expectation']
    exception = c['exception']
    action = c['action']
    pause = c.get('pause', 1)

    while True:
        if method == 'post':
            response = requests.post(url)
        else:
            response = requests.get(url)

        if name not in status:
            status[name] = 0

        #print(type(expection['status']))

        if type(expection['status']) == int:
            if response.status_code == expection['status']:
                status[name] = 0
            else:
                status[name] += 1
        if type(expection['status']) == list:
            if response.status_code in expection['status']:
                status[name] = 0
            else:
                status[name] += 1
        #print(expection['status'])

        #print(response.status_code)
        #print(status)

        if status[name] >= exception['count']:
            #print(action['command'])
            subprocess.Popen([action['command']], shell=True)
            status[name] = 0
            time.sleep(action.get('pause', 30))
        time.sleep(pause)
        break
    return True

do_main_program(config)

