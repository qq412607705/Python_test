#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import paramiko
import os

hostname = '192.168.10.101'
username = 'root'
password = '666666'

#发送paramiko日志到syslogin文件
paramiko.util.log_to_file('syslogin.log')
#创建一个ssh客户端client对象
ssh = paramiko.SSHClient()
#自动添加主机名及主机密钥到本地Hostkey
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#定义密钥存放路径
privatekey = os.path.expanduser('~/.ssh/id_rsa')
#创建密钥对象key
key = paramiko.RSAKey.from_private_key_file(privatekey)
#创建ssh连接
ssh.connect(hostname=hostname,username=username,pkey = key)
#调用远程执行命令方法exec_command（）
stdin,stdout,stderr=ssh.exec_command('free -m')
#打印命令执行结果，得到Python列表形式，可以使用stdout.readlines()
print stdout.read()
#关闭ssh连接
ssh.close()

