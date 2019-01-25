#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import paramiko

hostname = '192.168.10.101'
username = 'root'
password = '666666'
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
#上传文件
    sftp.put("/home/user/info.db","/data/user/info.db")
#下载文件
    sftp.get("/data/user/info1.db","/home/user/info1.db")
#创建目录
    sftp.mkdir("/home/userdir", 0o755)
#删除目录
    sftp.rmdir("/home/userdir")
#文件重命名
    sftp.rename("/home/test.sh","/home/testfile.sh")
#打印文件信息
    print (sftp.stat("/home/testfile.sh"))
#打印目录列表
    print (sftp.listdir("/home"))
    t.close();
except Exception as e:
    print (str(e))

