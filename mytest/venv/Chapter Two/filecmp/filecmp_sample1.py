#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import filecmp

a = "/home/test/filecmp/dir1"       #定义左目录
b = "/home/test/filecmp/dir2"       #定义右目录
dirobj = filecmp.dircmp(a,b,['test.py'])             #目录比较，忽略test.py文件
dirobj.report()                                     #比较当前目录中的内容
dirobj.report_partial_closure()                     #比较当前指定目录和第一级子目录的内容
dirobj.report_full_closure()                        #递归比较所有指定目录的内容
print "left_list:" + str(dirobj.left_list)
print "right_list:" + str(dirobj.right_list)
print "common:" + str(dirobj.common)
print "left_only" + str(dirobj.left_only)
print "right_only" + str(dirobj.right_only)
print "common_dirs:" + str(dirobj.common_dirs)
print "common_files:" + str(dirobj.common_files)
print "common_funny:" + str(dirobj.common_funny)
print "same_files:" + str(dirobj.same_files)
print "diff_files:" + str(dirobj.diff_files)
print "funny_files:" + str(dirobj.funny_files)
