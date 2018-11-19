#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import paramiko

hostname = '192.168.10.101'
username = 'root'
password = '666666'

#发送paramiko日志到syslogin文件
paramiko.util.log_to_file('syslogin.log')
#创建一个ssh客户端client对象
ssh = paramiko.SSHClient()
#获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定
ssh.load_system_host_keys()
#若主机没有使用密钥进行验证，则自动选择密码进行验证登录
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#创建ssh连接
ssh.connect(hostname=hostname,username=username,password=password)
#调用远程执行命令方法exec_command（）
stdin,stdout,stderr=ssh.exec_command('free -m')
#打印命令执行结果，得到Python列表形式，可以使用stdout.readlines()
print stdout.read()
#关闭ssh连接
ssh.close()

