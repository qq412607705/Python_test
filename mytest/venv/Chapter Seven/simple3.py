#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

from fabric import *

def host_typr():
    run('uname -s')
