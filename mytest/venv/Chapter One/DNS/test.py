#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import httplib
import os
import dns.resolver


iplist = []  # 定义域名IP列表变量
# appdomain = "www.google.com.hk"  # 定义业务域名
appdomain = "www.baidu.com"  # 定义业务域名

# 域名解析函数，解析成功IP将追加到iplist
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')  # 解析A记录类型
    except Exception, e:
        print "dns resolver error:" + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j)  # 追加到iplist
    return True


def checkip(ip):
    checkurl = str(ip) + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)  # 定义http连接超时时间(5秒)
    conn = httplib.HTTPConnection(checkurl)  # 创建http连接对象

    try:
        conn.request("GET", "/", headers={"Host": appdomain})  # 发起URL请求，添加host主机头
        r = conn.getresponse()
        getcontent = r.read(15)  # 获取URL页面前15个字符，以便做可用性校验
    finally:
        if getcontent.lower() == "<!doctype html>":  # 监控URL页的内容一般是事先定义好，比如“HTTP200”等
            print str(ip) + " [OK]"
        else:
            print str(ip) + " [Error]"  # 此处可放告警程序，可以是邮件、短信通知


if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:  # 条件：域名解析正确且至少要返回一个IP
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."