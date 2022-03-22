# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : get_excel.py
import xlrd
from log  import LOG,logger
'''
解析excel文件，返回一个数组，数组元素为一条或多条用例，每条用例是一个字典
pip install xlrd==1.2.0
'''
@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[0]
        nrows=me.nrows
        testcases = []
        for i in range(1,nrows):
            testcase = {}
            testcase['id'] = me.cell(i, 0).value
            testcase['name'] = me.cell(i, 1).value
            testcase['url'] = me.cell(i, 2).value
            testcase['paramstype'] = me.cell(i, 3).value.upper()
            testcase['params'] = me.cell(i, 4).value
            testcase['method'] = me.cell(i, 5).value.upper()
            testcase['responsetype'] = me.cell(i, 6).value.upper()
            testcase['expect'] = me.cell(i, 7).value
            testcases.append(testcase)
        return testcases
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return

#ff = datacel('init.xlsx')