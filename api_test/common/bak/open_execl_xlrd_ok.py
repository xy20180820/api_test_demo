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
# https://blog.csdn.net/sinat_41774836/article/details/85061007
from pdb import set_trace
import os
# 打开excel，读取表里的数据，返回指定sheet的数据
import xlrd
class Open_excel(object):
    def __init__(self, sheet_name):
        set_trace()
        self.sheet_name = sheet_name
        cc_path = os.getcwd()
        self.data_name = cc_path+"\\data\\data001.xlsx"
        # self.data_name = "D:\\python2.7.13\\mypython\\python-http-api\\2018\\test_api_demo\\test_demo01\\data\\data001.xlsx"
    def open_excel(self):
        # set_trace()
        # 打开execl
        # data_name = "D:\\python2.7.13\\mypython\\python-http-api\\2018\\test_api_demo\\test_demo01\\data\\data001.xlsx"
        # data = xlrd.open_workbook(data_name)
        data = xlrd.open_workbook(self.data_name)
        # 获取指定sheet名的sheet表的内容
        sheet_names = data.sheet_names()
        # table1 = data.sheet_by_name(sheet_name=sheet_names[0])
        table1 = data.sheet_by_name(sheet_name=self.sheet_name)
        rows = table1.nrows
        result = []
        # 列表result保存excel的每一个行数据，每一个行作为result列表的一个元素
        for i in range(1, rows):
            # set_trace()
            print u'第：%d行'%i
            # 获取表的第一行
            col = table1.row_values(i)
            # 获取表的第0行
            col_0 = table1.row_values(0)
            # 将表的第0行和第i行对应为字典
            col_dict = dict(zip(col_0, col))
            # 每一行是列表的一个元素
            result.append(col_dict)
            # set_trace()
            print result[0]['params']
            print result[0]['base_url']
        return result
        # 返回列表，每个元素都是字典
# if __name__ == '__main__':
#     instance1 = Open_excel()
#     list1 = instance1.open_excel()
#     set_trace()
#     print 'ok'
