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
import configparser
import os
cur_path = os.path.dirname(os.getcwd())
conf_path = "\\config"
config_path = cur_path+conf_path
os.chdir(config_path)
cf = configparser.ConfigParser()
# 读取文件内容
filename = cf.read("test_env.ini")

# sessions(),得到所有的section，以列表形式返回
sec = cf.sections()
print sec
# options(section) 得到section下的所有option
opt = cf.options("mysql")
print opt
# items 得到section的所有键值对
value = cf.items("base")
print value
# get(section,option) 得到section中的option值，返回string/int类型的结果
set_trace()
mysql_host = cf.get("mysql", "host")


