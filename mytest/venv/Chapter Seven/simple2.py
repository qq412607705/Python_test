#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *

env.passwords = {
    'root@192.168.10.100:22': '666666',
    'root@192.168.10.101:22': '666666',
    'root@39.104.162.125:22': 'Qq15538698678'
}
env.roledefs = {
    'webservers':['192.168.10.100','192.168.10.101'],
    'dbservers':['39.104.162.125']
}

@roles('webservers')
def webtssk():
    run('yum update')
Qq
@roles('dbservers')
def dbtask():
    run('netstat -napt')

@roles('webservers','dbservers')
def pubclitask():
    run('uptime')

def deploy():
    execute(webtssk)
    execute(dbtask)
    execute(pubclitask)