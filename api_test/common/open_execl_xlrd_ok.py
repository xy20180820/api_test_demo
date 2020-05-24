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
# set_trace()
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# package_path = os.path.dirname(os.getcwd())
# sys.path.append(package_path)
from read_env_config_ok import Read_config
import logging
logger = logging.getLogger(__name__)

# 打开excel，读取表里的数据，返回指定sheet的数据
import xlrd
class Open_excel(object):
    def __init__(self, sheet_name):
        # set_trace()
        self.sheet_name = sheet_name  # 传入sheet表名称
        logger.info(u'开始sheet表：%s' % self.sheet_name)
        # set_trace()
        cc_path = os.getcwd()
        self.data_name = cc_path+"\\data\\data001.xlsx"  # 数据路径
        # self.data_name = "D:\\python2.7.13\\mypython\\python-http-api\\2018\\test_api_demo\\test_demo01\\data\\data001.xlsx"
    def open_excel(self):
        try:
            # set_trace()
            # import sys
            # reload(sys)
            # sys.setdefaultencoding('utf8')
            # set_trace()
            logger.info(u'获取sheet表：%s的数据' % self.sheet_name)
            # set_trace()
            # 打开execl
            # data_name = "D:\\python2.7.13\\mypython\\python-http-api\\2018\\test_api_demo\\test_demo01\\data\\data001.xlsx"
            # data = xlrd.open_workbook(data_name)
            data = xlrd.open_workbook(self.data_name)  # 打开excel
            # 获取所有表的名称
            sheet_names = data.sheet_names()
            # table1 = data.sheet_by_name(sheet_name=sheet_names[0])
            # set_trace()
            table1 = data.sheet_by_name(sheet_name=self.sheet_name)
            rows = table1.nrows  # 获取行数
            result = []
            # 列表result保存excel的每一个行数据，每一个行作为result列表的一个元素
            # set_trace()
            for i in range(1, rows):
                # set_trace()
                # print u'表：%s； 第：%d行' %(self.sheet_name,i)  #此行会报错IOError: [Errno 2] No such file or directory
                # 获取表的第一行
                col = table1.row_values(i)  # 获取第i上的数据
                # 获取表的第0行
                col_0 = table1.row_values(0)  # 获取第一个行的数据，表头
                # 将表的第0行和第i行对应为字典
                col_dict = dict(zip(col_0, col))
                # 每一行是列表的一个元素

                logger.info(u'读取sheet表：%s第%d行的数据' % (self.sheet_name, i))
                # set_trace()

                # set_trace()
                result.append(col_dict)
                get_url = Read_config()
                config_url = get_url.get_base_conf('base_url')  # 从配置文件读取base_url，便于在不同的环境进行测试
                if config_url == 'no opt':  # 如果配置文件有base_url的值，优先使用配置文件中的值；否则使用excel中的值
                    pass
                else:
                    result[-1]['base_url'] = config_url
                # set_trace()
                # 查看最新添加的一行数据
                # print result[-1]['params']
                # print result[-1]['base_url']
                # print result[-1]['headers']
                # print type(result[-1]['headers'])
            # logger.info(u'返回sheet表：%s的数据' % self.sheet_name)
            return result
            # 返回列表，每个元素都是字典
        except:
            logger.error(u"如果存在错误，已记录在日志文件中")
            logger.exception(sys.exc_info())  # 将错误信息记录在日志文件中


# if __name__ == '__main__':
#     instance1 = Open_excel()
#     list1 = instance1.open_excel()
#     set_trace()
#     print 'ok'
