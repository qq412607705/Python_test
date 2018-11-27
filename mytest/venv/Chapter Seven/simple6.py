#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import *

env.user = 'root'
env.roledefs = {
    'webservers': ['192.168.10.100', '192.168.10.101'],
    'dbserver': ['192.168.10.102']
}
env.hosts = ['192.168.10.100', '192.168.10.101']
env.passwords = {
    'root@192.168.10.100:22': '666666',
    'root@192.168.10.101:22': '666666',
    'root@192.168.10.102:22': '666666',
    'root@39.104.162.125:22': 'Qq15538698678'
}


@roles('webservers')  # webtask任务函数引用webservers角色修饰符
def webtask():  # 部署nginx,php,pip-fpm等环境
    print
    yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")


@roles('dbservers')  # dbtask任务函数引用dbserver角色修饰符
def dbtask():  # 部署mysql环境
    print
    yellow("Install mysql mysql-server...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")


@roles('webservers', 'dbservers')  # publictask任务函数同时引用两个角色修饰符
def publictask():
    print
    yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("yum -y install ntp")
        run("rpm -Uvh http://mirrors.kernel.org/fedora-epel/7/x86_64/e/epel-release-7-10.noarch.rpm ")


def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)
