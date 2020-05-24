# -------------------------------------------------------------------------------
# _*_encoding:utf-8_*_
# Name:        $[ActiveDoc-Name]
# Purpose:     
#
# Author:      $[UserName]
#
# Created:     $[DateTime-'DD/MM/YYYY'-DateFormat]
# Copyright:   (c) $[UserName] $[DateTime-'YYYY'-DateFormat]
# Licence:     <your licence>
# -------------------------------------------------------------------------------
# !/usr/bin/env python
# conding=utf-8
from nose.tools import set_trace
# set_trace()
from nose.tools import assert_equal
from nose.tools import assert_in
from common import open_excel_xlsx
import requests
from win32com.client import Dispatch
import win32com.client
class Api001(object):
    def __init__(self):
        print "Api001.__init__"
    def api001(self):
        set_trace()
        # url=1
        # params=2
        respon = requests.get(url=url, params=params)
        respon_code = respon.status_code
        respon_json = respon.json()
        #判断状态码是否相等；判断expect_json是否为respon_json的子集
        # set_trace()
        return expect_code,respon_code,expect_json,respon_json
class Request_api1(object):
    def __init__(self):
        print 'Request_api1:__init__'
    def get_parmas(self,casename):
        #优化：参数获取通过读取excel
        set_trace()
        sht,cols_1 = open_excel_xlsx.open_excel_xlsx()
        case_raw = cols_1.index(casename)
        set_trace()
        case_raw_tuple = sht.Range(sht.Cells(cols_1, 1), sht.Cells(cols_1, 11)).Value
        method = case_raw_tuple[0][1]
        base_url = case_raw_tuple[0][2]
        url = case_raw_tuple[0][2]+case_raw_tuple[0][3]
        params = case_raw_tuple[0][5]
        expect_code = case_raw_tuple[0][6]
        expect_json = case_raw_tuple[0][7]


        # method='get'
        # base_url = "http://httpbin.org/"
        # url = base_url + "get?"
        # params = {"name": "akui", "email": r"a_kui@163.com"}
        # expect_code = 200
        # expect_json = {u'args': {u'email': u'a_kui@163.com', u'name': u'akui'}}
        #优化：方法调用需要封装，get、post等进行封装到子类中
        respon = requests.get(url=url, params=params)

        respon_code = respon.status_code
        respon_json = respon.json()

        #判断状态码是否相等；判断expect_json是否为respon_json的子集
        # set_trace()
        return expect_code,respon_code,expect_json,respon_json
    def get_parma_2(self,casename):
        #扩展：针对此接口输入不同的参数，正常、异常情况
        #优化：参数获取通过读取excel
        #通过casename，获取执行用例的行号，在此行获取相关数据
        set_trace()
        sht,cols_1 = open_excel_xlsx.open_excel_xlsx()
        case_raw = cols_1.index(casename)
        case_raw_tuple = sht.Range(sht.Cells(cols_1, 1), sht.Cells(cols_1, 11)).Value
        method = case_raw_tuple[0][1]
        base_url = case_raw_tuple[0][2]
        url = case_raw_tuple[0][2]+case_raw_tuple[0][3]
        params = case_raw_tuple[0][5]
        expect_code = case_raw_tuple[0][6]
        expect_json = case_raw_tuple[0][7]
        # method='get'
        # base_url = "http://httpbin.org/"
        # url = base_url + "get?"
        # params = {"name": "akui2", "email": r"a_kui2@163.com"}
        # expect_code = 200
        # expect_json = {u'args': {u'email': u'a_kui2@163.com', u'name': u'akui2'}}
        #优化：方法调用需要封装，get、post等进行封装到子类中
        respon = requests.get(url=url, params=params)

        respon_code = respon.status_code
        respon_json = respon.json()

        #判断状态码是否相等；判断expect_json是否为respon_json的子集
        # set_trace()
        return expect_code,respon_code,expect_json,respon_json



