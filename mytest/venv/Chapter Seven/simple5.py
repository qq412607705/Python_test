#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import *

env.user = 'root'
env.gateway = '192.168.10.100'  #定义堡垒机IP，作为上传、执行的中转设备
env.hosts = ['192.168.10.100','192.168.10.101']
env.passwords = {
    'root@192.168.10.100:22': '666666',
    'root@192.168.10.101:22': '666666',
    'root@39.104.162.125:22': 'Qq15538698678'
}

@task
@runs_once
def tar_task():     #本地打包任务函数，只执行一次
    with lcd("/data/logs"):
        locals("tar -czf access.tar.gz access.log")

@task
def put_task():     #上传文件任务函数
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        result = put("/data/logs/access.tar.gz","/data/logs/access.tar.gz")
    if result.failed and not confirm("put file failed,Continue[Y/N]?"):
        abort("Aborting file put task!")    #出现异常时，确认用户是否继续，（Y继续）
@task
def check_task():   #校验文件任务函数
    with settings(warn_only=True):
        #本地local命令需要配置capture=True才能捕获返回值
        lmd5=local("md5sum /data/logs/access.tar.gz",capture=True).split(' ')[0]
        rmd5=run("md5sum /data/logs/access.tar.gz").split(' ')[0]
    if lmd5==rmd5:  #对比本地及远程文件md5信息
        print ("OK")
    else:
        print ("ERROR")

@task
def go():
    tar_task()
    put_task()
    check_task()