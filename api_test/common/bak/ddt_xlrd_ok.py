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
#https://blog.csdn.net/sinat_41774836/article/details/85061007
import ddt
from nose.tools import set_trace
# set_trace()
from open_execl_xlrd_ok import Open_excel
import requests
import json
from nose.tools import assert_equal
from nose.tools import assert_dict_contains_subset
from nose.tools import assert_dict_equal
@ddt.ddt
class Test_api001(object):
    # def __init__(self):
    # NameError: name 'self' is not defined,此方法存在问题
    #     self.ex = Open_excel('Sheet1')
    #     self.test_data1 = self.ex.open_excel()
    # 获取指定sheet的内容
    ex = Open_excel('Sheet1')
    test_data = ex.open_excel()
    # 将excel的每一行作为列表的一个元素，组成列表test_data1
    # def setUp(self):
    #     print("Start!")
    # def tearDown(self):
    #     print("end!")
    @ddt.data(*test_data)
    def test_api001(self,datas):
        #近一步优化，将request请求进行封装
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url+api_command
        # unicode 转换为str
        # 当params为空的unicode时，使用eval会报错，所以，需要判断一下：
        # 当params为非空时，使用eval(datas['params'])将unicode转换为str
        # 当params为空的nnicode类型时，重新定义params='',此时params为空的str类型；
        params = datas['params']
        if params != '':
            params = eval(datas['params'])
            print 'ok'
        else:
            params = ''
            print 'nothing'
        # set_trace()
        res = requests.get(url=url, params=params)
        res_code = res.status_code
        # 字典
        res_result = res.json()
        expect_code = int(datas['expect_code'])
        # excel中读取的expect_result是unicode格式，使用eval转换dict
        expect_result = eval(datas['expect_result'])
        # 比较状态码和结果

        # return expect_code,expect_result,res_code,res_result

        assert_equal(expect_code, res_code,msg=u'请求错误%d'%res_code)
        assert_dict_contains_subset(expect_result,res_result,msg=u'预期结果错误%s'%res_result)
@ddt.ddt
class Test_api002(object):
    def __init__(self):
        pass
    ex = Open_excel('Sheet2')
    test_data = ex.open_excel()

    @ddt.data(*test_data)
    def test_api002(self,datas):
        # set_trace()
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url+api_command
        # 当params为空的unicode时，使用eval会报错，所以，需要判断一下：
        # 当params为非空时，使用eval(datas['params'])将unicode转换为str

        # 当params为空的nnicode类型时，重新定义params='',此时params为空的str类型；
        params = datas['params']
        if params != '':
            params = eval(datas['params'])
        else:
            params = ''
        # set_trace()
        res = requests.get(url=url, params=params)
        res_code = res.status_code
        res_result = res.json()

        expect_code = int(datas['expect_code'])
        expect_result = eval(datas['expect_result'])
        assert_equal(expect_code, res_code, msg=u'请求错误%d' % res_code)
        assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s' % res_result)

@ddt.ddt
class Test_api003(object):
    def __init__(self):
        pass

    ex = Open_excel('Sheet3')
    test_data = ex.open_excel()

    @ddt.data(*test_data)
    def test_api003(self, datas):
        # set_trace()
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url + api_command
        # 当params为空的unicode时，使用eval会报错，所以，需要判断一下：
        # 当params为非空时，使用eval(datas['params'])将unicode转换为str

        # 当params为空的nnicode类型时，重新定义params='',此时params为空的str类型；
        params = datas['params']
        if params != '':
            params = eval(datas['params'])
        else:
            params = ''
        # set_trace()
        res = requests.get(url=url, params=params)
        res_code = res.status_code
        res_result = res.json()

        expect_code = int(datas['expect_code'])
        expect_result = eval(datas['expect_result'])
        assert_equal(expect_code, res_code, msg=u'请求错误%d' % res_code)
        assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s' % res_result)

@ddt.ddt
class Test_api004(object):
    def __init__(self):
        pass

    ex = Open_excel('Sheet4')
    test_data = ex.open_excel()

    @ddt.data(*test_data)
    def test_api004(self, datas):
        # set_trace()
        base_url = datas['base_url']
        api_command = datas['api_command']
        url = base_url + api_command
        # 当params为空的unicode时，使用eval会报错，所以，需要判断一下：
        # 当params为非空时，使用eval(datas['params'])将unicode转换为str

        # 当params为空的nnicode类型时，重新定义params='',此时params为空的str类型；
        params = datas['params']
        if params != '':
            params = eval(datas['params'])
        else:
            params = ''
        # set_trace()
        res = requests.post(url=url, data=params)
        res_code = res.status_code
        res_result = res.json()

        expect_code = int(datas['expect_code'])
        expect_result = eval(datas['expect_result'])
        assert_equal(expect_code, res_code, msg=u'请求错误%d' % res_code)
        assert_dict_contains_subset(expect_result, res_result, msg=u'预期结果错误%s' % res_result)
#  列表的每一行作为一个参数传给该测试用例，test_ddt1
    # @ddt.data(*test_data1)
    # def test_ddt1_list(self, data):
    #     set_trace()
    #     print data
    #     expect_code = data['expect_code']
    #     expect_result = data['expect_result']
    # @ddt.data(*test_data1) # NameError: name 'self' is not defined



