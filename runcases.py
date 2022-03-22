# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : runcases.py
'''执行用例'''
from test_requests import requ
from get_excel import datacel
from testassert import assert_in


def runcases(casepath):
    pass_cases = []
    fail_cases = []
    error_cases = []
    print(casepath)
    testcases = datacel(casepath)
    for testcase in testcases:
        all_cases = {}
        id = testcase['id']
        name = testcase['name']
        url = testcase['url']
        #paramstype = testcase['paramstype']
        params = testcase['params']
        method = testcase['method']
        responsetype = testcase['responsetype']
        expect = testcase['expect']
        request = requ()
        if method == 'GET':
            res = request.get(url, params)
        elif method == 'POST':
            res = request.json_post(url, params)
        rescode = res['code']
        response = res['result']
        if rescode == 0:
            testresult = assert_in(expect, response, responsetype)
            all_cases['id'] = id
            all_cases['name'] = name
            all_cases['url'] = url
            all_cases['method'] = method
            all_cases['expect'] = expect
            all_cases['realdata'] = testresult['realdata']
            if testresult['code'] == 0:
                all_cases['result'] = 'pass'
                pass_cases.append(all_cases)
            elif testresult['code'] == 1:
                all_cases['result'] = 'fail'
                fail_cases.append(all_cases)
            elif testresult['code'] == 2:
                all_cases['result'] = 'error'
                error_cases.append(all_cases)
        else:
            all_cases['id'] = id
            all_cases['name'] = name
            all_cases['url'] = url
            all_cases['method'] = method
            all_cases['expect'] = expect
            all_cases['realdata'] = testresult['realdata']
            all_cases['result'] = 'error'
            error_cases.append(all_cases)
    return pass_cases, fail_cases, error_cases


#casepath = 'init.xlsx'
#pass_cases,fail_cases,error_cases = runcases(casepath)
#print(pass_cases)
#print(fail_cases)
#print(error_cases)