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
'''
1、调试测试用例
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_d
emo01>nosetests -v -s testcase\nose_test.py:Test_001
执行时，会将nose_test.py中所有类的顶层语句执行：x =1 print。。。会被执行；
同时class Test_002中的y =1 pring。。。也会被执行
2、跑用例：
(venv_http_api_test) D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_d
emo01>
3、生成报告：

'''
from nose.tools import set_trace
set_trace()
class Test_001(object):
    x = 1
    print u'x is %d' %x
    @classmethod
    def setUpClass(cls):
        print u'Test_001类：setUpClass。。。'
    @classmethod
    def TearDownClass(cls):
        print u'Test_001类：TearDownClass。。。'
    def setUp(self):
        print u'Test_001类:setUp。。。'
    def tearDown(self):
        print u'Test_001类:tearDown。。。'
    def test_001(self):
        print u'Test_001类test_001。。。用例'
class Test_002(object):
    y = 2
    print u'y is %d' % y
    @classmethod
    def setUpClass(cls):
        print u'Test_002类：setUpClass---'
    @classmethod
    def TearDownClass(cls):
        print u'Test_002类：TearDownClass---'
    def setUp(self):
        print u'Test_002类:setUp---'
    def tearDown(self):
        print u'Test_002类:tearDown---'
    def test_002(self):
        print u'Test_002类test_002。。。用例'