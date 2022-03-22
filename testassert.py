# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : testassert.py
from analysis import analysis_dict,analysis_xml
from log import LOG,logger
@logger('断言测试结果')
def assert_in(expect,res,responsetype):
    if len(expect.split('=')) > 1:
        data = expect.split(';')
        result = dict([(item.split('=')) for item in data])
        value2=([(str(value)) for value in result.values()])
        try:
            if responsetype.upper()=='JSON':
                value1=([(str(analysis_dict(res,key)[0])) for key in result.keys()])
            elif responsetype.upper()=='XML':
                value1=([(str(analysis_xml(res,key)[0])) for key in result.keys()])
        except Exception as e:
                LOG.info('用例格式或者内容不合法:%s'%e)
                return  {'code':2,'result':'fail','expect':value2,'realdata':'Null'}    
        if value1==value2:
            return  {'code':0,'result':'pass','expect':value2,'realdata':value1}
        else:
            return {'code':1,'result':'fail','expect':value2,'realdata':value1}
    else:
        LOG.info('用例格式或者内容不合法')
        return  {"code":2,'result':'用例格式或者内容不合法'}
