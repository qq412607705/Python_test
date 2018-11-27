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

tmpdir = "/tmp"
remotedir = "/root"
#本地源文件路径
localpath = "/root/111.txt"
#堡垒机临时路径
tmppath = tmpdir+"/111.txt"
#业务主机目标路径
remotepath = remotedir+"/111.txt"
port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogn.log')
t = paramiko.Transport(blip,port)
t.connect(username=bluser,password=blpassword)
sftp = paramiko.SFTPClient.from_transport(t)
#上传本地源文件到堡垒机临时路径
sftp.put(localpath,tmppath)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,username=username,password=blpassword)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
#scp中转目录文件到目标主机
channel.send('scp '+tmppath+' '+username+'@'+hostname+':'+remotepath+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print ('Error info:%s connection time.' %(str(e)))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
        buff = ' '

channel.send(password+'\n')

buff = ''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:
        print ('Error info: Authentication failed.')
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
print (buff)
channel.close()
ssh.close()



























