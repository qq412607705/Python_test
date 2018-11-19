#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import sys
import pexpect


child = pexpect.spawn('ssh root@192.168.10.101')
#fout = file('mylog.txt','w')
#child.logfile = fout
child.logfile = sys.stdout

child.expect("password:")
child.sendline("666666")
child.expect('#')
child.sendline('ls -lh /root')
child.expect('#')