# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : test_request.py
import requests,json
from log import LOG,logger
'''
API请求，请求方式支持get和post，post请求参数支持json格式和xml，返回json格式
'''
@logger('requests封装')
class requ():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
        self.json_headers = {"Content-Type":"application/json"}
        self.xml_headers = {"Content-Type":"text/xml"}
    def get(self, url,params):#get消息
        try:
            get_url=url+params
            r = requests.get(get_url, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info('get请求出错，出错原因:%s'%e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s'%e}
    def json_post(self, url, params):#json消息
        try:
            r=requests.post(url,data=params,headers=self.json_headers)
            json_response = json.loads(r.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('json_post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}
    def xml_post(self, url, params):#xml消息
        data = json.dumps(params)
        try:
            r =requests.post(url,params=data,headers=self.xml_headers)
            json_response = r.text
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}
