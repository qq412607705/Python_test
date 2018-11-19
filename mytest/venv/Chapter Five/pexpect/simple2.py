#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import sys
import pexpect

try:
    index = p.pexpect(['good','bad'])
    if index == 0:
        do_something()
    elif index == 1 :
        do_something_else()
except EOF:
    do_some_other_thing()
except TIMEOUT:
    do_something_completely_different()