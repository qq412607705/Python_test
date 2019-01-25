#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import *

env.user = 'root'
env.gateway = '192.168.10.100'  # 定义堡垒机IP，作为上传、执行的中转设备
env.hosts = ['192.168.10.100', '192.168.10.101']
env.passwords = {
    'root@192.168.10.100:22': '666666',
    'root@192.168.10.101:22': '666666',
    'root@39.104.162.125:22': 'Qq15538698678'
}

lpackpath = "/root/download/lnmp0.9.tar.gz"  # 本地安装包路径
rpackpath = "/tmp/install"  # 远程安装包路径


@task
def put_task():
    run("mkdir -p /tmp/install")
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)  # 上传安装包
    if result.failed and not confirm("put file failed,Continue[Y/N]?"):
        abort("Aborting file put task!")


@task
def run_task():  # 执行远程命令，安装lnmp环境
    with cd("/tmp/install"):
        run("tar -zvxf lnmp0.9.tar.gz")
        with cd("lnmp0.9/"):  # 使用with继续继承/tmp/install目录位置状态
            run("./centos.sh")


@task
def go():  # 上传、安装
    put_task()
    run_task()
