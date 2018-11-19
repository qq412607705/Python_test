#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import smtplib
from email.mime.multipart import MIMEMultipart      #导入 MIMEMultipart类
from email.mime.text import MIMEText        #导入 MIMEText类
from email.mime.image import MIMEImage      #导入MIMEImage 类

HOST = "smtp.163.com"     #定义smtp主机
SUBJECT = "Test email from python"      #定义邮件的主题
TO = "412607705@qq.com"     #定义收件人
FROM = "15538698678@163.com"      #定义发件人

def addimg(src, imgid):      #添加图片函数，参数1：图片路径，参数2：图片ID
    fp = open(src, 'rb')        #打开文件
    msgImage = MIMEImage(fp.read())     #创建MIMEImage对象，读取图片内容并作为参数
    fp.close()      #关闭文件
    msgImage.add_header('Content-ID', imgid)    #指定图片文件的Content-ID，img标签src用到
    return msgImage     #返回msgImage 对象
msg = MIMEMultipart('related')      #创建MIMEMultipart对象，采用related定义内嵌资源的邮件体

msgtext = MIMEText("""      #创建一个MIMEText对象，分别指定HTML内容、类型（文本或HTML）、字符编码
    <table width ="600" border="0" cellspacing="0" cellpadding="4">
        <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
            <td colspan=2>* 官网数据    <a href="monitor.domain.com">更多>></a></td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:io">
            </td>
            <td>
                <img src="cid:key_hit">
            </td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
            <img src="cid:men">
            </td>
            <td>
            <img src="cid:swap">
            </td>
        </tr>
    </table>""","html","utf-8")     #<img>标签的src属性是通过Content-ID来引用的
msg.attach(msgtext)     #MIMEMultipart对象附加MIMEText的内容
msg.attach(addimg("img/bytes_io.png","io"))     #使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_men.png","men"))
msg.attach(addimg("img/os_swap.png","swap"))
msg['Subject'] = SUBJECT       # 邮件主题
msg['from'] = FROM      #邮件发件人，邮件头部可见
msg['To'] = TO      #邮件收件人，邮件头部可见
try:
    server = smtplib.SMTP()  # 创建一个SMTP()对象
    server.connect(HOST, "25")  # 通过connect方法连接smtp主机
    server.starttls()  # 启动安全模式
    server.login("15538698678@163.com", "qq412607705")  # 邮箱账号登录校验
    server.sendmail(FROM, TO, BODY)  # 邮件发送
    server.quit()  # 断开smtp连接
    print "邮件发送成功"
except  Exception,e:
    print "失败:" + str(e)

