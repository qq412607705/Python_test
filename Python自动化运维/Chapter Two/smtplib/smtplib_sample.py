#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import smtplib
import string

HOST = "smtp.163.com"     #定义smtp主机
SUBJECT = "Test email from python"      #定义邮件的主题
TO = "412607705@qq.com"     #定义收件人
FROM = "15538698678@163.com"      #定义发件人
text = "python rules them all!"     #邮件内容
#组装sendmail方法的邮件主体内容，各段以"\r\n"进行分隔
BODY = str.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ),'\r\n')
try:
    server = smtplib.SMTP()  # 创建一个SMTP()对象
    server.connect(HOST, "25")  # 通过connect方法连接smtp主机
    server.starttls()  # 启动安全模式
    server.login("15538698678@163.com", "qq412607705")  # 邮箱账号登录校验
    server.sendmail(FROM, TO, BODY)  # 邮件发送
    server.quit()  # 断开smtp连接
    print ("邮件发送成功")
except  Exception as e:
    print ("失败:" + str(e))