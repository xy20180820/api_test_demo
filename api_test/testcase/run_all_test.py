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
set_trace()
import ddt
import os
import time
now_time = time.strftime("%Y-%m-%d-%H%M%S")
print now_time
current_path = os.getcwd()
all_path = os.path.dirname(current_path)
result_path = all_path+'\\report\\'+now_time+'result'
report_path = all_path+'\\report\\'+now_time+'report'

#在cmd运行命令
os.system("nosetests -v test_api_case.py --with-allure --logdir=%s" %result_path)
# nosetests -v testcase\test_api_case.py --with-allure --logdir=D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\result001
#生成html报告
os.system("allure generate %s -o %s %(result_path,report_path)")
# allure generate report\result001 -o D:\python2.7.13\mypython\python-http-api\2018\test_api_demo\test_demo01\report\report003
file_list = os.listdir(report_path)
for i in file_list:
    print i

