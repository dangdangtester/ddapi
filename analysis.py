""" 
@author: fh
@file: analysis.py 
@time: 2021/06/09 13:54 
"""
'''通过递归解析返回值'''
from json import loads,dumps
from xml.etree import ElementTree
from log  import LOG,logger

@logger('解析返回值')
def analysis_dict(d,code):
    result=[]
    if isinstance(d, dict) and code in d.keys():
        value = d[code]
        result.append(value)
    elif isinstance(d, (list, tuple)):
            for item in d:
                value=analysis_dict(item,code)
                if value =="None" or value is None:
                    pass
                elif len(value)==0:
                    pass
                else:
                    result.append(value)
    else:
        if isinstance(d, dict):
            for k in d:
                value=analysis_dict(d[k], code)
                if value =="None" or value is None :
                    pass
                elif len(value)==0:
                    pass
                else:
                    for item in value:
                        result.append(item[0])
    return result

def analysis_xml(d,code):
    result=[]
    data = ElementTree.XML(d)
    item=data.find(code).text
    result.append(item)
    return result






















