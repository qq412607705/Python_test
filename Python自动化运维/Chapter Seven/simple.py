#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.10.100', '192.168.10.101']
env.password = '666666'


@runs_once  # 检查本地系统信息，当有多台主机时，只运行一次
def local_task():  # 本地任务函数
    local("uname -a")


def remote_task():
    with cd("/home"):  # “with”的作用是让后面的表达式的语句继承当前状态，实现“cd /root/download&&ls -l”的效果
        run('ls -l')
