#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import http.client
import os
import dns.resolver

iplist = []  # 定义域名IP列表变量
appdomain = "www.google.cn"  # 定义业务域名


def get_iplist(domain=""):  # 域名解析函数，解析成功IP将被追加到iplist
    try:
        A = dns.resolver.query(appdomain, 'A')  # 解析A记录类型
    except Exception as e:
        print ("dns resolver error:" +str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)        # 追加到iplist
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    code=None
    http.client.socket.setdefaulttimeout(5)             # 定义http连接超时时间（5秒）
    conn=http.client.HTTPConnection(checkurl)    # 创建http连接对象

    try:
        conn.request("GET", "/",headers = {"Host": appdomain})      # 发起url请求，添加host主机头
        r=conn.getresponse()
        getcontent = r.read(15)         # 获取url页面前15个字符，以便做可用性校验
        code=r.code
    finally:
        if getcontent == "<!DOCTYPE html>":      # 监控url页的内容一般是事先定义好的，比如http2.0等
            print (ip+" [OK]")
        elif code in [200,301,302]:                 #正常状态码
            print(ip + " [OK]")
        else:
            print (ip+" [Error]")      #此处可放告警程序，可以是邮件、短信通知

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist) > 0:       # 条件：域名解析正确且至少返回一个IP
        for ip in iplist:
            checkip(ip)
    else:
        print ("dns resolver error.")
