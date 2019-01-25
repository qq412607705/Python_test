#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import paramiko
import os,sys,time

#定义堡垒机的信息
blip = "192.168.10.100"
bluser = "root"
blpassword = "666666"

#服务主机信息
hostname = "39.104.162.125"
username = "root"
password = "Qq15538698678"

port = 22
#输入服务器密码的前标志串
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

#ssh登录堡垒机
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=username,password=blpassword)

#创建会话，开启命令调用
channel = ssh.invoke_shell()
#会话命令执行超时时间，单位为秒
channel.settimeout(10)

buff = ' '
resp = ' '
#执行ssh登录业务主机
channel.send('ssh '+username+'@'+hostname+'\n')
#ssh登录的提示信息判断，输出串尾含有“\s password:"时，退出while循环
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print ('Error info:%s connection time.' %(str(e)))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
#输出串尾含有“yes/no”时，发送“yes”并回车
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
        buff=''

#发送业务主机密码
channel.send(password+'\n')

buff=''
#输出串尾为#时说明校验通过并退出while循环
while not buff.endswith('# '):
    resp = channel.recv(9999)
#输出串尾含有“\'s password: ”时，说明密码不正确，要求重新输入
    if not resp.find(passinfo)==-1:
        print ('Error info: Authentication failed')
#关闭连接对象后退出
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp

#认证通过后发送ifconfig命令查看结果
channel.send('ifconfig\n')
buff = ''
try:
    while buff.find('# ')==-1:
        resp = channel.recv(9999)
        buff += resp
except Exception as e:
    print ("Error info:"+str(e))
print (buff)
channel.close()
ssh.close()











