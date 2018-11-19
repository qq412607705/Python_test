#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import pexpect
import sys
from pexpect import *

ip = "192.168.10.101"       #定义目标主机
user = "root"               #目标主机用户
passwd = "666666"           #目标主机密码
target_file = "/root/111.txt"       #目标主机文件

child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip])         #运行ssh命令
fout = file('mylog.txt','w')        #输入、输出日志写入mylog.txt文件
child.logfile = fout

try:
    child.expect('(?i)password')        #匹配password字符串，（？i）表示不区别大小写
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /root/111.tat.gz '+ target_file)       #打包文件
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:         #定义EOF异常处理
    print "expect EOF"
except TIMEOUT:     #定义TIMEOUT异常处理
    print "expect TIMEOUT"

#启动scp远程拷贝命令，实现将打包好的文件复制到本地/home目录
child = pexpect.spawn('/usr/bin/scp' [user+'@'+ip +':/root/111.tar.gz' ,'/home'])
fout = file('mylog.txt','a')
child.logfile = fout

try:
#   child.expect('(?i)password')
#   child.sendline(passwd)
    child.expect(pexpect.EOF)       #匹配缓冲区EOF（结尾），保证文件复制正常完成
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect timeout"








