#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import *
from fabric.colors import *
import time

env.user = 'root'
env.roledefs = {
    'webservers': ['192.168.10.100','192.168.10.101'],
    'dbserver': ['192.168.10.102']
}
env.hosts = ['192.168.10.100','192.168.10.101']
env.passwords = {
    'root@192.168.10.100:22': '666666',
    'root@192.168.10.101:22': '666666',
    'root@192.168.10.102:22': '666666',
    'root@39.104.162.125:22': 'Qq15538698678'
}

env.project_dev_source = '/data/dev/Lwebadmin/'      #开发机项目主目录
env.project_tar_source = '/data/dev/releases/'      #开发机项目压缩包存储目录
env.project_pack_name = 'release'                   #项目压缩包名前缀，文件名为release.tar.gz

env.deploy_project_root = '/data/www/Lwebadmin'     #项目生产环境主目录
env.deploy_release_dir = 'release'
env.deploy_current_dir = 'current'
env.deploy_version = time.strftime("%Y%m%d")+"v2"   #版本号

@runs_once
def input_versionid():      #获得用户输入的版本号，以便做版本回滚操作
    return prompt("Please input project rollback version ID:",default="")

@task
@runs_once
def tar_source():       #打包本地项目主目录，并将压缩包存储到本地压缩目录
    print (yellow("Creating source package..."))
    with lcd(env.project_dev_source):
        local("tar -czf %s.tar.gz ." % (env.project_tar_source + env.project_pack_name))
    print (green("Creating source package sucess!"))

@task
def put_package():      #上传任务函数
    print (yellow("Start put package..."))
    with settings(warn_only=True):
        with cd(env.deploy_project_root + env.deploy_release_dir):
            run("mkdir %s" % (env.deploy_version))      #创建版本目录
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version
    with settings(warn_only=True):  #上传项目压缩包至此目录
        result = put(env.project_tar_source + env.project_pack_name +".tar.gz",env.deploy_full_path)
    if result.failed and not("put file failed,Continue[Y/N]?"):
        abort("Aborting file put task!")

    with cd(env.deploy_full_path):      #成功解压后删除压缩包
        run("tar -zxvf %s.tar.gz" % (env.project_pack_name))
        run("rm -rf %s.tar.gz" % (env.project_pack_name))

    print (green("Put & untar package success!"))

@task
def make_symlink():     #为当前版本目录做软连接
    print (yellow("update current symlink"))
    env.deploy_full_path=env.deploy_project_root + env.deploy_release_dir + "/"+env.deploy_version
    with settings(warn_only=True):      #删除软连接，重新创建并指定软连接目录，新版本生效
        run("rm -rf %s" % (env.deploy_project_root + env.deploy_current_dir))
        run("ln -s %s %S" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
    print (green("make symlink success!"))

@task
def rollback():     #版本回滚任务函数
    print (yellow("rollback project version..."))
    versionid = input_versionid()       #获得用户输入的回滚版本号
    if versionid=='':
        abrot("Project version ID error,abort!")

    env.deploy_full_path=env.deploy_project_root + env.deploy_release_dir +"/"+versionid
    run("rm -f %s" % env.deploy_project_root + env.deploy_current_dir)
    run("ln -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))  #删除软连接，重新创建并指定软连接目录，新版本生效
    print (green("rollback success!"))

@task
def go():       #自动化程序版本发布入口函数
    tar_source()
    put_package()
    make_symlink()





