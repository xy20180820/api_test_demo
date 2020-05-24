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
import os,sys
current_path = os.getcwd()
sys.path.append(current_path)
from nose.plugins.attrib import attr
from nose.tools import assert_equal
from nose.tools import assert_in
from nose.tools import assert_dict_contains_subset
from nose.tools import assert_dict_equal
import requests
import time
import random
import json
set_trace()
# from bs4 import BeautifulSoup
import inspect
# from request.request_api1 import Api001
from ddt_xlrd_ok import Test_api001
# from common import ddt_xlrd_ok
# from common.ddt_xlrd_ok import Test_api001
class Test_api001_case(object):
    @classmethod
    def setUpClass(cls):
        set_trace()
        cls.rr1 = Test_api001()
        print u'setUpClass......'
    @classmethod
    def tearDownClass(cls):
        # set_trace()
        print u'tearDownClass......'
    def setUp(self):
        # set_trace()
        print u'setup...'
    def tearDown(self):
        # set_trace()
        print u'teardown...'

    def test_api001_case(self):
        set_trace()
        # self.rr1，没有test_api001()属性，有'test_api001_1', 'test_api001_2',属性
        expect_code, expect_result, res_code, res_result = self.rr1.test_api001()
        assert_equal(expect_code, res_code, msg=u'请求错误%d' % res_code)
        assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s' % res_result)


# 调试
'''
1、
D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo00>
nosetests -v -a debug testcase\test_case01.py

'''