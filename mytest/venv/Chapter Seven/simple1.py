#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.100.100','192.168.100.101']
env.password = '666666'

@runs_once  #主机遍历过程中，只有第一台出发此函数
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
        run("ls -l "+dirname)

@task       #限定只有go函数对fab命令可见
def go():
    getdirname = input_raw()
    worktask(getdirname)

