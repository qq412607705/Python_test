#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import sys
import pexpect

ip = "39.104.162.125"
name = "root"
pwd = "Qq15538698678"

child = pexpect.spawn('ssh% user@xxx%s'%(name,ip))
#fout = file('mylog.txt','w')
#child.logfile = fout
child.logfile = sys.stdout

child.expect('password:')
child.sendline(pwd)
child.expect('#')
child.sendline('ls -lh /root')
child.expect('#')