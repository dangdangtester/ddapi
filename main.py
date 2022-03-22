# -*- coding: utf-8 -*-
# @Date    : 2020-06-02 21:54:08
# @Author  : fh
# @File    : main.py
'''主函数'''
from runcases import runcases
from py_Html import *
from send_mail import send_email
import os,datetime,time
import config

if __name__ == '__main__':
    for casefiles in config.casefiles:
        starttime = datetime.datetime.now()
        #执行用例
        pass_cases,fail_cases,error_cases = runcases(config.casepaths + casefiles)
        casename = os.path.basename(config.casepaths + casefiles).split('.')[0]
        endtime = datetime.datetime.now()
        #拼接报告主体
        relus = result_msg(pass_cases)+result_msg(fail_cases)+result_msg(error_cases)
        #生成报告
        report_html = fullhtml(titles,starttime,endtime,len(pass_cases),len(fail_cases),len(error_cases),relus)
        day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        filepath =os.path.join('test_Report\\%s-result.html' % day)
        createhtml(report_html,filepath)
        #发送邮件
        send_email(casename)


