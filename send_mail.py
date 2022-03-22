# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : send_mail.py
import smtplib  #发送邮件模块
from email.mime.text import MIMEText  #定义邮件内容
from email.mime.multipart import MIMEMultipart  #用于传送附件
from find_mailfile import FindNewFile
import time
import config

def send_email(casename):
    #发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    #发送邮箱用户名密码
    user = '214848917@qq.com'
    password = 'yenjupcbkqnwbjea'
    #发送和接收邮箱
    sender = '214848917@qq.com'
    #receives = ['fanghua@dangdang.com']
    #receives=['fanghua@dangdang.com','dushuang@dangdang.com']
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    #发送邮件主题和内容
    subject = day + casename + 'API测试报告'
    content = '<html><h1 style="color:red">' + casename + day + '测试报告请参见附件，谢谢！' + '</h1></html>'
    reportfile = FindNewFile().find_NewFile('test_Report')
    #构造附件内容：定义附件，构造附件内容
    send_file = open(reportfile, 'rb').read()  #'rb'表示r读取，b表示二进制方式读取

    att = MIMEText(send_file, 'base64', 'utf-8')  #调用传送附件模块，传送附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="%sreport.html"' % day  #附件描述外层要用单引号

    #构建发送与接收信息
    msgRoot = MIMEMultipart()  #发送附件的方法定义为一个变量
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))  #发送附件的方法中嵌套发送正文的方法
    msgRoot['subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(config.receives)
    msgRoot.attach(att)  #添加附件到正文中

    #SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    #HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    #服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录邮箱服务器用户名和密码
    smtp.login(user, password)
    print("Start send email...")
    smtp.sendmail(sender, config.receives, msgRoot.as_string())
    smtp.quit()
    print("Send End！")


if __name__ == '__main__':
    send_email()